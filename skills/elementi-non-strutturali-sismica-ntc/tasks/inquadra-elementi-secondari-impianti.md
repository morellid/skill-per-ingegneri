# Task: inquadra-elementi-secondari-impianti

Inquadra i criteri per gli **elementi strutturali secondari** (§7.2.3) e per gli **impianti** (§7.2.4) in zona
sismica secondo le **NTC 2018**. Supporto documentale: **non** esegue le verifiche.

## Quando usarla

Il progettista deve classificare elementi strutturali come secondari o impostare la progettazione antisismica
degli impianti. Per la forza Fa sugli elementi costruttivi non strutturali usa
`inquadra-forza-elementi-non-strutturali`.

## Passi

### Elementi strutturali secondari (§7.2.3)

1. **Trattamento nell'analisi**: nell'analisi della risposta sismica la **rigidezza e la resistenza alle azioni
   orizzontali** degli elementi secondari possono essere **trascurate**.
2. **Progettazione**: gli elementi secondari e i loro collegamenti sono progettati per resistere ai **soli
   carichi verticali** e per **seguire gli spostamenti** della struttura senza perdere capacita' portante,
   valutati per la piu' sfavorevole condizione sismica allo **SLC** (§7.3.3.3 lineare / §7.3.4 non lineare).
3. **Limiti alla scelta**: la scelta degli elementi da considerare secondari **non** puo' trasformare una
   struttura **irregolare** in **regolare** (§7.2.1), ne' il loro **contributo totale** a rigidezza e resistenza
   sotto azioni orizzontali puo' **superare il 15%** dell'analogo contributo degli elementi primari.

### Impianti (§7.2.4)

4. **Principio di verifica**: la **capacita'** dei componenti dell'impianto (e degli elementi che li sostengono e
   collegano) deve essere **maggiore della domanda sismica** per ogni SL (§7.3.6).
5. **Responsabilita'**: della progettazione antisismica **dell'impianto** e' responsabile il **produttore**;
   degli **elementi di alimentazione e collegamento**, l'**installatore**; degli **orizzontamenti, tamponature e
   tramezzi** a cui si ancorano gli impianti, il **progettista strutturale**. Il progettista della struttura
   individua la domanda; fornitore/installatore forniscono impianti e collegamenti di capacita' adeguata.
6. **Soglie per lo studio specifico**: richiedono uno **specifico studio** (fuori dalle prescrizioni del §7.2.4)
   gli impianti che eccedano il **30% del carico permanente totale del campo di solaio** su cui sono collocati (o
   del pannello di tamponatura/tramezzatura a cui sono appesi) o il **10% del carico permanente totale dell'intera
   struttura**.

Usa la checklist in `../references/estratti/elementi-non-strutturali-checklist.md` (sezioni 1 e 3).

## Output atteso

Un inquadramento che indichi: per gli elementi secondari il trattamento nell'analisi, i criteri di progettazione
allo SLC e il limite del 15%; per gli impianti il principio capacita' > domanda, la ripartizione delle
responsabilita' e le soglie del 30%/10% per lo studio specifico, con **rinvio ai paragrafi** NTC. Nessuna verifica.

## Cosa NON fare

- Non eseguire le verifiche ne' calcolare il contributo di rigidezza/resistenza o i carichi permanenti al posto
  del progettista.
- Non trattare la forza Fa sugli elementi costruttivi non strutturali (usa l'altro task) ne' i metodi di analisi
  (§7.3).
