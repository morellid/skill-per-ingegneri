# Changelog - verifiche-geotecniche-slu-ntc

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-22

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento del **framework delle verifiche geotecniche
  agli stati limite ultimi** (SLU EQU/STR/GEO, approcci progettuali 1 e 2, coefficienti parziali A/M/R) secondo il
  **§6.2.4** delle **NTC 2018** (D.M. 17 gennaio 2018), con il valore caratteristico del **§6.2.2**.
- Fonte: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), SHA256
  `dda1e397...`, trascritto verbatim in `references/fonti/ntc2018-par-6-2-4.md`.
- Due task: `inquadra-approcci-progettuali-slu` e `inquadra-coefficienti-parametri-geotecnici`.
- Due esempi: scelta dell'approccio e delle combinazioni per uno SLU GEO non trattato specificamente; applicazione
  dei coefficienti M2 ai parametri del terreno.
- Tab. 6.2.I e 6.2.II verificate sul testo e sull'immagine della pagina PDF 190 (pdftotext altera pedici,
  operatori e la notazione delle combinazioni).
