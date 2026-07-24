# CHANGELOG - dispositivi-antisismici-qualificazione-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #470)
- Prima versione della skill di supporto al **progettista strutturale**, al **Direttore dei Lavori** e al
  **collaudatore** per la **qualificazione** e i **controlli di accettazione in cantiere** dei **dispositivi
  antisismici e di controllo delle vibrazioni** (isolatori, dissipatori, dispositivi di vincolo) secondo le
  **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.9** (Cap. 11), nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.9 (pagine PDF 358-364) estratto con `pdftotext -layout`; **tutti** i valori numerici (tabelle Tab.
    11.9.I-IV, formule [11.9.1]-[11.9.9], numerosità delle prove) verificati sull'immagine (`pdftoppm -r 150 -png`)
    delle pagine PDF 358/360/361/362/363/364 e trascritti verbatim in `references/fonti/ntc2018-par-11-9.md`.
- Estratto operativo `references/estratti/dispositivi-antisismici-checklist.md`.
- Due task: `inquadra-tipologie-e-qualificazione.md` e `imposta-accettazione-e-prove-per-tipo.md`.
- Due esempi: accettazione in cantiere di isolatori elastomerici con campionamento del Direttore dei Lavori;
  qualificazione di dissipatori viscosi.

### Contenuto ancorato al testo
- Generalità (§11.9): vita di servizio > 10 anni; campo di temperatura in assenza di indicazioni almeno −15 °C /
  +45 °C; piani di manutenzione/sostituzione; UNI EN 15129 (dbd = spostamento SLV; γx·dbd = SLC). Tipologie
  (§11.9.1): vincolo temporaneo (a fusibile/provvisorio), dipendenti dallo spostamento (lineari/non lineari),
  viscosi, isolatori (elastomerici/a scorrimento), combinazioni. Qualificazione (§11.9.2): punto A del §11.1 → UNI
  EN 15129 + Marcatura CE (sistema VVCP per applicazioni critiche); non ricadenti → caso C del §11.1; manuale di
  posa/manutenzione. Accettazione (§11.9.3): obbligatoria per tutte le tipologie, demandata al Direttore dei Lavori
  (campionamento sui lotti del cantiere, verifica geometrica/tolleranze, rifiuto non conformi); prove certificate da
  laboratorio art. 59 DPR 380/2001 (FPC tests). Prove e limiti per tipo (§11.9.4-11.9.10): ≥ 20% dei dispositivi e
  comunque ≥ 4; prova quasi statica ≥ 5 cicli ±d2; Tab. 11.9.I-IV; lineari ξe < 15% e |Ke−Kin|/Kin < 20%; non
  lineari del = d2/20 e K2/K1 ≤ 0,05 → 0,01; viscosi γv = (1+td)·(1,5)^α, rotazione ≥ 2°, forza trasversale ≥ 2×
  peso; elastomerici piastre 18% e spessore 2/20 mm, frequenze 0,1/0,5 Hz, carico verticale ≤ 15%; scorrimento
  attrito ≤ 25% e 1,25 d2; fusibile ±10%, 3 cicli monotonici, forza di rilascio ±15%; vincolo provvisorio corsa ≥
  ±50 mm ponti / ±25 mm edifici e FS sovrappressioni 1,5 (o ≥ 1,1) e velocità 0,5-5 mm/s.

### Scope e limiti
- Non esegue il progetto delle costruzioni con isolamento/dissipazione né dimensiona i dispositivi (§7.10); non
  tratta la qualificazione dei materiali del Cap. 11 (cls/acciaio §§11.2/11.3). Non sostituisce il progettista, il
  Direttore dei Lavori né il laboratorio ex art. 59.

### Note di sviluppo
- Distinta da `isolamento-sismico-ntc` (§7.10, progetto), che rinvia esplicitamente al §11.9 come fuori scope, e
  dalle skill materiali del Cap. 11. Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con
  ingegnere strutturista esperto di isolamento sismico / collaudatore.
