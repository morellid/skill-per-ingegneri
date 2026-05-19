---
name: dm37-2008-dichiarazione-conformita
description: Supporta la compilazione e verifica della Dichiarazione di Conformita' (DdC) degli impianti tecnologici ai sensi del DM 22/01/2008 n. 37. Verifica completezza del modello Allegato I (7 categorie impianti a-g), determina gli allegati obbligatori (relazione materiali sempre; schema impianto sempre; progetto da professionista sopra soglie Art. 5). Use when an Italian installer or engineer needs to compile, check, or review a Dichiarazione di Conformita' for building systems (electrical, heating, gas, plumbing, fire protection, etc.) under DM 37/2008. Target users are installatori abilitati, ingegneri/periti, responsabili tecnici di imprese installatrici, collaudatori.
license: MIT
area: impianti-macchine-prodotti
title: "DM 37/2008 - Dichiarazione Conformita' Impianti"
summary: "Compilazione e verifica della Dichiarazione di Conformita' (DdC) degli impianti tecnologici (7 categorie a-g modello Allegato I), determinazione degli allegati obbligatori e dell'obbligo di progetto da professionista ex Art. 5"
normative_refs:
  - "DM 22/1/2008 n. 37"
version: 0.1.2-alpha
status: alpha
tags:
  - dm-37-2008
  - impianti
  - didc
---

# DM 37/2008 - Dichiarazione di Conformita' impianti

## Quando usare questa skill

Usare quando un installatore, ingegnere o responsabile tecnico chiede di:
- **Verificare una DdC gia' redatta**: controllare che il modello Allegato I sia compilato in tutti i campi obbligatori e che gli allegati richiesti siano presenti
- **Determinare gli allegati obbligatori**: sapere quali documenti devono essere allegati alla DdC in base alla categoria di impianto (a-g) e alle dimensioni/potenza
- **Verificare l'obbligo di progetto**: determinare se per l'impianto in questione era obbligatoria la progettazione da professionista ai sensi dell'Art. 5 (in ogni caso serve un elaborato tecnico minimo)
- **Classificare l'impianto**: identificare sotto quale categoria (a-g) ricade l'impianto e quali regole si applicano

**Non usare** se l'utente chiede:
- Progettare l'impianto (dimensionamento elettrico, calcolo carichi termici, ecc.)
- Verifiche periodiche messa a terra DPR 462/2001 (skill separata)
- Pratiche SUAP o autorizzazioni comunali (fuori scope DM 37/2008)
- Verifiche di conformita' antincendio DM 3/8/2015 per impianti cat. g) (skill dedicata)

## Avvertenza

Questa skill e' uno strumento di supporto alla compilazione e verifica della Dichiarazione di Conformita'. **Non sostituisce il giudizio del responsabile tecnico firmatario ne' la verifica in campo dell'impianto.** La DdC attesta la conformita' dell'impianto alle regole dell'arte; la skill verifica la completezza formale del documento, non la correttezza tecnica dell'impianto. La responsabilita' per la veridicita' dei contenuti della DdC resta esclusivamente in capo all'installatore firmatario (Art. 7 co. 4 DM 37/2008).

## Sotto-attivita' disponibili

- **Verifica completezza DdC**: l'utente chiede "e' completa la DdC?", "mancano campi?", "cosa devo controllare nel modello?" -> leggi [`tasks/verifica-completezza-ddc.md`](tasks/verifica-completezza-ddc.md)
- **Identifica allegati obbligatori**: l'utente chiede "cosa devo allegare?", "serve lo schema impianto?", "c'era obbligo di progetto?" -> leggi [`tasks/identifica-allegati-obbligatori.md`](tasks/identifica-allegati-obbligatori.md)

Se la richiesta e' generica ("compila/verifica questa DdC"), esegui prima identificazione allegati, poi verifica completezza.

## Processo generale

1. Determina la categoria di impianto (a-g, Art. 1 DM 37/2008)
2. Verifica le soglie dimensionali/potenza per capire se progetto da professionista era obbligatorio (Art. 5); in ogni caso e' necessario uno schema/elaborato tecnico
3. Carica il task file corrispondente alla sotto-attivita' richiesta
4. Applica la procedura e produci il report con citazioni normative precise
5. Concludi sempre con rinvio al responsabile tecnico firmatario

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM 22 gennaio 2008 n. 37, Art. 1, 3, 4, 5, 7 e Allegato I
- Normattiva - testo consolidato vigente DM 37/2008

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non verifica la correttezza tecnica dell'impianto (sezione cavi, portata termica, ecc.)
- Non calcola i parametri di progetto (potenza installata, carichi, ecc.)
- Non produce la DdC firmata o il modello compilato in PDF
- Non verifica l'iscrizione CCIAA dell'installatore in tempo reale
- Non conosce requisiti aggiuntivi regionali o comunali specifici
- Non sostituisce il sopralluogo del responsabile tecnico o del collaudatore
- Non interpreta il DPR 380/2001 (edilizia) in combinato con DM 37/2008
