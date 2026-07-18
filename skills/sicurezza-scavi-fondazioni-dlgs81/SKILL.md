---
name: sicurezza-scavi-fondazioni-dlgs81
description: "Supporto documentale al coordinatore per la sicurezza (CSP/CSE), al direttore dei lavori e all'impresa per la sicurezza degli scavi e delle fondazioni in cantiere - splateamenti, sbancamenti, pozzi, trincee e cunicoli - ai sensi del D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza), Titolo IV, Capo II, Sezione III, artt. 118-121. Aiuta a inquadrare, per lo splateamento e lo sbancamento, l'obbligo di dare alle fronti di attacco un'inclinazione o un tracciato tali da impedire i franamenti in relazione alla natura del terreno, il divieto di scavo manuale per scalzamento alla base quando la parete supera 1,50 metri, l'armatura o il consolidamento del terreno quando siano da temere frane, il divieto di presenza degli operai nel campo d'azione dell'escavatore e sul ciglio, la protezione del posto di manovra e la delimitazione della zona di pericolo (art. 118); per pozzi, scavi e cunicoli, le armature di sostegno per pozzi e trincee profondi oltre 1,50 metri, le tavole di rivestimento sporgenti almeno 30 centimetri, le armature dei cunicoli e nelle sottomurazioni, le precauzioni nell'infissione di pali, l'impalcato di protezione nei pozzi di fondazione profondi oltre 3 metri, l'assistenza esterna e le dimensioni per il recupero di un infortunato, il sollevamento del materiale secondo l'Allegato XVIII (art. 119); il divieto di depositi di materiali presso il ciglio degli scavi salvo puntellature (art. 120); la presenza di gas negli scavi, con le misure contro gas tossici, asfissianti, infiammabili o esplosivi, i dispositivi di protezione delle vie respiratorie e il sistema di salvataggio con sorveglianza esterna, la bonifica mediante ventilazione, il divieto di fiamme e il lavoro in coppia (art. 121). Use when a safety coordinator, works supervisor, or contractor must frame the safety of excavations and foundations on site - slope and shoring of faces, spoil deposits at the edge, gases in excavations - under D.Lgs. 81/2008; it is a documentary aid and does NOT draft the safety plan (PSC/POS) or the geotechnical report, does NOT size the shoring or compute the stability of the excavation walls, does NOT reproduce annex XVIII, and does NOT replace the coordinator, the works supervisor, the designer, or the supervisor (preposto)."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Sicurezza degli scavi e delle fondazioni in cantiere (D.Lgs. 81/2008)"
summary: "Inquadra la sicurezza degli scavi (D.Lgs. 81/2008 artt. 118-121): inclinazione/armatura delle fronti e divieto scalzamento oltre 1,50 m (118), armature di pozzi/trincee e tavole sporgenti 30 cm (119), divieto di deposito sul ciglio (120), gas negli scavi (121). Non redige il POS."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza) - Titolo IV, Capo II, Sezione III (Scavi e fondazioni), artt. 118-121: splateamenti, pozzi e cunicoli, deposito sul ciglio, gas negli scavi"
  - "Rinvio (non riprodotti): Allegato XVIII punto 3.4 (sollevamento materiale) D.Lgs. 81/2008; D.Lgs. 106/2009 (modifiche artt. 118-119); PSC/POS (artt. 96, 100)"
version: 0.1.0-alpha
status: alpha
tags:
  - scavi
  - splateamenti-sbadacchiature
  - dlgs-81-2008
  - sicurezza-cantieri
  - fondazioni
---

# Sicurezza degli scavi e delle fondazioni in cantiere (D.Lgs. 81/2008 artt. 118-121)

## Quando usare questa skill

Usala quando un **coordinatore per la sicurezza** (CSP/CSE), un **direttore dei lavori** o un'**impresa**
deve **inquadrare** i presidi di **sicurezza degli scavi e delle fondazioni** (splateamenti,
sbancamenti, pozzi, trincee, cunicoli), secondo il **D.Lgs. 9 aprile 2008, n. 81** (Testo unico
sicurezza), **Titolo IV, Capo II, Sezione III, artt. 118-121**:

- **splateamento e sbancamento**: inclinazione/armatura delle fronti, escavatore, delimitazione (art.
  118);
- **pozzi, scavi e cunicoli**: armature di sostegno, sporgenza delle tavole, impalcato, recupero
  dell'infortunato (art. 119);
- **deposito di materiali** presso il ciglio (art. 120);
- **presenza di gas** negli scavi (art. 121).

**Non è** uno strumento che redige il POS/PSC o la relazione geotecnica, né dimensiona le armature o
calcola la stabilità delle pareti: è un **supporto documentale** che inquadra obblighi, presidi e
soglie.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-presidi-scavo` | Inquadra i presidi contro il franamento e il seppellimento per splateamenti, sbancamenti, pozzi e trincee, con le soglie di 1,50 m, 30 cm e 3 m (artt. 118-120) |
| `inquadra-gas-negli-scavi` | Inquadra le misure contro la presenza di gas tossici/asfissianti/infiammabili/esplosivi in pozzi, fogne e cunicoli: DPI, sistema di salvataggio, bonifica, lavoro in coppia (art. 121) |

## Punti chiave (verificati sul testo)

- **Splateamento** (art. 118): fronti con **inclinazione/tracciato** anti-franamento; **divieto di
  scalzamento alla base oltre m 1,50** (c. 1); armatura/consolidamento se rischio frane (c. 2); divieti
  nel **campo d'azione dell'escavatore** e sul ciglio (c. 3); **delimitazione** della zona di pericolo
  (c. 5).
- **Pozzi/scavi/cunicoli** (art. 119): **armature per pozzi/trincee oltre m 1,50** (c. 1); tavole di
  rivestimento **sporgenti ≥ 30 cm** (c. 2); armature nei cunicoli e nelle **sottomurazioni** (cc.
  3-4); **impalcato nei pozzi oltre 3 m** (c. 6); **assistenza esterna** e recupero dell'infortunato
  (c. 7).
- **Deposito sul ciglio** (art. 120): **vietato**, salvo **puntellature**.
- **Gas negli scavi** (art. 121): misure contro gas tossici/asfissianti/infiammabili/esplosivi (c. 1);
  **DPI vie respiratorie + sistema di salvataggio** con **sorveglianza esterna** (c. 2); **bonifica con
  ventilazione** e **divieto di fiamme** (c. 4); **lavoro in coppia** (c. 5).

## Fonti

- **D.Lgs. 9 aprile 2008, n. 81** (Testo unico sicurezza) - Titolo IV, Capo II, Sezione III, **artt.
  118-121** - testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 008G0104,
  idGruppo 21).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il POS/PSC né la relazione geotecnica; **non dimensiona** armature/sbadacchiature né
  **calcola** la stabilità delle pareti dello scavo.
- **Non riproduce** l'**Allegato XVIII**; **non tratta** la gestione delle terre (DPR 120/2017, skill
  `terre-rocce-scavo-dpr120`) né la capacità portante geotecnica (NTC).
- **Non tratta** gli ambienti confinati (DPR 177/2011) se non nei richiami all'art. 121.

**La skill è un supporto documentale: non sostituisce il coordinatore, il direttore dei lavori, il
progettista o il preposto, né la lettura degli artt. 118-121 del D.Lgs. 81/2008 e dell'Allegato XVIII.**
