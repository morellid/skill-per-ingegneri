# Changelog - fattore-comportamento-q-sismica-ntc

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-22

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento del **comportamento strutturale**
  (dissipativo / non dissipativo, classi di duttilità CD"A"/CD"B", progettazione in capacità) secondo il
  **§7.2.2** e del **fattore di comportamento q** (qlim = q0·KR [7.3.1], non dissipativo [7.3.2]) secondo il
  **§7.3.1** delle **NTC 2018** (D.M. 17 gennaio 2018).
- Fonte: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), SHA256
  `dda1e397...`, trascritto verbatim in `references/fonti/ntc2018-par-7-2-2-7-3-1.md`.
- Due task: `inquadra-comportamento-strutturale` e `inquadra-fattore-comportamento-q`.
- Due esempi: scelta comportamento/classe di duttilità per un edificio in c.a.; qlim per una struttura a telaio in
  c.a. CD"A".
- Formule [7.3.1], [7.3.2] e Tab. 7.3.II verificate sul testo e sull'immagine delle pagine PDF 220-221 (pdftotext
  perde gli operatori ·, =, ≤, /).
