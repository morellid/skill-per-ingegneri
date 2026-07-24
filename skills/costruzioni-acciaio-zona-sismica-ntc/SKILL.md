---
name: costruzioni-acciaio-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le regole generali delle costruzioni di acciaio in zona sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.5. Aiuta a inquadrare: le caratteristiche dei materiali del par. 7.5.1 (acciaio conforme al par. 11.3.4.9 e fattore di sovraresistenza del materiale gamma_ov pari a 1,25 per gli acciai S235, S275 ed S355 e pari a 1,15 per gli acciai S420 ed S460); le tipologie strutturali del par. 7.5.2.1 (strutture intelaiate; strutture con controventi concentrici a diagonale tesa attiva, a V oppure a K, dove la configurazione a K non e' dissipativa; strutture con controventi eccentrici; strutture a mensola o a pendolo inverso; strutture intelaiate con controventi concentrici; strutture intelaiate con tamponature); i fattori di comportamento del par. 7.5.2.2 (q0 dalla Tab. 7.3.II; rapporto alpha_u su alpha_1 pari a 1,1 per gli edifici a un piano, 1,2 per i telai a piu' piani con una sola campata, 1,3 per i telai a piu' piani e piu' campate, 1,2 per i controventi eccentrici a piu' piani, 1,0 per le strutture a mensola o a pendolo inverso); e le regole generali per gli elementi dissipativi del par. 7.5.3 con la Tab. 7.5.I (classe della sezione trasversale in funzione della classe di duttilita' e di q0: CD\"B\" con 2 minore di q0 minore o uguale a 4 richiede sezioni di Classe 1 o 2, CD\"A\" con q0 maggiore di 4 richiede sezioni di Classe 1; per le colonne primarie dissipative dei telai il rapporto NEd su Npl,Rd non deve superare 0,3). Use when a structural engineer must frame the general rules for steel buildings in seismic zones under the Italian NTC 2018 par. 7.5; it is a documentary aid, does NOT run the member/connection resistance and ductility verifications, does NOT design the connections, and does NOT replace the designer. It is distinct from the static steel skill (par. 4.2) and the behaviour-factor q skill (par. 7.3.1)."
license: MIT
area: strutture-geotecnica
title: "Acciaio in zona sismica: regole generali (NTC 2018 par. 7.5)"
summary: "Inquadra le regole generali dell'acciaio in zona sismica (NTC 2018 par. 7.5): materiali e sovraresistenza gamma_ov 1,25/1,15 (7.5.1), tipologie strutturali (7.5.2.1), fattori q0 e alpha_u/alpha_1 1,1-1,3 (7.5.2.2), classe della sezione Tab. 7.5.I e NEd/Npl,Rd<=0,3 (7.5.3)."
normative_refs:
  - "NTC 2018 - par. 7.5: acciaio sismico, gamma_ov 1,25/1,15 (7.5.1); tipologie strutturali (7.5.2.1); q0 e alpha_u/alpha_1 1,1-1,3 (7.5.2.2); Tab. 7.5.I classe sezione, NEd/Npl,Rd<=0,3 (7.5.3)"
  - "Rinvio (fuori scope): verifiche RES/DUT di membrature e collegamenti (7.5.3.1-7.5.6); acciaio statico par. 4.2 e fattore q par. 7.3.1 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - acciaio
  - zona-sismica
  - ntc-2018
  - fattore-comportamento
  - tipologie-strutturali
---

# Acciaio in zona sismica: regole generali (NTC 2018 par. 7.5)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le regole generali** delle **costruzioni di acciaio
in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.5**:

- **caratteristiche dei materiali** e fattore di sovraresistenza γov (§7.5.1);
- **tipologie strutturali** (§7.5.2.1);
- **fattori di comportamento** q0 e αu/α1 (§7.5.2.2);
- **regole generali** per gli elementi dissipativi e **classe della sezione** (§7.5.3, Tab. 7.5.I).

È un **supporto documentale**: inquadra materiali, tipologie, fattori di comportamento e classe delle sezioni;
**non** esegue le verifiche (resistenza/duttilità di membrature e collegamenti) né progetta i collegamenti. È
**distinta** da `costruzioni-acciaio-ntc` (§4.2, materiali e verifiche **statiche**) e da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-materiali-fattore-q` | Materiali/γov (§7.5.1), tipologie strutturali (§7.5.2.1) e fattori di comportamento q0/αu/α1 (§7.5.2.2) |
| `verifica-requisiti-classe-sezione-dissipativi` | Regole generali per elementi dissipativi e classe della sezione (§7.5.3, Tab. 7.5.I; NEd/Npl,Rd ≤ 0,3) |

## Punti chiave (verificati sul testo/immagine)

- **Materiali** (§7.5.1): acciaio conforme al **§11.3.4.9**; **fattore di sovraresistenza del materiale γov =
  1,25** per **S235/S275/S355** e **= 1,15** per **S420/S460**.
- **Tipologie** (§7.5.2.1): a) intelaiate (zone dissipative alle estremità delle travi); b) controventi
  concentrici (b1 diagonale tesa attiva, b2 a V, **b3 a K non dissipativa**); c) controventi eccentrici
  (dissipazione nei traversi); d) a mensola/pendolo inverso; e) intelaiate con controventi; f) intelaiate con
  tamponature. Dispositivi antisismici esclusi; nuclei/pareti c.a. → §7.4.
- **Fattori di comportamento** (§7.5.2.2): **q0** max in **Tab. 7.3.II**; **αu/α1** = **1,1** (un piano) / **1,2**
  (telaio più piani, 1 campata) / **1,3** (telaio più piani, più campate) / **1,2** (controventi eccentrici) /
  **1,0** (mensola/pendolo inverso).
- **Regole generali dissipativi** (§7.5.3): zone dissipative **nelle membrature**; capacity design del
  collegamento **Rj,d ≥ 1,1·γov·Rpl,Rd**; duttilità locale **μ = θu/θy** (θu al **−15%** della resistenza max).
  **Tab. 7.5.I**: CD "B" (**2 < q0 ≤ 4**) → **Classe 1 o 2**; CD "A" (**q0 > 4**) → **Classe 1**. Colonne primarie
  dissipative dei telai: **NEd/Npl,Rd ≤ 0,3**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 243-246 (γov, αu/α1, Tab. 7.5.I, limite NEd/Npl,Rd).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche** di resistenza (RES) e di duttilità (DUT) di membrature e collegamenti né le
  regole specifiche per tipologia (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6).
- **Non progetta** i **collegamenti** né calcola il valore numerico di **q0** per tipologia (Tab. 7.3.II).
- **Non tratta** i requisiti **statici** (§4.2, → skill `costruzioni-acciaio-ntc`) né il framework del **fattore
  q** (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); **non** sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.5 delle NTC 2018 e della relativa Circolare applicativa.**
