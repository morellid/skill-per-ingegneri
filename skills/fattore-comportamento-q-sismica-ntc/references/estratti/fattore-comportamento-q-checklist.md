# Checklist - Comportamento strutturale e fattore di comportamento q (NTC 2018 par. 7.2.2 e 7.3.1)

> Parafrasi operativa dei par. 7.2.2 e 7.3.1 delle NTC 2018, ancorata alla trascrizione verbatim in
> `../fonti/ntc2018-par-7-2-2-7-3-1.md` (PDF GU S.O. n. 8 alla G.U. n. 42 del 20/02/2018, SHA256 `dda1e397...`).
> Ogni voce rinvia al paragrafo/formula/tabella della fonte. La skill e' un **supporto documentale**: non calcola
> q ne' la domanda sismica, e non riproduce il set completo delle tabelle q0 (par. 7.4-7.9).

## Sezione 1 - Comportamento strutturale (par. 7.2.2)

- [ ] **Scelta** (§7.2.2): per le costruzioni non isolate/dissipate si progetta secondo un comportamento
      **non dissipativo** oppure **dissipativo**.
- [ ] **Non dissipativo** (§7.2.2): tutte le membrature e i collegamenti restano in **campo elastico** o
      sostanzialmente elastico; domanda calcolata con **modello elastico** (§7.2.6), indipendentemente dalla
      tipologia e senza non linearita' di materiale.
- [ ] **Dissipativo** (§7.2.2): un numero elevato di membrature/collegamenti **evolve in campo plastico**; la
      capacita' dissipativa e' presa in conto **implicitamente** tramite il fattore di comportamento **q** (§7.3,
      modello elastico) o **esplicitamente** con adeguata legge costitutiva (§7.2.6).
- [ ] **Classi di duttilita'** (§7.2.2): una costruzione dissipativa persegue **CD"A"** (alta capacita'
      dissipativa) o **CD"B"** (media); differiscono per l'entita' delle plasticizzazioni previste (locali e
      globali).
- [ ] **Progettazione in capacita'** (§7.2.2): distingue elementi/meccanismi **duttili e fragili**; la capacita'
      in resistenza allo **SLV** dei fragili deve essere **maggiore** di quella dei duttili alternativi; la
      capacita' dei duttili si incrementa col **fattore di sovraresistenza γRd** (globale **almeno 1,25** ove non
      specificato).

## Sezione 2 - Fattore di comportamento q (par. 7.3.1)

- [ ] **Uso** (§7.3.1): in analisi lineare la domanda sismica si calcola sullo **spettro di progetto**
      (§3.2.3.4-3.2.3.5) ottenuto assumendo q dai limiti Tab. 7.3.I con base q0 Tab. 7.3.II.
- [ ] **Limite superiore** (§7.3.1): **qlim = q0 · KR** [7.3.1] (operatore verificato sull'immagine).
- [ ] **q0** (§7.3.1, Tab. 7.3.II): valore base allo SLV, dipende da **classe di duttilita'**, **tipologia
      strutturale**, coefficiente **Ω** (§7.9.2.1) e rapporto **αu/α1**; la scelta di q0 va **esplicitamente
      giustificata**. Esempi: c.a. a telaio CD"A" **4,5·αu/α1** / CD"B" **3,0·αu/α1**; acciaio intelaiate CD"A"
      **5,0·αu/α1** / CD"B" **4,0**.
- [ ] **KR** (§7.3.1): **1** per costruzioni **regolari in altezza**, **0,8** per **non regolari in altezza**.
- [ ] **αu/α1** (§7.3.1): regolari in pianta -> valori dei paragrafi successivi; **non regolari in pianta** ->
      **media tra 1,0** e tali valori.
- [ ] **Riduzione kw** (§7.3.1): con pareti in c.a., q0 ridotto tramite **kw** (1,00 per telai/miste equivalenti a
      telai; **(1+α0)/3**, con **0,5 ≤ kw ≤ 1**, per pareti/miste equivalenti a pareti/torsionalmente
      deformabili).
- [ ] **Componente verticale** (§7.3.1): **q = 1,5** per qualunque tipologia e materiale, tranne i **ponti**
      (**q = 1**).
- [ ] **Non dissipativo** (§7.3.1): **1 ≤ qND = (2/3)·qCD"B" ≤ 1,5** [7.3.2] (frazione e disuguaglianze verificate
      sull'immagine).

## Cosa la skill NON fa

- [ ] Non **calcola** q, qlim, qND, kw o αu/α1, ne' la **domanda sismica** / lo **spettro di progetto** (§3.2.3).
- [ ] Non riproduce il **set completo** delle Tab. 7.3.II per ogni tipologia/materiale (§7.4-7.9): riporta valori
      rappresentativi e rinvia alle skill/paragrafi di materiale.
- [ ] Non sostituisce il **progettista** ne' la lettura diretta dei par. 7.2.2-7.3.1 delle NTC 2018.
