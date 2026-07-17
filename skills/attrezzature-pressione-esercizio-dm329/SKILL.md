---
name: attrezzature-pressione-esercizio-dm329
description: "Supporto documentale alla messa in servizio e alle verifiche delle attrezzature e degli insiemi a pressione in esercizio (fase post-marcatura CE) secondo il D.M. 1 dicembre 2004, n. 329. Aiuta a inquadrare il campo di applicazione e i tipi di verifica (primo impianto/messa in servizio, periodiche, riqualificazione periodica, riparazione/modifica - art. 1), la verifica obbligatoria di messa in servizio quando l'attrezzatura è installata e assemblata dall'utilizzatore, con attestazione ed eventuale divieto di messa in servizio in caso di esito negativo (art. 4), le esclusioni dal controllo della messa in servizio (art. 5), la dichiarazione di messa in servizio da inviare all'ISPESL (oggi INAIL) e alla ASL con i suoi contenuti - elenco attrezzature, relazione tecnica e schema, dichiarazione di conformità al manuale d'uso, verbale della verifica, componenti in scorrimento viscoso o fatica oligociclica - e la dichiarazione cumulativa per le attrezzature in serie GPL e criogeniche (art. 6), la riqualificazione periodica con la classificazione per categorie, le verifiche di integrità e di funzionamento e la periodicità delle tabelle degli allegati A e B, riducibile su indicazione del fabbricante (art. 10), le esenzioni dalla riqualificazione periodica per soglie di pressione e prodotto pressione-volume (art. 11) e la verifica di funzionamento con il controllo degli accessori di sicurezza e la taratura delle valvole di sicurezza (art. 13). Use when an engineer, employer, or user must set up the messa in servizio or the periodic requalification of pressure equipment in service under Italian D.M. 329/2004; it is a documentary aid and does NOT perform the verifications, does NOT draft the dichiarazione di messa in servizio, does NOT reproduce the periodicity tables of annexes A and B, and does NOT replace the user/employer, the verifying body (INAIL/ASL/authorized bodies), or the manufacturer."
license: MIT
area: impianti-macchine-prodotti
title: "Attrezzature a pressione: messa in servizio e verifiche (DM 329/2004)"
summary: "Messa in servizio e verifiche delle attrezzature/insiemi a pressione in esercizio (DM 329/2004): verifica di primo impianto (art. 4), dichiarazione a INAIL/ASL (art. 6), riqualificazione periodica ed esenzioni (artt. 10-11), verifica di funzionamento. Non esegue le verifiche."
normative_refs:
  - "D.M. 1 dicembre 2004, n. 329 - artt. 1, 4, 5, 6, 10, 11, 13"
  - "Richiamati: D.Lgs. 25 febbraio 2000, n. 93 (PED, allegato II); D.Lgs. 311/1991; allegati A e B (periodicità); DM 11 aprile 2011 (verifiche periodiche attrezzature ex D.Lgs. 81/2008 art. 71)"
version: 0.1.0-alpha
status: alpha
tags:
  - attrezzature-a-pressione
  - messa-in-servizio
  - riqualificazione-periodica
  - dm-329-2004
  - inail
---

# Attrezzature a pressione in esercizio: messa in servizio e verifiche (D.M. 329/2004)

## Quando usare questa skill

Usala quando un **ingegnere, datore di lavoro o utilizzatore** deve impostare la **messa in
servizio** o la **riqualificazione periodica** di **attrezzature e insiemi a pressione in
esercizio** (fase **post-marcatura CE**), secondo il **D.M. 1 dicembre 2004, n. 329**:

- individuare **cosa rientra** e **quali verifiche** si applicano;
- impostare la **verifica di messa in servizio** e la **dichiarazione di messa in servizio**;
- inquadrare la **riqualificazione periodica** (integrità + funzionamento), la **periodicità** e le
  **esenzioni**.

> Questa skill copre la **fase di esercizio** (DM 329/2004), **distinta** dalla **marcatura CE** di
> immissione sul mercato (D.Lgs. 93/2000, direttiva PED): per la classificazione e la conformità
> dell'attrezzatura nuova vedi `ped-classificazione-conformita`. Per le **verifiche periodiche
> delle attrezzature di lavoro** ex art. 71 D.Lgs. 81/2008 vedi
> `verifiche-periodiche-attrezzature-dlgs81`.

> **Nota istituzionale**: l'**ISPESL** citato nel testo storico è **soppresso**; le sue funzioni
> sono oggi attribuite all'**INAIL** (D.L. 78/2010).

## Campo di applicazione e tipi di verifica (art. 1)

- **Ambito** (c. 1): attrezzature/insiemi a pressione ex **D.Lgs. 93/2000**; attrezzature
  **preesistenti al 29/5/2002** (omologate ISPESL o da classificare); **recipienti semplici** ex
  D.Lgs. 311/1991.
- **Verifiche** (c. 2): **primo impianto/messa in servizio**; **periodiche**; **riqualificazione
  periodica**; **riparazione o modifica**.

## Verifica di messa in servizio (art. 4) ed esclusioni (art. 5)

- **Quando** (art. 4, c. 1): dovuta **solo se** l'attrezzatura/insieme è **installato e assemblato
  dall'utilizzatore** sull'impianto; su **richiesta** dell'azienda utilizzatrice (c. 2).
- **Esito**: **attestazione** dei risultati; in caso di **esito negativo**, **divieto di messa in
  servizio** (c. 3); **temporanea messa in funzione** ammessa ai soli fini della verifica (c. 4).
- **Esclusioni** (art. 5): attrezzature già escluse dall'art. 2; **estintori portatili** e bombole
  per respiratori; **recipienti semplici** con PS ≤ 12 bar e PS·V < 8000 bar·l; **insiemi** con
  verifiche di accessori già effettuate da organismo notificato/ispettorato.

## Dichiarazione di messa in servizio (art. 6)

- **A chi**: l'utilizzatore la invia all'**ISPESL (oggi INAIL)** e alla **USL/ASL** (c. 1).
- **Contenuto** (c. 1): elenco attrezzature (pressione, temperatura, capacità, fluido); relazione
  tecnica con schema d'impianto; dichiarazione di **installazione conforme al manuale d'uso**;
  verbale della **verifica art. 4** ove prescritta; elenco componenti in **scorrimento viscoso** /
  **fatica oligociclica**.
- **Dichiarazione cumulativa** per attrezzature in serie (**GPL ≤ 13 m³**; **criogenici ≤ 35 m³**),
  semestrale (c. 2); **accessori** seguono l'attrezzatura protetta (c. 3); per gli **esclusi** ex
  art. 5, consente l'attivazione con attestazione dell'utilizzatore (c. 4).

## Riqualificazione periodica (art. 10) ed esenzioni (art. 11)

- **Cosa** (c. 1-2): classificazione per **categorie** (all. II D.Lgs. 93/2000); comprende
  **verifiche di integrità** (art. 12) e **di funzionamento** (art. 13).
- **Periodicità** (c. 3): nelle **tabelle degli allegati A e B**; **ridotta** se il fabbricante
  indica intervalli inferiori (corrosione/erosione). Accessori con la **stessa periodicità** (c. 4).
  **Deroghe/ispezioni alternative** equivalenti previa **autorizzazione del Ministero** (c. 5).
- **Esenzioni** (art. 11): soglie di **PS** e **PS·V** per fluidi del gruppo 2, recipienti
  frigoriferi, vapore autoproduttori/non, generatori di acetilene, estintori portatili, ecc.

## Verifica di funzionamento (art. 13)

- **Rispondenza** dell'uso effettivo alla **dichiarazione di messa in servizio**/istruzioni del
  fabbricante (c. 1 lett. a);
- **Funzionalità degli accessori di sicurezza** (prove a banco/simulazioni/in opera); per le
  **valvole di sicurezza**, accertamento della **taratura** entro i limiti del fabbricante e delle
  periodicità di riqualificazione (c. 1 lett. b).

## Cosa NON fa (limiti)

- **Non esegue** le verifiche (primo impianto, riqualificazione, funzionamento) né rilascia
  attestazioni/verbali: le eseguono **INAIL/ASL** o i **soggetti abilitati**.
- **Non redige** la **dichiarazione di messa in servizio** né la relazione tecnica di impianto.
- **Non riproduce** le **tabelle di periodicità (allegati A e B)** né gli articoli non trascritti
  (artt. 2, 3, 12): rinvia all'atto, agli allegati e al **manuale d'uso** del fabbricante.
- **Non sostituisce** l'utilizzatore/datore di lavoro, il soggetto verificatore né il fabbricante;
  non tratta la **marcatura CE** (→ `ped-classificazione-conformita`).

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`imposta-messa-in-servizio`](tasks/imposta-messa-in-servizio.md) | Verifica se è dovuta la verifica di messa in servizio (art. 4/5) e compone i contenuti della dichiarazione di messa in servizio (art. 6) |
| [`imposta-riqualificazione-periodica`](tasks/imposta-riqualificazione-periodica.md) | Inquadra la riqualificazione periodica (integrità + funzionamento), la periodicità (allegati A/B) e le esenzioni (art. 11) |

## Riferimenti normativi

- **D.M. 1 dicembre 2004, n. 329** - **art. 1** (campo di applicazione, tipi di verifica), **art. 4**
  (verifica di primo impianto/messa in servizio), **art. 5** (esclusioni), **art. 6** (dichiarazione
  di messa in servizio), **art. 10** (riqualificazione periodica), **art. 11** (esenzioni), **art. 13**
  (verifica di funzionamento).
- **Richiamati** (non riprodotti): **D.Lgs. 25 febbraio 2000, n. 93** (PED, allegato II categorie),
  **D.Lgs. 311/1991** (recipienti semplici), **allegati A e B** (periodicità), artt. **2, 3, 12**;
  **DM 11 aprile 2011** e **art. 71 D.Lgs. 81/2008** per le verifiche periodiche delle attrezzature
  di lavoro (→ `verifiche-periodiche-attrezzature-dlgs81`).

Dettaglio in `references/sources.yaml`, `references/fonti/dm-329-2004-artt-1-4-5-6-10-11-13.md`,
`references/estratti/attrezzature-pressione-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: le **verifiche**, la **dichiarazione di messa in servizio** e la
gestione dell'esercizio restano responsabilità dell'**utilizzatore/datore di lavoro**, del
**soggetto verificatore** (INAIL/ASL/soggetti abilitati) e del **fabbricante**, sul testo vigente
del D.M. 329/2004 e dei suoi allegati. La skill **non sostituisce** tali soggetti né la lettura
degli articoli e delle tabelle di periodicità.
