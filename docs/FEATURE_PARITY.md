# FEATURE PARITY — Referans Eşleşme Matrisi

> **Güncelleme (TASK-004, 2026-10-13):** Referans `index (30).html` artık repoda (SHA-256 `17208314…50ea2`). "Referans karşılığı" sütunu `docs/REFERENCE_INVENTORY.md` envanterine dayanarak dolduruldu. Hiçbir madde hâlâ "eşleşiyor" işaretli değildir: yeni uygulama karşılıkları yazılmadan parity iddia edilmez. Farklar ya düzeltilecek ya da `DECISIONS.md` kaydıyla gerekçelendirilecek.

Kısaltmalar: Durum = `NOT_IMPLEMENTED` (yeni kod yok) · Referans = envanter satır karşılığı (REFERENCE_INVENTORY.md)

| # | Özellik (brief) | Referans karşılığı | Yeni karşılık | Durum | Doğrulama |
|---|---|---|---|---|---|
| 3.1 | Sembol arama/öneri, son fiyat + 24s değişim, WS göstergesi, favori, ayarlar kısayolu, kalıcı seçim | `symInput/symDrop` (6328–6345), `load24hrTicker` (5728), `renderWsStatus` (1475), `fs_symbol/fs_favs` | — | NOT_IMPLEMENTED | TASK-008 |
| 3.2 | Mum grafiği 1m/5m, REST geçmiş + WS canlı mum | `loadKlines` (974), `wsConnect/@kline_` (1018), `initChart` (3996), LWC 4.2.0 (satır 7) | — | NOT_IMPLEMENTED | TASK-008/009 |
| 3.2 | AL/SAT/İZLEMEDE/HAZIRLIK/NÖTR şeridi, puan halkası, gerekçe, veri yaşı, tetikleyiciler | `renderDecisionStrip` (3704), `dStrip/dRing`, `runEngine` (3515), `runPreSignal` (4208) | — | NOT_IMPLEMENTED | TASK-012 |
| 3.2 | CVD/OBI/OI/funding/sweep/iceberg mini paneli | `flowMini`, `computeObi` (1232), `flowSnapshot` (3000), `renderFlowMini` (4383) | — | NOT_IMPLEMENTED | TASK-010/012 |
| 3.2 | Likidite ısı haritası, DOM overlay, canlı duvar + etiket + ömür | `drawHeatmap` (2401), `drawDepthOverlay` (2716), `drawLiveWalls` (2568), `wallAges` | — | NOT_IMPLEMENTED | TASK-011/012 |
| 3.2 | Whale/sweep/absorpsiyon işaretçileri; boyutlandırma ve görünür aralık | `detectSweep/Absorption/DeltaBurst` (2290–2325), `addWhaleMarker` (1663), `fs_ranges` | — | NOT_IMPLEMENTED | TASK-012 |
| 3.3 | Sinyal ekranı: karar kartı, raw-flow güven skoru, neden listesi, desen performansı | `renderSignalTab` (4364), `evaluateRawFlow` (3753), `patternRenderSignalContext` (5379) | — | NOT_IMPLEMENTED | TASK-012 |
| 3.3 | Metrikler: CVD 10/30/60s, OBI 5/15/30s, OI değişimi, funding, 60s likidasyon, spread, whale, duvarlar, sweep, iceberg | `sumTrades/sumLiqs/rangeStats` (2968–3000), `raw*Val` id'leri | — | NOT_IMPLEMENTED | TASK-010/012 |
| 3.3 | Olay akışı ve sinyal geçmişi | `addFlowEvent/renderFlowLog` (2331–2374), `engine.log`, `sigLog` | — | NOT_IMPLEMENTED | TASK-012 |
| 3.4 | Ayarlar: arama, presetler, tema; Genel/Risk/Uyarılar/Pattern Pool/Sinyal motoru/Raw Flow/DOM/Canlı duvar/Scalping pusulası/Klasik TA/Görünürlük/Çizgi/Oturum kaydedici kategorileri | `bindSettings` (6093), `PRESETS` (6030), `set*` id'leri (envanter §1/§3) | — | NOT_IMPLEMENTED | TASK-013 (her kontrol gerçek davranışa bağlanacak) |
| 3.5 | Pattern Pool: IndexedDB, Wilson alt sınırı, Ret10, MFE/MAE, filtre, detay, backfill, import/export, migration + bozuk dosya davranışı | `patternPoolInit` (4977, `fs_pattern_pool` v1), `wilsonLower` (5296), `patternBackfill*` (5176), Export/Import (5473/5481); bozuk import davranışı derin incelemede doğrulanacak | — | NOT_IMPLEMENTED | TASK-013 |
| 3.6 | Çoklu sembol tarayıcı: favoriler/Top20/Top50, 1m/5m, AL/SAT filtresi, ilerleme, satırdan terminale geçiş, hız sınırı/iptal/kısmi hata | `symbolScanner.run` (4482), `scan*` id'leri, `aborted` iptali (5518) | — | NOT_IMPLEMENTED | TASK-013 |
| 3.7 | Walk-forward backtest: 300/500/700/1000 mum IS/OOS, OOS metrikleri (win rate, net PnL, PF, max DD, R), look-ahead yasağı, maliyet varsayımları açık | `wfBacktest.run` (4662), `wfWindowSel` HTML'de 300/500/700 (573–577); 1000 ve maliyet modeli derin incelemede (Q-11) | — | NOT_IMPLEMENTED | TASK-013 |
| 3.8 | Favoriler + son kullanılanlar, kalıcılık | `renderFavs` (5696), `fs_favs/fs_recents`, `data-go/data-del` (5703) | — | NOT_IMPLEMENTED | TASK-013 |
| 3.9 | Oturum kaydedici: kayıt, süre sınırı, MD/HTML/JSON export, prompt şablonu, hassas veri yasağı | `sessionRecorder` (5798), `session*` id'leri | — | NOT_IMPLEMENTED | TASK-013 |

## Kurallar

- Satır, ancak kodu + testi + taze kanıtı birlikte varken `VERIFIED` olur; piksel eşleşmesi yalnızca referans ekran görüntüsü alınabiliyorsa ölçülür, alınmadan iddia edilmez (brief Bölüm 7).
- Referans davranışı belirsiz çıkan her nokta uydurulmaz; `docs/OPEN_QUESTIONS.md` içine yazılır.
