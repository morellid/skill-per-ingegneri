# Task: inquadra-limiti-spostamento-interpiano

Inquadra i **limiti di spostamento di interpiano** per la verifica di rigidezza (RIG) allo stato limite di danno
secondo le **NTC 2018 par. 7.3.6.1**. Supporto documentale: **non** calcola gli spostamenti ne' esegue l'analisi.

## Quando usarla

Il progettista deve individuare il limite di spostamento di interpiano applicabile in funzione del tipo di
tamponatura/struttura. Per la scelta dello stato limite e della classe d'uso e le regole di applicazione usa
`inquadra-classe-uso-stato-limite`.

## Passi

1. **Grandezze in gioco** (§7.3.6.1): la verifica confronta **q*dr** con un limite espresso come frazione
   dell'altezza di piano **h**, dove:
   - **dr** = spostamento di interpiano = differenza tra gli spostamenti del **solaio superiore** e del **solaio
     inferiore**, calcolati con analisi lineare (§7.3.3.3) o non lineare (§7.3.4), sul **modello di calcolo non
     comprensivo delle tamponature**;
   - **q** = fattore di comportamento; **h** = altezza del piano.
2. **Individua il tipo** di tamponatura o struttura portante e applica il limite corrispondente (per CU I e II,
   allo SLD):
   - **(a) tamponature collegate rigidamente** alla struttura, che interferiscono con la sua deformabilita':
     - **fragili**: q*dr **<=** 0,0050 h  [7.3.11a];
     - **duttili**: q*dr **<=** 0,0075 h  [7.3.11b];
   - **(b) tamponature progettate per non subire danni** (deformabilita' intrinseca o collegamenti):
     - q*dr **<=** drp **<=** 0,0100 h  [7.3.12];
   - **(c) muratura ordinaria**: q*dr **<=** 0,0020 h  [7.3.13];
   - **(d) muratura armata**: q*dr **<=** 0,0030 h  [7.3.14];
   - **(e) muratura confinata**: q*dr **<** 0,0025 h  [7.3.15].
3. **Attenzione all'operatore**: i casi a-d usano **<=** (minore o uguale); il caso e (muratura confinata) usa
   **<** (strettamente minore).
4. Ricorda che, per le CU III e IV (SLO), i limiti si **riducono ai 2/3** e che, in caso di coesistenza di tipi
   diversi nel medesimo piano, si assume il limite **piu' restrittivo** (vedi `inquadra-classe-uso-stato-limite`).

Usa la checklist in `../references/estratti/spostamenti-interpiano-checklist.md` (sezioni 2-3).

## Output atteso

Un inquadramento che, per il tipo di tamponatura/struttura in esame, indichi il limite applicabile (formula
[7.3.11a]-[7.3.15]), l'operatore corretto (<= o <), la definizione di dr (su modello senza tamponature) e di h,
con **rinvio ai paragrafi/formule** NTC. Nessun calcolo di spostamenti.

## Cosa NON fare

- Non calcolare gli spostamenti di interpiano ne' eseguire l'analisi (rinvio §7.3.3.3/§7.3.4); non determinare q.
- Non trattare le verifiche di **resistenza (RES)** o **duttilita' (DUT)** degli elementi strutturali, ne' quelle
  di **elementi non strutturali** (§7.3.6.2) e **impianti** (§7.3.6.3).
