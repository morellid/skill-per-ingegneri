---
name: deposito-classificazione-rifiuti-dlgs152
description: "Supporto documentale alla classificazione dei rifiuti e al deposito temporaneo prima della raccolta secondo il D.Lgs. 3 aprile 2006, n. 152, Parte quarta, artt. 183, 184 e 185-bis. Aiuta a inquadrare le definizioni (rifiuto, produttore, detentore, gestione, raccolta, deposito temporaneo, sottoprodotto - art. 183), a classificare i rifiuti secondo l'origine in urbani e speciali e secondo la pericolosita' in pericolosi e non pericolosi, con l'elenco europeo dei rifiuti (allegato D, vincolante per i pericolosi), l'attribuzione dei codici a cura del produttore sulla base delle linee guida e il divieto di declassificazione per diluizione o miscelazione (art. 184), e a impostare il deposito temporaneo prima della raccolta nel luogo di produzione con i relativi limiti (avvio a recupero o smaltimento con cadenza almeno trimestrale, oppure al raggiungimento di 30 metri cubi di cui al massimo 10 metri cubi di rifiuti pericolosi; se sotto tale limite all'anno il deposito non puo' durare piu' di un anno), il raggruppamento per categorie omogenee e l'esonero dall'autorizzazione (art. 185-bis). Use when an engineer, waste producer, or environmental consultant must classify a waste (urban/special, hazardous/non-hazardous) or set up a temporary storage before collection under Italian D.Lgs. 152/2006 artt. 183/184/185-bis; it is a documentary aid and does NOT assign the EER codes, does NOT reproduce the EER list or the hazard annexes, does NOT draft registers or the FIR, and does NOT replace the producer/holder or the consultant."
license: MIT
area: ambiente-territorio-mobilita
title: "Classificazione e deposito temporaneo dei rifiuti (D.Lgs. 152/2006)"
summary: "Inquadra classificazione dei rifiuti (urbani/speciali, pericolosi/non pericolosi - art. 184) e deposito temporaneo (art. 185-bis: cadenza trimestrale o 30 mc di cui max 10 pericolosi, durata max 1 anno, senza autorizzazione) - D.Lgs. 152/2006. Non attribuisce i codici EER."
normative_refs:
  - "D.Lgs. 3 aprile 2006, n. 152 - Parte quarta, artt. 183, 184, 185-bis"
  - "Elenco europeo dei rifiuti (EER, allegato D), allegato I (caratteristiche di pericolo HP), Linee guida SNPA di classificazione (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - classificazione-rifiuti
  - deposito-temporaneo
  - dlgs-152-2006
  - rifiuti-pericolosi
  - codici-eer
---

# Classificazione e deposito temporaneo dei rifiuti (D.Lgs. 152/2006 artt. 183-185-bis)

## Quando usare questa skill

Usala quando un **ingegnere, produttore di rifiuti o consulente ambientale** deve **classificare
un rifiuto** o impostare il **deposito temporaneo prima della raccolta**, secondo la **Parte
quarta del D.Lgs. 3 aprile 2006, n. 152**, artt. **183, 184, 185-bis**:

- inquadrare le **definizioni** (rifiuto, produttore, detentore, deposito temporaneo,
  sottoprodotto);
- **classificare** il rifiuto (urbano/speciale, pericoloso/non pericoloso);
- impostare **condizioni, limiti e tempi** del deposito temporaneo.

Per il **trasporto e il FIR** usa `trasporto-rifiuti-fir-dlgs152`; per le **terre e rocce da
scavo** usa `terre-rocce-scavo-dpr120`; per la **bonifica** usa `bonifica-siti-contaminati-dlgs152`.
Questa skill copre **classificazione** e **deposito temporaneo**.

## Definizioni (art. 183)

- **Rifiuto**: sostanza od oggetto di cui il detentore **si disfi** o abbia l'intenzione/obbligo
  di disfarsi. Rilevano **produttore**, **detentore**, **gestione**, **raccolta**, **deposito
  temporaneo**, **sottoprodotto** e la nozione di **rifiuto urbano** (lett. b-ter).

## Classificazione (art. 184)

- **Secondo l'origine**: **urbani** (art. 183, lett. b-ter) e **speciali** (agricoli; da
  **costruzione e demolizione**; industriali; artigianali; commerciali; da servizi; da
  recupero/smaltimento e depurazione; sanitari; **veicoli fuori uso**).
- **Secondo la pericolosita'**: **pericolosi** (caratteristiche dell'**allegato I**) / **non
  pericolosi**.
- **Codici EER** (c. 5): l'**elenco dei rifiuti (allegato D)** e' **vincolante** per i pericolosi;
  la **corretta attribuzione dei codici** e delle caratteristiche di pericolo e' a **cura del
  produttore**, sulla base delle **Linee guida** (SNPA).
- **Divieto di declassificazione** (c. 5-ter): non da pericoloso a non pericoloso tramite
  **diluizione o miscelazione**.

## Deposito temporaneo prima della raccolta (art. 185-bis)

- **Dove** (c. 1): nel **luogo di produzione** (l'intera area dell'attivita' che ha prodotto i
  rifiuti); regole particolari per **responsabilita' estesa del produttore** (lett. b) e per i
  rifiuti da **costruzione e demolizione** (lett. c).
- **Tempi/quantita'** (c. 2 lett. b), **a scelta del produttore**: avvio a recupero/smaltimento
  con **cadenza almeno trimestrale** (a prescindere dalle quantita'), **oppure** al raggiungimento
  di **30 metri cubi**, di cui **al massimo 10 metri cubi di pericolosi**. Se il quantitativo
  **non supera** tale limite **all'anno**, il deposito **non puo' durare piu' di un anno**.
- **Come** (c. 2 lett. a, c, d): **norme tecniche** di stoccaggio/imballaggio; **categorie
  omogenee**; per i pericolosi, norme sullo stoccaggio e **etichettatura**; POP ex Reg. (CE)
  850/2004.
- **Autorizzazione** (c. 3): il deposito temporaneo alle condizioni dei commi 1 e 2 **non
  necessita di autorizzazione**.

## Cosa NON fa (limiti)

- **Non attribuisce i codici EER** ne' esegue la **caratterizzazione analitica**: rinvia
  all'**allegato D**, all'**allegato I** e alle **Linee guida** (SNPA).
- **Non redige** registri di carico/scarico (art. 190), formulari/**FIR** (art. 193) ne'
  MUD/dichiarazioni: per il trasporto vedi `trasporto-rifiuti-fir-dlgs152`.
- **Non sostituisce** il **produttore/detentore** ne' il consulente; non tratta le
  **autorizzazioni** alla gestione (artt. 208 e ss.) se non come richiamo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`classifica-rifiuto`](tasks/classifica-rifiuto.md) | Classifica il rifiuto per origine (urbano/speciale) e pericolosita' (pericoloso/non pericoloso), con il rinvio all'EER e alle linee guida |
| [`imposta-deposito-temporaneo`](tasks/imposta-deposito-temporaneo.md) | Imposta condizioni, limiti (30/10 mc, trimestrale, 1 anno) e modalita' del deposito temporaneo prima della raccolta |

## Riferimenti normativi

- **D.Lgs. 3 aprile 2006, n. 152** (Parte quarta) - **art. 183** (definizioni), **art. 184**
  (classificazione: urbani/speciali, pericolosi/non pericolosi, EER allegato D, attribuzione dei
  codici a cura del produttore, divieto di declassificazione), **art. 185-bis** (deposito
  temporaneo prima della raccolta: luogo, limiti 30/10 mc, cadenza trimestrale, durata max 1 anno,
  categorie omogenee, esonero da autorizzazione).
- **Richiamati** (non riprodotti): **elenco europeo dei rifiuti (EER, allegato D)**, **allegato I**
  (caratteristiche di pericolo HP), **Linee guida SNPA** di classificazione, artt. **190** (registri),
  **193** (FIR), **208 e ss.** (autorizzazioni).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-152-2006-artt-183-184-185bis.md`,
`references/estratti/rifiuti-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la **classificazione** con l'attribuzione dei codici EER e la
**caratterizzazione**, nonche' la gestione del deposito, restano responsabilita' del
**produttore/detentore** e del consulente, sul testo vigente della Parte quarta del D.Lgs.
152/2006 e sulle Linee guida. La skill **non sostituisce** tali soggetti ne' la lettura degli
artt. 183/184/185-bis e degli allegati richiamati.
