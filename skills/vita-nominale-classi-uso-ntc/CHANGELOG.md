# Changelog - vita-nominale-classi-uso-ntc

Tutte le modifiche rilevanti a questa skill sono documentate qui.

## [0.1.0-alpha] - 2026-07-22

### Aggiunto

- Prima versione della skill: supporto documentale per l'inquadramento di **vita nominale di progetto V_N**
  (§2.4.1), **classi d'uso** (§2.4.2) e **periodo di riferimento per l'azione sismica V_R = V_N · C_U** (§2.4.3)
  secondo le **NTC 2018** (D.M. 17 gennaio 2018), par. 2.4.
- Fonte: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), SHA256
  `dda1e397...`, trascritto verbatim in `references/fonti/ntc2018-par-2-4.md`.
- Due task: `inquadra-vita-nominale-classe-uso` e `inquadra-periodo-riferimento-vr`.
- Due esempi: scelta V_N/classe d'uso/V_R per un edificio residenziale ordinario e ricavo di V_R per una scuola
  (Classe III).
- Costanti (V_N 10/50/100, C_U 0,7/1,0/1,5/2,0, formula [2.4.1]) verificate sul testo e sull'immagine della
  pagina PDF.
