---
name: rup-responsabile-unico-progetto-dlgs36
description: "Supporto documentale all'inquadramento del Responsabile unico del progetto (RUP) nei contratti pubblici ai sensi dell'art. 15 del D.Lgs. 36/2023 (Codice dei contratti pubblici). Aiuta a inquadrare la nomina nel primo atto di avvio dell'intervento per le fasi di programmazione, progettazione, affidamento ed esecuzione (c. 1), la nomina tra i dipendenti in possesso dei requisiti dell'allegato I.2 con le regole per gli enti non pubbliche amministrazioni, la carenza di organico, l'obbligatorieta' e non rifiutabilita' dell'ufficio e il subentro ex lege in caso di mancata nomina (c. 2), l'indicazione del nominativo nel bando/avviso/invito/affidamento diretto (c. 3), l'unicita' del RUP e i modelli organizzativi con responsabili di procedimento per fase sotto supervisione, indirizzo e coordinamento del RUP (c. 4), i compiti del RUP e il completamento dell'intervento (c. 5), la struttura di supporto e le risorse fino all'1 per cento della base di gara (c. 6), il piano di formazione (c. 7), il divieto di cumulo degli incarichi nel contraente generale e nel partenariato pubblico-privato (c. 8) e il RUP delle centrali di committenza e aggregazioni (c. 9). Use when a contracting authority, a granting body or a RUP must frame the role, the appointment, the requirements and the incompatibilities of the single project officer under the Italian public contracts code; it is a documentary aid, does not appoint the RUP, does not draft the tender documents and does not verify the Annex I.2 requirements in concreto."
license: MIT
area: appalti-opere-pubbliche
title: "Responsabile unico del progetto (RUP) - D.Lgs. 36/2023 art. 15"
summary: "Inquadra il Responsabile unico del progetto - RUP (D.Lgs. 36/2023 art. 15): nomina e requisiti allegato I.2 (c.1-2), nominativo nel bando (c.3), unicita' e modelli organizzativi (c.4), compiti e supporto (c.5-6), formazione (c.7), incompatibilita' contraente generale/PPP (c.8)."
normative_refs:
  - "D.Lgs. 31/3/2023 n. 36 - art. 15 c. 1-4 (nomina, requisiti, indicazione nel bando, unicita' e modelli organizzativi)"
  - "D.Lgs. 31/3/2023 n. 36 - art. 15 c. 5-9 (compiti, struttura di supporto, formazione, incompatibilita', centrali di committenza)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-36-2023
  - contratti-pubblici
  - rup
  - stazione-appaltante
  - responsabile-procedimento
  - allegato-i2
---

# Responsabile unico del progetto (RUP) - D.Lgs. 36/2023 art. 15

## Quando usare questa skill

Usala quando devi **inquadrare la figura del Responsabile unico del progetto (RUP)**
nei contratti pubblici e ancorarla all'**art. 15 del D.Lgs. 36/2023** (Codice dei
contratti pubblici):

- **nomina** - **art. 15 c. 1**: nel **primo atto di avvio** dell'intervento
  pubblico, per le fasi di **programmazione, progettazione, affidamento ed
  esecuzione** di ciascuna procedura soggetta al codice;
- **soggetto e requisiti** - **art. 15 c. 2**: nomina tra i **dipendenti** (anche a
  tempo determinato), preferibilmente dell'unita' organizzativa titolare del potere
  di spesa, in possesso dei **requisiti dell'allegato I.2**; regole per gli enti che
  **non sono PA**; possibilita' di nominare tra dipendenti di **altre
  amministrazioni** in caso di carenza di organico; ufficio **obbligatorio e non
  rifiutabile**; in mancanza di nomina subentra **ex lege** il responsabile
  dell'unita' organizzativa competente;
- **pubblicita'** - **art. 15 c. 3**: il **nominativo** e' indicato nel
  **bando/avviso** o, in mancanza, nell'**invito** o nel provvedimento di
  **affidamento diretto**;
- **unicita' e modelli organizzativi** - **art. 15 c. 4**: il RUP e' **unico**; sono
  ammessi modelli con **responsabili di procedimento** per fase
  (programmazione/progettazione/esecuzione e affidamento), ferme le funzioni di
  **supervisione, indirizzo e coordinamento** del RUP;
- **compiti** - **art. 15 c. 5**: il RUP assicura il **completamento**
  dell'intervento svolgendo le attivita' dell'**allegato I.2** (o comunque
  necessarie, se non di competenza di altri organi);
- **struttura di supporto e formazione** - **art. 15 c. 6-7**: struttura di supporto
  e risorse fino all'**1%** della base di gara; **piano di formazione** del personale;
- **incompatibilita'** - **art. 15 c. 8**: nel **contraente generale** e nel **PPP**
  e' vietato attribuire RUP, responsabile dei lavori, direttore dei lavori o
  collaudatore all'affidatario o a soggetti collegati;
- **centrali di committenza** - **art. 15 c. 9**: designano un RUP per le attivita'
  di propria competenza.

**Non e' una skill di redazione**: non nomina il RUP, non redige gli atti di gara e
non verifica in concreto i requisiti dell'allegato I.2.

## Cosa NON fa (limiti)

- Non **nomina** il RUP ne' redige l'atto di avvio, il bando/avviso o l'atto di
  nomina.
- Non riproduce l'**allegato I.2** (requisiti di professionalita' e elenco dei
  compiti del RUP): e' citato come rinvio.
- Non **verifica in concreto** il possesso dei requisiti ne' l'adeguatezza delle
  competenze professionali: rinvia alla stazione appaltante/ente concedente.
- Non decide la **ripartizione delle responsabilita'** tra RUP e responsabili di
  procedimento in un caso concreto: ne inquadra il modello (c. 4).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-nomina-rup`](tasks/inquadra-nomina-rup.md) | Verifica il momento e l'atto di nomina (c. 1, 3), il soggetto e i requisiti (c. 2), l'unicita' e l'eventuale modello organizzativo con responsabili di procedimento (c. 4) |
| [`verifica-compiti-incompatibilita`](tasks/verifica-compiti-incompatibilita.md) | Inquadra i compiti e la struttura di supporto (c. 5, 6), la formazione (c. 7), il divieto di cumulo nel contraente generale/PPP (c. 8) e il RUP delle centrali di committenza (c. 9) |

## Riferimenti normativi

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - **art. 15**
  (Responsabile unico del progetto - RUP), commi **1-9**; **allegato I.2**
  (requisiti e compiti del RUP, rinvio); richiamato l'**art. 37** (programmazione).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-36-2023-art15.md`,
`references/estratti/rup-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la nomina del RUP, la verifica dei requisiti
dell'allegato I.2, la definizione del modello organizzativo e la redazione degli
atti restano in capo alla **stazione appaltante** o all'**ente concedente**.
**Non sostituisce** la stazione appaltante, il RUP, ne' la lettura dell'art. 15 e
dell'allegato I.2 del D.Lgs. 36/2023.
