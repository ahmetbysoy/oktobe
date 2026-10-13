# OPEN QUESTIONS — Açık Sorular

Sessizce uydurulan varsayım yoktur; kapsamı etkileyen her belirsizlik burada sahibini bekler. Kapanan soru, karar kaydına (`DECISIONS.md`) işlenerek buradan "KAPANDI" diye işaretlenir.

## Proje sahibinden beklenenler

| # | Soru | Neden kritik | Bekleyen görev |
|---|---|---|---|
| Q-01 | Referans `index (30).html` dosyası repoya eklenecek mi (veya ajanın erişebileceği bir konuma bırakılacak mı)? Eklenecekse dosya adı aynen korunacak mı? | Brief'in birincil kaynağı; olmadan Aşama 0 envanteri ve parity denetimi yapılamaz, formüller tahmin edilemez | TASK-003, TASK-004 |
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
