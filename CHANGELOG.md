# CHANGELOG

Biçim: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) esinli. Sürüm etiketi, ancak `docs/RELEASE_PLAN.md` kapıları kanıtla geçildiğinde kullanılır.

## [Unreleased]

### Added (2026-10-13, Kurulum Turu — TASK-001)

- İki ajanlı takım belleği kuruldu: `AGENTS.md`, `docs/` belge seti (audit, mimari taslak, yetenekler, kararlar, görev/test/güvenlik/yayın planları, parity matrisi, açık sorular, durum), `.agent/` durum dosyaları (`baton.json`, `state.json`, `goal.json`, `tasks.json`, `attempts.jsonl`, `evidence.jsonl`).
- Protokol doğrulayıcısı `scripts/validate-protocol.py` ve birim testleri (`tests/test_validate_protocol.py`).
- GitHub şablonları: Issue şablonları, PR şablonu, CODEOWNERS, protokol doğrulama CI workflow'u (GitHub'da henüz çalıştırılmadı).
- İlk konuşma dosyası: `docs/talk/0001-KIBIR-kickoff.md` (SOKAK'a yetenek/inceleme çağrısı).

### Known limitations

- Ürün kodu yok; referans dosya (`index (30).html`) repoda olmadığı için parity denetimi bloklu.
- İkinci ajan doğrulanmadığı için hiçbir görev `VERIFIED` değildir.
