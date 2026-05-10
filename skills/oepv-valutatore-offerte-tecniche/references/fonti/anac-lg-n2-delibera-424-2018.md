# Fonte: ANAC Linea Guida n. 2 - Offerta economicamente piu' vantaggiosa

**Fonte ufficiale**: ANAC - Linee guida n. 2, di attuazione del D.lgs. 18 aprile 2016, n. 50, recanti "Offerta economicamente piu' vantaggiosa"
**Approvazione**: Delibera n. 1005, del 21 settembre 2016; aggiornate con Delibera n. 424 del 2 maggio 2018
**URL**: https://www.anticorruzione.it/documents/91439/221cee7f-adba-5368-6d25-69fd2884aa91
**SHA256**: 719e06f3ec3ce5b36d1f606adaa874377438a83f92fc2e47bf9c6dde7c93d1f8
**Data accesso**: 2026-05-10
**Licenza**: public-domain-italian-law

**Nota di vigenza**: Le Linee guida n. 2 ANAC sono state emanate in attuazione del D.Lgs. 50/2016 (vecchio codice appalti). Con l'entrata in vigore del D.Lgs. 36/2023 (nuovo codice, efficace 1 luglio 2023), le linee guida non sono state formalmente aggiornate ne' ritirate per la materia OEPV. Nella prassi dei disciplinari di gara e nella giurisprudenza TAR/CdS continuano ad essere citate come riferimento metodologico. La metodologia aggregativo-compensatore e le formule descritte rimangono coerenti con le disposizioni del nuovo art. 108 D.Lgs. 36/2023, ma i riferimenti alle norme del D.Lgs. 50/2016 (es. art. 95 co. 10-bis, soglie 36/40.000 EUR, ecc.) non sono piu' vigenti.

Trascrizione verbatim dei paragrafi rilevanti per la skill oepv-valutatore-offerte-tecniche.
Le sezioni trascritte sono: PREMESSA (estratto), Sezione IV (Valutazione elementi quantitativi, formule economica), Sezione V (Valutazione elementi qualitativi, criteri motivazionali), Sezione VI cap. 1 (Metodo aggregativo compensatore).

---

## PREMESSA (estratto)

Al fine di facilitare le stazioni appaltanti e gli operatori economici, ai sensi dell'art. 213, comma 2, del Decreto Legislativo 18 aprile 2016, n. 50 (di seguito Codice), l'Autorita' ha predisposto le presenti linee guida, di natura prevalentemente tecnico-matematica, finalizzate a fornire indicazioni operative per il calcolo dell'OEPV, soprattutto per quanto concerne la scelta del criterio di attribuzione dei punteggi per i diversi elementi qualitativi e quantitativi che compongono l'offerta e la successiva aggregazione dei punteggi. [...] Le linee guida trovano applicazione nelle procedure a evidenza pubblica a cui risultano applicabili, in quanto compatibili con la tipologia e il settore dell'affidamento, le disposizioni contenute nell'art. 95 del Codice. Si raccomanda alle stazioni appaltanti di definire in maniera chiara e precisa il criterio di aggiudicazione nonche' i criteri di valutazione, i metodi e le formule per l'attribuzione dei punteggi e il metodo per la formazione della graduatoria, finalizzati all'individuazione dell'offerta economicamente piu' vantaggiosa; devono, pertanto, essere evitate formulazioni oscure o ambigue, assicurando la trasparenza dell'attivita' e la consapevolezza della partecipazione.

---

## Sezione III - LA PONDERAZIONE (estratto rilevante: riparametrazione)

*(p. 10 del PDF)*

La stazione appaltante procede, se previsto nel bando di gara, alla riparametrazione dei punteggi per riallinearli ai punteggi previsti per l'elemento di partenza. L'operazione di riparametrazione puo' avvenire sia in relazione ai criteri qualitativi sia in relazione ai criteri quantitativi (laddove non siano previste modalita' che consentono di attribuire alla migliore offerta il punteggio massimo) con riferimento ai punteggi relativi ai singoli criteri o, laddove siano previsti, in relazione ai singoli sub-criteri.

La stazione appaltante puo' procedere, altresi', a una seconda riparametrazione dei punteggi ottenuti per la parte tecnica o quella economica, complessivamente considerate. Anche in questo caso condizioni essenziali per procedere alla riparametrazione e' che la stessa sia prevista nel bando di gara e che siano chiaramente individuati gli elementi che concorrono a formare la componente tecnica e la componente economica.

In sostanza, da un punto di vista matematico, quando il coefficiente ovvero il punteggio massimo ottenuto per un determinato criterio dall'offerta migliore non raggiunge il valore 1, si procede alla riparametrazione dividendo il coefficiente di ciascuna offerta per il coefficiente massimo attribuito per quel criterio. Allo stesso modo, e' possibile procedere qualora si faccia riferimento al punteggio ottenuto anziche' al coefficiente.

La riparametrazione risponde ad una scelta discrezionale della stazione appaltante che deve essere espressamente prevista nei documenti di gara ed e' finalizzata a preservare l'equilibrio tra le diverse componenti dell'offerta, in modo che in relazione a tutte le componenti, l'offerta migliore ottenga il massimo punteggio, con conseguente rimodulazione delle altre offerte.

---

## Sezione IV - LA VALUTAZIONE DEGLI ELEMENTI QUANTITATIVI

*(p. 11-13 del PDF)*

Di regola l'offerta e' composta da elementi di natura quantitativa (quali, ad esempio, il prezzo, il tempo di esecuzione dei lavori, il rendimento, la durata della concessione, il livello delle tariffe), da elementi riferiti all'assenza o presenza di una determinata caratteristica (possesso di una certificazione di qualita', del rating di legalita', ecc.) e da elementi di natura qualitativa, sui quali la commissione di gara deve esprimere il proprio giudizio, secondo i criteri prestabiliti nel bando di gara.

Per quanto concerne gli elementi di natura quantitativa, quali il prezzo, di regola nei bandi e' fissato il prezzo massimo che la stazione appaltante intende sostenere (non sono ammesse offerte al rialzo [...]) e i concorrenti propongono sconti rispetto a tale prezzo. Il punteggio minimo, pari a zero, e' attribuito all'offerta che non presenta sconti rispetto al prezzo a base di gara, mentre il punteggio massimo all'offerta che presenta lo sconto maggiore.

Di seguito si riportano modalita' di calcolo dei punteggi economici che rispettano i criteri suddetti, utilizzabili soprattutto quando il criterio di formazione della graduatoria e' quello aggregativo compensatore.

### Formula lineare (interpolazione lineare)

*(p. 11 del PDF)*

Il punteggio attribuito alle offerte puo' essere calcolato tramite un'interpolazione lineare.
In simboli:

```
V_ai = R_a / R_max
```

dove:
- V_ai = Coefficiente della prestazione dell'offerta (a) rispetto al requisito (i), variabile tra 0 e 1
- R_a = Valore (ribasso) offerto dal concorrente a
- R_max = Valore (ribasso) dell'offerta piu' conveniente

Quando il concorrente a non effettua alcuno sconto, R_a assume il valore 0, cosi' come il coefficiente V_ai; mentre per il concorrente che offre il maggiore sconto V_ai assume il valore 1. Tale coefficiente andra' poi moltiplicato per il punteggio massimo attribuibile.

Tale metodo di calcolo presenta l'inconveniente, piu' volte evidenziato, di poter condurre a differenze elevate anche a fronte di scarti in valore assoluto limitati; cio' si verifica quando il ribasso massimo rispetto al prezzo a base di gara e' contenuto; accentua inoltre la concorrenza, inducendo a formulare offerte aggressive.

### Formula bilineare con valore soglia

*(p. 11-12 del PDF)*

In alternativa al metodo dell'interpolazione lineare, specie per l'elemento prezzo, si puo' utilizzare il metodo cosiddetto bilineare, secondo il quale il punteggio cresce linearmente fino a un valore soglia, calcolato ad esempio come la media del ribasso dei concorrenti, per poi flettere e crescere a un ritmo molto limitato.

Dal punto di vista matematico la formula si presenta nel seguente modo:

```
C_i (per A_i <= A_soglia) = X * A_i / A_soglia
C_i (per A_i > A_soglia) = X + (1 - X) * [(A_i - A_soglia) / (A_max - A_soglia)]
```

dove:
- C_i = coefficiente attribuito al concorrente i-esimo
- A_i = valore dell'offerta (ribasso) del concorrente i-esimo
- A_soglia = media aritmetica dei valori delle offerte (ribasso sul prezzo) dei concorrenti
- X = 0,80 oppure 0,85 oppure 0,90
- A_max = valore dell'offerta (ribasso) piu' conveniente

### Metodo tabellare (criteri on/off e scala discreta)

*(p. 13 del PDF)*

Per le forniture e per taluni servizi, ovvero quando non e' necessario esprimere una valutazione di natura soggettiva, e' possibile attribuire il punteggio anche sulla base tabellare o del punteggio assoluto. In questo caso, sara' la presenza o assenza di una data qualita' e l'entita' della presenza, che concorreranno a determinare il punteggio assegnato a ciascun concorrente per un determinato parametro. Anche in questo caso si attribuisce il punteggio 0 al concorrente che non presenta il requisito richiesto e un punteggio crescente (predeterminato) al concorrente che presenta il requisito richiesto con intensita' maggiore. Ad esempio, se per il rating di legalita' sono previsti fino a tre punti, e' attribuito il punteggio 0 a chi non ha il rating, il punteggio 1 a chi lo ha con una stella, 2 a chi ha due stelle e 3 a chi ha tre stelle.

---

## Sezione V - LA VALUTAZIONE DEGLI ELEMENTI QUALITATIVI: I CRITERI MOTIVAZIONALI

*(p. 14-16 del PDF)*

Gli elementi di valutazione cosiddetti qualitativi richiedono una valutazione discrezionale da parte dei commissari di gara. Al fine di permettere ai concorrenti di presentare una proposta consapevole e alla commissione di gara di esprimere una valutazione delle offerte coerente con gli obiettivi della stazione appaltante [...] e' assolutamente necessario che vengano indicati - gia' nel bando o in qualsiasi altro atto di avvio della procedura di affidamento - i criteri motivazionali a cui deve attenersi la commissione per la valutazione delle offerte. Tali criteri devono essere almeno non discriminatori [...], conosciuti da tutti i concorrenti e basati su elementi accessibili alle imprese.

La stazione appaltante resta libera di determinare il criterio di attribuzione dei punteggi per i criteri di natura qualitativa [...], tuttavia nella prassi applicativa si ricorre a due gruppi di sistemi alternativi:
a) l'attribuzione discrezionale di un coefficiente (da moltiplicare poi per il punteggio massimo attribuibile in relazione al criterio), variabile tra zero e uno, da parte di ciascun commissario di gara;
b) il confronto a coppie tra le offerte presentate, da parte di ciascun commissario di gara.

### Attribuzione discrezionale del coefficiente (metodo a)

*(p. 14-15 del PDF)*

Sulla base del primo criterio, ciascun commissario attribuisce un punteggio a ciascuna offerta. Le ragioni di tale attribuzione devono essere adeguatamente motivate e la motivazione deve essere collegata ai criteri presenti nel bando.

In relazione a ciascun criterio o subcriterio di valutazione la stazione appaltante deve indicare gli specifici profili oggetto di valutazione, in maniera analitica e concreta. Con riferimento a ciascun criterio o subcriterio devono essere indicati i relativi descrittori che consentono di definire i livelli qualitativi attesi e di correlare agli stessi un determinato punteggio, assicurando la trasparenza e la coerenza delle valutazioni.

Una volta che ciascun commissario ha attribuito il coefficiente a ciascun concorrente, viene calcolata la media dei coefficienti attribuiti, viene attribuito il valore 1 al coefficiente piu' elevato e vengono di conseguenza riparametrati tutti gli altri coefficienti.

---

## Sezione VI, cap. 1 - IL METODO AGGREGATIVO COMPENSATORE

*(p. 17 del PDF)*

Il metodo aggregativo compensatore, semplice e intuitivo, e' il piu' utilizzato dalle stazioni appaltanti; si basa sulla sommatoria dei coefficienti attribuiti per ciascun criterio, ponderati per il peso relativo del criterio. A ciascun candidato il punteggio viene assegnato sulla base della seguente formula:

```
P_i = sommatoria [ W_i * V_ai ]
```

dove:
- P_i = Punteggio dell'offerta i-esima
- n = numero totale dei requisiti
- W_i = peso o punteggio attribuito al requisito (i)
- V_ai = coefficiente della prestazione dell'offerta (a) rispetto al requisito (i) variabile tra zero ed uno

Il metodo aggregativo compensatore presenta l'inconveniente di compensare i punteggi attribuiti ai diversi elementi e di colmare, nell'ambito del punteggio finale, eventuali profili carenti dell'offerta con quelli piu' completi.
