---
name: terre-rocce-scavo-dpr120
description: "Supporto documentale alla gestione delle terre e rocce da scavo secondo il D.P.R. 13 giugno 2017, n. 120 (regolamento sulla disciplina semplificata, coordinato con la Parte IV del D.Lgs. 152/2006). Aiuta a qualificare le terre e rocce da scavo come sottoprodotto anziche' rifiuto (art. 4, in attuazione dell'art. 184-bis del D.Lgs. 152/2006: generazione durante la realizzazione di un'opera; utilizzo conforme al piano di utilizzo o alla dichiarazione per reinterri, riempimenti, rimodellazioni e rilevati; idoneita' all'utilizzo senza trattamenti diversi dalla normale pratica industriale; rispetto dei requisiti ambientali), a distinguere la dimensione del cantiere (di piccole dimensioni fino a 6.000 metri cubi, di grandi dimensioni oltre tale soglia, sottoposti o meno a VIA e AIA - art. 2), a gestire per i cantieri di piccole dimensioni i requisiti ambientali (Concentrazioni Soglia di Contaminazione, colonne A e B, Tabella 1, Allegato 5, Parte IV del D.Lgs. 152/2006 - art. 20) e la dichiarazione di utilizzo (autocertificazione ex art. 47 del DPR 445/2000, modulo dell'allegato 6, da trasmettere almeno 15 giorni prima dell'inizio degli scavi al Comune e all'ARPA, con utilizzo entro un anno - art. 21), e a impostare l'utilizzo nel sito di produzione delle terre escluse dalla disciplina dei rifiuti (art. 24, ex art. 185 del D.Lgs. 152/2006). Use when an engineer, environmental consultant, or contractor must determine whether excavated soil and rocks qualify as a by-product, are excluded from waste rules (reuse on site), or must be managed as waste, and set up the declaration or use plan under DPR 120/2017; it is a documentary aid and does NOT reproduce the contamination threshold values (CSC in Annex 5, Part IV of Legislative Decree 152/2006) or the technical annexes (sampling/analysis, forms), does not perform the sampling/analysis and does not replace ARPA, the environmental professional or the use plan for large sites."
license: MIT
area: ambiente-territorio-mobilita
title: "Terre e rocce da scavo: sottoprodotto e riutilizzo (DPR 120/2017)"
summary: "Qualifica le terre e rocce da scavo secondo il DPR 120/2017: sottoprodotto, escluse dai rifiuti se riusate nel sito, o rifiuto; distingue cantieri piccoli e grandi, con requisiti ambientali (CSC) e dichiarazione di utilizzo. Non riproduce le CSC ne' le analisi."
normative_refs:
  - "D.P.R. 13 giugno 2017, n. 120 - artt. 1, 2, 4, 20, 21, 24 (+ artt. 9 e ss. piano di utilizzo)"
  - "D.Lgs. 152/2006 Parte IV artt. 183, 184-bis, 185 + CSC Tab. 1 Allegato 5 Titolo V (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - terre-e-rocce-da-scavo
  - dpr-120-2017
  - sottoprodotto
  - rifiuti
  - cantieri
---

# Terre e rocce da scavo: sottoprodotto e riutilizzo (DPR 120/2017)

## Quando usare questa skill

Usala quando un **ingegnere, consulente ambientale o impresa** deve gestire le **terre e rocce
da scavo** di un cantiere e stabilire se possono essere **sottoprodotto** (anziche' rifiuto),
**escluse dalla disciplina rifiuti** (riutilizzo nel sito) o vanno gestite come **rifiuto**,
impostando la **dichiarazione** o il **piano di utilizzo**, secondo il **D.P.R. 13 giugno 2017,
n. 120** (coordinato con la Parte IV del **D.Lgs. 152/2006**):

- **qualificare** le terre (sottoprodotto / escluse / rifiuto);
- distinguere la **dimensione del cantiere** e la procedura applicabile;
- gestire i **requisiti ambientali** e gli **adempimenti** (dichiarazione, tempi, ARPA).

Per la disciplina dei **rifiuti** in senso proprio e la loro tracciabilita' vedi
`trasporto-rifiuti-fir-dlgs152`; per la **bonifica** dei siti contaminati vedi
`bonifica-siti-contaminati-dlgs152`.

## Le tre qualificazioni possibili

- **Sottoprodotto** (art. 4, ex **art. 184-bis** D.Lgs. 152/2006) - **tutti** i requisiti:
  (a) **generate durante la realizzazione di un'opera** (di cui sono parte integrante, non lo
  scopo primario); (b) **utilizzo conforme** al **piano di utilizzo** (art. 9, grandi cantieri)
  o alla **dichiarazione** (art. 21, piccoli cantieri), per reinterri, riempimenti,
  rimodellazioni, rilevati; (c) **idonee all'utilizzo** senza trattamenti diversi dalla normale
  pratica industriale; (d) **requisiti ambientali** rispettati.
- **Escluse dalla disciplina rifiuti** (art. 24, ex **art. 185**, c. 1, lett. c): terre
  **utilizzate nel sito di produzione**, **non contaminate** (verifica ai sensi dell'allegato 4).
- **Rifiuto**: in mancanza dei requisiti del sottoprodotto e dell'esclusione, si applica la
  **Parte IV** del D.Lgs. 152/2006.

## Dimensione del cantiere (art. 2)

- **Piccole dimensioni**: produzione **<= 6.000 mc** (dalle sezioni di progetto) -> Capo dei
  **piccoli cantieri** (artt. 20-21, **dichiarazione di utilizzo**).
- **Grandi dimensioni** (> 6.000 mc): **piano di utilizzo** (artt. 9 e ss.), con distinzione tra
  cantieri **sottoposti a VIA/AIA** e non.

## Piccoli cantieri: requisiti ambientali e dichiarazione (artt. 20-21)

- **Requisiti ambientali** (art. 20): il produttore dimostra che non sono superate le
  **Concentrazioni Soglia di Contaminazione (CSC)** delle **colonne A e B, Tabella 1, Allegato 5,
  Titolo V, Parte IV, D.Lgs. 152/2006** (in relazione alle matrici ambientali e alla
  **destinazione d'uso urbanistica** del sito di destinazione), e l'assenza di contaminazione
  delle **acque sotterranee** (salvi i **valori di fondo naturale**).
- **Dichiarazione di utilizzo** (art. 21): **dichiarazione sostitutiva di atto di notorieta'**
  (art. 47 DPR 445/2000), modulo **allegato 6**, trasmessa (anche telematicamente) **almeno 15
  giorni prima** dell'inizio degli scavi al **Comune** e all'**ARPA**; indica quantita',
  eventuale **deposito intermedio**, **sito di destinazione**, autorizzazioni e **tempi** di
  utilizzo (**non oltre 1 anno** dalla produzione, salvo opera con termine superiore). Al termine
  si presenta la **dichiarazione di avvenuto utilizzo (DAU)**.

## Utilizzo nel sito di produzione (art. 24)

Le terre **utilizzate nel sito di produzione** e **non contaminate** (allegato 4) sono
**escluse** dalla disciplina rifiuti (art. 185, c. 1, lett. c, D.Lgs. 152/2006). Le terre da
affioramenti naturali con **amianto** oltre soglia si riutilizzano **solo nel sito di
produzione** sotto controllo delle autorita' (comunicazione ad ARPA e ASL).

## Cosa NON fa (limiti)

- **Non riproduce i valori delle CSC** (Tab. 1, Allegato 5, Parte IV, D.Lgs. 152/2006) ne' gli
  **Allegati tecnici** del regolamento (campionamento/analisi, modulistica): rinvia agli atti.
- **Non esegue** il campionamento/le analisi, **non redige** il piano di utilizzo o la
  dichiarazione e **non sostituisce** l'**ARPA** ne' il professionista ambientale.
- Per i **grandi cantieri** (> 6.000 mc, VIA/AIA) il **piano di utilizzo** (artt. 9 e ss.) e' qui
  solo richiamato.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`qualifica-terre-scavo`](tasks/qualifica-terre-scavo.md) | Stabilisce se le terre sono sottoprodotto (art. 4), escluse dai rifiuti (art. 24) o rifiuto, e la dimensione del cantiere |
| [`gestisci-dichiarazione-piccoli-cantieri`](tasks/gestisci-dichiarazione-piccoli-cantieri.md) | Imposta la dichiarazione di utilizzo dei piccoli cantieri (allegato 6, 15 gg, Comune/ARPA, tempi, DAU) |

## Riferimenti normativi

- **D.P.R. 13 giugno 2017, n. 120** - **art. 1** (oggetto), **art. 2** (definizioni), **art. 4**
  (qualifica come sottoprodotto), **art. 20** (piccoli cantieri - requisiti ambientali), **art. 21**
  (dichiarazione di utilizzo), **art. 24** (utilizzo nel sito di produzione); **artt. 9 e ss.**
  (piano di utilizzo - grandi cantieri, richiamati).
- **D.Lgs. 152/2006** - **art. 183** (definizioni rifiuti), **art. 184-bis** (sottoprodotto),
  **art. 185** (esclusioni), **CSC** Tabella 1, Allegato 5, Titolo V, Parte IV (richiamati).

Dettaglio in `references/sources.yaml`, `references/fonti/dpr-120-2017.md`,
`references/estratti/terre-rocce-scavo-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione delle terre, il campionamento/le analisi e
la redazione della dichiarazione o del piano di utilizzo restano responsabilita' del
professionista e del **produttore**, sotto il controllo dell'**ARPA**. La skill **non
sostituisce** l'ARPA, il professionista ambientale ne' la lettura del D.P.R. 120/2017 (e dei suoi Allegati) e delle CSC del D.Lgs. 152/2006.
