# CHANGELOG - mog-231-reati-ambientali

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #63)
- Prima versione della skill di supporto documentale alla parte speciale ambientale
  del Modello di Organizzazione, Gestione e Controllo (MOG) ex D.Lgs 231/2001.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 8/6/2001 n. 231** - pagina indice Normattiva pinnata a
    `!vig=2026-07-15`
    SHA256: 73e26d0e0cd6289659b198c153eda69ef124417c3a7cac2d94ed655b5f4df76b
    (riproducibile, doppio download). Artt. 6 (modelli di organizzazione, funzione
    esimente, OdV), 7 (soggetti sottoposti all'altrui direzione) e 25-undecies
    (reati ambientali: ecoreati c.p. 452-bis ss.; D.Lgs 152/2006 artt. 137, 256,
    256-bis, 257, 258, 259, 260-bis, 279; L. 150/1992 CITES; L. 549/1993 ozono;
    D.Lgs 202/2007 navi; sanzioni pecuniarie a quote e interdittive; interdizione
    definitiva) letti via caricaArticolo e trascritti verbatim in
    `references/fonti/dlgs-231-2001.md`.
- Estratto operativo `references/estratti/reati-ambientali-231-mappa.md` (mappa
  reato -> area di compliance -> sanzione -> controlli della parte speciale).
- Due task: `mappa-reati-presupposto.md` e `struttura-parte-speciale.md`.
- Due esempi: gestione rifiuti (art. 256 e collegati); scarichi industriali (art.
  137) e funzione esimente del MOG.

### Note di source-grounding e scope
- La skill mappa i **reati presupposto** (art. 25-undecies) e la **funzione
  esimente** (artt. 6-7). Il **testo dei singoli reati** richiamati (c.p.; D.Lgs
  152/2006; L. 150/1992; L. 549/1993; D.Lgs 202/2007) e' citato per numero e NON
  riprodotto: per gli aspetti tecnici si rinvia alle skill ambientali del repo
  (scarichi/emissioni, rifiuti/FIR, bonifica). La valutazione legale della
  responsabilita' e la redazione del Modello sono fuori scope.
- **Area di catalogo**: `ambiente-territorio-mobilita` (dominio ambientale),
  coerente con la catalogazione per dominio delle altre skill di compliance del
  repo (GDPR/NIS2/DORA in software-dati-cybersecurity).

### Note di sviluppo
- Fonte Normattiva: l'art. 25-undecies e' frequentemente novellato (da ultimo D.L.
  116/2025 e L. 91/2025): ad ogni aggiornamento riscaricare la pagina pinnata
  (nuovo hash) e rileggere l'articolo.
- Validazione Livello 2 da effettuare con legale 231 / esperto compliance
  ambientale.
