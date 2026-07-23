# CHANGELOG - requisiti-igienico-sanitari-alloggi-dm1975

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #452)
- Prima versione della skill di supporto al **tecnico** (geometra, ingegnere, architetto) per l'**inquadramento
  dei requisiti igienico-sanitari minimi** dei locali di abitazione secondo il **DM 5 luglio 1975** (Ministero
  della sanità), nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **DM 5 luglio 1975** - PDF della G.U. Serie Generale n. 190 del 18 luglio 1975 - SHA256:
    3fd9f3552dadfd2f791910d4813f593f57422cd802831a084f64eff51cd178d1 (doppio download riproducibile dallo
    stesso URL eli della Gazzetta Ufficiale).
  - Il PDF è una scansione GURITEL (immagine): gli articoli 1-9 sono stati letti renderizzando le pagine in
    immagine (`pdftoppm -r 150 -png`, pagine PDF 12-13) e trascritti verbatim in
    `references/fonti/dm-5-7-1975.md`.
- Estratto operativo `references/estratti/requisiti-igienico-sanitari-checklist.md`.
- Due task: `verifica-altezze-superfici-minime.md` e `verifica-aeroilluminazione-servizi-impianti.md`.
- Due esempi: verifica di altezze e superfici di un alloggio; verifica del rapporto aeroilluminante (1/8) e
  dell'altezza minima del bagno.

### Contenuto ancorato al testo
- Altezza minima interna (art. 1): 2,70 m; 2,40 m per corridoi/disimpegni/bagni/gabinetti/ripostigli; 2,55 m
  per comuni montani > 1000 m s.l.m. Superfici (art. 2): 14 mq/abitante (primi 4) + 10 mq successivi; stanze da
  letto 9 mq (1 persona) / 14 mq (2 persone); soggiorno ≥ 14 mq; finestra apribile per letto/soggiorno/cucina.
  Alloggio monostanza (art. 3): 28 mq (1 persona) / 38 mq (2 persone), comprensivo dei servizi. Riscaldamento
  (art. 4): temperatura di progetto 18-20 °C; no condensazione permanente. Aeroilluminazione (art. 5):
  illuminazione naturale diretta; fattore di luce diurna medio ≥ 2%; superficie finestrata apribile ≥ 1/8 della
  superficie del pavimento. Ventilazione (art. 6): meccanica ove manca la naturale; aspirazione fumi; posto di
  cottura. Bagno (art. 7): apertura all'esterno o aspirazione meccanica; almeno una dotata di vaso, bidet,
  vasca da bagno o doccia, lavabo. Protezione acustica (art. 8). Abrogazione parziale delle istruzioni 20/6/1896
  (art. 9).

### Scope e limiti
- Non redige il progetto né esegue calcoli illuminotecnici/termotecnici di dettaglio; non riproduce i
  regolamenti edilizi regionali/comunali e il Regolamento Edilizio Tipo né le deroghe per il recupero dei
  sottotetti; non fornisce i valori limite acustici (DPCM 5/12/1997) né l'accessibilità (DM 236/1989). Non
  sostituisce il progettista.

### Note di sviluppo
- Distinta da `requisiti-acustici-passivi-edifici-dpcm` e `barriere-architettoniche-edifici-privati-dm236`;
  complementare a `segnalazione-agibilita-dpr380`. Fonte GURITEL letta via immagine. Validazione Livello 2 con
  tecnico comunale/ASL o progettista edile.
