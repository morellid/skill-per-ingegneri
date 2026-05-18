# CHANGELOG - cer-cacer-configurazione-gse

Il formato e' basato su Keep a Changelog e questa skill aderisce a Semantic Versioning.

## [Unreleased]

### Fixed (source-grounding)
- riclassificate `gse-portale-autoconsumo` e `gse-pnrr-cacer` come riferimenti istituzionali online URL-only: la skill le usa solo per instradamento operativo verso il portale GSE, non come snapshot HTML binary-backed

## [0.2.0] - 2026-05-18

### Added
- nuova fonte `gse-news-pnrr-facilities-concessione-cacer-20260512`: notizia GSE del 12/05/2026 sui primi atti di concessione PNRR Facilities CACER e notizie 8-9/05/2026 su riattivazione/esaurimento contatore M.7 I.17 (issue #170)
- nuova fonte `gse-pnrr-cer-5000-bando`: pagina GSE PNRR CER comuni <5000 ab., bando e atti di concessione, letta il 18/05/2026 (issue #170)
- sezione "Stato aggiornato PNRR Facilities CACER (maggio 2026)" in SKILL.md con:
  - conferma emissione primi atti di concessione PNRR CACER (12 maggio 2026, ai sensi art. 27 DL 19/2026)
  - scadenza del 30 giugno 2026 per stipula accordi di concessione da parte del GSE
  - scadenza finale 31 dicembre 2027 per entrata in esercizio impianti
  - risorse richieste al 30/11/2025: 1.456 Mln euro, 3.343,8 MW
  - nota disambiguante su misura M.7 I.17 (edifici pubblici, distinta da PNRR CACER)
- aggiornato `last_verified` in sources.yaml: 2026-05-18

## [0.1.1] - 2026-05-11

### Fixed (source-grounding)
- sostituite le fonti speculative/non verificate con sole fonti ufficiali GSE effettivamente lette e trascritte
- aggiunti `references/fonti/` per Regole Operative CACER, portale GSE Autoconsumo e pagina GSE PNRR
- riscritti estratti, task e skill per limitare la logica ai contenuti operativi effettivamente verificati
- rimosse dalla logica operativa affermazioni normative non trascritte su DM successivi, TIAD e decreto legislativo
- trasformata la skill in pre-check operativo GSE, non in consulenza normativa completa su CER
