---
name: mog-231-reati-ambientali
description: "Supporto documentale alla parte speciale ambientale del Modello di Organizzazione, Gestione e Controllo (MOG) ex D.Lgs 231/2001: mappa i reati presupposto ambientali dell'art. 25-undecies (ecoreati del codice penale 452-bis e seguenti - inquinamento ambientale, disastro ambientale, delitti colposi, traffico di materiale radioattivo, omessa bonifica, attivita' organizzate per il traffico illecito di rifiuti, uccisione di specie protette, distruzione di habitat; reati del D.Lgs 152/2006 su scarichi art. 137, gestione rifiuti art. 256-256-bis, bonifica art. 257, tracciabilita' artt. 258-259-260-bis, emissioni art. 279; reati della L. 150/1992 CITES, della L. 549/1993 sull'ozono e del D.Lgs 202/2007 sull'inquinamento da navi) con le relative sanzioni pecuniarie a quote e interdittive, e collega ciascun reato alle aree di compliance ambientale e ai controlli della parte speciale (individuazione delle attivita' a rischio, protocolli, flussi informativi verso l'Organismo di Vigilanza, sistema disciplinare, whistleblowing) ai sensi degli artt. 6-7. Use when an HSE/environmental engineer, compliance officer or OdV member must map the environmental predicate offences and structure the environmental part of a 231 organisational model; it is a documentary aid and does not draft the model, does not reproduce the single offences and does not perform the legal assessment of liability."
license: MIT
area: ambiente-territorio-mobilita
title: "MOG 231 - Reati ambientali (art. 25-undecies D.Lgs 231/2001)"
summary: "Parte speciale ambientale del Modello 231: mappa i reati presupposto ambientali dell'art. 25-undecies D.Lgs 231/2001 (ecoreati c.p., D.Lgs 152/2006 su scarichi/rifiuti/bonifica/emissioni, CITES, ozono, navi) con sanzioni a quote/interdittive e i controlli del MOG (artt. 6-7)."
normative_refs:
  - "D.Lgs. 8/6/2001 n. 231 - art. 25-undecies (reati ambientali), artt. 6-7 (modelli di organizzazione) e art. 9 (sanzioni interdittive)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-231-2001
  - reati-ambientali
  - mog-231
  - art-25-undecies
  - compliance-ambientale
---

# MOG 231 - Reati ambientali (art. 25-undecies D.Lgs 231/2001)

## Quando usare questa skill

Usala quando devi impostare o rivedere la **parte speciale ambientale** di un
**Modello di Organizzazione, Gestione e Controllo (MOG)** ai sensi del **D.Lgs
231/2001**:

- **mappare i reati presupposto ambientali** dell'**art. 25-undecies** (ecoreati
  del codice penale 452-bis ss.; reati del **D.Lgs 152/2006** su scarichi, rifiuti,
  bonifica, emissioni; **L. 150/1992** CITES; **L. 549/1993** ozono; **D.Lgs
  202/2007** navi) con le relative **sanzioni** pecuniarie a quote e **interdittive**;
- **collegare** ciascun reato alle **aree di compliance ambientale** e ai
  **controlli** della parte speciale (attivita' a rischio, protocolli, flussi
  informativi verso l'**Organismo di Vigilanza**, sistema disciplinare,
  whistleblowing), ai sensi degli **artt. 6-7**.

**Non e' una skill legale ne' redazionale**: non redige il Modello, non riproduce
il testo dei singoli reati e non effettua la valutazione legale della
responsabilita'.

## Cosa NON fa (limiti)

- Non riproduce ne' interpreta il **testo dei singoli reati** (452-bis ss. c.p.;
  artt. 137, 256 ss., 279 D.Lgs 152/2006, ecc.): li mappa e rinvia alle fonti (per
  gli aspetti tecnici, alle skill del repo su scarichi/emissioni, rifiuti, bonifica).
- Non redige il **Modello 231** ne' i protocolli operativi: ne fornisce la struttura.
- Non effettua la **valutazione legale** della responsabilita' dell'ente ne' quantifica
  le sanzioni (la **quota** e' fissata dal giudice tra minimo e massimo edittale).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`mappa-reati-presupposto`](tasks/mappa-reati-presupposto.md) | Date le attivita' ambientali dell'ente, individua i reati presupposto ambientali applicabili (art. 25-undecies) e le relative sanzioni |
| [`struttura-parte-speciale`](tasks/struttura-parte-speciale.md) | Struttura la parte speciale ambientale del MOG (attivita' a rischio, protocolli, flussi OdV, sistema disciplinare) ai sensi degli artt. 6-7 |

## Riferimenti normativi

- **D.Lgs. 8/6/2001 n. 231** - **art. 25-undecies** (reati ambientali: sanzioni per
  ecoreati c.p., D.Lgs 152/2006, L. 150/1992, L. 549/1993, D.Lgs 202/2007), **artt.
  6-7** (modelli di organizzazione, funzione esimente, OdV), **art. 9** (sanzioni
  interdittive, citato).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-231-2001.md`,
`references/estratti/reati-ambientali-231-mappa.md`.

## Avvertenza

Skill di **supporto documentale**: la costruzione del Modello 231, la valutazione
della sua idoneita' e la valutazione legale della responsabilita' dell'ente
restano in capo ai professionisti competenti (legale, compliance, OdV) e agli
organi dell'ente. La skill **non sostituisce** il consulente legale, l'Organismo di
Vigilanza ne' il giudizio tecnico sulle singole autorizzazioni ambientali.
