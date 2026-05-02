# CHANGELOG - bandi-tipo-anac-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02 (rev 2 - post Codex adversarial review)

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

### Fixed (post Codex adversarial review)
- Corretti articoli D.Lgs. 36/2023 errati: DGUE art. 87->91; garanzia provvisoria art. 117->106;
  garanzia definitiva art. 118->117; fatturato limit art. 102->100
- Chiarito che art. 87 D.Lgs. 36/2023 e' il disciplinare, NON il DGUE
- Aggiornate soglie europee a valori 2026: lavori 5.404.000; PA centrali 140.000;
  sub-centrali 216.000; settori speciali 432.000
- Ridotto catalogo schemi ANAC: rimossi 3 schemi non verificati; mantenuto solo Bando tipo n. 1/2023
  (Delibera n. 365/2025 confermato) per SF-OEPV; altri da verificare su portale ANAC
- Garanzia provvisoria: aggiunto range 1-4% (non solo 2%); nota su procedure sotto soglia
- Tabella vecchio/nuovo codice: aggiunta riga art. 85 D.Lgs. 50/2016 -> art. 91 D.Lgs. 36/2023 (DGUE)
- Aggiunto avvertenza su avvalimento (art. corretto da verificare su Normattiva)
- Aggiunto art. 57 (CAM), art. 58 (lotti), art. 60 (revisione prezzi) nella copertura

### Note di sviluppo
- Skill non ancora validata da RUP o consulente legale esterno
- Gli schemi ANAC non sono embedabili per intero: la skill verifica struttura e norme,
  non il testo verbatim degli schemi
- Numerazioni articoli D.Lgs. 36/2023 verificate nella revisione post-Codex ma occorre
  ulteriore verifica su Normattiva per gli articoli sull'avvalimento
- Closes GitHub issue #4
