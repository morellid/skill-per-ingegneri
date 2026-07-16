---
name: verifiche-periodiche-attrezzature-dlgs81
description: "Supporto documentale al regime dei controlli e delle verifiche periodiche delle attrezzature di lavoro secondo il D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza), art. 71 e Allegato VII. Aiuta a distinguere i controlli delle attrezzature (iniziale, periodico, straordinario, da persona competente, con risultati scritti conservati almeno tre anni - commi 8-10) dalle verifiche periodiche delle sole attrezzature elencate nell'Allegato VII (apparecchi di sollevamento, gru, ponti mobili sviluppabili, generatori di vapore, recipienti e insiemi a pressione), a impostare la prima verifica a cura dell'INAIL entro quarantacinque giorni dalla richiesta (poi, decorso il termine, soggetti pubblici o privati abilitati) e le verifiche successive a libera scelta del datore dalle ASL o dall'ARPA o da soggetti abilitati (comma 11), a inquadrare la qualifica dei soggetti privati abilitati come incaricati di pubblico servizio (comma 12), il rinvio al decreto sulle modalita' - DM 11 aprile 2011 (comma 13), l'effettuazione diretta da parte dei vigili del fuoco per le proprie attrezzature (comma 13-bis) e l'aggiornamento dell'elenco (comma 14), con oneri e conservazione dei verbali a carico del datore di lavoro. Use when an engineer, employer, RSPP, or maintenance manager must set up first and periodic statutory inspections of work equipment (lifting appliances, pressure vessels, steam generators) under Italian D.Lgs. 81/2008 art. 71 and Allegato VII; it is a documentary aid and does NOT carry out the inspections, does NOT draft the reports, does NOT reproduce the Allegato VII frequencies (graphic annex), and does NOT replace INAIL, the ASL/ARPA, the accredited bodies, or the employer."
license: MIT
area: impianti-macchine-prodotti
title: "Verifiche periodiche attrezzature di lavoro (D.Lgs. 81/2008 art. 71)"
summary: "Inquadra controlli e verifiche periodiche delle attrezzature di lavoro (D.Lgs. 81/2008 art. 71 e Allegato VII): controlli da persona competente (verbali 3 anni), prima verifica INAIL entro 45 giorni, successive ASL/ARPA o soggetti abilitati. Non esegue le verifiche."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 (T.U. sicurezza) - art. 71 e Allegato VII"
  - "DM 11 aprile 2011 (modalita' delle verifiche periodiche e abilitazione dei soggetti) (richiamato)"
version: 0.1.0-alpha
status: alpha
tags:
  - verifiche-periodiche
  - attrezzature-di-lavoro
  - dlgs-81-2008
  - allegato-vii
  - inail-asl
---

# Verifiche periodiche delle attrezzature di lavoro (D.Lgs. 81/2008 art. 71 e Allegato VII)

## Quando usare questa skill

Usala quando un **ingegnere, datore di lavoro, RSPP o responsabile della manutenzione** deve
impostare i **controlli** e le **verifiche periodiche** delle **attrezzature di lavoro**
(apparecchi di sollevamento, gru, ponti mobili sviluppabili, generatori di vapore,
recipienti/insiemi a pressione) secondo l'**art. 71 e l'Allegato VII del D.Lgs. 9 aprile 2008,
n. 81**:

- **distinguere** i **controlli** (art. 71, c. 8-10) dalle **verifiche periodiche** delle
  attrezzature dell'**Allegato VII** (c. 11);
- impostare **chi**, **con quali termini** e **a carico di chi** esegue prima verifica e
  verifiche successive.

Per gli **ascensori** usa `verifiche-periodiche-ascensori-dpr162`; per gli **impianti di messa
a terra** usa `verifiche-messa-a-terra-dpr462`; per la **conformita' PED** delle attrezzature a
pressione usa `ped-classificazione-conformita`.

## Due regimi da non confondere

- **Controlli** (art. 71, c. 8-10): riguardano **tutte** le attrezzature la cui sicurezza
  dipende dall'installazione o soggette a deterioramento; sono a cura del datore secondo le
  indicazioni del **fabbricante** / **norme di buona tecnica**, eseguiti da **persona
  competente**; i risultati vanno **per iscritto** e **conservati almeno tre anni** (c. 9); per
  l'uso fuori sede occorre il documento dell'**ultimo controllo con esito positivo** (c. 10).
- **Verifiche periodiche** (art. 71, c. 11): riguardano **solo** le attrezzature elencate
  nell'**Allegato VII**, con la **frequenza indicata nel medesimo allegato**, e coinvolgono
  **soggetti pubblici** (INAIL, ASL/ARPA) **o privati abilitati**.

## Verifiche periodiche: chi, quando, a carico di chi (art. 71, c. 11-14)

- **Prima verifica**: a cura dell'**INAIL**, entro **quarantacinque giorni** dalla richiesta;
  decorso inutilmente il termine, il datore puo' avvalersi di **altri soggetti pubblici o
  privati abilitati**.
- **Verifiche successive**: a **libera scelta** del datore, dalle **ASL** (o **ARPA** dove
  previsto da legge regionale) o da **soggetti pubblici/privati abilitati**.
- **Oneri**: verifiche a **titolo oneroso**, spese a **carico del datore di lavoro**; i
  **verbali** vanno conservati e tenuti a disposizione dell'organo di vigilanza.
- **Soggetti privati abilitati** (c. 12): sono **incaricati di pubblico servizio**. Le
  **modalita'** delle verifiche e i **criteri di abilitazione** sono fissati con **decreto**
  (**DM 11 aprile 2011**) (c. 13). Il **Corpo nazionale dei vigili del fuoco** puo' effettuare
  direttamente le verifiche sulle proprie attrezzature (c. 13-bis). L'**elenco** dell'Allegato
  VII e' aggiornato con decreto (c. 14).

## Cosa NON fa (limiti)

- **Non riproduce l'Allegato VII** (elenco delle attrezzature soggette e periodicita' delle
  verifiche): su Normattiva e' **"Parte di provvedimento in formato grafico"** e va **letto
  sull'atto** e sul **DM 11/4/2011**. Stesso pattern onesto di Tabella A (D.Lgs. 222/2016),
  Allegato I (DPR 151/2011) e art. 8 del DM 236/1989.
- **Non esegue** le verifiche ne' i controlli, **non redige** i verbali e **non sostituisce**
  INAIL, ASL/ARPA, i soggetti abilitati ne' il datore di lavoro.
- **Non tratta** i requisiti di conformita' delle attrezzature (art. 70, Allegato V) se non
  come richiamo, ne' la formazione degli operatori (Accordo Stato-Regioni).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-regime-attrezzatura`](tasks/inquadra-regime-attrezzatura.md) | Stabilisce se un'attrezzatura e' soggetta a soli controlli (art. 71 c. 8-10) o anche a verifiche periodiche dell'Allegato VII (c. 11) |
| [`imposta-verifiche-periodiche`](tasks/imposta-verifiche-periodiche.md) | Imposta prima verifica (INAIL, 45 giorni) e verifiche successive (ASL/ARPA/abilitati), oneri, conservazione dei verbali |

## Riferimenti normativi

- **D.Lgs. 9 aprile 2008, n. 81** (T.U. sicurezza) - **art. 71** (Obblighi del datore di
  lavoro): commi 8-10 (controlli, verbali conservati 3 anni), 11 (verifiche periodiche
  Allegato VII: prima verifica INAIL a 45 giorni, successive ASL/ARPA/abilitati, oneri), 12
  (soggetti privati abilitati incaricati di pubblico servizio), 13 (rinvio al decreto), 13-bis
  (VVF), 14 (aggiornamento elenco); **Allegato VII** (elenco attrezzature e periodicita', in
  formato grafico).
- **DM 11 aprile 2011** (modalita' di effettuazione delle verifiche periodiche e criteri di
  abilitazione dei soggetti) - **richiamato**, non riprodotto.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-81-2008-art71-allegatoVII.md`,
`references/estratti/verifiche-attrezzature-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'esecuzione delle verifiche e dei controlli, la redazione
dei verbali e la valutazione di conservazione/efficienza restano responsabilita' di **INAIL**,
**ASL/ARPA**, dei **soggetti abilitati** e del **datore di lavoro**, sull'Allegato VII e sul DM
11/4/2011 vigenti. La skill **non sostituisce** tali soggetti ne' la lettura dell'art. 71,
dell'Allegato VII e del DM 11 aprile 2011.
