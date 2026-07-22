---
name: criteri-modellazione-sismica-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento dei criteri di modellazione della struttura e dell'azione sismica ai fini della progettazione sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.2.6. Aiuta a inquadrare la modellazione della struttura (modello tridimensionale che rappresenti masse, rigidezza e resistenza, con attenzione alle forze d'inerzia verticali su travi di grande luce e sbalzi; leggi costitutive elastiche per comportamento non dissipativo o dissipativo con coefficiente di comportamento q; considerazione della fessurazione con rigidezza flessionale e a taglio di elementi in muratura, calcestruzzo armato e acciaio-calcestruzzo riducibile sino al 50% di quella dei corrispondenti elementi non fessurati; orizzontamenti considerabili infinitamente rigidi nel piano medio se in calcestruzzo armato, oppure in latero-cemento con soletta in c.a. di almeno 40 mm o in struttura mista con soletta in c.a. di almeno 50 mm collegata da connettori a taglio; elementi non strutturali non collaboranti, come tamponature e tramezzi, rappresentati unicamente in termini di massa, con contributo di rigidezza e resistenza considerato solo se ha effetti negativi sulla sicurezza) e la modellazione dell'azione sismica (forze statiche equivalenti, spettri di risposta o storie temporali; con analisi di risposta sismica locale o di interazione terreno-struttura lo spettro con 5% di smorzamento deve essere almeno pari al 70% di quello per sottosuolo di tipo A e la risultante di taglio e sforzo normale alla fondazione almeno pari al 70% di quella a base fissa; divieto di storie temporali artificiali per tali analisi; eccentricita' accidentale del centro di massa non inferiore a 0,05 volte la dimensione media dell'edificio misurata perpendicolarmente alla direzione dell'azione sismica, costante per entita' e direzione su tutti gli orizzontamenti). Use when a structural designer must frame the modelling criteria of the structure and of the seismic action under the Italian NTC 2018 par. 7.2.6; it is a documentary aid and does NOT build the model nor run the analysis, does NOT determine q, does NOT cover the local seismic response (par. 3.2.3.6) nor the piled rafts (par. 6.4.3), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Criteri di modellazione sismica della struttura (NTC 2018 par. 7.2.6)"
summary: "Inquadra i criteri di modellazione sismica (NTC 2018 par. 7.2.6): modello 3D, rigidezza fessurata sino al 50%, orizzontamenti rigidi (soletta c.a. 40/50 mm), elementi non strutturali come massa, eccentricita' accidentale >= 0,05 della dimensione media perpendicolare."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.2.6: modello 3D, rigidezza fessurata sino al 50%, orizzontamenti rigidi (c.a., soletta 40/50 mm), elementi non strutturali come massa"
  - "NTC 2018 - par. 7.2.6: azione sismica (forze/spettri/storie), risposta sismica locale e ITS >= 70% (5% smorzamento), eccentricita' accidentale >= 0,05 della dimensione media perpendicolare"
version: 0.1.0-alpha
status: alpha
tags:
  - modellazione-strutturale
  - progettazione-sismica
  - eccentricita-accidentale
  - ntc-2018
  - rigidezza-fessurata
---

# Criteri di modellazione della struttura e dell'azione sismica (NTC 2018 par. 7.2.6)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **impostare il modello di calcolo** di una costruzione ai fini
della progettazione sismica secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.2.6**:

- **modellazione della struttura** (modello 3D, rigidezza fessurata, orizzontamenti, elementi non strutturali);
- **modellazione dell'azione sismica** (spettri/storie, interazione terreno-struttura, eccentricità accidentale).

**Non è** uno strumento che costruisce il modello o esegue l'analisi: è un **supporto documentale** che inquadra i
criteri di modellazione. Complementa `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc`
(§7.3.6.1), `periodo-proprio-t1-ntc` (§7.3.3.2) e `spettro-risposta-ntc` (§3.2).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-modellazione-struttura` | Modello 3D, leggi costitutive, rigidezza fessurata (sino al 50%), orizzontamenti rigidi (soletta c.a. 40/50 mm), elementi non strutturali come massa (§7.2.6) |
| `inquadra-modellazione-azione-sismica` | Rappresentazione dell'azione (forze/spettri/storie), limiti 70% per RSL/ITS (5% smorzamento), eccentricità accidentale ≥ 0,05 della dimensione media (§7.2.6) |

## Punti chiave (verificati sul testo)

- **Struttura** (§7.2.6): modello **tridimensionale** (attenzione a forze d'inerzia verticali su travi di grande
  luce/sbalzi); **leggi costitutive elastiche** per comportamento non dissipativo o dissipativo con q; **rigidezza
  fessurata** riducibile **sino al 50%** di quella non fessurata (muratura, c.a., acciaio-cls); **orizzontamenti
  infinitamente rigidi** se c.a., latero-cemento con soletta c.a. **≥ 40 mm** o mista con soletta c.a. **≥ 50 mm**
  con connettori a taglio; **elementi non strutturali** non collaboranti (tamponature, tramezzi) **solo in massa**
  (rigidezza/resistenza solo se effetti negativi).
- **Azione sismica** (§7.2.6): forze statiche equivalenti, spettri o storie temporali; con **RSL/interazione
  terreno-struttura** lo spettro (5% smorzamento) **≥ 70%** di quello per sottosuolo A e taglio/normale alla
  fondazione **≥ 70%** di quello a base fissa; **eccentricità accidentale** ≥ **0,05** × dimensione media
  perpendicolare all'azione, **costante** su tutti gli orizzontamenti.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non costruisce** il modello né **esegue** l'analisi (metodi al §7.3); **non** determina **q**.
- **Non tratta** la **risposta sismica locale** (§3.2.3.6) né le **fondazioni miste** (§6.4.3).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.2.6 delle NTC 2018 e della Circolare applicativa.**
