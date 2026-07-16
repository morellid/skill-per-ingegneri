# CHANGELOG - verifica-accessibilita-dichiarazione-agid

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #247)
- Prima versione della skill di supporto al **metodo di verifica dell'accessibilita'**
  (verifica tecnica + verifica soggettiva) e alla **dichiarazione di accessibilita'** degli
  strumenti informatici, secondo le **Linee guida AgID** (ex art. 11 L. 4/2004, versione
  21/12/2022), nell'area `software-dati-cybersecurity`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **AgID - Linee guida sull'accessibilita' degli strumenti informatici** (21/12/2022),
    PDF ufficiale su agid.gov.it, SHA256:
    9043373eef2c585a9ffc09739fa4a156603d27e4abe189b8399eaf7d150f95e8
    (39 pagine, testo nativo, riproducibile). Estratti verbatim dei capitoli 2, 3, 4, 6, 7
    in `references/fonti/linee-guida-accessibilita-agid.md`.
- Estratto operativo `references/estratti/accessibilita-verifica-checklist.md`.
- Due task: `imposta-verifica-accessibilita.md` e `predisponi-dichiarazione-accessibilita.md`.
- Due esempi: verifica soggettiva obbligatoria sopra soglia comunitaria; riesame annuale
  della dichiarazione (23 settembre) e obiettivi annuali PA (31 marzo).

### Contenuto ancorato al testo
- Requisiti Web / WCAG 2.1 AA e punto 9 EN 301549 (cap. 2); verifica tecnica e verifica
  soggettiva a 4 fasi con scala 1-5, livelli di qualita' e 12 criteri essenziali,
  obbligatoria sopra soglia art. 35 D.Lgs 50/2016 (cap. 3); dichiarazione sulla piattaforma
  AgID, link nel footer, riesame 23 settembre, art. 9 L. 4/2004, obiettivi annuali PA 31
  marzo (cap. 4); onere sproporzionato art. 3-ter L. 4/2004 e casi a-h (cap. 6); feedback
  (art. 3-bis) e Difensore civico digitale (art. 3-quinquies, 30 giorni) (cap. 7).

### Scope e limiti
- Non esegue l'audit tecnico WCAG/EN 301549 ne' la verifica soggettiva; non riproduce la
  norma UNI CEI EN 301549 (a pagamento) ne' le WCAG; non compila la dichiarazione sulla
  piattaforma AgID; non copre gli obblighi/sanzioni della L. 4/2004 (complementare a
  `accessibilita-siti-app-l4-2004`).

### Note di sviluppo
- AgID: ad ogni aggiornamento riscaricare le Linee guida sull'accessibilita' su agid.gov.it
  (nuovo hash del PDF) e verificare gli aggiornamenti della EN 301549 e delle WCAG richiamate.
- Validazione Livello 2 con esperto di accessibilita' / RTD.
