# CHANGELOG - pums-validator-dm397

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-13

### Added
- Prima versione alpha della skill di validazione PUMS.
- Fonti normative scaricate, verificate via SHA256 e convertite in markdown committato:
  - DM 4 agosto 2017 n. 397 (GU n. 233 del 5/10/2017, S.O. 53).
  - DM 28 agosto 2019 n. 396 (modifica del DM 397/2017, introduce nuova Tabella 1).
  - Vademecum MIMS del 27 settembre 2022 (indirizzi operativi PUMS).
- Estratti curati per ciascuna fonte in `references/estratti/`.
- 5 sotto-attivita' di validazione in `tasks/`:
  - `check-ambito-obbligo.md` (art. 3 c.1 DM 397/2017 + art. 2 DM 396/2019).
  - `check-procedura-redazione-pums.md` (Allegato 1 lett. a-h).
  - `check-obiettivi-pums.md` (17 macro-obiettivi minimi, aree A/B/C/D).
  - `check-indicatori-tabella1.md` (Tabella 1 DM 396/2019, tempo "0", target).
  - `check-monitoraggio-aggiornamento.md` (Vademecum 3.6 + art. 4 c.1 DM 397/2017).
- Esempi:
  - Caso conforme (Comune 220.000 ab. con PUMS adottato 2024).
  - Caso problematico ("Piano della Mobilita' Sostenibile" con difformita' multiple).
- SKILL.md con frontmatter dual-agent (Claude Code + Codex CLI).
- AGENTS.md di skill con convenzioni di dominio.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (validazione Livello 1: autore singolo).
- Da considerare draft finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
- Linee guida regionali integrative non catalogate in questa versione.
- Avvisi per finanziamenti TRM non catalogati (rinvio agli avvisi specifici).
