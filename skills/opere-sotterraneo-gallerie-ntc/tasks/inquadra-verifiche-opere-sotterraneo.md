# Task: inquadra-verifiche-opere-sotterraneo

Inquadra le **analisi progettuali e le verifiche di sicurezza** di un'opera in sotterraneo (galleria, caverna,
pozzo) secondo le **NTC 2018 par. 6.7.5**. Supporto documentale: **non** calcola le verifiche ne' dimensiona
l'opera o i rivestimenti.

## Quando usarla

Il progettista deve impostare gli stati limite e le combinazioni da verificare per un'opera in sotterraneo. Per
la caratterizzazione, i criteri di progetto e il monitoraggio (par. 6.7.1-6.7.4, 6.7.6) usa
`inquadra-caratterizzazione-progetto-monitoraggio`.

## Passi

1. **Fasi e stati limite**: riferisci le analisi alle **diverse fasi di scavo e costruzione** e alle
   **condizioni di esercizio**; verifica agli **stati limite ultimi (SLU)** e agli **stati limite di esercizio
   (SLE)**.
2. **Stati limite ultimi da considerare** (§6.7.5):
   - **GEO** - raggiungimento della resistenza del terreno o dell'ammasso roccioso interessato dallo scavo;
   - **STR** - raggiungimento della resistenza degli elementi strutturali di stabilizzazione e di rivestimento
     (prima fase e definitivi);
   - **UPL** - spinte idrauliche al fronte e al contorno dello scavo in fase di avanzamento;
   - **HYD** - elevati gradienti idraulici, con attraversamento di terreni suscettibili al sifonamento.
   Valuta inoltre quantitativamente gli **effetti indotti sui manufatti e sulle costruzioni esistenti**.
3. **Stabilita' di versanti e imbocchi**: le verifiche di stabilita' globale dei versanti con cui l'opera
   interagisce e dei **fronti di scavo agli imbocchi** si eseguono con i criteri dei **§6.3** (pendii naturali)
   e **§6.8** (fronti di scavo).
4. **Approccio e combinazioni**: le verifiche SLU si eseguono con l'**Approccio 1**, considerando **entrambe** le
   combinazioni:
   - **Combinazione 1: (A1+M1+R1)**;
   - **Combinazione 2: (A2+M2+R2)**;
   con i coefficienti parziali delle **Tab. 6.2.I** (azioni) e **6.2.II** (parametri geotecnici) e con i
   coefficienti **gamma_R dei gruppi R1 e R2 pari all'unita' (1,0)**.
5. **Verifiche strutturali e idrauliche**: le verifiche strutturali degli elementi di rinforzo (in avanzamento
   dal fronte e sulle pareti) e delle strutture di rivestimento si eseguono come al **§6.2.4.1.3**, usando i
   **valori caratteristici** dei parametri geotecnici; le verifiche idrauliche seguono il **§6.2.4.2**.
6. **Metodo osservazionale** (§6.2.5): se adottato, le analisi devono permettere previsioni sulle grandezze
   rappresentative del comportamento della cavita' - **convergenza radiale**, **deformazione longitudinale del
   fronte** e, se pertinenti, **spostamenti di superficie** - da confrontare con i valori misurati.

Usa la checklist in `../references/estratti/opere-sotterraneo-checklist.md` (sezione 6).

## Output atteso

Un inquadramento che elenchi: gli stati limite da verificare (GEO, STR, UPL, HYD + effetti su manufatti
esistenti), l'approccio e le due combinazioni (Approccio 1: Comb 1 A1+M1+R1 e Comb 2 A2+M2+R2, gamma_R = 1,0 per
R1/R2), i rinvii per verifiche strutturali (§6.2.4.1.3) e idrauliche (§6.2.4.2), e le grandezze del metodo
osservazionale, con **rinvio ai paragrafi** NTC. Nessun calcolo o dimensionamento.

## Cosa NON fare

- Non calcolare le verifiche ne' dimensionare i rivestimenti o gli interventi di stabilizzazione.
- Non definire il modello geotecnico ne' scegliere i parametri al posto del progettista.
- Non trattare la **sicurezza dei lavoratori** in sotterraneo, le macchine di scavo (TBM) come prodotti ne' la
  progettazione sismica (Cap. 7).
