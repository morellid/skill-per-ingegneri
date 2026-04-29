# AGENTS.md - spettro-risposta-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per il calcolo dello spettro di risposta elastico in accelerazione (componente orizzontale) ai sensi delle NTC 2018 par. 3.2 e Circolare 7/2019. Riferimenti normativi: DM 17/01/2018 (NTC 2018) e Circolare MIT 21/01/2019 n. 7 - entrambi pubblici e disponibili su Gazzetta Ufficiale. Target: ingegneri strutturisti italiani che progettano nuove costruzioni o valutano costruzioni esistenti in zona sismica.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **NTC 2018** (DM 17/01/2018) - id `ntc2018-dm-17-01-2018`, hash da calcolare al fetch (`./scripts/fetch-sources.sh`)
- **Circ. 7/2019 MIT** (21/01/2019) - id `circ-7-2019-mit`, hash da calcolare al fetch
- **Reticolo INGV** ([zonesismiche.mi.ingv.it](http://zonesismiche.mi.ingv.it/)) - id `ingv-reticolo-pericolosita`, lookup spaziale dei parametri di pericolosita' (non incorporato)
- **Foglio Excel CSLP** ([cslp.mit.gov.it](https://www.cslp.mit.gov.it/)) - id `cslp-spettri-ntc`, benchmark di validazione

Estratti pertinenti in `references/estratti/`:
- `ntc2018-classi-uso-vita.md` - par. 2.4: V_N, classi d'uso, V_R, Tab. 2.4.II
- `ntc2018-par-3-2.md` - par. 3.2: stati limite, P_VR, categorie sottosuolo/topografia, formule spettro 3.2.4, coefficienti SS/CC/eta, periodi T_B/T_C/T_D
- `ntc2018-allegato-a-tab.md` - Allegato A: reticolo, 9 T_R, interpolazione log-log
- `circ-7-2019-c-3-2.md` - C3.2: commento applicativo + esempio sintetico

## Articoli e punti chiave

- **NTC par. 2.4.1**: vita nominale V_N (Tab. 2.4.I)
- **NTC par. 2.4.2**: classi d'uso I/II/III/IV (Tab. 2.4.II: C_U = 0.7/1.0/1.5/2.0)
- **NTC par. 2.4.3**: V_R = V_N * C_U (eq. 2.4.1), clamp a 35 anni
- **NTC par. 3.2.1**: stati limite SLO/SLD/SLV/SLC, Tab. 3.2.I (P_VR = 81/63/10/5%)
- **NTC par. 3.2.2**: categorie sottosuolo A/B/C/D/E + S1/S2 (rifiutate, richiedono RSL)
- **NTC par. 3.2.3.2.1**: spettro orizzontale, eq. 3.2.4 (a tratti), eq. 3.2.6 (eta), eq. 3.2.7-3.2.8 (T_B, T_C, T_D)
- **NTC Tab. 3.2.IV**: formule SS, CC per categoria sottosuolo (clamp ai limiti)
- **NTC Tab. 3.2.V**: ST per categoria topografica (T1=1.0, T2=T3=1.2, T4=1.4 in sommita')
- **NTC Allegato A**: reticolo INGV + interpolazione log-log sui 9 T_R {30,50,72,101,140,201,475,975,2475}
- **Circ. 7/2019 par. C3.2**: commento applicativo, esempi numerici

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti in `references/estratti/` (par. 3.2, Allegato A, Circ. C3.2) sono materiale di citazione normativa: ti servono per spiegare i passaggi, NON per riprodurre Se(T), TR, S, SS, CC, eta, TB/TC/TD in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/spettro.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non inventare parametri di pericolosita'** a_g/F_0/T_C* per il sito: la skill richiede i 9 valori dall'utente. Mai estrarli da memoria o da training data.
- **Non eseguire il calcolo per S1/S2**: NTC par. 3.2.2 prescrive analisi di risposta sismica locale. Il modulo Python solleva `ValueError`; l'agent deve riportare il messaggio bloccante e suggerire RSL.
- **Non estrapolare fuori reticolo**: se T_R < 30 o T_R > 2475 anni, il modulo solleva errore; non aggirarlo.
- **Non confondere spettro elastico Se(T) e spettro di progetto S_d(T)**: la skill calcola solo Se(T). La riduzione con q dipende da scelte progettuali, fuori scope.
- **Non applicare ST T2/T3/T4 senza chiedere se l'edificio e' in sommita'**: per quote intermedie va interpolato (NTC eq. 3.2.5), correzione non automatizzata.
- **Non sostituire la categoria sottosuolo con un'altra "vicina"** se il dato dichiarato dal committente non corrisponde alla relazione geologica: chiedere chiarimento.
- **Non usare path relativi tipo `tasks/lib/spettro.py`** nei comandi Bash: la CWD dell'utente quasi mai coincide con la skill. Usa sempre `${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py` (Claude Code) o il path assoluto della skill installata (Codex / altri).

### Cosa fare

- **Citare sempre il paragrafo NTC** per ogni passaggio (es. "P_VR=10% per SLV - Tab. 3.2.I NTC", "T_C = C_C * T_C* - eq. 3.2.7 NTC").
- **Eseguire il modulo Python** `tasks/lib/spettro.py` per il calcolo, non riprodurre i numeri "a mano". Output del modulo + parafrasi in linguaggio naturale.
- **Mostrare la struttura completa**: per ciascuno SL stampare TR, ag, F0, Tc*, SS, ST, S, CC, eta, TB, TC, TD prima della tabella Se(T).
- **Concludere con rinvio al progettista**: "L'output va verificato dal progettista strutturale firmatario prima dell'uso. Lo spettro di progetto S_d(T) richiede scelta del fattore q (par. 3.2.3.5 e par. 7), non eseguita dalla skill."
- **Quando l'utente chiede confronto vs altro software**: se i numeri divergono entro tolleranze (vedi `tasks/run-test-suite.md`), spiegare che differenze sotto soglia sono attese (interpolazione finita, arrotondamenti); sopra soglia sono bug da segnalare.

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere strutturista che esegua confronto vs foglio CSLP su almeno 10 casi reali (siti sparsi sul territorio italiano, categorie sottosuolo diverse, classi d'uso diverse).

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh spettro-risposta-ntc`); test suite Python: 44/44 pass (12 classi: formule chiuse, raccordi, interpolazione, validazione input hardening, copertura categorie D/E/T2/T3/T4 e xi != 5%, anti-drift fixture-based su `examples/caso-conforme-.../{input,expected}.json`, CLI con --input-json + error handling friendly su chiavi mancanti, stato_limite invalido, file --tr-riferimento incompleto). Livello 2 (confronto vs foglio CSLP su 10+ casi reali) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-spettro.md`
  - `tasks/valida-input-sito.md`
  - `tasks/run-test-suite.md`
- Modulo di calcolo: `tasks/lib/spettro.py` + `tasks/lib/test_spettro.py`
- Esempi: 1 conforme (`caso-conforme-fittizio-cu2-c-t1`) + 1 problematico (`caso-problematico-cat-S2`)
