---
name: standard-urbanistici-distanze-dm1444
description: "Supporto documentale al tecnico (geometra, ingegnere, architetto, urbanista) per inquadrare i limiti inderogabili del DM 2 aprile 1968 n. 1444 nella formazione o revisione degli strumenti urbanistici e nella verifica di conformita' urbanistica. Aiuta a inquadrare: le zone territoriali omogenee dell'art. 2 (A storiche o di pregio ambientale; B edificate, considerate parzialmente edificate se la superficie coperta e' almeno il 12,5 per cento della superficie fondiaria e la densita' territoriale supera 1,5 mc/mq; C nuovi complessi insediativi; D insediamenti industriali; E usi agricoli; F attrezzature e impianti di interesse generale); gli standard urbanistici dell'art. 3, con la dotazione minima inderogabile di 18 mq per abitante ripartiti in 4,50 mq per l'istruzione, 2,00 mq per attrezzature di interesse comune, 9,00 mq per verde attrezzato, gioco e sport e 2,50 mq per parcheggi, assumendo 25 mq di superficie lorda per abitante; le quantita' per zona dell'art. 4 (zone C 18 mq oppure 12 mq per comuni fino a 10.000 abitanti, zone E 6 mq, zone F 1,5 piu' 1 piu' 15 mq per abitante) e per gli insediamenti produttivi dell'art. 5 (zone D almeno il 10 per cento, insediamenti commerciali e direzionali 80 mq ogni 100 mq); i limiti di densita' edilizia dell'art. 7 (zone A non oltre il 50 per cento della densita' media e comunque 5 mc/mq, zone B 7, 6 o 5 mc/mq secondo la popolazione del comune, zone E 0,03 mc/mq); i limiti di altezza dell'art. 8; e i limiti di distanza tra i fabbricati dell'art. 9, con la distanza minima assoluta di 10 metri tra pareti finestrate per i nuovi edifici, la distanza pari all'altezza del fabbricato piu' alto nelle zone C e le maggiorazioni per strade interposte (5, 7,50 o 10 metri per lato). Use when a technician must frame the Italian urban-planning standards, homogeneous zones and building-distance limits under DM 1444/1968; it is a documentary aid on the original 1968 text, does NOT draft the urban-planning instrument, does NOT reproduce the regional or municipal articulations nor later amendments, and does NOT replace the planner or designer. It is distinct from the civil-code building-distances skill (artt. 873-907, private law)."
license: MIT
area: edilizia-urbanistica-catasto
title: "Standard urbanistici, zone omogenee e distanze (DM 1444/1968)"
summary: "Inquadra i limiti inderogabili del DM 1444/1968: zone omogenee A-F (art. 2), standard urbanistici 18 mq/abitante (art. 3), quantita' per zona e produttivi (artt. 4-5), densita' edilizia (art. 7), altezze (art. 8), distanze 10 m tra pareti finestrate (art. 9)."
normative_refs:
  - "DM 1444/1968: zone A-F (art. 2); standard 18 mq/ab (art. 3); quantita' per zona (art. 4); produttivi (art. 5); densita' (art. 7); altezze (art. 8); distanze 10 m fra pareti finestrate (art. 9)"
  - "Rinvio (fuori scope): redazione strumenti urbanistici; articolazioni regionali/comunali; modifiche successive; distanze del codice civile artt. 873-907 (skill distanze-legali-costruzioni-cc)"
version: 0.1.0-alpha
status: alpha
tags:
  - standard-urbanistici
  - zone-omogenee
  - distanze-fabbricati
  - dm-1444-1968
  - urbanistica
---

# Standard urbanistici, zone omogenee e distanze (DM 1444/1968)

## Quando usare questa skill

Usala quando un **tecnico** (geometra, ingegnere, architetto, urbanista) deve **inquadrare i limiti
inderogabili** del **DM 2 aprile 1968 n. 1444** — nella **formazione o revisione degli strumenti urbanistici**
(PRG, piani particolareggiati, lottizzazioni, regolamenti edilizi) e nella **verifica di conformità
urbanistica** di un intervento:

- **zone territoriali omogenee** A-F (art. 2);
- **standard urbanistici** (spazi pubblici per abitante) e quantità per zona (artt. 3-5);
- **limiti di densità edilizia** (art. 7), **altezza** (art. 8) e **distanza tra i fabbricati** (art. 9).

È un **supporto documentale sul testo originario** del 1968: inquadra zone, standard, densità, altezze e
distanze; **non** redige lo strumento urbanistico, **non** riproduce le articolazioni regionali/comunali né le
modifiche successive. È **distinta** da `distanze-legali-costruzioni-cc` (codice civile artt. 873-907, diritto
privato): il DM 1444/1968 fissa limiti di **natura pubblicistica**, inderogabili ai fini urbanistici.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-zone-omogenee-standard` | Classificazione delle zone territoriali omogenee (art. 2) e computo degli standard urbanistici per zona (artt. 3-5) |
| `verifica-densita-altezza-distanze` | Limiti inderogabili di densità edilizia (art. 7), altezza (art. 8) e distanza tra i fabbricati (art. 9) |

## Punti chiave (verificati sul testo/immagine)

- **Zone omogenee** (art. 2): **A** storiche/di pregio; **B** edificate (parziali se coperto ≥ **12,5%** e
  densità > **1,5 mc/mq**); **C** nuovi complessi; **D** industriali; **E** agricole; **F** attrezzature di
  interesse generale.
- **Standard residenziali** (art. 3): **18 mq/abitante** (**4,50** istruzione + **2,00** interesse comune +
  **9,00** verde/sport + **2,50** parcheggi); **25 mq/abitante** di superficie lorda.
- **Quantità per zona** (art. 4): A)/B) computo **doppio**; C) **18 mq** (o **12 mq**, di cui **4** scuole, per
  comuni ≤ 10.000 ab.); E) **6 mq**; F) **1,5 + 1 + 15 mq/ab.**. Produttivi (art. 5): D) **≥ 10%**;
  commerciale/direzionale **80 mq ogni 100 mq**.
- **Densità edilizia** (art. 7): A) ≤ 50% media e ≤ **5 mc/mq**; B) **7 / 6 / 5 mc/mq** (comuni > 200.000 /
  200.000-50.000 / < 50.000 ab.); E) **0,03 mc/mq**.
- **Distanze** (art. 9): **10 m tra pareti finestrate** (nuovi edifici); zone C) ≥ **altezza del fabbricato più
  alto** (anche una sola parete finestrata se sviluppo > **12 m**); **strade interposte**: larghezza sede +
  **5 / 7,50 / 10 m** per lato (strade < 7 / 7-15 / > 15 m).

## Fonti

- **DM 2 aprile 1968 n. 1444** — **G.U. Serie Generale n. 97 del 16/4/1968** (PDF Gazzetta Ufficiale, SHA256
  `418cbdf7...`). Scansione **GURITEL**: gli articoli 1-10 sono stati letti renderizzando le pagine in immagine
  (`pdftoppm`, pagine PDF 24-26) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** lo strumento urbanistico né esegue il dimensionamento del piano; è un inquadramento dei
  **limiti inderogabili** del testo originario.
- **Non riproduce** le **articolazioni regionali/comunali** né le **modifiche normative successive** e
  l'**interpretazione giurisprudenziale** (in particolare sull'art. 9).
- **Non tratta** le distanze del **codice civile** (artt. 873-907, → skill `distanze-legali-costruzioni-cc`);
  **non** sostituisce il pianificatore né il progettista.

**La skill è un supporto documentale: non sostituisce il pianificatore né il progettista, né la lettura del DM 1444/1968, degli strumenti urbanistici vigenti e delle norme regionali/comunali applicabili.**
