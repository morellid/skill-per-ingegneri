---
name: cra-classificazione-pde
description: Guida la classificazione di un prodotto con elementi digitali (PDE) ai sensi del Regolamento (UE) 2024/2847 (Cyber Resilience Act) e la selezione della procedura di valutazione della conformita' e della documentazione tecnica. Use when an engineer or product compliance manager needs to determine whether a product is in scope of CRA, whether it is "important" (Annex III Class I/II) or "critical" (Annex IV), which conformity assessment module (A, B+C, H, or European cybersecurity certification) applies, and which technical documentation (Annex VII) is required.
license: MIT
area: software-dati-cybersecurity
title: "CRA - Classificazione PDE e valutazione della conformita'"
summary: "Classificazione di un prodotto con elementi digitali (PDE) ai sensi del CRA (default / importante Classe I / Classe II / critico) e selezione del modulo di valutazione della conformita' (A, B+C, H, certificazione europea) + struttura documentazione tecnica Allegato VII"
normative_refs:
  - "Reg. UE 2024/2847 (Cyber Resilience Act)"
version: 0.1.0-alpha
status: alpha
tags:
  - cra
  - reg-ue-2024-2847
  - cyber
---

# CRA - Classificazione PDE e valutazione della conformita'

## Quando usare questa skill

Quando un ingegnere/tecnico (compliance manager, security engineer, product manager con responsabilita' di marcatura CE) deve impostare la **classificazione di un prodotto con elementi digitali (PDE)** ai sensi del **Regolamento (UE) 2024/2847 - Cyber Resilience Act (CRA)**. La skill copre tre aree:

1. Verifica se il prodotto rientra nell'ambito del CRA (Art. 2).
2. Classificazione (default / importante Classe I / importante Classe II / critico) sulla base degli artt. 7-8 e degli Allegati III-IV.
3. Selezione del **modulo di valutazione della conformita'** ammissibile (modulo A, B+C, H, o certificazione europea) ai sensi dell'art. 32 e della **struttura della documentazione tecnica** richiesta (art. 31 + Allegato VII).

Quando NON usarla:
- Prodotti coperti da altri regolamenti settoriali esclusi dal CRA (dispositivi medici Reg. 2017/745 e 2017/746, omologazione veicoli Reg. 2019/2144, aviazione civile Reg. 2018/1139, equipaggiamento marittimo Direttiva 2014/90/UE, sicurezza nazionale/difesa, pezzi di ricambio identici).
- Implementazione tecnica dei requisiti essenziali di cibersicurezza dell'Allegato I (es. progettazione SBOM, politica CVD, hardening). Questa skill aiuta a stabilire **cosa documentare** e **quale procedura seguire**, non a progettare i controlli tecnici.
- Procedure ENISA di certificazione europea (Reg. (UE) 2019/881) viste dall'interno dell'ente certificatore.
- Obblighi di segnalazione vulnerabilita'/incidenti dell'art. 14 (questi richiedono una skill operativa dedicata).

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario** ne' quello del responsabile della conformita' del fabbricante. L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito (dichiarazione di conformita' UE firmata, documentazione tecnica completa) ne' valuta la conformita' di un PDE ai requisiti essenziali dell'Allegato I; il fabbricante (o il suo rappresentante autorizzato) resta unico responsabile della corretta classificazione, della scelta della procedura di valutazione e del contenuto della DoC UE.

La skill si basa sul testo del Regolamento pubblicato in GU UE L del 20/11/2024 (ELI: <http://data.europa.eu/eli/reg/2024/2847/oj>). **Non sostituisce** ne' integra il previsto **atto di esecuzione del 11 dicembre 2025** sulla descrizione tecnica delle categorie dell'Allegato III (art. 7 par. 4) ne' i futuri **atti delegati ex art. 8 par. 1** che individueranno le categorie dell'Allegato IV soggette a certificazione europea obbligatoria. Quando questi atti saranno pubblicati, gli output della skill dovranno essere riletti alla luce delle descrizioni tecniche ufficiali.

## Sotto-attivita' disponibili

Questa skill supporta quattro sotto-attivita'. In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Verifica ambito di applicabilita' del CRA**: quando l'utente chiede "questo prodotto rientra nel CRA?", leggere `tasks/check-ambito-applicabilita.md`.
- **Classificazione del PDE (default / importante Classe I / Classe II / critico)**: quando l'utente conosce le funzionalita' principali del prodotto e chiede a quale categoria appartiene, leggere `tasks/classifica-pde.md`.
- **Scelta del modulo di valutazione della conformita'**: quando l'utente, nota la categoria, chiede quale modulo (A, B+C, H, certificazione UE) sia ammissibile e quando interviene un organismo notificato, leggere `tasks/scegli-procedura-conformita.md`.
- **Checklist della documentazione tecnica (Allegato VII)**: quando l'utente vuole verificare se la documentazione tecnica del prodotto copre i requisiti dell'art. 31 e dell'Allegato VII, leggere `tasks/check-documentazione-tecnica.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera e quali input ha gia' a disposizione (descrizione del prodotto, funzionalita' principali, presenza di norme armonizzate applicate).

## Processo generale

1. Identifica la sotto-attivita' richiesta dall'utente.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input minimi specificati nel task.
4. Applica la procedura citando articoli e allegati del Regolamento (UE) 2024/2847 (estratti in `references/estratti/reg-ue-2024-2847-cra-classificazione.md`).
5. Produci l'output nel formato atteso dal task.
6. Concludi sempre con un rinvio al fabbricante o al professionista firmatario per la responsabilita' finale sulla classificazione e sulla DoC UE.

## Fonti normative

Riferimento unico autoritativo: **Regolamento (UE) 2024/2847 del Parlamento europeo e del Consiglio del 23 ottobre 2024** (regolamento sulla cibersicurezza - Cyber Resilience Act), pubblicato in GU UE L del 20/11/2024. Trascrizione fedele dei capi e allegati rilevanti in `references/fonti/reg-ue-2024-2847-cra.md`. Estratto curato di classificazione e moduli in `references/estratti/reg-ue-2024-2847-cra-classificazione.md`. Riferimenti completi e hash SHA256 in `references/sources.yaml`.

## Limiti

Cosa questa skill NON fa:
- Non produce dichiarazioni di conformita' UE firmate, ne' fascicoli tecnici pronti per la marcatura CE.
- Non valuta tecnicamente la conformita' del PDE ai requisiti essenziali dell'Allegato I (parte I, prodotto; parte II, gestione vulnerabilita').
- Non legge gli atti delegati/di esecuzione attesi ex artt. 7 par. 4 e 8 par. 1 (rispettivamente, descrizione tecnica Allegato III e classi critiche Allegato IV): rinvia alla pubblicazione di tali atti per categorie di confine.
- Non valida la designazione dell'organismo notificato: il fabbricante deve scegliere un organismo notificato attivo (banca dati NANDO della Commissione europea) per il CRA dopo l'11 giugno 2026 (art. 71 par. 2).
- Non si occupa degli obblighi di segnalazione delle vulnerabilita' attivamente sfruttate e degli incidenti gravi (art. 14): questi richiedono procedure operative dedicate (CSIRT coordinatore, ENISA, piattaforma unica di segnalazione art. 16).
- Non sostituisce il giudizio del fabbricante o del professionista firmatario su classificazione, modulo, contenuto della DoC UE e della documentazione tecnica.
- Non e' una guida all'implementazione tecnica della SBOM, della politica CVD o degli aggiornamenti automatici di sicurezza.
- Non valuta la conformita' alle norme armonizzate (presunzione di conformita' ex art. 27): segnala il loro eventuale utilizzo e l'impatto sulla procedura, ma non ne verifica l'applicabilita' al progetto concreto.
- Non interpreta il diritto degli Stati membri sulle sanzioni amministrative ex art. 64.
