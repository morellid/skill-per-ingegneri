# CHANGELOG - denuncia-opere-strutturali-l1086

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-22

### Added
- Prima versione alpha della skill: diagnosi adempimenti strutturali e
  sismici ex DPR 380/2001 (artt. 65, 67, 83, 93, 94, 94-bis).
- Fonte normativa: DPR 6 giugno 2001 n. 380 testo multivigente Normattiva
  al 2026-05-22 (sha256 verificato, trascrizione fedele committata in
  `references/fonti/`).
- 3 estratti operativi: art. 65 (denuncia c.a./c.a.p./metalliche),
  art. 67 (collaudo statico), artt. 93-94-94-bis (zona sismica).
- 4 task files: diagnosi adempimenti, checklist art. 65, checklist
  zona sismica, checklist collaudo.
- 2 esempi: villetta c.a. zona 3 (caso conforme), scuola zona 2 ag=0,22 g
  (caso problematico - rifiuto qualificazione opportunistica come
  intervento locale).

### Limiti noti v0.1
- Classificazione operativa ex art. 94-bis c. 2 delegata a discipline
  regionali (rinvio strutturale).
- Distinzione adeguamento/miglioramento/intervento locale e' tema NTC
  2018 cap. 8 - di competenza del progettista strutturale firmatario.
- Sanzioni artt. 71-76 e 95 e ss. DPR 380 fuori scope.
- Titolo edilizio (PdC/SCIA/CILA) fuori scope: vedi skill
  `modulistica-edilizia-unificata`.

### Validazione
- Livello 1 (source-grounded sul DPR 380 Normattiva).
- Livello 2 (revisione ingegnere strutturista esperto pratiche genio
  civile): non ancora effettuata, skill in stato `alpha`.
