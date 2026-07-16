---
name: documento-informatico-firme-cad
description: "Supporto documentale al valore giuridico del documento informatico e delle firme elettroniche secondo il Codice dell'amministrazione digitale (D.Lgs. 7 marzo 2005, n. 82), artt. 20, 21 e 24. Aiuta a stabilire quando un documento informatico soddisfa il requisito della forma scritta e ha l'efficacia probatoria dell'articolo 2702 del Codice civile (quando vi e' apposta una firma digitale, una firma elettronica qualificata o avanzata, o e' formato con identificazione informatica dell'autore attraverso un processo con i requisiti AgID ex articolo 71) e quando invece la sua idoneita' e il valore probatorio sono liberamente valutabili in giudizio (art. 20, comma 1-bis), con la presunzione di riconducibilita' al titolare del dispositivo di firma qualificata o digitale (comma 1-ter); a riconoscere gli atti che a pena di nullita' richiedono firma qualificata o digitale (scritture private ex art. 1350, numeri da 1 a 12, del Codice civile; atto pubblico informatico - art. 21) e i requisiti della firma digitale (riferimento univoco al soggetto e al documento, sostituzione di sigilli e timbri, certificato qualificato non scaduto, revocato o sospeso, con equiparazione a mancata sottoscrizione in caso di certificato revocato - art. 24). Use when an engineer or professional must frame the legal value of a digitally signed document, a PEC, a telematic filing, or an electronic signature type under the Italian CAD (D.Lgs. 82/2005 artt. 20/21/24); it is a documentary aid and does NOT reproduce the AgID technical guidelines or eIDAS, does NOT apply or verify signatures, and does NOT replace the professional, the notary, or the judge."
license: MIT
area: software-dati-cybersecurity
title: "Documento informatico e firme elettroniche (CAD artt. 20, 21, 24)"
summary: "Inquadra il valore giuridico del documento informatico e delle firme elettroniche (CAD, D.Lgs. 82/2005 artt. 20, 21, 24): forma scritta ed efficacia ex art. 2702 c.c., atti nulli senza firma qualificata/digitale, requisiti della firma digitale. Non appone ne' verifica firme."
normative_refs:
  - "D.Lgs. 7 marzo 2005, n. 82 (CAD) - artt. 20, 21, 24"
  - "Linee guida AgID (art. 71 CAD) e Reg. UE 910/2014 (eIDAS) - regole tecniche (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - documento-informatico
  - firma-digitale
  - firma-elettronica
  - cad-dlgs-82-2005
  - valore-probatorio
---

# Documento informatico e firme elettroniche: valore giuridico (CAD artt. 20, 21, 24)

## Quando usare questa skill

Usala quando un **ingegnere o professionista** deve inquadrare il **valore giuridico** di un
**documento informatico** (es. un elaborato firmato digitalmente, un PDF firmato, un atto in
formato digitale, un deposito telematico) e i **tipi di firma elettronica**, secondo gli **artt.
20, 21 e 24 del Codice dell'amministrazione digitale** (D.Lgs. 7 marzo 2005, n. 82):

- stabilire se il documento **soddisfa la forma scritta** e con quale **efficacia probatoria**;
- riconoscere gli **atti nulli** senza firma qualificata/digitale;
- verificare i **requisiti** della **firma digitale** e del **certificato**.

Per gli **obblighi di riuso/rilascio del software** delle PA (CAD artt. 68-69) usa
`riuso-software-pa-cad69`. Questa skill copre il **documento informatico e le firme** (artt. 20-24).

## Valore giuridico del documento informatico (art. 20)

- **Forma scritta + efficacia art. 2702 c.c.** (c. 1-bis): il documento informatico soddisfa il
  **requisito della forma scritta** e ha l'**efficacia probatoria della scrittura privata (art.
  2702 c.c.)** quando vi e' apposta una **firma digitale**, altra **firma elettronica
  qualificata** o **avanzata**, **oppure** e' formato - previa **identificazione informatica**
  dell'autore - con un **processo** avente i requisiti **AgID (art. 71)** che garantisca
  **sicurezza, integrita', immodificabilita'** e riconducibilita' all'autore.
- **Altri casi**: l'idoneita' alla forma scritta e il valore probatorio sono **liberamente
  valutabili in giudizio** (in relazione a sicurezza, integrita', immodificabilita').
- **Data e ora** opponibili ai terzi se apposte **in conformita' alle Linee guida**.
- **Presunzione** (c. 1-ter): l'uso del dispositivo di **firma qualificata o digitale** si
  **presume riconducibile al titolare**, salvo **prova contraria**.

## Atti nulli senza firma qualificata/digitale (art. 21)

- **Scritture private art. 1350, nn. 1-12, c.c.** (c. 2-bis): se fatte con documento
  informatico, **a pena di nullita'** vanno sottoscritte con **firma qualificata** o **digitale**
  (salvo sottoscrizione autenticata). Per l'atto del **n. 13**: firma **avanzata, qualificata o
  digitale** (o modalita' ex art. 20, c. 1-bis).
- **Atto pubblico informatico** (c. 2-ter): il **pubblico ufficiale** sottoscrive a pena di
  nullita' con **firma qualificata o digitale**; le parti con firma **avanzata/qualificata/
  digitale** o **autografa acquisita digitalmente**.

## Firma digitale (art. 24)

- **Univocita'** (c. 1): riferimento **univoco** a **un solo soggetto** e al **documento**.
- **Effetto** (c. 2): **integra e sostituisce** sigilli, punzoni, timbri, contrassegni e marchi.
- **Certificato qualificato** (c. 3-4): al momento della sottoscrizione **non scaduto, revocato
  o sospeso**; reca validita', identificativi di titolare e certificatore ed eventuali **limiti
  d'uso**.
- **Certificato revocato/scaduto/sospeso** (c. 4-bis): la firma su tale certificato equivale a
  **mancata sottoscrizione** (salvo annullamento della sospensione); revoca/sospensione hanno
  effetto dalla **pubblicazione**.

## Cosa NON fa (limiti)

- **Non riproduce** le **Linee guida AgID** (art. 71, regole tecniche su formazione, firme,
  validazione temporale, conservazione) ne' il **Reg. UE 910/2014 (eIDAS)**: vi **rinvia**.
- **Non appone ne' verifica** firme, **non valuta** la validita' del singolo atto.
- **Non sostituisce** il **professionista**, il **notaio** ne' il **giudice**; non tratta la
  **conservazione** (art. 43-44), la **copia/duplicato** informatico (artt. 22-23-bis) se non
  come richiamo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`valuta-valore-documento`](tasks/valuta-valore-documento.md) | Stabilisce se un documento informatico soddisfa la forma scritta / art. 2702 c.c. o e' liberamente valutabile (art. 20), secondo il tipo di firma |
| [`inquadra-firma-atto`](tasks/inquadra-firma-atto.md) | Individua il tipo di firma richiesto (a pena di nullita' per gli atti art. 1350 c.c.) e verifica i requisiti del certificato (art. 21, 24) |

## Riferimenti normativi

- **D.Lgs. 7 marzo 2005, n. 82** (CAD) - **art. 20** (validita' ed efficacia probatoria del
  documento informatico; forma scritta ed efficacia art. 2702 c.c.; libera valutazione;
  presunzione di riconducibilita'), **art. 21** (atti a pena di nullita' con firma qualificata/
  digitale; scritture private art. 1350 c.c.; atto pubblico informatico), **art. 24** (firma
  digitale: univocita', sostituzione di sigilli/timbri, certificato qualificato valido, firma su
  certificato revocato = mancata sottoscrizione).
- **Linee guida AgID** (art. 71 CAD) e **Reg. UE 910/2014 (eIDAS)** - **richiamati** per le
  regole tecniche, non riprodotti.

Dettaglio in `references/sources.yaml`, `references/fonti/cad-artt-20-21-24.md`,
`references/estratti/documento-informatico-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione del valore giuridico e della validita' del
singolo atto resta responsabilita' del **professionista**, del **notaio** e - in giudizio - del
**giudice**, sul testo vigente del CAD e sulle Linee guida AgID / eIDAS. La skill **non
sostituisce** tali soggetti ne' la lettura degli artt. 20/21/24 e delle regole tecniche.
