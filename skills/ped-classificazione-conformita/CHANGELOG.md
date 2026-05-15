# CHANGELOG - ped-classificazione-conformita

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-14

### Added
- Prima versione alpha della skill PED.
- Trascrizione fedele del D.Lgs 26/2016 (GU n.53 del 04/03/2016) in `references/fonti/dlgs-26-2016.md`, source-grounded sul PDF della Gazzetta Ufficiale (SHA256 `20e9eb35c39f6f2c51773e58d6864694583ea9b45af5a3d45e6d3540ca1387f5`).
- Estratto curato su classificazione e moduli in `references/estratti/dlgs-26-2016-classificazione-moduli.md`.
- Cinque task: `check-ambito-applicabilita`, `classifica-fluido`, `determina-categoria`, `scegli-procedura-conformita`, `check-marcatura-ce-dichiarazione`.
- Due esempi: caso conforme (recipiente acqua fluido gruppo 2, categoria I, modulo A) e caso problematico (errata classificazione del fluido).
- Formato dual-agent (Claude Code + OpenAI Codex) con `agents/openai.yaml`.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2): da considerare draft finche' un ingegnere meccanico esterno all'autore non valida classificazione, mappatura categoria-modulo e contenuto della dichiarazione UE.
- Le tabelle 1-9 dell'Allegato II (categorie I/II/III/IV in funzione di PS, V o DN) sono diagrammi grafici nel PDF della GU. La skill rinvia al PDF per la lettura puntuale e non fabbrica valori soglia.
- Direttiva 2014/68/UE non inclusa come fonte separata: i sandbox EUR-Lex bloccano il download (HTTP 202). Il D.Lgs 26/2016 e' la norma vincolante in Italia e ne riproduce il contenuto tecnico.
