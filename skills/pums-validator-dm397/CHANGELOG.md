# CHANGELOG - pums-validator-dm397

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Estesa la catena normativa alla versione vigente: aggiunte come fonti il DM 26 gennaio 2021 n. 29 (proroga termini PUMS) e il DM 12 novembre 2021 n. 444 (termine unitario 1 gennaio 2023; nuovo art. 1 c.2 DM 397/2017 che estende il gate di adozione alla mobilita' ciclistica; abrogazione dell'art. 7 c.3 DM 396/2019).
- Riscritto `tasks/check-ambito-obbligo.md` per riflettere il termine unitario 1/1/2023, il gate finanziamenti distinto dalla conformita' generale del PUMS, il criterio premiale 2022 e l'abrogazione del regime transitorio art. 7 c.3 DM 396/2019.
- Riformulato `tasks/check-indicatori-tabella1.md` distinguendo gli obblighi del decreto (Tabella 1, target di Piano a 10 anni) dagli indirizzi operativi del Vademecum 2022 (triade target a 2/3, 5, 10 anni come "Vademecum alignment", non come NON CONFORMITA' al decreto).
- Aggiornati gli esempi `examples/conforme/` e `examples/problematico/` separando il gate dell'art. 1 c.2 (adozione) dalla conformita' generale del PUMS.
- Aggiornati estratti DM 397/2017 e DM 396/2019 con riferimenti incrociati a DM 29/2021 e DM 444/2021 (in particolare: nota di abrogazione su art. 7 c.3 DM 396/2019).

### Added
- `references/fonti/dm-26-1-2021-29-pums.md`
- `references/fonti/dm-12-11-2021-444-pums.md`
- `references/estratti/dm-26-1-2021-29-pums.md`
- `references/estratti/dm-12-11-2021-444-pums.md`

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
