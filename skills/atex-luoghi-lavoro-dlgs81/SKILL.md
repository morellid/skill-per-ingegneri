---
name: atex-luoghi-lavoro-dlgs81
description: "Supporto documentale alla protezione dei lavoratori dai rischi da atmosfere esplosive (ATEX luoghi di lavoro) ai sensi del Titolo XI del D.Lgs. 81/2008 (recepimento dir. 1999/92/CE): aiuta a capire quando si applica (definizione di atmosfera esplosiva, esclusioni dell'art. 287), gli obblighi del datore di lavoro (prevenire la formazione, evitare l'accensione, attenuare gli effetti - art. 289), la valutazione dei rischi di esplosione (art. 290), la classificazione delle aree in zone (art. 293, allegato XLIX) con le prescrizioni minime (allegato L) e la segnaletica (allegato LI), il documento sulla protezione contro le esplosioni (DPCE, art. 294), le verifiche delle installazioni elettriche nelle zone (art. 296, DPR 462/2001) e le sanzioni (art. 297). Use when an Italian employer, RSPP or safety consultant must map the workplace explosive-atmosphere duties, zone classification and the explosion protection document; it is a documentary aid, does not classify the zones nor draft the DPCE, and does not cover ATEX equipment marking (2014/34/EU)."
license: MIT
area: sicurezza-lavoro-cantieri
title: "ATEX luoghi di lavoro - D.Lgs. 81/2008 Titolo XI"
summary: "Protezione dei lavoratori dalle atmosfere esplosive (ATEX luoghi di lavoro, D.Lgs. 81/2008 Titolo XI): ambito (art. 287), obblighi del datore (art. 289), valutazione del rischio (art. 290), zone (art. 293), documento protezione dalle esplosioni (art. 294), sanzioni (art. 297)"
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 (testo vigente) - Titolo XI, artt. 287-290, 293, 294, 296, 297 (recepimento dir. 1999/92/CE)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - atex
  - atmosfere-esplosive
  - sicurezza-lavoro
  - classificazione-zone
---

# ATEX luoghi di lavoro - D.Lgs. 81/2008 Titolo XI

## Quando usare questa skill

Usala quando devi orientarti sulla **protezione dei lavoratori dai rischi da
atmosfere esplosive** ai sensi del **Titolo XI del D.Lgs. 81/2008** (recepimento
della dir. 1999/92/CE):

- capire se il Titolo XI **si applica** (definizione di atmosfera esplosiva,
  esclusioni dell'art. 287);
- individuare gli **obblighi del datore di lavoro** (art. 289) e la **valutazione
  del rischio di esplosione** (art. 290);
- impostare la **classificazione delle aree in zone** (art. 293, allegato XLIX),
  le **prescrizioni minime** (allegato L) e la **segnaletica** (allegato LI);
- redigere/verificare il **documento sulla protezione contro le esplosioni**
  (DPCE, art. 294) e conoscere **verifiche** (art. 296) e **sanzioni** (art. 297).

**Non e' una skill di calcolo**: non classifica le zone (allegato XLIX), non
redige la valutazione del rischio ne' il DPCE, e **non tratta la marcatura ATEX
degli apparecchi** (dir. prodotti 2014/34/UE).

## Cosa NON fa (limiti)

- Non riproduce la **classificazione delle zone** (allegato XLIX), le
  **prescrizioni minime** (allegato L) ne' la **segnaletica** (allegato LI):
  rinvia agli allegati e alle norme tecniche (es. CEI EN 60079).
- Non redige la valutazione del rischio di esplosione ne' il **DPCE**.
- Non copre la **marcatura ATEX** degli apparecchi (dir. 2014/34/UE).
- Non sostituisce il datore di lavoro, l'RSPP ne' il tecnico qualificato.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`applicabilita-e-obblighi`](tasks/applicabilita-e-obblighi.md) | Dato il luogo di lavoro (sostanze infiammabili, processi, esclusioni), determina se si applica il Titolo XI e la sequenza degli obblighi (prevenzione, valutazione, zone, DPCE) |
| [`checklist-dpce`](tasks/checklist-dpce.md) | Verifica i contenuti minimi del documento sulla protezione contro le esplosioni (art. 294) e le sanzioni (art. 297) |

## Riferimenti normativi

- **D.Lgs. 9/4/2008 n. 81** (TU sicurezza), Titolo XI, testo vigente su
  Normattiva:
  - art. 287 (ambito), art. 288 (definizioni), art. 289 (prevenzione/
    protezione), art. 290 (valutazione), art. 293 (zone), art. 294 (DPCE),
    art. 296 (verifiche), art. 297 (sanzioni).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-81-2008.md`,
`references/estratti/atex-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione delle zone e la valutazione
del rischio richiedono la lettura degli allegati e delle norme tecniche e
l'intervento di tecnici qualificati; la responsabilita' resta del datore di
lavoro.
