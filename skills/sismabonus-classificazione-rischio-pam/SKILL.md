---
name: sismabonus-classificazione-rischio-pam
description: Calcolo code-driven della classe di rischio sismico di un edificio ai sensi del DM 58/2017 Allegato A (testo aggiornato DM 65/2017, DM 24/2020, DM 329/2020), con il metodo convenzionale: PAM (Perdita Annua Media) come area trapezoidale della Curva di Individuazione su SLID/SLO/SLD/SLV/SLC + termine di coda SLR, IS-V (Indice di Sicurezza per la Vita) come PGA_C(SLV)/PGA_D(SLV), classe finale come la peggiore tra classe PAM (8 classi A+..G) e classe IS-V (7 classi A+..F), salto classi tra stato di fatto e stato di progetto. Implementazione deterministica e riproducibile: la versione 0.1.0-alpha include solo test di consistenza interna delle formule; la validazione di campo (confronto numerico vs software certificati ClaSS / CDM Win / EdiSis / MasterSap-SismiClass su 10+ edifici reali) e' prerequisito del release stabile e non e' ancora stata eseguita. Skill solo per il METODO CONVENZIONALE su edifici esistenti; il metodo semplificato per edifici in muratura e la generazione dei modelli di asseverazione (Allegato B / B-bis) sono fuori scope di questa versione. Use when an Italian structural engineer asks to compute the seismic risk class of an existing building under DM 58/2017 (sismabonus), check whether an intervention produces a class jump, or verify PAM/IS-V values produced by other software. Target users are structural engineers preparing sismabonus asseverations or vulnerability studies under NTC 2018 cap. 8.
license: MIT
---

# Classificazione rischio sismico DM 58/2017 - PAM + IS-V (sismabonus)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve:
- Calcolare la classe di rischio sismico (A+, A, B, C, D, E, F, G) di un edificio esistente con il METODO CONVENZIONALE del DM 58/2017 Allegato A, dato l'output dell'analisi di vulnerabilita' (PGA_C e TR_C per i 4 SL NTC: SLO, SLD, SLV, SLC) e i parametri sismici al sito (PGA_D dalle NTC 2018 par. 3.2)
- Calcolare il PAM (Perdita Annua Media) come area sottesa alla Curva di Individuazione (formula trapezoidale a 5 punti SLID->SLO->SLD->SLV->SLC + termine di coda SLR=100% al λ di SLC)
- Calcolare l'IS-V (Indice di Sicurezza per la Vita) = PGA_C(SLV) / PGA_D(SLV)
- Determinare la classe finale come la peggiore tra classe PAM e classe IS-V (Allegato A punto 2.3)
- Confrontare uno stato di fatto e uno stato di progetto e calcolare il salto classi (numero di classi guadagnate dall'intervento), come indicatore tecnico per l'asseverazione sismabonus
- Verificare valori di PAM, IS-V o classe prodotti da altri software (ClaSS, CDM Win, EdiSis, MasterSap-SismiClass)

**Non usare** quando l'utente chiede:
- Il METODO SEMPLIFICATO per edifici in muratura (DM 58/2017 Allegato A punto 3, tabelle tipologie x numero piani): fuori scope di questa versione 0.1.0-alpha
- L'esecuzione dell'analisi di vulnerabilita' sismica (NTC 2018 cap. 8): la skill prende PGA_C e TR_C in input, non li calcola. La skill non sostituisce il modello strutturale ne' l'analisi (lineare, pushover, time-history)
- La generazione del modello di asseverazione tecnica Allegato B / B-bis pronto al deposito (firma del professionista, marca da bollo, allegati grafici): la skill produce i numeri e la classe, l'asseverazione formale e' a carico del professionista
- Il calcolo delle aliquote di detrazione fiscale sismabonus (50%, 70%, 75%, 80%, 85%): variano nel tempo per legge finanziaria, fuori scope. La skill produce il salto classi; l'aliquota applicabile va verificata dal commercialista o da norme fiscali vigenti
- Edifici nuovi: la classificazione DM 58/2017 si applica a edifici esistenti per la valutazione del miglioramento conseguente a intervento. Per edifici nuovi vale per definizione la classe associata al nuovo livello di sicurezza progettuale (NTC 2018)
- Edifici a destinazione monumentale o tutelati ex Codice dei Beni Culturali: l'applicabilita' del sismabonus e del DM 58/2017 e' specifica e va verificata caso per caso (DPCM Beni Culturali 9/2/2011)

## Avvertenza

Questa skill e' uno strumento di supporto al calcolo di PAM, IS-V e classe di rischio sismico DM 58/2017. **Non sostituisce il giudizio del progettista strutturale firmatario.** L'output e' deterministico (formule chiuse trapezoidali) e quindi **confrontabile** dal progettista contro software certificati (ClaSS, CDM Win, EdiSis, MasterSap-SismiClass): il confronto resta in capo al professionista. **Nello stato v0.1.0-alpha la skill non e' ancora stata validata con confronto numerico vs software certificati su casi reali**; i test interni coprono solo la consistenza delle formule, i bordi delle tabelle classi e l'anti-drift fixture-based. La skill non produce l'asseverazione tecnica Allegato B / B-bis pronta al deposito e non firma elaborati. **L'analisi di vulnerabilita' (NTC 2018 cap. 8) che produce PGA_C e TR_C per i 4 SL NTC e' prerequisito non automatizzato dalla skill: e' responsabilita' esclusiva del progettista strutturale.**

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Calcolo classificazione**: l'utente chiede "qual e' la classe di rischio?", "calcola PAM e IS-V per questo edificio", "che classe esce con questi TR_C?", "confronta fatto e progetto e dimmi il salto" -> leggi [`tasks/calcola-classificazione.md`](tasks/calcola-classificazione.md)
- **Validazione input edificio**: l'utente chiede "i miei TR_C e PGA_C sono coerenti?", "la curva e' monotona?", "l'analisi e' affidabile per la classificazione?" -> leggi [`tasks/valida-input.md`](tasks/valida-input.md)
- **Esecuzione test suite**: utente o validatore vuole verificare la consistenza interna del modulo (formule, bordi tabelle, validazione input, fixture esempio) o pianificare la validazione di campo vs software certificati -> leggi [`tasks/run-test-suite.md`](tasks/run-test-suite.md)

Se la richiesta e' generica ("aiutami con il sismabonus"), chiedi se l'utente vuole solo classificare lo stato di fatto, confrontare fatto+progetto per il salto classi, o validare gli input. La sequenza naturale e': prima `valida-input` (sanity check su monotonia e coerenza fisica), poi `calcola-classificazione`.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule chiuse del DM 58/2017 Allegato A (PAM trapezoidale, IS-V, classificazione, salto classi) sono implementate nel modulo Python [`tasks/lib/sismabonus.py`](tasks/lib/sismabonus.py). La test suite [`tasks/lib/test_sismabonus.py`](tasks/lib/test_sismabonus.py) copre **solo consistenza interna**: formula PAM (4 trapezoidi + coda SLR), bordi delle tabelle classi PAM (8 classi A+..G) e IS-V (7 classi A+..F), regola "classe finale = peggiore" (Allegato A punto 2.3), regola salto classi, rilevamento curva non monotona (warning sull'edificio fisicamente incongruente), validazione input (NaN/inf, negativi, stringhe, bool, JSON RFC 8259), CLI con --input-json + error handling friendly su chiavi mancanti, anti-drift fixture-based su `examples/caso-conforme-fittizio/{input,expected}.json`. **Non** confronta vs software certificati: la validazione di campo e' prerequisito del release stabile e va eseguita seguendo `tasks/run-test-suite.md`.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni calcolo numerico (lambda da TR, PAM, IS-V, classi PAM/IS-V, classe finale, salto classi) **devi invocare il modulo Python via Bash**. NON riprodurre i numeri "a mano" leggendo le formule dagli estratti in `references/estratti/`: gli estratti sono materiale di citazione normativa, non sostituiscono l'esecuzione del modulo. Calcolare a mano vanifica l'intera ragion d'essere della skill (output deterministico e riproducibile, confrontabile dal progettista) e introduce errore stocastico.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill. Usala in tutti i comandi Bash:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/sismabonus.py --help
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/sismabonus.py --input-json caso.json
```

In Codex e altri agent compatibili AGENTS.md la variabile potrebbe non essere risolta: in tal caso sostituiscila con il path assoluto della directory che contiene **questo** `SKILL.md` (l'agent conosce sempre il path da cui ha caricato la skill). Non usare path relativi tipo `tasks/lib/sismabonus.py`: la CWD dell'utente quasi mai coincide con la skill dir.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' richiesta dall'utente.
2. Carica il task file specifico in `tasks/`.
3. Acquisisci dall'utente i dati necessari per ciascuno stato (di fatto, eventualmente di progetto):
   - Per ciascuno dei 4 SL NTC (SLO, SLD, SLV, SLC):
     - **TR_C** [anni]: periodo di ritorno di capacita' dell'evento che porta l'edificio a quel SL (output dell'analisi di vulnerabilita', NTC 2018 cap. 8)
     - **PGA_C** [g]: accelerazione di picco al suolo di capacita' associata
     - **PGA_D** [g]: accelerazione di picco al suolo di domanda al sito (NTC 2018 par. 3.2 + Allegato A)
   - SLID e' convenzionale: TR=10 anni, CR=0% (Allegato A punto 2.1).
   - SLR e' convenzionale: stesso lambda di SLC, CR=100% (termine di coda della formula PAM).
4. Costruisci il file JSON di input (formato in `tasks/calcola-classificazione.md`) e invoca il modulo Python con `--input-json`.
5. Riporta in chat l'output JSON del modulo accompagnato dalla parafrasi in linguaggio naturale, con citazione esplicita degli articoli del DM 58/2017 Allegato A.
6. Concludi con rinvio al progettista strutturale firmatario per la verifica dei numeri e per la redazione dell'asseverazione tecnica (Allegato B / B-bis), che la skill non produce.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM Min. Infrastrutture e Trasporti 28/2/2017 n. 58 - Linee guida per la classificazione del rischio sismico delle costruzioni
- DM MIT 7/3/2017 n. 65 - sostituzione dell'Allegato A
- DM MIT 9/1/2020 n. 24 - aggiornamento sezioni Allegato A
- DM MIT 6/8/2020 n. 329 - aggiornamento ulteriore (testo coordinato vigente)
- NTC 2018 (DM 17/1/2018) - cap. 3.2 (azione sismica al sito), cap. 8 (costruzioni esistenti)
- Circ. MIT 21/1/2019 n. 7 - cap. C8 (commento a NTC cap. 8)

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non esegue l'analisi di vulnerabilita' (NTC 2018 cap. 8): l'utente deve fornire TR_C, PGA_C per i 4 SL NTC, prodotti dal progettista strutturale tramite analisi conformi
- Non incorpora il reticolo INGV per PGA_D: l'utente deve fornire PGA_D per i 4 SL NTC, prodotti seguendo NTC par. 3.2 + Allegato A (vedi anche skill `spettro-risposta-ntc` per supporto al calcolo dello spettro/PGA al sito)
- Non implementa il METODO SEMPLIFICATO per edifici in muratura (Allegato A punto 3): fuori scope di questa versione
- Non genera l'Allegato B / B-bis (asseverazione tecnica del professionista): produce solo i numeri e la classe; il modulo formale e' a cura del professionista firmatario
- Non determina le aliquote di detrazione fiscale sismabonus: variano per legge finanziaria, fuori scope della skill (rinvio al commercialista o al professionista delegato)
- Non gestisce edifici a destinazione monumentale o tutelati ex Codice dei Beni Culturali (DPCM 9/2/2011): l'applicabilita' va verificata caso per caso
- Non sostituisce la firma del progettista strutturale sull'asseverazione

**Ogni output va verificato dal progettista strutturale prima di essere usato per asseverazione, deposito al SUE o richiesta di detrazione fiscale.**
