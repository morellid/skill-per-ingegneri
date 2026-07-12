# CHANGELOG - cedimenti-edometrici-ntc

## [Unreleased]

## [0.2.0] - 2026-07-12

### Added (reintroduzione calcolatore su fonte pubblica - closes #32)
- Nuova fonte primaria **FHWA NHI-06-088 "Soils and Foundations - Reference Manual Volume I"** (U.S. DOT, dicembre 2006, pubblico dominio, "No restrictions"):
  - URL ufficiale https://www.fhwa.dot.gov/engineering/geotech/pubs/nhi06088.pdf
  - SHA256: f970902490ea97b07225f0eea51402dfe4c4988229aab8a0f0336429357340b4 (riproducibile, doppio download verificato)
  - trascrizione parr. 7.5.2 (eq. 7-2..7-7) e 5.4.6.1 in `references/fonti/fhwa-nhi-06-088.md`
- Trascrizione del **cap. 12 NTC 2018** ("altri codici internazionali") aggiunta a `references/fonti/ntc2018-dm-17-01-2018.md`: e' l'aggancio normativo per l'uso della fonte FHWA
- Nuovo estratto `references/estratti/fhwa-consolidazione-primaria.md`
- Nuovo modulo `tasks/lib/cedimento_edometrico.py` (+ 15 test): eq. [7-2] NC, [7-4] OC con pf > pc, [7-6] sottoconsolidato dichiarato; multistrato con somma; rifiuto esplicito dei casi non coperti (OC con sigma_f <= sigma_p; OCR < 1 non dichiarato)
- Nuovo task `tasks/calcola-cedimento-edometrico.md`

### Changed
- SKILL.md riscritto: due sotto-attivita' (calcolo + verifica documentale); normative_refs con FHWA NHI-06-088 e NTC cap. 12
- `tasks/calcola-cedimento.md` rinominato in `tasks/check-verifica-cedimenti.md` (contenuto: verifica documentale invariata, con rinvio al nuovo task di calcolo)
- Esempi riscritti sull'output reale del nuovo modulo: caso conforme OC con transizione (110,1 mm, eq. [7-4]); caso problematico OCR < 1 (rifiuto di default; eq. [7-6] solo con dichiarazione di sottoconsolidazione ex FHWA 7.5.2.3 - comportamento migliorato rispetto al vecchio "fisicamente non ammissibile")
- AGENTS.md e agents/openai.yaml riallineati (erano rimasti alla versione pre-remediation 0.1.0)
- Rimosso il tombstone `references/estratti/formulazione-edometrica-classica.md`

### Nota di conformita' (Regola zero)
Il calcolatore rimosso nella 0.1.1 torna perche' ora la formulazione e' trascritta da fonte pubblica scaricata e hashata; il modulo implementa le SOLE equazioni trascritte e rifiuta i casi che la fonte non copre, senza integrare da training data.

## [0.1.1] - 2026-05-11

### Fixed (source-grounding)
- aggiunti hash reali e `references/fonti/` per NTC 2018 e Circolare 7/2019
- rimossa dalla logica della skill l'implementazione del calcolatore basato su formulazioni non presenti nelle fonti ufficiali lette
- riscritta la skill come strumento di verifica documentale/completa dei cedimenti SLE
- rimossi il modulo Python e i test numerici non source-grounded
- riscritti task, estratti ed esempi per limitare le affermazioni a contenuti normativi tracciabili
