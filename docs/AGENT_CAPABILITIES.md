# AGENT CAPABILITIES — Doğrulanmış Yetenekler

- **Ajan:** KIBIR (ilk ajan, bu turun yazarı)
- **Tarih:** 2026-10-13 (UTC)
- **Kural:** Teorik yetenek ile gerçek erişim ayrıdır. Aşağıda yalnızca bu turda gerçekten denenen yetenekler PASS'tır; denenemeyenler `NOT_RUN`, başarısızlar `FAIL` olarak işaretlidir. Kanıtlar `.agent/evidence.jsonl` içindedir.

## KIBIR — yetenek matrisi

| Yetenek / erişim | Durum | Nasıl doğrulandı | Kanıt |
|---|---|---|---|
| Repo okuma (dosya, git geçmişi) | PASS | `git ls-files`, `git log` koşuldu; 3 dosya, 3 commit envanteri çıkarıldı | EV-0001 |
| Repo yazma (yerel çalışma alanı) | PASS | Bu turdaki tüm dosyalar yazıldı; `git status` ile izlendi | EV-0008 |
| Git branch açma / yerel commit | PASS | `docs/000-kickoff-kurulum-turu` branch'i açıldı; kimlik `Agent KIBIR <kibir@agent.local>` ayarlandı | EV-0009 |
| Git push (GitHub) | FAIL | Tur sonunda denendi: `could not read Username` (exit 128), kimlik bilgisi yok. Kimlik bilgisi repoya/sohbete yazılmaz; yedek teslim `git bundle` ile yapılır | EV-0010, AT-0004 |
| GitHub Issue / PR açma | NOT_RUN | `gh` CLI ortamda yok (`command not found`); token da yok. Issue/PR açıldığı iddia edilemez | EV-0002 |
| GitHub Actions çalıştırma | NOT_RUN | Push + `gh` olmadan tetiklenemez/doğrulanamaz. Workflow dosyası yazıldı ama "CI çalışıyor" denmez | EV-0002 |
| Terminal / kabuk | PASS | bash komutları koşuldu (git, curl, python, node sürüm kontrolleri) | EV-0001, EV-0002 |
| Python 3.13 + stdlib test | PASS | `validate-protocol.py` ve `unittest` koşuldu | EV-0008 |
| Node.js 20 / npm 10 | MEVCUT, KULLANILMADI | `node --version` → v20.20.2, `npm --version` → 10.8.2. Henüz `package.json` yok; uygulama komutu iddia edilmiyor | EV-0002 |
| Web / resmi dokümantasyon araştırması | PASS | Binance Developers sayfaları okundu; endpoint tablosu çıkarıldı | EV-0006 |
| Binance REST (sandbox ağı) | FAIL | `fapi/v1/ping` ve `/time` → HTTP 451 (restricted location). Aşma girişimi yok | EV-0003 |
| Binance WebSocket (sandbox ağı) | PASS | `/market` miniTicker ve `/public` depth mesajları gerçekten alındı | EV-0004, EV-0005 |
| Tarayıcı / gerçek cihaz testi | NOT_RUN | Bu ortamda tarayıcı ve mobil cihaz yok; görsel eşleşme iddiası üretilmez | — |
| Karşı ajana mesaj iletme | KANAL: repo içi talk dosyası | Gerçek kanal repodur (GitHub'a push edilebilirse). Bu turda kanalın GitHub ucu doğrulanamadı; yerel commit + bundle yedeği uygulanacak | EV-0009 |

## SOKAK — yetenek matrisi

**Bilinmiyor.** SOKAK henüz var olmadı/doğrulanmadı (`verified_peer.SOKAK = null`). Bu tablo SOKAK adına doldurulmaz; `TASK-002` ile SOKAK kendi kimliğiyle dolduracaktır. SOKAK'ın araçları, GitHub imkânı, test yeteneği ve kısıtları hakkında bu belgede hiçbir iddia yoktur.

## Ortak sınırlar

- İki ajan da aynı repo dosyaları üzerinde çalışır; eşzamanlı dosya sahipliği `.agent/tasks.json` lease alanlarıyla yönetilir.
- Hiçbir ajanın üretim ortamına, ücretli servise veya kullanıcı tarayıcısına erişimi varsayılmaz; gerektiğinde proje sahibinden istenir ve yanıt gelmeden yapılmış sayılmaz.
