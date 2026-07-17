---
name: denuncia-collaudo-statico-ca-dpr380
description: "Supporto documentale al progettista strutturale, al direttore dei lavori e al collaudatore statico per le opere in conglomerato cementizio armato, normale e precompresso, ed a struttura metallica, ai sensi del D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia), Parte II, Capo I, artt. 64-67. Aiuta a inquadrare i soggetti e le responsabilita': progetto esecutivo e direzione affidati a un tecnico abilitato iscritto all'albo, con la responsabilita' diretta del progettista sulle strutture e quella del direttore dei lavori e del costruttore sulla rispondenza al progetto, sui materiali e sulla posa in opera (art. 64); la denuncia dei lavori presentata dal costruttore allo sportello unico tramite PEC prima dell'inizio, con l'indicazione di committente, progettista, direttore dei lavori e costruttore e con allegati il progetto firmato e la relazione sui materiali, la denuncia delle varianti, la relazione a struttura ultimata depositata dal direttore dei lavori entro sessanta giorni con i certificati dei laboratori dell'articolo 59, i dati del precompresso e le prove di carico, l'attestazione di deposito e la trasmissione all'ufficio tecnico regionale (art. 65); i documenti da conservare in cantiere e il giornale dei lavori vistato dal direttore dei lavori (art. 66); il collaudo statico obbligatorio per le costruzioni che interessano la pubblica incolumita', eseguito da un ingegnere o architetto iscritto all'albo da almeno dieci anni e non intervenuto nella progettazione, direzione o esecuzione, la nomina contestuale alla denuncia, la terna dell'ordine quando il costruttore esegue in proprio, i sessanta giorni per il collaudo dopo la copertura, il certificato di collaudo inviato via PEC ed equivalente al certificato di rispondenza alle norme tecniche dell'articolo 62, e la dichiarazione di regolare esecuzione del direttore dei lavori che sostituisce il collaudo per gli interventi di riparazione e locali (art. 67). Use when a structural designer, works supervisor, or static tester must frame the works notification, the on-site documents, the as-built report, or the static testing of reinforced-concrete, prestressed, or steel structures under DPR 380/2001; it is a documentary aid and does NOT draft the structural design, the report, or the test certificate, does NOT perform the calculation or the testing, does NOT reproduce the NTC 2018 or articles 53/59/62/94-bis, and does NOT replace the qualified engineer, the works supervisor, the tester, or the competent offices."
license: MIT
area: strutture-geotecnica
title: "Denuncia dei lavori e collaudo statico opere in c.a. (DPR 380/2001)"
summary: "Inquadra gli adempimenti su opere c.a./c.a.p. e acciaio (DPR 380/2001 artt. 64-67): denuncia dei lavori allo sportello unico via PEC (65), documenti in cantiere (66), relazione a struttura ultimata e collaudo statico da ingegnere/architetto iscritto da 10 anni (67). Non redige."
normative_refs:
  - "D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia) - Parte II, Capo I, artt. 64-67: responsabilita' (64), denuncia dei lavori (65), documenti in cantiere (66), collaudo statico (67)"
  - "Rinvio (non riprodotti): artt. 53 (opere soggette), 59 (laboratori prove), 62 (rispondenza NTC), 94-bis (interventi) DPR 380/2001; NTC 2018 (D.M. 17/1/2018)"
version: 0.1.0-alpha
status: alpha
tags:
  - collaudo-statico
  - denuncia-lavori-strutture
  - cemento-armato
  - dpr-380-2001
  - direttore-lavori
---

# Denuncia dei lavori e collaudo statico - opere in c.a./c.a.p. e acciaio (DPR 380/2001 artt. 64-67)

## Quando usare questa skill

Usala quando un **progettista strutturale**, un **direttore dei lavori** o un **collaudatore statico**
deve **inquadrare** gli adempimenti sulle **opere in conglomerato cementizio armato** (normale e
precompresso) **e a struttura metallica**, secondo il **D.P.R. 6 giugno 2001, n. 380** (Testo unico
edilizia), **Parte II, Capo I, artt. 64-67**:

- **soggetti e responsabilità** di progettista, direttore dei lavori e costruttore (art. 64);
- **denuncia dei lavori** allo sportello unico via PEC, allegati e **varianti** (art. 65, cc. 1-5);
- **documenti in cantiere** e **giornale dei lavori** (art. 66);
- **relazione a struttura ultimata** entro 60 giorni (art. 65, cc. 6-8);
- **collaudo statico**: obbligo, **collaudatore** indipendente iscritto da 10 anni, nomina, termini e
  certificato (art. 67).

**Non è** uno strumento che redige il progetto, la relazione o il certificato di collaudo, né esegue il
calcolo o il collaudo: è un **supporto documentale** che inquadra obblighi, soggetti, documenti e
termini.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-denuncia-lavori` | Inquadra soggetti e responsabilità (art. 64), la denuncia allo sportello unico con allegati e varianti (art. 65 cc. 1-5), i documenti in cantiere (art. 66) e la relazione a struttura ultimata (art. 65 cc. 6-8) |
| `inquadra-collaudo-statico` | Inquadra obbligo, requisiti e indipendenza del collaudatore, nomina, termini, certificato di collaudo e i casi di dichiarazione di regolare esecuzione (art. 67) |

## Punti chiave (verificati sul testo)

- **Soggetti** (art. 64): progetto esecutivo e direzione a **tecnico abilitato iscritto all'albo**;
  responsabilità diretta del **progettista** sulle strutture (c. 4); **direttore dei lavori** e
  **costruttore** rispondono di rispondenza al progetto, materiali e posa in opera (c. 5).
- **Denuncia** (art. 65): dal **costruttore** allo **sportello unico** via **PEC** prima dell'inizio,
  con **progetto** e **relazione sui materiali** (c. 3); varianti prima dell'esecuzione (c. 5).
- **Relazione a struttura ultimata** (art. 65, cc. 6-8): dal **direttore dei lavori** entro **60
  giorni**, con certificati dei laboratori **art. 59**, dati del c.a.p. e prove di carico; consegnata
  anche al collaudatore.
- **Documenti in cantiere** (art. 66): atti dell'art. 65 + **giornale dei lavori**, sotto la
  responsabilità del direttore dei lavori.
- **Collaudo statico** (art. 67): **obbligatorio** (c. 1); **ingegnere/architetto iscritto da 10 anni**
  e **indipendente** (c. 2); **nomina** contestuale alla denuncia (c. 3) o **terna** dell'ordine (c.
  4); **60 giorni** dalla copertura (c. 5); **certificato** via PEC, equivalente al certificato di
  rispondenza NTC (art. 62, c. 7). Per **interventi locali/riparazioni** vale la **dichiarazione di
  regolare esecuzione** del DL (cc. 8-bis, 8-ter).

## Fonti

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - Parte II, Capo I, **artt. 64-67** - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429, idGruppo 12).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il progetto strutturale, la relazione o il certificato di collaudo; **non esegue** il
  calcolo di resistenza/stabilità né il collaudo.
- **Non riproduce** le **NTC 2018** (D.M. 17/1/2018) né gli artt. 53/59/62/94-bis se non nei richiami.
- **Non tratta** la disciplina sismica (artt. 93-94, skill `denuncia-autorizzazione-sismica-dpr380`) se
  non nei rimandi.

**La skill è un supporto documentale: non sostituisce il tecnico abilitato, il direttore dei lavori, il
collaudatore o gli uffici competenti, né la lettura degli artt. 64-67 del D.P.R. 380/2001 e delle NTC.**
