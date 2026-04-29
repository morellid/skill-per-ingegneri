# CHANGELOG - spettro-risposta-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Test di validazione hardening su `ParametriRiferimento` (`TestValidazioneInput`, 7 test): rifiuto di valori zero/negativi/NaN/inf/non-numerici/bool ai 27 parametri (9 TR x ag/F0/Tc*), incluso JSON con `null` (mappato a None).
- Test di copertura categorie (`TestCoperturaCategorie`, 4 test): D, E, T2/T3/T4, smorzamento xi != 5%. Le formule SS/CC sono confrontate contro l'algebra di Tab. 3.2.IV.
- Test anti-drift sull'esempio canonico (`TestEsempioConforme`, 2 test): il modulo viene rieseguito sull'input documentato e confrontato bit-per-bit con il fixture machine-readable `examples/caso-conforme-fittizio-cu2-c-t1/expected.json`. Drift fra docs e codice fallisce subito.
- Fixture machine-readable `examples/caso-conforme-fittizio-cu2-c-t1/expected.json`: stdout JSON del modulo per il caso canonico (4 SL, ordinate Se(T) tabulate 0:4:0.1), usato come golden master.

### Changed
- **Hardening `ParametriRiferimento.__post_init__`**: oltre alla lunghezza, ora valida che tutti i valori di ag, F0, Tc* siano numerici, finiti e strettamente positivi. Messaggi d'errore con indice e suggerimenti di unita' (ag in g, non m/s^2).
- **Esempio caso conforme rigenerato dallo stdout reale del modulo.** L'`expected-output.md` precedente conteneva un valore errato al raccordo TD (0.16142 a T=2.472 invece del valore corretto 0.15775; T=2.472 cade sul ramo TD-inf perche' TD = 2.4716 < 2.472). La nuova pagina punta al fixture JSON come riferimento autoritativo.
- **Claim CSLP corretti.** SKILL.md, sources.yaml, docstring del modulo Python e della test suite ora dichiarano esplicitamente che la versione 0.1.0-alpha contiene **solo test di consistenza interna**; il confronto numerico vs foglio Excel CSLP (validazione di campo, 10+ casi reali) e' prerequisito del release stabile e non e' stato eseguito. La pagina precedente sopravvalutava lo stato di validazione.

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
