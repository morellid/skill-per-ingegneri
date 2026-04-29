# CHANGELOG - spettro-risposta-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Path resolution dei comandi Bash: tutti gli esempi nei file `.md` ora usano `${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py` invece del path relativo `tasks/lib/spettro.py`, che falliva quando la CWD dell'utente non coincideva con la skill dir.
- Regola operativa esplicita in `SKILL.md` e in `AGENTS.md`: l'agent **deve** invocare il modulo Python via Bash per qualunque numero (TR, ag/F0/Tc*, S, eta, TB/TC/TD, Se(T)); ricalcolare a mano dagli estratti normativi e' vietato e annulla l'invariante code-driven.

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill
- `SKILL.md` con routing per 3 sotto-attivita'
- Task file `tasks/calcola-spettro.md`: calcolo completo spettro elastico orizzontale per uno o piu' SL
- Task file `tasks/valida-input-sito.md`: precheck input prima del calcolo
- Task file `tasks/run-test-suite.md`: documentazione esecuzione test
- Modulo Python `tasks/lib/spettro.py`: implementazione delle formule chiuse di NTC par. 3.2.3.2.1 (componente orizzontale) e par. 2.4 (V_R, T_R), con interpolazione logaritmica sui 9 T_R di riferimento dell'Allegato A. Solo libreria standard Python 3.9+.
- Test suite `tasks/lib/test_spettro.py`: 23 test su formule chiuse, raccordi, interpolazione, casi limite, rifiuto S1/S2, CLI. Tutti passano.
- Estratti normativi:
  - `references/estratti/ntc2018-classi-uso-vita.md`
  - `references/estratti/ntc2018-par-3-2.md`
  - `references/estratti/ntc2018-allegato-a-tab.md`
  - `references/estratti/circ-7-2019-c-3-2.md`
- `references/sources.yaml` con 4 fonti catalogate (NTC, Circ., INGV, CSLP)
- 1 esempio conforme (`examples/caso-conforme-fittizio-cu2-c-t1/`)
- 1 esempio problematico (`examples/caso-problematico-cat-S2/`) con rifiuto bloccante
- `agents/openai.yaml` con UI metadata Codex

### Note di sviluppo
- Skill **non ancora validata da dominio terzo** (Livello 2). I parametri usati negli esempi sono fittizi e progettati per leggibilita'.
- I file binari delle fonti (NTC 2018 PDF, Circ. 7/2019 PDF) **non sono ancora archiviati** in `not_in_repo/`: gli sha256 in `sources.yaml` sono placeholder `REPLACE_WHEN_DOWNLOADED`. Eseguire `./scripts/fetch-sources.sh` prima del release stabile.
- La validazione Livello 2 richiede confronto numerico vs foglio Excel CSLP su almeno 10 casi reali (siti sparsi sul territorio nazionale, categorie sottosuolo diverse, classi d'uso diverse). Tolleranze documentate in `tasks/run-test-suite.md`.
- Da considerare draft fino a validazione Livello 2 superata. Vedi `methodology/validazione.md`.

### Limiti noti (versione 0.1.0-alpha)
- Solo componente orizzontale (par. 3.2.3.2.1). Verticale (3.2.3.2.2) in roadmap.
- Solo spettro elastico Se(T). Spettro di progetto S_d(T) con riduzione q (par. 3.2.3.5) fuori scope.
- Categorie sottosuolo S1/S2 rifiutate (richiedono RSL ai sensi par. 3.2.2).
- ST T2/T3/T4 applicato in sommita' del rilievo. Quote intermedie (NTC eq. 3.2.5) non automatizzate.
- Non incorpora il reticolo INGV: l'utente fornisce i 9 valori (a_g, F_0, T_C*) al sito.
