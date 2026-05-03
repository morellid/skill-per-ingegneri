# CHANGELOG - combinazioni-carico-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su Keep a Changelog e questa skill aderisce a Semantic Versioning.

## [0.1.0-alpha] - 2026-05-03

### Added
- Skill code-driven per combinazioni delle azioni NTC 2018 par. 2.5.3
- Modulo Python `tasks/lib/combinazioni.py` con coefficienti psi Tab. 2.5.I e gamma Tab. 2.6.I
- Task per generazione matrice e verifica matrice esistente
- Estratto normativo strutturato e `sources.yaml`
- Due esempi: caso ordinario con sismica e caso con categoria non supportata
- Test suite standard-library per coefficienti, combinazioni e CLI
