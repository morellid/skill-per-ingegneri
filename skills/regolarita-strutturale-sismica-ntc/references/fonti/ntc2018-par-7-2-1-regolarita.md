# NTC 2018 - Regolarità strutturale (par. 7.2.1) e conseguenze (par. 7.3.1, 7.3.3.1)

> Trascrizione verbatim dal PDF del Supplemento Ordinario n. 8 alla Gazzetta Ufficiale n. 42 del 20 febbraio
> 2018 (D.M. 17 gennaio 2018 - "Aggiornamento delle Norme tecniche per le costruzioni"), pp. 208 e ss.
> SHA256 del PDF: `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
> Estratto con `pdftotext -layout` (par. 7.2.1 dalla pagina PDF 212-213; richiami dei par. 7.3.1 e 7.3.3.1).

---

## 7.2.1. CARATTERISTICHE GENERALI DELLE COSTRUZIONI

### REGOLARITÀ

Le costruzioni devono avere, quanto più possibile, struttura iperstatica caratterizzata da regolarità in pianta e
in altezza. Se necessario, ciò può essere conseguito suddividendo la struttura, mediante giunti, in unità tra
loro dinamicamente indipendenti.

Per quanto riguarda gli edifici, **una costruzione è regolare in pianta se tutte le seguenti condizioni sono
rispettate**:

a) la distribuzione di masse e rigidezze è approssimativamente simmetrica rispetto a due direzioni ortogonali e
   la forma in pianta è compatta, ossia il contorno di ogni orizzontamento è convesso; il requisito può ritenersi
   soddisfatto, anche in presenza di rientranze in pianta, quando esse non influenzano significativamente la
   rigidezza nel piano dell'orizzontamento e, per ogni rientranza, l'area compresa tra il perimetro
   dell'orizzontamento e la linea convessa circoscritta all'orizzontamento non supera il 5% dell'area
   dell'orizzontamento;
b) il rapporto tra i lati del rettangolo circoscritto alla pianta di ogni orizzontamento è inferiore a 4;
c) ciascun orizzontamento ha una rigidezza nel proprio piano tanto maggiore della corrispondente rigidezza degli
   elementi strutturali verticali da potersi assumere che la sua deformazione in pianta influenzi in modo
   trascurabile la distribuzione delle azioni sismiche tra questi ultimi e ha resistenza sufficiente a garantire
   l'efficacia di tale distribuzione.

Sempre riferendosi agli edifici, **una costruzione è regolare in altezza se tutte le seguenti condizioni sono
rispettate**:

d) tutti i sistemi resistenti alle azioni orizzontali si estendono per tutta l'altezza della costruzione o, se
   sono presenti parti aventi differenti altezze, fino alla sommità della rispettiva parte dell'edificio;
e) massa e rigidezza rimangono costanti o variano gradualmente, senza bruschi cambiamenti, dalla base alla
   sommità della costruzione (le variazioni di massa da un orizzontamento all'altro non superano il 25%, la
   rigidezza non si riduce da un orizzontamento a quello sovrastante più del 30% e non aumenta più del 10%); ai
   fini della rigidezza si possono considerare regolari in altezza strutture dotate di pareti o nuclei in c.a. o
   di pareti e nuclei in muratura di sezione costante sull'altezza o di telai controventati in acciaio, ai quali
   sia affidato almeno il 50% dell'azione sismica alla base;
f) il rapporto tra la capacità e la domanda allo SLV non è significativamente diverso, in termini di resistenza,
   per orizzontamenti successivi (tale rapporto, calcolato per un generico orizzontamento, non deve differire più
   del 30% dall'analogo rapporto calcolato per l'orizzontamento adiacente); può fare eccezione l'ultimo
   orizzontamento di strutture intelaiate di almeno tre orizzontamenti;
g) eventuali restringimenti della sezione orizzontale della costruzione avvengano con continuità da un
   orizzontamento al successivo; oppure avvengano in modo che il rientro di un orizzontamento non superi il 10%
   della dimensione corrispondente all'orizzontamento immediatamente sottostante, né il 30% della dimensione
   corrispondente al primo orizzontamento. Fa eccezione l'ultimo orizzontamento di costruzioni di almeno quattro
   orizzontamenti, per il quale non sono previste limitazioni di restringimento.

Qualora, immediatamente al di sopra della fondazione, sia presente una struttura scatolare rigida, purché
progettata con comportamento non dissipativo, i controlli sulla regolarità in altezza possono essere riferiti
alla sola struttura soprastante la scatolare, a condizione che quest'ultima abbia rigidezza rispetto alle azioni
orizzontali significativamente maggiore di quella della struttura ad essa soprastante. Tale condizione si può
ritenere soddisfatta se gli spostamenti della struttura soprastante la scatolare, valutati su un modello con
incastri al piede, e gli spostamenti della struttura soprastante, valutati tenendo conto anche della
deformabilità della struttura scatolare, sono sostanzialmente coincidenti.

Per i ponti le condizioni di regolarità sono definite nel § 7.9.2.1.

---

## Conseguenze della regolarità

### Fattore di comportamento - par. 7.3.1

> Il limite superiore q_lim del fattore di comportamento relativo allo SLV è calcolato tramite la seguente
> espressione: q_lim = q0 · KR [7.3.1]

dove:

> KR è un fattore che dipende dalle caratteristiche di regolarità in altezza della costruzione, con valore pari
> ad 1 per costruzioni regolari in altezza e pari a 0,8 per costruzioni non regolari in altezza.

(q0 è il valore base del fattore di comportamento allo SLV, i cui massimi valori sono riportati in Tab. 7.3.II in
dipendenza della classe di duttilità, della tipologia strutturale, ecc.)

### Analisi lineare statica - par. 7.3.3.1

> L'analisi lineare statica consiste nell'applicazione di forze statiche equivalenti alle forze d'inerzia indotte
> dall'azione sismica e può essere effettuata per costruzioni che rispettino i requisiti specifici riportati nei
> paragrafi successivi, a condizione che il periodo del modo di vibrare principale nella direzione in esame (T1)
> non superi 2,5 TC o TD e che la costruzione sia regolare in altezza.

---

## Note sulla trascrizione

- **Fonte unica**: PDF ufficiale della Gazzetta Ufficiale (S.O. n. 8 alla G.U. n. 42 del 20/02/2018), la stessa
  usata dalle altre skill NTC del repo (SHA256 `dda1e397...`), con hash riproducibile via doppio download e
  validato live dalla CI del repo su ogni PR.
- **Soglie di regolarità** (§7.2.1) verificate a testo (numeri in chiaro, senza segni matematici a rischio di
  perdita in `pdftotext`): rientranze in pianta ≤ **5%** dell'area; rapporto lati del rettangolo circoscritto
  **< 4**; variazioni di massa ≤ **25%**; rigidezza che non si riduce > **30%** né aumenta > **10%** da un piano
  al sovrastante; rapporto capacità/domanda SLV che non differisce > **30%** tra orizzontamenti adiacenti;
  restringimenti con rientro ≤ **10%** della dimensione sottostante, né > **30%** del primo orizzontamento.
- **Conseguenze**: fattore **KR = 1** (regolare in altezza) / **KR = 0,8** (non regolare in altezza) sul fattore
  di comportamento (§7.3.1); l'**analisi lineare statica** è applicabile solo se **T1 ≤ 2,5 TC o TD** **e** la
  costruzione è **regolare in altezza** (§7.3.3.1). La stima e i limiti di T1 sono trattati dalla skill
  `periodo-proprio-t1-ntc` (§7.3.3.2).
- La regolarità **in pianta** (a-c) e **in altezza** (d-g) sono requisiti distinti: incidono su modello,
  distribuzione delle forze e metodo di analisi.
