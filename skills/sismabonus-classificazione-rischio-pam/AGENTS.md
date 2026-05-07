# AGENTS.md - sismabonus-classificazione-rischio-pam

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per la classificazione del rischio sismico di edifici esistenti ai sensi del DM 58/2017 (sismabonus), metodo CONVENZIONALE. Riferimenti normativi: DM 28/2/2017 n. 58 (testo aggiornato dal DM 7/3/2017 n. 65, dal DM 9/1/2020 n. 24, dal DM 6/8/2020 n. 329), NTC 2018 (DM 17/1/2018), Circ. MIT 21/1/2019 n. 7. Tutte fonti pubbliche disponibili sul sito MIT e sulla Gazzetta Ufficiale. Target: ingegneri strutturisti italiani che eseguono valutazioni di vulnerabilita' sismica e asseverazioni sismabonus.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **DM 58/2017** (28/2/2017) - id `dm-58-2017`, hash da calcolare al fetch (`./scripts/fetch-sources.sh`). Decreto istitutivo delle Linee guida.
- **DM 65/2017** (7/3/2017) - id `dm-65-2017`. Sostituzione Allegato A (versione attualmente vigente come base, con ulteriori modifiche).
- **DM 24/2020** (9/1/2020) - id `dm-24-2020`. Aggiornamento Allegato A dopo NTC 2018.
- **DM 329/2020** (6/8/2020) - id `dm-329-2020`. Ulteriore aggiornamento (testo coordinato attualmente vigente).
- **NTC 2018** (DM 17/1/2018) - id `ntc-2018`. Cap. 3.2 azione sismica, cap. 8 costruzioni esistenti.
- **Circolare 7/2019 MIT** (21/1/2019) - id `circ-7-2019`. Cap. C8 commento a costruzioni esistenti.

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dm-58-2017-allegato-a-formula-pam.md` - Allegato A punto 2.1: definizione PAM, Curva di Individuazione, formula trapezoidale, %CR per SL.
- `dm-58-2017-allegato-a-isv.md` - Allegato A punto 2.2: definizione IS-V.
- `dm-58-2017-allegato-a-tabelle-classi.md` - Allegato A punto 2.3: tabelle classi PAM (8 classi A+..G) e IS-V (7 classi A+..F), regola classe finale.
- `dm-58-2017-allegato-a-salto-classi.md` - Allegato A punto 3 e art. 3 DM 58: regola del salto classi e rinvio alle aliquote fiscali (fuori scope skill).

## Articoli e punti chiave

- **DM 58/2017 art. 3**: l'attribuzione della classe di rischio e' "determinata in base ai parametri convenzionali PAM e IS-V" (rinvio Allegato A).
- **Allegato A punto 1**: oggetto e ambito - edifici esistenti, esclusi nuovi e tutelati monumentali (con specifica disciplina).
- **Allegato A punto 2.1**: definizione PAM come area sottesa alla Curva di Individuazione; formula trapezoidale: PAM = Σ_{i=2}^{5} [λ(SL_i) − λ(SL_{i-1})] × [CR(SL_i) + CR(SL_{i-1})] / 2 + λ(SLC) × CR(SLR), con SL_1=SLID (TR=10 anni convenzionale, CR=0%), SL_2=SLO (CR=7%), SL_3=SLD (CR=15%), SL_4=SLV (CR=50%), SL_5=SLC (CR=80%), SLR (CR=100% al λ di SLC).
- **Allegato A punto 2.2**: IS-V = PGA_C(SLV) / PGA_D(SLV).
- **Allegato A punto 2.3**: tabelle classi PAM (A+ ≤ 0.50%, A ≤ 1.0%, B ≤ 1.5%, C ≤ 2.5%, D ≤ 3.5%, E ≤ 4.5%, F ≤ 7.5%, G > 7.5%) e classi IS-V (A+ > 100%, A 80-100%, B 60-80%, C 45-60%, D 30-45%, E 15-30%, F < 15%); regola classe finale = peggiore tra le due.
- **Allegato A punto 3**: salto classi tra stato di fatto e stato di progetto, indicatore di efficacia dell'intervento di miglioramento sismico ai fini sismabonus.
- **NTC 2018 par. 3.2.1 + Tab. 3.2.I**: P_VR = 81/63/10/5 % per SLO/SLD/SLV/SLC -> da cui TR_D di domanda.
- **NTC 2018 par. 8**: criteri di valutazione di sicurezza per costruzioni esistenti (analisi lineari/non lineari, livelli di conoscenza LC1/LC2/LC3, fattori di confidenza). Output: PGA_C(SL) per ciascun SL.

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti in `references/estratti/` (Allegato A punti 2.1/2.2/2.3 + tabelle classi) sono materiale di citazione normativa: ti servono per spiegare i passaggi, NON per riprodurre PAM, IS-V, classi in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/sismabonus.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non inventare TR_C o PGA_C** per l'edificio: la skill richiede questi valori dall'utente come output dell'analisi di vulnerabilita'. Mai estrarli da memoria, da training data o da plausibilita' percettiva.
- **Non implementare il metodo semplificato muratura** (Allegato A punto 3, tabelle tipologie): non e' nello scope della v0.1.0-alpha. Se l'utente chiede questo metodo, segnala che non e' supportato e rinvia al testo letterale dell'Allegato A.
- **Non generare Allegato B / B-bis pronto al deposito**: la skill produce numeri e classi, non documenti firmabili. Non simulare il modulo ministeriale.
- **Non interpretare le aliquote di detrazione fiscale sismabonus** (50/70/75/80/85%): cambiano per legge finanziaria; non sono nello scope della skill. Suggerire al committente di rivolgersi a commercialista o consulente fiscale.
- **Non "correggere" automaticamente la non monotonia di lambda** (caso TR_C(SLO) > TR_C(SLD), ecc.): il modulo segnala `monotona=False` ma calcola comunque. Riportare il warning e rinviare al progettista per la diagnosi (errore di analisi? edificio realmente non duttile? capping da applicare?).
- **Non sostituire PGA_D al sito** con valori "tipici" o di altri siti: la PGA_D dipende dal sito e va presa dal reticolo INGV / spettro NTC. Se l'utente non l'ha calcolata, suggerire la skill `spettro-risposta-ntc` per il calcolo dello spettro orizzontale e l'estrazione di PGA_D = a_g × S × η × F_0 (al periodo zero). PGA_D = PGA al sito = a_g × S (per T=0, F_0 e η non rilevanti per il valore di PGA puro).
- **Non confondere PGA di Stato di fatto vs Stato di progetto sul lato DOMANDA**: la PGA_D dipende dal SITO, non dall'edificio. Stato di fatto e Stato di progetto condividono la stessa PGA_D; quello che cambia tra fatto e progetto e' la CAPACITA' (PGA_C, TR_C) per effetto dell'intervento di rinforzo.
- **Non usare path relativi tipo `tasks/lib/sismabonus.py`** nei comandi Bash: la CWD dell'utente quasi mai coincide con la skill. Usa sempre `${CLAUDE_SKILL_DIR}/tasks/lib/sismabonus.py` (Claude Code) o il path assoluto della skill installata (Codex / altri).

### Cosa fare

- **Citare sempre il punto dell'Allegato A** per ogni passaggio (es. "PAM = formula trapezoidale - Allegato A punto 2.1", "IS-V = PGA_C/PGA_D - Allegato A punto 2.2", "classe finale = peggiore - Allegato A punto 2.3").
- **Eseguire il modulo Python** `tasks/lib/sismabonus.py` per il calcolo, non riprodurre i numeri "a mano". Output del modulo + parafrasi in linguaggio naturale.
- **Mostrare la struttura completa**: per stato di fatto e stato di progetto stampare per ciascun SL TR_C, PGA_C, lambda; PAM (con i 4 contributi trapezoidali + coda SLR), classe PAM; IS-V, classe IS-V; classe finale; e (se entrambi gli stati sono forniti) salto classi.
- **Segnalare warning se la curva non e' monotona** (`monotona: false` nell'output): "ATTENZIONE: i TR_C forniti non sono monotonicamente decrescenti per severita' crescente del SL. Verificare l'analisi di vulnerabilita' o applicare capping coerente con il punto 2.1 dell'Allegato A. La PAM calcolata potrebbe non essere fisicamente significativa."
- **Concludere con rinvio al progettista**: "L'output va verificato dal progettista strutturale firmatario prima dell'uso per l'asseverazione tecnica (Allegato B / B-bis). La determinazione dell'aliquota di detrazione fiscale (50/70/75/80/85%) e' demandata alla legislazione fiscale vigente e al commercialista."
- **Quando l'utente chiede confronto vs altro software**: se i numeri divergono entro tolleranze accettabili (per software diversi possono esserci piccole differenze di trapezoidale, capping, arrotondamento), spiegare che differenze sotto soglia (≤ 0.05% in PAM, ≤ 0.5% in IS-V, classe diversa solo al bordo della tabella) sono attese; sopra soglia o classe diversa lontana dal bordo sono bug da segnalare.

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere strutturista esperto di sismabonus che esegua confronto vs software certificati (ClaSS S.I.S., CDM Win STS, EdiSis Newsoft, MasterSap-SismiClass AMV) su almeno 10 edifici reali (mix c.a. / muratura / acciaio, classi sismiche di sito diverse, livelli di conoscenza LC1/LC2/LC3 diversi).

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh sismabonus-classificazione-rischio-pam`); test suite Python: 47 pass + 1 skipped fixture-based (anti-drift su `examples/caso-conforme-fittizio/{input,expected}.json`). Livello 2 (confronto vs software certificati su 10+ edifici reali) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-classificazione.md`
  - `tasks/valida-input.md`
  - `tasks/run-test-suite.md`
- Modulo di calcolo: `tasks/lib/sismabonus.py` + `tasks/lib/test_sismabonus.py`
- Esempi: 1 conforme (`caso-conforme-fittizio`) + 1 problematico (`caso-non-monotono`)
