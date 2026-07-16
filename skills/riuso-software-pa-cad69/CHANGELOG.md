# CHANGELOG - riuso-software-pa-cad69

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #51)
- Prima versione della skill di supporto agli obblighi di **acquisizione, riuso e
  rilascio in open source** del software delle PA (C.A.D. artt. 68-69) e alla
  documentazione AgID a corredo, nell'area `software-dati-cybersecurity`.
- Aggiunti gli host istituzionali **agid.gov.it** e **developers.italia.it** alla
  allowlist della CI (`OFFICIAL_HOST_SUFFIXES` in `verify-sources.py`).
- Fonti scaricate, hashate e lette (Regola zero):
  - **C.A.D. (D.Lgs. 82/2005)** artt. 68-69 - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 5e75c6b9215888cba2dd5d118c6aa3baf6b3d26eee09d54af7c2f84e20f28222
    (codice 005G0104). Articoli via caricaArticolo.
  - **AgID - Linee guida su acquisizione e riuso di software per le PA** - PDF ufficiale
    su agid.gov.it, SHA256: 41925c4dae94c5a8b7ab5b39be03563dc80e033705b503710792d297cd225a43
    (101 pagine, riproducibile). Estratti verbatim dell'Allegato A (A.7, A.8, A.9, A.11).
  - Trascrizioni in `references/fonti/riuso-software-pa.md`.
- Estratto operativo `references/estratti/riuso-software-checklist.md`.
- Due task: `imposta-analisi-comparativa.md` e `prepara-rilascio-open-source.md`.
- Due esempi: obbligo di rilascio di un gestionale comunale; formati ammessi per la
  documentazione (no PDF/DOCX per la documentazione tecnica).

### Contenuto ancorato al testo
- Art. 68 (analisi comparativa); art. 69 (obbligo di rilascio del codice sorgente sotto
  licenza aperta). Allegato A Linee guida: README (A.7), documentazione versionabile
  (A.8), tempi 15 gg (A.9), publiccode.yml + Developers Italia (A.11).

### Scope e limiti
- Non sceglie la licenza; non riproduce il formato campo-per-campo del publiccode.yml
  (standard Developers Italia, richiamato non riprodotto); non esegue la valutazione
  comparativa tecnica. Complementare a `specifiche-tecniche-ict-appalti-dlgs36` (#50).

### Note di sviluppo
- Normattiva/AgID: ad ogni aggiornamento riscaricare l'indice C.A.D. pinnato (nuovo hash)
  e verificare nuove versioni delle Linee guida su agid.gov.it (nuovo hash del PDF).
- Validazione Livello 2 con RTD / esperto open source PA.
