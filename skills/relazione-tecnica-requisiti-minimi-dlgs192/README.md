# relazione-tecnica-requisiti-minimi-dlgs192

> Versione: 0.2.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con termotecnico / certificatore energetico da completare)

Skill di **supporto documentale** per il **tecnico** (progettista, direttore dei lavori) sulla
**relazione tecnica di progetto attestante la rispondenza ai requisiti minimi di contenimento dei
consumi energetici** (la storica **"relazione ex legge 10"**), ai sensi del **D.Lgs. 19 agosto 2005,
n. 192, art. 8** (con le sanzioni dell'art. 15).

**Non redige la relazione** né esegue i calcoli/verifiche e **non sostituisce** il progettista né il
direttore dei lavori: inquadra l'adempimento e la sua collocazione procedurale.

## Target

Ingegneri e architetti che, come progettisti o direttori dei lavori, devono predisporre, depositare
e asseverare la relazione tecnica energetica di un intervento edilizio/impiantistico.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-relazione-deposito` | Stabilisce se la relazione è dovuta, chi la redige, cosa contiene (incl. sistemi alternativi) e come/quando si deposita (art. 8 cc. 1, 1-bis) |
| `inquadra-asseverazione-sanzioni` | Inquadra l'asseverazione del DL a fine lavori, i controlli del Comune e le sanzioni a professionista e DL (art. 8 cc. 2-5; art. 15 cc. 1, 3, 4) |
| `verifica-obblighi-fer-edifici` | Stabilisce se e in che misura scattano gli obblighi FER dell'Allegato III del D.Lgs. 199/2021 modificato dal D.Lgs. 5/2026, e cosa deve contenere la relazione di conseguenza |

Nucleo: **chi redige e cosa contiene** la relazione, **deposito** in doppia copia con la DIA/titolo
(art. 8 c. 1), **esclusioni** (PdC ≤ 15 kW; sostituzione generatore sotto soglia DM 37/2008),
**sistemi alternativi** ad alta efficienza (c. 1-bis), **obblighi FER** dell'Allegato III del D.Lgs.
199/2021 come modificato dal **D.Lgs. 5/2026** (RED III) - quote 60/40/15/15% secondo la categoria di
intervento, maggiorazione per edifici pubblici, potenza elettrica minima, esonero per
teleriscaldamento efficiente, deroga motivata in relazione, trasmissione di copia al GSE -,
**asseverazione + AQE** del direttore dei lavori a fine lavori (c. 2), **controlli** del Comune
(cc. 3-5), **sanzioni** al professionista (700-4200 €) e al DL (1000-6000 €) - art. 15.

## Fonti consultate

- **D.Lgs. 19 agosto 2005, n. 192** - artt. 8, 15 - testo vigente su Normattiva (indice pinnato a
  `!vig=2026-07-17`, codice 005G0219)
- **D.Lgs. 9 gennaio 2026, n. 5** (RED III) - artt. 29-30 e Allegato III del D.Lgs. 199/2021
  risultante - GU Serie generale n. 15 del 20 gennaio 2026 (codice 26G00018)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la relazione tecnica né l'asseverazione/AQE; **non esegue** i calcoli/verifiche
  energetiche (rinvio a `trasmittanza-termica-opache-dm2015` e al DM 26/6/2015).
- **Non riproduce** gli schemi di relazione del decreto attuativo MiSE né i requisiti numerici del DM
  26/6/2015.
- **Non qualifica** l'intervento come ristrutturazione importante di primo o secondo livello o come
  ristrutturazione dell'impianto termico: le definizioni sono nel DM 26/6/2015 come modificato dal DM
  MASE 28/10/2025 (rinvio). La categoria è un **input**, non un output.
- **Non riproduce** l'Allegato II del D.Lgs. 199/2021 (requisiti e specifiche tecniche degli impianti
  FER), il resto dell'Allegato IV (requisiti minimi di prodotto) né le linee guida CTI previste dalla
  Sezione C punto 4. La **formula** della potenza elettrica FER è pubblicata come immagine in
  Gazzetta e va letta sull'originale.
- La **decorrenza** dell'obbligo FER (180 giorni dall'entrata in vigore, cioè 3 agosto 2026 se
  riferiti al D.Lgs. 5/2026) poggia su una formula testualmente ambigua: la skill segnala
  l'incertezza, non la risolve.
- **Non copre** l'APE (art. 6, skill `attestato-prestazione-energetica-dlgs192`), l'esercizio degli
  impianti (art. 7) né i commi 2 e 5-10 dell'art. 15.

**La skill è un supporto documentale: non sostituisce il progettista, il direttore dei lavori né la
lettura dell'art. 8 del D.Lgs. 192/2005 e dei decreti attuativi.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
