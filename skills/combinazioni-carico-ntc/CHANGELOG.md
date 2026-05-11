# CHANGELOG - combinazioni-carico-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su Keep a Changelog e questa skill aderisce a Semantic Versioning.

## [0.1.1-alpha] - 2026-05-11

### Fixed

- fix(source-grounding): aggiunto `references/fonti/ntc2018-dm-17-01-2018.md` con trascrizione fedele di
  par. 2.5.1.3, 2.5.2 (Tab. 2.5.I), 2.5.3 (eq. [2.5.1]-[2.5.7]), 2.6.1 (Tab. 2.6.I) letti dal PDF
  ufficiale NTC 2018 (GU n. 42 del 20/02/2018, SHA256 verificato).
- fix(source-grounding): aggiunto `md_path` in `sources.yaml` per rispettare la nuova policy CI.
- fix(source-grounding): estratto aggiornato con citazioni precise di pagina e riferimento a fonti/.
- fix(combinazione-eccezionale): corretto coefficiente azione variabile principale in combinazione
  eccezionale da psi2 a psi1 (NTC 2018 eq. [2.5.6]: `G1+G2+P+Ad+psi1*Qk1+psi2*Qk2+...`).
  Tutte le costanti numeriche PSI e GAMMA nel codice verificate contro Tab. 2.5.I e Tab. 2.6.I del PDF.

## [0.1.0-alpha] - 2026-05-03

### Added
- Skill code-driven per combinazioni delle azioni NTC 2018 par. 2.5.3
- Modulo Python `tasks/lib/combinazioni.py` con coefficienti psi Tab. 2.5.I e gamma Tab. 2.6.I
- Task per generazione matrice e verifica matrice esistente
- Estratto normativo strutturato e `sources.yaml`
- Due esempi: caso ordinario con sismica e caso con categoria non supportata
- Test suite standard-library per coefficienti, combinazioni e CLI

### Fixed
- Generazione della combinazione SLU fondamentale anche in assenza di azioni variabili
- Normalizzazione degli spazi nelle categorie delle azioni variabili
- Hash SHA256 reale per il PDF ufficiale NTC 2018 in `sources.yaml`
