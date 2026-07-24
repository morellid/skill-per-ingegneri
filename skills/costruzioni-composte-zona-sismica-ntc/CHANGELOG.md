# CHANGELOG - costruzioni-composte-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #462)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle regole
  generali** delle **costruzioni composte di acciaio-calcestruzzo in zona sismica** secondo le **NTC 2018** (DM
  17 gennaio 2018), **paragrafo 7.6**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.6 (pagine PDF 251-253) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per classi cls, B450C, n=7, q0, EU,Rd=1,1·γov·Epl,Rd e NEd/Npl,Rd≤0,3; trascritto verbatim in
    `references/fonti/ntc2018-par-7-6.md`.
- Estratto operativo `references/estratti/composte-sismica-checklist.md`.
- Due task: `inquadra-materiali-tipologie-fattore-q.md` e `verifica-requisiti-capacity-design.md`.
- Due esempi: materiali/tipologia e q0 di un telaio composto; capacity design e limite NEd/Npl,Rd di una colonna
  dissipativa.

### Contenuto ancorato al testo
- Comportamenti (§7.6): a) non dissipativo (→ §4.3); b) dissipativo con zone dissipative in membrature composte;
  c) dissipativo con zone dissipative in acciaio (integrità del cls compresso). Materiali (§7.6.1): cls non
  inferiore a C20/25 o LC20/22 e non superiore a C40/50 o LC40/44; acciaio per c.a. B450C (B450A solo casi
  §7.4.2.2); acciaio strutturale §7.5 e §11.3.4. Tipologie e fattori (§7.6.2): a) intelaiate, b) controventi
  concentrici in acciaio, c) controventi eccentrici (connessioni in acciaio), d) mensola/pendolo inverso, e)
  intelaiate controventate; pareti/nuclei c.a. → §7.4; q0 max Tab. 7.3.II. Rigidezza (§7.6.3): coefficiente di
  omogeneizzazione n=Ea/Ecm=7 (cls compresso); I1 non fessurato, I2 fessurato. Capacity design (§7.6.4): EU,Rd =
  1,1·γov·Epl,Rd (γov §7.5.1); Rj,d ≥ RU,Rd [7.6.1]; pannello d'anima Vwp,Rd = 0,8·(Vwp,s,Rd + Vwp,c,Rd) [7.6.2]
  se differenza altezze ≤ 40%; μ = θu/θy (θu al −15%); colonne primarie dissipative dei telai NEd/Npl,Rd ≤ 0,3
  [7.6.3]; rapporti larghezza/spessore solo acciaio §7.5.6, rivestite in cls Tab. 7.6.I.

### Scope e limiti
- Non esegue le verifiche di dettaglio RES/DUT né le regole per tipologia/elemento e i dettagli costruttivi (§§
  7.6.4-7.6.8, Tab. 7.6.I-IV); non calcola il q0 numerico (Tab. 7.3.II); non tratta i requisiti statici (§4.3),
  le regole sismiche dell'acciaio (§7.5) né il fattore q (§7.3.1). Non sostituisce il progettista.

### Note di sviluppo
- Distinta da `costruzioni-composte-acciaio-cls-ntc` (§4.3, statica), `costruzioni-acciaio-zona-sismica-ntc`
  (§7.5) e `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la fonte GU con le altre skill NTC. Nota: il
  coefficiente è γov (gamma), verificato sull'immagine perché pdftotext lo altera in «·ov». Validazione Livello 2
  con ingegnere strutturista esperto di strutture composte.
