# CHANGELOG - componenti-prefabbricati-ca-cap-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #468)
- Prima versione della skill di supporto al **progettista strutturale**, al **Direttore dei Lavori** e ai
  **produttori** per la **qualificazione**, il **controllo di produzione** e l'**accettazione** dei **componenti
  prefabbricati in c.a. e c.a.p.** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.8** (Cap. 11),
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.8 (pagine GU 351-353 = pagine PDF 355-357) estratto con `pdftotext -layout` e verificato sull'immagine
    (`pdftoppm -r 150 -png`) delle pagine PDF 356/357 per le frequenze delle prove, i registri, la marchiatura e le
    validità quinquennali; trascritto verbatim in `references/fonti/ntc2018-par-11-8.md`.
- Estratto operativo `references/estratti/prefabbricati-checklist.md`.
- Due task: `inquadra-qualificazione-e-controllo-produzione.md` e `verifica-marchiatura-e-documenti-accettazione.md`.
- Due esempi: qualificazione di una serie in stabilimento; accettazione in cantiere di una fornitura di elementi
  prefabbricati con verifica marchiatura e certificato d'origine.

### Contenuto ancorato al testo
- Generalità (§11.8.1): processo industrializzato + sistema permanente di controllo della produzione in
  stabilimento (comprende il cls secondo §11.2); per elementi qualificati ai punti A/C del §11.1 assolti i
  requisiti procedurali del deposito art. 58 DPR 380/2001 (restano gli adempimenti presso l'ufficio territoriale;
  art. 56 per pannelli portanti); Metodi 1/2/3 di dichiarazione delle prestazioni; materiali base qualificati
  all'origine (§11.1). Requisiti stabilimenti (§11.8.2): sili/contenitori, dosaggio a peso dei solidi, sequenza di
  controllo, sistema documentato. Controllo di produzione (§11.8.3): sistema qualità UNI EN ISO 9001; cls controllo
  continuo §11.2, apparecchiature tarate annualmente, registri 10 anni, prove a 28 giorni, resistenza
  caratteristica controllo tipo B in stabilimento, controlli esterni ≥ 1 prelievo ogni 5 giorni con controllo tipo
  A su 3 prelievi; acciaio piegatura 3 campioni ogni 90 t (min mensile, UNI EN ISO 15630-1), trazione 3 campioni
  ogni 10 rotoli, solo per prodotti privi di marcatura CE. Marchiatura (§11.8.3.4): fissa/indelebile per la
  rintracciabilità; per manufatti > 8 kN indicazione del peso. Qualificazione (§11.8.4): STC art. 58 DPR 380; serie
  dichiarata (§4.1.10.2.1) attestato quinquennale rinnovabile; serie controllata (§4.1.10.2.2) Certificato di
  Valutazione Tecnica quinquennale + prove a rottura su prototipo; sospensioni/revoche. Documenti (§11.8.5): il
  Direttore dei Lavori rifiuta le forniture non conformi; istruzioni trasporto/montaggio, disegni d'assieme,
  certificato d'origine, prove a compressione, verifica marchiatura (art. 65 DPR 380).

### Scope e limiti
- Non esegue il progetto degli elementi prefabbricati né le verifiche (§4.1.10); non tratta i controlli di
  accettazione generali di cls/acciaio (§§11.2/11.3) né la denuncia/collaudo statico (DPR 380). Non sostituisce il
  progettista né il Direttore dei Lavori.

### Note di sviluppo
- Distinta da `costruzioni-calcestruzzo-ntc` (§4.1), `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3) e
  `denuncia-collaudo-statico-ca-dpr380` (DPR 380). Condivide la fonte GU con le altre skill NTC. Validazione
  Livello 2 con ingegnere strutturista / Direttore tecnico di stabilimento di prefabbricati.
