# valutazione-rischio-biologico-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RSPP / tecnico della sicurezza o medico competente da completare)

Skill di **supporto documentale** al **RSPP/ASPP**, al **datore di lavoro** e al **tecnico della
sicurezza** per l'inquadramento della **valutazione e gestione del rischio da esposizione ad agenti
biologici** ai sensi del **D.Lgs. 9 aprile 2008, n. 81, Titolo X (artt. 266-280)**.

**Non redige** il DVR né la valutazione del rischio, **non classifica** i singoli agenti e **non
sostituisce** il datore di lavoro, l'RSPP o il medico competente: inquadra definizioni, classificazione,
obblighi e adempimenti.

## Target

RSPP/ASPP, datori di lavoro, tecnici della sicurezza e dell'igiene industriale (sanità, laboratori,
depurazione, zootecnia, ecc.) che devono inquadrare la valutazione e la gestione del rischio da agenti
biologici.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classificazione-valutazione-biologico` | Campo, definizioni, classificazione in 4 gruppi, valutazione del rischio e misure tecniche/igieniche (artt. 266-273) |
| `inquadra-sorveglianza-registro-biologico` | Sorveglianza sanitaria (vaccini, allontanamento) e registro degli esposti e degli eventi accidentali (artt. 279-280) |

Nucleo: **definizioni** e **classificazione** in 4 gruppi (artt. 267-268), **valutazione del rischio** e
integrazione del DVR (art. 271), **misure** tecniche e igieniche (artt. 272-273), **sorveglianza
sanitaria** (art. 279) e **registro degli esposti** dei gruppi 3/4 (art. 280).

## Fonti consultate

- **D.Lgs. 9 aprile 2008, n. 81** - Titolo X, artt. 266-280 - testo vigente su Normattiva (indice pinnato
  a `!vig=2026-07-17`, codice 008G0104).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il DVR né la valutazione del rischio; **non classifica** i singoli agenti biologici.
- **Non riproduce** gli **Allegati XLIV/XLV/XLVI** né definisce i **livelli di contenimento** (artt.
  274-275).
- **Non tratta** gli **agenti chimici** (Titolo IX Capo I, skill `valutazione-rischio-chimico-dlgs81`) né
  i **cancerogeni/mutageni** (Titolo IX Capo II, skill `valutazione-rischio-cancerogeni-mutageni-dlgs81`),
  se non nei richiami.

**La skill è un supporto documentale: non sostituisce il datore di lavoro, l'RSPP o il medico competente,
né la lettura degli artt. 266-280 del D.Lgs. 81/2008 e dei relativi allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
