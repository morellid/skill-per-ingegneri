# Checklist — Ponti in zona sismica (NTC 2018 §7.9, regole generali)

Estratto operativo ancorato a `../fonti/ntc2018-par-7-9.md` (NTC 2018, DM 17/1/2018, GU n. 42 del 20/2/2018 —
S.O. n. 8). Ogni valore è tratto dal testo del par. 7.9 letto anche sull'immagine delle pagine PDF 269-270.

## 1. Campo di applicazione (§7.9.1)

- [ ] Ponte a **pile e travate**: travate **continue su più pile** o **semplicemente appoggiate**; pile a
      **fusto unico** (sezione generica, piena/cava, mono/multicellulare; anche a portale).
- [ ] Pile a geometria complessa (es. telaio spaziale) → criteri/metodi specifici; tipologie diverse documentate,
      fermi i **q0 di Tab. 7.3.II**.

## 2. Criteri generali di progettazione (§7.9.2)

- [ ] Comportamento **non dissipativo**: capacità secondo il **Cap. 4**; c.a. nessuna sezione oltre la **curvatura
      di prima plasticizzazione** (§7.4.4.1.2); c.a.p./acciaio nessun materiale oltre lo **snervamento**.
- [ ] Comportamento **dissipativo**: meccanismo dissipativo **stabile** con **dissipazione limitata alle pile**;
      comportamento inelastico **flessionale**, **esclusa la rottura per taglio**; impegnare il **maggior numero
      di pile**; zone dissipative **accessibili**.
- [ ] **Pali di fondazione**: sollecitazioni sismiche **divise per 1,5**; per **10 diametri** dalla sommità
      dettagli **CD "B"** (§7.9.6.1).
- [ ] Capacità sezioni c.a. con **confinamento** (§4.1.2.1.2.1) considerando la **perdita dei copriferri** alla
      deformazione ultima del cls **non confinato (0,35%)**.
- [ ] Elementi sempre **elastici** (progettazione in capacità): **impalcato, apparecchi di appoggio, fondazioni,
      spalle**, pile che non scambiano azioni orizzontali con l'impalcato.

## 3. Valori del fattore di comportamento (§7.9.2.1)

- [ ] **Non dissipativo**: **q0 = 1,0** (due componenti orizzontali).
- [ ] **Dissipativo**: q0 max da **Tab. 7.3.II**; **λ(α) = 1 se α ≥ 3**, **λ(α) = (α/3)^0,5 se 3 > α ≥ 1**,
      **α = L/H**.
- [ ] Elementi duttili in **c.a.**: q0 valido solo se **νk = NEd/(Ac·fck) ≤ 0,3**; comunque **νk ≤ 0,6**. Per
      **0,3 < νk < 0,6**: **q0(νk) = q0 − [(νk/0,3) − 1]·(q0 − 1)** [7.9.1].
- [ ] **Regolarità**: ri = q0·MEd,i/MRd,i; **r̃ = rmax/rmin < 2 → KR = 1**; **r̃ ≥ 2 → KR = 2/r̃** [7.9.2],
      comunque **q = q0·KR ≥ 1**. Escludibili le pile con resistenza a taglio ≤ **20%** della resistenza totale /
      n. elementi.
- [ ] Ponti a **geometria irregolare** (obliquità > 45°, raggio ridotto): **q = 1,5**; fino a **3,5** solo con
      **analisi non lineare**.

## 4. Modello e analisi lineare (§7.9.3-7.9.4.1)

- [ ] **Eccentricità accidentale** (§7.2.6): **0,03 volte** la dimensione dell'impalcato ⊥ all'azione sismica.
- [ ] Attenzione ai **moti rigidi** per obliquità **φ > 20°** o **B/L > 2,0**; rigidezza c.a. secondo lo stato di
      **fessurazione**.
- [ ] Metodi lineari: incremento flettente per non linearità geometriche **ΔM = dEd·NEd** [7.9.3].
- [ ] **Analisi statica lineare** ammessa se: a) travate appoggiate, massa efficace pila ≤ **1/5** massa impalcato
      portato; b) direzione longitudinale, massa efficace pile ≤ **1/5** massa impalcato; c) direzione trasversale
      (se b) e simmetria o **eccentricità ≤ 5%** della lunghezza).

## 5. Fuori scope

- [ ] Verifiche di **duttilità/resistenza** delle pile e dei dispositivi, **analisi non lineare** e **dettagli
      costruttivi** (§§ 7.9.4-7.9.6); **carichi da traffico** statici (§§ 5.1.3, 5.2.2, skill dedicate);
      framework del **fattore q** per edifici (§ 7.3.1, skill dedicata).
