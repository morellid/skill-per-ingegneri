---
name: fascicolo-opera-manutenzione-dlgs81
description: "Supporto documentale al coordinatore per la sicurezza in fase di progettazione (CSP) e al committente per la predisposizione, l'aggiornamento e la verifica di completezza del Fascicolo con le caratteristiche dell'opera secondo il D.Lgs 81/2008, art. 91 comma 1 lettera b) e Allegato XVI. Aiuta a inquadrare: la titolarita' e il ciclo di vita del fascicolo (predisposto la prima volta dal CSP, modificato in fase esecutiva dal CSE ex art. 92, aggiornato dal committente a seguito delle modifiche nella vita dell'opera; accompagna l'opera per tutta la sua durata; non e' predisposto per i lavori di manutenzione ordinaria ex art. 3 comma 1 lettera a del DPR 380); la struttura in tre capitoli (Capitolo I descrizione sintetica dell'opera e soggetti coinvolti, scheda I; Capitolo II individuazione dei rischi e delle misure preventive e protettive in dotazione dell'opera e ausiliarie per gli interventi successivi prevedibili come le manutenzioni ordinarie e straordinarie, schede II-1, II-2 e II-3; Capitolo III riferimenti alla documentazione di supporto esistente, schede III-1, III-2 e III-3); la distinzione tra misure in dotazione dell'opera (incorporate o a servizio dell'opera, come linee vita, ganci, parapetti permanenti) e misure ausiliarie (richieste ai datori di lavoro e ai lavoratori autonomi dei lavori successivi, come ponteggi, trabattelli, DPI anticaduta); i sette elementi da considerare (accessi ai luoghi di lavoro; sicurezza dei luoghi di lavoro; impianti di alimentazione e scarico; approvvigionamento e movimentazione materiali; approvvigionamento e movimentazione attrezzature; igiene sul lavoro; interferenze e protezione dei terzi); e le informazioni sulle modalita' operative per utilizzare le misure in sicurezza e mantenerle nel tempo (verifiche, interventi manutentivi e periodicita'). Use when a safety coordinator (CSP/CSE) or the client must draft, update or check the completeness of the Fascicolo dell'opera under the Italian D.Lgs 81/2008 art. 91 and Allegato XVI; it is a documentary aid, does NOT design the actual measures (linee vita, ganci) nor replace the coordinator, and is distinct from the PSC and the POS."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Fascicolo dell'opera (D.Lgs 81/2008 art. 91 + Allegato XVI)"
summary: "Inquadra la predisposizione e verifica del Fascicolo dell'opera (D.Lgs 81/2008 art. 91 + Allegato XVI): titolarita' (CSP/CSE/committente), struttura in 3 capitoli (opera e soggetti; rischi e misure in dotazione/ausiliarie per interventi successivi; documentazione) e 7 elementi."
normative_refs:
  - "D.Lgs 81/2008 - art. 91 c.1 lett. b) e Allegato XVI: il CSP predispone il fascicolo, il CSE lo adegua (art. 92), il committente lo aggiorna; non per manutenzione ordinaria (art. 3 DPR 380)"
  - "D.Lgs 81/2008 - Allegato XVI: 3 capitoli (opera/soggetti scheda I; rischi e misure in dotazione/ausiliarie per interventi successivi schede II; documentazione schede III); 7 elementi"
version: 0.1.0-alpha
status: alpha
tags:
  - fascicolo-opera
  - sicurezza-cantieri
  - coordinatore-sicurezza
  - dlgs-81-2008
  - manutenzione
---

# Fascicolo dell'opera (D.Lgs 81/2008 art. 91 + Allegato XVI)

## Quando usare questa skill

Usala quando un **coordinatore per la sicurezza in fase di progettazione (CSP)**, un **CSE** o il **committente** deve
**predisporre**, **aggiornare** o **verificare la completezza** del **Fascicolo con le caratteristiche dell'opera**
secondo il **D.Lgs 81/2008**, **art. 91 comma 1 lett. b)** e **Allegato XVI**:

- **titolarità e ciclo di vita** del fascicolo (CSP, CSE, committente; validità per tutta la vita dell'opera);
- **struttura** in tre capitoli e relative schede (I, II-1/2/3, III-1/2/3);
- distinzione tra **misure in dotazione dell'opera** e **misure ausiliarie** e i **7 elementi** da analizzare;
- informazioni per **utilizzare le misure in sicurezza** e **mantenerle nel tempo**.

È un **supporto documentale**: inquadra la struttura e i contenuti del fascicolo; **non** lo redige al posto del
coordinatore né **progetta** le misure concrete (linee vita, ganci). È **distinta** da
`psc-piano-sicurezza-coordinamento-dlgs81` (PSC, Allegato XV) e da `pos-allegato-xv-checker` (POS).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-struttura-e-schede-fascicolo` | Titolarità/ciclo di vita (artt. 91-92, Introduzione) e struttura in 3 capitoli con le schede I, II-1/2/3, III-1/2/3 |
| `imposta-misure-per-interventi-successivi` | Capitolo II: distinzione misure in dotazione/ausiliarie, i 7 elementi, informazioni per l'uso in sicurezza e la manutenzione nel tempo |

## Punti chiave (dal testo di legge)

- **Titolarità/ciclo di vita**: il **CSP predispone** il fascicolo (art. 91 c.1 lett. b), il **CSE lo adegua** (art.
  92 c.1 lett. b), il **committente lo aggiorna** nella vita dell'opera. **Non** per la **manutenzione ordinaria**
  (art. 3 c.1 lett. a DPR 380). **Accompagna l'opera per tutta la sua durata di vita**.
- **Struttura** (Allegato XVI, 3 capitoli): **Cap. I** descrizione opera + soggetti (scheda I); **Cap. II** rischi e
  misure per gli **interventi successivi prevedibili** (manutenzioni), schede II-1/II-2/II-3; **Cap. III** riferimenti
  alla **documentazione** di supporto (schede III-1/2/3).
- **Misure in dotazione dell'opera** (incorporate/a servizio — es. linee vita, ganci, parapetti permanenti) vs
  **misure ausiliarie** (richieste ai datori/lavoratori autonomi dei lavori successivi — es. ponteggi, DPI anticaduta).
- **7 elementi** (Cap. II): accessi; sicurezza dei luoghi; impianti alimentazione/scarico; approvvigionamento/
  movimentazione materiali; approvvigionamento/movimentazione attrezzature; igiene; interferenze e protezione dei terzi.
- **Scheda II-3**: per ciascuna misura in dotazione, informazioni per l'**uso in sicurezza**, il **controllo di
  efficienza** e la **manutenzione** (verifiche, interventi, **periodicità**).

## Fonti

- **D.Lgs 9 aprile 2008 n. 81** - **art. 91-92 e Allegato XVI** - Testo coordinato Edizione gennaio 2025 (INL), SHA256
  `f593e18...`, estratto con `pdftotext`. Edizione INL non ufficiale: per uso autoritativo cross-checkare su
  Normattiva/Gazzetta Ufficiale.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il fascicolo al posto del coordinatore né **progetta** le misure concrete (linee vita/ganci — norme
  UNI di buona tecnica); non compila le schede.
- **Non tratta** il **PSC** (art. 100 + Allegato XV, → skill `psc-piano-sicurezza-coordinamento-dlgs81`), il **POS**
  (Allegato XV punto 3.2, → skill `pos-allegato-xv-checker`), i **ruoli/obblighi** di CSP/CSE (artt. 89-92, → skill
  `coordinatori-sicurezza-cantieri-dlgs81`) né la **notifica preliminare** (art. 99).
- **Non** sostituisce il coordinatore firmatario del fascicolo.

**La skill è un supporto documentale: non sostituisce il coordinatore per la sicurezza firmatario del fascicolo né la lettura dell'art. 91 e dell'Allegato XVI del D.Lgs 81/2008.**
