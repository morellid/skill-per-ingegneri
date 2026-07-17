---
name: direzione-lavori-esecuzione-dlgs36
description: "Supporto documentale all'inquadramento della direzione dei lavori (DL) e della direzione dell'esecuzione del contratto (DEC) nella fase esecutiva dei contratti pubblici, secondo il Codice dei contratti pubblici (D.Lgs. 31 marzo 2023, n. 36), art. 114. Aiuta a chiarire che l'esecuzione dei contratti di lavori, servizi e forniture e' diretta dal RUP, che nella fase esecutiva si avvale del DEC o del DL, del coordinatore per la sicurezza in esecuzione (D.Lgs. 81/2008) e del collaudatore/verificatore e accerta lo svolgimento delle funzioni (comma 1); per i lavori, che il direttore dei lavori e' nominato prima dell'avvio della procedura su proposta del RUP e puo' essere coadiuvato da un ufficio di direzione lavori (direttori operativi, ispettori di cantiere) ed eventualmente dalle figure dell'allegato I.9 (comma 2), ed e' preposto al controllo tecnico, contabile e amministrativo anche con metodi di gestione informativa digitale (comma 3); che per contratti <= 1 milione di euro senza lavori complessi ne' rischi di interferenze il DL, se in possesso dei requisiti, svolge anche le funzioni di coordinatore per la sicurezza in esecuzione, altrimenti si designa un direttore operativo (comma 4); che le attivita' e i compiti di dettaglio sono demandati all'allegato II.14 (comma 5); che le PA affidano la direzione dei lavori ai propri dipendenti, in mancanza a dipendenti di centrali di committenza/altre PA o all'esterno con le modalita' del codice (comma 6). Per i servizi e le forniture, che le funzioni del direttore dell'esecuzione sono svolte di norma dal RUP (comma 7), che l'allegato II.14 individua i contratti per cui il DEC deve essere diverso dal RUP (comma 8) e che si possono nominare assistenti con funzioni di direttore operativo (comma 10). Use when an engineer, RUP, or contracting-authority operator must frame the direzione lavori / direzione dell'esecuzione roles in an Italian public contract under D.Lgs. 36/2023 art. 114; it is a documentary aid and does NOT appoint the DL/DEC, does NOT draft the direzione-lavori acts, and does NOT replace the contracting authority or the RUP."
license: MIT
area: appalti-opere-pubbliche
title: "Direzione lavori ed esecuzione dei contratti (D.Lgs. 36/2023 art. 114)"
summary: "Inquadra la direzione dei lavori (DL) e dell'esecuzione (DEC) nei contratti pubblici (D.Lgs. 36/2023 art. 114): esecuzione diretta dal RUP, nomina e compiti del DL, ufficio di direzione lavori, DL come CSE sotto 1 milione, DEC per servizi/forniture. Non nomina il DL/DEC."
normative_refs:
  - "D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici) - art. 114 (Direzione dei lavori e dell'esecuzione dei contratti)"
  - "Richiamati dall'art. 114 (non riprodotti): allegato II.14 (attivita'/compiti), allegato I.9 (BIM), D.Lgs. 81/2008 (coordinatore sicurezza), art. 15 L. 241/1990, art. 30 D.Lgs. 267/2000 (accordi PA)"
version: 0.1.0-alpha
status: alpha
tags:
  - direzione-lavori
  - direzione-esecuzione
  - dlgs-36-2023
  - contratti-pubblici
  - codice-appalti
---

# Direzione dei lavori e dell'esecuzione dei contratti pubblici (D.Lgs. 36/2023 art. 114)

## Quando usare questa skill

Usala quando un **ingegnere, RUP o operatore di stazione appaltante** deve **inquadrare** i
ruoli della **direzione dei lavori (DL)** e della **direzione dell'esecuzione del contratto
(DEC)** nella **fase esecutiva** di un **contratto pubblico**, secondo l'**art. 114 del Codice
dei contratti pubblici** (D.Lgs. 31 marzo 2023, n. 36):

- chiarire il **ruolo del RUP** nella direzione dell'esecuzione e le figure di cui si avvale
  (comma 1);
- per i **lavori**: **nomina**, **ufficio di direzione lavori** e **compiti** del DL (commi
  2-3), il DL come **coordinatore per la sicurezza in esecuzione** (comma 4), l'**affidamento**
  (comma 6);
- per **servizi e forniture**: il **DEC** e i casi in cui deve essere **diverso dal RUP**
  (commi 7-8, 10).

Per il **RUP** in generale usa `rup-responsabile-unico-progetto-dlgs36`; per il **collaudo/
verifica di conformita'** usa la skill dedicata; per il **coordinatore per la sicurezza** usa
le skill dell'area sicurezza (D.Lgs. 81/2008). Questa copre l'**inquadramento del DL/DEC**
nell'art. 114.

## Chi dirige l'esecuzione (comma 1)

- L'**esecuzione** dei contratti di **lavori, servizi o forniture** e' **diretta dal RUP**, che
  **controlla i livelli di qualita'** delle prestazioni.
- Nella fase esecutiva il RUP **si avvale**: del **direttore dell'esecuzione (DEC)** o del
  **direttore dei lavori (DL)**; del **coordinatore per la sicurezza in esecuzione** (D.Lgs. 9
  aprile 2008, n. 81); del **collaudatore/commissione di collaudo** o del **verificatore della
  conformita'**; e **accerta** il corretto svolgimento delle funzioni affidate a ciascuno.

## Lavori: nomina, ufficio e compiti del DL (commi 2-3)

- **Nomina** (c. 2): per la direzione e il controllo dell'esecuzione dei **lavori** la stazione
  appaltante nomina, **prima dell'avvio della procedura** per l'affidamento, **su proposta del
  RUP**, un **direttore dei lavori**.
- **Ufficio di direzione lavori** (c. 2): in relazione alla **complessita'** dell'intervento, il
  DL puo' essere coadiuvato da un ufficio costituito da **direttori operativi** e **ispettori di
  cantiere**, ed eventualmente dalle **figure dell'allegato I.9**.
- **Compiti** (c. 3): il DL, con l'ufficio ove costituito, e' preposto al **controllo tecnico,
  contabile e amministrativo** dell'esecuzione, anche mediante **metodi e strumenti di gestione
  informativa digitale** (allegato I.9) se previsti, per eseguire i lavori **a regola d'arte** e
  in conformita' a progetto e contratto.

## Lavori: DL come coordinatore per la sicurezza (comma 4)

- Per contratti di importo **non superiore a 1 milione di euro** e **in assenza di lavori
  complessi e di rischi di interferenze**, il **DL** - se in possesso dei **requisiti** sulla
  sicurezza - svolge **anche** le funzioni di **coordinatore per la sicurezza in fase di
  esecuzione (CSE)**.
- Se il DL **non puo'** svolgere tali funzioni, la stazione appaltante **designa almeno un
  direttore operativo** in possesso dei requisiti. Il CSE assume la **responsabilita'** per le
  funzioni assegnate dalla normativa sulla sicurezza, operando **in piena autonomia**.

## Lavori: affidamento della direzione lavori (comma 6)

- Le **amministrazioni pubbliche** affidano la direzione dei lavori ai **propri dipendenti**;
  in **mancanza**, a dipendenti di **centrali di committenza** o **altre PA** (previo accordo ex
  art. 15 L. 241/1990 o convenzione ex art. 30 D.Lgs. 267/2000).
- Se mancano **competenze/personale**, per **lavori complessi** o che richiedono professionalita'
  specifiche, o se la stazione appaltante **non e' una PA**, l'incarico e' affidato con le
  **modalita' previste dal codice** (affidamento esterno).

## Servizi e forniture: il DEC (commi 7-8, 10)

- **Regola** (c. 7): per i contratti di **servizi e forniture** le funzioni del **direttore
  dell'esecuzione** sono svolte **di norma dal RUP**, che provvede al **coordinamento, alla
  direzione e al controllo tecnico, contabile e amministrativo** dell'esecuzione, anche con
  metodi di gestione informativa digitale (allegato I.9), assicurando la regolare esecuzione.
- **DEC diverso dal RUP** (c. 8): l'**allegato II.14** individua i contratti di servizi e
  forniture di **particolare importanza** (per qualita' o importo) per cui il DEC **deve essere
  diverso dal RUP**.
- **Assistenti** (c. 10): per tali contratti la stazione appaltante, su indicazione del DEC e
  sentito il RUP, puo' nominare **assistenti con funzioni di direttore operativo**.

## Rinvii agli allegati (commi 5, 9)

- **Allegato II.14** (c. 5): stabilisce le **attivita' e i compiti** demandati al DL e agli
  assistenti (direttori operativi, ispettori di cantiere) e alle figure dell'allegato I.9 (il
  secondo periodo del comma 5 e' stato **soppresso dal D.Lgs. 209/2024**).
- **Rinvio** (c. 9): se la stazione appaltante non dispone di competenze/personale per la
  direzione dell'esecuzione, si applica il **comma 6** (affidamento a dipendenti PA o esterno).

## Cosa NON fa (limiti)

- **Non nomina** il DL o il DEC e **non propone** i nominativi: la nomina spetta alla **stazione
  appaltante** su proposta del **RUP**.
- **Non redige** gli atti della direzione lavori/esecuzione (verbali, contabilita', ordini di
  servizio, certificati) ne' i **piani di sicurezza**.
- **Non riproduce** l'**allegato II.14** (attivita' e compiti di dettaglio) ne' l'**allegato
  I.9** (gestione informativa digitale/BIM e figure di supporto), citati come rinvio; **non
  tratta** il coordinamento sicurezza del D.Lgs. 81/2008 se non nei richiami dell'art. 114.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-direzione-lavori`](tasks/inquadra-direzione-lavori.md) | Inquadra nomina, ufficio di direzione lavori, compiti e DL come coordinatore sicurezza in esecuzione per i contratti di lavori (commi 2-4, 6) |
| [`inquadra-direzione-esecuzione`](tasks/inquadra-direzione-esecuzione.md) | Inquadra la direzione dell'esecuzione dei contratti di servizi e forniture: DEC di norma dal RUP e casi in cui deve essere diverso (commi 7-10) |

## Riferimenti normativi

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - **art. 114** (Direzione dei
  lavori e dell'esecuzione dei contratti): commi 1 (esecuzione diretta dal RUP), 2-3 (nomina,
  ufficio e compiti del DL), 4 (DL come CSE sotto 1 milione), 5 (rinvio allegato II.14), 6
  (affidamento), 7-8 (DEC per servizi e forniture), 9 (rinvio comma 6), 10 (assistenti).
- Fonti **richiamate** dall'art. 114 (non riprodotte): **allegato II.14** (attivita' e compiti),
  **allegato I.9** (gestione informativa digitale/BIM), **D.Lgs. 81/2008** (coordinatore
  sicurezza in esecuzione), **art. 15 L. 241/1990** e **art. 30 D.Lgs. 267/2000** (accordi tra
  PA), **art. 15** del Codice (RUP), **art. 116** (collaudo/verifica di conformita').

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-36-2023-art114.md`,
`references/estratti/direzione-lavori-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la **nomina** del DL/DEC, la **redazione** degli atti della
direzione lavori/esecuzione e le valutazioni discrezionali restano responsabilita' della
**stazione appaltante** e del **RUP**, sul testo vigente dell'art. 114 (il Codice e' soggetto a
decreti correttivi). La skill **non sostituisce** la stazione appaltante, il RUP ne' la lettura
dell'art. 114 e degli allegati e articoli da esso richiamati.
