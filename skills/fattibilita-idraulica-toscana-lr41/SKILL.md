---
name: fattibilita-idraulica-toscana-lr41
description: "Supporto documentale alla fattibilita' delle trasformazioni nelle aree a pericolosita' per alluvioni in Toscana ai sensi della L.R. 41/2018: aiuta a inquadrare il sito (aree a pericolosita' per alluvioni frequenti o poco frequenti) e la magnitudo idraulica (moderata, severa, molto severa, in funzione di battente e velocita' della corrente, art. 2), a individuare le opere per la gestione del rischio necessarie a raggiungere il rischio medio R2 (opere idrauliche per l'assenza o la riduzione degli allagamenti, opere di sopraelevazione, interventi di difesa locale, art. 8), le limitazioni assolute nelle aree a pericolosita' frequente (ospedali, strutture strategiche, impianti AIA - art. 10) e le condizioni per la nuova costruzione (art. 11) e per gli interventi sul patrimonio edilizio esistente (art. 12). Use when an engineer or planner in Tuscany must check whether a building intervention is admissible in a flood-hazard area and which hydraulic safety works are required; it is a documentary aid and does not read the hazard maps, does not measure the water depth/velocity nor size the works."
license: MIT
area: edilizia-urbanistica-catasto
title: "Fattibilita' idraulica delle trasformazioni in Toscana - L.R. 41/2018"
summary: "Fattibilita' delle trasformazioni nelle aree a pericolosita' per alluvioni in Toscana (L.R. 41/2018): magnitudo idraulica moderata/severa/molto severa (art. 2), opere per il rischio medio R2 (art. 8), limitazioni (art. 10), condizioni per nuova costruzione (art. 11) ed esistente"
normative_refs:
  - "L.R. Toscana 24/7/2018 n. 41 - artt. 2, 7, 8, 10, 11, 12 (attuazione d.lgs. 49/2010, dir. 2007/60/CE)"
version: 0.1.0-alpha
status: alpha
tags:
  - lr-toscana-41-2018
  - rischio-alluvioni
  - pericolosita-idraulica
  - toscana
  - fattibilita-idraulica
---

# Fattibilita' idraulica delle trasformazioni in Toscana - L.R. 41/2018

## Quando usare questa skill

Usala quando, in **Toscana**, devi verificare se un intervento edilizio e'
ammissibile in un'**area a pericolosita' per alluvioni** e quali **opere di messa
in sicurezza idraulica** sono richieste, ai sensi della **L.R. 41/2018**:

- inquadrare il sito (aree a pericolosita' per alluvioni **frequenti** o **poco
  frequenti**) e la **magnitudo idraulica** (moderata / severa / molto severa, in
  base a **battente** e **velocita'**, art. 2);
- individuare le **opere per la gestione del rischio** necessarie a raggiungere il
  **rischio medio R2** (art. 8);
- conoscere le **limitazioni assolute** (art. 10) e le condizioni per la **nuova
  costruzione** (art. 11) e per il **patrimonio esistente** (art. 12).

**Non e' una skill di calcolo**: non individua la classe di pericolosita' del
sito, non misura battente/velocita', non dimensiona le opere ne' calcola i volumi
di compenso/laminazione.

## Cosa NON fa (limiti)

- Non individua la **classe di pericolosita'** del sito ne' misura **battente/
  velocita'**: sono dati del **PGRA**/Piani di bacino e della relazione idraulica.
- Non progetta le **opere idrauliche/di sopraelevazione** ne' calcola i **volumi**
  di compenso/laminazione (rinvio a DGR/allegati tecnici e al progettista).
- Non riproduce il **DPGR 5/R/2020** (indagini geologiche/idrauliche/sismiche) ne'
  le mappe di pericolosita'.
- Vale per la **Toscana**; altre regioni hanno discipline proprie.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-fattibilita`](tasks/verifica-fattibilita.md) | Dato il sito (area a pericolosita' frequente/poco frequente, battente e velocita' -> magnitudo) e l'intervento (nuova costruzione, esistente, opera pubblica), determina l'ammissibilita' e le opere di messa in sicurezza richieste |
| [`checklist-interventi`](tasks/checklist-interventi.md) | Verifica le limitazioni assolute (art. 10) e le condizioni delle opere (art. 8) per l'intervento, con il rinvio agli atti di pianificazione di bacino |

## Riferimenti normativi

- **L.R. Toscana 24/7/2018 n. 41** (rischio alluvioni e tutela dei corsi
  d'acqua), testo vigente sulla Raccolta Normativa del Consiglio regionale -
  artt. 2, 7, 8, 10, 11, 12 (attuazione d.lgs. 49/2010, dir. 2007/60/CE).

Dettaglio in `references/sources.yaml`, `references/fonti/lr-toscana-41-2018.md`,
`references/estratti/fattibilita-idraulica-checklist.md`.

> Nota sulla scheda #49: la issue cita il DPGR 5/R/2020, che pero' disciplina il
> deposito/controllo delle indagini geologiche, idrauliche e sismiche, non la
> fattibilita' idraulica. La fonte corretta e' la **L.R. 41/2018**, usata qui.

## Avvertenza

Skill di **supporto documentale**: la classe di pericolosita', i valori di
battente/velocita' e il progetto delle opere richiedono il PGRA, la relazione
idraulica e un tecnico abilitato; la decisione spetta al Comune e all'autorita'
idraulica. **Non sostituisce** il PGRA, il progettista abilitato ne' l'autorita'
idraulica/comunale.
