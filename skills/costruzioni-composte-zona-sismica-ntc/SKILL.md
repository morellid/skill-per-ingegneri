---
name: costruzioni-composte-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le regole generali delle costruzioni composte di acciaio-calcestruzzo in zona sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.6. Aiuta a inquadrare: i comportamenti strutturali del par. 7.6 (a) non dissipativo secondo il par. 4.3; b) dissipativo con zone dissipative in membrature composte; c) dissipativo con zone dissipative in acciaio, con integrita' del calcestruzzo compresso); le caratteristiche dei materiali del par. 7.6.1 (calcestruzzo non inferiore a C20/25 o LC20/22 e non superiore a C40/50 o LC40/44; acciaio per c.a. B450C, con B450A ammesso nei casi del par. 7.4.2.2; acciaio strutturale secondo i par. 7.5 e 11.3.4); le tipologie strutturali e i fattori di comportamento del par. 7.6.2 (tipologie intelaiate, con controventi concentrici in acciaio, con controventi eccentrici a connessioni in acciaio, a mensola o a pendolo inverso, intelaiate controventate; pareti o nuclei in c.a. rinviati al par. 7.4; q0 dalla Tab. 7.3.II); la rigidezza della sezione composta del par. 7.6.3 (coefficiente di omogeneizzazione n=Ea/Ecm=7 per il calcestruzzo compresso; momento d'inerzia non fessurato I1 e fessurato I2); e i criteri per le strutture dissipative del par. 7.6.4 (capacity design con EU,Rd=1,1 gamma_ov Epl,Rd; Rj,d>=RU,Rd; per le colonne primarie dei telai il rapporto NEd/Npl,Rd non oltre 0,3). Use when a structural engineer must frame the general rules for steel-concrete composite buildings in seismic zones under the Italian NTC 2018 par. 7.6; it is a documentary aid, does NOT run the member/connection resistance and ductility verifications, does NOT design the connections, and does NOT replace the designer. It is distinct from the static composite skill (par. 4.3), the seismic steel skill (par. 7.5) and the behaviour-factor q skill (par. 7.3.1)."
license: MIT
area: strutture-geotecnica
title: "Composte acciaio-cls in zona sismica: regole generali (NTC 2018 par. 7.6)"
summary: "Inquadra le regole generali delle composte acciaio-cls in zona sismica (NTC 2018 par. 7.6): comportamenti a/b/c, materiali (cls C20/25-C40/50, acciaio B450C; 7.6.1), tipologie e q0 (7.6.2), rigidezza n=Ea/Ecm=7 (7.6.3), capacity design EU,Rd e NEd/Npl,Rd<=0,3 (7.6.4)."
normative_refs:
  - "NTC 2018 - par. 7.6: composte sismiche, materiali cls C20/25-C40/50, B450C (7.6.1); tipologie e q0 (7.6.2); rigidezza n=7 (7.6.3); EU,Rd=1,1 gamma_ov Epl,Rd, NEd/Npl,Rd<=0,3 (7.6.4)"
  - "Rinvio (fuori scope): verifiche RES/DUT e dettagli (7.6.4-7.6.8); composte statiche par. 4.3, acciaio sismico par. 7.5, fattore q par. 7.3.1 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - strutture-composte
  - zona-sismica
  - ntc-2018
  - fattore-comportamento
  - acciaio-calcestruzzo
---

# Composte acciaio-cls in zona sismica: regole generali (NTC 2018 par. 7.6)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le regole generali** delle **costruzioni composte di
acciaio-calcestruzzo in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.6**:

- **comportamenti** strutturali dissipativo/non dissipativo (§7.6);
- **caratteristiche dei materiali** (§7.6.1);
- **tipologie strutturali** e **fattori di comportamento** q0 (§7.6.2);
- **rigidezza** della sezione composta (§7.6.3) e **criteri**/capacity design per le strutture dissipative (§7.6.4).

È un **supporto documentale**: inquadra comportamenti, materiali, tipologie, fattori di comportamento, rigidezza e
capisaldi del capacity design; **non** esegue le verifiche (resistenza/duttilità di membrature e collegamenti) né
progetta i collegamenti. È **distinta** da `costruzioni-composte-acciaio-cls-ntc` (§4.3, **statica**), da
`costruzioni-acciaio-zona-sismica-ntc` (§7.5) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-tipologie-fattore-q` | Comportamenti (§7.6), materiali (§7.6.1), tipologie e fattori di comportamento q0 (§7.6.2) e rigidezza n=7 (§7.6.3) |
| `verifica-requisiti-capacity-design` | Criteri e capisaldi del capacity design per le strutture dissipative (§7.6.4: EU,Rd, Rj,d≥RU,Rd, NEd/Npl,Rd ≤ 0,3, μ) |

## Punti chiave (verificati sul testo/immagine)

- **Comportamenti** (§7.6): a) non dissipativo (→ §4.3); b) dissipativo con zone dissipative in **membrature
  composte**; c) dissipativo con zone dissipative in **acciaio** (integrità del cls compresso).
- **Materiali** (§7.6.1): calcestruzzo **≥ C20/25 (LC20/22)** e **≤ C40/50 (LC40/44)**; acciaio per c.a. **B450C**
  (B450A solo casi §7.4.2.2); acciaio strutturale secondo §7.5 e §11.3.4.
- **Tipologie e q0** (§7.6.2): a) intelaiate; b) controventi concentrici in acciaio; c) controventi eccentrici
  (connessioni in acciaio); d) mensola/pendolo inverso; e) intelaiate controventate. Pareti/nuclei c.a. → §7.4.
  **q0** max in **Tab. 7.3.II** (prescrizioni §7.5.2).
- **Rigidezza** (§7.6.3): cls compresso **n = Ea/Ecm = 7**; momento d'inerzia **non fessurato I1** / **fessurato I2**.
- **Capacity design** (§7.6.4): **EU,Rd = 1,1·γov·Epl,Rd** (γov §7.5.1); **Rj,d ≥ RU,Rd** [7.6.1]; pannello d'anima
  **Vwp,Rd = 0,8·(Vwp,s,Rd + Vwp,c,Rd)** [7.6.2] se altezze differiscono **≤ 40%**; **μ = θu/θy** (θu al **−15%**);
  colonne primarie dissipative dei telai **NEd/Npl,Rd ≤ 0,3** [7.6.3].

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 251-253 (classi cls, B450C, n=7, q0, EU,Rd, NEd/Npl,Rd).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche** di resistenza (RES) e di duttilità (DUT) di membrature e collegamenti né le
  regole specifiche per tipologia/elemento (§§ 7.6.4-7.6.8, Tab. 7.6.I-IV).
- **Non progetta** i **collegamenti** né calcola il valore numerico di **q0** (Tab. 7.3.II).
- **Non tratta** i requisiti **statici** (§4.3, → skill `costruzioni-composte-acciaio-cls-ntc`), le regole sismiche
  dell'**acciaio** (§7.5, → skill dedicata) né il **fattore q** (§7.3.1, → skill dedicata); **non** sostituisce il
  progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.6 delle NTC 2018 e della relativa Circolare applicativa.**
