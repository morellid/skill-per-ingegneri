# CHANGELOG - materiali-legno-strutturale-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #466)
- Prima versione della skill di supporto al **progettista strutturale** e al **Direttore dei Lavori** per la
  **qualificazione** e le **proprietà** dei **materiali e prodotti a base di legno** per uso strutturale secondo
  le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.7** (Cap. 11), nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.7 (pagine PDF 349-350 e seguenti) estratto con `pdftotext -layout` e verificato sull'immagine
    (`pdftoppm -r 150 -png`) per la Tab. 11.7.I, le formule di kh e le condizioni di prova; trascritto verbatim
    in `references/fonti/ntc2018-par-11-7.md`.
- Estratto operativo `references/estratti/legno-materiali-checklist.md`.
- Due task: `inquadra-proprieta-e-profilo-resistente.md` e `qualifica-prodotti-e-accettazione.md`.
- Due esempi: profilo resistente + coefficiente kh per una trave in legno massiccio; qualificazione di un prodotto
  in legno lamellare.

### Contenuto ancorato al testo
- Generalità (§11.7.1): qualificazione §11.1 (caso A marcatura CE / B qualificazione / C Linee Guida CSLP);
  sistema qualità e rintracciabilità; il Direttore dei Lavori rifiuta le forniture non conformi ed effettua i
  controlli di accettazione (§11.7.10.2); laboratori art. 59 DPR 380/2001 o notificati (D.Lgs 106/2017 + Reg. UE
  305/2011). Proprietà (§11.7.1.1): valori caratteristici = frattile 5%; prove 300 s a 20±2 °C e UR 65±5%; profilo
  resistente Tab. 11.7.I (fm,k, ft,0,k, ft,90,k, fc,0,k, fc,90,k, fv,k; E0,mean, E0,05, E90,mean, Gmean; ρk,
  ρmean); kh massiccio min[(150/h)^0,2;1,3] [11.7.1], lamellare min[(600/h)^0,1;1,1] [11.7.2]. Prodotti
  (§11.7.2-11.7.6): massiccio UNI EN 14081-1 + CE, classi UNI EN 338, profili UNI 11035, prove UNI EN 384; giunti
  a dita caso C (UNI EN 14081-1, ISO 9001); lamellare/massiccio incollato UNI EN 14080, tavole UNI EN 14081-1,
  classi > C30 solo classificazione a macchina; pannelli UNI EN 13986 (valori UNI EN 12369); altri derivati caso C.
  Accettazione (§11.7.10): identificazione/rintracciabilità e controlli in cantiere a cura del Direttore dei Lavori.

### Scope e limiti
- Non esegue le verifiche di progetto né calcola le resistenze di progetto (fd = kmod·fk/γM); non tratta in
  dettaglio adesivi (§11.7.7), collegamenti (§11.7.8) e durabilità (§11.7.9); non tratta il progetto (§4.4), la
  sismica (§7.7) né l'accettazione di muratura/cls/acciaio (§§11.10/11.2/11.3). Non sostituisce il progettista né
  il Direttore dei Lavori.

### Note di sviluppo
- Distinta da `costruzioni-legno-ntc` (§4.4), `costruzioni-legno-zona-sismica-ntc` (§7.7),
  `muratura-portante-materiali-ntc` (§11.10) e `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3). Condivide la
  fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere strutturista esperto di legno / Direttore
  dei Lavori.
