---
name: spettro-risposta-ntc
description: Calcola lo spettro di risposta elastico in accelerazione (componente orizzontale) ai sensi delle NTC 2018 par. 3.2 e Circolare 7/2019, dato il sito (parametri ag, F0, Tc* dal reticolo INGV per i 9 TR di riferimento), la vita nominale, la classe d'uso, la categoria di sottosuolo e la categoria topografica. Output: tempi di ritorno TR per gli stati limite SLO/SLD/SLV/SLC, parametri ag/F0/Tc* interpolati al TR di progetto, parametri costruttivi S, eta, TB, TC, TD e ordinate Se(T) tabulate. Implementazione code-driven con test suite, output verificabile vs foglio Excel CSLP. Use when an Italian structural engineer asks to compute the NTC 2018 elastic response spectrum, look up site seismic parameters interpolated on the return period, build the response spectrum table for a limit state, or verify spectrum values produced by other software. Target users are structural engineers preparing seismic design or assessment of new and existing buildings under NTC 2018.
license: MIT
---

# Spettro di risposta elastico NTC 2018 (par. 3.2)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve:
- Calcolare lo spettro di risposta elastico in accelerazione (componente orizzontale) ai sensi di NTC 2018 par. 3.2.3, per uno o piu' degli stati limite SLO, SLD, SLV, SLC, dati i parametri sismici di pericolosita' al sito
- Determinare il tempo di ritorno TR di progetto a partire da vita nominale VN e classe d'uso CU (par. 2.4) e dalla probabilita' di superamento PVR per ciascuno stato limite (Tab. 3.2.I)
- Interpolare logaritmicamente sui 9 TR di riferimento del reticolo INGV (Allegato A NTC) i parametri ag, F0, Tc* al TR di progetto
- Costruire e tabulare le ordinate Se(T) per uno o piu' stati limite, da utilizzare come input ad analisi statiche lineari, modali, push-over o time-history
- Verificare valori di spettro prodotti da altri software o fogli di calcolo, confrontandoli con la formulazione normativa

**Non usare** quando l'utente chiede:
- Lo spettro di risposta verticale (par. 3.2.3.2.2 NTC) - la versione corrente della skill copre solo la componente orizzontale par. 3.2.3.2.1
- Lo spettro di progetto Sd(T) ridotto da fattore q (par. 3.2.3.5) - la skill produce lo spettro elastico Se(T); la riduzione con q dipende da scelte progettuali sul sistema strutturale e va fatta a valle dal progettista
- Categorie di sottosuolo S1 o S2: NTC par. 3.2.2 prescrive analisi specifiche di risposta sismica locale, fuori scope di questa skill
- Calcolo dei parametri ag, F0, Tc* per coordinate non disponibili sul reticolo INGV (estrapolazione fuori reticolo): la skill richiede che l'utente fornisca i 9 valori per i TR di riferimento, ricavati da INGV o foglio Excel CSLP
- Valutazione della classe di rischio sismico (DM 58/2017) o calcolo PAM: skill diversa, candidata in roadmap
- Analisi non lineari di edificio completo (push-over, time-history su modello FEM)

## Avvertenza

Questa skill e' uno strumento di supporto al calcolo dello spettro di risposta NTC 2018. **Non sostituisce il giudizio del progettista strutturale firmatario.** L'output e' verificabile contro il foglio Excel CSLP e contro software di calcolo strutturale certificati: la responsabilita' del controllo dei valori e dell'uso nello spettro di progetto resta in capo al progettista. La skill non produce relazioni di calcolo pronte al deposito al Genio Civile e non firma elaborati. **Per categorie di sottosuolo S1 o S2 la skill rifiuta il calcolo e rinvia ad analisi specifiche di risposta sismica locale come prescritto da NTC par. 3.2.2.**

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Calcolo dello spettro elastico**: l'utente chiede "calcola lo spettro NTC", "qual e' Se(T) per il sito X?", "dammi i parametri S, eta, TB, TC, TD per SLV", "tabulami lo spettro per il mio sito" -> leggi [`tasks/calcola-spettro.md`](tasks/calcola-spettro.md)
- **Validazione input sito**: l'utente chiede "i miei input sono coerenti?", "il reticolo INGV copre questo sito?", "VN/CU/PVR sono ragionevoli per questa opera?" -> leggi [`tasks/valida-input-sito.md`](tasks/valida-input-sito.md)
- **Esecuzione test suite**: utente o validatore vuole verificare che il modulo Python produca i valori attesi rispetto al foglio CSLP -> leggi [`tasks/run-test-suite.md`](tasks/run-test-suite.md)

Se la richiesta e' generica ("aiutami con lo spettro NTC"), chiedi se l'utente vuole calcolare lo spettro completo o solo validare gli input. La sequenza naturale e': prima `valida-input-sito` (sanity check), poi `calcola-spettro`.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule chiuse di NTC par. 3.2.3 sono implementate nel modulo Python [`tasks/lib/spettro.py`](tasks/lib/spettro.py). La test suite [`tasks/lib/test_spettro.py`](tasks/lib/test_spettro.py) verifica i valori contro casi di confronto con il foglio Excel CSLP.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni calcolo numerico (TR, ag/F0/Tc* interpolati, S, eta, TB/TC/TD, Se(T)) **devi invocare il modulo Python via Bash**. NON riprodurre i numeri "a mano" leggendo le formule dagli estratti in `references/estratti/`: gli estratti sono materiale di citazione normativa, non sostituiscono l'esecuzione del modulo. Calcolare a mano vanifica l'intera ragion d'essere della skill (output deterministico verificabile vs CSLP) e introduce errore stocastico.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill. Usala in tutti i comandi Bash:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py --help
```

In Codex e altri agent compatibili AGENTS.md la variabile potrebbe non essere risolta: in tal caso sostituiscila con il path assoluto della directory che contiene **questo** `SKILL.md` (l'agent conosce sempre il path da cui ha caricato la skill). Non usare path relativi tipo `tasks/lib/spettro.py`: la CWD dell'utente quasi mai coincide con la skill dir.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' richiesta dall'utente.
2. Carica il task file specifico in `tasks/`.
3. Acquisisci dall'utente i dati necessari: vita nominale VN (anni), classe d'uso (I/II/III/IV), categoria di sottosuolo (A/B/C/D/E - rifiuta S1/S2), categoria topografica (T1/T2/T3/T4) ed eventuale altezza relativa per coefficiente ST se non in sommita', i 9 valori (ag in g, F0 adim., Tc* in s) per i TR di riferimento {30, 50, 72, 101, 140, 201, 475, 975, 2475} anni, smorzamento viscoso xi (% - default 5%).
4. Esegui il calcolo invocando le funzioni del modulo (citate nel task file), con citazione esplicita della formula NTC.
5. Produci output strutturato (tabelle TR per SL, parametri spettrali, ordinate Se(T) tabulate, eventuale CSV).
6. Concludi con rinvio al progettista per verifica del valore di q, dello spettro di progetto Sd(T), e delle scelte di modellazione.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM 17/01/2018 (NTC 2018) - in particolare par. 2.4 (vita nominale, classi d'uso, vita di riferimento), par. 3.2 (azione sismica, definizioni stati limite, categorie di sottosuolo, spettro di risposta elastico), Allegato A (reticolo di riferimento, 9 TR)
- Circolare MIT n. 7 del 21/01/2019 - par. C2.4 e C3.2 con commento applicativo e procedure di interpolazione

Estratti testuali in [`references/estratti/`](references/estratti/).

Parametri di pericolosita' al sito (ag, F0, Tc* per i 9 TR): consultabili sul servizio INGV [zonesismiche.mi.ingv.it](http://zonesismiche.mi.ingv.it/) o sul foglio Excel CSLP.

## Limiti

Questa skill NON fa:
- Non incorpora il reticolo INGV: l'utente deve fornire i 9 valori (ag, F0, Tc*) per i TR di riferimento al sito di interesse
- Non calcola lo spettro verticale (par. 3.2.3.2.2)
- Non calcola lo spettro di progetto Sd(T) con riduzione da q (par. 3.2.3.5)
- Non gestisce categorie di sottosuolo S1 e S2 (richiedono analisi specifiche di risposta sismica locale, par. 3.2.2)
- Non sostituisce la relazione geologica/geotecnica per la determinazione di Vs,30 e della categoria di sottosuolo
- Non sostituisce la firma del progettista strutturale sulle relazioni di calcolo

**Ogni output va verificato dal progettista strutturale prima di essere usato per analisi di calcolo, dimensionamento o asseverazione.**
