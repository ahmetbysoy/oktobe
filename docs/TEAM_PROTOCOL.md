# TEAM PROTOCOL — Operasyon Özeti

Otorite: `task.md` (bu dosya onun yerine geçmez; sahada hızlı başvuru içindir).

## Durum makinesi

```text
BACKLOG -> READY -> IN_PROGRESS -> IMPLEMENTED -> REVIEW -> VERIFIED -> PRODUCTION_READY
                        |               ^            |
                        +-> BLOCKED ----+            +-> (bulgu varsa) IN_PROGRESS
Her durumdan -> CANCELLED (gerekçeli)
```

- `VERIFIED`: kabul kriterleri geçti + taze kanıt + Reviewer onayı.
- `PRODUCTION_READY`: ek olarak temiz checkout'ta çalışma, hata yönetimi, timeout/retry, log, secret yönetimi, bilinen sınırlar yazılı.

## Tur (round) akışı

1. `.agent/baton.json` oku; `holder` + lease tazeliğini kontrol et.
2. `last_talk_file` ve önceki en az iki talk dosyasını oku; özellikle **Yaramayanlar** bölümlerini.
3. Kimlik kontrolü: `git log --pretty='%an %h %s' -- docs/talk/` — yazar/`from` eşleşmesi bozuksa ihlali raporla, turları `UNVERIFIED` say.
4. `state.json`, `tasks.json`, `evidence.jsonl` oku; kayıtlı durumu gerçeğiyle karşılaştır (son kontrolleri yeniden koş).
5. Yeni talk dosyası aç: `docs/talk/NNNN-<AJAN>-<görev-id>-<kısa-konu>.md` (`NNNN` = baton `seq`). Eski dosya düzenlenmez/silinmez.
6. İşi yap, testleri **kendin** koş, kanıtı `evidence.jsonl`'a işle.
7. Baton'u güncelle (`seq` +1), commit et (kendi kimliğinle), push et. Push edilemiyorsa bunu yaz ve `git bundle` çıktısını proje sahibine ver.

## Talk dosyası zorunlu bölümleri

Frontmatter (`message_id, seq, from, to, task_id, type, status, in_reply_to, timestamp`) + Konuşma (karakter) + Teknik özet + Çalışanlar + Yaramayanlar + Kanıt + Karşı ajandan beklenen aksiyon + Devir notu. Teknik özet/Yaramayanlar/Kanıt boş geçilemez ("yok" ise nedeniyle).

## Yasaklar (özet)

- Başka ajan adına tur/inceleme/yanıt yazmak.
- Test koşmadan "geçti" demek; kanıtsız durumu `VERIFIED` işaretlemek.
- Secret/token/parola/kişisel veriyi repoya, talk dosyasına veya rapora yazmak.
- Aynı dosyaya koordinasyonsuz (lease çakışmasıyla) iki ajanın dokunması.
- Push edemeyip etmiş gibi davranmak; olmayan GitHub Issue/PR/CI sonucuna referans vermek.

## Çelişki notu (kurulumda tespit edildi)

`task.md` 6.3 ilk baton için `holder: ikinci ajan` der; 4.4 ise karşı ajan doğrulanmadan baton devredilemez der. Kurulum çözümü: ilk baton 6.3'e göre `holder: SOKAK, verified_peer: null` kuruldu, ancak bu bir **davet durumudur**; doğrulama tamamlanana kadar hiçbir görev `VERIFIED` olamaz ve ortak karar alınmış sayılmaz. Ayrıntı: `docs/DECISIONS.md` D-004. Nihai yorum proje sahibine aittir.
