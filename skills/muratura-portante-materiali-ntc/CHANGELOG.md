# CHANGELOG - muratura-portante-materiali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #464)
- Prima versione della skill di supporto al **progettista strutturale** e al **Direttore dei Lavori** per la
  **qualificazione dei materiali** e la **determinazione dei parametri meccanici** della **muratura portante**
  secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.10** (Cap. 11), nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.10 (pagine PDF 365-368) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per le Tab. 11.10.I/II/V/VI/VII/VIII e le formule di accettazione; trascritto verbatim in
    `references/fonti/ntc2018-par-11-10.md`.
- Estratto operativo `references/estratti/muratura-materiali-checklist.md`.
- Due task: `inquadra-elementi-e-malte.md` e `determina-fk-e-fvk0.md`.
- Due esempi: categoria elementi + classe malta + accettazione; stima di fk dalla Tab. 11.10.VI con fbk = 0,8·fbm.

### Contenuto ancorato al testo
- Elementi (§11.10.1): UNI EN 771 + Marcatura CE; Tab. 11.10.I Categoria I → sistema 2+, Categoria II → sistema 4;
  Cat. I con probabilità di insuccesso ≤ 5%; γM al §4.5.6. Accettazione (§11.10.1.1): laboratorio art. 59 DPR
  380/2001; 1 campione ogni 350 m³ (Cat. II) / 650 m³ (Cat. I); n ≥ 6; media ≥ fbm [11.10.1] e f1 ≥ 0,80·fbm
  [11.10.2]; oppure f1 ≥ fbk. Malte (§11.10.2): classe M (fm in N/mm², Tab. 11.10.II M2,5-M20/Md); non ammesse
  fm < 2,5 per muratura portante; a prestazione garantita (sistema 2+) / a composizione prescritta (sistema 4,
  Tab. 11.10.V) / in cantiere; accettazione 3 provini 40×40×160 ogni 350 m³ o 700 m³. Parametri (§11.10.3): fk
  sperimentale su n muretti (n ≥ 6, UNI EN 1052-1) o stimata da Tab. 11.10.VI (artificiali) e 11.10.VII (naturali),
  con fbk = 0,8·fbm (artificiali) o 0,75·fbm (naturali) [11.10.3], validità giunti 5-15 mm, interpolazione lineare
  e mai estrapolazione; fvk0 (assenza di tensioni normali) sperimentale (n ≥ 6, UNI EN 1052-3) o stimata da Tab.
  11.10.VIII (laterizio 0,30/0,20/0,10; silicato di calcio e cls 0,20/0,15/0,10; malta strati sottili e alleggerita).

### Scope e limiti
- Non esegue le verifiche di progetto né calcola le resistenze di progetto (fd = fk/γM); non tratta fvk con
  tensioni normali (§11.10.3.3) né i moduli di elasticità (§11.10.3.5); non tratta il progetto (§4.5), la sismica
  (§7.8) né l'accettazione di cls/acciaio (§§11.2/11.3). Non sostituisce il progettista né il Direttore dei Lavori.

### Note di sviluppo
- Distinta da `costruzioni-muratura-ntc` (§4.5), `costruzioni-muratura-zona-sismica-ntc` (§7.8.1) e
  `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3). Condivide la fonte GU con le altre skill NTC. Validazione
  Livello 2 con ingegnere strutturista esperto di muratura / Direttore dei Lavori.
