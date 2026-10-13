#!/usr/bin/env python3
"""Validate the two-agent protocol state in this repository.

Checks (task.md section 4.4 / 11.1):
  - .agent/*.json parse and required baton fields are present/sane
  - .agent/*.jsonl lines are valid single JSON objects with unique evidence ids
  - docs/talk/* files: filename pattern, frontmatter (from/seq/message_id),
    seq uniqueness, consecutive messages from different agents
  - task list: unique ids, builder != reviewer, no overlapping active leases
  - git author of committed talk files matches the frontmatter `from`
    (files not yet committed are reported as UNVERIFIED warnings, not errors)

Exit code 0 = no errors (warnings allowed), 1 = errors found.
Stdlib only. Run from anywhere:  python3 scripts/validate-protocol.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = {"KIBIR", "SOKAK"}
GIT_NAME = {"KIBIR": "Agent KIBIR", "SOKAK": "Agent SOKAK"}
TALK_RE = re.compile(r"^(\d{4})-(KIBIR|SOKAK)-(.+)\.md$")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(rel: str):
    path = ROOT / rel
    if not path.exists():
        err(f"missing file: {rel}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report any parse failure
        err(f"invalid JSON in {rel}: {exc}")
        return None


def check_baton(baton) -> None:
    if not isinstance(baton, dict):
        return
    if baton.get("schema") != 3:
        err("baton.schema must be 3")
    seq = baton.get("seq")
    if not isinstance(seq, int) or seq < 0:
        err("baton.seq must be a non-negative integer")
    if baton.get("holder") not in AGENTS:
        err("baton.holder must be KIBIR or SOKAK")
    peer = baton.get("verified_peer")
    if not isinstance(peer, dict) or set(peer) != AGENTS:
        err("baton.verified_peer must have exactly KIBIR and SOKAK keys")
    elif any(v is not None and not (isinstance(v, str) and re.fullmatch(r"[0-9a-f]{7,40}", v)) for v in peer.values()):
        err("baton.verified_peer values must be null or a commit hash")


def files_overlap(a: str, b: str) -> bool:
    """Crude glob-prefix overlap: 'src/data/**' vs 'src/data/binance/x.ts'."""
    def norm(p: str) -> str:
        return p[:-3] if p.endswith("/**") else p
    na, nb = norm(a), norm(b)
    return na == nb or na.startswith(nb.rstrip("/") + "/") or nb.startswith(na.rstrip("/") + "/")


def check_tasks(data) -> None:
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        err("tasks.json must be an object with a tasks list")
        return
    ids = set()
    active = [t for t in data["tasks"] if t.get("status") in {"IN_PROGRESS", "REVIEW", "IMPLEMENTED"} and (t.get("lease") or {}).get("holder")]
    for task in data["tasks"]:
        tid = task.get("id")
        if tid in ids:
            err(f"duplicate task id: {tid}")
        ids.add(tid)
        if task.get("builder") == task.get("reviewer"):
            err(f"{tid}: builder and reviewer must differ")
        if task.get("builder") not in AGENTS or task.get("reviewer") not in AGENTS:
            err(f"{tid}: builder/reviewer must be KIBIR or SOKAK")
        if not task.get("acceptance_criteria"):
            err(f"{tid}: acceptance_criteria must not be empty")
    for i, left in enumerate(active):
        for right in active[i + 1:]:
            for fa in left.get("files", []):
                for fb in right.get("files", []):
                    if files_overlap(fa, fb):
                        err(f"active lease overlap: {left['id']} ({fa}) vs {right['id']} ({fb})")


def check_jsonl(rel: str, id_field: str) -> None:
    path = ROOT / rel
    if not path.exists():
        err(f"missing file: {rel}")
        return
    seen = set()
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            err(f"{rel}:{lineno}: blank line in JSONL")
            continue
        try:
            rec = json.loads(line)
        except Exception as exc:  # noqa: BLE001
            err(f"{rel}:{lineno}: invalid JSON: {exc}")
            continue
        rid = rec.get(id_field)
        if rid in seen:
            err(f"{rel}:{lineno}: duplicate {id_field} {rid}")
        seen.add(rid)
        if id_field == "evidence_id" and rec.get("result") not in {"PASS", "FAIL", "NOT_RUN"}:
            err(f"{rel}:{lineno}: result must be PASS, FAIL or NOT_RUN")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    out = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def git_author_for(path: Path) -> str | None:
    """Author of the commit that added this file, or None if uncommitted."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%an", "-1", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
    except Exception:  # noqa: BLE001 - git unavailable is a warning, not data corruption
        return None
    name = out.stdout.strip().splitlines()
    return name[0] if name else None


def check_talk() -> None:
    talk_dir = ROOT / "docs" / "talk"
    files = sorted(talk_dir.glob("*.md")) if talk_dir.exists() else []
    if not files:
        warn("docs/talk contains no talk files yet")
        return
    seqs: dict[int, str] = {}
    previous_from = None
    for path in files:
        match = TALK_RE.match(path.name)
        if not match:
            err(f"talk filename does not match NNNN-AGENT-... pattern: {path.name}")
            continue
        file_seq, file_agent = int(match.group(1)), match.group(2)
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("from") != file_agent:
            err(f"{path.name}: frontmatter from={fm.get('from')!r} != filename agent {file_agent}")
        if fm.get("seq") != str(file_seq):
            err(f"{path.name}: frontmatter seq={fm.get('seq')!r} != filename seq {file_seq}")
        if file_seq in seqs:
            err(f"duplicate talk seq {file_seq}: {seqs[file_seq]} and {path.name}")
        seqs[file_seq] = path.name
        if previous_from == file_agent and fm.get("type") not in {"BLOCKED", "HANDOFF"}:
            err(f"{path.name}: same agent wrote two consecutive talk files ({file_agent})")
        previous_from = file_agent
        author = git_author_for(path)
        if author is None:
            warn(f"{path.name}: not committed yet; author/from match UNVERIFIED")
        elif author != GIT_NAME.get(file_agent):
            err(f"{path.name}: IDENTITY VIOLATION commit author {author!r} != {GIT_NAME.get(file_agent)!r}")


def main() -> int:
    baton = load_json(".agent/baton.json")
    check_baton(baton)
    load_json(".agent/state.json")
    load_json(".agent/goal.json")
    check_tasks(load_json(".agent/tasks.json"))
    check_jsonl(".agent/evidence.jsonl", "evidence_id")
    check_jsonl(".agent/attempts.jsonl", "attempt_id")
    check_talk()
    for msg in warnings:
        print(f"WARN  {msg}")
    for msg in errors:
        print(f"ERROR {msg}")
    print(f"validate-protocol: {len(errors)} error(s), {len(warnings)} warning(s)")
    print("RESULT " + ("FAIL" if errors else "PASS"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
