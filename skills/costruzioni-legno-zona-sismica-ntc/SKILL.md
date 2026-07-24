---
name: costruzioni-legno-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le regole generali delle costruzioni di legno in zona sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.7. Aiuta a inquadrare: gli aspetti concettuali del par. 7.7.1 (comportamento strutturale dissipativo, con classe di duttilita' CD\"A\" o CD\"B\", oppure non dissipativo; zone dissipative localizzate nei collegamenti e membrature lignee a comportamento elastico; nella progettazione in capacita' le componenti non dissipative dimensionate sulla capacita' della zona dissipativa amplificata del fattore di sovraresistenza, con valori comunque non inferiori a 1,3 per la CD\"A\" e a 1,1 per la CD\"B\"); i materiali e le proprieta' delle zone dissipative del par. 7.7.2 (rinvio al par. 4.4; unioni incollate in generale non dissipative; spessori minimi dei pannelli di rivestimento: particelle almeno 13 mm, compensato almeno 9 mm, OSB almeno 12 mm se a coppia o 15 mm se singoli); le tipologie strutturali e i fattori di comportamento del par. 7.7.3 (q0 dalla Tab. 7.3.II, con obbligo del Progettista di giustificare q0); le precisazioni sulla duttilita' del par. 7.7.3.1 (almeno tre cicli, rapporto di duttilita' statica pari a 4 per la CD\"B\" e a 6 per la CD\"A\", riduzione di resistenza non oltre il 20 per cento; diametro dei mezzi di unione non oltre 12 mm con spessore delle membrature almeno 10 volte il diametro, oppure chiodi non oltre 3,1 mm con rivestimento almeno 4 volte il diametro); e le disposizioni costruttive e le verifiche dei par. 7.7.5-7.7.7 (giunti di carpenteria con coefficiente parziale aggiuntivo 1,3; resistenza ridotta del 20 per cento per il degrado ciclico). Use when a structural engineer must frame the general rules for timber buildings in seismic zones under the Italian NTC 2018 par. 7.7; it is a documentary aid, does NOT run the resistance/ductility verifications, does NOT design the connections, and does NOT replace the designer. It is distinct from the static timber skill (par. 4.4) and the behaviour-factor q skill (par. 7.3.1)."
license: MIT
area: strutture-geotecnica
title: "Legno in zona sismica: regole generali (NTC 2018 par. 7.7)"
summary: "Inquadra le regole generali del legno in zona sismica (NTC 2018 par. 7.7): comportamento dissipativo CD\"A\"/CD\"B\" (7.7.1), materiali e pannelli (7.7.2), fattori q0 (7.7.3), duttilita' statica 4/6 e mezzi di unione (7.7.3.1), disposizioni costruttive e verifiche (7.7.5-7.7.7)."
normative_refs:
  - "NTC 2018 - par. 7.7: legno sismico CD\"A\"/CD\"B\" e sovraresistenza >=1,3/1,1 (7.7.1); pannelli 13/9/12/15 mm (7.7.2); q0 Tab. 7.3.II (7.7.3); duttilita' 4/6, d<=12 mm & 10d, d<=3,1 mm & 4d (7.7.3.1)"
  - "Rinvio (fuori scope): verifiche resistenza/duttilita' e q0 numerico (Tab. 7.3.II); legno statico par. 4.4 e fattore q par. 7.3.1 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - legno
  - zona-sismica
  - ntc-2018
  - fattore-comportamento
  - duttilita
---

# Legno in zona sismica: regole generali (NTC 2018 par. 7.7)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le regole generali** delle **costruzioni di legno
in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.7**:

- **aspetti concettuali** della progettazione e classe di duttilità (§7.7.1);
- **materiali** e proprietà delle zone dissipative, pannelli di rivestimento (§7.7.2);
- **tipologie strutturali** e **fattori di comportamento** q0 (§7.7.3);
- **precisazioni sulla duttilità** e sui mezzi di unione (§7.7.3.1);
- **disposizioni costruttive**, **verifiche** e regole di dettaglio (§§7.7.4-7.7.7).

È un **supporto documentale**: inquadra comportamento, materiali, fattori q0 e requisiti di duttilità; **non**
esegue le verifiche (resistenza/duttilità di elementi e collegamenti) né progetta i collegamenti. È **distinta**
da `costruzioni-legno-ntc` (§4.4, materiali e verifiche **statiche**) e da `fattore-comportamento-q-sismica-ntc`
(§7.3.1, framework **generale** del fattore q).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-comportamento-materiali-fattore-q` | Aspetti concettuali/CD (§7.7.1), materiali e pannelli (§7.7.2) e fattori di comportamento q0 (§7.7.3) |
| `verifica-requisiti-duttilita-dettagli` | Precisazioni sulla duttilità (§7.7.3.1), disposizioni costruttive, verifiche e dettagli (§§7.7.5-7.7.7) |

## Punti chiave (verificati sul testo/immagine)

- **Aspetti concettuali** (§7.7.1): comportamento **dissipativo** → **CD "A"** o **CD "B"** (requisiti §7.7.3) o
  **non dissipativo** (→ §4.4). Zone dissipative nei **collegamenti**, membrature lignee **elastiche**. In
  progettazione in capacità: componenti non dissipative su capacità della zona dissipativa **× ηRd** (Tab. 7.2.I);
  valori inferiori solo se **≥ 1,3 (CD "A")** / **≥ 1,1 (CD "B")** e giustificati.
- **Materiali** (§7.7.2): si applica il **§4.4**; **unioni incollate** in generale **non dissipative**; **pannelli
  di rivestimento**: particelle **≥ 13 mm**, compensato **≥ 9 mm**, OSB **≥ 12 mm** (coppia) / **≥ 15 mm** (singoli);
  connettori a gambo cilindrico conformi al **§11.7.8**.
- **Fattori di comportamento** (§7.7.3): **q0 dalla Tab. 7.3.II** (nel framework generale **q = q0·KR**); per le
  dissipative **il Progettista deve giustificare q0**.
- **Duttilità** (§7.7.3.1): **≥ 3 cicli**, **duttilità statica ≥ 4 (CD "B")** / **≥ 6 (CD "A")**, riduzione di
  resistenza **≤ 20%**. Regole: a) legno-legno/legno-acciaio perni/chiodi **d ≤ 12 mm** e membrature **≥ 10d**;
  b) pareti/diaframmi a telaio chiodi **d ≤ 3,1 mm** e rivestimento **≥ 4d**. Alternativa **8d/3d** → CD "B".
- **Verifiche/dettagli** (§§7.7.5-7.7.7): impalcati con vincoli **bilateri**; **giunti di carpenteria** con
  **coefficiente parziale aggiuntivo 1,3**; per le dissipative RES §7.3.6.1 con **resistenza ridotta del 20%**
  (degrado ciclico); **perni/bulloni d > 16 mm** non usati nei collegamenti legno-legno/legno-acciaio.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 258-260 (spessori pannelli, rapporti di duttilità, mezzi di unione, coefficienti).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche** di resistenza e di duttilità dei singoli elementi e collegamenti né calcola il
  valore numerico di **q0** per tipologia (Tab. 7.3.II).
- **Non progetta** i **collegamenti** né i dettagli di cui al §7.7.7; non riproduce le regole di dettaglio complete.
- **Non tratta** i requisiti **statici** (§4.4, → skill `costruzioni-legno-ntc`) né il framework del **fattore q**
  (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); **non** sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.7 delle NTC 2018 e della relativa Circolare applicativa.**
