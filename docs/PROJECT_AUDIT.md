# PROJECT AUDIT — Mevcut Durum Denetimi

- **Tur:** Kurulum Turu (`TASK-001`), Builder: KIBIR, Reviewer: SOKAK (henüz doğrulanmadı)
- **Tarih:** 2026-10-13 (UTC)
- **Yöntem:** Her bulgu, bu turda gerçekten çalıştırılan bir komuta veya resmi dokümantasyon kontrolüne dayanır. Kanıt kayıtları: `.agent/evidence.jsonl` (EV-0001 … EV-0009). Çalıştırılamayan kontroller `NOT_RUN` olarak işaretlidir; hiçbiri çalıştırılmış gibi yazılmamıştır.

## 1. Repo envanteri (gerçek)

2026-10-13 tarihinde `git ls-files` çıktısı — repo yalnızca üç dosyadan oluşuyor:

| Dosya | Boyut | İçerik | Durum |
|---|---|---|---|
| `README.md` | 8 bayt | Yalnızca `# oktobe` başlığı | Bu turda gerçek içerikle genişletildi |
| `task.md` | 28.574 bayt | İki ajanlı geliştirme protokolü (süreç otoritesi) | Değiştirilmedi, salt referans |
| `PROJECT_BRIEF.md` | 27.851 bayt | Ürün brief'i (Futures Scanner / Order-Flow Terminal) | Değiştirilmedi, salt referans |

- **Uygulama kodu yok.** Giriş noktası, paket yöneticisi dosyası (`package.json`), build/test/lint/typecheck komutu, CI workflow'u, `.agent/` ve `docs/` yapısı kurulum turu öncesi mevcut değildi.
- Git geçmişi (3 commit, tamamı proje sahibi `ahmetbysoy`, 2026-10-13, GitHub web yüklemesi): `e516700 Initial commit (README)`, `be39db8 Add files via upload (task.md)`, `499bc96 Add files via upload (PROJECT_BRIEF.md)`.
- Branch durumu bu tur öncesi: yalnızca `main` (`origin/main` ile senkron). Bu tur `docs/000-kickoff-kurulum-turu` branch'inde çalışıldı; ana dala doğrudan yazılmadı.
- GitHub Actions, Issue, PR: **NOT_RUN / doğrulanamadı** — ortamda `gh` CLI yok, token yok. Var oldukları iddia edilmiyor (`EV-0002`).

## 2. Kritik bulgu: referans uygulama dosyası yok

Brief'in birincil kaynağı olan `index (30).html` **repoda yok**; git geçmişinde hiç yer almamış; çalışma alanında da bulunamadı (`EV-0007`: repo + geçmiş + `/home/user` taraması boş döndü).

Sonuçları:

- `docs/PROJECT_AUDIT.md` Bölüm 10 "Aşama 0" (ekran/fonksiyon/state/DOM/olay/ağ/depolama envanteri) **başlatılamaz**; başlatılmış gibi yazılmadı.
- `docs/FEATURE_PARITY.md`, brief Bölüm 3 ekran envanteri üzerinden kuruldu; referans sütunu tüm maddelerde `BLOCKED — referans yok` durumundadır. Hiçbir özellik "referansla eşleşiyor" diye işaretlenmedi.
- Bu engel `TASK-003` olarak proje sahibine atandı: dosyanın repoya eklenmesi gerekiyor. Dosya gelmeden ürün kapsamı yalnızca brief metniyle sınırlıdır ve parity iddiası üretilemez.

## 3. Hedef ürün (brief özeti)

Binance USDⓈ-M Futures public piyasa verisiyle çalışan, mobil öncelikli **Futures Scanner / Order-Flow Terminal**: mum grafiği (1m/5m), AL/SAT/İZLEMEDE karar motoru, CVD/OBI/OI/funding, DOM/order book, likidite duvarları ve ısı haritası, likidasyonlar, sinyal ekranı, çoklu sembol tarayıcı, desen havuzu (IndexedDB), walk-forward backtest, favoriler, kapsamlı ayarlar, oturum kaydedici. Emir gönderimi ve hesap anahtarı kapsam dışıdır (`PROJECT_BRIEF.md` Bölüm 1–3).

## 4. Mimari (mevcut)

Mevcut mimari yoktur; yeşil alan (greenfield). Önerilen hedef mimari brief Bölüm 6'daki modül sınırlarına dayanır ve `docs/ARCHITECTURE.md` içinde **taslak/UNVERIFIED** olarak yazıldı: iki ajanın bağımsız değerlendirmesi (`TASK-006`) tamamlanmadan mimari karar sayılmaz. UI / veri bağlantısı / hesaplama motoru ayrımı, depth senkronizasyonu ve durum akışı kuralları orada tanımlıdır.

## 5. Binance sözleşmesi — resmi dokümantasyon doğrulaması (ön bulgular)

Kurulum turunda dokümantasyon düzeyinde doğrulandı (`EV-0006`); kod sözleşmesine `TASK-005` dönüştürecek:

| Konu | Brief'teki ifade | Resmi dokümantasyon bulgusu | Karar durumu |
|---|---|---|---|
| REST kökü | `https://fapi.binance.com` | Doğru: base endpoint `https://fapi.binance.com` | Ön doğrulama PASS |
| Market WS | `wss://fstream.binance.com/market` | Doğru ve güncel: yönlendirilmiş uçlar `/public`, `/market`, `/private` | Ön doğrulama PASS |
| Public/depth WS | `wss://fstream.binance.com/public` | Doğru: yüksek frekanslı public veri (depth dahil) `/public` üzerinden | Ön doğrulama PASS |
| Eski URL biçimi | Brief'te yok | `wss://fstream.binance.com/ws/...` legacy biçimi **2026-04-23 sonrası kalıcı olarak kaldırıldı**; yönlendirmesiz bağlantı yalnızca `/public` verisi alır | Yeni kod legacy biçim kullanmayacak |
| Stream → uç eşlemesi | Genel ifade | Ör. aggTrade/markPrice/kline → `/market`; depth → `/public`. Her stream kod yazımında tek tek resmi sayfasından doğrulanacak | `TASK-005` kapsamında |
| Yerel order book | Brief Bölüm 4 kuralları | Resmi akış: WS buffer → REST snapshot (`/fapi/v1/depth`) → `u < lastUpdateId` olayları düşür → `pu == önceki u` zinciri; koparsa baştan snapshot | Mimariye işlendi |

Kaynaklar: Binance Developers — USDⓈ-M Futures *Websocket Market Streams*, *Important WebSocket Change Notice*, *General Info*, *How to manage a local order book correctly* (URL'ler `TASK-005` kaydında ve konuşma dosyası kanıt bölümünde).

## 6. Bağlantı gerçekliği (bu sandbox ortamında koşuldu)

| Kontrol | Komut/yöntem | Sonuç | Kanıt |
|---|---|---|---|
| REST ping | `curl https://fapi.binance.com/fapi/v1/ping` | **FAIL — HTTP 451** ("Service unavailable from a restricted location"). Aşma girişimi yapılmadı, yapılmayacak | EV-0003 |
| REST time | `curl https://fapi.binance.com/fapi/v1/time` | **FAIL — HTTP 451** (aynı mesaj) | EV-0003 |
| WS market | `wss://fstream.binance.com/market/ws/btcusdt@miniTicker` (python websocket-client) | **PASS** — bağlantı açıldı, `24hrMiniTicker` mesajı alındı | EV-0004 |
| WS public | `wss://fstream.binance.com/public/ws/btcusdt@depth@100ms` | **PASS** — `depthUpdate` alındı; `U/u/pu` alanları mevcut | EV-0005 |

Yorum (varsayım değil, sınırlarıyla): Sandbox çıkış ağında REST 451 iken WebSocket çalışıyor. Bu, kullanıcının tarayıcısının/cihazının bulunduğu ağda da aynı sonucun çıkacağı anlamına gelmez; REST canlılığı hedef cihaz/ağdan ayrıca doğrulanmalıdır (`TASK-008` kabul kriteri). 451 durumu UI'da gizlenmeyecek bir hata sınıfı olarak tasarlanacak.

## 7. Çalışan / eksik özellikler

- Çalışan ürün özelliği: **yok** (kod yok).
- Bu turda kurulan ve gerçekten koşulan tek yazılım: `scripts/validate-protocol.py` + `tests/test_validate_protocol.py` (protokol doğrulayıcısı). Sonuçlar `EV-0008`/`EV-0009`.
- Eksik olan her şey `docs/FEATURE_PARITY.md` matrisinde madde madde `NOT_IMPLEMENTED` olarak listelidir.

## 8. Teknik borç ve riskler

Kod olmadığı için klasik teknik borç yok. Gerçek riskler:

1. **Referans dosya yokluğu** — parity ve Aşama 0 bloklu (en yüksek risk).
2. **İkinci ajan yokluğu** — protokol gereği inceleme/VERIFIED kapısı kapalı; tek ajanlı çalışma protokolü içeriden boşaltır.
3. **REST 451 (ortama bağlı)** — kline geçmişi ve depth snapshot REST'e bağımlı; hedef ağ doğrulanmadan canlı veri vaadi verilemez.
4. **GitHub erişimi yokluğu** — branch push/Issue/PR/CI bu ortamdan doğrulanamıyor; yerel commit + bundle yolu kullanılacak (bkz. konuşma dosyası).
5. **Kapsam büyüklüğü** — brief 9 ekran, 13 dikey dilim; tek görevde toplama riski `TASK-012/013` bölme kuralıyla yönetiliyor.

## 9. Güvenlik durumu

Repoda kod, secret, token, kişisel veri yok (bu turda da yazılmadı; git kimlik e-postaları `agent.local` sahte iç alan adlarıdır, gerçek adres değildir). Gelecek kuralları `docs/SECURITY.md` içindedir: anahtar istememe, import/export doğrulama ve escape, bağımlılık sabitleme. Üretim verisi/migration riski şu aşamada yok.

## 10. Hedef ile mevcut arasındaki fark ve strateji

| Katman | Hedef | Mevcut | Farkı kapatan görev |
|---|---|---|---|
| Referans envanteri | Tam parity matrisi | Brief tabanlı matris, referans sütunu bloklu | TASK-003 → TASK-004 |
| Mimari | İki ajan onaylı karar | Tek ajan taslağı (UNVERIFIED) | TASK-002 → TASK-006 |
| Altyapı | TS/Vite/test/CI çalışıyor | Yalnızca protokol doğrulayıcı çalışıyor | TASK-007 |
| Veri katmanı | REST+WS, senkron kitap | Sözleşme ön doğrulaması + canlı WS kanıtı | TASK-005, 008–011 |
| Ürün ekranları | 9 ekran grubu | Yok | TASK-008 … 014 |

Strateji: önce protokol kapıları (ikinci ajan + referans dosya), sonra mimari karar, sonra brief Bölüm 10 sırasıyla dikey dilimler; her dilimde implementasyon → test → taze kanıt → karşı inceleme.
