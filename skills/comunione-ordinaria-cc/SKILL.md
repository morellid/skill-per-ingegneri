---
name: comunione-ordinaria-cc
description: "Supporto documentale all'ingegnere, al geometra e al tecnico incaricato (CTU/CTP o tecnico di parte) nei compiti tecnici che ruotano attorno alla comunione ordinaria di beni immobili (terreni, fabbricati, cose comuni) disciplinata dal Codice civile (R.D. 262/1942, Libro III, Titolo VII, Capo I), artt. 1100-1116. Il fulcro tecnico è la DIVISIONE: valutare se il bene è comodamente divisibile in parti corrispondenti alle quote (art. 1114), impostare il progetto di divisione in natura e, quando non è comodamente divisibile, inquadrare l'attribuzione con conguaglio o la vendita (rinvio alla divisione ereditaria, art. 1116). Inquadra inoltre il contesto in cui il tecnico opera: quote presunte eguali e concorso in vantaggi e pesi (art. 1101); uso della cosa comune senza alterarne la destinazione né impedire il pari uso (art. 1102); ripartizione delle spese di conservazione e godimento in proporzione alle quote (art. 1104); le maggioranze per l'amministrazione, per valore delle quote (art. 1105), per le innovazioni migliorative sulla cosa comune (opere, impianti) con i due terzi del valore e il consenso unanime per alienazioni, diritti reali e locazioni ultra-novennali (art. 1108); il rimborso delle spese necessarie di conservazione (art. 1110); lo scioglimento sempre domandabile e il patto di indivisione entro dieci anni (art. 1111); le cose non soggette a divisione (art. 1112) e l'intervento dei creditori (art. 1113). Use when an engineer, geometra, or court-appointed/party technical expert (CTU/CTP) must support the technical side of a jointly owned property matter under the Italian Civil Code - above all assessing comoda divisibilità and drafting the division project, or framing the majorities/expenses for works on the common asset; it is a documentary aid and does NOT draft legal acts, does NOT give legal advice, does NOT quantify the actual valuations or conguagli (that is the appraisal work itself), does NOT cover condominium (artt. 1117 ss.) nor marital communion, and does NOT replace the lawyer or the judge."
license: MIT
area: forense
title: "Comunione e divisione di beni immobili per il tecnico/CTU (c.c. artt. 1100-1116)"
summary: "Supporta l'ingegnere/geometra/CTU sulla comunione ordinaria (c.c. artt. 1100-1116): comoda divisibilità e progetto di divisione in natura (art. 1114), scioglimento, maggioranze per innovazioni/opere sulla cosa comune (2/3), ripartizione spese per quote. Non redige atti legali."
normative_refs:
  - "Codice civile (R.D. 16 marzo 1942, n. 262) - Libro III, Titolo VII, Capo I (Della comunione in generale), artt. 1100-1116"
  - "Rinvio (non riprodotti): artt. 1117 ss. c.c. (condominio, skill dedicata), artt. 177 ss. (comunione legale coniugi), artt. 713 ss. (divisione ereditaria, richiamata dall'art. 1116)"
version: 0.1.0-alpha
status: alpha
tags:
  - comunione
  - comproprieta
  - codice-civile
  - divisione
  - amministrazione
---

# Comunione e divisione di beni immobili per il tecnico/CTU (c.c. artt. 1100-1116)

## Quando usare questa skill

Usala quando un **ingegnere, geometra o tecnico incaricato** (CTU nominato dal giudice, CTP di
parte, o professionista che redige una relazione di stima/divisione) deve **inquadrare il quadro
civilistico** entro cui svolge i propri **compiti tecnici** su un **bene immobile in comunione
ordinaria** (comproprietà di terreni, fabbricati, cose comuni), secondo il **Codice civile** (R.D.
16 marzo 1942, n. 262), Libro III, Titolo VII, **Capo I (Della comunione in generale)**, artt.
1100-1116.

Il **compito tecnico** tipico e' la **divisione**:

- valutare la **comoda divisibilita'** del bene in parti corrispondenti alle quote (art. 1114);
- impostare il **progetto di divisione in natura** (lotti, quote, eventuali servitu' e accessi);
- quando il bene **non e' comodamente divisibile**, inquadrare l'**attribuzione con conguaglio** o
  la **vendita** (rinvio alle norme sulla divisione ereditaria, art. 1116).

A supporto, la skill inquadra anche il **contesto** in cui il tecnico opera: **uso** e **spese**
sulla cosa comune (artt. 1102, 1104), le **maggioranze** per le **innovazioni/opere e impianti**
sulla cosa comune (art. 1108), lo **scioglimento** e i **diritti dei creditori** (artt. 1111-1113).

Per la comunione **negli edifici** (**condominio**, parti comuni, assemblea, tabelle millesimali,
artt. 1117 ss.) usa `condominio-parti-comuni-assemblea-cc`; per la **relazione peritale** e
l'**ATP** usa `relazione-peritale-ctu-cpc` e `accertamento-tecnico-preventivo-cpc`. Questa copre
il quadro civilistico della **comunione ordinaria** (non condominiale) a supporto del tecnico.

> **Nota di ruolo**: la skill **non da' consulenza legale** e **non redige atti** (l'atto di
> divisione, la domanda giudiziale e le valutazioni di diritto restano dell'avvocato e del giudice).
> Serve al **tecnico** per collocare correttamente la propria relazione (comoda divisibilita',
> progetto di divisione, stima di lotti e conguagli) nel quadro degli artt. 1100-1116.

## Quote, uso e disposizione (artt. 1100-1103)

- **Norme regolatrici** (art. 1100): si applicano se il **titolo** o la **legge** non dispongono
  diversamente.
- **Quote** (art. 1101): si **presumono eguali**; il concorso nei **vantaggi** e nei **pesi** e' in
  proporzione alle quote.
- **Uso della cosa comune** (art. 1102): ciascun partecipante puo' **servirsene** purche' non ne
  **alteri la destinazione** ne' impedisca agli altri il **pari uso**; puo' apportare a proprie
  spese le modificazioni per il miglior godimento. Non puo' **estendere** il proprio diritto in
  danno degli altri se non muta il titolo del possesso.
- **Disposizione della quota** (art. 1103): ciascuno puo' **disporre** del proprio diritto e cedere
  il godimento **nei limiti della sua quota**.

## Spese, amministrazione e regolamento (artt. 1104-1107, 1110)

- **Obblighi/spese** (art. 1104): concorso nelle spese di **conservazione/godimento** e in quelle
  deliberate dalla maggioranza, salva la **rinunzia liberatoria** al diritto (che non giova a chi
  ha approvato la spesa); il **cessionario** e' solidale col cedente per i contributi non versati.
- **Amministrazione** (art. 1105): tutti concorrono; per l'**ordinaria amministrazione** le
  delibere della **maggioranza per valore delle quote** vincolano la minoranza, previa
  **informazione** di tutti; in caso di stallo o inerzia si ricorre al **giudice** (che puo'
  nominare un amministratore).
- **Regolamento e amministratore** (art. 1106): con la stessa maggioranza si adotta un
  **regolamento** e si delega l'amministrazione a partecipanti o a un **estraneo**.
- **Impugnazione del regolamento** (art. 1107): entro **trenta giorni** dalla delibera (dalla
  comunicazione per gli assenti).
- **Rimborso spese** (art. 1110): chi, per trascuranza altrui, sostiene **spese necessarie di
  conservazione** ha diritto al rimborso.

## Innovazioni, atti eccedenti e impugnazioni (artt. 1108-1109)

- **Innovazioni e atti eccedenti** (art. 1108): con la maggioranza dei **due terzi del valore** si
  dispongono **innovazioni** migliorative (che non pregiudichino il godimento di alcuno ne'
  comportino spesa **eccessivamente gravosa**) e gli altri atti eccedenti l'ordinaria
  amministrazione. Serve il **consenso di tutti** per **alienazioni**, costituzione di **diritti
  reali** sul bene comune e **locazioni ultra-novennali** (oltre 9 anni).
- **Impugnazione delle deliberazioni** (art. 1109): la minoranza dissenziente puo' impugnare entro
  **trenta giorni**, a pena di **decadenza** (delibere gravemente pregiudizievoli, difetto di
  informazione, innovazioni in contrasto con l'art. 1108).

## Scioglimento e divisione (artt. 1111-1116)

- **Scioglimento** (art. 1111): **sempre** domandabile; il giudice puo' disporre una **dilazione**
  (max **cinque anni**); il **patto di indivisione** vale al massimo **dieci anni** (i termini
  maggiori si riducono a dieci).
- **Cose non divisibili** (art. 1112): niente scioglimento se la divisione farebbe **cessare l'uso**
  cui la cosa e' destinata.
- **Creditori e aventi causa** (art. 1113): possono **intervenire** nella divisione; per gli
  immobili l'opposizione va **trascritta** prima della divisione.
- **Divisione in natura** (art. 1114): se la cosa e' **comodamente divisibile** in parti
  corrispondenti alle quote; altrimenti si procede diversamente (vendita).
- **Obbligazioni solidali** (art. 1115) e **rinvio** alle norme sulla **divisione ereditaria** (art.
  1116, in quanto compatibili).

## Cosa NON fa (limiti)

- **Non redige** atti (regolamento della comunione, delibere, verbali, domanda di divisione,
  contratti di cessione della quota).
- **Non quantifica** quote, spese, conguagli ne' il valore dei beni.
- **Non tratta** il **condominio** negli edifici (artt. 1117 ss., skill dedicata), la **comunione
  legale tra coniugi** (artt. 177 ss.) ne' la **divisione ereditaria** (artt. 713 ss.), citati come
  rinvio/fuori perimetro.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-uso-amministrazione`](tasks/inquadra-uso-amministrazione.md) | Inquadra uso della cosa comune, spese, amministrazione a maggioranza per valore, regolamento e innovazioni/atti eccedenti con le relative maggioranze (artt. 1102-1109) |
| [`inquadra-scioglimento-divisione`](tasks/inquadra-scioglimento-divisione.md) | Inquadra lo scioglimento della comunione, il patto di indivisione, la divisione in natura e i diritti dei creditori (artt. 1111-1116) |

## Riferimenti normativi

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - Libro III, Titolo VII, **Capo I (Della comunione
  in generale)**: artt. **1100** (norme regolatrici), **1101** (quote), **1102** (uso), **1103**
  (disposizione della quota), **1104** (obblighi/spese), **1105** (amministrazione), **1106**
  (regolamento e amministratore), **1107** (impugnazione del regolamento), **1108** (innovazioni e
  atti eccedenti), **1109** (impugnazione delle deliberazioni), **1110** (rimborso spese), **1111**
  (scioglimento), **1112-1116** (divisione).
- Citati come **rinvio** (non riprodotti): artt. **1117 ss.** (condominio - skill
  `condominio-parti-comuni-assemblea-cc`), artt. **177 ss.** (comunione legale tra coniugi), artt.
  **713 ss.** (divisione ereditaria, richiamata dall'art. 1116).

Dettaglio in `references/sources.yaml`, `references/fonti/cc-comunione-1100-1116.md`,
`references/estratti/comunione-ordinaria-checklist.md`.

## Avvertenza

Skill di **supporto documentale** per il **tecnico** (ingegnere/geometra, CTU/CTP): inquadra il
quadro civilistico entro cui redigere la relazione tecnica (comoda divisibilita', progetto di
divisione, stima dei lotti e dei conguagli). La **consulenza legale**, la redazione dell'**atto di
divisione**/della domanda giudiziale e le valutazioni di **diritto** restano dell'**avvocato** e
del **giudice**; la **stima** in concreto e' l'oggetto della perizia stessa. La skill
**non sostituisce** il tecnico incaricato, l'avvocato ne' la lettura degli artt. 1100 ss. e del titolo/
regolamento della comunione.
