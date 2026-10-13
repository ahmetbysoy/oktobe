# OPEN QUESTIONS — Açık Sorular

Sessizce uydurulan varsayım yoktur; kapsamı etkileyen her belirsizlik burada sahibini bekler. Kapanan soru, karar kaydına (`DECISIONS.md`) işlenerek buradan "KAPANDI" diye işaretlenir.

## Proje sahibinden beklenenler

| # | Soru | Neden kritik | Bekleyen görev |
|---|---|---|---|
| Q-01 | **KAPANDI (2026-10-13):** referans dosya sahibi tarafından repoya eklendi (39d098b); SHA-256 EV-0015'te kayıtlı | — | TASK-003 VERIFIED |
| Q-02 | İkinci ajan (SOKAK) nasıl başlatılacak? Ayrı bir ajan oturumu/araç mı kullanılacak, proje sahibi mi mesaj taşıyacak? | Protokol, tek ajanın iki karakteri oynamasını en ağır ihlal sayar; SOKAK olmadan inceleme ve VERIFIED kapısı kapalıdır | TASK-002, TASK-006 |
| Q-03 | Uygulama hangi ağ/cihazda kullanılacak (örn. Türkiye'den tarayıcı)? Binance REST erişimi (451 durumu) o ağdan biliniyor mu? | Sandbox REST 451 dönüyor; canlı veri davranışının asıl doğrulaması hedef ağda yapılmalı | TASK-008 |
| Q-04 | Deploy hedefi var mı (GitHub Pages, başka statik hosting, yalnızca yerel)? | Build/deploy biçimi ve RELEASE_PLAN buna göre yazılır | TASK-007, TASK-014 |

## İki ajan arasında kapanacaklar (SOKAK gelince)

| # | Soru | Not |
|---|---|---|
| Q-05 | Yığın: TypeScript + Vite + Vanilla TS yeterli mi, React gerekli mi? | TASK-006; ölçülebilir karmaşıklığa göre |
| Q-06 | Grafik kütüphanesi ve sürümü (Lightweight Charts lisans/sürüm doğrulaması dahil) | TASK-006 öncesi kontrol |
| Q-07 | Backtest maliyet modeli: referansta yoksa komisyon/slippage/funding varsayımı ne olacak? | Referans gelmeden cevaplanamaz; karar kaydıyla |
| Q-08 | Baton `holder` yorumunda D-004 çözümü (davet durumu) proje sahibince onaylanıyor mu? | Protokol çelişkisi; nihai yorum sahibinindir |

## Referans dosya gelince açılacaklar

- Belirsiz sinyal/confirm/veto kuralları, duvar/iceberg/sweep eşikleri ve preset varsayılanları — dosya incelenmeden soru olarak bile kesinleştirilemez; `TASK-004` sırasında bu listeye kaynak satır referansıyla eklenecek.

## TASK-004 envanterinden açılanlar (2026-10-13)

| # | Soru | Not |
|---|---|---|
| Q-09 | Lightweight Charts: referans 4.2.0'da mı kalınacak, 5.2.1'e mi geçilecek? | v5 seri API'si farklı; karar TASK-006'da, attribution/NOTICE ile |
| Q-10 | Referansta açık trade/olay dedup katmanı yok; brief dedup ister. Eklenecek dedup sapma olarak kabul ediliyor mu? | DECISIONS kaydı önerilir (TASK-005/010) |
| Q-11 | `wfWindowSel` HTML seçenekleri 300/500/700; brief 1000'i de sayıyor. 1000 dinamik mi ekleniyor, brief mi eksik/hatalı? | `wfBacktest.run` derin incelemesi (TASK-013) |
| Q-12 | Desen havuzu bozuk import davranışının tam karşılığı (kısmi kabul mü, toptan ret mi)? | `patternPoolImport` (5481) derin incelemesi (TASK-013) |
