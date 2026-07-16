---
name: regimi-suap-attivita-produttive-dlgs222
description: "Supporto documentale all'individuazione del regime amministrativo (comunicazione, SCIA, SCIA unica, SCIA condizionata, silenzio-assenso, autorizzazione) applicabile all'avvio, alla modifica, al subingresso o alla cessazione di un'attivita' privata produttiva o commerciale presso lo Sportello unico (SUAP), sulla base del D.Lgs. 222/2016 (\"SCIA 2\") e della sua Tabella A. Aiuta a impostare la lettura della Tabella A (a ciascuna attivita' elencata si applica il regime ivi indicato - art. 2, c. 1), a riconoscere gli effetti di ciascun regime (comunicazione che produce effetto con la presentazione; SCIA con avvio immediato e controlli entro 60 giorni, 30 nell'edilizia; SCIA unica ex art. 19-bis c. 2 con trasmissione dello Sportello alle altre amministrazioni; SCIA condizionata ex art. 19-bis c. 3 con Conferenza di servizi entro 5 giorni e avvio subordinato al rilascio delle autorizzazioni; autorizzazione con provvedimento espresso salvo silenzio-assenso ex art. 20; combinazione autorizzazione + SCIA/comunicazione allegata), a gestire le attivita' non elencate (ricondotte a quelle corrispondenti e pubblicate sul sito dell'ente - art. 2, c. 6) e a verificare eventuali livelli ulteriori di semplificazione di regioni ed enti locali (art. 5). Use when an engineer, geometra, consultant, or SUAP/SUE operator must classify an Italian private/productive activity to determine which administrative regime applies before filing at the one-stop business desk (SUAP) under D.Lgs. 222/2016 Tabella A; it is a documentary aid and does NOT reproduce the full activity-by-activity Tabella A (the exact regime of each activity must be read on the table itself), does not replace the SUAP's assessment and does not cover the building/edilizia interventions handled by the modulistica-edilizia-unificata skill."
license: MIT
area: edilizia-urbanistica-catasto
title: "Regime amministrativo SUAP per attivita' produttive (D.Lgs 222/2016)"
summary: "Individua il regime amministrativo (comunicazione, SCIA, SCIA unica, SCIA condizionata, autorizzazione) di un'attivita' produttiva/commerciale al SUAP tramite la Tabella A del D.Lgs 222/2016. Inquadra effetti e tempi; non riproduce la Tabella A per ogni attivita'."
normative_refs:
  - "D.Lgs. 25 novembre 2016, n. 222 (\"SCIA 2\") - artt. 1, 2, 5 e Tabella A"
  - "L. 241/1990 - artt. 19 (SCIA), 19-bis (SCIA unica/condizionata), 20 (silenzio-assenso)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-222-2016
  - suap
  - scia
  - tabella-a
  - attivita-produttive
---

# Regime amministrativo SUAP per attivita' produttive (D.Lgs 222/2016)

## Quando usare questa skill

Usala quando un **ingegnere, geometra, consulente o operatore del SUAP/SUE** deve
**individuare il regime amministrativo** applicabile all'**avvio, modifica, subingresso o
cessazione** di un'**attivita' privata produttiva o commerciale** presso lo **Sportello
unico per le attivita' produttive (SUAP)**, sulla base del **D.Lgs. 222/2016 ("SCIA 2")**
e della sua **Tabella A**:

- capire **quale regime** (comunicazione, SCIA, SCIA unica, SCIA condizionata,
  silenzio-assenso, autorizzazione) la Tabella A associa all'attivita';
- riconoscere gli **effetti e i tempi** di ciascun regime;
- gestire le **attivita' non elencate** e i **livelli ulteriori di semplificazione** di
  regioni/enti locali.

Per la parte **edilizia** (regime degli interventi edilizi, modulistica unificata) usa la
skill `modulistica-edilizia-unificata`: questa copre le **attivita' produttive/commerciali**.

## Art. 1 - Oggetto

Il decreto, in attuazione della delega dell'art. 5 L. 124/2015, provvede alla **precisa
individuazione delle attivita'** oggetto di procedimento di **comunicazione** o
**segnalazione certificata di inizio attivita' (SCIA)** o di **silenzio-assenso**, nonche'
di quelle per cui e' necessario il **titolo espresso**. Le amministrazioni procedenti
forniscono **gratuitamente consulenza** funzionale all'istruttoria per le attivita' della
Tabella A, salvi i soli **diritti di segreteria** (art. 1, c. 3).

## Art. 2 - Regimi amministrativi delle attivita' private (Tabella A)

**A ciascuna attivita' elencata nella Tabella A si applica il regime amministrativo ivi
indicato** (art. 2, c. 1). I regimi e i loro effetti:

- **Comunicazione** (c. 2): produce effetto con la **presentazione** all'amministrazione
  competente o allo **Sportello unico**. Se servono altre comunicazioni/attestazioni, si
  puo' presentare **un'unica comunicazione** allo Sportello (art. 19-bis L. 241/1990), con
  le asseverazioni/certificazioni previste da legge o regolamento.
- **SCIA** (c. 3 -> **art. 19 L. 241/1990**): l'attivita' puo' essere **avviata
  immediatamente**; l'amministrazione effettua i controlli **entro 60 giorni (30
  nell'edilizia)** e, in carenza di requisiti, puo' **vietare la prosecuzione** o chiedere
  di **conformarsi**.
- **SCIA unica** (c. 3 -> **art. 19-bis, c. 2**): quando servono **altre SCIA o
  comunicazioni/notifiche**, si presenta **un'unica SCIA** allo Sportello unico, che la
  **trasmette immediatamente** alle altre amministrazioni per i controlli (termine 60/30
  giorni).
- **SCIA condizionata** ad atti di assenso (c. 3 -> **art. 19-bis, c. 3**): la SCIA e'
  presentata **contestualmente** all'istanza per le autorizzazioni; **entro 5 giorni** e'
  convocata la **Conferenza di servizi**; l'**avvio e' subordinato** al rilascio delle
  autorizzazioni, comunicato dallo Sportello unico.
- **Autorizzazione** (c. 5 -> **art. 20 L. 241/1990**): serve un **provvedimento
  espresso**, **salvo silenzio-assenso** ove indicato; se servono ulteriori atti di
  assenso, si applica la **Conferenza di servizi** (artt. 14 e ss. L. 241), convocata
  entro 5 giorni.
- **Autorizzazione + SCIA / SCIA unica / Comunicazione**: alla domanda di autorizzazione
  si puo' **allegare** la SCIA / SCIA unica / comunicazione per le attivita' che le
  prevedono (es. SCIA prevenzione incendi; notifica sanitaria).

**Attivita' non elencate** (c. 6): l'amministrazione puo' **ricondurle** all'attivita'
corrispondente, **pubblicandole sul proprio sito** istituzionale. Per la SCIA, il termine
di **18 mesi** dell'art. 21-nonies (annullamento d'ufficio) decorre dalla scadenza del
termine per il potere ordinario di verifica (c. 4).

## Art. 5 - Livelli ulteriori di semplificazione

Regioni ed enti locali, nel disciplinare i regimi di loro competenza, **fermi restando i
livelli di semplificazione e le garanzie del decreto**, possono prevedere **livelli
ulteriori di semplificazione**: verificare la disciplina locale.

## Cosa NON fa (limiti)

- **Non riproduce la Tabella A attivita' per attivita'** (~245 KB): il **regime esatto**
  della singola attivita' va **letto sulla Tabella A** dell'atto. La skill inquadra il
  quadro e il metodo di lettura.
- **Non sostituisce** la valutazione del SUAP ne' la lettura della normativa di settore.
- **Non copre l'edilizia** (interventi edilizi/modulistica): rinvia a
  `modulistica-edilizia-unificata`.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`individua-regime-attivita`](tasks/individua-regime-attivita.md) | Individua il regime amministrativo di un'attivita' produttiva/commerciale sulla Tabella A e ne inquadra effetti e tempi |
| [`gestisci-scia-unica-condizionata`](tasks/gestisci-scia-unica-condizionata.md) | Distingue e imposta SCIA, SCIA unica (art. 19-bis c. 2) e SCIA condizionata (art. 19-bis c. 3) con la Conferenza di servizi |

## Riferimenti normativi

- **D.Lgs. 25 novembre 2016, n. 222** ("SCIA 2") - **art. 1** (oggetto), **art. 2**
  (regimi amministrativi delle attivita' private; rinvio alla **Tabella A**), **art. 5**
  (livelli ulteriori di semplificazione) e **Tabella A** (legenda dei regimi).
- **L. 7 agosto 1990, n. 241** - **art. 19** (SCIA), **art. 19-bis** (SCIA unica, c. 2;
  SCIA condizionata, c. 3), **art. 20** (silenzio-assenso), artt. 14 e ss. (Conferenza di
  servizi).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-222-2016.md`,
`references/estratti/regimi-suap-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione dell'attivita' e la determinazione
del regime restano responsabilita' del professionista e del **SUAP** competente, sulla
Tabella A vigente. La skill **non sostituisce** lo Sportello unico, la lettura della Tabella A dell'atto ne' la normativa di settore applicabile all'attivita'.
