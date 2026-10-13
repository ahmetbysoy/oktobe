# ENGINEERING STANDARDS — Mühendislik Standartları

Nihai yığın `TASK-006` kararıyla kilitlenecek; bu belge yığından bağımsız bağlayıcı kuralları ve kilit sonrası aday standartları ayırır.

## Bağlayıcı (şimdiden geçerli)

- **Kanıt disiplini:** Taze koşulmamış kontrol "geçti" sayılmaz; kanıt `evidence.jsonl`'a, başarısız denemeler `attempts.jsonl`'a işlenir.
- **Değişiklik disiplini:** Branch + PR; ana dala doğrudan push yok. Commit mesajları kısa, açıklayıcı, nötr dilde. Kimse kendi PR'ını onaylamaz.
- **Dosya sahipliği:** Görev `files` alanı dışına taşılmaz; aktif lease ile kesişen dosyaya dokunulmaz.
- **Dürüst durum:** Çalışmayan özellik gizlenmez; `NOT_RUN`, `BLOCKED`, `UNVERIFIED` etiketleri çekinmeden kullanılır.
- **Veri dürüstlüğü:** Mock/sahte piyasa verisi canlı diye sunulmaz; replay yalnızca testtedir ve öyle etiketlenir.
- **Güvenlik:** Secret/token repoya ve loga yazılmaz; kullanıcı metni HTML çıktısında escape edilir; JSON import şema + boyut doğrulamasından geçer (ayrıntı: `SECURITY.md`).

## Yığın kilidi sonrası aday standartlar (TASK-006/007'de onaylanacak)

- TypeScript `strict`, ESLint + formatter; sürümler ve bağımlılıklar lockfile ile sabitlenir.
- Hesaplama modülleri saf ve deterministik; DOM/`window`/ağ bağımlılığı yasak. Fiyat/miktar hassasiyeti için string→decimal dönüşüm kuralları tek modülde (`core/numeric`) ve testli.
- Her modül tek sorumluluk; public API yüzeyi dar tutulur; döngüsel bağımlılık yok; dev `utils.ts` yok.
- Hata sınıfları merkezi (`core/errors`): ağ (451/403/429/5xx), şema, senkron (depth gap), depolama hataları birbirine karışmaz; loglar secret içermez.
- Test adlandırma ve fixture düzeni `TEST_STRATEGY.md` katmanlarına uyar; her davranış değişikliği testle gelir.
- Yüksek frekanslı render birleştirilir; her WS mesajında tam UI çizimi yapılmaz.

## İnceleme standardı

Bulgular `CRITICAL/HIGH/MEDIUM/LOW` şiddetinde, dosya/satır + gerekçe + etki + önerilen düzeltmeyle yazılır; her inceleme turu tek `PASS` veya `FAIL` kararıyla biter. Karakter dili bulgu raporuna giremez (yalnızca talk "Konuşma" bölümü).
