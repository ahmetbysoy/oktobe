# DECISIONS — Karar Kayıtları

Biçim: bağlam → seçenekler → seçim → gerekçe → doğrulama yöntemi → yeniden değerlendirme koşulu. Karşı ajan doğrulanmadan alınan kararlar "tek taraflı kurulum kararı" olarak işaretlenir; ortak karar değildir.

## D-001 — İlk ajan karakteri: KIBIR

- **Bağlam:** `task.md` 6.3 ilk ajanın karakter seçmesini ister. Ortamda tek ajan oturumu var.
- **Seçenekler:** KIBIR (denetim/edge-case odaklı) veya SOKAK (saha/çalıştırma odaklı).
- **Seçim:** Kurulum turunu KIBIR yürütür; SOKAK davet edilen ikinci ajandır.
- **Gerekçe:** İlk tur kod değil denetim, envanter ve kanıt disiplinidir; karakter tanımı bu işe uyar. Seçim kalıcı rol değildir; görev bazında Builder/Reviewer rolleri `tasks.json`'da döner.
- **Doğrulama:** `git config user.name = Agent KIBIR`; talk dosyası `from: KIBIR` ve commit yazarı eşleşmesi `validate-protocol.py` ile denetlenir.
- **Yeniden değerlendirme:** Proje sahibi tersini isterse yeni kickoff turuyla düzeltilir.

## D-002 — Tek kanonik protokol dosyası: `task.md`

- **Bağlam:** Brief Bölüm 13 `TASK.md`, mevcut repo `task.md` ister (Linux'ta ikisi ayrı dosyadır).
- **Seçenekler:** (a) dosyayı `TASK.md` olarak yeniden adlandırmak, (b) iki kopya tutmak, (c) mevcut `task.md`'yi kanonik saymak.
- **Seçim:** (c). `AGENTS.md` bu seçimi açıkça yazar.
- **Gerekçe:** Yeniden adlandırma proje sahibinin verdiği adı bozar; çift kopya kaçınılmaz olarak ıraksar (divergence). Tek kaynak + açık işaret, en düşük risk.
- **Yeniden değerlendirme:** Proje sahibi büyük harf isterse tek commit'te `git mv` yapılır ve tüm referanslar güncellenir.

## D-003 — `PROJECT_BRIEF.md` tek kopya (repo kökü)

- **Bağlam:** `task.md` 6.5 ağacı `docs/PROJECT_BRIEF.md`, brief Bölüm 13 ise kökte `PROJECT_BRIEF.md` listeler; brief Bölüm 15 "bu brief'i repo içine `PROJECT_BRIEF.md` olarak koy" der ve dosya zaten köktedir.
- **Seçim:** Kanonik kopya kökteki dosyadır; `docs/` altına ikinci kopya konmaz, belgeler kök dosyaya referans verir.
- **Gerekçe:** D-002 ile aynı ıraksama riski. Brief'in kendi metni de kök konumu söyler.
- **Yeniden değerlendirme:** Proje sahibi `docs/` kopyası isterse kopya değil, üretim (generate) kuralı tanımlanır.

## D-004 — Protokol içi çelişki: baton `holder` (6.3 vs 4.4)

- **Bağlam:** 6.3 ilk batonda `holder: ikinci ajan` der; 4.4 "karşı ajan doğrulanmadan baton devredilmez; holder aynı kalır" der.
- **Seçim:** İlk baton 6.3'e göre kuruldu (`seq:1, holder:SOKAK, verified_peer:null`) ancak bu kayıt **davet durumu** olarak yorumlandı: SOKAK kendi kimliğiyle claim edene kadar hiçbir görev `VERIFIED` olamaz, ortak mimari karar alınamaz, SOKAK adına tur yazılamaz.
- **Gerekçe:** 6.3 ilk duruma özgü açık talimattır; 4.4'ün koruma amacı (sahte devir/inceleme) davet yorumuyla aynen korunur. İki kuralı da delen yorum (ör. SOKAK adına dosya yazmak) seçilmedi.
- **Doğrulama:** `baton.json.handoff_note` ve `docs/TEAM_PROTOCOL.md` bu yorumu yazar; STATUS'ta peer durumu açıkça "doğrulanmadı" görünür.
- **Yeniden değerlendirme:** Proje sahibi nihai yorumu verir; gerekirse ilk gerçek devirde düzeltilir.

## D-005 — Binance URL sözleşmesi: yönlendirilmiş uçlar, legacy yok

- **Bağlam:** Brief Bölüm 4 adresleri "resmi dokümantasyondan doğrulamadan kopyalama" der.
- **Bulgu:** REST kökü `https://fapi.binance.com` doğru. WS'te `/public` ve `/market` yönlendirmesi güncel resmi biçim; yönlendirmesiz/legacy bağlantı 2026-04-23 sonrası yalnızca `/public` verisi verir. Depth `/public`, aggTrade/kline/markPrice `/market` tarafındadır (stream bazında tek tek doğrulanacak).
- **Seçim:** Yeni kod yalnızca yönlendirilmiş uçları kullanır; stream→uç tablosu `TASK-005`'te resmi kaynaklarla kilitlenir.
- **Doğrulama:** `EV-0004`, `EV-0005` canlı WS kanıtları; `EV-0006` dokümantasyon kaydı.

## D-006 — Sandbox REST 451: aşma yok, durum raporlanır

- **Bağlam:** Sandbox çıkışından `fapi.binance.com` HTTP 451 döndürüyor; aynı ağdan WebSocket çalışıyor.
- **Seçim:** Hiçbir aşma tekniği (proxy/VPN/ayna endpoint) denenmez ve ürüne konmaz. Uygulama 451'i ayrı hata sınıfı olarak gösterir. Canlı REST doğrulaması hedef cihaz/ağda yeniden koşulur (`TASK-008`).
- **Gerekçe:** Brief Bölüm 2 ve 4 açık yasağı; ayrıca yasal/bölgesel kısıtlamayı gizlemek doğruluk kuralı ihlalidir.

## D-007 — CI kapsamı (şu an): protokol doğrulama

- **Bağlam:** Uygulama yığını henüz seçilmedi; olmayan `npm` komutlarını CI'a yazmak sahte CI üretir.
- **Seçim:** `.github/workflows/ci.yml` şu an yalnızca `validate-protocol.py` + `unittest` koşar. Uygulama işleri `TASK-007`'de gerçek komutlarla eklenir.
- **Durum notu:** Workflow yazıldı ancak GitHub'da **çalıştırılmadı** (push/gh yok). "CI yeşil" iddiası yoktur.

## D-008 — Ürün koduna bu turda başlanmaması

- **Bağlam:** Brief Bölüm 15 ilk çalıştırmada dikey dilim de ister; `task.md` Bölüm 6 ise "ilk görev kod yazmak değildir" der ve kickoff sonrası karşı yanıt beklenmesini şart koşar. Hiyerarşide süreç protokolü + brief birlikte okunur; mimari karar (6.4) iki ajan ister.
- **Seçim:** Bu turda ürün kodu yazılmaz. Kod, `TASK-002` (karşı ajan) → `TASK-006` (mimari karar) → `TASK-007` (iskele) sırası açılınca başlar.
- **Gerekçe:** Tek ajanla mimariyi kilitleyip kod yazmak, protokolün yazar≠onaylayıcı ve bağımsız değerlendirme kurallarını ilk günden bozar; üstelik referans dosya yokken yazılan arayüz parity'siz tahmin olur.

## Açık kararlar (sahibi bekliyor)

| Karar | Sahibi | Bağlı görev |
|---|---|---|
| Referans dosyanın sağlanması | Proje sahibi | TASK-003 |
| İkinci ajanın (SOKAK) nasıl başlatılacağı (ayrı oturum/araç) | Proje sahibi | TASK-002 |
| Nihai yığın ve grafik kütüphanesi | İki ajan + gerekirse sahibi onayı | TASK-006 |
| Deploy hedefi | Proje sahibi | TASK-007/014 |
| Backtest maliyet modeli (referansta yoksa) | Karar kaydıyla iki ajan | TASK-013 |
