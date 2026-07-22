---
name: fattore-comportamento-q-sismica-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento del comportamento strutturale (dissipativo o non dissipativo) e del fattore di comportamento q secondo le NTC 2018 (DM 17 gennaio 2018), paragrafi 7.2.2 e 7.3.1. Aiuta a scegliere il comportamento strutturale (non dissipativo: tutte le membrature e i collegamenti restano in campo elastico, domanda calcolata con modello elastico; dissipativo: un numero elevato di membrature e collegamenti evolve in campo plastico e la capacita' dissipativa e' presa in conto implicitamente tramite il fattore di comportamento q o esplicitamente con adeguata legge costitutiva), le classi di duttilita' CD alta e CD media, e la progettazione in capacita' con il fattore di sovraresistenza (globale almeno 1,25); e a determinare il fattore di comportamento q: limite superiore qlim uguale al prodotto tra il valore base q0 e il fattore KR (pari a 1 per le costruzioni regolari in altezza e a 0,8 per quelle non regolari in altezza), formula 7.3.1, con q0 dalla Tabella 7.3.II in funzione della classe di duttilita', della tipologia strutturale e del rapporto alfa-u su alfa-1; riduzione kw per le pareti in calcestruzzo armato; componente verticale q uguale a 1,5 (ponti q uguale a 1); comportamento non dissipativo con q compreso tra 1 e 1,5 pari a due terzi del q della CD media, formula 7.3.2. Use when a structural designer must frame the choice of dissipative or non-dissipative behavior, ductility classes and the behaviour factor q under the Italian NTC 2018 par. 7.2.2-7.3.1; it is a documentary aid and does NOT compute q nor the seismic demand, does NOT reproduce the full material q0 tables (par. 7.4-7.9), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Comportamento strutturale e fattore q (NTC 2018 par. 7.2.2-7.3.1)"
summary: "Inquadra la scelta del comportamento strutturale (dissipativo/non dissipativo, duttilita' CD\"A\"/CD\"B\") e il fattore q (NTC 2018 par. 7.2.2-7.3.1): qlim = q0*KR [7.3.1] (KR 1/0,8), non dissipativo 1<=qND=(2/3)qCD\"B\"<=1,5 [7.3.2], verticale q=1,5 (ponti 1)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.2.2: comportamento non dissipativo/dissipativo, classi di duttilita' CD\"A\"/CD\"B\", progettazione in capacita', sovraresistenza globale >= 1,25"
  - "NTC 2018 - par. 7.3.1: fattore di comportamento q, qlim = q0*KR [7.3.1] con KR 1 (regolare in altezza)/0,8 (non regolare); q0 Tab. 7.3.II; kw per pareti c.a.; verticale q=1,5 (ponti 1)"
  - "NTC 2018 - par. 7.3.1: comportamento non dissipativo qND, 1 <= qND = (2/3) qCD\"B\" <= 1,5 [7.3.2]; spettro di progetto par. 3.2.3.4-3.2.3.5"
version: 0.1.0-alpha
status: alpha
tags:
  - fattore-comportamento
  - comportamento-dissipativo
  - classi-duttilita
  - progettazione-sismica
  - ntc-2018
---

# Comportamento strutturale e fattore di comportamento q (NTC 2018 par. 7.2.2-7.3.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la scelta del **comportamento strutturale**
(dissipativo o non dissipativo) e la determinazione del **fattore di comportamento q** — che riduce lo spettro
elastico allo **spettro di progetto** — secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.2.2 e 7.3.1**:

- **comportamento strutturale** e **classi di duttilità** (§7.2.2);
- **fattore di comportamento q** allo SLV (§7.3.1).

**Non è** uno strumento che calcola q o la domanda sismica: è un **supporto documentale** che inquadra criteri e
formula. A valle, per lo spettro di progetto usa `spettro-risposta-ntc` (§3.2); per la regolarità (che fissa KR)
`regolarita-strutturale-sismica-ntc` (§7.2.1).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-comportamento-strutturale` | Comportamento non dissipativo vs dissipativo, classi di duttilità CD"A"/CD"B" e progettazione in capacità (γRd globale ≥ 1,25) (§7.2.2) |
| `inquadra-fattore-comportamento-q` | Fattore q allo SLV: qlim = q0·KR [7.3.1] (KR 1/0,8), q0 Tab. 7.3.II, kw pareti c.a., verticale q=1,5 (ponti 1), non dissipativo [7.3.2] (§7.3.1) |

## Punti chiave (verificati sul testo)

- **Comportamento strutturale** (§7.2.2): **non dissipativo** (membrature/collegamenti in campo elastico, modello
  elastico §7.2.6) o **dissipativo** (plasticizzazioni diffuse; capacità dissipativa in conto **implicitamente**
  via q o **esplicitamente** via legge costitutiva). Le costruzioni dissipative perseguono **CD"A"** (alta) o
  **CD"B"** (media).
- **Progettazione in capacità** (§7.2.2): distingue elementi **duttili/fragili**; la capacità allo **SLV** dei
  fragili deve superare quella dei duttili alternativi, incrementando i duttili col **fattore di sovraresistenza
  γRd** (globale **≥ 1,25** ove non specificato).
- **Fattore di comportamento q** (§7.3.1): limite superiore **qlim = q0 · KR** [7.3.1], con **KR = 1** (regolare
  in altezza) / **0,8** (non regolare); **q0** dalla **Tab. 7.3.II** secondo CD, tipologia, Ω e rapporto **αu/α1**
  (es. c.a. a telaio CD"A" 4,5·αu/α1, CD"B" 3,0·αu/α1). Con **pareti in c.a.** q0 è ridotto dal fattore **kw**.
- **Casi particolari** (§7.3.1): componente **verticale q = 1,5** (ponti **q = 1**); comportamento **non
  dissipativo** **1 ≤ qND = (2/3)·qCD"B" ≤ 1,5** [7.3.2].

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.2 e 7.3.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; le formule [7.3.1], [7.3.2] e la Tab. 7.3.II verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** q, qlim, qND, kw o αu/α1 né **la domanda sismica** / lo **spettro di progetto** (§3.2.3).
- **Non riproduce** il **set completo** delle Tab. 7.3.II per ogni tipologia/materiale (§7.4-7.9): riporta valori
  rappresentativi e rinvia alle skill/paragrafi di materiale.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura dei par. 7.2.2-7.3.1 delle NTC 2018 e della Circolare applicativa.**
