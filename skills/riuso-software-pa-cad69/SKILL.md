---
name: riuso-software-pa-cad69
description: "Supporto documentale all'obbligo di riuso e rilascio in open source del software delle pubbliche amministrazioni: analisi comparativa nell'acquisizione (art. 68 C.A.D.) e obbligo di rendere disponibile il codice sorgente completo di documentazione, in repertorio pubblico sotto licenza aperta e in uso gratuito ad altre PA (art. 69 C.A.D.), con le Linee guida operative AgID su acquisizione e riuso. Aiuta a impostare la valutazione comparativa tra le soluzioni (software sviluppato ad hoc, riuso di software di altre PA, software libero/open source, cloud, proprietario - art. 68), a gestire il rilascio sotto licenza aperta (scelta della licenza, materiali da rilasciare, organizzazione del repository), a predisporre la documentazione a corredo richiesta dalle Linee guida (file README.md con i contenuti obbligatori MUST/SHOULD, documentazione tecnica in formato versionabile riga per riga, esclusi ODT/DOCX/PDF), a rispettare i tempi di rilascio (entro 15 giorni dall'acquisizione se non si adotta il modello di sviluppo aperto) e a registrare il software su Developers Italia tramite il file publiccode.yml pubblicato nella root del repository. Use when a public administration or its supplier must comply with the software reuse/open-source release obligations of the Italian CAD and prepare the accompanying documentation (README, publiccode.yml, licence) per the AgID guidelines; it is a documentary aid and does NOT choose the licence for you, does not reproduce the full field-by-field publiccode.yml schema (a Developers Italia technical standard) and does not perform the technical comparative evaluation."
license: MIT
area: software-dati-cybersecurity
title: "Riuso e rilascio open source del software PA (C.A.D. artt. 68-69)"
summary: "Obbligo di riuso e rilascio open source del software PA: analisi comparativa (art. 68 C.A.D.), rilascio del codice sotto licenza aperta (art. 69), documentazione AgID (README, tempi 15gg, publiccode.yml su Developers Italia). Non sceglie la licenza ne' compila i campi."
normative_refs:
  - "D.Lgs. 82/2005 (C.A.D.) artt. 68 (analisi comparativa) e 69 (riuso e standard aperti)"
  - "AgID - Linee guida su acquisizione e riuso di software per le PA (Allegato A)"
version: 0.1.0-alpha
status: alpha
tags:
  - riuso-software-pa
  - cad-art-69
  - open-source-pa
  - publiccode-yml
  - developers-italia
---

# Riuso e rilascio open source del software PA (art. 68-69 C.A.D. + Linee guida AgID)

## Quando usare questa skill

Usala quando una **pubblica amministrazione** (o un suo **fornitore**) deve rispettare
gli obblighi del **Codice dell'Amministrazione Digitale (C.A.D.)** su **acquisizione,
riuso e rilascio in open source** del software e predisporre la **documentazione a
corredo** richiesta dalle **Linee guida AgID**:

- impostare l'**analisi comparativa** tra le soluzioni prima di acquisire (art. 68);
- gestire l'**obbligo di rilascio** del codice sorgente sotto **licenza aperta**, in
  repertorio pubblico, in uso gratuito ad altre PA (art. 69);
- preparare **README.md**, **documentazione tecnica** e **publiccode.yml**;
- rispettare i **tempi di rilascio** e **registrare** il software su **Developers Italia**.

## Art. 68 - analisi comparativa (acquisizione)

La PA acquisisce software previa **valutazione comparativa tecnico-economica** tra:
(a) software sviluppato per suo conto; (b) **riuso** di software di altre PA; (c)
**software libero/open source**; (d) software in **cloud**; (e) software **proprietario**
(licenza d'uso). Principi: economicita', efficienza, tutela degli investimenti, **riuso**,
neutralita' tecnologica.

## Art. 69 - obbligo di riuso e rilascio

Le PA titolari di software realizzato **su specifiche indicazioni del committente
pubblico** hanno l'**obbligo di rendere disponibile il codice sorgente completo di
documentazione**, **rilasciato in repertorio pubblico sotto licenza aperta**, in **uso
gratuito** ad altre PA/soggetti che intendano adattarlo, salvo motivate ragioni di
ordine e sicurezza pubblica, difesa nazionale e consultazioni elettorali.

## Documentazione a corredo (Linee guida AgID, Allegato A)

- **README.md** (A.7): contenuti obbligatori (MUST) - titolo/sottotitolo, descrizione
  estesa e casi d'uso, prerequisiti e dipendenze, istruzioni di installazione, stato del
  progetto, detentori del copyright (l'Amministrazione committente), manutentori, **e-mail
  per le segnalazioni di sicurezza** (non via issue tracker pubblico); vari SHOULD (CI,
  code coverage, Docker...).
- **Documentazione tecnica** (A.8): MUST allegare la documentazione per installare
  dipendenze/ambiente, compilare e installare in produzione, comprendere l'architettura;
  in **formato versionabile riga per riga** (HTML, Markdown, reStructuredText, LaTeX):
  **ODT/DOCX/PDF non ammessi**.
- **Tempi di rilascio** (A.9): se non si adotta il **modello di sviluppo aperto**, il
  rilascio deve avvenire **entro 15 giorni** dall'acquisizione/collaudo/produzione (MUST).
- **Registrazione su Developers Italia** (A.11): pubblicare un file **`publiccode.yml`**
  nella **root** del repository (rilevato dal crawler per generare la scheda nel catalogo)
  e registrare l'organizzazione di code-hosting.

## Cosa NON fa (limiti)

- **Non sceglie la licenza** aperta al posto tuo: inquadra l'obbligo e i criteri, la
  scelta e la validazione legale restano dell'Amministrazione.
- **Non riproduce il formato campo-per-campo del `publiccode.yml`** (standard tecnico di
  Developers Italia, richiamato dalle Linee guida): rinvia alla documentazione ufficiale
  del formato.
- **Non esegue la valutazione comparativa tecnica** (art. 68) ne' redige il codice/la
  documentazione: struttura obblighi e contenuti.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`imposta-analisi-comparativa`](tasks/imposta-analisi-comparativa.md) | Imposta la valutazione comparativa tecnico-economica tra le soluzioni dell'art. 68 (sviluppo ad hoc, riuso, open source, cloud, proprietario) |
| [`prepara-rilascio-open-source`](tasks/prepara-rilascio-open-source.md) | Struttura il rilascio ex art. 69: licenza aperta, README.md e documentazione (formati ammessi), tempi (15 gg), registrazione su Developers Italia via publiccode.yml |

## Riferimenti normativi

- **D.Lgs. 82/2005 (C.A.D.)** - **art. 68** (analisi comparativa delle soluzioni) e
  **art. 69** (riuso delle soluzioni e standard aperti).
- **AgID** - **Linee guida su acquisizione e riuso di software per le PA** (adottate ex
  art. 71 C.A.D.), in particolare l'**Allegato A** (README, documentazione, tempi,
  publiccode.yml, registrazione su Developers Italia).

Dettaglio in `references/sources.yaml`, `references/fonti/riuso-software-pa.md`,
`references/estratti/riuso-software-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la scelta della licenza, la valutazione comparativa e
la validazione della documentazione restano responsabilita' dell'Amministrazione e del
suo fornitore. La skill **non sostituisce** il RTD, il consulente legale ne' la lettura
delle Linee guida AgID e della documentazione del formato publiccode.yml.
