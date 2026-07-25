# Task — Imposta l'analisi non lineare dinamica o statica/pushover (NTC 2018 §7.3.4)

Supporto documentale per impostare l'**analisi non lineare** — **dinamica** (integrazione al passo) o **statica**
(**pushover**) — secondo le NTC 2018 (DM 17/1/2018), §7.3.4. **Non** esegue l'analisi né le verifiche.

Fonte: `../references/fonti/ntc2018-par-7-3-2-7-3-4.md`; checklist: `../references/estratti/metodi-analisi-checklist.md`.

## Input tipico

- Scopo dell'analisi (spostamenti, duttilità SLC, valutazione capacità di un esistente, αu/α1, progetto nuovo).
- Direzione dell'azione sismica, periodo fondamentale T1 e TC del sito, partecipazione di massa del modo fondamentale.

## Passi

1. **Quando usare l'analisi non lineare (§7.3.4)**
   - Per: valutare gli spostamenti allo SL di interesse; verifiche di duttilità allo SLC; individuare la domanda
     inelastica nelle strutture progettate con q; valutare i rapporti **αu/α1**; come metodo di progetto per gli
     edifici nuovi; per la **valutazione della capacità di edifici esistenti**.

2. **Analisi non lineare dinamica (§7.3.4.1)**
   - Calcolo della risposta mediante **integrazione delle equazioni del moto**, con modello non lineare e **storie
     temporali** del moto del terreno (§3.2.3.6).
   - **Deve essere confrontata con un'analisi modale con spettro** per controllare le differenze nelle sollecitazioni
     globali alla base.
   - Per le costruzioni con **isolamento alla base** è **obbligatoria** se il sistema non è rappresentabile con un
     modello lineare equivalente (§7.10.5.2).

3. **Analisi non lineare statica / pushover (§7.3.4.2)**
   - Associa al sistema reale un **sistema strutturale equivalente non lineare**; applica i carichi gravitazionali e,
     per la direzione considerata, **forze orizzontali** con risultante (taglio alla base) **Fb**, scalate per far
     crescere **monotonamente** (in entrambi i versi, fino al collasso) lo spostamento **dc** di un **punto di
     controllo al centro di massa dell'ultimo livello** (esclusi i torrini; considerare anche punti alternativi se
     rilevante l'accoppiamento traslazioni-rotazioni). Il diagramma **Fb–dc** è la **curva di capacità**.
   - Considerare **almeno due distribuzioni di forze**, una del **Gruppo 1** e una del **Gruppo 2**:
     - **Gruppo 1 (principali)**: se il modo fondamentale ha **massa partecipante ≥ 75%** → distribuzione
       proporzionale alle forze statiche (§7.3.3.2) o alla forma del modo fondamentale; in tutti i casi si può usare la
       distribuzione delle forze di piano di un'analisi dinamica lineare con modi **≥ 85%** di massa, **obbligatoria se
       T1 > 1,3·TC**;
     - **Gruppo 2 (secondarie)**: a) **uniforme**; b) **adattiva**; c) **multimodale** con **≥ 6 modi**.

4. **Output**: scheda con tipo di analisi non lineare (dinamica o pushover), scopo, e — per la pushover — le
   distribuzioni scelte (Gruppo 1 + Gruppo 2) con la verifica delle condizioni (≥75%, T1 vs 1,3·TC). Segnala che
   l'esecuzione dell'analisi e le verifiche restano fuori scope.

## Cosa NON fare

- Non **eseguire** l'analisi (time-history o pushover) né tracciare/valutare numericamente la curva di capacità.
- Non definire lo **spettro** o le **storie temporali** (§3.2.3.5/3.2.3.6) né il **q** (§7.3.1): fuori scope.
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-7-3-2-7-3-4.md`.
