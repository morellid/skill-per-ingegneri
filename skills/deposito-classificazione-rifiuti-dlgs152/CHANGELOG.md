# CHANGELOG - deposito-classificazione-rifiuti-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #278)
- Prima versione della skill di supporto alla **classificazione dei rifiuti** e al **deposito
  temporaneo prima della raccolta**, ai sensi degli **artt. 183, 184, 185-bis del D.Lgs. 3 aprile
  2006, n. 152** (Parte quarta), nell'area `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 3 aprile 2006, n. 152** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: fac1fb98fa463fc91ac96e641197c5628729cd62699a6d4ae5761d4873631e40
    (codice 006G0171). Artt. 183, 184, 185-bis via `caricaArticolo` (idGruppo 34).
  - Trascrizione verbatim in `references/fonti/dlgs-152-2006-artt-183-184-185bis.md`: artt. 183,
    184 e 185-bis per intero (testo vigente, con i blocchi (( )) dei provvedimenti successivi).
- Estratto operativo `references/estratti/rifiuti-checklist.md`.
- Due task: `classifica-rifiuto.md` e `imposta-deposito-temporaneo.md`.
- Due esempi: rifiuti da costruzione e demolizione (speciali); deposito temporaneo di rifiuti
  pericolosi (limiti 30/10 mc, trimestrale, 1 anno).

### Contenuto ancorato al testo
- Art. 183 definizioni (rifiuto, produttore, detentore, deposito temporaneo, sottoprodotto,
  rifiuto urbano). Art. 184 classificazione (urbani/speciali; pericolosi/non pericolosi; EER
  allegato D vincolante; codici a cura del produttore; divieto di declassificazione per
  diluizione - c. 5-ter). Art. 185-bis deposito temporaneo (luogo di produzione; cadenza almeno
  trimestrale oppure 30 mc di cui max 10 mc pericolosi; durata max 1 anno; categorie omogenee;
  esonero da autorizzazione - c. 3).

### Scope e limiti
- Non attribuisce i codici EER ne' riproduce l'allegato D / allegato I (HP): rinvio agli allegati
  e alle Linee guida SNPA. Non redige registri (art. 190), FIR (art. 193), MUD: cfr.
  `trasporto-rifiuti-fir-dlgs152`. Non sostituisce il produttore/detentore ne' il consulente.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 152/2006 pinnato (nuovo hash)
  e verificare le modifiche (es. D.Lgs. 116/2020; testo tra `(( ))`).
- Validazione Livello 2 con tecnico ambientale / consulente rifiuti.
