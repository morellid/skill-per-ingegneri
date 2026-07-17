# servitu-coattive-prediali-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / CTU da completare)

Skill di **supporto documentale** per il **tecnico** (ingegnere, geometra, **CTU/CTP**) nei
compiti tecnici legati alle **servitù prediali coattive** (passaggio, acquedotto, elettrodotto):
verificare l'**interclusione**, individuare il **tracciato/la localizzazione** dell'accesso o della
conduttura con i criteri di legge (accesso più breve e minor danno, sottopassaggio, veicoli) e
fornire la **base tecnica dell'indennità**, secondo il **Codice civile (R.D. 262/1942), Libro III,
Titolo VI**.

**Non dà consulenza legale**, **non redige** atti o domande giudiziali, **non quantifica**
l'indennità (è l'oggetto della stima) e **non sostituisce** l'avvocato o il giudice: inquadra
presupposti, criteri di localizzazione e base dell'indennità a supporto del tecnico.

## Target

Ingegneri, geometri e tecnici incaricati (CTU nominati dal giudice, CTP di parte) chiamati a
localizzare l'accesso/la conduttura o a fornire la base tecnica dell'indennità.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-passaggio-coattivo` | Verifica i presupposti del passaggio coattivo (fondo intercluso art. 1051 o non intercluso art. 1052), i criteri di localizzazione, l'indennità (art. 1053) e la cessazione (art. 1055) |
| `inquadra-servitu-acque-elettrodotto` | Inquadra l'acquedotto coattivo (art. 1033), l'elettrodotto coattivo (art. 1056) e le vie funicolari (art. 1057), con costituzione e indennità (artt. 1031-1032) |

Nucleo: **nozione** (art. 1027); **costituzione** coattiva con sentenza, modalità e
indennità (artt. 1031-1032); **acquedotto coattivo** (art. 1033); **passaggio coattivo**
del fondo intercluso e non intercluso (artt. 1051-1052); **indennità** (art. 1053);
**cessazione** (art. 1055); **elettrodotto** (art. 1056) e **vie funicolari** (art. 1057).

## Fonti consultate

- **Codice civile (R.D. 16/3/1942 n. 262)** - Libro III, Titolo VI - artt. 1027, 1031,
  1032, 1033, 1051, 1052, 1053, 1055, 1056, 1057 - testo vigente su Normattiva (indice
  pinnato a `!vig=2026-07-17`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** atti costitutivi né domande giudiziali.
- **Non quantifica** l'indennità (art. 1053, che rinvia all'art. 1038): la inquadra.
- **Non riproduce** le leggi speciali su acque (R.D. 1775/1933) ed elettrodotti richiamate
  dagli artt. 1033/1056/1057.
- **Non tratta** la servitù di elettrodotto **amministrativa** (asservimento espropriativo,
  DPR 327/2001) né le **distanze legali** (artt. 873 ss.).
- **Non sostituisce** l'avvocato né il CTU.

**La skill è un supporto documentale: non sostituisce l'avvocato, il CTU, né la lettura
degli articoli del Codice civile e delle leggi speciali richiamate.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
