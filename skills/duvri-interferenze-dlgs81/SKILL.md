---
name: duvri-interferenze-dlgs81
description: "Supporto documentale agli obblighi del committente nei contratti d'appalto, d'opera o di somministrazione e alla redazione del Documento Unico di Valutazione dei Rischi da Interferenze (DUVRI) ai sensi dell'art. 26 del D.Lgs. 81/2008. Aiuta a impostare la verifica dell'idoneita' tecnico-professionale delle imprese appaltatrici e dei lavoratori autonomi (certificato camerale, autocertificazione ex art. 47 DPR 445/2000 - art. 26 c.1 lett. a), l'informazione sui rischi specifici dell'ambiente e sulle misure di emergenza (c.1 lett. b), la cooperazione e il coordinamento tra i datori di lavoro (c.2), l'elaborazione del DUVRI - unico documento che indica le misure per eliminare o ridurre al minimo i rischi da interferenze, da allegare al contratto e aggiornare in funzione dell'evoluzione dei lavori, con le esclusioni previste (servizi di natura intellettuale, mere forniture, lavori/servizi di durata non superiore a cinque uomini-giorno salvo rischi particolari) e la possibilita' di nominare un incaricato nei settori a basso rischio (c.3, 3-bis), l'indicazione dei costi delle misure di sicurezza da interferenze non soggetti a ribasso (c.5) e gli adempimenti su tessera di riconoscimento (c.8) e responsabilita' solidale. Use when a client/employer must set up the interference-risk management and DUVRI for a service/works/supply contract that is NOT a Title IV construction site; it is a documentary aid and does NOT assess the contractor's own specific risks, does not replace the DVR (art. 28) and does NOT cover construction sites subject to PSC/POS (Titolo IV)."
license: MIT
area: sicurezza-lavoro-cantieri
title: "DUVRI e obblighi negli appalti (art. 26 D.Lgs 81/2008)"
summary: "Obblighi del committente negli appalti e DUVRI (art. 26 D.Lgs 81/2008): idoneita' tecnico-professionale, informazione sui rischi, cooperazione/coordinamento, documento unico rischi da interferenze, costi non ribassabili. Non copre i cantieri Titolo IV (PSC/POS)."
normative_refs:
  - "D.Lgs. 81/2008 art. 26 (obblighi negli appalti e DUVRI)"
version: 0.1.0-alpha
status: alpha
tags:
  - duvri
  - interferenze
  - appalti
  - art-26-dlgs81
  - sicurezza-lavoro
---

# DUVRI e obblighi negli appalti (art. 26 D.Lgs 81/2008)

## Quando usare questa skill

Usala quando, come **datore di lavoro committente** (o suo consulente/RSPP), affidi
**lavori, servizi o forniture** dentro la tua azienda/unita' produttiva o nel ciclo
produttivo e devi gestire i **rischi da interferenza** e redigere il **DUVRI** ai sensi
dell'**art. 26 D.Lgs 81/2008**:

- **verificare l'idoneita' tecnico-professionale** dell'impresa appaltatrice/lavoratore
  autonomo (certificato camerale, autocertificazione ex art. 47 DPR 445/2000) - c.1 a);
- **informare** sui rischi specifici dell'ambiente e sulle misure di emergenza - c.1 b);
- attivare **cooperazione** e **coordinamento** tra i datori di lavoro - c.2;
- **elaborare il DUVRI** (unico documento sui rischi da interferenza), allegarlo al
  contratto e aggiornarlo - c.3;
- indicare i **costi della sicurezza da interferenze**, **non soggetti a ribasso** - c.5.

## Il DUVRI (art. 26 c.3)

- Il **committente** elabora un **unico documento di valutazione dei rischi** che indica
  le misure per **eliminare** o, ove non possibile, **ridurre al minimo i rischi da
  interferenze**; e' **allegato al contratto** e **adeguato in funzione dell'evoluzione**
  dei lavori. Vi accedono **RLS** e organizzazioni sindacali.
- **Non riguarda i rischi specifici propri** dell'attivita' delle imprese appaltatrici o
  dei lavoratori autonomi (quelli restano nel loro DVR).
- **Esclusioni** (c.3-bis): servizi di **natura intellettuale**, **mere forniture** di
  materiali/attrezzature, lavori/servizi di durata **non superiore a cinque uomini-giorno**
  - salvo rischi da agenti cancerogeni, biologici, atmosfere esplosive o rischi particolari.
- Nei **settori a basso rischio** (art. 29 c.6-ter) il committente puo', in alternativa,
  nominare un **incaricato** con adeguata formazione/competenza per sovrintendere a
  cooperazione e coordinamento.

## Costi della sicurezza (c.5)

- Nei contratti (di appalto/subappalto/somministrazione) vanno **indicati i costi delle
  misure adottate per eliminare o ridurre i rischi da interferenza**: tali costi **non
  sono soggetti a ribasso**. Nei contratti pubblici sono quantificati dalla stazione
  appaltante.

## Cosa NON fa (limiti)

- **Non copre i cantieri edili** del **Titolo IV** (per cui valgono **PSC e POS**): vedi
  `pos-allegato-xv-checker`. L'art. 26 riguarda gli appalti "interni" non-cantiere.
- **Non valuta i rischi specifici** propri dell'attivita' dell'appaltatore (restano nel
  suo DVR); non redige il **DVR** del committente (art. 28-29 - vedi `dvr-generico`).
- **Non quantifica tecnicamente** i costi della sicurezza: struttura l'obbligo e le voci,
  la stima resta del committente/stazione appaltante.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-idoneita-e-informazione`](tasks/verifica-idoneita-e-informazione.md) | Imposta la verifica dell'idoneita' tecnico-professionale (c.1 a) e l'informazione sui rischi specifici e sulle misure di emergenza (c.1 b) |
| [`imposta-duvri`](tasks/imposta-duvri.md) | Verifica se il DUVRI e' dovuto (esclusioni c.3-bis), ne struttura i contenuti (rischi da interferenza, misure, aggiornamento) e imposta l'indicazione dei costi non ribassabili (c.5) |

## Riferimenti normativi

- **D.Lgs. 81/2008 art. 26** - obblighi connessi ai contratti d'appalto/d'opera/
  somministrazione: idoneita' tecnico-professionale (c.1), cooperazione e coordinamento
  (c.2), DUVRI ed esclusioni (c.3, 3-bis, 3-ter), costi della sicurezza (c.5), tessera di
  riconoscimento (c.8), responsabilita' solidale.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-81-art-26.md`,
`references/estratti/duvri-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione dei rischi da interferenza, la stima
dei relativi costi e le misure di coordinamento dipendono dal caso concreto e dalla
responsabilita' del datore di lavoro committente e dell'RSPP. La skill **non sostituisce**
il datore di lavoro, l'RSPP ne' il coordinamento tra le imprese.
