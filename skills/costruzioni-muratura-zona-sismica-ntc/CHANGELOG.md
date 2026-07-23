# CHANGELOG - costruzioni-muratura-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #454)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle regole
  generali** delle **costruzioni di muratura in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018),
  **paragrafo 7.8.1**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.8.1 (pagine PDF 261-262) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per i valori dei materiali, i fattori αu/α1 e la Tab. 7.8.I; trascritto verbatim in
    `references/fonti/ntc2018-par-7-8-1.md`.
- Estratto operativo `references/estratti/muratura-sismica-checklist.md`.
- Due task: `inquadra-materiali-fattori-comportamento.md` e `verifica-requisiti-geometrici-pareti.md`.
- Due esempi: requisiti dei materiali e scelta di αu/α1 per una muratura ordinaria; verifica dei requisiti
  geometrici di una parete (Tab. 7.8.I).

### Contenuto ancorato al testo
- Premessa (§7.8.1.1): muratura moderatamente dissipativa → CD"B"; coefficienti parziali del Cap. 4 riducibili
  del 20% e comunque ≥ 2. Materiali (§7.8.1.2, oltre §4.5.2, per agS > 0,075g): vuoti ≤ 45%; f_bk ≥ 5 MPa (o
  f_b ≥ 6 MPa) in direzione portante; f_bk ≥ 1,5 MPa perpendicolare; malta ≥ 5 MPa; limiti per giunti sottili
  (0,5-3 mm, solo agS ≤ 0,15g) e a secco (setti ≥ 7/10 mm, foratura ≤ 55%). Fattori di comportamento (§7.8.1.3):
  q = q0·KR (q0 Tab. 7.3.II); αu/α1 ≤ 2,5; in assenza di analisi non lineare ordinaria 1,7, armata 1,5 (1,3 con
  capacity design), confinata 1,6 (1,3 con capacity design). Requisiti geometrici (§7.8.1.4): piante compatte/
  simmetriche, pareti continue in elevazione (no pareti in falso), distanza max tra due solai ≤ 5 m; Tab. 7.8.I
  (t_min, (h0/t)max, (l/h')min): ordinaria pietra squadrata 300 mm/10/0,5; ordinaria artificiali 240/12/0,4;
  armata 240/15/qualsiasi; confinata 240/15/0,3; artificiali semipieni (agS≤0,075g) 200/20/0,3; pieni
  (agS≤0,075g) 150/20/0,3.

### Scope e limiti
- Non esegue le verifiche dei pannelli (pressoflessione/taglio, §§ 7.8.2-7.8.4) né i metodi di analisi
  (§7.8.1.5); non progetta l'armatura né i dettagli/cordoli (§§ 7.8.1.7-7.8.5); non tratta i requisiti statici
  (§4.5) né il fattore q generale (§7.3.1). Non sostituisce il progettista.

### Note di sviluppo
- Distinta da `costruzioni-muratura-ntc` (§4.5, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1).
  Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere strutturista esperto di
  muratura.
