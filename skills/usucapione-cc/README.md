# usucapione-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / CTU da completare)

Skill di **supporto documentale** all'inquadramento dell'**usucapione** (acquisto della
proprietà e dei diritti reali di godimento per possesso continuato): termini per tipo di
bene, usucapione ordinaria e abbreviata, requisiti del possesso, rapporto con la
prescrizione e interruzione, secondo il **Codice civile (R.D. 262/1942), Libro III, Titolo
VIII (artt. 1158-1167)**.

**Non redige** atti o domande giudiziali, **non gestisce** la mediazione, **non valuta** in
concreto il possesso e **non sostituisce** l'avvocato o il CTU: inquadra presupposti e
termini.

## Target

Tecnici, geometri, avvocati, CTU.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-usucapione` | Determina il tipo di usucapione e il termine (immobili/mobili/registrati/universalità, ordinaria vs abbreviata) in base a bene, buona fede, titolo e trascrizione (artt. 1158-1162) |
| `verifica-requisiti-possesso` | Verifica i requisiti del possesso (non vizioso, interversione), l'applicazione delle norme sulla prescrizione e l'interruzione (artt. 1163-1167) |

Nucleo: **immobili** 20 anni ordinaria (1158) / 10 anni abbreviata (1159); **piccola
proprietà rurale** 15/5 anni (1159-bis); **universalità e beni mobili/registrati**
(1160-1162); **vizi e interversione** del possesso (1163-1164); **prescrizione e
interruzione** (1165-1167).

## Fonti consultate

- **Codice civile (R.D. 16/3/1942 n. 262)** - Libro III, Titolo VIII - artt. 1158-1167 -
  testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** atti o domande giudiziali di accertamento dell'usucapione.
- **Non gestisce** la mediazione ex art. 5 D.Lgs. 28/2010 (skill
  `mediazione-civile-conciliazione-dlgs28`).
- **Non valuta** in concreto il possesso ad usucapionem (continuità, animus, buona fede).
- **Non riproduce** le norme sulla prescrizione (artt. 2934 ss., 2942) né la legge speciale
  sulla piccola proprietà rurale.
- **Non sostituisce** l'avvocato né il CTU.

**La skill è un supporto documentale: non sostituisce l'avvocato, il CTU, né la lettura degli
articoli del Codice civile sull'usucapione e delle norme sulla prescrizione.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
