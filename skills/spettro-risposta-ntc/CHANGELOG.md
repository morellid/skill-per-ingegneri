# CHANGELOG - spettro-risposta-ntc

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed (source-grounding remediation semantica - issue #111)

- **URL corretti in sources.yaml**: l'url dei due decreti puntava alle pagine HTML del portale GU.it invece che ai PDF diretti. Corretti a URL PDF diretti (eli/gu/.../pdf) per entrambe le fonti. Il CI scaricava HTML e otteneva SHA256 diverso da quello del PDF.
  - NTC 2018: url corretto da `.../eli/id/2018/2/20/18A00716/sg` a `.../eli/gu/2018/02/20/42/so/8/sg/pdf`
  - Circ. 7/2019: url corretto da `.../eli/id/2019/02/11/19A00855/sg` a `.../eli/gu/2019/02/11/35/so/5/sg/pdf`
- **Fonti scaricate e hashate**: NTC 2018 (DM 17/01/2018, GU n. 42 S.O. n. 8) e Circolare MIT n. 7/2019 (GU n. 35 S.O. n. 5) scaricati dal portale Gazzetta Ufficiale, SHA256 calcolati e committati in `sources.yaml`. Circolare (48 MB) scaricata e hashata il 2026-05-11; SHA256 confermato coincidente con quello gia' dichiarato nel commit precedente.
  - NTC 2018: SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  - Circ. 7/2019: SHA256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`
- **Trascrizioni verbatim create** (directory `references/fonti/` precedentemente assente):
  - `references/fonti/ntc2018-dm-17-01-2018.md`: testo letto con pdftotext, trascritti par. 2.4.1, 2.4.2, 2.4.3, 3.2, 3.2.1, 3.2.2, 3.2.3.2.1, Tab. 3.2.I-V
  - `references/fonti/circ-7-2019-mit.md`: testo letto con pdftotext, trascritti par. C2.4.1, C2.4.3 (Tab. C2.4.I), C3.2, C3.2.1, C3.2.3, C3.2.3.2.1
- **Estratti riscritti** dopo lettura del PDF (non dai training data):
  - `ntc2018-par-3-2.md`: corretti i numeri delle equazioni (Se(T) e' eq. [3.2.2] non [3.2.4]; eta e' eq. [3.2.4] non [3.2.6]; TC=[3.2.5], TB=[3.2.6], TD=[3.2.7]); corretta la nota su S1/S2 (non sono nella Tab. 3.2.II NTC 2018, solo A-E); aggiunte citazioni pagina.
  - `ntc2018-classi-uso-vita.md`: corretta la fonte del VR minimo 35 anni (non e' in NTC 2018 par. 2.4.3 ma emerge dalla Tab. C2.4.I della Circolare 7/2019); aggiunte citazioni pagina.
  - `ntc2018-allegato-a-tab.md`: corretto: il NTC 2018 non ha un proprio Allegato A numerico, ma rinvia all'Allegato A al DM 14/01/2008; i 9 TR sono confermati dalla Circolare.
  - `circ-7-2019-c-3-2.md`: riscritto dall'esempio inventato a testo reale letto dal PDF; rimossa la "nota sintetica" che era un esempio inventato non corrispondente al testo.
- **Docstring spettro.py corrette**: equazioni NTC corrette ([3.2.0] per TR, [3.2.2] per Se(T), [3.2.3] per S, [3.2.4] per eta, [3.2.5]-[3.2.7] per TC/TB/TD); fonte del VR minimo 35 anni corretta (Circ. Tab. C2.4.I, non NTC 2018 par. 2.4.3); commento S1/S2 aggiornato (non in Tab. 3.2.II NTC 2018); aggiunti riferimenti a `references/fonti/`.
- **Valori numerici verificati**: tutti i coefficienti di Tab. 3.2.IV (SS formule e clamp, CC esponenti), i valori ST di Tab. 3.2.V, la formula TD = 4*(ag/g)+1.6, i coefficienti CU di Tab. 2.4.II, e i valori P_VR di Tab. 3.2.I corrispondono ESATTAMENTE al testo letto dal PDF (nessuna discrepanza trovata).



### Added
- **Per-state error reporting nella CLI** (Codex round 7): con `--stato-limite TUTTI` (default), se uno stato limite produce TR fuori reticolo (es. VN=50 CU I -> V_R=35 -> TR_SLO~21<30), gli altri stati continuano a essere calcolati invece di abortire l'intero run. Lo stato fallito appare nell'output JSON come `{"stato_limite": "SLO", "errore": "..."}` e nel testo come blocco `=== SLO === ATTENZIONE: stato non calcolabile -> ...`. Il run abortisce con `parser.error()` solo se **tutti** gli stati richiesti falliscono. Test: +2 (`test_tutti_con_slo_fuori_reticolo_continua`, `test_tutti_falliti_abortisce`).
- **Validazione type-mismatch nel JSON di input** (Codex round 6): l'`--input-json` ora valida i tipi di top-level (deve essere dict), `parametri_calcolo`/`parametri_pericolosita_sito` (dict), `ag_g`/`F0`/`Tc_star` (liste), `tabula_periodi` (dict), `stati_limite` (lista di string) prima di passarli al pipeline. Senza questi check, un JSON malformato (es. `ag_g: 0.2` scalare invece di lista, oppure `stati_limite: [1]`) crashava con `TypeError`/`AttributeError` Python invece del friendly `parser.error()`. Test: +4 (`test_input_json_ag_g_non_lista`, `test_input_json_stati_limite_con_int`, `test_input_json_pc_non_dict`, `test_input_json_top_level_non_dict`).
- **Fail-closed esteso ai coefficient helpers pubblici** (Codex round 5): `coeff_SS`, `coeff_CC` e `periodi_caratteristici` ora validano i propri scalari (NaN/inf/non-numerici/non-positivi). Senza questo controllo, `coeff_SS('C', NaN, 2.5)` ritornava silenziosamente `1.0` (clamp inferiore) invece di sollevare. La pipeline `calcola_parametri` era gia' coperta via `ParametriRiferimento`, ma chiamate dirette in notebook/lib bypassavano. Test: +6 (`test_coeff_SS_rifiuta_nan_inf`, `test_coeff_SS_rifiuta_zero_negativo`, `test_coeff_SS_rifiuta_bool`, `test_coeff_CC_rifiuta_nan_inf`, `test_coeff_CC_rifiuta_zero_negativo`, `test_periodi_caratteristici_rifiuta_non_finiti`).
- **Fail-closed su scalari non finiti** (Codex adversarial review round 4): `vita_riferimento`, `coeff_eta` e `Se_T` ora rifiutano NaN/inf/non-numerici via helper `_assert_finito`, coerentemente con la validazione vettoriale di `ParametriRiferimento.__post_init__`. Senza questa correzione, `xi_percento=NaN` produceva silenziosamente `eta=NaN` e tutte le ordinate `Se(T)` NaN, output corrotto in dominio strutturale ad alto rischio.
- **`json.load(parse_constant=...)`**: i token JSON non standard `NaN`/`Infinity`/`-Infinity` (RFC 8259 li vieta ma il parser Python li accetta di default) sono ora rifiutati in entrambi i path CLI (`--input-json` e `--tr-riferimento`).
- **Validazione `tabula_periodi`**: `_parse_periodi` valida ora che `start`/`stop`/`step` siano finiti, che `step > 0` e che `stop >= start`. Test: 7 nuovi (`TestFailClosedScalari` 4 + `TestCLINaNHandling` 3).
- **Error handling CLI friendly su Mode A e Mode B**: chiavi mancanti in `parametri_pericolosita_sito` (`ag_g`/`F0`/`Tc_star`), in `parametri_calcolo` (`vn_anni`/`classe_uso`/`cat_sottosuolo`/`cat_topografica`), in `tabula_periodi`, oppure stato limite/categoria sottosuolo non valido in `stati_limite`, sollevano ora un `parser.error()` con messaggio chiaro al posto di un traceback Python. Stessa cosa per file `--tr-riferimento` incompleto. Test di copertura: 5 nuovi (`test_input_json_sito_chiavi_mancanti`, `test_input_json_pc_chiavi_mancanti`, `test_input_json_stato_limite_invalido`, `test_classe_uso_case_insensitive`, `test_carica_parametri_riferimento_chiavi_mancanti`).
- **`vita_riferimento` accetta `classe_uso` case-insensitive** (`"ii"`, `"II"`, `"Ii"`): la CLI gia' protetta da `argparse choices` non cambia comportamento; chiamate programmatiche da agent / notebook diventano piu' tolleranti.
- **`carica_parametri_riferimento` valida la presenza** delle chiavi `ag_g`/`F0`/`Tc_star` nel file JSON: chiave mancante -> `ValueError` esplicito invece di `KeyError`.
- **Flag CLI `--input-json`**: consente di passare al modulo Python tutti i parametri di calcolo (`parametri_calcolo`) e di pericolosita' al sito (`parametri_pericolosita_sito`) in un singolo file JSON, invece di duplicarli su 7+ flag scalari. Schema in `examples/caso-conforme-fittizio-cu2-c-t1/input.json`. Round 3 Codex review: elimina il drift residuo fra il comando bash documentato (`input.md`) e il fixture (`input.json`). I flag scalari (`--vn`, `--classe-uso`, etc.) restano supportati come alternativa.
- Test CLI di equivalenza: modalita' `--input-json` produce stdout bit-per-bit identico a modalita' flag scalari ed entrambi coincidono con `expected.json` (`TestCLI.test_input_json_equivalente_ai_flag_scalari`).
- Test CLI di error handling: schema mancante in `--input-json` -> errore parser; flag scalari obbligatori mancanti -> errore parser con messaggio esplicito.
- Test di validazione hardening su `ParametriRiferimento` (`TestValidazioneInput`, 7 test): rifiuto di valori zero/negativi/NaN/inf/non-numerici/bool ai 27 parametri (9 TR x ag/F0/Tc*), incluso JSON con `null` (mappato a None).
- Test di copertura categorie (`TestCoperturaCategorie`, 4 test): D, E, T2/T3/T4, smorzamento xi != 5%. Le formule SS/CC sono confrontate contro l'algebra di Tab. 3.2.IV.
- Test anti-drift sull'esempio canonico (`TestEsempioConforme`, 2 test): legge `examples/caso-conforme-fittizio-cu2-c-t1/input.json` ed esegue il modulo, poi confronta bit-per-bit con il golden master `expected.json`. Drift fra l'input documentato e quello eseguito dal test e' impossibile (round 2 Codex review).
- Fixture machine-readable `examples/caso-conforme-fittizio-cu2-c-t1/input.json`: input canonico (parametri di calcolo + parametri di pericolosita') letto da test, `input.md` e CLI `--input-json`.
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
- I file binari delle fonti (NTC 2018 PDF, Circ. 7/2019 PDF) erano placeholder al momento del tag 0.1.0-alpha; la remediation source-grounding semantica (issue #111) li ha scaricati, hashati e convertiti a MD.
- La validazione Livello 2 richiede confronto numerico vs foglio Excel CSLP su almeno 10 casi reali (siti sparsi sul territorio nazionale, categorie sottosuolo diverse, classi d'uso diverse). Tolleranze documentate in `tasks/run-test-suite.md`.
- Da considerare draft fino a validazione Livello 2 superata. Vedi `methodology/validazione.md`.

### Limiti noti (versione 0.1.0-alpha)
- Solo componente orizzontale (par. 3.2.3.2.1). Verticale (3.2.3.2.2) in roadmap.
- Solo spettro elastico Se(T). Spettro di progetto S_d(T) con riduzione q (par. 3.2.3.5) fuori scope.
- Sottosuoli non classificabili nelle categorie A-E rifiutati (richiedono RSL ai sensi par. 3.2.2 NTC 2018; le categorie S1/S2 della NTC 2008 non sono in Tab. 3.2.II NTC 2018).
- ST T2/T3/T4 applicato in sommita' del rilievo. Quote intermedie (decremento lineare, NTC 2018 par. 3.2.3.2.1 dopo Tab. 3.2.V) non automatizzate.
- Non incorpora il reticolo INGV: l'utente fornisce i 9 valori (a_g, F_0, T_C*) al sito.
