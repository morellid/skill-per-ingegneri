# Task: inquadra-classe-uso-stato-limite

Inquadra la **scelta dello stato limite (SLD/SLO) in funzione della classe d'uso** e le **regole di applicazione**
dei limiti di spostamento di interpiano secondo le **NTC 2018 par. 7.3.6 e 7.3.6.1**. Supporto documentale:
**non** calcola gli spostamenti ne' esegue l'analisi.

## Quando usarla

Il progettista deve stabilire a quale stato limite riferire la verifica di rigidezza e come applicare i limiti
(riduzione ai 2/3, coesistenza, estensione delle verifiche). Per i valori numerici dei limiti usa
`inquadra-limiti-spostamento-interpiano`.

## Passi

1. **Quadro delle verifiche** (§7.3.6, Tab. 7.3.III): per gli elementi strutturali primari (ST) la verifica di
   **rigidezza (RIG)** e' richiesta:
   - allo **SLD** per le **CU I e II**;
   - allo **SLO** per le **CU III e IV**.
   (Le verifiche di resistenza RES si riferiscono allo SLV, quelle di duttilita' DUT allo SLC nei casi indicati:
   fuori dall'ambito di questa skill.)
2. **Riduzione ai 2/3 per CU III e IV** (§7.3.6.1): per le CU III e IV, riferite allo SLO, gli spostamenti
   d'interpiano devono essere **inferiori ai 2/3 dei limiti** indicati per lo SLD (es. tamponature fragili:
   2/3 * 0,0050 h; tamponature duttili: 2/3 * 0,0075 h).
3. **Coesistenza** (§7.3.6.1): in caso di coesistenza di **diversi tipi di tamponamento o struttura portante nel
   medesimo piano**, deve essere assunto il **limite di spostamento piu' restrittivo**.
4. **Estensione delle verifiche** (§7.3.6.1): qualora gli spostamenti di interpiano siano **superiori a 0,005 h
   (caso b)**, le **verifiche della capacita' di spostamento** degli elementi non strutturali vanno **estese** a
   tutte le tamponature, alle **tramezzature interne** e agli **impianti**.

Usa la checklist in `../references/estratti/spostamenti-interpiano-checklist.md` (sezioni 1 e 4).

## Output atteso

Un inquadramento che indichi: lo stato limite di riferimento in funzione della classe d'uso (SLD per CU I/II, SLO
con limiti ridotti ai 2/3 per CU III/IV), l'assunzione del limite piu' restrittivo in caso di coesistenza e i
casi in cui le verifiche vanno estese, con **rinvio ai paragrafi** NTC. Nessun calcolo.

## Cosa NON fare

- Non calcolare gli spostamenti ne' eseguire l'analisi; non determinare la classe d'uso al posto del progettista.
- Non trattare le verifiche di resistenza (RES) o duttilita' (DUT), ne' quelle di elementi non strutturali
  (§7.3.6.2) e impianti (§7.3.6.3).
