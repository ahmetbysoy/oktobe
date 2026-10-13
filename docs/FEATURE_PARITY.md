# FEATURE PARITY — Referans Eşleşme Matrisi

> **Durum uyarısı:** Birincil referans `index (30).html` repoda **yoktur** (`TASK-003`, BLOCKED). Bu matris brief Bölüm 3 ekran envanterinden türetildi; "Referans karşılığı" sütunu dosya gelmeden doğrulanamaz. Hiçbir madde "eşleşiyor" işaretli değildir. Dosya geldiğinde `TASK-004` her satıra kaynak fonksiyon/DOM karşılığını işleyecek; farklar ya düzeltilecek ya da `DECISIONS.md` kaydıyla gerekçelendirilecek.

Kısaltmalar: Durum = `NOT_IMPLEMENTED` (kod yok) · Referans = `BLOCKED` (dosya yok)

| # | Özellik (brief) | Referans karşılığı | Yeni karşılık | Durum | Doğrulama |
|---|---|---|---|---|---|
| 3.1 | Sembol arama/öneri, son fiyat + 24s değişim, WS göstergesi, favori, ayarlar kısayolu, kalıcı seçim | BLOCKED | — | NOT_IMPLEMENTED | TASK-008 |
| 3.2 | Mum grafiği 1m/5m, REST geçmiş + WS canlı mum | BLOCKED | — | NOT_IMPLEMENTED | TASK-008/009 |
| 3.2 | AL/SAT/İZLEMEDE/HAZIRLIK/NÖTR şeridi, puan halkası, gerekçe, veri yaşı, tetikleyiciler | BLOCKED | — | NOT_IMPLEMENTED | TASK-012 |
| 3.2 | CVD/OBI/OI/funding/sweep/iceberg mini paneli | BLOCKED | — | NOT_IMPLEMENTED | TASK-010/012 |
| 3.2 | Likidite ısı haritası, DOM overlay, canlı duvar + etiket + ömür | BLOCKED | — | NOT_IMPLEMENTED | TASK-011/012 |
| 3.2 | Whale/sweep/absorpsiyon işaretçileri; boyutlandırma ve görünür aralık | BLOCKED | — | NOT_IMPLEMENTED | TASK-012 |
| 3.3 | Sinyal ekranı: karar kartı, raw-flow güven skoru, neden listesi, desen performansı | BLOCKED | — | NOT_IMPLEMENTED | TASK-012 |
| 3.3 | Metrikler: CVD 10/30/60s, OBI 5/15/30s, OI değişimi, funding, 60s likidasyon, spread, whale, duvarlar, sweep, iceberg | BLOCKED | — | NOT_IMPLEMENTED | TASK-010/012 |
| 3.3 | Olay akışı ve sinyal geçmişi | BLOCKED | — | NOT_IMPLEMENTED | TASK-012 |
| 3.4 | Ayarlar: arama, presetler, tema; Genel/Risk/Uyarılar/Pattern Pool/Sinyal motoru/Raw Flow/DOM/Canlı duvar/Scalping pusulası/Klasik TA/Görünürlük/Çizgi/Oturum kaydedici kategorileri | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 (her kontrol gerçek davranışa bağlanacak) |
| 3.5 | Pattern Pool: IndexedDB, Wilson alt sınırı, Ret10, MFE/MAE, filtre, detay, backfill, import/export, migration + bozuk dosya davranışı | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 |
| 3.6 | Çoklu sembol tarayıcı: favoriler/Top20/Top50, 1m/5m, AL/SAT filtresi, ilerleme, satırdan terminale geçiş, hız sınırı/iptal/kısmi hata | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 |
| 3.7 | Walk-forward backtest: 300/500/700/1000 mum IS/OOS, OOS metrikleri (win rate, net PnL, PF, max DD, R), look-ahead yasağı, maliyet varsayımları açık | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 |
| 3.8 | Favoriler + son kullanılanlar, kalıcılık | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 |
| 3.9 | Oturum kaydedici: kayıt, süre sınırı, MD/HTML/JSON export, prompt şablonu, hassas veri yasağı | BLOCKED | — | NOT_IMPLEMENTED | TASK-013 |

## Kurallar

- Satır, ancak kodu + testi + taze kanıtı birlikte varken `VERIFIED` olur; piksel eşleşmesi yalnızca referans ekran görüntüsü alınabiliyorsa ölçülür, alınmadan iddia edilmez (brief Bölüm 7).
- Referans davranışı belirsiz çıkan her nokta uydurulmaz; `docs/OPEN_QUESTIONS.md` içine yazılır.
