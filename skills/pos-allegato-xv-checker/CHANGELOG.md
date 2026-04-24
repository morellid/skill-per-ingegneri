# CHANGELOG - pos-allegato-xv-checker

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added (2026-04-25, post v0.1.0-alpha)
- Estratto integrale Allegato XV punti 1, 3, 4 + Allegati XV.1 e XV.2 in `references/estratti/allegato-xv-testo.md`
- Estratto art. 96 e 97 D.Lgs. 81/2008 in `references/estratti/dlgs-81-art-96-97.md`
- `sources.yaml` aggiornato con hash SHA256 reali per:
  - Testo coordinato INL gennaio 2025 (fonte primaria, f593e18...)
  - Testo originale GU 2008 (riferimento storico, bcc0e07...)
- `tasks/check-completezza.md` completato con procedura operativa basata sul testo Allegato XV 3.2.1
- Portale Normattiva dichiarato come fonte di cross-check autoritativo

### Added (2026-04-25, secondo batch)
- Esempi di test per `check-completezza.md`:
  - `examples/conforme-cantiere-piccolo/` - POS ben redatto, piccola impresa, ristrutturazione
  - `examples/incompleto-voci-mancanti/` - POS con 11 problemi (3 assenze, 5 inadeguatezze, 3 note medie)
  - Ogni esempio ha input.md (POS sintetico), expected-output.md (output atteso), note.md (razionale dominio)

### Da fare (prossime iterazioni)
- Completare contenuto di `check-coerenza-rischi.md`, `check-costi-sicurezza.md`, `check-coordinamento.md`
- Esempi aggiuntivi: caso borderline-boilerplate, caso con PSC mancante
- Validazione Livello 1 completa con test reale su caso d'uso
- Individuare validatore di dominio per Livello 2 (potenziale: Fabrizio Vitale per aspetti RSPP/art. 96)
- Valutare e catalogare interpelli rilevanti (INTERPELLO 25/2014, 13/2016)
- Testare la skill su POS reale (con consenso) per verificare che l'output atteso sia effettivamente cio' che produce

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
