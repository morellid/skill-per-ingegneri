---
name: spostamenti-interpiano-sld-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della verifica di deformabilita' allo stato limite di danno (SLD) - i limiti di spostamento di interpiano - degli elementi strutturali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafi 7.3.6 e 7.3.6.1 (verifiche di rigidezza RIG). Aiuta a inquadrare il quadro delle verifiche (Tab. 7.3.III: per gli elementi strutturali primari la verifica di rigidezza si esegue allo SLD per le classi d'uso I e II e allo SLO per le classi d'uso III e IV); i limiti di spostamento di interpiano, con il prodotto tra fattore di comportamento q e spostamento di interpiano dr rapportato all'altezza di piano h: q per dr minore o uguale a 0,0050 h per tamponature fragili collegate rigidamente [7.3.11a], minore o uguale a 0,0075 h per tamponature duttili collegate rigidamente [7.3.11b], minore o uguale a drp e comunque a 0,0100 h per tamponature progettate per non subire danni [7.3.12], minore o uguale a 0,0020 h per muratura ordinaria [7.3.13], minore o uguale a 0,0030 h per muratura armata [7.3.14] e strettamente minore di 0,0025 h per muratura confinata [7.3.15]; la definizione di dr (differenza tra gli spostamenti del solaio superiore e inferiore, calcolati con analisi lineare al paragrafo 7.3.3.3 o non lineare al paragrafo 7.3.4, sul modello di calcolo non comprensivo delle tamponature) e di h (altezza di piano); e le regole di applicazione (per le classi d'uso III e IV, riferite allo SLO, i limiti sono i 2/3 di quelli indicati; in caso di coesistenza di diversi tipi di tamponamento o struttura portante nel medesimo piano si assume il limite piu' restrittivo; se gli spostamenti di interpiano superano 0,005 h le verifiche della capacita' di spostamento si estendono a tutte le tamponature, tramezzature interne e impianti). Use when a structural designer must frame the damage-limit-state (SLD) deformability check - the interstory drift limits - of a building under the Italian NTC 2018 par. 7.3.6.1; it is a documentary aid and does NOT compute the displacements nor run the analysis (par. 7.3.3.3 / 7.3.4), does NOT determine q, does NOT cover the strength (RES) or ductility (DUT) checks nor the non-structural elements (par. 7.3.6.2) and systems (par. 7.3.6.3), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Spostamenti di interpiano allo SLD (NTC 2018 par. 7.3.6.1)"
summary: "Inquadra la verifica di deformabilita' allo SLD (NTC 2018 par. 7.3.6.1): limiti di spostamento di interpiano q*dr/h per tipo di tamponatura/struttura (0,0050/0,0075/0,0100/0,0020/0,0030/0,0025 h), SLD per CU I-II e SLO (2/3) per CU III-IV, dr su modello senza tamponature."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.3.6.1: q*dr <= 0,0050 h (fragili), 0,0075 h (duttili), 0,0100 h (b), 0,0020 h (mur. ordinaria), 0,0030 h (armata), < 0,0025 h (confinata); dr senza tampon."
  - "NTC 2018 - par. 7.3.6 (Tab. 7.3.III): verifica di rigidezza allo SLD per CU I-II, allo SLO per CU III-IV (limiti ai 2/3); coesistenza -> limite piu' restrittivo; dr > 0,005 h -> verifiche estese"
version: 0.1.0-alpha
status: alpha
tags:
  - spostamenti-di-interpiano
  - stato-limite-di-danno
  - progettazione-sismica
  - ntc-2018
  - deformabilita
---

# Spostamenti di interpiano allo SLD (NTC 2018 par. 7.3.6.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare la verifica di deformabilità allo stato limite di
danno (SLD)** - i **limiti di spostamento di interpiano** degli elementi strutturali - secondo le **NTC 2018**
(DM 17 gennaio 2018), **paragrafi 7.3.6 e 7.3.6.1** (verifiche di rigidezza RIG):

- **quadro delle verifiche** e stato limite per classe d'uso (§7.3.6, Tab. 7.3.III);
- **limiti di spostamento di interpiano** [7.3.11a]-[7.3.15] (§7.3.6.1);
- **regole di applicazione** (2/3 per CU III/IV, coesistenza, estensione delle verifiche).

**Non è** uno strumento che calcola gli spostamenti o esegue l'analisi: è un **supporto documentale** che inquadra
i limiti di drift e la loro applicazione. Complementa `regolarita-strutturale-sismica-ntc` (§7.2.1/7.3.1),
`periodo-proprio-t1-ntc` (§7.3.3.2) e `spettro-risposta-ntc` (§3.2).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-limiti-spostamento-interpiano` | I sei limiti [7.3.11a]-[7.3.15] per tipo di tamponatura/struttura, con q, dr (modello senza tamponature) e h (§7.3.6.1) |
| `inquadra-classe-uso-stato-limite` | Stato limite per classe d'uso (SLD per CU I-II, SLO per CU III-IV con limiti ai 2/3), coesistenza ed estensione delle verifiche (§7.3.6, 7.3.6.1) |

## Punti chiave (verificati sul testo)

- **Quadro** (§7.3.6, Tab. 7.3.III): la verifica di **rigidezza (RIG)** degli elementi strutturali si esegue allo
  **SLD** per le **CU I e II** e allo **SLO** per le **CU III e IV**.
- **Limiti di spostamento di interpiano** (§7.3.6.1), con **q·dr** rapportato all'altezza di piano **h**:
  - **q·dr ≤ 0,0050 h** — tamponature **fragili** collegate rigidamente [7.3.11a];
  - **q·dr ≤ 0,0075 h** — tamponature **duttili** collegate rigidamente [7.3.11b];
  - **q·dr ≤ drp ≤ 0,0100 h** — tamponature **progettate per non subire danni** [7.3.12];
  - **q·dr ≤ 0,0020 h** — **muratura ordinaria** [7.3.13];
  - **q·dr ≤ 0,0030 h** — **muratura armata** [7.3.14];
  - **q·dr < 0,0025 h** — **muratura confinata** [7.3.15] (operatore strettamente minore).
- **dr** = differenza tra gli spostamenti del solaio superiore e inferiore (analisi lineare §7.3.3.3 o non lineare
  §7.3.4), su **modello senza tamponature**; **h** = altezza di piano; **q** = fattore di comportamento.
- **Regole**: per **CU III e IV** (SLO) i limiti sono i **2/3**; **coesistenza** nello stesso piano → limite **più
  restrittivo**; se **dr > 0,005 h** (caso b) → verifiche di capacità di spostamento **estese** a tamponature,
  tramezzature e impianti.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.3.6 e 7.3.6.1** - testo del Supplemento Ordinario n. 8 alla
  G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim; i sei limiti e gli operatori (≤ per a-d, < per e) verificati anche sull'immagine della
  pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** gli spostamenti né **esegue** l'analisi (§7.3.3.3 / §7.3.4); **non** determina **q**.
- **Non tratta** le verifiche di **resistenza (RES)** o **duttilità (DUT)** degli elementi strutturali, né quelle
  degli **elementi non strutturali** (§7.3.6.2) e degli **impianti** (§7.3.6.3).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.3.6.1 delle NTC 2018 e della Circolare applicativa.**
