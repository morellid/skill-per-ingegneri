# CHANGELOG - bandi-tipo-anac-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02

### Added
- SKILL.md: routing verso due sotto-attivita' (check-conformita', identifica-anomalie)
- AGENTS.md: convenzioni di dominio, articoli chiave D.Lgs. 36/2023, anti-pattern
- tasks/check-conformita-disciplinare.md: verifica strutturata con tabelle sezioni e clausole chiave
- tasks/identifica-anomalie-clausole.md: scansione anomalie per pattern (vecchio codice, subappalto, CCNL, ...)
- references/sources.yaml: D.Lgs. 36/2023 (originale + correttivo), 4 schemi ANAC 2023
- references/estratti/dlgs-36-artt-clausole-disciplinare.md: artt. 11, 74, 87, 90, 94-103, 117-120
- references/estratti/anac-bandi-tipo-struttura-2023.md: struttura schemi ANAC, tabella vecchio/nuovo codice
- examples/conforme-servizi-ppb/: disciplinare servizi informatici conforme SF-PPB
- examples/non-conforme-lavori-anomalie/: disciplinare lavori con 5 anomalie critiche tipiche
- agents/openai.yaml: metadata Codex (display_name, short_description, default_prompt)
- README.md: documentazione utente con installazione e limiti noti

### Note di sviluppo
- Skill non ancora validata da RUP o consulente legale esterno
- Gli schemi ANAC non sono embedabili per intero: la skill verifica struttura e norme,
  non il testo verbatim degli schemi
- Closes GitHub issue #4
