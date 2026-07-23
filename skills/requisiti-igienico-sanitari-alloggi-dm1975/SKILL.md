---
name: requisiti-igienico-sanitari-alloggi-dm1975
description: "Supporto documentale al tecnico (geometra, ingegnere, architetto) per inquadrare i requisiti igienico-sanitari minimi dei locali di abitazione secondo il DM 5 luglio 1975 (Ministero della sanita'), nella progettazione degli alloggi, nei frazionamenti o cambi di destinazione e nella verifica di agibilita'. Aiuta a inquadrare: l'altezza minima interna utile dell'art. 1, fissata in 2,70 m e riducibile a 2,40 m per corridoi, disimpegni, bagni, gabinetti e ripostigli, con riduzione a 2,55 m per i comuni montani oltre i 1000 m sul livello del mare; le superfici minime dell'art. 2 (superficie abitabile di almeno 14 mq per abitante per i primi 4 abitanti e 10 mq per ciascuno dei successivi, stanze da letto di almeno 9 mq per una persona e 14 mq per due, stanza di soggiorno di almeno 14 mq, con finestra apribile per letto, soggiorno e cucina); l'alloggio monostanza dell'art. 3 (almeno 28 mq per una persona e 38 mq per due, comprensivo dei servizi); il riscaldamento e la temperatura di progetto dell'aria interna tra 18 e 20 gradi dell'art. 4; l'illuminazione naturale diretta, il fattore di luce diurna medio non inferiore al 2 per cento e la superficie finestrata apribile non inferiore a 1/8 della superficie del pavimento dell'art. 5; la ventilazione naturale o meccanica e l'aspirazione di fumi e vapori dell'art. 6; la stanza da bagno e la sua dotazione minima (vaso, bidet, vasca da bagno o doccia, lavabo) dell'art. 7; e la protezione acustica dei materiali dell'art. 8. Use when a technician must frame the minimum health and hygiene requirements of dwellings under the Italian DM 5 July 1975; it is a documentary aid, does NOT draft the project, does NOT reproduce the regional or municipal building regulations nor the derogations for the recovery of attics/existing premises, and does NOT replace the designer. It is distinct from the passive acoustic requirements skill (DPCM 5 December 1997) and the accessibility skill (DM 236/1989)."
license: MIT
area: edilizia-urbanistica-catasto
title: "Requisiti igienico-sanitari minimi degli alloggi (DM 5 luglio 1975)"
summary: "Inquadra i requisiti igienico-sanitari minimi degli alloggi (DM 5 luglio 1975): altezza minima 2,70 m (art. 1), superfici minime e monostanza 28/38 mq (artt. 2-3), riscaldamento 18-20 gradi (art. 4), aeroilluminazione (art. 5), ventilazione e bagno (artt. 6-7)."
normative_refs:
  - "DM 5 luglio 1975: altezza 2,70 m / 2,40 servizi (art. 1); superfici 14+10 mq/ab, letto 9/14 (art. 2); monostanza 28/38 mq (art. 3); 18-20 gradi (art. 4); finestra >= 1/8 pavimento (art. 5)"
  - "Rinvio (fuori scope): regolamenti edilizi regionali/comunali e Reg. Edilizio Tipo; deroghe recupero sottotetti; requisiti acustici DPCM 5/12/1997; accessibilita' DM 236/1989 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - requisiti-igienico-sanitari
  - altezza-minima
  - aeroilluminazione
  - dm-5-luglio-1975
  - agibilita
---

# Requisiti igienico-sanitari minimi degli alloggi (DM 5 luglio 1975)

## Quando usare questa skill

Usala quando un **tecnico** (geometra, ingegnere, architetto) deve **inquadrare i requisiti igienico-sanitari
minimi** dei **locali di abitazione** secondo il **DM 5 luglio 1975** (Ministero della sanità) — nella
**progettazione** degli alloggi, nei **frazionamenti/cambi di destinazione** e nella **verifica di agibilità**:

- **altezze minime** interne (art. 1);
- **superfici minime** per abitante, stanze e alloggio monostanza (artt. 2-3);
- **riscaldamento**, **aeroilluminazione**, **ventilazione** e **servizi** (artt. 4-7);
- **protezione acustica** dei materiali (art. 8).

È un **supporto documentale** sui **requisiti minimi nazionali**: inquadra i valori; **non** redige il
progetto, **non** riproduce i regolamenti edilizi regionali/comunali né le deroghe (es. recupero sottotetti).
È **distinta** da `requisiti-acustici-passivi-edifici-dpcm` (DPCM 5/12/1997, valori limite acustici) e da
`barriere-architettoniche-edifici-privati-dm236` (accessibilità); complementare a `segnalazione-agibilita-dpr380`.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-altezze-superfici-minime` | Altezza minima interna (art. 1) e superfici minime per abitante, stanze da letto, soggiorno e alloggio monostanza (artt. 2-3) |
| `verifica-aeroilluminazione-servizi-impianti` | Riscaldamento (art. 4), illuminazione/aeroilluminazione (art. 5), ventilazione (art. 6), bagno (art. 7) e protezione acustica (art. 8) |

## Punti chiave (verificati sul testo/immagine)

- **Altezza minima** (art. 1): **2,70 m**; **2,40 m** per corridoi/disimpegni/bagni/gabinetti/ripostigli;
  **2,55 m** nei **comuni montani > 1000 m** s.l.m.
- **Superfici** (art. 2): **≥ 14 mq/abitante** (primi 4), **10 mq** per i successivi; **stanze da letto 9 mq**
  (1 pers.) / **14 mq** (2 pers.); **soggiorno ≥ 14 mq**; finestra apribile per letto/soggiorno/cucina.
- **Monostanza** (art. 3): **≥ 28 mq** (1 pers.) / **38 mq** (2 pers.), comprensivo dei servizi.
- **Riscaldamento** (art. 4): temperatura di progetto **18-20 °C**; no condensazione permanente.
- **Aeroilluminazione** (art. 5): illuminazione naturale diretta; **fattore di luce diurna medio ≥ 2%**;
  **superficie finestrata apribile ≥ 1/8 del pavimento**.
- **Ventilazione/bagno** (artt. 6-7): ventilazione meccanica ove manca la naturale; **stanza da bagno** con
  apertura/aspirazione, dotata (almeno una) di **vaso, bidet, vasca o doccia, lavabo**.

## Fonti

- **DM 5 luglio 1975** — **G.U. Serie Generale n. 190 del 18/7/1975** (PDF Gazzetta Ufficiale, SHA256
  `3fd9f355...`). Scansione **GURITEL**: gli articoli 1-9 sono stati letti renderizzando le pagine in immagine
  (`pdftoppm`, pagine PDF 12-13) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il progetto né esegue calcoli illuminotecnici/termotecnici di dettaglio (fattore di luce
  diurna, dispersioni); è un inquadramento dei **requisiti minimi**.
- **Non riproduce** i **regolamenti edilizi regionali/comunali** e il **Regolamento Edilizio Tipo**, né le
  **deroghe** per il **recupero dei sottotetti**/locali esistenti (leggi regionali).
- **Non fornisce** i **valori limite acustici** (→ skill `requisiti-acustici-passivi-edifici-dpcm`, DPCM
  5/12/1997) né i requisiti di **accessibilità** (→ skill `barriere-architettoniche-edifici-privati-dm236`);
  **non** sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista, né la lettura del DM 5 luglio 1975 e dei regolamenti edilizi regionali/comunali applicabili.**
