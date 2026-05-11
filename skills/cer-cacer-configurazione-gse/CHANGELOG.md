# CHANGELOG - cer-cacer-configurazione-gse

Il formato e' basato su Keep a Changelog e questa skill aderisce a Semantic Versioning.

## [Unreleased]

## [0.1.1] - 2026-05-11

### Fixed (source-grounding)
- sostituite le fonti speculative/non verificate con sole fonti ufficiali GSE effettivamente lette e trascritte
- aggiunti `references/fonti/` per Regole Operative CACER, portale GSE Autoconsumo e pagina GSE PNRR
- riscritti estratti, task e skill per limitare la logica ai contenuti operativi effettivamente verificati
- rimosse dalla logica operativa affermazioni normative non trascritte su DM successivi, TIAD e decreto legislativo
- trasformata la skill in pre-check operativo GSE, non in consulenza normativa completa su CER
