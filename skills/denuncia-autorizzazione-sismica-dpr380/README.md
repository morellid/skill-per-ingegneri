# denuncia-autorizzazione-sismica-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista/ufficio sismica da completare)

Skill di **supporto documentale** agli adempimenti per le **costruzioni in zone sismiche**:
denuncia dei lavori e deposito del progetto (art. 93), autorizzazione preventiva all'inizio
dei lavori (art. 94) e classificazione degli interventi strutturali rilevanti/di minore
rilevanza/privi di rilevanza (art. 94-bis), secondo il **DPR 380/2001**, Parte II, Capo IV.

**Non redige** la denuncia/istanza né il progetto strutturale, **non esegue** calcoli (NTC),
**non riproduce** le linee guida MIT/regionali e **non sostituisce** l'ufficio tecnico
regionale o il SUE: inquadra gli adempimenti e la classificazione.

## Target

Progettisti, direttori dei lavori, uffici tecnici regionali, SUE.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-denuncia-autorizzazione` | Imposta il preavviso/denuncia e il deposito del progetto (art. 93) e verifica se serve l'autorizzazione preventiva (art. 94) |
| `classifica-intervento-sismico` | Classifica l'intervento come rilevante, di minore rilevanza o privo di rilevanza (art. 94-bis) e ne deduce il regime |

Nucleo: **denuncia/deposito** del progetto asseverato allo sportello unico (sempre in zona
sismica, art. 93); **autorizzazione preventiva** dell'ufficio tecnico regionale con termine
di 30 giorni e silenzio assenso (art. 94); **classificazione** in interventi rilevanti/minore
rilevanza/privi di rilevanza per zona sismica e regime conseguente (art. 94-bis).

## Fonti consultate

- **D.P.R. 6/6/2001 n. 380** (Testo unico edilizia) - Parte II, Capo IV - artt. 93, 94,
  94-bis - testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la denuncia/istanza, l'asseverazione né il progetto strutturale.
- **Non esegue** calcoli strutturali/sismici (NTC, DM 17/1/2018): rinvio alle skill NTC.
- **Non riproduce** le linee guida MIT (DM 30/4/2018) né le elencazioni/procedure regionali.
- **Non tratta** la denuncia delle opere in c.a./acciaio (art. 65, skill
  `denuncia-opere-strutturali-l1086`).
- **Non individua** la classificazione sismica del sito (zona 1-4, art. 83): dato di fatto.
- **Non sostituisce** l'ufficio tecnico regionale né il SUE.

**La skill è un supporto documentale: non sostituisce il progettista/direttore dei lavori,
l'ufficio tecnico regionale, il SUE, né la lettura degli artt. 93, 94, 94-bis del DPR
380/2001, delle NTC e delle disposizioni regionali.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
