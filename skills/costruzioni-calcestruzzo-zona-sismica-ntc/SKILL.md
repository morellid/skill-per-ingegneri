---
name: costruzioni-calcestruzzo-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare la progettazione sismica delle costruzioni di calcestruzzo armato secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.4. Aiuta a inquadrare: le caratteristiche dei materiali del par. 7.4.2 (acciaio B450C; B450A ammesso solo con diametri tra 5 e 10 mm per reti e tralicci, o come armatura trasversale se la plasticizzazione e' impedita dalla gerarchia delle resistenze, negli elementi secondari o nelle strutture non dissipative); le tipologie strutturali del par. 7.4.3.1 (a telaio con taglio alla base almeno il 65%, a pareti semplici/composte e singole/accoppiate, miste telaio-pareti equivalenti a telai se oltre il 50% dell'azione orizzontale e' ai telai, a pendolo inverso, a pendolo inverso intelaiate monopiano con forza assiale non oltre il 30% della resistenza del cls, deformabili torsionalmente con r2/ls2 almeno 1, a pareti estese debolmente armate con periodo non superiore a TC); i fattori di comportamento del par. 7.4.3.2 (q secondo il par. 7.3.1 e la Tab. 7.3.II; pareti accoppiate se il momento alla base e' equilibrato per almeno il 20% dalla coppia degli sforzi verticali; alpha_u/alpha_1 pari a 1,1-1,2-1,3 per i telai e 1,0-1,1-1,2 per le pareti; scelta della classe di duttilita' CD A o CD B); e la gerarchia delle resistenze del par. 7.4.4 (fattori di sovraresistenza gamma_Rd della Tab. 7.2.I; taglio delle travi dalla capacita' flessionale amplificata; pilastri con domanda a compressione non oltre il 55% in CD A e il 65% in CD B della capacita' del solo cls; nodo pilastro forte-trave debole con somma dei momenti resistenti dei pilastri maggiore o uguale a gamma_Rd per la somma di quelli delle travi). Use when a structural engineer must frame the seismic design of reinforced concrete buildings (structural typologies, behaviour factor, capacity design of beams, columns and joints) under the Italian NTC 2018 par. 7.4; it is a documentary aid, does NOT run the design or the detailed member checks and detailing (par. 7.4.6), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni di calcestruzzo in zona sismica (NTC 2018 par. 7.4)"
summary: "Inquadra la progettazione sismica del c.a. (NTC 2018 par. 7.4): materiali B450C (7.4.2), tipologie e taglio base >=65% (7.4.3.1), fattori di comportamento alpha_u/alpha_1 e scelta CD A/CD B (7.4.3.2), gerarchia delle resistenze di travi, pilastri e nodi con gamma_Rd (7.4.4)."
normative_refs:
  - "NTC 2018 - par. 7.4: acciaio B450C (7.4.2); tipologie telaio/pareti/miste/pendolo inverso, taglio base >=65% (7.4.3.1); alpha_u/alpha_1 1,1-1,3 telai e 1,0-1,2 pareti, CD A/CD B (7.4.3.2)"
  - "NTC 2018 - par. 7.4.4: gerarchia delle resistenze (gamma_Rd, Tab. 7.2.I); taglio travi da capacita' amplificata; pilastri compressione <=55%/65%; nodo sum(Mc,Rd)>=gamma_Rd*sum(Mb,Rd) [7.4.4]"
version: 0.1.0-alpha
status: alpha
tags:
  - calcestruzzo-armato
  - zona-sismica
  - gerarchia-resistenze
  - ntc-2018
  - fattore-comportamento
---

# Costruzioni di calcestruzzo in zona sismica (NTC 2018 par. 7.4)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve inquadrare la **progettazione sismica** delle **costruzioni di
calcestruzzo armato** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.4** (Cap. 7):

- **materiali** per le zone dissipative (§7.4.2);
- **tipologie strutturali** e **fattori di comportamento** (αu/α1, scelta CD"A"/CD"B") (§7.4.3);
- **gerarchia delle resistenze** (capacity design) di travi, pilastri, nodi e pareti (§7.4.4);
- **dettagli costruttivi** CD"A"/CD"B" (§7.4.6, richiamati come contesto).

È un **supporto documentale**: inquadra il **quadro progettuale sismico** del c.a.; **non** esegue il progetto né le
verifiche di dettaglio. È **distinta** da `costruzioni-calcestruzzo-ntc` (§4.1, progetto **ordinario non sismico**) e
da `fattore-comportamento-q-sismica-ntc` (§7.3.1, macchina generale del q): il §7.4 è la **specifica sismica del c.a.**

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-e-fattore-comportamento` | Materiali (§7.4.2), tipologie strutturali (§7.4.3.1) e fattori di comportamento αu/α1 e scelta CD"A"/CD"B" (§7.4.3.2) |
| `applica-gerarchia-delle-resistenze` | Gerarchia delle resistenze (§7.4.4): γRd (Tab. 7.2.I), taglio travi, pressoflessione pilastri (55%/65%), nodo pilastro forte-trave debole [7.4.4] |

## Punti chiave (verificati sul testo/immagine)

- **Materiali** (§7.4.2): acciaio **B450C**; **B450A** solo **Ø 5-10 mm** (reti/tralicci) o trasversale se
  plasticizzazione impedita/secondari/non dissipativo.
- **Tipologie** (§7.4.3.1): telaio e pareti con **taglio alla base ≥ 65%**; miste (**> 50%** ai telai → equiv. telai);
  pendolo inverso (**≥ 50% massa** terzo superiore; monopiano **N ≤ 30%** resistenza cls); deformabili torsionalmente
  **r²/ls² ≥ 1**; pareti estese debolmente armate **T ≤ TC** (solo CD"B").
- **Fattori** (§7.4.3.2): q via §7.3.1/Tab. 7.3.II; pareti accoppiate se momento base equilibrato **≥ 20%**; **αu/α1**
  telai **1,1/1,2/1,3**, pareti **1,0/1,1/1,2**; travi a spessore → **CD"B"**.
- **Gerarchia** (§7.4.4): **γRd** da **Tab. 7.2.I**; travi taglio da **capacità flessionale amplificata**; pilastri
  compressione **≤ 55% (CD"A") / 65% (CD"B")** del solo cls; nodo **ΣMc,Rd ≥ γRd·ΣMb,Rd** [7.4.4]; travi CD"A" con
  eventuali armature **±45°** ([7.4.1]/[7.4.2]); duttilità travi **μφ** [7.4.3], **μφ = 2μd − 1**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con i valori
  numerici/formule verificati sull'immagine delle pagine PDF 228-230 (tipologie, αu/α1, 55%/65%, [7.4.1]-[7.4.4]).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** il **progetto** né le **verifiche di dettaglio** (verifiche RES/DUT complete, dettagli costruttivi
  §7.4.6): il dettaglio numerico resta nella norma.
- **Non tratta** il **progetto ordinario non sismico** (§4.1, → skill `costruzioni-calcestruzzo-ntc`) né la macchina
  generale del **q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`).
- **Non** sostituisce il progettista né la Circolare applicativa 2019.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
