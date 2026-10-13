"""Unit tests for scripts/validate-protocol.py (stdlib unittest, no deps)."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "validate-protocol.py"
spec = importlib.util.spec_from_file_location("validate_protocol", SCRIPT)
vp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vp)


class FrontmatterTests(unittest.TestCase):
    def test_parses_frontmatter(self):
        text = "---\nmessage_id: MSG-0001\nseq: 1\nfrom: KIBIR\n---\n\nbody\n"
        fm = vp.parse_frontmatter(text)
        self.assertEqual(fm["from"], "KIBIR")
        self.assertEqual(fm["seq"], "1")
        self.assertEqual(fm["message_id"], "MSG-0001")

    def test_missing_frontmatter_returns_empty(self):
        self.assertEqual(vp.parse_frontmatter("no frontmatter here"), {})


class OverlapTests(unittest.TestCase):
    def test_glob_prefix_overlaps_child(self):
        self.assertTrue(vp.files_overlap("src/data/**", "src/data/binance/rest-client.ts"))

    def test_sibling_dirs_do_not_overlap(self):
        self.assertFalse(vp.files_overlap("src/data/**", "src/storage/**"))

    def test_exact_match_overlaps(self):
        self.assertTrue(vp.files_overlap(".agent/baton.json", ".agent/baton.json"))


if __name__ == "__main__":
    unittest.main()
