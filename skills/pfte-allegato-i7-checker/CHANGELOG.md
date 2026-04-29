# CHANGELOG - pfte-allegato-i7-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Esempi dedicati al task di verifica coerenza PFTE/esecutivo (`coerenza-nuova-costruzione/`, `coerenza-scostamenti/`).
- Estensione integrazione bandi-tipo ANAC (catalog PR.2).

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill PFTE Allegato I.7 Checker
- Task files: `genera-checklist-pfte.md`, `verifica-completezza-pfte.md`, `verifica-coerenza-esecutivo.md`
- Fonti normative consultate: D.Lgs. 36/2023 (art. 41 + Allegato I.7) e D.Lgs. 209/2024 correttivo
- Estratti testuali strutturati: `dlgs-36-art-41.md`, `allegato-i7-pfte.md`, `allegato-i7-esecutivo.md`, `dlgs-209-2024-modifiche.md`
- Esempi: 1 conforme (nuova costruzione) + 1 incompleto (manutenzione straordinaria con elaborati mancanti)
- Documentazione dual-agent (Claude Code + OpenAI Codex)

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1: autore-driven, fonti pubbliche).
- Da considerare draft finche' non passa validazione Livello 2 con un RUP / ingegnere civile esperto in procedure post D.Lgs. 36/2023 (vedi `methodology/validazione.md`).
- I PDF delle fonti (D.Lgs. 36/2023 e correttivo) non sono stati scaricati automaticamente: i campi `sha256` in `sources.yaml` sono `null`. Per popolarli eseguire manualmente `scripts/fetch-sources.sh pfte-allegato-i7-checker` (richiede permessi di rete) e committare sources.yaml aggiornato.
- Issue di riferimento: GitHub issue #3 ([P1] PR.1).
