---
name: relazione-tecnica-requisiti-minimi-dlgs192
description: "Supporto documentale al progettista e al direttore dei lavori per la relazione tecnica di progetto attestante la rispondenza alle prescrizioni per il contenimento del consumo di energia (la 'relazione ex legge 10'), ai sensi del D.Lgs. 19 agosto 2005, n. 192, art. 8 (con le sanzioni dell'art. 15, commi 1, 3, 4). Use when an engineer or architect (as designer or works director) must frame the energy-compliance technical report, its deposit/asseveration duties and the renewable-energy integration obligations for a building project under D.Lgs. 192/2005 art. 8 and Allegato III of D.Lgs. 199/2021; it is a documentary aid and does NOT draft the report, does NOT perform the energy calculations/verifications (see the minimum-requirements decree DM 26/6/2015), does NOT cover the APE (art. 6), and does NOT replace the designer or the works director."
license: MIT
area: energia-incentivi
title: "Relazione tecnica requisiti minimi energetici (D.Lgs. 192/2005 art. 8)"
summary: "Inquadra la relazione tecnica sui requisiti minimi energetici ('ex legge 10') - D.Lgs. 192/2005 art. 8: chi la redige, deposito, esclusioni, asseverazione del DL, sanzioni. Include gli obblighi FER dell'Allegato III del D.Lgs. 199/2021 modificato dal D.Lgs. 5/2026. Non la redige."
normative_refs:
  - "D.Lgs. 19 agosto 2005, n. 192 - art. 8 (relazione tecnica, accertamenti e ispezioni) e art. 15, commi 1, 3, 4 (sanzioni)"
  - "D.Lgs. 9 gennaio 2026, n. 5 (RED III) - artt. 29-30, che modificano l'Allegato III (obblighi di integrazione delle fonti rinnovabili negli edifici) e l'Allegato IV del D.Lgs. 8 novembre 2021, n. 199"
  - "Rinvio (non riprodotti): DM 26/6/2015 come mod. dal DM MASE 28/10/2025 (requisiti minimi e definizioni), schemi di relazione, DM 37/2008, Allegato II del D.Lgs. 199/2021, art. 6 (APE) e art. 7"
version: 0.2.0-alpha
status: alpha
tags:
  - relazione-tecnica
  - legge-10
  - dlgs-192-2005
  - requisiti-minimi
  - efficienza-energetica
  - fonti-rinnovabili
  - red-iii
---

# Relazione tecnica di rispondenza ai requisiti minimi - ex legge 10 (D.Lgs. 192/2005 art. 8)

## Quando usare questa skill

Usala quando un **ingegnere o architetto** (come **progettista** o **direttore dei lavori**) deve
collocare correttamente la **relazione tecnica di progetto** attestante la **rispondenza alle
prescrizioni per il contenimento del consumo di energia** (la storica **"relazione ex legge 10"**)
in un intervento edilizio/impiantistico, secondo il **D.Lgs. 19 agosto 2005, n. 192, art. 8** (con
le **sanzioni** dell'art. 15):

- **chi** la redige e **cosa** deve contenere (calcoli e verifiche), **quando** e **dove** si
  deposita (art. 8 c. 1);
- le **esclusioni** e la **valutazione dei sistemi alternativi** (cc. 1, 1-bis);
- l'**asseverazione** del direttore dei lavori a fine lavori e i **controlli** del Comune (cc. 2-5);
- il **regime sanzionatorio** per professionista e direttore dei lavori (art. 15 cc. 1, 3, 4).

Per l'**APE** (attestato di prestazione energetica, art. 6) usa
`attestato-prestazione-energetica-dlgs192`; per le **verifiche numeriche** (trasmittanza, requisiti
del DM 26/6/2015) usa `trasmittanza-termica-opache-dm2015`. Questa copre l'**adempimento della
relazione tecnica** (art. 8), non i calcoli.

## Chi la redige, cosa contiene, dove si deposita (art. 8, c. 1)

- **Chi**: il **progettista o i progettisti**, nelle rispettive competenze **edili, impiantistiche
  termotecniche, elettriche e illuminotecniche**, inseriscono i **calcoli e le verifiche** previsti
  dal decreto nella **relazione tecnica di progetto** attestante la **rispondenza** ai requisiti.
- **Deposito**: il **proprietario** (o chi ne ha titolo) la deposita **in doppia copia** presso le
  **amministrazioni competenti**, **contestualmente** alla **dichiarazione di inizio lavori** o alla
  **domanda di titolo abilitativo**.
- **Esclusioni**: adempimenti e relazione **non dovuti** per installazione di **pompa di calore <=
  15 kW** e per **sostituzione del generatore** di calore sotto la soglia del **DM 37/2008**.
- **Schemi**: gli **schemi e le modalita'** di compilazione sono definiti con **decreto MiSE**
  (rinvio; un periodo e' stato abrogato dal D.Lgs. 48/2020), per nuove costruzioni, ristrutturazioni
  importanti e riqualificazioni energetiche.

## Sistemi alternativi ad alta efficienza (art. 8, c. 1-bis)

Per **nuove costruzioni** e **ristrutturazioni importanti**, la relazione include una **valutazione
di fattibilita' tecnica, ambientale ed economica** dei **sistemi alternativi ad alta efficienza**
(fornitura da **fonti rinnovabili**, **cogenerazione**, **teleriscaldamento/teleraffrescamento**,
**pompe di calore**, sistemi di monitoraggio/controllo attivo dei consumi), **documentata** e
disponibile a fini di verifica.

## Obblighi FER negli edifici (Allegato III D.Lgs. 199/2021, modificato dal D.Lgs. 5/2026)

Il **D.Lgs. 9 gennaio 2026, n. 5** (recepimento della direttiva UE 2023/2413, **RED III**) modifica
con l'**art. 29** l'**Allegato III del D.Lgs. 199/2021** con una serie di sostituzioni puntuali, tra
cui l'integrale sostituzione del punto 1 della Sezione A (ambito) e del punto 1 della Sezione B
(quote di copertura). Rileva qui perche' l'Allegato III
stabilisce esso stesso che **calcoli, verifiche e motivazioni si scrivono nella relazione tecnica ex
art. 8, c. 1** (Sezione D punto 1 e Sezione E punto 1).

**Ambito** (Sezione A): edifici di **nuova costruzione**, edifici esistenti oggetto di
**ristrutturazione importante** (primo o secondo livello) e edifici esistenti oggetto di
**ristrutturazione dell'impianto termico**, per i quali la **richiesta del titolo edilizio** e'
presentata **decorsi 180 giorni dall'entrata in vigore** del decreto. Il D.Lgs. 5/2026 non ha un
articolo di entrata in vigore; Normattiva attesta l'entrata in vigore al **4 febbraio 2026**, e 180
giorni dopo cade il **3 agosto 2026**. La formula e' pero' **testualmente ambigua** (e' inserita
dentro l'Allegato III del D.Lgs. 199/2021): vedi
`references/estratti/obblighi-fer-allegato-iii.md`, sezione 1.

**Quote di copertura** (Sezione B punto 1), da rispettare **contemporaneamente** dove ne sono
indicate due:

| Intervento | Quota su ACS | Quota sulla somma |
|---|---|---|
| Nuova costruzione | 60% | 60% di ACS + clim. invernale + clim. estiva |
| Ristrutturazione importante di **primo** livello | 40% | 40% di ACS + clim. invernale + clim. estiva |
| Ristrutturazione importante di **secondo** livello | - | 15% di clim. invernale + clim. estiva |
| Ristrutturazione dell'**impianto termico** | - | 15% di clim. invernale + clim. estiva |

Le ultime due righe sono la **novita' sostanziale**: la ristrutturazione di secondo livello e la
sostituzione/ristrutturazione dell'impianto termico entrano nell'ambito con una quota propria.
Per gli **edifici pubblici** le percentuali sono **maggiorate di 5 punti** e la potenza elettrica FER
obbligatoria e' **incrementata del 10%** (punto 5).

Restano da verificare: divieto di assolvere l'obbligo con **effetto Joule** salvo unita' in **classe
B o superiore** (punto 2); **potenza elettrica FER** minima con k = 0,025 (esistenti) / 0,05 (nuovi)
sulla superficie in pianta (punto 3, formula pubblicata come immagine in Gazzetta); **esonero** per
allaccio a **teleriscaldamento/teleraffrescamento efficiente** a copertura integrale (punto 4);
collocazione degli impianti su edificio o pertinenze, con **esclusione del fotovoltaico a terra**
(Sezione C). In caso di **impossibilita' tecnica o non convenienza economica** la motivazione va
**dettagliata in relazione esaminando tutte le opzioni tecnologiche**, e l'obbligo compensativo su
EP H,C,W,nren scatta **solo** per nuovi edifici e ristrutturazioni importanti di **primo** livello
(Sezione D). Copia della relazione va **trasmessa al GSE** e la verifica e' fatta **dai Comuni su
quella relazione** (Sezione E).

Dettaglio operativo in `references/estratti/obblighi-fer-allegato-iii.md` e nel task
[`verifica-obblighi-fer-edifici`](tasks/verifica-obblighi-fer-edifici.md).

## Asseverazione a fine lavori e controlli (art. 8, cc. 2-5)

- **Asseverazione** (c. 2): a fine lavori il **direttore dei lavori** assevera la **conformita'**
  delle opere (e delle varianti) alla relazione tecnica e l'**attestato di qualificazione energetica
  (AQE)** dell'edificio come realizzato, presentandoli al **Comune** con la **dichiarazione di fine
  lavori**. Senza tale documentazione **asseverata** la **fine lavori e' inefficace** a qualsiasi
  titolo.
- **Conservazione e controlli** (cc. 3-5): il **Comune** conserva copia ed esegue **accertamenti e
  ispezioni** in corso d'opera **o entro cinque anni** dalla fine lavori, anche **su richiesta** di
  committente/acquirente/conduttore (a spese del richiedente).

## Regime e sanzioni (art. 15, cc. 1, 3, 4)

- **Dichiarazione sostitutiva** (c. 1): la relazione tecnica, l'asseverazione e l'AQE (oltre ad APE
  e rapporto di controllo) sono rese in forma di **dichiarazione sostitutiva di atto notorio** (art.
  47 DPR 445/2000).
- **Sanzione al professionista** (c. 3): il professionista che rilascia la **relazione tecnica non
  conforme** agli schemi/modalita' (art. 8, cc. 1 e 1-bis) e' punito con **sanzione da 700 a 4200
  euro** (con comunicazione all'ordine/collegio).
- **Sanzione al direttore dei lavori** (c. 4): il DL che **omette** di presentare al Comune
  l'**asseverazione** e l'AQE prima del rilascio dell'**agibilita'** e' punito con **sanzione da
  1000 a 6000 euro**.

## Cosa NON fa (limiti)

- **Non redige** la relazione tecnica ne' l'asseverazione/AQE; **non esegue** i **calcoli e le
  verifiche** energetiche (rinvio a `trasmittanza-termica-opache-dm2015` e al **DM 26/6/2015**).
- **Non riproduce** gli **schemi di relazione** del decreto attuativo MiSE ne' i requisiti numerici
  del DM 26/6/2015.
- **Non qualifica** l'intervento come ristrutturazione importante di primo o secondo livello o come
  ristrutturazione dell'impianto termico: le definizioni sono nel **DM 26/6/2015** come modificato
  dal **DM MASE 28/10/2025**, richiamate per rinvio e non riprodotte.
- **Non riproduce** l'**Allegato II** del D.Lgs. 199/2021 (requisiti e specifiche tecniche degli
  impianti FER) ne' l'**Allegato IV** (requisiti minimi di prodotto), ne' le **linee guida CTI**
  previste dalla Sezione C punto 4.
- **Non copre** l'**APE** (art. 6, skill dedicata), l'**esercizio degli impianti** (art. 7) ne' i
  commi 2 e 5-10 dell'art. 15 (controlli e sanzioni APE/impianti).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-relazione-deposito`](tasks/inquadra-relazione-deposito.md) | Stabilisce se la relazione tecnica e' dovuta, chi la redige, cosa contiene (incl. sistemi alternativi) e come/quando si deposita (art. 8 cc. 1, 1-bis) |
| [`inquadra-asseverazione-sanzioni`](tasks/inquadra-asseverazione-sanzioni.md) | Inquadra l'asseverazione del DL a fine lavori, i controlli del Comune e le sanzioni a professionista e DL (art. 8 cc. 2-5; art. 15 cc. 1, 3, 4) |
| [`verifica-obblighi-fer-edifici`](tasks/verifica-obblighi-fer-edifici.md) | Stabilisce se e in che misura scattano gli obblighi FER dell'Allegato III del D.Lgs. 199/2021 modificato dal D.Lgs. 5/2026, e cosa deve contenere la relazione tecnica di conseguenza |

## Riferimenti normativi

- **D.Lgs. 19 agosto 2005, n. 192** - **art. 8** (Relazione tecnica, accertamenti e ispezioni):
  cc. 1 (relazione e deposito, esclusioni), 1-bis (sistemi alternativi), 2 (asseverazione del DL a
  fine lavori), 3-5 (conservazione, accertamenti e ispezioni); **art. 15** (Sanzioni): cc. 1
  (dichiarazione sostitutiva), 3 (professionista, 700-4200 euro), 4 (direttore dei lavori, 1000-6000
  euro).
- **D.Lgs. 9 gennaio 2026, n. 5** (attuazione della direttiva UE 2023/2413, RED III), **art. 29**
  (modifiche all'**Allegato III del D.Lgs. 199/2021** - obblighi di integrazione delle fonti
  rinnovabili negli edifici: Sezione A campo di applicazione, Sezione B obblighi, Sezione C
  caratteristiche degli impianti, Sezione D impossibilita' tecnica e non convenienza economica,
  Sezione E modalita' di verifica) e **art. 30** (Allegato IV), pubblicato in **GU Serie generale
  n. 15 del 20 gennaio 2026**.
- Citati come **rinvio** (non riprodotti): **DM 26/6/2015** come modificato dal **DM MASE
  28/10/2025** (requisiti minimi e definizioni di ristrutturazione importante e di ristrutturazione
  dell'impianto termico), **decreto MiSE** con gli **schemi** di relazione, **DM 37/2008** (soglia
  generatore), **Allegato II** del D.Lgs. 199/2021, **D.Lgs. 102/2014** art. 2 c. 2 lett. tt)
  (teleriscaldamento efficiente), **art. 6** (APE), **art. 7** (esercizio impianti), **DPR 445/2000**
  (dichiarazioni sostitutive).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-192-2005-art8-15.md`,
`references/fonti/dlgs-5-2026-allegato-iii.md`,
`references/estratti/relazione-tecnica-checklist.md`,
`references/estratti/obblighi-fer-allegato-iii.md`.

## Avvertenza

Skill di **supporto documentale** per il **tecnico** (progettista, direttore dei lavori): inquadra
l'adempimento della relazione tecnica ex legge 10 e la sua collocazione procedurale. La **redazione**
della relazione, l'esecuzione dei **calcoli/verifiche** e l'**asseverazione** restano responsabilita'
del **progettista** e del **direttore dei lavori**, sul testo vigente dell'art. 8 e del DM 26/6/2015.
La skill **non sostituisce** il progettista, il direttore dei lavori ne' la lettura dell'art. 8 e
dei decreti attuativi.
