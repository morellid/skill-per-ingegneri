# Task: inquadra-forza-elementi-non-strutturali

Inquadra la **verifica sismica degli elementi costruttivi non strutturali** e la **forza orizzontale Fa** secondo
le **NTC 2018 par. 7.2.3**. Supporto documentale: **non** calcola Fa ne' esegue le verifiche.

## Quando usarla

Il progettista deve verificare un elemento non strutturale (tamponatura, controsoffitto, parapetto, camino,
rivestimento) rispetto all'azione sismica. Per gli elementi strutturali secondari e gli impianti (par. 7.2.3
elementi secondari, 7.2.4) usa `inquadra-elementi-secondari-impianti`.

## Passi

1. **Definizione** (§7.2.3): sono elementi costruttivi non strutturali quelli con rigidezza, resistenza e massa
   tali da influenzare significativamente la risposta strutturale, o quelli significativi per la **sicurezza/
   incolumita' delle persone**.
2. **Principio di verifica** (§7.2.3): la **capacita'** dell'elemento (e degli elementi che lo sostengono e
   collegano alla struttura principale) deve essere **maggiore della domanda sismica** corrispondente a ciascuno
   stato limite (§7.3.6).
3. **Responsabilita'** (§7.2.3): per l'elemento **costruito in cantiere**, il progettista della struttura
   individua la domanda e progetta la capacita' (con formulazioni di comprovata validita'), il direttore dei
   lavori verifica l'esecuzione; per l'elemento **assemblato in cantiere**, il progettista individua la domanda,
   il fornitore/installatore fornisce elementi e collegamenti di capacita' adeguata, il DL verifica
   l'assemblaggio.
4. **Irregolarita' della distribuzione** (§7.2.3): se la distribuzione degli elementi non strutturali e'
   fortemente **irregolare in pianta**, si tiene conto degli effetti incrementando **di un fattore 2
   l'eccentricita' accidentale** (§7.2.6); se fortemente **irregolare in altezza**, si incrementa **di un fattore
   1,4 la domanda sismica sugli elementi verticali** (pilastri e pareti) dei livelli con significativa riduzione
   degli elementi non strutturali.
5. **Forza orizzontale Fa** (§7.2.3): la domanda sismica sull'elemento non strutturale puo' essere determinata
   applicando la forza orizzontale:

       Fa = (Sa x Wa) / qa    [7.2.1]

   dove **Fa** e' la forza nel centro di massa (direzione piu' sfavorevole), **Sa** l'accelerazione massima
   adimensionalizzata rispetto a g che l'elemento subisce (stato limite in esame, §3.2.1), **Wa** il peso
   dell'elemento e **qa** il fattore di comportamento dell'elemento. In assenza di specifiche determinazioni, per
   **Sa** e **qa** ci si riferisce a documenti di comprovata validita'.

Usa la checklist in `../references/estratti/elementi-non-strutturali-checklist.md` (sezione 2).

## Output atteso

Un inquadramento che indichi: la definizione, il principio capacita' > domanda, la ripartizione delle
responsabilita', gli incrementi per irregolarita' (fattore 2 in pianta, 1,4 in altezza) e la formula **Fa = (Sa x
Wa) / qa** con il significato dei termini, con **rinvio ai paragrafi/formula** NTC. Nessun calcolo di Fa.

## Cosa NON fare

- Non calcolare **Fa** ne' eseguire le verifiche; non determinare **Sa** e **qa** (documenti di comprovata
  validita').
- Non calcolare gli spostamenti/domanda (§7.3.3.3/§7.3.4/§7.3.6) ne' lo spettro (§3.2) al posto del progettista.
