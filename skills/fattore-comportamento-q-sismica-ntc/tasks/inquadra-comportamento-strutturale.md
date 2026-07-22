# Task: inquadra-comportamento-strutturale

Inquadra la scelta del **comportamento strutturale** (dissipativo o non dissipativo), delle **classi di duttilità**
e della **progettazione in capacità** secondo le **NTC 2018 par. 7.2.2**. Supporto documentale: **non** calcola q
né la domanda.

## Quando usarla

All'impostazione del progetto sismico il progettista deve decidere se progettare a comportamento dissipativo o non
dissipativo e, se dissipativo, la classe di duttilità. Per il fattore di comportamento q usa
`inquadra-fattore-comportamento-q`.

## Passi

1. **Alternativa** (§7.2.2): per le costruzioni non isolate/dissipate si progetta secondo un comportamento
   **a) non dissipativo** oppure **b) dissipativo**.
2. **Non dissipativo** (§7.2.2): tutte le membrature e i collegamenti rimangono in **campo elastico** o
   sostanzialmente elastico; la domanda si calcola con un **modello elastico** (§7.2.6), indipendentemente dalla
   tipologia strutturale e senza non linearità di materiale.
3. **Dissipativo** (§7.2.2): un numero elevato di membrature/collegamenti **evolve in campo plastico**, la restante
   parte resta elastica; la capacità dissipativa è presa in conto **implicitamente attraverso il fattore di
   comportamento q** (§7.3, modello elastico) oppure **esplicitamente** con adeguata legge costitutiva (§7.2.6).
4. **Classi di duttilità** (§7.2.2): una costruzione dissipativa persegue **CD"A"** (Alta, elevata capacità
   dissipativa) o **CD"B"** (Media); differiscono per l'entità delle plasticizzazioni previste, a livello locale e
   globale.
5. **Progettazione in capacità** (§7.2.2): per CD"A" e CD"B" si impiegano i procedimenti della progettazione in
   capacità (nelle costruzioni di muratura dove esplicitamente specificato). Si distinguono elementi/meccanismi
   **duttili e fragili**; si evitano le rotture fragili e i meccanismi globali fragili/instabili; si localizzano le
   dissipazioni nelle zone duttili.
6. **Fattore di sovraresistenza γRd** (§7.2.2): la capacità in resistenza allo **SLV** degli elementi **fragili**
   deve essere **maggiore** di quella dei **duttili** alternativi; la capacità dei duttili si incrementa col
   fattore **γRd**. Ove non esplicitamente specificato, il γRd dei **meccanismi globali fragili** deve essere
   **almeno pari a 1,25**.

Usa la checklist in `../references/estratti/fattore-comportamento-q-checklist.md` (sezione 1).

## Output atteso

Un inquadramento che indichi: la scelta tra comportamento non dissipativo e dissipativo (con il rispettivo
trattamento della domanda), la classe di duttilità CD"A"/CD"B" per il caso dissipativo e i principi della
progettazione in capacità (duttili/fragili, γRd globale ≥ 1,25), con **rinvio ai paragrafi** NTC. Nessun calcolo.

## Cosa NON fare

- Non **calcolare** q né la domanda sismica (usa l'altro task per l'inquadramento di q, e `spettro-risposta-ntc`
  per lo spettro).
- Non decidere al posto del progettista la classe di duttilità o i dettagli della progettazione in capacità dei
  singoli materiali (§7.4-7.9).
