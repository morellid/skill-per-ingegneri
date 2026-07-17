---
name: sottoprodotti-end-of-waste-dlgs152
description: "Supporto documentale all'inquadramento del sottoprodotto (art. 184-bis) e della cessazione della qualifica di rifiuto - End of Waste (art. 184-ter) del D.Lgs. 152/2006 (Codice dell'ambiente), Parte IV. Aiuta a distinguere quando una sostanza od oggetto è un sottoprodotto e non un rifiuto verificando le quattro condizioni cumulative dell'art. 184-bis (origine da un processo di produzione di cui è parte integrante e non scopo primario; certezza dell'utilizzo nello stesso o in un successivo processo; utilizzo diretto senza trattamento diverso dalla normale pratica industriale; utilizzo legale con requisiti di prodotto, salute e ambiente e nessun impatto negativo) e quando un rifiuto cessa di essere tale dopo un'operazione di recupero soddisfacendo le condizioni dell'art. 184-ter (scopi specifici, mercato o domanda, requisiti tecnici e standard di prodotto, nessun impatto negativo), con i criteri fissati da regolamenti UE o caso per caso con decreto ministeriale, le autorizzazioni degli articoli 208, 209 e 211 e del titolo III-bis con parere ISPRA/ARPA in mancanza di criteri, il registro RECER e il Nucleo End of Waste (NEW). Use when a technician, producer, waste manager or environmental consultant must frame whether a material is a by-product or has ceased to be waste (End of Waste) under the Italian Environmental Code; it is a documentary aid, does not classify the specific material, does not reproduce the ministerial criteria decrees and does not replace the competent authority or ISPRA/ARPA."
license: MIT
area: ambiente-territorio-mobilita
title: "Sottoprodotti ed End of Waste (D.Lgs. 152/2006 artt. 184-bis, 184-ter)"
summary: "Inquadra sottoprodotto (art. 184-bis D.Lgs. 152/2006) ed End of Waste (art. 184-ter): le 4 condizioni del sottoprodotto, la cessazione della qualifica di rifiuto dopo recupero, i criteri UE/DM, le autorizzazioni 208/209/211 con parere ISPRA/ARPA, registro RECER e Nucleo NEW."
normative_refs:
  - "D.Lgs. 3/4/2006 n. 152 - art. 184-bis (Sottoprodotto: quattro condizioni cumulative, criteri con DM)"
  - "D.Lgs. 3/4/2006 n. 152 - art. 184-ter (Cessazione della qualifica di rifiuto/End of Waste: condizioni, criteri, autorizzazioni, RECER, NEW)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-152-2006
  - rifiuti
  - sottoprodotto
  - end-of-waste
  - economia-circolare
  - ambiente
---

# Sottoprodotti ed End of Waste (D.Lgs. 152/2006 artt. 184-bis, 184-ter)

## Quando usare questa skill

Usala quando devi **distinguere un rifiuto** da un **sottoprodotto** o stabilire se un
rifiuto ha **cessato di essere tale (End of Waste)**, ancorandolo al **D.Lgs. 152/2006,
Parte IV**:

- **sottoprodotto** - **art. 184-bis**: una sostanza od oggetto **è un sottoprodotto e non
  un rifiuto** (ai sensi dell'art. 183 c. 1 lett. a) solo se soddisfa **tutte e quattro**
  le condizioni **cumulative** del c. 1:
  - **a)** è **originato da un processo di produzione** di cui costituisce **parte
    integrante** e il cui **scopo primario non** è produrlo;
  - **b)** è **certo** che sarà **utilizzato** nello stesso o in un successivo processo, dal
    produttore o da terzi;
  - **c)** può essere **utilizzato direttamente** senza **alcun ulteriore trattamento**
    diverso dalla **normale pratica industriale**;
  - **d)** l'**ulteriore utilizzo è legale** (requisiti di prodotto, salute e ambiente,
    nessun impatto complessivo negativo);
  - criteri qualitativi/quantitativi per specifiche tipologie con **DM** (c. 2);
- **cessazione della qualifica di rifiuto (End of Waste)** - **art. 184-ter**: un rifiuto
  **cessa di essere tale** quando è stato sottoposto a un'**operazione di recupero** e
  soddisfa i **criteri** che rispettano le condizioni del c. 1 (**a** scopi specifici, **b**
  mercato/domanda, **c** requisiti tecnici e standard di prodotto, **d** nessun impatto
  negativo);
  - i criteri sono fissati da **regolamenti UE** o, in mancanza, **caso per caso** con **DM**
    (c. 2);
  - in **mancanza di criteri**, tramite le **autorizzazioni** artt. **208/209/211** e Titolo
    III-bis, con **parere obbligatorio e vincolante di ISPRA/ARPA** (c. 3);
  - **comunicazioni** e **controlli a campione** (cc. 3-bis, 3-ter), registro **RECER** (c.
    3-septies), computo per gli **obiettivi di recupero/riciclaggio** (c. 4), applicazione
    della disciplina rifiuti **fino alla cessazione** (c. 5), requisiti **REACH** per il
    primo utilizzatore (c. 5-bis) e **Nucleo End of Waste - NEW** dal 1° gennaio 2026 (c.
    5-ter).

**Non è una skill di classificazione/redazione**: non decide in concreto se un materiale è
sottoprodotto o EoW, non riproduce i DM di criterio e non sostituisce l'autorità
competente o ISPRA/ARPA.

## Cosa NON fa (limiti)

- Non **classifica in concreto** un materiale come sottoprodotto o End of Waste: inquadra le
  condizioni di legge.
- Non riproduce i **decreti ministeriali** di criterio (c. 2) né i **regolamenti UE** per
  tipologia (es. DM 264/2016 sottoprodotti; regolamenti/DM EoW): rinvio.
- Non riproduce l'**art. 183** (definizioni di rifiuto/produttore) né gli **artt.
  208/209/211** (autorizzazioni): citati come rinvio.
- Non **redige** la dichiarazione di conformità (art. 184-ter c. 3 lett. e) né l'istanza
  autorizzativa.
- Non tratta il **deposito temporaneo** e la **classificazione HP** dei rifiuti (skill
  `deposito-classificazione-rifiuti-dlgs152`) né il **trasporto/FIR**
  (`trasporto-rifiuti-fir-dlgs152`).

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`verifica-sottoprodotto`](tasks/verifica-sottoprodotto.md) | Verifica le quattro condizioni cumulative del sottoprodotto (art. 184-bis c. 1 a-d) e inquadra il rinvio ai criteri con DM (c. 2) |
| [`inquadra-end-of-waste`](tasks/inquadra-end-of-waste.md) | Inquadra la cessazione della qualifica di rifiuto (art. 184-ter): operazione di recupero, condizioni, criteri UE/DM, autorizzazioni con parere ISPRA/ARPA, RECER e NEW |

## Riferimenti normativi

- **D.Lgs. 3 aprile 2006, n. 152** (Norme in materia ambientale) - Parte IV - **art.
  184-bis** (Sottoprodotto) e **art. 184-ter** (Cessazione della qualifica di rifiuto);
  richiamati l'art. **183** (definizioni), gli artt. **208/209/211** (autorizzazioni), il
  Titolo III-bis, la **direttiva 2008/98/CE** e i **DM** di criterio (rinvio).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-152-2006-184bis-184ter.md`,
`references/estratti/sottoprodotti-eow-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione in concreto di un materiale come
sottoprodotto o End of Waste, la scelta della procedura (criteri UE/DM o autorizzazione) e
la relativa istruttoria restano in capo al **produttore/detentore**, all'**autorità
competente** e a **ISPRA/ARPA**. **Non sostituisce** l'autorità competente, ISPRA/ARPA né
la lettura degli artt. 184-bis e 184-ter del D.Lgs. 152/2006 e dei decreti di criterio.
