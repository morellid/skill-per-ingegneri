# Estratto: ANAC Linea Guida n. 2 - Metodologia valutazione OEPV

**Fonte**: ANAC Delibera n. 1005 del 21 settembre 2016 / aggiornata con Delibera n. 424 del 2 maggio 2018
**Titolo**: "Linee guida n. 2 - Offerta economicamente piu' vantaggiosa"
**URL**: https://www.anticorruzione.it/documents/91439/221cee7f-adba-5368-6d25-69fd2884aa91
**Testo di riferimento**: `references/fonti/anac-lg-n2-delibera-424-2018.md`
**SHA256 PDF**: 719e06f3ec3ce5b36d1f606adaa874377438a83f92fc2e47bf9c6dde7c93d1f8
**Vigenza normativa**: vincolante sotto D.Lgs. 50/2016; sotto D.Lgs. 36/2023 non e' stata aggiornata ne' ritirata. Usare come riferimento metodologico di prassi (non come norma vincolante). In caso di contrasto con l'art. 108 D.Lgs. 36/2023, il decreto prevale.

---

## Metodo aggregativo-compensatore (Sezione VI, cap. 1, p. 17 del PDF)

Il metodo aggregativo compensatore, semplice e intuitivo, e' il piu' utilizzato dalle stazioni appaltanti; si basa sulla sommatoria dei coefficienti attribuiti per ciascun criterio, ponderati per il peso relativo del criterio. A ciascun candidato il punteggio viene assegnato sulla base della seguente formula:

```
P_i = sommatoria [ W_i * V_ai ]
```

dove:
- P_i = Punteggio dell'offerta i-esima
- n = numero totale dei requisiti
- W_i = peso o punteggio attribuito al requisito (i)
- V_ai = coefficiente della prestazione dell'offerta (a) rispetto al requisito (i) variabile tra zero ed uno

---

## Metodi di attribuzione del coefficiente V_ai

### Metodo tabellare (on/off o scala discreta) (Sezione IV, p. 13 del PDF)

Per le forniture e per taluni servizi, ovvero quando non e' necessario esprimere una valutazione di natura soggettiva, e' possibile attribuire il punteggio anche sulla base tabellare o del punteggio assoluto. Si attribuisce il punteggio 0 al concorrente che non presenta il requisito richiesto e un punteggio crescente (predeterminato) al concorrente che presenta il requisito richiesto con intensita' maggiore.

**Esempio dal PDF**: se per il rating di legalita' sono previsti fino a tre punti, e' attribuito il punteggio 0 a chi non ha il rating, il punteggio 1 a chi lo ha con una stella, 2 a chi ha due stelle e 3 a chi ha tre stelle.

### Metodo discrezionale con coefficiente variabile (Sezione V, p. 14-15 del PDF)

Ciascun commissario attribuisce un coefficiente (da moltiplicare poi per il punteggio massimo attribuibile in relazione al criterio), variabile tra zero e uno. Le ragioni di tale attribuzione devono essere adeguatamente motivate e la motivazione deve essere collegata ai criteri presenti nel bando.

In relazione a ciascun criterio o subcriterio di valutazione la stazione appaltante deve indicare gli specifici profili oggetto di valutazione, in maniera analitica e concreta, con i relativi descrittori che consentono di definire i livelli qualitativi attesi.

**Procedura di calcolo**: Una volta che ciascun commissario ha attribuito il coefficiente a ciascun concorrente, viene calcolata la media dei coefficienti attribuiti, viene attribuito il valore 1 al coefficiente piu' elevato e vengono di conseguenza riparametrati tutti gli altri coefficienti. (Sezione V, p. 15 del PDF)

**Nota di procedura**: Il metodo del confronto a coppie e' un'alternativa al metodo del coefficiente discrezionale (Sezione V, p. 15-16 del PDF).

### Metodo con formula quantitativa per elementi numerici (Sezione IV, p. 11 del PDF)

#### Formula lineare (interpolazione lineare) - formula base

```
V_ai = R_a / R_max
```

dove:
- V_ai = Coefficiente della prestazione dell'offerta (a) rispetto al requisito (i), variabile tra 0 e 1
- R_a = Valore (ribasso) offerto dal concorrente a
- R_max = Valore (ribasso) dell'offerta piu' conveniente

**Nota importante**: La formula e' espressa in termini di **ribasso** (sconto percentuale), non in termini di prezzo assoluto. Il punteggio minimo (zero) e' per l'offerta che non presenta sconti; il massimo per lo sconto maggiore.

Il coefficiente va poi moltiplicato per il punteggio massimo attribuibile al criterio.

#### Formula bilineare con valore soglia (Sezione IV, p. 11-12 del PDF)

```
C_i (per A_i <= A_soglia) = X * A_i / A_soglia
C_i (per A_i > A_soglia) = X + (1 - X) * [(A_i - A_soglia) / (A_max - A_soglia)]
```

dove:
- C_i = coefficiente attribuito al concorrente i-esimo
- A_i = valore dell'offerta (ribasso) del concorrente i-esimo
- A_soglia = media aritmetica dei valori delle offerte (ribasso sul prezzo) dei concorrenti
- X = 0,80 oppure 0,85 oppure 0,90 (da scegliere e dichiarare nel bando)
- A_max = valore dell'offerta (ribasso) piu' conveniente

---

## Riparametrazione (Sezione III, p. 10 del PDF)

La riparametrazione si applica quando il coefficiente (o punteggio) massimo ottenuto per un determinato criterio dall'offerta migliore non raggiunge il valore 1 (o il punteggio massimo previsto). In questo caso:

```
V_riparam = V_i / V_max
```

dove V_max e' il coefficiente massimo attribuito tra tutte le offerte per quel criterio.

**Condizione essenziale**: la riparametrazione deve essere espressamente prevista nei documenti di gara. Se non e' prevista nel bando, la sua applicazione da parte della commissione e' contestabile.

La riparametrazione "e' finalizzata a preservare l'equilibrio tra le diverse componenti dell'offerta, in modo che in relazione a tutte le componenti, l'offerta migliore ottenga il massimo punteggio, con conseguente rimodulazione delle altre offerte." (p. 10 del PDF)

---

## Differenze rispetto alla versione precedente dell'estratto

L'estratto precedente (v0.1.0-alpha) conteneva affermazioni non corrispondenti al testo del PDF ANAC LG n.2:

### 1. Formula per il punteggio economico: espressa in modo impreciso
L'estratto precedente riportava la formula economica come:
```
Pe_i = Vmax x (Prezzo_min / Prezzo_i)
```
Questa formula e' espressa in termini di prezzo assoluto. Il PDF ANAC LG n.2 (Sezione IV, p. 11) esprime la formula in termini di **ribasso** (sconto):
```
V_ai = R_a / R_max
```
dove R_a e' il ribasso offerto e R_max e' il ribasso massimo. Nella pratica le due formulazioni sono equivalenti (un prezzo piu' basso corrisponde a un ribasso piu' alto), ma la formulazione corretta nel documento e' per ribasso. Il punteggio si ottiene moltiplicando il coefficiente per Vmax.

### 2. Procedura di attribuzione coefficienti discrezionali: dettagli di procedura
L'estratto precedente descriveva la procedura di attribuzione individuale e simultanea con riferimento alla "attribuzione individuale simultanea" e al "non consultarsi". Il PDF ANAC LG n.2 (Sezione V, p. 14-15) descrive il metodo in modo piu' generico: ciascun commissario attribuisce, poi si calcola la media, poi si riparametra. La simultaneita' e il divieto di consultazione non sono tematizzati esplicitamente nel PDF ANAC; e' la giurisprudenza TAR/CdS che ha consolidato quel requisito procedurale.

### 3. Formule per parametri crescenti/decrescenti: non presenti nel PDF ANAC LG n.2
L'estratto precedente riportava formule per "parametro crescente" (V = Ra/Ra_max) e "parametro decrescente" (V = Ra_min/Ra_i). Queste formule non compaiono nel PDF ANAC LG n.2 in questa forma. Nel PDF ANAC le formule quantitative sono espresse in termini di ribasso. Le formule per altri parametri quantitativi (tempi, risorse) sono una convenzione di prassi non esplicitamente descritta in questo documento.

### 4. Esempio numerico: costruito ad hoc, non nel PDF
L'estratto precedente conteneva un esempio numerico completo con 3 offerenti. Questo esempio non e' presente nel PDF ANAC LG n.2; era un'elaborazione dell'agent. L'unico esempio nel PDF riguarda il rating di legalita' con punteggio tabellare (p. 13).
