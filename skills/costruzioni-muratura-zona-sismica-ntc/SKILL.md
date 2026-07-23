---
name: costruzioni-muratura-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le regole generali delle costruzioni di muratura in zona sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.8.1. Aiuta a inquadrare: la premessa del par. 7.8.1.1 (le costruzioni di muratura, nel rispetto dei par. 4.5 e 11.10, sono moderatamente dissipative e appartengono alla classe di duttilita' CD\"B\"; i coefficienti parziali di sicurezza del Capitolo 4 possono essere ridotti del 20 per cento e comunque non oltre un valore non inferiore a 2); i requisiti dei materiali del par. 7.8.1.2 (oltre a quelli del par. 4.5.2 e salvo le costruzioni con agS minore o uguale a 0,075g: percentuale di vuoti non superiore al 45 per cento, resistenza caratteristica a rottura nella direzione portante fbk almeno 5 MPa oppure resistenza media normalizzata fb almeno 6 MPa, resistenza perpendicolare almeno 1,5 MPa, malta di allettamento almeno 5 MPa, con limiti per i giunti sottili e a secco); le modalita' costruttive e i fattori di comportamento del par. 7.8.1.3 (muratura ordinaria, armata o confinata; q uguale a q0 per KR; rapporto alpha_u su alpha_1 pari a 1,7 per la muratura ordinaria, 1,5 per l'armata e 1,3 con progettazione in capacita', 1,6 per la confinata e 1,3 con progettazione in capacita', comunque non oltre 2,5); e i criteri di progetto e i requisiti geometrici del par. 7.8.1.4 (piante compatte e simmetriche, pareti continue in elevazione senza pareti in falso, distanza massima tra due solai non oltre 5 metri, e la Tab. 7.8.I con lo spessore minimo, la snellezza massima h0 su t e il rapporto minimo l su h' delle pareti resistenti al sisma). Use when a structural engineer must frame the general rules for masonry buildings in seismic zones under the Italian NTC 2018 par. 7.8.1; it is a documentary aid, does NOT run the pier verifications (in-plane/out-of-plane bending, shear), does NOT design the reinforcement, and does NOT replace the designer. It is distinct from the static masonry skill (par. 4.5) and the behaviour-factor q skill (par. 7.3.1)."
license: MIT
area: strutture-geotecnica
title: "Muratura in zona sismica: regole generali (NTC 2018 par. 7.8.1)"
summary: "Inquadra le regole generali della muratura in zona sismica (NTC 2018 par. 7.8.1): CD\"B\" (7.8.1.1), requisiti dei materiali (fbk>=5 MPa, malta>=5, vuoti<=45%; 7.8.1.2), fattori alpha_u/alpha_1 1,7/1,5/1,6 (7.8.1.3) e requisiti geometrici Tab. 7.8.I (7.8.1.4)."
normative_refs:
  - "NTC 2018 - par. 7.8.1: muratura CD\"B\" (7.8.1.1); materiali fbk>=5 MPa, malta>=5, vuoti<=45% (7.8.1.2); alpha_u/alpha_1 1,7/1,5/1,6 (7.8.1.3); Tab. 7.8.I tmin/(h0/t)max/(l/h')min (7.8.1.4)"
  - "Rinvio (fuori scope): verifiche pannelli (7.8.2-7.8.4) e analisi (7.8.1.5); muratura statica par. 4.5 e fattore q par. 7.3.1 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - muratura
  - zona-sismica
  - ntc-2018
  - requisiti-geometrici
  - fattore-comportamento
---

# Muratura in zona sismica: regole generali (NTC 2018 par. 7.8.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le regole generali** delle **costruzioni di
muratura in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.8.1** (par. 7.8
«Costruzioni di muratura»):

- **premessa** e classe di duttilità CD"B" (§7.8.1.1);
- requisiti dei **materiali** (§7.8.1.2);
- **modalità costruttive** e **fattori di comportamento** αu/α1 (§7.8.1.3);
- **criteri di progetto** e **requisiti geometrici** delle pareti (§7.8.1.4, Tab. 7.8.I).

È un **supporto documentale**: inquadra materiali, fattori di comportamento e requisiti geometrici; **non**
esegue le verifiche (pressoflessione/taglio dei pannelli) né progetta l'armatura. È **distinta** da
`costruzioni-muratura-ntc` (§4.5, materiali e verifiche **statiche**) e da `fattore-comportamento-q-sismica-ntc`
(§7.3.1, framework **generale** del fattore q).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-fattori-comportamento` | Premessa/CD"B" (§7.8.1.1), requisiti dei materiali (§7.8.1.2) e fattori di comportamento αu/α1 (§7.8.1.3) |
| `verifica-requisiti-geometrici-pareti` | Criteri di progetto e requisiti geometrici delle pareti resistenti al sisma (§7.8.1.4, Tab. 7.8.I) |

## Punti chiave (verificati sul testo/immagine)

- **Premessa** (§7.8.1.1): muratura (§§4.5 e 11.10) **moderatamente dissipativa** → **CD"B"**; coefficienti
  parziali del Cap. 4 **riducibili del 20%** e comunque **≥ 2**.
- **Materiali** (§7.8.1.2, oltre §4.5.2, per **agS > 0,075g**): vuoti **≤ 45%**; **f_bk ≥ 5 MPa** (o f_b ≥ 6 MPa)
  in direzione portante; **f_bk ≥ 1,5 MPa** perpendicolare; **malta ≥ 5 MPa** (M5). Limiti per **giunti sottili**
  (0,5-3 mm, solo agS ≤ 0,15g) e **a secco** (setti ≥ 7/10 mm, foratura ≤ 55%).
- **Fattori di comportamento** (§7.8.1.3): q = q0·KR (q0 Tab. 7.3.II); **αu/α1 ≤ 2,5**; in assenza di analisi non
  lineare: ordinaria **1,7**, armata **1,5** (**1,3** con capacity design), confinata **1,6** (**1,3** con
  capacity design).
- **Requisiti geometrici** (§7.8.1.4): piante **compatte/simmetriche**; pareti **continue in elevazione** (no
  pareti in falso); **distanza max tra due solai ≤ 5 m**. **Tab. 7.8.I** (t_min, (h0/t)max, (l/h')min):
  ordinaria pietra squadrata **300 mm / 10 / 0,5**; ordinaria artificiali **240 / 12 / 0,4**; armata **240 / 15
  / qualsiasi**; confinata **240 / 15 / 0,3**; artificiali semipieni (agS≤0,075g) **200 / 20 / 0,3**; pieni
  (agS≤0,075g) **150 / 20 / 0,3**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.8.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 261-262 (valori dei materiali e Tab. 7.8.I).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche** dei pannelli murari (pressoflessione nel piano e fuori piano, taglio: §§ 7.8.2
  ordinaria, 7.8.3 armata, 7.8.4 confinata) né i **metodi di analisi** (§7.8.1.5).
- **Non progetta** l'**armatura** né i **dettagli/cordoli** (§§ 7.8.1.7-7.8.5); non riproduce la muratura armata
  di dettaglio.
- **Non tratta** i requisiti **statici** (§4.5, → skill `costruzioni-muratura-ntc`) né il framework del **fattore
  q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); **non** sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.8 delle NTC 2018 e della relativa Circolare applicativa.**
