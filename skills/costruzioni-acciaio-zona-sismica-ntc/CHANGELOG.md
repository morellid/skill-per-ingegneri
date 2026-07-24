# CHANGELOG - costruzioni-acciaio-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #458)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle regole
  generali** delle **costruzioni di acciaio in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018),
  **paragrafo 7.5**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.5 (pagine PDF 243-246) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per γov, αu/α1, Tab. 7.5.I e il limite NEd/Npl,Rd; trascritto verbatim in
    `references/fonti/ntc2018-par-7-5.md`.
- Estratto operativo `references/estratti/acciaio-sismica-checklist.md`.
- Due task: `inquadra-tipologie-materiali-fattore-q.md` e `verifica-requisiti-classe-sezione-dissipativi.md`.
- Due esempi: materiali/γov, tipologia e αu/α1 di un telaio in acciaio; classe della sezione per un elemento
  dissipativo (Tab. 7.5.I).

### Contenuto ancorato al testo
- Materiali (§7.5.1): acciaio conforme §11.3.4.9; fattore di sovraresistenza del materiale γov = 1,25 (S235/
  S275/S355) e 1,15 (S420/S460). Tipologie (§7.5.2.1): a) intelaiate; b) controventi concentrici (b1 diagonale
  tesa attiva, b2 a V, b3 a K non dissipativa); c) controventi eccentrici; d) a mensola/pendolo inverso (carico
  assiale normalizzato ≤ 0,3 → telaio); e) intelaiate con controventi; f) intelaiate con tamponature. Fattori di
  comportamento (§7.5.2.2): q0 max in Tab. 7.3.II; αu/α1 = 1,1 (un piano) / 1,2 (telaio più piani 1 campata) /
  1,3 (telaio più piani più campate) / 1,2 (controventi eccentrici) / 1,0 (mensola/pendolo inverso). Regole
  generali dissipativi (§7.5.3): zone dissipative nelle membrature; capacity design collegamenti 1,1·γov·Rpl,Rd;
  μ = θu/θy (θu al −15% della resistenza max); Tab. 7.5.I (CD"B" 2<q0≤4 → Classe 1 o 2; CD"A" q0>4 → Classe 1);
  colonne primarie dissipative dei telai NEd/Npl,Rd ≤ 0,3.

### Scope e limiti
- Non esegue le verifiche RES/DUT di membrature e collegamenti né le regole specifiche per tipologia (§§ 7.5.3.1-
  7.5.3.2, 7.5.4-7.5.6); non progetta i collegamenti; non calcola il q0 numerico (Tab. 7.3.II); non tratta i
  requisiti statici (§4.2) né il fattore q generale (§7.3.1). Non sostituisce il progettista.

### Note di sviluppo
- Distinta da `costruzioni-acciaio-ntc` (§4.2, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1).
  Condivide la fonte GU con le altre skill NTC. Nota: il coefficiente è γov (gamma), verificato sull'immagine
  perché pdftotext lo altera in «Jov»/«·ov». Validazione Livello 2 con ingegnere strutturista esperto di
  strutture in acciaio.
