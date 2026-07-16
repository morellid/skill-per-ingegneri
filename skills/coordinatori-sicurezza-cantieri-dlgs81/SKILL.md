---
name: coordinatori-sicurezza-cantieri-dlgs81
description: "Supporto documentale al regime dei cantieri temporanei o mobili e al ruolo dei coordinatori per la sicurezza secondo il D.Lgs. 9 aprile 2008, n. 81, Titolo IV, artt. 89-92. Aiuta a inquadrare le definizioni (cantiere, committente, responsabile dei lavori, coordinatore per la progettazione - CSP, coordinatore per l'esecuzione - CSE, con le relative incompatibilita' - art. 89), gli obblighi del committente o del responsabile dei lavori (designazione del CSP contestualmente all'incarico di progettazione e del CSE prima dell'affidamento quando e' prevista la presenza di piu' imprese esecutrici anche non contemporanea; verifica dell'idoneita' tecnico-professionale con l'allegato XVII, DURC e patente a crediti ex art. 27; notifica preliminare ex art. 99; sospensione dell'efficacia del titolo abilitativo in assenza di PSC, fascicolo, notifica o DURC; esonero per lavori privati non soggetti a permesso e sotto 100.000 euro - art. 90), gli obblighi del CSP (redazione del piano di sicurezza e coordinamento ex art. 100 e allegato XV e del fascicolo ex allegato XVI - art. 91) e gli obblighi del CSE (verifica dell'applicazione del PSC e dei POS, coordinamento, contestazione e proposta di sospensione, sospensione diretta delle lavorazioni in caso di pericolo grave e imminente - art. 92). Use when an engineer, client (committente), works manager, or safety coordinator must frame roles, appointments, and duties on an Italian Title IV construction site under D.Lgs. 81/2008 artt. 89-92; it is a documentary aid and does NOT appoint the coordinators, does NOT draft the PSC/POS/fascicolo, does NOT reproduce the annexes, and does NOT replace the client, the CSP, the CSE, or the supervisory authority."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Coordinatori sicurezza cantieri Titolo IV (D.Lgs. 81/2008 artt. 89-92)"
summary: "Inquadra i cantieri Titolo IV (D.Lgs. 81/2008 artt. 89-92): quando nominare CSP e CSE (piu' imprese), obblighi del committente (idoneita', notifica preliminare, sospensione del titolo), PSC e fascicolo del CSP, vigilanza e sospensione del CSE. Non nomina i coordinatori."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 (T.U. sicurezza) - Titolo IV, artt. 89, 90, 91, 92"
  - "Articoli/allegati richiamati: art. 98 (requisiti coordinatori), art. 99 (notifica), art. 100 (PSC), allegati X, XV, XVI, XVII (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - cantieri-temporanei-mobili
  - coordinatore-sicurezza
  - csp-cse
  - dlgs-81-2008
  - psc-fascicolo
---

# Coordinatori sicurezza e obblighi del committente nei cantieri (D.Lgs. 81/2008 Tit. IV)

## Quando usare questa skill

Usala quando un **ingegnere, committente, responsabile dei lavori o coordinatore per la
sicurezza** deve inquadrare **ruoli, nomine e obblighi** in un **cantiere temporaneo o mobile**
(Titolo IV) secondo gli **artt. 89-92 del D.Lgs. 9 aprile 2008, n. 81**:

- stabilire **quando** vanno nominati **CSP** e **CSE**;
- inquadrare gli **obblighi del committente/responsabile dei lavori**, del **CSP** e del **CSE**.

Per la **compilazione/verifica del POS** usa `pos-allegato-xv-checker`; per gli **appalti NON di
cantiere** (art. 26, DUVRI) usa `duvri-interferenze-dlgs81`. Questa skill copre la **gestione del
cantiere Titolo IV** (committente, coordinatori, PSC/fascicolo).

## Soggetti e definizioni (art. 89)

- **Cantiere**: luogo di **lavori edili o di ingegneria civile** dell'**allegato X**.
- **Committente** (per conto del quale l'opera e' realizzata; per l'opera pubblica il titolare
  del potere decisionale/di spesa), eventuale **responsabile dei lavori**, **CSP**, **CSE**,
  **imprese affidatarie/esecutrici**, **lavoratori autonomi**.
- **Incompatibilita' del CSE**: non puo' essere il **datore di lavoro** delle imprese
  affidatarie/esecutrici, un suo dipendente o il suo **RSPP** (salvo coincidenza
  committente-impresa esecutrice).

## Quando nominare CSP e CSE (art. 90, c. 3-8, 11)

- **Presenza di piu' imprese esecutrici** (anche **non contemporanea**): il committente/
  responsabile dei lavori **designa il CSP** contestualmente all'incarico di progettazione e il
  **CSE** prima dell'affidamento, entrambi con i **requisiti dell'art. 98**.
- Vale anche se, dopo l'affidamento a **un'unica impresa**, i lavori sono affidati a **piu'
  imprese** (c. 5).
- **Esonero** (c. 11): per **lavori privati non soggetti a permesso** e **< 100.000 euro** non si
  applica il c. 3 (le funzioni del CSP le svolge il CSE).

## Verifiche del committente e sospensione del titolo (art. 90, c. 9-10)

- **Idoneita' tecnico-professionale** (allegato XVII); per cantieri **< 200 uomini-giorno** senza
  rischi dell'allegato XI basta **iscrizione CCIAA + DURC + autocertificazione**.
- **Organico medio annuo** e **CCNL**; **patente a crediti** ex art. 27 o **SOA**.
- **Notifica preliminare** ex art. 99 all'amministrazione concedente.
- **Sospensione dell'efficacia del titolo abilitativo** (c. 10) in assenza di **PSC**, **fascicolo**,
  **notifica** o **DURC** quando previsti; l'organo di vigilanza comunica l'inadempienza.

## Obblighi del CSP (art. 91)

- Prima della richiesta delle offerte: **redige il PSC** (art. 100, contenuti allegato XV) e
  **predispone il fascicolo** (allegato XVI; non dovuto per manutenzione ordinaria). Valuta il
  rischio da **ordigni bellici inesplosi** negli scavi.

## Obblighi del CSE (art. 92)

- **Verifica** l'applicazione del **PSC** e l'idoneita'/coerenza dei **POS**; **adegua** PSC e
  fascicolo all'evoluzione dei lavori.
- **Coordina** cooperazione, coordinamento e informazione reciproca.
- **Contestazione e proposta di sospensione** al committente/responsabile dei lavori (inosservanze
  artt. 94-97 e PSC); in caso di inerzia, comunica ad **ASL** e **ITL**.
- **Sospensione diretta** delle **singole lavorazioni** in caso di **pericolo grave e imminente**.

## Cosa NON fa (limiti)

- **Non nomina** i coordinatori ne' verifica i loro **requisiti** (art. 98).
- **Non redige** il **PSC**, il **POS** ne' il **fascicolo**, e **non riproduce** gli allegati (X,
  XV, XVI, XVII): rinvia agli atti e a `pos-allegato-xv-checker`.
- **Non sostituisce** il committente, il CSP, il CSE ne' l'organo di vigilanza; non tratta gli
  obblighi delle imprese/lavoratori (artt. 95-97) se non come richiamo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-obbligo-coordinatori`](tasks/verifica-obbligo-coordinatori.md) | Stabilisce se vanno nominati CSP e CSE (piu' imprese anche non contemporanee), con l'esonero per lavori privati < 100.000 euro |
| [`obblighi-committente-cantiere`](tasks/obblighi-committente-cantiere.md) | Imposta le verifiche del committente (idoneita', DURC, patente, notifica preliminare) e i casi di sospensione del titolo abilitativo |

## Riferimenti normativi

- **D.Lgs. 9 aprile 2008, n. 81** (T.U. sicurezza) - **Titolo IV**: **art. 89** (definizioni),
  **art. 90** (obblighi del committente/responsabile dei lavori: nomina CSP/CSE, verifica
  idoneita', notifica, sospensione del titolo, esonero < 100.000 euro), **art. 91** (obblighi
  del CSP: PSC + fascicolo), **art. 92** (obblighi del CSE: vigilanza, contestazione, sospensione).
- Articoli/allegati **richiamati** (non riprodotti): **art. 98** (requisiti dei coordinatori),
  **art. 99** (notifica preliminare), **art. 100** (PSC), **allegati X, XV, XVI, XVII**, **art. 27**
  (patente a crediti), **artt. 94-97** (obblighi imprese/lavoratori).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-81-2008-titolo4-artt-89-92.md`,
`references/estratti/coordinatori-cantieri-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la **nomina** dei coordinatori, la **redazione** di PSC/POS/
fascicolo e la **vigilanza** in cantiere restano responsabilita' del **committente**, del **CSP**,
del **CSE** e degli **organi di vigilanza**, sul testo vigente del Titolo IV. La skill **non
sostituisce** tali soggetti ne' la lettura degli artt. 89-92 e degli allegati richiamati.
