# Changelog - isolamento-sismico-ntc

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-23

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento delle **costruzioni con isolamento e/o
  dissipazione sismica** (scopo e strategie, requisiti, dispositivi, modellazione/analisi, verifiche SLE/SLV/SLC)
  secondo il **§7.10** delle **NTC 2018** (D.M. 17 gennaio 2018).
- Fonte: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), SHA256
  `dda1e397...`, trascritto verbatim in `references/fonti/ntc2018-par-7-10.md`.
- Due task: `inquadra-scopo-requisiti-dispositivi` e `inquadra-modellazione-analisi-verifiche`.
- Due esempi: applicabilità dell'analisi statica lineare a un edificio isolato; verifiche SLD/SLV/SLC di una
  costruzione isolata.
- Le soglie di §7.10 (800, 50%/30%/10%/2,5%, 3·Tbf, TV<0,1 s, q≤1,50, ≥1,5) verificate sul testo e sull'immagine
  delle pagine PDF 279 e 281 (pdftotext altera operatori, pedici e radici).
