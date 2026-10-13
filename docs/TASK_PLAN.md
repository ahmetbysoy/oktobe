# TASK PLAN — Görev Planı

Kanonik görev kaydı `.agent/tasks.json` dosyasıdır; bu belge aşama görünümüdür. Durum modeli `task.md` Bölüm 7'nindir (brief Bölüm 14'teki PLANNED/WORKING etiketleri burada sırasıyla BACKLOG/IN_PROGRESS karşılıklarıyla okunur; tek model kullanılır, bkz. D-002/D-003 tek-kaynak ilkesi).

## Aşamalar (task.md 6.6 ↔ brief Bölüm 10)

| Aşama | İçerik | Görevler | Çıkış kapısı |
|---|---|---|---|
| 0. Gereksinim ve denetim | Repo auditi, referans envanter | TASK-001 (kurulum), TASK-003 (dosya), TASK-004 (envanter) | FEATURE_PARITY referans sütunu dolu |
| 1. Yetenek doğrulama + iletişim | İki ajan yetenek raporu, baton fiilen devir | TASK-002 | `verified_peer` iki yönde dolu |
| 2. Mimari ve standartlar | Bağımsız değerlendirmeler, karşılaştırmalı karar | TASK-005, TASK-006 | DECISIONS'da kilitli yığın + sözleşme |
| 3. İş paketleri + test planı | İskelet, CI, test altyapısı | TASK-007 | build/lint/typecheck/test yerelde ve CI'da gerçek |
| 4. Kontrollü modül geliştirme | Brief sırasıyla dikey dilimler | TASK-008 … TASK-013 (012/013 alt görevlere bölünerek) | Her dilim: kod + test + kanıt + karşı inceleme |
| 5. Entegrasyon, regresyon, güvenlik | Uçtan uca akışlar, hata durumları | TASK-014 (ilk yarı) | Regresyon + güvenlik kontrol listesi kanıtlı |
| 6. Kullanıcı kabulü + yayın hazırlığı | Parity denetimi, release kriterleri | TASK-014 | RELEASE_PLAN kapıları geçti |
| 7. Yayın sonrası doğrulama | Canlı ortamda veri tazeliği/bağlantı kontrolü | TASK-014 sonrası açılacak | Hedef ağdan canlı kanıt |

## Bağımlılık zinciri (özet)

```text
TASK-001 (kurulum, IMPLEMENTED - inceleme bekliyor)
  └─ TASK-002 (SOKAK yanıtı) ── TASK-006 (mimari karar) ── TASK-007 (iskelet)
  └─ TASK-003 (referans dosya, BLOCKED: sahip) ── TASK-004 (envanter) ──┐
TASK-005 (sözleşme doğrulama, ön bulgu hazır) ──────────────────────────┴─ TASK-008..013 (dilimler) ── TASK-014 (parity/yayın)
```

## Kurallar

- Görevler küçük ve doğrulanabilir tutulur; `TASK-012/013` tek seferde alınmaz, uygulama öncesi alt görevlere bölünür.
- Bağımlılık çözülmeden entegrasyona geçilmez; kapsamı etkileyen karar proje sahibi adına uydurulmaz (`OPEN_QUESTIONS`).
- Her görevde: kabul kriterleri + test komutları + beklenen kanıtlar görev kaydında yazılıdır; durum değişimi kanıtsız yapılmaz.
- Lease çakışması olan görev alınmaz (aktif lease dosyaları kesişemez; `validate-protocol.py` denetler).
