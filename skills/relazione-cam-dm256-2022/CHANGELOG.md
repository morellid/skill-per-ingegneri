# Changelog - relazione-cam-dm256-2022

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-01

### Added
- SKILL.md: entry point con routing ai 3 task, avvertenza vigenza normativa, limiti
- Task `identifica-criteri-applicabili.md`: classificazione NC/R1/R2/MS e tabella criteri applicabili
- Task `draft-relazione-cam.md`: guida dialogica per la redazione criterio per criterio
- Task `check-relazione-cam.md`: verifica completezza e conformita' al DM 256/2022
- `references/sources.yaml`: 3 fonti (DM 256/2022, Allegato, D.Lgs. 36/2023 art. 57)
- Estratti testuali: criteri di base 2.1-2.9, criteri premianti 4.1-4.6, artt. chiave DM, art. 57
- Esempio conforme: nuova costruzione uffici (tutti criteri applicabili NC)
- Esempio non conforme: ristrutturazione R1 con relazione lacunosa (criteri mancanti e generici)
- README.md, AGENTS.md, agents/openai.yaml

### Known issues / TODO v0.2
- SHA256 fonti non popolato (da effettuare download manuale)
- Aggiungere esempio MS (manutenzione straordinaria)
- Validazione Livello 2 da effettuare con professionista esperto appalti PA
