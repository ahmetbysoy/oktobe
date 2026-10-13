# TEST STRATEGY — Test Stratejisi

## Değişmez kurallar

- Test edilmemiş kod `VERIFIED`/`PRODUCTION_READY` olamaz. Her "geçti" iddiası, o turda koşulmuş komutun çıktısına ve `.agent/evidence.jsonl` kaydına dayanır (tazelik kuralı, `task.md` 11.2).
- Çalıştırılamayan kontrol `NOT_RUN` + nedenle kaydedilir. Ağ engeli (ör. 451) birim test başarısızlığı gibi gizlenmez; canlı bağlantı testi ayrı raporlanır.
- Reviewer, Builder'ın çıktısına güvenmez: testi kendisi koşar; ayrıca kodu bilerek bozup testin hâlâ geçip geçmediğini dener (kırma testi). Boş test HIGH bulgudur.
- Replay fixture'ları yalnızca test amaçlıdır; canlı veri yerine UI'da sunulmaz. Fixture kaynağı ve zamanı belgelenir.

## Katmanlar

### Şu an çalışan (kurulum turu)

| Katman | Komut | Kapsam | Durum |
|---|---|---|---|
| Protokol doğrulama | `python3 scripts/validate-protocol.py` | baton/tasks şeması, JSON/JSONL geçerliliği, talk frontmatter/ardışıklık, lease çakışması, commit yazarı↔`from` eşleşmesi | Çalışıyor (EV-0008) |
| Birim test | `python3 -m unittest discover -s tests -v` | Doğrulayıcının frontmatter ve çakışma fonksiyonları | Çalışıyor (EV-0008) |

### Ürün koduyla gelecek (TASK-007 sonrası kurulacak)

- **Birim:** gösterge test vektörleri (SMA/EMA/SAR/Bollinger/RSI/MACD/VWAP), CVD/OBI pencereleri, spread, likidasyon toplamı, duvar algılama, depth sequence sync + gap, deduplication/out-of-order, sinyal confirm/veto ve tekrar engelleme, Wilson/Ret10/MFE-MAE ve backtest metrikleri, timestamp/fiyat string hassasiyeti, settings migration ve JSON import/export.
- **Entegrasyon:** REST şema doğrulama + hata sınıflandırma, WS reconnect/yeniden abonelik, IndexedDB repository, sembol/zaman değişimi, tarayıcı/pattern/backtest akışları, bildirim izni olmayan durumlar.
- **Replay:** Gerçek veriden üretilmiş, kaynağı/zamanı yazılı fixture'larla determinizm (aynı girdi → aynı çıktı).
- **Canlı bağlantı (ayrı rapor):** bağlantı kuruldu mu / şema doğru mu / veri taze mi — üç soru ayrı cevaplanır; sandbox'ta REST şu an 451 (FAIL), WS PASS (EV-0003…0005).
- **Görsel/işlevsel kabul:** brief Bölüm 3'teki her madde için test veya doğrulama kanıtı; dar mobil + masaüstü kontrolü. Ekran görüntüsü alınmadan piksel eşleşmesi iddia edilmez.

## CI

`.github/workflows/ci.yml` şu an protokol doğrulama işini koşacak biçimde yazıldı; GitHub'da henüz çalıştırılmadı (D-007). Uygulama işleri (install/lint/typecheck/test/build) `TASK-007`'de gerçek komutlarla eklenecek ve ilk gerçek CI sonucu evidence'a işlenmeden "CI geçiyor" denmeyecek.
