# Changelog - requisiti-acustici-passivi-edifici-dpcm

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-23

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento dei **requisiti acustici passivi degli
  edifici** (classificazione degli ambienti in categorie, grandezze e indici di valutazione, valori limite,
  rumore degli impianti) secondo il **DPCM 5 dicembre 1997**.
- Fonte: PDF ufficiale della Gazzetta Ufficiale (Serie Generale n. 297 del 22/12/1997), SHA256
  `5a8ae1f4...`, riproducibile via doppio download; contenuto letto renderizzando le pagine in immagine
  (`pdftoppm`) perché il PDF GURITEL non è estraibile con `pdftotext`, e trascritto verbatim in
  `references/fonti/dpcm-5-12-1997.md`.
- Due task: `classifica-ambiente-e-valori-limite` e `inquadra-grandezze-e-rumore-impianti`.
- Due esempi: valori limite per un edificio residenziale (categoria A); rumore degli impianti tecnologici per una
  scuola (categoria E).
- Tab. A, Tab. B e le costanti dell'Allegato A (T0 = 0,5 s; 35/25 dB(A)) verificate direttamente sull'immagine
  delle pagine PDF 5-7.
