# oktobe — Futures Scanner / Order-Flow Terminal

Binance USDⓈ-M Futures public piyasa verisiyle çalışan, mobil öncelikli **Futures Scanner ve Order-Flow Terminal**'in sıfırdan yeniden geliştirmesi. Ürün tanımı ve kabul ölçütleri: [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md). Çalışma protokolü: [`task.md`](task.md) ve [`AGENTS.md`](AGENTS.md).

> **Dürüst durum (2026-10-13):** Bu repo şu an **kurulum aşamasındadır; ürün kodu yoktur ve canlı özellik iddia edilmez.** İki açık kapı vardır: (1) referans uygulama `index (30).html` repoda olmadığı için parity denetimi blokludur, (2) ikinci ajan (SOKAK) henüz kendi kimliğiyle yanıt vermediği için hiçbir görev `VERIFIED` değildir. Ayrıntılar: [`docs/STATUS.md`](docs/STATUS.md), [`docs/PROJECT_AUDIT.md`](docs/PROJECT_AUDIT.md).

## İlkeler

- Mock/sahte piyasa verisi canlı veri gibi sunulmaz; bağlantı ve veri yaşı her zaman gerçek gösterilir.
- Binance API anahtarı gerekmez ve istenmez; kapsam yalnızca public market data'dır, emir gönderimi yoktur.
- "Tamamlandı" yalnızca kod + test + taze kanıt (`/.agent/evidence.jsonl`) birlikteyken söylenir.

## Şu an çalıştırılabilenler

Uygulama yığını mimari kararla (`docs/DECISIONS.md`, TASK-006) kilitlenecektir; şu an yalnızca takım protokolü araçları çalışır:

```bash
python3 scripts/validate-protocol.py       # baton/görev/konuşma/kanıt tutarlılığı
python3 -m unittest discover -s tests -v   # doğrulayıcı birim testleri
```

## Belgeler

| Belge | İçerik |
|---|---|
| `docs/PROJECT_AUDIT.md` | Mevcut durum, bağlantı gerçekliği, riskler |
| `docs/ARCHITECTURE.md` | Hedef mimari (taslak — karşı inceleme bekliyor) |
| `docs/FEATURE_PARITY.md` | Referans eşleşme matrisi |
| `docs/AGENT_CAPABILITIES.md` | Ajanların doğrulanmış yetenekleri |
| `docs/DECISIONS.md` | Karar kayıtları |
| `docs/TASK_PLAN.md` · `docs/TEST_STRATEGY.md` · `docs/SECURITY.md` · `docs/RELEASE_PLAN.md` | Planlar ve standartlar |
| `docs/OPEN_QUESTIONS.md` | Proje sahibinden beklenen girdiler |
| `docs/talk/` | Ajanlar arası konuşma dosyaları (eklemeli, düzenlenmez) |
| `.agent/` | `baton.json` (sıra), `tasks.json` (görevler), `evidence.jsonl` (kanıtlar), `attempts.jsonl` (denemeler) |
