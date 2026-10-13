# RELEASE PLAN — Yayın Planı

## Durum

Yayın hedefi ve tarihi yoktur; ürün kodu mevcut değildir. Bu belge, bir özelliğin `PRODUCTION_READY` sayılması için gerekli kapıları önceden tanımlar (brief Bölüm 11/14, `task.md` Bölüm 7).

## PRODUCTION_READY kapıları (tamamı kanıtlı olmalı)

1. Temiz checkout'ta kurulum + build + testler gerçekten çalışıyor.
2. `FEATURE_PARITY.md` satırlarının tamamı `VERIFIED` veya gerekçeli karar kaydıyla kapatılmış.
3. Canlı veri davranışı hedef ağ/cihazda doğrulanmış: REST ve WS ayrı ayrı; 451 gibi engeller UI'da açık durum olarak görünüyor; eski veriden sinyal üretilmiyor.
4. Hata yönetimi: bağlantı kopması, yeniden bağlanma (backoff+jitter), depth senkron kaybında yeniden kurulum, şema bozukumunda çökmeden loglama/sayma.
5. Performans: yüksek frekanslı akışta UI kilitlenmesi yok; render birleştirme doğrulanmış.
6. Güvenlik: `SECURITY.md` kontrolleri; secret taraması temiz; import/export kaçış (escape) testleri geçmiş.
7. Mobil + masaüstü kullanılabilirlik kontrolü yapılmış; taşma/tıklanamama bulguları kapalı.
8. Bilinen sınırlar README ve bu belgede yazılı; geri alma (rollback) yolu tanımlı: statik dağıtımda önceki build artefaktına dönüş.

## Yayın biçimi (karar bekliyor)

Brief statik deploy uyumlu yapı ister; hosting hedefi proje sahibince doğrulanacak (Q-04). Backend eklenmez; gerekirse ayrı karar kaydı gerekir.

## Yayın sonrası doğrulama

Dağıtım sonrası canlı ortamda: sayfa açılışı, WS bağlantı göstergesinin gerçekliği, veri yaşı, REST hata gösterimi ve sürüm/artefakt eşleşmesi kontrol edilip evidence'a işlenir. Kontrol yapılmadan "yayında ve çalışıyor" denmez.
