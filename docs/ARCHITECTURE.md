# ARCHITECTURE — Hedef Mimari (Taslak)

> **Durum: UNVERIFIED / TASLAK.** Bu belge KIBIR'ın tek taraflı ön değerlendirmesidir. `task.md` 6.4 gereği nihai mimari, SOKAK'ın bağımsız değerlendirmesiyle karşılaştırılıp `docs/DECISIONS.md` içinde karara bağlanmadan (`TASK-006`) bağlayıcı değildir. Karşı değerlendirme gelene kadar bu belgeye dayanarak ürün kodu yazılmaz.

## 1. İlkeler (brief Bölüm 6'dan, bağlayıcı)

- UI, veri bağlantısı ve hesaplama motoru birbirinden ayrılır.
- WebSocket istemcileri DOM'a doğrudan erişmez; hesaplama modülleri DOM/`window`/ağ bağımlılığı taşımaz.
- State güncellemeleri tek açık akıştan geçer; başlatma/durdurma idempotenttir.
- Her modül: tek sorumluluk, açık giriş/çıkış sözleşmesi, test.
- Hesaplamalar saf fonksiyonlar + deterministik girdilerle replay edilebilir olmalı.

## 2. Aday yığın (karar bekliyor)

| Katman | Aday | Durum |
|---|---|---|
| Dil | TypeScript (strict) | Brief önerisi; TASK-006 kararı gerekli |
| Build | Vite | Brief önerisi; TASK-006 kararı gerekli |
| UI | Vanilla TS (hafif) — React yalnızca karmaşıklık gerçekten gerektirirse | Brief önerisi; TASK-006 kararı gerekli |
| Grafik | Lightweight Charts (sürüm + lisans doğrulanıp sabitlenecek) | Doğrulanmadı; TASK-006 öncesi kontrol edilecek |
| Depolama | IndexedDB üzerinde ince repository katmanı | Şema/migration testleri TASK-013 |
| Test | Vitest (aday) + replay fixture'ları | TASK-007'de kurulacak |
| Kalite | ESLint + formatter + TypeScript strict | TASK-007'de kurulacak |

Alternatifler (tek dosyalık HTML'i sürdürmek, React'a doğrudan geçmek) `TASK-006`'da artı/eksiyle karşılaştırılacak; popülerlik gerekçe sayılmaz.

## 3. Modül sınırları (brief Bölüm 6 ağacı esas alınır)

`src/app` (bootstrap, router, app-state) · `src/core` (config, clock, logger, errors, event-bus, numeric) · `src/data/binance` (rest-client, symbol/kline servisi, market-ws, depth-ws, schemas, rate-limiter, reconnect-policy) · `src/data/normalize` (trade/depth normalizer, deduplicator, sequence-sync) · `src/domain/market` + `src/domain/analytics` (MA/SAR/Bollinger/RSI/MACD/VWAP/CVD/OBI/flow-events/wall-detector/signal-engine/compass) · `src/domain/patterns` · `src/domain/backtest` · `src/storage` (settings/favorites/pattern/session repository + migrations) · `src/features/*` (chart, signal, scanner, pattern-pool, backtest, favorites, settings, session-recorder) · `src/ui` · `src/workers`.

İhtiyaç duyulmayan modül, gerekçeli kararla sadeleştirilebilir; tek dev `app.ts`/`utils.ts` ve döngüsel bağımlılık kabul edilmez.

## 4. Veri akışı ve sözleşmeler (resmi doğrulamaya tabi)

- **REST:** `https://fapi.binance.com` — sembol listesi/ticker, kline geçmişi, depth snapshot, OI, mark/funding. Her yanıt şema doğrulamasından geçer; hatalar sınıflandırılır (451/403/429/5xx ayrı ele alınır, gizlenmez).
- **WS yönlendirme:** `/market` (aggTrade, kline, markPrice vb.) ve `/public` (depth vb.) ayrı bağlantılar; her stream'in ucu kod yazımında resmi sayfasından doğrulanır (`TASK-005`). Legacy `wss://fstream.binance.com/ws/...` biçimi kullanılmaz (2026-04-23 sonrası geçersiz).
- **Depth senkronu (resmi akış):** WS olayları buffer'lanır → REST snapshot alınır → `u < lastUpdateId` olayları düşürülür → ilk olay snapshot'ı kapsar → sonraki her olayda `pu == önceki u` doğrulanır; koparsa kitap geçersiz sayılıp süreç baştan kurulur.
- **Bütünlük:** trade/olay deduplication (zaman + kimlik), ms/sn dönüşümleri tek yerden, yüksek frekanslı olaylarda micro-batch/buffer, veri yaşı göstergesi + eski veriden sinyal üretmeme kuralı.
- **Bağlantı sağlığı:** exponential backoff + jitter, yeniden abonelik, bağlantı durumu UI'da her zaman gerçek (kopukken yeşil gösterilmez).

## 5. Sinyal motoru sınırları

Teknik göstergeler ile raw-flow confirm/veto kuralları ayrı modüllerdedir. Skor bileşenleri açıklanabilir olmalı; yetersiz/ eski veride veya kitap senkron dışıyken güven düşürülür ya da sinyal geçersiz sayılır. AL/SAT çıktısı yatırım tavsiyesi diliyle sunulmaz.

## 6. Açık mimari sorular

Deploy hedefi (statik hosting varsayımı doğrulanacak), grafik kütüphanesi lisansı, worker kullanımı gerekliliği, backtest maliyet modeli (brief: referansta yoksa karar kaydıyla) — tamamı `docs/OPEN_QUESTIONS.md` ve `TASK-006` kapsamındadır.
