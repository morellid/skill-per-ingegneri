# AGENTS.md - sismabonus-classificazione-rischio-pam

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per la classificazione del rischio sismico di edifici esistenti ai sensi del DM 58/2017 (sismabonus), metodo CONVENZIONALE. Riferimenti normativi: DM 28/2/2017 n. 58 (decreto istitutivo); DM 7/3/2017 n. 65 (sostituisce l'Allegato A - testo letterale di riferimento di questa skill); DM 9/1/2020 n. 24; DM 6/8/2020 n. 329 (modifica art. 3 e Allegato B, NON Allegato A). NTC 2018 (DM 17/1/2018), Circ. MIT 21/1/2019 n. 7. Tutte fonti pubbliche disponibili sul sito MIT e sulla Gazzetta Ufficiale. Target: ingegneri strutturisti italiani che eseguono valutazioni di vulnerabilita' sismica e asseverazioni sismabonus.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **DM 58/2017** (28/2/2017) - id `dm-58-2017`. Decreto istitutivo delle Linee guida (Allegato A originale poi sostituito).
- **DM 65/2017** (7/3/2017) - id `dm-65-2017`. **Sostituisce** l'Allegato A originale del DM 58/2017 con la versione vigente (testo letterale di riferimento di questa skill, fetched da PDF MIT ufficiale).
- **DM 24/2020** (9/1/2020) - id `dm-24-2020`. Aggiornamento successivo.
- **DM 329/2020** (6/8/2020) - id `dm-329-2020`. **Modifica art. 3 del DM 58/2017** (commi 4-bis, 4-ter, 4-quater: super-sismabonus 110%, polizza assicurativa, SAL) e **sostituisce l'Allegato B** (asseverazione tecnica). NON modifica l'Allegato A. Fuori scope diretto della skill (tocca asseverazione e adempimenti fiscali, non la procedura di calcolo).
- **NTC 2018** (DM 17/1/2018) - id `ntc-2018`. Cap. 3.2 azione sismica, cap. 8 costruzioni esistenti.
- **Circolare 7/2019 MIT** (21/1/2019) - id `circ-7-2019`. Cap. C8 commento a costruzioni esistenti.

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dm-58-2017-allegato-a-formula-pam.md` - Allegato A punto 2.1: definizione PAM, Curva di Individuazione, formula trapezoidale, %CR per SL.
- `dm-58-2017-allegato-a-isv.md` - Allegato A punto 2.2: definizione IS-V.
- `dm-58-2017-allegato-a-tabelle-classi.md` - Allegato A punto 2.3: tabelle classi PAM (8 classi A+..G) e IS-V (7 classi A+..F), regola classe finale.
- `dm-58-2017-allegato-a-salto-classi.md` - Allegato A punto 3 e art. 3 DM 58: regola del salto classi e rinvio alle aliquote fiscali (fuori scope skill).

## Articoli e punti chiave

- **DM 58/2017 art. 3** (modificato da DM 329/2020 con commi 4-bis, 4-ter, 4-quater): l'attribuzione della classe di rischio e' "determinata in base ai parametri convenzionali PAM e IS-V" (rinvio Allegato A).
- **Allegato A punto 1**: oggetto e ambito - costruzioni in generale; metodo convenzionale per qualsiasi tipologia, metodo semplificato solo per muratura (fuori scope della skill).
- **Allegato A punto 2.1**: definizione PAM come area sottesa alla Curva di Individuazione; formula trapezoidale (passo 7): PAM = Σ_{i=2}^{5} [λ(SL_i) − λ(SL_{i-1})] × [CR(SL_i) + CR(SL_{i-1})] / 2 + λ(SLC) × CR(SLR), con SL_1=SLID (TR=10 anni convenzionale, CR=0%), SL_2=SLO (CR=7%), SL_3=SLD (CR=15%), SL_4=SLV (CR=50%), SL_5=SLC (CR=80%), SLR (CR=100% al λ di SLC).
- **Allegato A punto 2.1 passo 3** (capping prescritto): TR_C(SLO) := min(TR_C(SLO), TR_C(SLV)); TR_C(SLD) := min(TR_C(SLD), TR_C(SLV)). "Si assume, di fatto, che non si possa raggiungere lo stato limite di salvaguardia della vita senza aver raggiunto gli stati limite di operativita' e danno." Il modulo applica questo capping di default (flag CLI `--no-capping` per disattivarlo).
- **Allegato A punto 2.1 nota a Tab. 1** (verifica numerica): "una costruzione con periodo di riferimento V_R pari a 50 anni, le cui prestazioni siano puntualmente pari ai minimi NTC [...] ha un valore di PAM pari a 1,13%". Test `test_pam_riferimento_decreto_VR_50` riproduce esattamente questo numero.
- **Allegato A punto 2.1 passo 9-11**: IS-V = PGA_C(SLV) / PGA_D(SLV); classe PAM da Tab. 1; classe IS-V da Tab. 2; classe finale = peggiore.
- **Allegato A Tab. 1** classi PAM: A+ ≤ 0,50%, A ≤ 1,0%, B ≤ 1,5%, C ≤ 2,5%, D ≤ 3,5%, E ≤ 4,5%, F ≤ 7,5%, G ≥ 7,5% (lower bound escluso, upper bound incluso).
- **Allegato A Tab. 2** classi IS-V: A+ > 100%, A 80-<100%, B 60-<80%, C 45-<60%, D 30-<45%, E 15-<30%, F ≤ 15% (lower bound INCLUSO, upper bound ESCLUSO; bordo IS-V = 100% formalmente non coperto, interpretazione conservativa = A).
- **Allegato A par. introduttivo "Laddove si preveda l'esecuzione di interventi..."**: salto classi - "l'attribuzione della Classe di Rischio pre e post intervento deve essere effettuata utilizzando il medesimo metodo e con le stesse modalita' di analisi e di verifica".
- **NTC 2018 par. 3.2.1 + Tab. 3.2.I**: P_VR = 81/63/10/5 % per SLO/SLD/SLV/SLC -> da cui TR_D di domanda.
- **NTC 2018 par. 8**: criteri di valutazione di sicurezza per costruzioni esistenti (analisi lineari/non lineari, livelli di conoscenza LC1/LC2/LC3, fattori di confidenza). Output: PGA_C(SL) per ciascun SL.

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti in `references/estratti/` (Allegato A punti 2.1/2.2/2.3 + tabelle classi) sono materiale di citazione normativa: ti servono per spiegare i passaggi, NON per riprodurre PAM, IS-V, classi in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/sismabonus.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non inventare TR_C o PGA_C** per l'edificio: la skill richiede questi valori dall'utente come output dell'analisi di vulnerabilita'. Mai estrarli da memoria, da training data o da plausibilita' percettiva.
- **Non implementare il metodo semplificato muratura** (Allegato A punto 3, tabelle tipologie): non e' nello scope della v0.1.0-alpha. Se l'utente chiede questo metodo, segnala che non e' supportato e rinvia al testo letterale dell'Allegato A.
- **Non generare Allegato B / B-bis pronto al deposito**: la skill produce numeri e classi, non documenti firmabili. Non simulare il modulo ministeriale.
- **Non interpretare le aliquote di detrazione fiscale sismabonus** (50/70/75/80/85%): cambiano per legge finanziaria; non sono nello scope della skill. Suggerire al committente di rivolgersi a commercialista o consulente fiscale.
- **Capping passo 2.1.3 e' applicato di default**, NON inventato dal modulo: e' prescritto dal decreto. Non disattivarlo via `--no-capping` se non per validazione vs software che applicano il capping a monte (input gia' capped) o per analisi avanzate giustificate.
- **Non "correggere" automaticamente la non monotonia residua** dopo il capping (caso TR_C(SLO) > TR_C(SLD), ecc., non disciplinato dal decreto): il modulo segnala `monotona=False` ma calcola comunque. Riportare il warning e rinviare al progettista per la diagnosi (errore di analisi? edificio realmente fragile e rigido? interpretazione conservativa da applicare?).
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
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh sismabonus-classificazione-rischio-pam`); test suite Python: 55/55 pass, incluso il test `test_pam_riferimento_decreto_VR_50` che verifica numericamente PAM = 1,13% per il caso V_R=50 ai minimi NTC dichiarato dal decreto stesso (Allegato A nota a Tab. 1). Livello 2 (confronto vs software certificati su 10+ edifici reali) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-classificazione.md`
  - `tasks/valida-input.md`
  - `tasks/run-test-suite.md`
- Modulo di calcolo: `tasks/lib/sismabonus.py` + `tasks/lib/test_sismabonus.py`
- Esempi: 1 conforme (`caso-conforme-fittizio`) + 1 problematico (`caso-non-monotono`)
