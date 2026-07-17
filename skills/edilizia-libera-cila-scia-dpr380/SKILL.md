---
name: edilizia-libera-cila-scia-dpr380
description: "Supporto documentale ai regimi del titolo edilizio diversi dal permesso di costruire secondo il DPR 380/2001 (Testo unico edilizia), Titolo II. Aiuta a inquadrare l'attivita' edilizia libera (art. 6: interventi eseguibili senza alcun titolo abilitativo - manutenzione ordinaria, eliminazione di barriere architettoniche, VEPA, tende/pergole, opere temporanee di ricerca, movimenti di terra agricoli, serre mobili, opere stagionali fino a 180 giorni, pavimentazioni di spazi esterni, aree ludiche, vasche per acque meteoriche - fatte salve le normative di settore), la CILA (art. 6-bis: comunicazione di inizio lavori asseverata da un tecnico abilitato per gli interventi residuali non riconducibili agli articoli 6, 10 e 22, con sanzione di 1.000 euro ridotta di due terzi se spontanea), la SCIA (art. 22: segnalazione certificata di inizio attivita' ex art. 19 legge 241/1990 per manutenzione straordinaria e restauro/risanamento su parti strutturali, ristrutturazione diversa da quella pesante, varianti a permessi) e la SCIA in alternativa al permesso di costruire (art. 23: ristrutturazione pesante e nuova costruzione/ristrutturazione urbanistica in attuazione di piani, con relazione del progettista e termine di trenta giorni prima dell'inizio dei lavori e contributo di costruzione). Use when a technician, designer or citizen must frame which building title applies (free building activity, CILA, SCIA or SCIA alternative to the building permit) under the Italian Testo unico edilizia; it is a documentary aid, does not qualify the specific intervention, does not draft the CILA/SCIA and does not replace the SUE/municipality or regional rules."
license: MIT
area: edilizia-urbanistica-catasto
title: "Edilizia libera, CILA e SCIA (DPR 380/2001 artt. 6, 6-bis, 22, 23)"
summary: "Inquadra i regimi del titolo edilizio diversi dal permesso di costruire (DPR 380/2001): edilizia libera senza titolo (art. 6), CILA asseverata residuale (art. 6-bis), SCIA ex art. 19 L. 241/1990 (art. 22), SCIA in alternativa al PdC con preavviso di 30 giorni (art. 23)."
normative_refs:
  - "D.P.R. 6/6/2001 n. 380 - artt. 6 (attivita' edilizia libera) e 6-bis (CILA)"
  - "D.P.R. 6/6/2001 n. 380 - artt. 22 (SCIA) e 23 (SCIA in alternativa al permesso di costruire)"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-380-2001
  - edilizia
  - titolo-edilizio
  - cila
  - scia
  - edilizia-libera
---

# Edilizia libera, CILA e SCIA (DPR 380/2001 artt. 6, 6-bis, 22, 23)

## Quando usare questa skill

Usala quando devi **inquadrare quale titolo edilizio** si applica a un intervento,
diverso dal **permesso di costruire**, ancorandolo al **DPR 380/2001, Titolo II**:

- **attivita' edilizia libera** - **art. 6**: interventi eseguibili **senza alcun titolo
  abilitativo** (manutenzione ordinaria, eliminazione di **barriere architettoniche** senza
  ascensori esterni/alterazione sagoma, **VEPA**, **tende/pergole**, opere temporanee di
  ricerca geognostica, movimenti di terra agricoli, serre mobili stagionali, **opere
  stagionali fino a 180 giorni**, pavimentazioni/finiture di spazi esterni, aree ludiche,
  vasche per acque meteoriche), **fatte salve** le normative di settore (sismica, sicurezza,
  antincendio, igiene, energia, idrogeologico, beni culturali/paesaggio);
- **CILA** - **art. 6-bis**: gli interventi **non riconducibili** agli artt. 6, 10 e 22 sono
  realizzabili previa **comunicazione di inizio lavori asseverata** da un tecnico abilitato
  (conformita' urbanistica, compatibilita' sismica/energetica, **nessun interessamento delle
  parti strutturali**); **sanzione 1.000 euro** (ridotta di due terzi se spontanea);
- **SCIA** - **art. 22**: **segnalazione certificata di inizio attivita'** (ex **art. 19 L.
  241/1990**) per manutenzione straordinaria e restauro/risanamento **su parti strutturali**,
  **ristrutturazione** diversa da quella "pesante" (art. 10 c. 1 lett. c), **varianti** a
  permessi di costruire;
- **SCIA in alternativa al permesso di costruire** - **art. 23**: **ristrutturazione
  "pesante"** (art. 10 c. 1 lett. c) e **nuova costruzione/ristrutturazione urbanistica** in
  attuazione di **piani attuativi**/strumenti generali con precise disposizioni
  plano-volumetriche; **relazione del progettista** e **termine di 30 giorni** prima
  dell'inizio dei lavori; **contributo di costruzione** (art. 16); efficacia **3 anni**.

**Non e' una skill di qualificazione/redazione**: non decide in concreto la categoria
dell'intervento (art. 3), non redige la CILA/SCIA e non sostituisce il SUE/Comune.

## Cosa NON fa (limiti)

- Non **qualifica in concreto** l'intervento (categoria ex art. 3): rinvio a
  `definizioni-interventi-edilizi-dpr380`.
- Non tratta il **permesso di costruire** (art. 10, 20): skill
  `permesso-costruire-dpr380`.
- Non riproduce il **glossario dell'edilizia libera** (DM 2/3/2018) ne' la **modulistica
  unificata** (skill `modulistica-edilizia-unificata`).
- Non **redige** la CILA/SCIA, l'asseverazione o la relazione del progettista.
- Non tratta le **discipline regionali** (che possono ampliare/ridurre gli ambiti) ne' i
  **vincoli** (paesaggio, sismica): rinvio.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`scegli-titolo-edilizio`](tasks/scegli-titolo-edilizio.md) | Inquadra il regime applicabile (edilizia libera art. 6, CILA art. 6-bis, SCIA art. 22, SCIA alternativa art. 23) a partire dalla categoria dell'intervento (art. 3) |
| [`imposta-scia-alternativa`](tasks/imposta-scia-alternativa.md) | Imposta gli adempimenti della SCIA (art. 22) e della SCIA in alternativa al PdC (art. 23): relazione, termini, contributo, efficacia |

## Riferimenti normativi

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - Titolo II - artt. **6**
  (edilizia libera), **6-bis** (CILA), **22** (SCIA), **23** (SCIA in alternativa al
  permesso di costruire); richiamati gli artt. **3** (definizioni), **10** (PdC), **16**
  (contributo), **37** e **44** (sanzioni) e l'**art. 19 della L. 241/1990**.

Dettaglio in `references/sources.yaml`,
`references/fonti/dpr-380-2001-6-6bis-22-23.md`,
`references/estratti/titoli-edilizi-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione dell'intervento, la scelta del
titolo in concreto, la redazione della CILA/SCIA e delle asseverazioni e il rispetto
delle discipline regionali e dei vincoli restano in capo al **tecnico abilitato** e al
**SUE/Comune**. **Non sostituisce** il tecnico abilitato ne' il SUE/Comune, ne' la
lettura degli artt. 6, 6-bis, 22, 23 del DPR 380/2001.
