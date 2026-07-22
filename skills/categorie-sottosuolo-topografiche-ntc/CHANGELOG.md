# Changelog - categorie-sottosuolo-topografiche-ntc

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-22

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento della **classificazione sismica del sito**
  (categorie di sottosuolo A-E via Vs,eq, categorie topografiche T1-T4) secondo il **§3.2.2** delle **NTC 2018**
  (D.M. 17 gennaio 2018).
- Fonte: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), SHA256
  `dda1e397...`, trascritto verbatim in `references/fonti/ntc2018-par-3-2-2.md`.
- Due task: `classifica-categoria-sottosuolo` e `classifica-categoria-topografica`.
- Due esempi: attribuzione della categoria di sottosuolo da un profilo Vs stratificato; categoria topografica di
  un pendio.
- Formula [3.2.1] e Tab. 3.2.II/3.2.III verificate sul testo e sull'immagine delle pagine PDF 50-51 (pdftotext
  perde frazione, sommatoria e operatori ≤, >).
