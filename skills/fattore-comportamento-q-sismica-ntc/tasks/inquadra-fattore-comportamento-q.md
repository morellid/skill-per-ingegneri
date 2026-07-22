# Task: inquadra-fattore-comportamento-q

Inquadra la determinazione del **fattore di comportamento q** allo SLV secondo le **NTC 2018 par. 7.3.1**.
Supporto documentale: **non** calcola q né la domanda/lo spettro.

## Quando usarla

Scelto il comportamento strutturale (§7.2.2, task `inquadra-comportamento-strutturale`), il progettista deve
determinare il fattore di comportamento q con cui ridurre lo spettro elastico allo spettro di progetto.

## Passi

1. **Uso di q** (§7.3.1): in **analisi lineare** la domanda sismica si calcola sullo **spettro di progetto**
   (§3.2.3.4-3.2.3.5) ottenuto, per ogni stato limite, assumendo per q i limiti della Tab. 7.3.I con i valori base
   q0 della Tab. 7.3.II.
2. **Limite superiore** (§7.3.1): il limite superiore relativo allo **SLV** è

       qlim = q0 · KR                                                  [7.3.1]

   (operatore di moltiplicazione verificato sull'immagine della pagina PDF).
3. **Valore base q0** (§7.3.1, Tab. 7.3.II): dipende dalla **classe di duttilità**, dalla **tipologia
   strutturale**, dal coefficiente **Ω** (§7.9.2.1) e dal rapporto **αu/α1**; la scelta di q0 va **esplicitamente
   giustificata**. Valori rappresentativi: c.a. a telaio/pareti accoppiate/miste CD"A" **4,5·αu/α1**, CD"B"
   **3,0·αu/α1**; acciaio intelaiate/controventi eccentrici CD"A" **5,0·αu/α1**, CD"B" **4,0**. Il set completo è
   nella Tab. 7.3.II e nei §7.4-7.9 (rinvia alle skill di materiale).
4. **Fattore KR** (§7.3.1): dipende dalla **regolarità in altezza** (§7.2.1): **KR = 1** per costruzioni regolari
   in altezza, **KR = 0,8** per non regolari.
5. **Rapporto αu/α1** (§7.3.1): per costruzioni **regolari in pianta**, senza analisi non lineare, si adottano i
   valori dei paragrafi successivi; per **non regolari in pianta** si adotta la **media tra 1,0** e tali valori.
6. **Riduzione kw** (§7.3.1): in presenza di **pareti in c.a.**, q0 va ridotto col fattore **kw** (1,00 per
   strutture a telaio/miste equivalenti a telai; **(1+α0)/3**, con **0,5 ≤ kw ≤ 1**, per pareti/miste equivalenti
   a pareti/torsionalmente deformabili).
7. **Casi particolari** (§7.3.1): per la **componente verticale** dell'azione sismica allo SLV, salvo analisi
   giustificative, **q = 1,5** per qualunque tipologia e materiale, tranne i **ponti** (**q = 1**). Per il
   comportamento **non dissipativo** si adotta **1 ≤ qND = (2/3)·qCD"B" ≤ 1,5** [7.3.2].

Usa la checklist in `../references/estratti/fattore-comportamento-q-checklist.md` (sezione 2).

## Output atteso

Un inquadramento che indichi la formula **qlim = q0·KR** [7.3.1] con il significato dei termini, il ruolo di q0
(Tab. 7.3.II, con valori rappresentativi e rinvio ai §7.4-7.9), di KR (1/0,8), di αu/α1 e di kw, e i casi
particolari (verticale q=1,5, ponti q=1; non dissipativo [7.3.2]), con **rinvio a paragrafi/formule** NTC. Nessun
calcolo di q.

## Cosa NON fare

- Non **calcolare** q, qlim, qND, kw o αu/α1, né lo **spettro di progetto** / la domanda (§3.2.3): rinvia a
  `spettro-risposta-ntc`.
- Non riprodurre il **set completo** delle Tab. 7.3.II per ogni tipologia/materiale: riporta valori
  rappresentativi e rinvia ai §7.4-7.9.
