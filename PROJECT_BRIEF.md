# PROJECT BRIEF — Futures Scanner / Order-Flow Terminal
## Sıfırdan yeniden geliştirme, birebir özellik eşleştirme ve doğrulanabilir kalite planı

> **Ana talimat:** Bu belgeyle birlikte verilen `index (30).html` dosyası mevcut ürünün referans uygulamasıdır. Amaç yalnızca benzer görünen bir ekran üretmek değil; referansın kullanıcı arayüzünü, etkileşimlerini, veri akışını, hesaplama davranışlarını ve bütün görünür özelliklerini inceleyip sıfırdan, modüler, test edilebilir ve sürdürülebilir bir uygulama olarak yeniden kodlamaktır.

## 1. Proje amacı

Binance USDⓈ-M Futures piyasa verilerini gerçek zamanlı kullanan, mobil öncelikli bir **Futures Scanner ve Order-Flow Terminal** geliştir.

Uygulama; fiyat grafiği, teknik göstergeler, ham order-flow metrikleri, order book/DOM, likidite duvarları, likidasyonlar, AL/SAT/İZLEMEDE sinyal kararı, çoklu sembol tarayıcı, desen istatistik havuzu, walk-forward backtest, favoriler ve kapsamlı ayarlar sunar.

Bu proje bir maket veya statik arayüz çalışması değildir. Arayüzde görünen her kontrolün gerçek davranışı olmalı; gerçek veri isteyen her bölüm gerçek veriyle çalışmalı; hesaplama iddiaları test ve kanıtla doğrulanmalıdır.

## 2. Kaynak ve doğruluk ilkesi

### Kaynak önceliği
1. `index (30).html`: mevcut arayüz, etkileşim, varsayılanlar ve ürün davranışı için birincil referans.
2. Bu `PROJECT_BRIEF.md`: yeniden geliştirme hedefleri, kalite koşulları ve teslim ölçütleri.
3. Binance'in güncel resmî dokümantasyonu: endpoint, WebSocket stream, hız limiti ve veri şemalarının doğrulanması için.
4. Açıkça belgelenmiş mimari kararlar ve test sonuçları.

Referans dosya yaklaşık 6.300 satırlık, HTML/CSS/JavaScript ağırlıklı tek dosyalı bir uygulamadır. Uygulamayı yalnızca dosyanın ilk ekranına bakarak yeniden yazma. Tüm JavaScript fonksiyonlarını, olay bağlarını, durum alanlarını, veri kaynaklarını, zamanlayıcıları, saklama katmanını ve ekranlar arası bağımlılıkları analiz et.

### Kanıt kuralları
- Mock/sahte piyasa verisi, rastgele fiyat, uydurma order book, sentetik likidasyon veya demo sinyal **yasaktır**.
- Bağlantı başarısızsa gerçek veriyi varmış gibi gösterme. Durumu `BAĞLANTI YOK`, `VERİ ESKİ`, `ISINIYOR` gibi açık bir durumla belirt.
- API/WebSocket hatalarını gizleme veya gerçek veri yerine sabit değerle doldurma.
- Çalıştırılmayan test için “başarılı” deme. Test komutu ve çıktısı/kanıtı kaydedilmeli.
- Hesaplama formüllerini tahmin edip mevcut davranışla aynıymış gibi sunma. Önce kaynak davranışını çıkar, sonra doğrula.
- Teknik göstergeler ile özel order-flow sinyallerini ayrı modüllerde tut.
- Hiçbir gerçek para işlemi, emir gönderimi veya hesap API anahtarı gerekmiyor. Kapsam piyasa verisi ve analizdir; kullanıcı açıkça ayrıca istemedikçe emir yürütme eklenmeyecek.
- Binance endpoint ve stream adreslerini kodlamadan önce resmî dokümantasyondan doğrula. Referansta görünen adreslerin güncel ve geçerli olduğunu varsayma.
- HTTP 451, bölgesel kısıtlama, CORS, DNS veya WebSocket bağlantı hatalarını uygulama içinden “aşılmış” gibi gösterme. Yalnızca yasal ve belgelenmiş bağlantı seçeneklerini dene; başarısızlık durumunu ve sebebini raporla.

## 3. Ürün kapsamı ve ekran envanteri

Aşağıdaki ekranlar ve özellikler referans uygulamadan çıkarılarak yeniden uygulanmalıdır.

### 3.1 Global üst başlık
- Seçili sembol arama/girişi ve sembol öneri listesi.
- Son fiyat ve 24 saatlik yüzde değişim.
- WebSocket bağlantı göstergesi.
- Favoriye ekleme/çıkarma.
- Ayarlar ekranına hızlı erişim.
- Seçili sembol, zaman aralığı ve uygun görünür grafik aralığının kalıcı saklanması.

### 3.2 Grafik / ana terminal
- Mum grafiği ve `1m` / `5m` zaman aralığı seçimi.
- Seçili sembol için geçmiş mumların REST üzerinden yüklenmesi, yeni mumların WebSocket ile güncellenmesi.
- AL / SAT / İZLEMEDE / HAZIRLIK / NÖTR karar şeridi.
- Karar puanı halkası, kısa gerekçe, veri yaşı/sağlık durumu ve tetikleyici etiketleri.
- CVD, OBI, OI, funding, sweep ve iceberg için mini panel.
- Likidite ısı haritası canvas katmanı.
- Order-book/DOM overlay katmanı.
- Canlı likidite duvarı, duvar etiketi, duvar ömrü ve fiyata yaklaşma görselleştirmesi.
- Whale/sweep/absorpsiyon gibi olay işaretçileri.
- Grafik yeniden boyutlandırma, görünür aralığı koruma ve sembol/zaman dilimi değişiminde tutarlı güncelleme.

### 3.3 Sinyal ekranı
- Karar kartı ve sinyalin tetikleyici açıklaması.
- Raw-flow güven skoru ve skor çubuğu.
- Sinyali oluşturan/engelleyen nedenlerin listesi.
- Tarihsel desen performansı özeti.
- **Metrikler** alt ekranı:
  - CVD (10s / 30s / 60s)
  - OBI (5s / 15s / 30s)
  - Open Interest değişimi
  - Funding
  - Son 60 saniyelik likidasyon
  - Spread
  - Whale modu
  - Alış/satış duvarları
  - DOM sweep
  - Iceberg
- **Olay akışı**: zaman damgalı order-flow olayları.
- **Sinyal geçmişi**: oluşturulan sinyaller ve nedenleri.

### 3.4 Ayarlar ekranı
Ayar araması, Scalper / Analist / Sade preset'leri, akordeon/kart davranışı ve tema yönetimi.

Kategoriler ve referansta bulunan ayarlar:
- Genel: koyu/açık tema, bağlantı durumu, manuel yeniden bağlanma.
- Risk takibi: günlük kayıp limiti aç/kapat, USDT limit değeri, günlük toplam ve sıfırlama.
- Uyarılar: ses, ses seviyesi, AL/SAT test sesi, tarayıcı bildirimi, bildirim izni, mobil titreşim; sinyal, yüksek flow ve günlük limit uyarıları.
- Pattern Pool: başarı eşiği, zayıf desen susturma seçeneğinin durumu, JSON dışa/içe aktarma.
- Sinyal motoru: hızlı/orta/yavaş MA, Parabolic SAR step/max, mum penceresi.
- Raw Flow: raw-flow onayı, mini panel, likidasyon işaretçisi, minimum likidasyon büyüklüğü, OI sorgulama aralığı, cascade eşiği.
- DOM/likidite: ladder görünürlüğü ve konumu, genişliği, duvar ışını uzunluğu/opaklığı/etiketleri, yalnızca belirli süre yaşayan duvarlar, ısı haritası, whale/sweep/spoof algılama, whale eşiği ve duvar yüzdelik eşiği.
- Canlı duvar takibi: duvar adedi, fiyat uzaklığı, pulse/flash, etiket görünürlüğü.
- Scalping pusulası: görünürlük, decay yarı ömrü, iceberg ve duvar tick mesafeleri.
- Klasik teknik analiz: Bollinger Bands, RSI, MACD ve VWAP seçenekleri/periyotları.
- Görünürlük: MA, SAR ve hacim paneli.
- Çizgi görünümü: gösterge renkleri, çizgi kalınlıkları ve varsayılana dönme.
- Oturum kaydedici: başlat/durdur/indir, MD/HTML/JSON formatı, maksimum kayıt süresi ve prompt şablonu seçeneği.

Tüm ayar kontrolleri gerçekten ilgili davranışı değiştirmeli. Bir kontrol henüz uygulanmadıysa ekranda çalışıyormuş gibi bırakma; uygulama kapsamından çıkarma kararı belgelenmeli veya gerçek işlevi tamamlanmalıdır.

### 3.5 Pattern Pool / desen havuzu
- IndexedDB tabanlı yerel veri saklama davranışını incele ve sağlam bir repository katmanıyla yeniden uygula.
- Desen adı, zaman dilimi, örnek sayısı, Wilson alt güven sınırı, Ret10, MFE/MAE ve durum sütunları.
- Zaman dilimi ve minimum örnek filtresi.
- Desen detay görünümü ve örnek/istatistik tablosu.
- Sembol ve mum geçmişi üzerinden backfill.
- Açık desen olaylarını güncelleme ve sonuçlarını tamamlama.
- İstatistikleri yeniden hesaplama, havuzu yenileme, JSON dışa/içe aktarma.
- Grafikte desen/olay overlay'leri varsa referanstaki davranışla eşleştir.
- Veri şeması, indeksler, migration ve bozuk içe aktarma dosyası davranışı test edilmeli.

### 3.6 Çoklu sembol tarayıcı
- Favoriler, Top 20 hacim, Top 50 hacim sembol havuzları.
- `1m` / `5m` zaman dilimi.
- Tümü / yalnız AL / yalnız SAT filtresi.
- Tarama ilerleme durumu ve sonuç adedi.
- Sembol, sinyal, kural açıklaması ve puan gösterimi.
- Sonuç satırına basınca ana terminali ilgili sembole yönlendirme.
- İstekler arasında hız sınırı, iptal ve kısmi hata yönetimi.

### 3.7 Walk-forward backtest
- Sembol ve zaman dilimi seçimi.
- Referansta bulunan IS/OOS pencere seçenekleri: 300, 500, 700, 1000 mumluk toplam pencereler.
- IS (in-sample) ve OOS (out-of-sample) verilerini birbirinden ayırma.
- OOS performans özeti: işlem sayısı, win rate, net PnL, profit factor, max drawdown, ortalama R-multiple.
- Pencere detayları, OOS işlem listesi ve açıklama/ilerleme log'u.
- Look-ahead bias olmamalı. OOS sonuçları parametre ayarlamak için kullanılmış gibi davranılmamalı.
- Komisyon, slippage ve varsa fonlama maliyeti varsayımları açıkça tanımlanmalı. Referansta mevcut olmayan bir maliyet modeli eklenirse karar kaydıyla belgelenmeli.
- Backtest sonuçları canlı performans veya kârlılık garantisi olarak sunulamaz.

### 3.8 Favoriler ve son kullanılanlar
- Favori sembolleri listeleme, seçme ve silme.
- Son kullanılan semboller.
- Favorilerden tarayıcı ve grafik ekranına geçiş.
- Veriler uygulama yeniden açıldığında korunmalı.

### 3.9 Oturum kaydedici
- Piyasa fiyatı, duvar davranışı ve order-flow olaylarının oturum sırasında kaydı.
- Maksimum süre dolduğunda kontrollü durdurma.
- Markdown, HTML ve JSON dışa aktarma.
- İsteğe bağlı analiz prompt şablonu.
- Kayıt dosyasına API anahtarı, özel kullanıcı bilgisi veya gereksiz hassas veri koyma.

## 4. Veri kaynakları ve bağlantı katmanı

Referans dosyada görünen kaynaklar:
- REST kökü: `https://fapi.binance.com`
- Market WebSocket adresi: `wss://fstream.binance.com/market`
- Public/depth WebSocket adresi: `wss://fstream.binance.com/public`

Bunlar yalnızca referansta görünen adreslerdir; uygulama geliştirilmeden önce güncel Binance resmî dokümantasyonuyla doğrulanmalıdır. Gerekirse geçerli stream adları ve bağlantı biçimi belgelenmiş resmî sözleşmeye göre düzeltilir. Kaynak adreslerini körlemesine kopyalamak kabul edilmez.

Veri aileleri:
- Futures perpetual sembol listesi ve 24 saatlik ticker.
- Kline/mum geçmişi ve canlı mum güncellemeleri.
- Aggregate trades.
- Order-book depth snapshot ve incremental depth update.
- Mark price/funding bilgisi.
- Force order / likidasyon akışı.
- Open interest REST sorgusu.
- Gerektiğinde best bid/ask ve spread.

### Veri bütünlüğü kuralları
- Depth snapshot ile incremental update sequence ID'leri doğru senkronize edilmeli; senkron bozulursa kitap geçersiz sayılıp yeniden oluşturulmalı.
- Aynı trade/olay iki kere işlenmemeli; olaylar zaman damgası ve uygun kimliklerle deduplicate edilmeli.
- REST/WebSocket zaman damgaları ve saniye/milisaniye dönüşümleri açık ve testli olmalı.
- Bağlantı kopması, gecikmiş veri, yeniden bağlanma, exponential backoff, jitter ve aboneliklerin yeniden kurulması uygulanmalı.
- Uygulama görünür bir veri yaşı göstergesi sunmalı. Eski veriden yeni sinyal üretilmesi engellenmeli veya açıkça geçersiz işaretlenmeli.
- Hız limitlerine saygı gösterilmeli; Top 50 taraması kontrolsüz biçimde eşzamanlı REST isteği başlatmamalı.
- Kullanıcı arayüzü veri akışının arkasında kilitlenmemeli. Yüksek frekanslı olaylar kontrollü micro-batch/buffer ile işlenmeli.
- Her veri adapter'ı şema doğrulaması yapmalı. Bozuk mesajlar uygulamayı çökertmek yerine loglanmalı ve sayılmalı.
- 451/403/429/5xx ve WebSocket close/error durumları ayrı sınıflandırılmalı; tanılama bilgisi gösterilmeli.

## 5. Analitik ve sinyal motoru

Hesaplama motoru UI'dan bağımsız, saf fonksiyonlar ve deterministik veri girdileriyle test edilebilir olmalı.

### Teknik göstergeler
- SMA/MA serileri.
- Parabolic SAR.
- Bollinger Bands.
- EMA.
- RSI.
- MACD.
- VWAP.
- Mum penceresi ve ATR/volatilite gibi referansta kullanılan yardımcı hesaplamalar.

### Raw-flow metrikleri ve olayları
- CVD ve çoklu zaman pencereleri.
- OBI ve çoklu zaman pencereleri.
- Open Interest değişimi.
- Funding ve spread.
- Likidasyon notional toplamı.
- Büyük işlem/whale işaretçileri.
- Sweep, absorpsiyon, delta burst, iceberg benzeri olay algılamaları.
- Order book duvarlarının tespiti, yaşam süresi, hareketi, çekilmesi ve fiyatla mesafesi.
- Scalping pusulası ve decay.
- Sinyal için confirm/veto kuralları.
- Pre-signal/erken hazırlık durumu ve nihai sinyalin ayrı ele alınması.

### Sinyal güvenliği ve anlamı
- AL/SAT sinyali yatırım tavsiyesi veya kâr garantisi gibi sunulmayacak.
- Skorun bileşenleri açıklanabilir olmalı; tek başına keyfî, sabit veya rastgele skor gösterilmemeli.
- Ham veri yetersizken, bağlantı kopukken veya kitap senkron dışındayken sinyal güveni düşürülmeli ya da sinyal geçersiz sayılmalı.
- Sinyal tetiklenme, veto ve iptal nedenleri loglanmalı.
- Aynı koşul devam ederken tekrar tekrar sinyal/uyarı spam'i önlenmeli.
- Geçmiş olaylar replay ile tekrar çalıştırıldığında aynı girdiler aynı sonucu üretmeli.

## 6. Önerilen teknoloji ve mimari

Referans tek HTML dosyasıdır; yeniden geliştirilen sürümün bakımı için modüler yapı tercih edilir. Mimari seçimi ilk audit sonunda belgelenmeli. Tercih edilen başlangıç yaklaşımı:
- TypeScript.
- Vite.
- Vanilla TypeScript veya hafif UI katmanı; React ancak durum/ekran karmaşıklığı gerçekten gerektiriyorsa.
- Lightweight Charts; kullanılacak sürümün API'si doğrulanmalı ve sürüm sabitlenmeli.
- IndexedDB için küçük ve test edilebilir bir repository/adapter katmanı.
- Vitest veya eşdeğer bir test runner.
- ESLint + formatter + TypeScript strict.
- GitHub Actions CI.
- Statik deploy uyumlu yapı; backend zorunluymuş gibi gereksiz sunucu ekleme.

### Önerilen modül sınırları
```text
src/
  app/
    bootstrap.ts
    router.ts
    app-state.ts
  core/
    config.ts
    clock.ts
    logger.ts
    errors.ts
    event-bus.ts
    numeric.ts
  data/
    binance/
      rest-client.ts
      symbol-service.ts
      kline-service.ts
      market-ws.ts
      depth-ws.ts
      schemas.ts
      rate-limiter.ts
      reconnect-policy.ts
    normalize/
      trade-normalizer.ts
      depth-normalizer.ts
      deduplicator.ts
      sequence-sync.ts
  domain/
    market/
      candle.ts
      trade.ts
      orderbook.ts
      liquidation.ts
    analytics/
      moving-averages.ts
      sar.ts
      bollinger.ts
      rsi.ts
      macd.ts
      vwap.ts
      cvd.ts
      obi.ts
      flow-events.ts
      wall-detector.ts
      signal-engine.ts
      compass.ts
    patterns/
      pattern-types.ts
      pattern-engine.ts
      pattern-outcomes.ts
      pattern-statistics.ts
      wilson.ts
    backtest/
      walk-forward.ts
      execution-model.ts
      performance-metrics.ts
  storage/
    settings-repository.ts
    favorites-repository.ts
    pattern-repository.ts
    session-repository.ts
    migrations.ts
  features/
    chart/
    signal/
    scanner/
    pattern-pool/
    backtest/
    favorites/
    settings/
    session-recorder/
  ui/
    components/
    theme/
    styles/
  workers/
    analytics.worker.ts
tests/
  unit/
  integration/
  replay/
  fixtures/
docs/
.agent/
.github/workflows/
```

Bu ağaç başlangıç önerisidir; mevcut kod audit'inden sonra ihtiyaç duyulmayan modüller gerekçeli olarak sadeleştirilebilir. Her şeyi tek bir `app.ts` içine taşımak, büyük bir `utils.ts` oluşturmak veya modüller arasında döngüsel bağımlılık kurmak kabul edilmez.

### Mimari kurallar
- UI, veri bağlantısı ve hesaplama motoru birbirinden ayrılmalı.
- WebSocket client'ları DOM elementlerine doğrudan erişmemeli.
- Hesaplama modülleri DOM, `window` ve doğrudan ağ çağrısı bağımlılığı taşımamalı.
- State güncellemeleri tek bir açık akış üzerinden yapılmalı.
- Kaynak bağlantısı başlatma/durdurma ve ekran değişiminde kaynak yönetimi idempotent olmalı.
- Her modül için tek sorumluluk, açık giriş/çıkış sözleşmesi ve test bulunmalı.
- Public API yüzeyi gereksiz yere genişletilmemeli.
- Ayarların doğrulaması, varsayılanları ve migration davranışı merkezi olmalı.

## 7. Görsel eşleşme ve mobil UX

- Referans ekranın koyu/açık teması, renkleri, panel hiyerarşisi, yoğun bilgi düzeni, alt navigasyonu ve grafik overlay'leri mümkün olduğunca birebir korunmalı.
- Öncelik mobil tarayıcıdır; küçük ekranlarda taşma, kesilen değerler, tıklanamayan kontroller ve klavye açılınca kaybolan alanlar test edilmeli.
- Güvenli alanlar (`safe-area-inset-*`), dikey kaydırma, dokunma alanları ve yatay tablo davranışı dikkate alınmalı.
- Grafik, overlay canvas ve DOM katmanları yeniden boyutlandırmada senkron kalmalı.
- Yüksek frekanslı render'lar birleştirilmeli; her WebSocket mesajında tüm arayüzü yeniden çizme.
- Erişilebilir etiketler, klavye ile temel kullanım ve renk dışında durum belirten metinler eklenmeli.
- Piksel düzeyindeki eşleşme yalnızca referans ekran görüntüleri alınabiliyorsa ölçülmeli; görüntü alınmadan “piksel piksel aynı” iddiası yapılmamalı.

## 8. Güvenlik ve gizlilik
- Binance API secret/key isteme veya saklama; kapsam public market data'dır.
- Token/secret değerleri kaynak koda, `index.html` içine, loglara veya commit'e yazılmayacak.
- Kullanıcı verileri yerel depoda tutuluyorsa hangi verinin nerede tutulduğu belgelenmeli.
- JSON içe aktarma dosyası şema ve boyut açısından doğrulanmalı; HTML dışa aktarma kullanıcı verisini çalıştırılabilir script olarak yorumlamamalı.
- HTML çıktısında kullanıcıdan gelen metinler güvenli biçimde escape edilmeli.
- Bağımlılık sürümleri sabitlenmeli; lisans ve güvenlik kontrolleri CI'a eklenmeli.

## 9. Test stratejisi ve kabul kriterleri

### Birim testleri
- Teknik göstergeler için sabit ve elle doğrulanabilir test vektörleri.
- CVD/OBI, spread, likidasyon toplamı ve duvar algılama testleri.
- Depth sequence senkronizasyonu, gap tespiti ve snapshot sonrası update testleri.
- Deduplication ve out-of-order mesaj testleri.
- Sinyal confirm/veto, pre-signal ve tekrar sinyal engelleme testleri.
- Wilson alt sınırı, win rate, Ret10, MFE/MAE ve backtest metrikleri.
- Zaman damgası ve fiyat string hassasiyeti testleri.
- Settings serialization/migration ve JSON import/export testleri.

### Entegrasyon testleri
- REST yanıtı doğrulama ve hata sınıflandırma.
- WebSocket bağlantısı, reconnect ve yeniden abonelik.
- IndexedDB repository işlemleri.
- Tarayıcı arayüzünde sembol/zaman dilimi değişimi.
- Tarayıcı tarama, pattern pool ve backtest akışları.
- Uyarı izinlerinin olmadığı veya desteklenmediği durumlar.

### Replay / gerçek veri testi
- Gerçek piyasa verisinden, hassas bilgi içermeyen ve kaynağı/zamanı belirtilmiş fixture'lar oluştur.
- Replay fixture'ları canlı veri yerine ürün çalıştırmak için kullanılmayacak; yalnızca test amaçlıdır ve UI'da gerçek zamanlı piyasa verisi diye sunulmayacak.
- Aynı fixture aynı sırayla işlendiğinde hesaplama sonuçları deterministik olmalı.
- Gerçek bağlantı testi, bağlantı kurulabildi mi/şema doğru mu/veri taze mi sorularını ayrı raporlamalı; ağ engeli olması unit test başarısızlığı olarak gizlenmemeli.

### Görsel/işlevsel kabul
- Dokuzuncu bölümdeki ekran envanterindeki her madde için test veya doğrulama kanıtı bulunmalı.
- Her görünen buton, seçim, slider ve toggle gerçek bir davranışa bağlı olmalı.
- Konsolda kontrolsüz hata, yakalanmamış Promise rejection veya sonsuz reconnect döngüsü olmamalı.
- Bağlantı kaybı ve eski veri kullanıcıdan saklanmamalı.
- Uygulama dar mobil ekranda ve masaüstünde kullanılabilir olmalı.
- Build, lint, typecheck ve testler CI'da çalışmalı.
- “Tamamlandı” etiketi yalnızca kod + test + kanıt birlikte mevcutsa verilmeli.

## 10. Ajan çalışma protokolü

Ajan, kod yazmaya başlamadan önce aşağıdaki aşamaları tamamlamalı. Her aşamada çıktılar depoya commit edilmeli.

### Aşama 0 — Kaynak uygulama audit'i
1. `index (30).html` dosyasını baştan sona incele.
2. Ekranlar, fonksiyonlar, state alanları, DOM ID'leri, olay dinleyicileri, ağ çağrıları, depolama ve zamanlayıcıların envanterini çıkar.
3. Özellik → kaynak fonksiyon/DOM alanı → yeni modül → test eşleştirme tablosu oluştur.
4. Referans davranışı belirsiz olan yerleri `docs/OPEN_QUESTIONS.md` içine yaz; sessizce uydurma.
5. Endpoint ve WebSocket şemalarını güncel resmî Binance belgeleriyle kontrol et.

### Aşama 1 — Mimari ve temel altyapı
1. `docs/PROJECT_AUDIT.md`, `docs/ARCHITECTURE.md`, `docs/FEATURE_PARITY.md`, `docs/TEST_STRATEGY.md` oluştur.
2. Build, lint, typecheck, test ve CI'ı ayağa kaldır.
3. Veri tipleri, hata sınıfları, logger, clock ve ayar modelini kur.
4. Boş ekran iskeletini değil, ilk modülü uçtan uca tamamlamayı hedefle.

### Aşama 2 — Modülleri dikey dilimler halinde geliştirme
Önerilen sıra:
1. REST sembol/mum verisi ve grafik.
2. Market WebSocket, bağlantı sağlığı ve yeniden bağlanma.
3. Aggregate trade/CVD/OBI/mark price/funding/OI/likidasyon veri akışları.
4. Depth snapshot + incremental update senkronizasyonu.
5. DOM, duvarlar, ısı haritası ve overlay.
6. Teknik analiz ve karar motoru.
7. Sinyal ekranı ve uyarılar.
8. Favoriler, ayarlar ve tema.
9. Pattern Pool ve desen istatistikleri.
10. Çoklu sembol tarayıcı.
11. Walk-forward backtest.
12. Oturum kaydedici ve dışa aktarma.
13. Performans, erişilebilirlik ve görsel eşleştirme.

Her dilim için: implementasyon → test → çalıştırma kanıtı → kod incelemesi → durum güncellemesi. Sonraki modüle yalnızca mevcut modülün arayüzü ve testleri sabitlendikten sonra geç.

### Aşama 3 — Birebirlik denetimi
- Referansın ekran ve davranış envanteriyle yeni uygulamayı madde madde karşılaştır.
- Eksik, farklı veya belirsiz davranışları `docs/FEATURE_PARITY.md` içine yaz.
- Her farkı ya düzelt ya da açık karar kaydıyla gerekçelendir.
- Çalışmayan özellikleri gizlemek yerine raporla.
- Sonuçları gerçek cihazda veya mobil emülasyonda kontrol et.

## 11. GitHub ve CI gereksinimleri
- Kısa, açıklayıcı commit'ler.
- Özellik başına branch ve pull request.
- PR açıklamasında amaç, değişiklik, test komutları, test sonucu ve bilinen riskler.
- GitHub Actions: install, lint, typecheck, unit/integration tests, build.
- Gerekirse bağımlılık denetimi ve statik güvenlik kontrolleri.
- `README.md`, `.env.example` (gerçek secret içermeyen), `CHANGELOG.md`, `docs/STATUS.md`.
- Her CI adımı gerçekten çalıştırılmalı; sadece YAML dosyası eklemek CI'ın çalıştığı anlamına gelmez.

## 12. İki ajanla çalışma (varsa)

İki ayrı ajan kullanılıyorsa:
- **Ajan A — Teknik lider/orchestrator:** kaynak audit'i, mimari, issue/task bölme, entegrasyon, durum ve kanıt kayıtlarından sorumlu.
- **Ajan B — Bağımsız mühendis/reviewer:** ayrı modül geliştirme, bağımsız kod incelemesi, test ve parity eksiklerini yakalama sorumluluğunda.
- Aynı dosyayı eşzamanlı değiştirmemeleri için dosya/modül sahipliği ve branch kuralları tanımlanmalı.
- Ajanlar arası iletişim gerçekten mevcut bir kanal (GitHub issue/PR, repo içi mesaj dosyası veya tanımlanmış connector) üzerinden yürümeli. Bir ajan diğer ajana mesaj gönderdiğini yalnızca metinde söyleyerek iletişim kurmuş sayılmaz.
- Bir ajan diğerinin test iddiasını mümkünse bağımsız olarak çalıştırmalı.
- Çatışmalar karar kaydıyla çözümlenmeli.

## 13. Zorunlu depo dosyaları

```text
README.md
TASK.md
PROJECT_BRIEF.md
AGENTS.md
CHANGELOG.md
docs/
  PROJECT_AUDIT.md
  PROJECT_BRIEF.md
  ARCHITECTURE.md
  FEATURE_PARITY.md
  ENGINEERING_STANDARDS.md
  TEST_STRATEGY.md
  SECURITY.md
  OPEN_QUESTIONS.md
  DECISIONS.md
  STATUS.md
  RELEASE_PLAN.md
.agent/
  state.json
  goal.json
  tasks.json
  attempts.jsonl
  evidence.jsonl
.github/
  pull_request_template.md
  workflows/ci.yml
```

İlk commit'te tüm dosyaları boş şablon olarak üretip işi bitmiş gibi gösterme. Önce gerçek içerikleri audit ve kararlarla doldur. JSON dosyaları geçerli JSON olmalı; JSONL kayıtları her satırda geçerli tek JSON nesnesi olmalı.

## 14. Durum modeli ve kanıt

Görev durumları:
- `PLANNED`: henüz başlanmadı.
- `WORKING`: geliştirme sürüyor.
- `IMPLEMENTED`: kod yazıldı, doğrulama henüz tamamlanmadı.
- `VERIFIED`: testler ve davranış kontrolleri geçti, kanıt kaydedildi.
- `BLOCKED`: açık engel ve denenmiş adımlar belgeli.
- `PRODUCTION-READY`: entegrasyon, güvenlik, performans ve release kriterleri tamamlandı.

Her görev için `docs/STATUS.md` veya `.agent/tasks.json` içinde şunlar bulunmalı:
- görev kimliği ve kabul kriterleri,
- sorumlu ajan,
- bağlı modül,
- durum,
- çalıştırılan komutlar,
- sonuçlar,
- kanıt bağlantıları,
- bilinen riskler/engeller.

`.agent/evidence.jsonl` içine tarih, görev kimliği, doğrulama türü, komut/işlem, sonuç ve log/CI/PR bağlantısı yazılmalı. Kanıt yoksa `VERIFIED` veya `PRODUCTION-READY` kullanılamaz.

## 15. İlk çalıştırmada ajanın yapacağı işler

1. Repo ağacını ve tüm mevcut dosyaları incele.
2. `index (30).html` referansını analiz et; kopyalayıp farklı isimle bırakma.
3. Bu brief'i repo içine `PROJECT_BRIEF.md` olarak koy.
4. Kaynak uygulamanın feature/function/state/network/storage envanterini çıkar.
5. Açık soruları, endpoint doğrulamalarını ve parity matrisini hazırla.
6. Mimari kararlarını gerekçeli biçimde yaz.
7. En küçük ama gerçek uçtan uca dikey dilimi belirle.
8. CI ve test altyapısını kur.
9. İlk dikey dilimi kodla, test et, gerçek çalıştırma kanıtı kaydet.
10. Kısa durum raporu üret: tamamlananlar, testler, kanıtlar, engeller ve sıradaki iş.

## 16. Kesinlikle kabul edilmeyen sonuçlar

- Yalnızca ekran görüntüsüne benzeyen statik maket.
- Tıklanınca hiçbir şey yapmayan butonlar veya etkisiz ayarlar.
- Rastgele/sabit/mocked piyasa verisinin canlı veri diye gösterilmesi.
- WebSocket çalışmıyorken bağlantı göstergesinin yeşil kalması.
- Endpoint hatalarının sessizce yutulması.
- Test çalıştırmadan “tüm testler geçti” denmesi.
- Bütün kodun tekrar dev bir dosyada toplanması.
- Gerçekte kurulmamış ajanlar arası iletişim varmış gibi raporlanması.
- Kaynak uygulamanın bazı özelliklerini incelemeden kapsam dışı bırakmak.
- Backtest performansını kârlılık garantisi olarak sunmak.
- Secret/token değerlerini repo veya loglara yazmak.

## 17. Nihai teslim paketi

- Çalışır, modüler uygulama kaynak kodu.
- Referansla eşleşme matrisi ve açıklanmış tüm farklar.
- Testler ve çalıştırılabilir CI workflow'u.
- Mimari, kurulum, veri kaynakları, bilinen kısıtlar ve deploy talimatlarını içeren README.
- Gerçek veri bağlantısının hangi koşullarda çalıştığını gösteren kanıtlar.
- Teknik analiz/order-flow formülleri ve sinyal kuralları dokümantasyonu.
- Backtest metodolojisi ve sınırlılıkları.
- Ajan görev/deneme/kanıt kayıtları.
- `VERIFIED` / `PRODUCTION-READY` olarak işaretlenmiş her özellik için gerçek doğrulama kaydı.

**Bitiş ölçütü:** Proje, yalnızca “kod yazıldı” diye tamamlanmış sayılmaz. Referanstaki özelliklerin envanteri çıkarılmış, her özelliğin yeni karşılığı uygulanmış, işlevsel test edilmiş, canlı veri bağlantısının durumu dürüstçe gösterilmiş ve tüm farklar kanıtlarla raporlanmış olmalıdır.
