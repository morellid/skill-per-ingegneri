---
name: domicilio-digitale-pec-cad
description: "Supporto documentale all'inquadramento del domicilio digitale e dei pubblici elenchi dei domicili digitali (PEC) secondo il Codice dell'amministrazione digitale (D.Lgs. 82/2005). Aiuta a inquadrare l'identita' digitale e il domicilio digitale (art. 3-bis: obbligo per pubbliche amministrazioni, professionisti tenuti all'iscrizione in albi/elenchi e imprese di dotarsi di un domicilio digitale iscritto in INI-PEC o IPA; facolta' per chiunque di eleggere il proprio domicilio digitale in INAD; possibilita' di un domicilio digitale speciale per determinati atti o affari), l'utilizzo del domicilio digitale e i suoi effetti giuridici (art. 6: le comunicazioni ai domicili digitali producono, quanto a spedizione e ricevimento, gli stessi effetti della raccomandata con ricevuta di ritorno ed equivalgono alla notificazione a mezzo posta; notifica diretta degli atti, comprese sanzioni amministrative e atti impositivi), l'Indice nazionale dei domicili digitali delle imprese e dei professionisti - INI-PEC (art. 6-bis, presso il MIMIT), l'Indice dei domicili digitali delle pubbliche amministrazioni e dei gestori di pubblici servizi - IPA (art. 6-ter, gestito da AgID) e l'Indice nazionale dei domicili digitali delle persone fisiche e degli altri enti - INAD (art. 6-quater, gestito da AgID). Use when a professional, firm, public body or citizen must frame the digital domicile (certified e-mail / PEC), which public index applies and the legal effects of communications under the Italian Codice dell'amministrazione digitale; it is a documentary aid, does not elect or register the digital domicile, does not perform notifications and does not replace AgID/MIMIT rules."
license: MIT
area: software-dati-cybersecurity
title: "Domicilio digitale e indici PEC - INAD, INI-PEC, IPA (CAD, D.Lgs. 82/2005)"
summary: "Inquadra il domicilio digitale e gli indici PEC del CAD (D.Lgs. 82/2005): obbligo/facolta' (art. 3-bis), effetti delle comunicazioni - raccomandata A/R e notificazione (art. 6), INI-PEC imprese/professionisti (6-bis), IPA PA (6-ter), INAD persone fisiche (6-quater)."
normative_refs:
  - "D.Lgs. 7/3/2005 n. 82 (CAD) - artt. 3-bis (identita' e domicilio digitale) e 6 (utilizzo ed effetti giuridici)"
  - "D.Lgs. 7/3/2005 n. 82 (CAD) - artt. 6-bis (INI-PEC), 6-ter (IPA), 6-quater (INAD)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-82-2005
  - cad
  - domicilio-digitale
  - pec
  - inad-inipec-ipa
  - amministrazione-digitale
---

# Domicilio digitale e indici PEC - INAD, INI-PEC, IPA (CAD, D.Lgs. 82/2005)

## Quando usare questa skill

Usala quando devi **inquadrare il domicilio digitale** (PEC/servizio elettronico di
recapito qualificato) e i **pubblici elenchi** in cui è iscritto, ancorandoli al **CAD
(D.Lgs. 82/2005)**:

- **identità e domicilio digitale** - **art. 3-bis**: **obbligo** per **PA**, **professionisti
  tenuti all'iscrizione in albi/elenchi** e **imprese** di dotarsi di un domicilio digitale
  iscritto in **INI-PEC** (art. 6-bis) o **IPA** (art. 6-ter) (c. 1); **facoltà** per
  **chiunque** di eleggere il proprio domicilio digitale in **INAD** (art. 6-quater) (c.
  1-bis); modalità di elezione (anche via **ANPR**/ufficio anagrafe, c. 1-ter); **domicilio
  digitale speciale** per determinati atti/affari (c. 4-quinquies);
- **utilizzo ed effetti giuridici** - **art. 6**: le comunicazioni ai domicili digitali degli
  elenchi 6-bis/6-ter/6-quater producono, quanto a **spedizione e ricevimento**, gli **stessi
  effetti della raccomandata A/R** ed **equivalgono alla notificazione a mezzo posta** (c. 1);
  **notifica diretta** degli atti, comprese sanzioni amministrative e atti impositivi (c.
  1-quater);
- **INI-PEC** - **art. 6-bis**: Indice nazionale dei domicili digitali di **imprese e
  professionisti** (presso il MISE/**MIMIT**, gestito tramite le Camere di commercio); i
  domicili ivi inseriti sono **mezzo esclusivo** di comunicazione/notifica con la PA;
- **IPA** - **art. 6-ter**: Indice dei domicili digitali di **PA, gestori di pubblici
  servizi e società a controllo pubblico** (gestito da **AgID**); aggiornamento almeno
  **semestrale**;
- **INAD** - **art. 6-quater**: Indice nazionale dei domicili digitali di **persone fisiche,
  professionisti e altri enti** non tenuti all'iscrizione in INI-PEC (gestito da **AgID**),
  con allineamento all'**ANPR**.

**Non è una skill operativa**: non elegge/registra il domicilio digitale, non effettua
notifiche e non sostituisce le Linee guida AgID.

## Cosa NON fa (limiti)

- Non **elegge/registra** il domicilio digitale né iscrive negli indici (INAD, INI-PEC, IPA).
- Non **effettua notifiche** né attesta la conformità delle copie.
- Non riproduce le **Linee guida AgID** attuative né i decreti (es. DM MISE 19/3/2013 per
  INI-PEC): rinvio.
- Non tratta le **firme elettroniche/il documento informatico** (skill
  `documento-informatico-firme-cad`) né l'**identità digitale SPID/CIE** in dettaglio (artt.
  64/64-bis): citati come rinvio.

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`inquadra-domicilio-digitale`](tasks/inquadra-domicilio-digitale.md) | Determina l'indice competente (INI-PEC, IPA, INAD) e il regime (obbligo/facoltà) del domicilio digitale in base al soggetto (art. 3-bis, 6-bis, 6-ter, 6-quater) |
| [`inquadra-effetti-notifica`](tasks/inquadra-effetti-notifica.md) | Inquadra gli effetti giuridici delle comunicazioni al domicilio digitale e la notifica diretta degli atti (art. 6) |

## Riferimenti normativi

- **D.Lgs. 7 marzo 2005, n. 82** (Codice dell'amministrazione digitale) - artt. **3-bis**
  (identità e domicilio digitale), **6** (utilizzo ed effetti), **6-bis** (INI-PEC),
  **6-ter** (IPA), **6-quater** (INAD); richiamati gli artt. **2**, **18-bis**, **22**,
  **23-bis**, **62** (ANPR), **64/64-bis** (identità digitale) e le **Linee guida AgID**
  (rinvio).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-82-2005-domicilio-digitale.md`,
`references/estratti/domicilio-digitale-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'elezione/registrazione del domicilio digitale, la
scelta dell'indice, l'esecuzione delle notifiche e l'applicazione delle Linee guida
restano in capo al **soggetto interessato**, ai **gestori degli indici** (AgID, MIMIT,
InfoCamere) e alla **PA**. **Non sostituisce** questi soggetti né la lettura degli artt.
3-bis, 6, 6-bis, 6-ter, 6-quater del CAD e delle Linee guida AgID.
