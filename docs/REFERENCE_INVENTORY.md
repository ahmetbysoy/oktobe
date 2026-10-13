# REFERENCE INVENTORY — `index (30).html` Envanteri (TASK-004)

- **Dosya kimliği:** repo kökü `index (30).html` · 6.370 satır · 303.780 bayt · SHA-256 `172083141623593f1d6c958a7f6d64453430dd20b9f1db72c8043e3e23850ea2` (EV-0015)
- **Yöntem:** Dosyanın tamamı üzerinde otomatik çıkarma (fonksiyon tanımları, DOM id'leri, olay bağları, ağ çağrıları, depolama, zamanlayıcılar) + kritik bölümlerin satır satır okunması. Satır numaraları bu SHA'ya aittir; dosya değişirse envanter yenilenir. Çıkarma komutları ve ham çıktılar bu turun kanıtıdır (EV-0019).
- **Başlık:** `Futures Scanner — Stage 4`. Tek harici bağımlılık: Lightweight Charts **4.2.0** CDN (`unpkg`, satır 7). Ana script: satır 618–6368 (`"use strict"`), 183 fonksiyon tanımı, 207 benzersiz DOM id'si.

## 1. Ekran envanteri (7 görünüm)

| Görünüm | DOM | Giriş | Ana bileşenler (id) |
|---|---|---|---|
| Grafik/terminal | `view-chart` | nav `data-view=chart`, varsayılan | `chart`, `chartWrap`, `heatmap-canvas`, `orderbook-overlay`, `dStrip` (karar şeridi), `flowMini`, `tfBar`, `sync-badge` |
| Sinyal | `view-signal` | nav `data-view=signal` | `dRing/dScore`, `sigStatus/sigRule/sigScore/sigConf`, `sigReasons`, `scoreFill`, ham metrikler `rawCvdVal…rawWallsVal`, `flowLog`, `sigLog`, `patternHist` |
| Tarayıcı | `view-scanner` | nav `data-view=scanner` | `scanListSel/scanTfSel/scanFilterSel`, `scanRunBtn`, `scanProgress`, `scanResultCount`, `scanResultsBody`, satır tıklaması → `switchSymbol + showView('chart')` (satır 5703 `data-go`) |
| Desen havuzu | `view-pool` | nav `data-view=pool` | `poolRows`, `poolTfFilter`, `poolMinFilter`, `poolRefresh/Export/ImportBtn`, `poolDetail`, `poolOverlayBtn`, `poolDbStatus` |
| Backtest | `view-backtest` | nav `data-view=backtest` | `wfSymSel/wfTfSel/wfWindowSel`, `wfRunBtn`, `wfWinRate/wfNetPnl/wfPF/wfMDD/wfAvgR`, `wfWindowRows`, `wfTradeRows` |
| Favoriler | `view-favs` | nav `data-view=favs` | `favList`, `recentList`, `data-go/data-del` |
| Ayarlar | `view-settings` | `settingsBtn`, grafik üstü inline `showView('settings')` | `setSearch`, `presetRow` (scalper/analist/sade), `set*` kontrolleri (aşağıda), `sessionRecCard` |

Navigasyon: `#nav button` → `showView(b.dataset.view)` (satır 6328). Ayarlar nav listesinde yok; ayrı butondan açılır.

## 2. Fonksiyon envanteri → yeni modül eşleştirmesi

| Alan (referans satırları) | Temsilci fonksiyonlar | Yeni modül (ARCHITECTURE) | Test karşılığı |
|---|---|---|---|
| State/config (618–915) | `S`, `engine`, `alertManager`, `dailyLoss` (819), `flow` (896) | `app/app-state`, `core/config` | Settings migration/varsayılan testleri |
| REST veri (947–1009, 3447, 4533, 5728) | `loadSymbols`, `fetchKlines/loadKlines`, `loadOpenInterest`, `load24hrTicker` | `data/binance/rest-client`, `symbol/kline-service` | Şema doğrulama, hata sınıflandırma |
| Kline WS (1014–1046, 1502) | `wsConnect`, `scheduleKlineReconnect` (backoff: `min(30s, 2^retry)`), `onKline` | `data/binance/market-ws`, `reconnect-policy` | Reconnect/yeniden abonelik |
| Raw akışlar (1041–1112, 1615–…) | `connectMarketRaw` (aggTrade+markPrice@1s+forceOrder), `connectPublicRaw` (depth), `onAggTrade`, `onMarkPrice`, `onForceOrder` | `data/binance/market-ws/depth-ws` | Stream yönlendirme, dedup |
| Depth senkron (1118–1232) | `fetchDepthSnapshot` (snapshot + buffer, `U/u` boşlukta yeniden snapshot), `applyDepthUpdate`, `recomputeBest`, `computeObi` | `data/normalize/sequence-sync`, `domain/market/orderbook` | Gap/snapshot sonrası update testleri |
| Duvar/olay algılama (1299–1465, 2290–2331) | `detectWalls`, `detectSweep/Absorption/DeltaBurst`, spoof izleri (`wallAges`, `SPOOF_MAX_AGE=8000`) | `domain/analytics/wall-detector`, `flow-events` | Duvar ömrü/spoof senaryoları |
| Overlay/çizim (2374–2914) | `drawHeatmap`, `drawCompass`, `drawLiveWalls`, `drawDepthOverlay`, `renderOverlayFrame` (rAF) | `features/chart` overlay katmanı | Boyutlandırma/render birleştirme |
| Göstergeler (3024–3127) | `sma`, `psar`, `bollinger`, `emaSeries`, `rsiSeriesCalc`, `macdCalc`, `vwapCalc` | `domain/analytics/*` (saf) | Sabit test vektörleri |
| Karar motoru (3515–3967, 4208–4364) | `runEngine` (MA cross + SAR flip + HTF bias veto), `fireSignal`, `evaluateRawFlow`, `renderDecisionStrip/Raw`, pre-signal (`runPreSignal`) | `domain/analytics/signal-engine` | Confirm/veto, pre-signal, tekrar engelleme |
| Desen havuzu (4939–5654) | `patternPoolInit` (IndexedDB), `patternBackfill*`, `patternRecomputeStats`, `wilsonLower` (5296), `patternPoolExport/Import`, grafik overlay | `domain/patterns/*`, `storage/pattern-repository` | Wilson/Ret10/MFE-MAE, migration, bozuk import |
| Tarayıcı (4478–4658) | `symbolScanner.run(listMode, tf, filterDir)`; iptal `aborted` bayrağı | `features/scanner` | Hız sınırı/iptal/kısmi hata |
| Walk-forward (4658–4945) | `wfBacktest.run(symbol, tf, totalBars)`; pencereler 300 (150/150), 500 (350/150), 700 (500/200) — `wfWindowSel` | `domain/backtest/*` | IS/OOS ayrımı, metrikler, look-ahead |
| Oturum kaydedici (5798–6030, 6301) | `sessionRecorder` (start/stop/download; MD/HTML/JSON, süre sınırı, prompt şablonu) | `features/session-recorder`, `storage/session-repository` | Export escape, süre sınırı |
| UI/ayarlar (5654–6368) | `switchSymbol`, `renderFavs`, `showView`, `applyTheme`, `applyPreset` (6030: scalper/analist/sade), `bindSettings/bindUI/bindLineCtrls` | `features/*`, `ui/*`, `storage/settings-repository` | Her kontrol → davranış bağı |

Kalıp notu: Olay bağlarının çoğu `addEventListener` (6) ile değil, 44 adet `.onclick/.onchange/.oninput` atamasıyla kurulur; yeni mimaride tekil yetkilendirme (delegation) veya bileşen bağları kullanılacak, davranış envanteri değişmeyecek.

## 3. Durum (state) envanteri

- `S` (628): `symbol/interval` (localStorage'dan), `candles` (zaman **saniye**), `symbols`, `settings` (varsayılanlar + `fs_settings` merge), `favs/recents`, kline WS durumu (`wsRetry/wsAlive/wsLastMsg`), `tickSize/pricePrecision`, `raw` (market/public WS + OI zamanlayıcıları), `htf.candles5m`.
- `flow` (896): trades/liqs tamponları, `cvd/obi/bidVol/askVol`, `oi/funding/markPrice`, `bestBid/bestAsk/spread`, `bidsBook/asksBook` (Map), `wallAges`, `depthSynced/depthBuffer/depthGen`, ısı haritası kareleri.
- `engine`: `pending/pendingMulti`, `status/statusText`, `log`, `markers`, `preSignal` (sinyal olmayan ön uyarı).
- `PPOOL` (4942): `PPOOL_DB_NAME="fs_pattern_pool"`, sürüm 1; store'lar `events` (indeksler: patternKey, coinPatternKey, coin, timeframe, timestamp, status, eventKey), `poolStats`, `metadata`.
- Ayar varsayılanları (636–656): MA 9/21/50, SAR 0.02/0.2, pencere 3; `liqMin=50000`, `oiPollSec=15`, `cascadePct=0.8`, `whaleMin=300000`, `wallPct=90`, merdiven sağ/48px, canlı duvar 5 adet/%0.5; BB 20/2, RSI 14, MACD 12/26/9; günlük kayıp kapalı/200 USDT; ses açık %60. Tam liste referans satır 636–656'da; yeni `settings-repository` bu varsayılanlarla birebir başlayacak ve migration testine girecek.

## 4. Ağ envanteri

| Çağrı | Satır | Uç | Not |
|---|---|---|---|
| `GET /fapi/v1/exchangeInfo` | 949 | REST | Sembol listesi + `tickSize/pricePrecision` kaynağı |
| `GET /fapi/v1/klines` | 967, 3447 (5m/200 HTF) | REST | Grafik geçmişi + HTF bias |
| `GET /fapi/v1/openInterest`, `premiumIndex` | 981, 993 | REST | OI polling varsayılan 15 sn |
| `GET /fapi/v1/depth?limit=1000` | 1119 | REST | Snapshot; hata `HTTP <status>` olarak fırlatılır |
| `GET /fapi/v1/ticker/24hr` | 4533, 5730 | REST | Tarayıcı havuzu + başlık fiyatı |
| WS kline | 1018 | `/market/ws/<sym>@kline_<interval>` | Tek stream; reconnect'te mumlar REST'ten tazelenir |
| WS raw market | 1066 | `/market/stream?streams=aggTrade/markPrice@1s/forceOrder` | Birleşik abonelik |
| WS depth | 1087 | `/public/ws/<sym>@depth@100ms` | Snapshot senkronu satır 1118 akışıyla (resmi akışla uyumlu: buffer → snapshot → `U/u` zinciri, boşlukta baştan) |

Referansın kendi yorumu (satır 621–625) routed uçları "Nisan 2026 migration" olarak işaretliyor; bu, TASK-005 ön doğrulamasıyla uyumlu. Dedup: referansta trade/olay düzeyinde açık bir dedup katmanı bulunamadı — yeni mimaride brief gereği eklenecek ve fark DECISIONS'a yazılacak.

## 5. Depolama ve zamanlayıcılar

- **localStorage:** `fs_symbol`, `fs_interval`, `fs_settings`, `fs_favs`, `fs_recents`, `fs_ranges` (görünür aralık), `fs_dloss_entries/fs_dloss_day` (günlük kayıp), `fs_cal_<SYMBOL>` (24 saatten eskiyse atlanan whale kalibrasyon medyanı, satır 1331). Yeni tasarımda bu anahtarlar migration ile karşılanacak.
- **IndexedDB:** yalnızca desen havuzu (yukarıda).
- **Zamanlayıcılar:** OI polling (1007), kline/raw/depth reconnect `setTimeout` zincirleri, başlık ve akış render aralıkları (1486/1493), overlay için `requestAnimationFrame` (2911–2966, 4177). Sonsuz döngü koruması reconnect üst sınırlarında incelenecek (TASK-009).

## 6. Sürüm notu (TASK-006 girdisi)

Referans, Lightweight Charts **4.2.0**'ı CDN'den sabitliyor (satır 7). Güncel kararlı sürüm **5.2.1** (Apache-2.0) bağımsız doğrulandı (EV-0020). v5'te seri API'si değiştiğinden "referansla birebir" ile "güncel sürüm" arasında bilinçli karar gerekir: ya 4.2.0'da kalınıp parity korunur ya 5.2.1'e geçilip API farkı uyarlanır. İki durumda da sürüm sabitlenecek, attribution/NOTICE yüklülüğü karara yazılacaktır. Bu karar TASK-006'nındır; envanter yalnızca gerçeği kaydeder.
