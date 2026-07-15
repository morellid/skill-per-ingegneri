---
name: trasporto-rifiuti-fir-dlgs152
description: "Supporto documentale agli obblighi del trasporto dei rifiuti ai sensi del D.Lgs. 152/2006: aiuta a impostare il formulario di identificazione dei rifiuti (FIR, art. 193 - obbligo, quattro copie, firme di produttore/detentore, trasportatore e destinatario, modello e digitalizzazione via RENTRI dell'art. 188-bis, imballaggio ed etichettatura dei rifiuti pericolosi, esclusioni per rifiuti urbani ai centri di raccolta e spedizioni transfrontaliere), a verificare l'obbligo di iscrizione all'Albo nazionale gestori ambientali (art. 212 - requisito per raccolta e trasporto, con la semplificazione per i produttori iniziali che trasportano i propri rifiuti non pericolosi o pericolosi fino a 30 kg/30 litri al giorno) e a conoscere le sanzioni (art. 258 - da 1.600 a 10.000 euro per trasporto senza formulario o con dati inesatti, reclusione da uno a tre anni per rifiuti pericolosi senza formulario). Use when an Italian company transporting waste must map the identification form and the environmental-operators register duties and the penalties; it is a documentary aid and does not classify the waste nor fill in the form."
license: MIT
area: ambiente-territorio-mobilita
title: "Trasporto rifiuti: formulario (FIR) e Albo gestori - D.Lgs. 152/2006"
summary: "Obblighi del trasporto dei rifiuti (D.Lgs. 152/2006): formulario di identificazione FIR (art. 193 - quattro copie, firme, RENTRI, esclusioni), iscrizione all'Albo gestori ambientali (art. 212 - requisito, semplificazioni per i propri rifiuti), sanzioni (art. 258)"
normative_refs:
  - "D.Lgs. 3/4/2006 n. 152 (testo vigente) - artt. 193, 212, 258 (Parte quarta - rifiuti)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-152-2006
  - rifiuti
  - formulario-fir
  - albo-gestori-ambientali
  - trasporti
---

# Trasporto rifiuti: formulario (FIR) e Albo gestori - D.Lgs. 152/2006

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi del **trasporto dei rifiuti** ai
sensi del **D.Lgs. 152/2006** (Parte quarta):

- impostare il **formulario di identificazione dei rifiuti (FIR)** (art. 193:
  obbligo, quattro copie, firme, modello/RENTRI, imballaggio ed etichettatura dei
  pericolosi, esclusioni);
- verificare l'obbligo di **iscrizione all'Albo nazionale gestori ambientali**
  (art. 212), incluse le **semplificazioni** per chi trasporta i **propri
  rifiuti**;
- conoscere le **sanzioni** (art. 258).

**Non e' una skill di calcolo**: non classifica il rifiuto (codici EER), non
redige il formulario, non riproduce il modello del FIR ne' le regole dell'Albo.

## Cosa NON fa (limiti)

- Non riproduce il **modello del formulario** ne' la disciplina del **RENTRI**
  (art. 188-bis) e dei decreti attuativi.
- Non riproduce le **categorie/classi** dell'Albo.
- Non tratta i **registri di carico/scarico** (art. 190), il **MUD** ne' la
  disciplina **ADR** oltre ai richiami.
- Non stabilisce la **classificazione** del rifiuto ne' redige il FIR.
- Non sostituisce il gestore, il trasportatore ne' l'Albo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-obblighi`](tasks/inquadra-obblighi.md) | Dato il soggetto (produttore, trasportatore conto terzi/proprio, tipo e quantita' di rifiuto), determina l'obbligo del FIR (art. 193) e dell'iscrizione all'Albo (art. 212) o l'applicabilita' delle semplificazioni |
| [`checklist-fir`](tasks/checklist-fir.md) | Verifica la corretta gestione del formulario (copie, firme, distribuzione) e le sanzioni (art. 258) |

## Riferimenti normativi

- **D.Lgs. 3/4/2006 n. 152** (TUA), Parte quarta, testo vigente su Normattiva
  (pagina indice pinnata `!vig=2026-07-14`) - **art. 193** (formulario FIR),
  **art. 212** (Albo gestori ambientali), **art. 258** (sanzioni). Richiami: art.
  188-bis (RENTRI), art. 190 (registri), ADR.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-152-2006.md`,
`references/estratti/trasporto-rifiuti-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione del rifiuto, la compilazione
del formulario e l'inquadramento all'Albo richiedono il gestore e i tecnici; il
modello del FIR segue il RENTRI (art. 188-bis).
