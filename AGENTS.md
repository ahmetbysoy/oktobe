# AGENTS.md — Ortak Çalışma Kuralları

Bu repo iki ajanlı protokolle çalışır. **Süreç otoritesi `task.md` dosyasıdır** (repo kökünde küçük harfle `task.md`; dosya adı çakışması/çift kopya riski nedeniyle ikinci bir `TASK.md` oluşturulmaz — bkz. `docs/DECISIONS.md` D-002). Bu dosya, `task.md`'yi özetlemez; günlük çalışmada uyulacak bağlayıcı kuralları işaret eder. Çakışmada hiyerarşi: proje sahibi > güvenlik/doğruluk > `task.md` + bu dosya > baton sahibi > challenger.

## Kimlikler

| Ajan | Git adı | Git e-postası | Karakter alanı |
|---|---|---|---|
| KIBIR | `Agent KIBIR` | `kibir@agent.local` | Yalnızca `docs/talk/` içindeki "Konuşma" bölümü |
| SOKAK | `Agent SOKAK` | `sokak@agent.local` | Yalnızca `docs/talk/` içindeki "Konuşma" bölümü |

- Her ajan yalnızca kendi kimliğiyle commit atar; yalnızca kendi adına konuşma dosyası yazar. Başka ajanın turunu yazmak protokolün en ağır ihlalidir (`task.md` 4.4).
- Kod, commit mesajı, PR açıklaması, bulgu raporu ve kullanıcı raporu **profesyonel ve nötr** dildedir. Karakter yalnızca talk "Konuşma" bölümündedir.
- Commit yazarı ile talk dosyasının `from` alanı eşleşmek zorundadır; `scripts/validate-protocol.py` bunu denetler.

## Baton ve devir

- Sıra bilgisi sohbette değil `.agent/baton.json` içindedir. Dosyayı okumadan işe başlama.
- Baton/görev almak = dosyayı güncelleyip commit + push etmek. Push çakışırsa alma başarısızdır; kazananın kaydı ezilmez.
- Karşı ajan farklı git kimliğiyle doğrulanmadan (`verified_peer` dolmadan) baton fiilen devredilmiş sayılmaz, hiçbir görev `VERIFIED` yapılamaz.
- Karşı ajan yanıt vermediyse "yanıt bekleniyor" yazılır; sahte yanıt, sahte mutabakat, hayalî ajan konuşması yazılmaz.

## Görevler ve kilitler

- Görev kaydı `.agent/tasks.json`. Başlamadan önce `files` alanının başka aktif lease ile kesişmediğini kontrol et; kesişiyorsa görevi alma.
- Durumlar: `BACKLOG, READY, IN_PROGRESS, BLOCKED, IMPLEMENTED, REVIEW, VERIFIED, PRODUCTION_READY, CANCELLED`. `IMPLEMENTED ≠ VERIFIED ≠ PRODUCTION_READY`.
- Her görevde Builder ≠ Reviewer. Yazar kendi kodunu tek başına onaylayamaz.
- Ana dala doğrudan push yok. Branch biçimi: `feat|fix|test|docs/<no>-<kısa-ad>`. Issue numarası yoksa `000` öneki kullanılır ve bu sapma görev kaydına yazılır.

## Kanıt (değişmez)

- "Çalıştı / geçti / düzeldi / tamam" iddiası, **o turda** çalıştırılmış komutun taze çıktısına ve `.agent/evidence.jsonl` kaydına dayanmak zorundadır (`task.md` 11.2). Kanıtsız iddia `UNVERIFIED` etiketlenir.
- Çalıştırılamayan kontrol `NOT_RUN` + neden olarak kaydedilir. Başarısız test başarılı gösterilmez.
- Aynı başarısız yaklaşım yeni kanıt olmadan en fazla iki kez denenir; üçüncüsünde `attempts.jsonl` + kök neden + farklı yaklaşım (`task.md` Bölüm 8).

## Ürüne özgü değişmezler (PROJECT_BRIEF.md)

- Mock/sahte/rastgele piyasa verisi canlı veri gibi **sunulamaz**. Bağlantı yoksa durum açıkça yazılır.
- Binance API anahtarı/secret istenmez, saklanmaz, loglanmaz. Kapsam yalnızca public market data'dır; emir gönderimi yok.
- HTTP 451/CORS gibi engeller belgelenmemiş yollarla aşılmaz; durum ve sebep raporlanır.
- Hesaplama modülleri DOM/`window`/ağ bağımlılığı taşımaz; WebSocket istemcileri DOM'a doğrudan erişmez.

## Şu an gerçekten çalışan komutlar

```bash
python3 scripts/validate-protocol.py          # protokol + JSON/JSONL doğrulama
python3 -m unittest discover -s tests -v      # protokol doğrulayıcı birim testleri
```

Uygulama yığını (TypeScript/Vite adayı) `TASK-006` mimari kararıyla kilitlenene kadar `npm` komutu yoktur; olmayan komutu CI'a veya rapora yazma. Karar sonrası bu bölüm gerçek komutlarla güncellenir.
