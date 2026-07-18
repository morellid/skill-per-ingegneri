---
name: classificazione-rifiuti-dlgs152
description: "Supporto documentale al tecnico ambientale, al responsabile del sistema di gestione ambientale (RSGA) e al produttore/detentore per la classificazione dei rifiuti e l'attribuzione dei codici dell'elenco europeo (EER), ai sensi del D.Lgs. 3 aprile 2006, n. 152 (Codice dell'ambiente), Parte IV, artt. 183 (definizioni) e 184 (classificazione). Aiuta a inquadrare le definizioni essenziali - rifiuto come sostanza od oggetto di cui il detentore si disfi o abbia intenzione o obbligo di disfarsi, produttore iniziale e nuovo produttore, detentore, deposito temporaneo prima della raccolta ai sensi dell'articolo 185-bis (art. 183) - e i due assi della classificazione: secondo l'origine in rifiuti urbani, cioe' i domestici e quelli simili per natura e composizione prodotti dalle attivita' degli allegati L-quater e L-quinquies, e rifiuti speciali (agricoli, da costruzione e demolizione e scavo, industriali, artigianali, commerciali, di servizio, da trattamento rifiuti e depurazione, sanitari, veicoli fuori uso), e secondo la pericolosita' in rifiuti pericolosi, che recano le caratteristiche di pericolo dell'Allegato I, e non pericolosi; l'elenco europeo dei rifiuti dell'Allegato D, vincolante per la determinazione dei pericolosi, e l'attribuzione dei codici e delle caratteristiche di pericolo a cura del produttore sulla base delle Linee guida SNPA (art. 184). Use when an environmental technician, environmental management system manager, or waste producer/holder must frame the classification of waste - urban vs special, hazardous vs non-hazardous - and the assignment of the European Waste Catalogue (EWC/EER) codes under D.Lgs. 152/2006; it is a documentary aid and does NOT assign the EER code or the hazard class of a specific waste, does NOT draft the characterization analysis or fill in the register/FIR/MUD, does NOT reproduce annexes D/I/L-quater/L-quinquies or the SNPA guidelines, and does NOT replace the producer, the environmental technician, or the laboratory."
license: MIT
area: ambiente-territorio-mobilita
title: "Classificazione dei rifiuti (D.Lgs. 152/2006 artt. 183-184)"
summary: "Inquadra la classificazione dei rifiuti (D.Lgs. 152/2006 artt. 183-184): definizioni di rifiuto/produttore/detentore (183), classificazione per origine (urbani/speciali) e pericolosita' (Allegato I), elenco europeo EER (Allegato D) con codice attribuito dal produttore (184)."
normative_refs:
  - "D.Lgs. 3 aprile 2006, n. 152 (Codice dell'ambiente) - Parte IV, artt. 183 (definizioni) e 184 (classificazione: urbani/speciali, pericolosi/non pericolosi, elenco EER)"
  - "Rinvio (non riprodotti): Allegati D (elenco EER), I (caratteristiche HP), L-quater/L-quinquies D.Lgs. 152/2006; artt. 184-bis/ter e 185-bis; Linee guida SNPA"
version: 0.1.0-alpha
status: alpha
tags:
  - classificazione-rifiuti
  - codici-eer
  - rifiuti-pericolosi
  - dlgs-152-2006
  - gestione-rifiuti
---

# Classificazione dei rifiuti - urbani/speciali, pericolosi/non pericolosi (D.Lgs. 152/2006 artt. 183-184)

## Quando usare questa skill

Usala quando un **tecnico ambientale**, un **RSGA** o un **produttore/detentore** deve **inquadrare** la
**classificazione di un rifiuto** e l'attribuzione dei **codici dell'elenco europeo (EER)**, secondo il
**D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente), **Parte IV, artt. 183 (definizioni) e 184
(classificazione)**:

- capire se qualcosa **è un rifiuto** e chi è **produttore/detentore** (art. 183);
- classificare **secondo l'origine** (urbani vs speciali) e **secondo la pericolosità** (pericolosi vs
  non pericolosi) (art. 184);
- inquadrare l'**elenco EER** (Allegato D) e chi **attribuisce il codice** (il produttore).

**Non è** uno strumento che attribuisce il codice EER o la classe di pericolo del singolo rifiuto, né
redige l'analisi di caratterizzazione: è un **supporto documentale** che inquadra definizioni e criteri.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-origine-rifiuto` | Stabilisce se è rifiuto (art. 183) e lo classifica per origine in urbano o speciale (art. 184 cc. 1-3) |
| `inquadra-pericolosita-codice` | Inquadra la pericolosità (Allegato I), l'elenco EER (Allegato D, voci a specchio) e l'attribuzione del codice a cura del produttore (art. 184 cc. 4-5) |

## Punti chiave (verificati sul testo)

- **Rifiuto** (art. 183, c. 1, lett. a): sostanza/oggetto di cui il **detentore** si disfi, abbia
  intenzione o obbligo di disfarsi. **Produttore** iniziale/nuovo (lett. f), **detentore** (lett. h),
  **deposito temporaneo prima della raccolta** (lett. bb, ex art. 185-bis).
- **Due assi** (art. 184, c. 1): **origine** (urbani/speciali) **e** **pericolosità** (pericolosi/non
  pericolosi), indipendenti.
- **Urbani** (art. 184 c. 2; art. 183 lett. b-ter): domestici e **simili** (All. L-quater/L-quinquies) +
  spazzamento, verde, mercati, ecc. **Speciali** (art. 184 c. 3): C&D e scavo, industriali, artigianali,
  commerciali, di servizio, fanghi/depurazione, sanitari, veicoli fuori uso.
- **Pericolosi** (art. 184 c. 4): caratteristiche di pericolo dell'**Allegato I** (HP 1-15); **elenco
  EER** (**Allegato D**) **vincolante** (c. 5); **voci a specchio** da valutare sulle sostanze
  pericolose.
- **Attribuzione del codice EER** (art. 184 c. 5): **a cura del produttore**, sulla base delle **Linee
  guida SNPA**.

## Fonti

- **D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente) - Parte IV, **artt. 183-184** - testo vigente
  su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 006G0171, idGruppo 34).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non attribuisce** il codice **EER** né la classe **HP** del singolo rifiuto; **non redige**
  l'analisi di caratterizzazione né compila **registro/FIR/MUD**.
- **Non riproduce** gli **Allegati D/I/L-quater/L-quinquies** né le **Linee guida SNPA**.
- **Non tratta** il **deposito temporaneo** (condizioni dell'art. 185-bis), i **sottoprodotti/EoW**
  (artt. 184-bis/ter, skill `sottoprodotti-end-of-waste-dlgs152`) né le **terre e rocce da scavo** (DPR
  120/2017) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il produttore, il tecnico ambientale o il
laboratorio, né la lettura degli artt. 183-184 del D.Lgs. 152/2006 e dei relativi allegati.**
