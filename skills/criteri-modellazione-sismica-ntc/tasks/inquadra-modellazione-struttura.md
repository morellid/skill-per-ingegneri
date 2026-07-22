# Task: inquadra-modellazione-struttura

Inquadra i **criteri di modellazione della struttura** ai fini della progettazione sismica secondo le **NTC 2018
par. 7.2.6**. Supporto documentale: **non** costruisce il modello ne' esegue l'analisi.

## Quando usarla

Il progettista deve impostare il modello di calcolo (dimensione, rigidezze, orizzontamenti, elementi non
strutturali). Per la modellazione dell'azione sismica (spettri/storie, eccentricità accidentale, ITS) usa
`inquadra-modellazione-azione-sismica`.

## Passi

1. **Modello tridimensionale** (§7.2.6): il modello deve essere **3D** e rappresentare le effettive distribuzioni
   spaziali di **massa, rigidezza e resistenza**, con attenzione alle situazioni in cui le componenti orizzontali
   dell'azione sismica producono **forze d'inerzia verticali** (travi di grande luce, sbalzi significativi).
2. **Leggi costitutive** (§7.2.6): per comportamento **non dissipativo** o **dissipativo con q**, si usano **leggi
   costitutive elastiche**; per comportamento dissipativo con capacita' dissipativa esplicita, il legame
   costitutivo (non linearità di materiale) va **giustificato**. Delle **non linearità geometriche**, se
   significative, si tiene conto in entrambi i casi.
3. **Rigidezza fessurata** (§7.2.6): nel rappresentare la rigidezza si deve **tener conto della fessurazione**. In
   assenza di analisi specifiche, la rigidezza **flessionale e a taglio** di elementi in **muratura, calcestruzzo
   armato, acciaio-calcestruzzo** puo' essere **ridotta sino al 50%** di quella dei corrispondenti elementi **non
   fessurati** (tenendo conto dello stato limite e della sollecitazione assiale permanente).
4. **Orizzontamenti infinitamente rigidi** (§7.2.6): a meno di specifiche valutazioni e purche' le aperture non ne
   riducano significativamente la rigidezza, gli orizzontamenti piani possono essere considerati **infinitamente
   rigidi nel loro piano medio** se realizzati in **calcestruzzo armato**, oppure in **latero-cemento con soletta
   c.a. di almeno 40 mm**, o in **struttura mista con soletta c.a. di almeno 50 mm** collegata agli elementi in
   acciaio o legno da connettori a taglio dimensionati.
5. **Elementi non strutturali** (§7.2.6): gli elementi non appositamente progettati come collaboranti (tamponature
   e tramezzi) possono essere rappresentati **unicamente in termini di massa**; il loro contributo in rigidezza e
   resistenza si considera **solo qualora abbia effetti negativi** ai fini della sicurezza.

Usa la checklist in `../references/estratti/modellazione-checklist.md` (sezione 1).

## Output atteso

Un inquadramento che indichi: la natura 3D del modello, le leggi costitutive, la riduzione della rigidezza per
fessurazione (sino al 50%), le condizioni per considerare gli orizzontamenti rigidi (40/50 mm) e il trattamento
degli elementi non strutturali (solo massa), con **rinvio al paragrafo** NTC. Nessuna costruzione del modello.

## Cosa NON fare

- Non costruire il modello ne' eseguire l'analisi; non determinare q.
- Non trattare la modellazione dell'**azione sismica** (usa l'altro task) ne' la **risposta sismica locale**
  (§3.2.3.6).
