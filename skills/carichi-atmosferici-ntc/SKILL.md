---
name: carichi-atmosferici-ntc
description: Calcola la pressione del vento p (NTC 2018 par. 3.3) e il carico neve sulla copertura q_s (NTC 2018 par. 3.4) per edifici civili e industriali correnti, dato sito (parametri zonali da Tab. 3.3.I per il vento e classificazione zona/altitudine per la neve), categoria di esposizione I-V, quota di riferimento z, coefficienti di forma c_p / mu_1 e coefficienti dinamici c_d / c_t. Output deterministico tabulato (v_b, c_r, v_r, q_r, c_e, p per il vento; q_sk, mu_1, c_E, q_s per la neve) con citazione esplicita dei paragrafi NTC. Implementazione code-driven, riproducibile. Use when an Italian structural engineer asks to compute NTC 2018 wind pressure or snow load for ordinary buildings, classify exposure category effects, or audit values produced by other software. Target users are structural engineers preparing static design of new and existing buildings under NTC 2018.
license: MIT
---

# Carichi atmosferici NTC 2018 (par. 3.3 vento + par. 3.4 neve)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve:
- Calcolare la pressione del vento p sull'inviluppo dell'edificio ai sensi di NTC 2018 par. 3.3, dato il sito (parametri zonali v_b_0, a_0, k_s da Tab. 3.3.I), la categoria di esposizione I-V, la quota di riferimento z e il coefficiente di forma c_p
- Calcolare il carico della neve q_s sulla copertura ai sensi di NTC 2018 par. 3.4, data la zona (I-Alpina, I-Mediterranea, II, III), l'altitudine a_s, l'inclinazione delle falde alpha e la classe di esposizione (battuta dai venti / normale / riparata)
- Verificare valori prodotti da altri software o fogli di calcolo, confrontandoli con la formulazione normativa
- Costruire un report di calcolo con citazione esplicita dei paragrafi NTC 2018 per la relazione tecnica strutturale

**Non usare** quando l'utente chiede:
- Coefficienti di forma c_p per geometrie non correnti (cupole, ciminiere, schermi, ponti, segnali, paratie): NTC par. 3.3.8 rinvia a documenti di comprovata validita' o prove in galleria del vento, fuori scope di questa skill. La skill richiede c_p come input, calcolato a parte dal progettista
- Azioni del vento sulle strutture sensibili al distacco di vortici, galloping, divergenza aeroelastica: NTC par. 3.3.9 (analisi dinamica) - fuori scope, c_d resta input dell'utente
- Coefficienti di forma per coperture mu_2 / mu_3 (carichi accidentali a deriva, sporgenze, parapetti): la skill copre solo mu_1 di NTC par. 3.4.5.2.1 (copertura ad una/due falde regolari)
- Carichi neve di spostamento o accumulo per ostruzioni / scorrimento: NTC par. 3.4.5.5 e Circolare C3.4 - fuori scope, da valutare separatamente
- Identificazione automatica della zona vento o neve a partire dal Comune o dalle coordinate: la skill non incorpora la mappa nazionale e richiede che l'utente indichi la zona dopo lookup su NTC Tab. 3.3.I e par. 3.4.2 (zone neve)
- Combinazione delle azioni con altri carichi (G1, G2, Q, E): per la matrice di combinazioni vedi la skill `combinazioni-carico-ntc`

## Avvertenza

Questa skill e' uno strumento di supporto al calcolo dei carichi atmosferici NTC 2018. **Non sostituisce il giudizio del progettista strutturale firmatario.** L'output e' deterministico (formule chiuse) ed e' confrontabile dal progettista contro fogli di calcolo o software certificati: il confronto resta in capo al professionista. **Nello stato v0.1.0-alpha la skill non e' ancora stata validata con confronto numerico vs casi reali pubblicati**; i test interni coprono solo la consistenza delle formule. La skill non produce relazioni di calcolo pronte al deposito e non firma elaborati. Per geometrie non correnti, edifici sensibili al vento o coperture con accumulo, **la skill rinvia ai paragrafi NTC pertinenti e richiede l'input del progettista**.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Calcolo pressione vento**: l'utente chiede "calcolami la pressione del vento", "qual e' p per il mio sito?", "che q_r ho per zona X a 600 m s.l.m.?", "tabulami c_e a varie quote" -> leggi [`tasks/calcola-vento.md`](tasks/calcola-vento.md)
- **Calcolo carico neve**: l'utente chiede "che neve ho a quota Y?", "calcolami q_s su copertura a 25 deg, zona II", "qual e' mu_1 per la mia falda?" -> leggi [`tasks/calcola-neve.md`](tasks/calcola-neve.md)

Se la richiesta e' generica ("aiutami con vento e neve NTC"), chiedi all'utente quale dei due calcoli serve per primo. I due calcoli sono indipendenti: la skill non genera la matrice di combinazione, che e' coperta dalla skill `combinazioni-carico-ntc`.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule NTC par. 3.3 e par. 3.4 sono implementate nel modulo Python [`tasks/lib/carichi_atmosferici.py`](tasks/lib/carichi_atmosferici.py). La test suite [`tasks/lib/test_carichi_atmosferici.py`](tasks/lib/test_carichi_atmosferici.py) copre **solo consistenza interna**: raccordo della velocita' di riferimento al passaggio a_s = a_0, raccordo del coefficiente di forma mu_1 a 30 e 60 gradi, clamp di c_e per z < z_min, monotonia di c_e in z e di c_r in T_R, copertura delle 5 categorie di esposizione e delle 4 zone di neve, validazione input non finiti / fuori dominio, errori CLI con campo mancante o zona invalida. **Non** confronta vs casi reali pubblicati: la validazione di campo e' prerequisito del release stabile.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni calcolo numerico (v_b, c_r, q_r, c_e, p; q_sk, mu_1, c_E, q_s) **devi invocare il modulo Python via Bash**. NON riprodurre i numeri "a mano" leggendo le formule dagli estratti in `references/estratti/`: gli estratti sono materiale di citazione normativa, non sostituiscono l'esecuzione del modulo. Calcolare a mano vanifica la ragion d'essere code-driven della skill (output deterministico e riproducibile, confrontabile dal progettista) e introduce errore stocastico.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill. Usala in tutti i comandi Bash:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/carichi_atmosferici.py vento --input-json input.json
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/carichi_atmosferici.py neve  --input-json input.json
```

In Codex e altri agent compatibili AGENTS.md, se la variabile non e' risolta, sostituiscila con il path assoluto della directory che contiene **questo** `SKILL.md`. Non usare path relativi: la CWD dell'utente quasi mai coincide con la skill dir.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' richiesta (vento o neve).
2. Carica il task file specifico in `tasks/`.
3. Acquisisci dall'utente i dati del sito (zona, altitudine, esposizione) e della struttura (quota di riferimento z, c_p o alpha della falda, c_d, c_t).
4. Esegui il calcolo invocando il sotto-comando corretto del modulo, con citazione esplicita della formula NTC.
5. Produci output strutturato: input riportati, valori intermedi tabulati, output finale in N/m^2 e kN/m^2 (vento) o kN/m^2 (neve), riferimenti normativi.
6. Concludi con rinvio al progettista: la pressione del vento e il carico neve sono valori caratteristici da combinare con altri carichi; la combinazione SLU/SLE va eseguita a valle (vedi skill `combinazioni-carico-ntc`).

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM 17/01/2018 (NTC 2018) - in particolare par. 3.3 (vento), par. 3.4 (neve), Tab. 3.3.I (zone vento), Tab. 3.3.II (categorie esposizione), Tab. 3.4.I (c_E neve)
- Circolare MIT n. 7 del 21/01/2019 - par. C3.3 e C3.4 con commento applicativo

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non incorpora la mappa nazionale zone vento (Tab. 3.3.I): l'utente deve fornire v_b_0, a_0, k_s per la zona del sito
- Non assegna automaticamente la categoria di esposizione I-V: NTC Tab. 3.3.III dipende da rugosita', distanza dalla costa, altitudine. L'utente deve dichiararla
- Non calcola c_p (vento) ne mu_2 / mu_3 (neve): la skill richiede c_p come input e copre solo mu_1 per copertura ad una/due falde
- Non calcola coefficiente dinamico c_d per strutture sensibili: NTC par. 3.3.9 e Circolare C3.3, fuori scope. Usa c_d = 1 (default) solo per costruzioni di tipologia ricorrente
- Non gestisce a_s > 1500 m (vento) ne T_R < 5 / > 500 anni: il modulo solleva ValueError
- Non valuta accumuli neve, deriva, scorrimento (NTC par. 3.4.5.5)
- Non sostituisce la firma del progettista strutturale sulle relazioni di calcolo

**Ogni output va verificato dal progettista strutturale prima di essere usato per analisi di calcolo, dimensionamento o asseverazione.**
