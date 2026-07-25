---
name: ancoraggi-precompressione-appoggi-qualificazione-ntc
description: "Supporto documentale al progettista strutturale e al Direttore dei Lavori per la qualificazione e i controlli di accettazione in cantiere di ancoranti per uso strutturale, giunti di dilatazione stradale, sistemi di precompressione a cavi post-tesi, tiranti di ancoraggio per uso geotecnico e appoggi strutturali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafi 11.4, 11.5 e 11.6. Aiuta a inquadrare: gli ancoranti per uso strutturale del par. 11.4.1 (qualificazione secondo il punto C del par. 11.1 sulla base della Linea guida ETAG 001, valida anche per le prove di accettazione; in presenza di azioni sismiche, per tutte le classi d'uso del punto 2.4.2, la categoria di prestazione minima da soddisfare e' la C2 dell'Annesso E dell'ETAG 001); i giunti di dilatazione stradale del par. 11.4.2 (punto C del par. 11.1, Linea guida ETAG 032); i sistemi di precompressione a cavi post-tesi del par. 11.5.1 (punto C del par. 11.1, qualificazione mediante Certificato di valutazione tecnica su Linea Guida del Consiglio Superiore dei Lavori Pubblici, fornitura con copia del certificato o marcatura CE su ETA e manuale, verifica e prove di accettazione del Direttore dei Lavori secondo ETAG 013); i tiranti di ancoraggio per uso geotecnico attivi e passivi del par. 11.5.2 (punto C del par. 11.1, per i tipo attivo Certificazione di valutazione tecnica su Linea Guida CSLP); e gli appoggi strutturali del par. 11.6 (punto A del par. 11.1, conformita' alla serie UNI EN 1337 e Marcatura CE, Sistema di Valutazione e Verifica della Costanza della Prestazione 1 per applicazioni critiche; altrimenti caso C del par. 11.1). Use when a structural engineer or works supervisor must frame the qualification and site acceptance of post-installed anchors, expansion joints, post-tensioning systems, ground anchors or structural bearings under the Italian NTC 2018 par. 11.4-11.6; it is a documentary aid, does NOT design or verify the products (bearings design, anchor checks, tendon design), and does NOT replace the designer or the works supervisor."
license: MIT
area: strutture-geotecnica
title: "Ancoranti, tiranti e appoggi: qualificazione (NTC 2018 par. 11.4-11.6)"
summary: "Inquadra qualificazione e accettazione di ancoranti, giunti, precompressione, tiranti e appoggi (NTC 2018 par. 11.4-11.6): ancoranti ETAG 001 e categoria sismica C2 (11.4), precompressione/tiranti via CVT/ETA e ETAG 013 (11.5), appoggi UNI EN 1337 + Marcatura CE (11.6)."
normative_refs:
  - "NTC 2018 - par. 11.4: ancoranti per uso strutturale punto C par. 11.1 ETAG 001, categoria sismica C2 per tutte le classi d'uso (11.4.1); giunti di dilatazione stradale ETAG 032 (11.4.2)"
  - "NTC 2018 - par. 11.5-11.6: precompressione post-tesi e tiranti geotecnici punto C par. 11.1 (CVT/ETA, prove ETAG 013); appoggi punto A par. 11.1 UNI EN 1337 + CE (VVCP 1) o caso C"
version: 0.1.0-alpha
status: alpha
tags:
  - ancoranti
  - precompressione
  - appoggi-strutturali
  - ntc-2018
  - accettazione
---

# Ancoranti, tiranti e appoggi: qualificazione e accettazione (NTC 2018 par. 11.4-11.6)

## Quando usare questa skill

Usala quando un **progettista strutturale** o un **Direttore dei Lavori** deve inquadrare la **qualificazione** e i
**controlli di accettazione in cantiere** dei prodotti/sistemi strutturali «speciali» secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafi 11.4, 11.5 e 11.6** (Cap. 11):

- **ancoranti per uso strutturale** (tasselli post-installati) e **giunti di dilatazione stradale** (§11.4);
- **sistemi di precompressione a cavi post-tesi** e **tiranti di ancoraggio per uso geotecnico** (§11.5);
- **appoggi strutturali** (§11.6).

È un **supporto documentale**: inquadra il **percorso di qualificazione** (punti A/C del §11.1, ETA/ETAG/CVT, UNI EN
1337) e la **verifica del Direttore dei Lavori**; **non** esegue il progetto né le verifiche dei prodotti. È
**distinta** da `tiranti-ancoraggio-ntc` (§6.6, progetto/verifiche geotecniche) e da
`dispositivi-antisismici-qualificazione-ntc` (§11.9, dispositivi antisismici UNI EN 15129).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-ancoranti-e-giunti` | Ancoranti per uso strutturale (ETAG 001, categoria sismica C2) e giunti di dilatazione stradale (ETAG 032) (§11.4) |
| `inquadra-precompressione-tiranti-e-appoggi` | Precompressione post-tesi e tiranti geotecnici (punto C, CVT/ETA, prove ETAG 013) (§11.5); appoggi strutturali (punto A, UNI EN 1337 + CE / caso C) (§11.6) |

## Punti chiave (verificati sul testo/immagine)

- **Ancoranti** (§11.4.1): qualificazione **punto C del §11.1**, base **ETAG 001** (anche per le prove di
  accettazione); in **azioni sismiche**, per **tutte le classi d'uso** (§2.4.2) categoria di prestazione minima
  **C2** (Annesso E, tab. 1.1, §1.2 ETAG 001).
- **Giunti di dilatazione stradale** (§11.4.2): **punto C del §11.1**, base **ETAG 032**.
- **Precompressione post-tesi** (§11.5.1): **punto C del §11.1**; **Certificato di valutazione tecnica** (Linea Guida
  CSLP); fornitura con **CVT o marcatura CE su ETA** + **manuale**; il **Direttore dei Lavori** verifica, rifiuta le
  forniture prive, verifica la posa e le **prove di accettazione** (geometria/tolleranze + caratteristiche
  meccaniche); prove secondo **ETAG 013**.
- **Tiranti geotecnici** (§11.5.2): attivi/passivi **punto C del §11.1**; per i **tipo attivo** CVT (Linea Guida
  CSLP); analoga verifica/prove del DL.
- **Appoggi strutturali** (§11.6): **punto A del §11.1** → **UNI EN 1337 + Marcatura CE**, **Sistema VVCP 1** per
  applicazioni critiche; se non ricadenti → **caso C del §11.1**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.4-11.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con i riferimenti
  (C2, VVCP 1, ETAG 001/032/013, UNI EN 1337) verificati sull'immagine della pagina PDF 348.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** il **progetto/verifiche** dei prodotti (progetto degli appoggi, verifiche degli ancoranti, progetto
  dei cavi post-tesi, verifiche geotecniche dei tiranti al §6.6).
- **Non riproduce** il **dettaglio delle prove** delle Linee guida/norme europee (ETAG 001/013/032, UNI EN 1337), che
  restano la fonte per procedure e valori.
- **Non** sostituisce il progettista, il Direttore dei Lavori né le Linee guida/norme europee applicabili.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura dei par. 11.4-11.6 delle NTC 2018 e delle Linee guida/norme europee applicabili (ETAG, UNI EN 1337).**
