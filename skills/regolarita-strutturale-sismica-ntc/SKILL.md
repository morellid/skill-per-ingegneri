---
name: regolarita-strutturale-sismica-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della valutazione della regolarita' di una costruzione in pianta e in altezza ai fini della progettazione sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.2.1, e delle sue conseguenze sul metodo di analisi e sul fattore di comportamento (paragrafi 7.3.1 e 7.3.3.1). Aiuta a inquadrare i criteri di regolarita' in pianta (masse e rigidezze approssimativamente simmetriche rispetto a due direzioni ortogonali e forma in pianta compatta con contorno convesso, rientranze ammesse se l'area tra perimetro e linea convessa circoscritta non supera il 5% dell'orizzontamento; rapporto tra i lati del rettangolo circoscritto inferiore a 4; orizzontamento rigido nel proprio piano - diaframma rigido - con resistenza sufficiente); i criteri di regolarita' in altezza (sistemi resistenti alle azioni orizzontali estesi per tutta l'altezza; massa e rigidezza costanti o graduali con variazioni di massa non superiori al 25% e rigidezza che non si riduce piu' del 30% ne' aumenta piu' del 10% da un orizzontamento al sovrastante; rapporto capacita'/domanda allo SLV che non differisce piu' del 30% tra orizzontamenti adiacenti; restringimenti con continuita' con rientro non superiore al 10% della dimensione sottostante ne' al 30% del primo orizzontamento); i casi particolari (struttura scatolare rigida alla base con controlli riferiti alla sola struttura soprastante; ponti al paragrafo 7.9.2.1); e le conseguenze della (ir)regolarita' in altezza sul fattore di comportamento (fattore KR uguale a 1 per costruzioni regolari in altezza e 0,8 per costruzioni non regolari in altezza, con q_lim = q0 per KR - paragrafo 7.3.1) e sul metodo di analisi (l'analisi lineare statica e' applicabile solo se il periodo T1 non supera 2,5 TC o TD e la costruzione e' regolare in altezza - paragrafo 7.3.3.1). Use when a structural designer must frame the assessment of structural regularity in plan and elevation of a building under the Italian NTC 2018 par. 7.2.1 and its consequences on the analysis method and behaviour factor; it is a documentary aid and does NOT compute the structure nor run the analysis, does NOT determine q0 (Tab. 7.3.II) nor the ductility classes (par. 7.2.2), does NOT compute T1 (par. 7.3.3.2) nor cover bridge regularity (par. 7.9.2.1), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Regolarità strutturale in pianta e in altezza (NTC 2018 par. 7.2.1)"
summary: "Inquadra la regolarita' strutturale in pianta e in altezza (NTC 2018 par. 7.2.1): criteri a-c (pianta) e d-g (altezza) con le soglie, e conseguenze su fattore di comportamento (KR = 1 o 0,8) e metodo di analisi (analisi statica solo se regolare in altezza e T1 <= 2,5 TC o TD)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.2.1: regolarita' in pianta (a-c) e in altezza (d-g) con le soglie (rientranze 5%, lati < 4, massa 25%, rigidezza 30/10, capacita'/domanda 30, rientri 10/30)"
  - "NTC 2018 - par. 7.3.1 (KR = 1 regolare / 0,8 non regolare in altezza, q_lim = q0 x KR) e par. 7.3.3.1 (analisi lineare statica se T1 <= 2,5 TC o TD e regolare in altezza)"
version: 0.1.0-alpha
status: alpha
tags:
  - regolarita-strutturale
  - progettazione-sismica
  - fattore-di-comportamento
  - ntc-2018
  - metodo-di-analisi
---

# Regolarità strutturale in pianta e in altezza (NTC 2018 par. 7.2.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare la valutazione della regolarità** di una
costruzione **in pianta e in altezza** ai fini della progettazione sismica secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 7.2.1**, e trarne le conseguenze sul **metodo di analisi** e sul **fattore di comportamento**
(§7.3):

- **criteri di regolarità in pianta** (§7.2.1, a-c);
- **criteri di regolarità in altezza** (§7.2.1, d-g);
- **conseguenze** su fattore di comportamento (§7.3.1) e metodo di analisi (§7.3.3.1).

**Non è** uno strumento che calcola la struttura o esegue l'analisi: è un **supporto documentale** che inquadra i
criteri di regolarità e le loro conseguenze. Complementa `spettro-risposta-ntc` (§3.2), `periodo-proprio-t1-ntc`
(§7.3.3.2, stima di T1) e `combinazioni-carico-ntc` (§2.5.3).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-regolarita-pianta-altezza` | Criteri di regolarità in pianta (a-c) e in altezza (d-g) con le relative soglie, struttura scatolare, rinvio ponti (§7.2.1) |
| `inquadra-conseguenze-regolarita` | Conseguenze sulla regolarità in altezza: fattore KR = 1 o 0,8 sul fattore di comportamento (§7.3.1) e ammissibilità dell'analisi lineare statica (§7.3.3.1) |

## Punti chiave (verificati sul testo)

- **Regolare in pianta** (§7.2.1, tutte le a-c): (a) masse/rigidezze **simmetriche** su due direzioni ortogonali
  e forma **compatta** (contorno convesso; rientranze ≤ **5%** dell'orizzontamento); (b) **rapporto tra i lati**
  del rettangolo circoscritto **< 4**; (c) **diaframma rigido**.
- **Regolare in altezza** (§7.2.1, tutte le d-g): (d) sistemi resistenti **estesi per tutta l'altezza**;
  (e) massa/rigidezza costanti o graduali (**massa ≤ 25%**, **rigidezza −30%/+10%** tra piani); (f) rapporto
  **capacità/domanda SLV** entro **30%** tra piani adiacenti; (g) **restringimenti** ≤ **10%** (rispetto al piano
  sottostante) e ≤ **30%** (rispetto al primo orizzontamento).
- **Casi particolari** (§7.2.1): **struttura scatolare rigida** → controlli riferiti alla sola struttura
  soprastante; **ponti** → §7.9.2.1.
- **Conseguenze**: **KR** sul fattore di comportamento (§7.3.1): **1** se regolare in altezza, **0,8** se non
  regolare (q_lim = q0·KR). **Analisi lineare statica** (§7.3.3.1): ammessa solo se **T1 ≤ 2,5 TC o TD** **e**
  regolare in altezza.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.1** (regolarità) e **par. 7.3.1/7.3.3.1** (conseguenze) -
  testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256
  `dda1e397...`), estratto con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** la struttura né **esegue** l'analisi; **non** determina **q0** (Tab. 7.3.II) né le classi di
  duttilità (§7.2.2); **non** calcola **T1** (§7.3.3.2, skill `periodo-proprio-t1-ntc`).
- **Non tratta** la **regolarità dei ponti** (§7.9.2.1).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.2.1 delle NTC 2018 e della Circolare applicativa.**
