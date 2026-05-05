# CHANGELOG - dnsh-pnrr-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Reso esplicito che il supporto PNC e' solo condizionato a una fonte misura-specifica che richiami il DNSH
- Aggiornate regole operative, task e metadata per impedire l'uso automatico della Guida RGS 2024 su casi PNC privi di base documentale

### Added
- Fonti integrative per supporto PNC condizionato (`DL 77/2021 art. 14` e pagina istituzionale Ministero della Salute sul principio DNSH)
- Estratti operativi dedicati al perimetro PNC condizionato

## [0.1.0-alpha] - 2026-05-04

### Added
- Prima versione alpha della skill DNSH PNRR
- SKILL.md con frontmatter `license: MIT` e routing verso 3 task files
- agents/openai.yaml con metadata Codex
- 3 task files:
  - `inquadra-misura-schede.md`
  - `verifica-checklist.md`
  - `piano-evidenze-report.md`
- references/sources.yaml con fonti UE/RGS e hash SHA256 dei PDF RGS scaricati in `not_in_repo/`
- references/estratti/ con 4 estratti sintetici strutturati
- README.md e AGENTS.md di dominio

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1)
- Da considerare draft finche' non passa validazione Livello 2
- Verificare periodicamente aggiornamenti sulla pagina ufficiale Italia Domani / RGS DNSH e template ReGiS
