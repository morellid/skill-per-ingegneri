# CHANGELOG - pos-allegato-xv-checker

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Da fare
- Popolare `references/sources.yaml` con D.Lgs. 81/2008 testo consolidato + Allegato XV
- Preparare estratti normativi in `references/estratti/`
- Completare contenuto dei 4 task files (attualmente scaffold)
- Aggiungere almeno 2 esempi in `examples/`
- Validazione Livello 1 (self-check)
- Individuare validatore di dominio per Livello 2

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold iniziale della skill
- `SKILL.md` con routing a 4 task files
- `tasks/` con stubs per check-completezza, check-coerenza-rischi, check-costi-sicurezza, check-coordinamento
- `references/sources.yaml` scheletro
- `CHANGELOG.md`, `README.md`

### Note
- **Non ancora utilizzabile in produzione**. Contenuto normativo da preparare nelle prossime sessioni a partire da documenti ufficiali.
- Skill considerata draft finche' non passa Livello 1 di validazione (vedi `methodology/validazione.md`).
