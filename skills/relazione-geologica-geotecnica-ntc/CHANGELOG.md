# CHANGELOG - relazione-geologica-geotecnica-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-11

### Added
- Prima versione alpha della skill (issue #38 del backlog, GT.1)
- Fonti lette e trascritte: NTC 2018 parr. 6.1-6.2.6; Circolare 7/2019
  C6 intro, C6.2-C6.2.4.3, C9.1 lett. g, C10.1 (sources.yaml con SHA256,
  trascrizioni in `references/fonti/`, estratti operativi in
  `references/estratti/`)
- Task: check-relazione-geologica, check-relazione-geotecnica,
  check-coerenza-geologica-geotecnica, draft-struttura-relazione-geotecnica
- Esempi: 1 caso conforme (edificio residenziale) + 1 caso problematico
  (capannone senza indagini)

### Note di sviluppo
- Skill non ancora validata da dominio terzo: da considerare draft finche'
  non passa validazione Livello 2 (vedi methodology/validazione.md)
- Noto per v0.2 (dalla review adversariale): gli esempi coprono solo il task
  check-relazione-geotecnica; aggiungere esempi per gli altri tre task.
  Le pagg. GU 173-174 della Circolare (C6 intro, C6.2.1, nota 1) sono
  scansioni immagine lette visivamente: da riconfermare dal validatore di
  Livello 2 sul PDF
- Fuori scope v0.1: verifiche delle singole opere geotecniche (NTC parr.
  6.3-6.11), progettazione sismica (parr. 3.2, 7.11), coefficienti parziali
  numerici (Tabb. 6.2.I-6.2.III), livelli di progettazione ex Codice dei
  contratti
