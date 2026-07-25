---
name: metodi-analisi-sismica-ntc
description: "Supporto documentale al progettista strutturale per la scelta e l'impostazione del metodo di analisi sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafi 7.3.2, 7.3.3 e 7.3.4. Aiuta a inquadrare: la scelta tra analisi dinamica e statica del par. 7.3.2 (il metodo di riferimento e' l'analisi modale con spettro di risposta, ossia l'analisi lineare dinamica; l'analisi lineare statica con il metodo delle forze laterali e' ammessa solo se la risposta non dipende significativamente dai modi superiori; in alternativa analisi non lineare dinamica o statica); l'analisi lineare dinamica del par. 7.3.3.1 (considerare tutti i modi con massa partecipante superiore al 5% e un numero di modi con massa totale superiore all'85%, con combinazione quadratica completa CQC e eccentricita' accidentale del centro di massa); l'analisi lineare statica del par. 7.3.3.2 (applicabile se il periodo T1 non supera 2,5 volte TC o TD e la costruzione e' regolare in altezza; forze Fh = Sd(T1) W lambda/g e Fi = Fh zi Wi diviso la somma di zj Wj, con lambda pari a 0,85 se T1 e' minore di 2 TC e ci sono almeno tre orizzontamenti, altrimenti 1,0); la valutazione degli spostamenti del par. 7.3.3.3 (dE = mu_d per dEe, con mu_d pari a q oppure 1+(q-1)TC/T1 e comunque non oltre 5q-4; spostamenti allo SLC pari a 1,25 volte quelli allo SLV); e l'analisi non lineare del par. 7.3.4 (dinamica con integrazione al passo; statica pushover con curva di capacita' Fb-dc, punto di controllo al centro di massa dell'ultimo livello e almeno due distribuzioni di forze, principali del Gruppo 1 con modo fondamentale non inferiore al 75% o distribuzione modale obbligatoria se T1 supera 1,3 TC, e secondarie del Gruppo 2 uniforme, adattiva o multimodale con almeno sei modi). Use when a structural engineer must choose or set up the seismic analysis method (modal response spectrum, lateral force, nonlinear pushover) under the Italian NTC 2018 par. 7.3.2-7.3.4; it is a documentary aid, does NOT run the analysis or the member checks, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Metodi di analisi sismica (NTC 2018 par. 7.3.2-7.3.4)"
summary: "Inquadra la scelta del metodo di analisi sismica (NTC 2018 par. 7.3.2-7.3.4): analisi modale di riferimento (7.3.2), lineare dinamica masse >=85% e CQC (7.3.3.1), lineare statica se T1<=2,5 TC con forze Fh/Fi (7.3.3.2), spostamenti mu_d e pushover con curva di capacita' (7.3.4)."
normative_refs:
  - "NTC 2018 - par. 7.3.2-7.3.3: metodo di riferimento analisi modale; lineare dinamica masse >5% e >=85%, CQC; lineare statica se T1<=2,5 TC, forze Fh e Fi [7.3.7], lambda 0,85/1,0"
  - "NTC 2018 - par. 7.3.3.3-7.3.4: spostamenti mu_d<=5q-4, SLC=1,25 SLV; pushover curva Fb-dc, >=2 distribuzioni (Gruppo 1 >=75% o modale se T1>1,3 TC; Gruppo 2 >=6 modi)"
version: 0.1.0-alpha
status: alpha
tags:
  - analisi-sismica
  - pushover
  - analisi-modale
  - ntc-2018
  - forze-laterali
---

# Metodi di analisi sismica (NTC 2018 par. 7.3.2-7.3.4)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **scegliere e impostare il metodo di analisi sismica** secondo le
**NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.3.2-7.3.4** (Cap. 7):

- **scelta** dinamica/statica e metodo di riferimento (§7.3.2);
- **analisi lineare dinamica** (modale con spettro di risposta) (§7.3.3.1);
- **analisi lineare statica** (forze laterali) e sua applicabilità (§7.3.3.2);
- **valutazione degli spostamenti** (§7.3.3.3);
- **analisi non lineare** dinamica (integrazione al passo) e statica (**pushover**) (§7.3.4).

È un **supporto documentale**: inquadra la **scelta del metodo** e le sue **condizioni di applicabilità**; **non**
esegue l'analisi né le verifiche. È **distinta** da `fattore-comportamento-q-sismica-ntc` (§7.3.1, q e scelta
lineare/non lineare), `periodo-proprio-t1-ntc` (§7.3.3.2, solo T1), `criteri-modellazione-sismica-ntc` (§7.2.6) e
`combinazione-componenti-sismiche-ntc` (§7.3.5).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `scegli-metodo-e-analisi-lineare` | Scelta dinamica/statica (§7.3.2); analisi modale (masse ≥85%, CQC) (§7.3.3.1); analisi lineare statica (applicabilità T1≤2,5 TC, Fh/Fi/λ) (§7.3.3.2); spostamenti μd (§7.3.3.3) |
| `applica-analisi-non-lineare` | Analisi non lineare dinamica (§7.3.4.1) e statica/pushover (§7.3.4.2): curva di capacità, punto di controllo, distribuzioni Gruppo 1/2 |

## Punti chiave (verificati sul testo/immagine)

- **Scelta** (§7.3.2): metodo di riferimento = **analisi modale con spettro** (lineare dinamica); **lineare statica**
  ammessa **solo** se la risposta non dipende dai modi superiori.
- **Modale** (§7.3.3.1): modi con **massa > 5%**, totale **≥ 85%**; combinazione **CQC** [7.3.4]; **eccentricità
  accidentale**.
- **Statica lineare** (§7.3.3.2): applicabile se **T1 ≤ 2,5·TC** (o TD) **e regolare in altezza**; **Fh =
  Sd(T1)·W·λ/g**; **Fi = Fh·zi·Wi/Σ(zj·Wj)** [7.3.7]; **λ = 0,85** (T1<2TC e ≥3 orizzontamenti) o **1,0**.
- **Spostamenti** (§7.3.3.3): **dE = μd·dEe** [7.3.8]; **μd = q** o **1+(q−1)·TC/T1** [7.3.9], **μd ≤ 5q−4**;
  **SLC = 1,25·SLV**. **P-Δ (θ)**: trascurabile se θ<0,1; amplifica 1/(1−θ) se 0,1–0,2; **θ ≤ 0,3**.
- **Non lineare** (§7.3.4): dinamica con **integrazione al passo** (confronto con modale); **pushover** con curva di
  capacità **Fb–dc**, punto di controllo al **centro di massa dell'ultimo livello**, **≥ 2 distribuzioni** (Gruppo 1
  modo fondamentale **≥ 75%** / modale se **T1 > 1,3·TC**; Gruppo 2 uniforme/adattiva/multimodale **≥ 6 modi**).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **parr. 7.3.2-7.3.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con tutti i valori
  numerici/formule verificati sull'immagine delle pagine PDF 222-224.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** l'**analisi** (modale, statica, pushover, time-history) né le **verifiche**; non dimensiona.
- **Non tratta** il **fattore q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`), la formula di **T1**
  (§7.3.3.2, → skill `periodo-proprio-t1-ntc`), i **criteri di modellazione** (§7.2.6) né la **combinazione delle
  componenti** (§7.3.5, → skill dedicate).
- **Non** sostituisce il progettista né la Circolare applicativa 2019.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura dei par. 7.3.2-7.3.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
