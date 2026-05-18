# CHANGELOG - pratiche-edilizie-lr65-2014-toscana

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2026-05-18

### Added
- Recepimento DL 7 maggio 2026 n. 66 "Piano Casa" (GU n. 104, in vigore dall'8/05/2026)
- Nuova fonte `references/fonti/dl-66-2026-piano-casa.md` (PDF scaricato e SHA256 verificato)
- Nuovo estratto `references/estratti/dl-66-2026-piano-casa-erp.md` con analisi artt. 8 e 9
- Sezione "Norma sopravvenuta: DL 66/2026 Piano Casa" in SKILL.md
- Verifica preliminare DL 66/2026 aggiunta al task `determina-tipo-pratica.md`

### Analysis
- Art. 9 DL 66/2026 NON modifica DPR 380/2001 artt. 10/22 (confermato da lettura PDF)
- Art. 8 co. 1: SCIA per demolizione/ricostruzione ERP (per rinvio a DL 76/2020 art. 10 co. 7-ter)
- Edilizia privata ordinaria: quadro LR 65/2014 + DPR 380/2001 invariato

## [0.1.1] - 2026-05-11

### Fixed (source-grounding)
- sostituiti i placeholder/null con hash reali per le fonti effettivamente usate dalla skill
- aggiunti `references/fonti/` per LR 65/2014, DPR 380/2001, regolamento toscano 1/R/2022 e pagina regionale sulla classificazione sismica
- riscritti gli estratti per limitare le affermazioni a contenuti tracciabili nelle fonti lette
- ridotto il perimetro della skill: rimossi dettagli non verificati su paesaggistica, portali comunali e altre fonti non trascritte
- riscritti task ed esempi per mantenere solo logica supportata da fonti autorevoli lette

## [0.1.0-alpha] - 2026-05-02

### Added
- prima versione alpha della skill
