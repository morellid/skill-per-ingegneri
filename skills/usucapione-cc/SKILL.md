---
name: usucapione-cc
description: "Supporto documentale all'inquadramento dell'usucapione (acquisto della proprietà e dei diritti reali di godimento per possesso continuato) secondo il Codice civile (R.D. 262/1942), Libro III, Titolo VIII. Aiuta a distinguere l'usucapione ordinaria dei beni immobili e dei diritti reali immobiliari in venti anni (art. 1158), l'usucapione decennale abbreviata di un immobile acquistato in buona fede da chi non è proprietario con titolo idoneo trascritto (art. 1159), l'usucapione speciale per la piccola proprietà rurale in quindici o cinque anni (art. 1159-bis), l'usucapione delle universalità di mobili in venti o dieci anni (art. 1160), l'usucapione dei beni mobili in dieci anni in buona fede o venti in mala fede (art. 1161), l'usucapione dei beni mobili iscritti in pubblici registri in tre o dieci anni (art. 1162), i vizi del possesso violento o clandestino (art. 1163), l'interversione del possesso del detentore (art. 1164), l'applicazione delle norme sulla prescrizione con sospensione, interruzione e computo dei termini (art. 1165), l'inefficacia delle cause di impedimento e di sospensione rispetto al terzo possessore (art. 1166) e l'interruzione dell'usucapione per perdita del possesso oltre un anno (art. 1167). Use when a technician, surveyor, lawyer or CTU must frame the requirements and time periods of adverse possession (usucapione) under the Italian Civil Code; it is a documentary aid, does not draft deeds or judicial claims, does not assess the possession in concreto and does not replace the lawyer or the court expert."
license: MIT
area: forense
title: "Usucapione - acquisto della proprietà per possesso (c.c. artt. 1158-1167)"
summary: "Inquadra l'usucapione (c.c. artt. 1158-1167): ordinaria di immobili 20 anni (1158) e abbreviata decennale (1159), piccola proprietà rurale (1159-bis), universalità e beni mobili/registrati (1160-1162), vizi e interversione (1163-1164), prescrizione e interruzione (1165-1167)."
normative_refs:
  - "Codice civile (R.D. 16/3/1942 n. 262) - artt. 1158, 1159, 1159-bis, 1160, 1161, 1162 (usucapione di immobili, universalità, mobili)"
  - "Codice civile (R.D. 16/3/1942 n. 262) - artt. 1163, 1164, 1165, 1166, 1167 (vizi/interversione del possesso, prescrizione, interruzione)"
version: 0.1.0-alpha
status: alpha
tags:
  - codice-civile
  - usucapione
  - possesso
  - diritti-reali
  - prescrizione
  - forense
---

# Usucapione - acquisto della proprietà per possesso (c.c. artt. 1158-1167)

## Quando usare questa skill

Usala quando devi **inquadrare i presupposti e i termini dell'usucapione** (acquisto della
proprietà e dei diritti reali di godimento per possesso continuato), ancorandoli al **Codice
civile, Libro III, Titolo VIII**:

- **immobili - ordinaria** - **art. 1158**: proprietà e diritti reali immobiliari in **20
  anni** di possesso continuato;
- **immobili - abbreviata (decennale)** - **art. 1159**: **10 anni** dalla trascrizione se
  **buona fede**, **titolo idoneo** trascritto, acquisto da **chi non è proprietario**;
- **piccola proprietà rurale** - **art. 1159-bis**: **15 anni** (ordinaria) e **5 anni**
  (abbreviata) per fondi rustici con fabbricati in comuni montani (o non montani entro i
  limiti di reddito della legge speciale);
- **universalità di mobili** - **art. 1160**: **20 anni** (ordinaria), **10 anni** con
  buona fede e titolo idoneo;
- **beni mobili** - **art. 1161**: **10 anni** in **buona fede** senza titolo; **20 anni**
  in **mala fede**;
- **mobili iscritti in pubblici registri** - **art. 1162**: **3 anni** (buona fede, titolo
  idoneo, trascrizione) o **10 anni**;
- **vizi del possesso** - **art. 1163**: il possesso **violento o clandestino** non giova
  finché la violenza/clandestinità non è cessata;
- **interversione del possesso** - **art. 1164**: il **detentore** non usucapisce senza
  **mutamento del titolo** (per causa da terzo o opposizione al proprietario);
- **rinvio alla prescrizione** - **art. 1165**: si applicano, in quanto compatibili, le
  norme su **sospensione, interruzione e computo dei termini**;
- **terzo possessore** - **art. 1166**: nell'usucapione ventennale non operano
  impedimento/sospensione rispetto al terzo possessore (art. 2942);
- **interruzione** - **art. 1167**: l'usucapione si **interrompe** con la perdita del
  possesso per **oltre un anno** (salvo azione di reintegra vittoriosa).

**Non è una skill di redazione/procedura**: non redige atti o domande giudiziali, non
gestisce la mediazione (condizione di procedibilità) e non valuta in concreto il possesso.

## Cosa NON fa (limiti)

- Non **redige** l'atto o la **domanda giudiziale** di accertamento dell'usucapione.
- Non gestisce la **mediazione** ex art. 5 D.Lgs. 28/2010 (condizione di procedibilità per
  l'usucapione): skill `mediazione-civile-conciliazione-dlgs28`.
- Non **valuta in concreto** il possesso ad usucapionem (continuità, animus, buona fede):
  rinvia all'avvocato/CTU.
- Non riproduce le **norme generali sulla prescrizione** (artt. 2934 ss., 2942) né la
  **legge speciale** sulla piccola proprietà rurale: rinvio.

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`inquadra-usucapione`](tasks/inquadra-usucapione.md) | Determina il tipo di usucapione e il termine applicabile (immobili/mobili/registrati/universalità, ordinaria vs abbreviata) in base a bene, buona fede, titolo e trascrizione (artt. 1158-1162) |
| [`verifica-requisiti-possesso`](tasks/verifica-requisiti-possesso.md) | Verifica i requisiti del possesso (non vizioso, interversione), l'applicazione delle norme sulla prescrizione e l'interruzione (artt. 1163-1167) |

## Riferimenti normativi

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - Libro III, Titolo VIII - artt. **1158**
  (immobili), **1159** (decennale), **1159-bis** (piccola proprietà rurale), **1160**
  (universalità), **1161** (mobili), **1162** (mobili registrati), **1163** (vizi), **1164**
  (interversione), **1165** (prescrizione), **1166** (terzo possessore), **1167**
  (interruzione); richiamati gli artt. **2934 ss.** e **2942** (prescrizione).

Dettaglio in `references/sources.yaml`,
`references/fonti/cc-usucapione-1158-1167.md`,
`references/estratti/usucapione-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione del possesso in concreto, la scelta
dell'azione, la mediazione e la redazione degli atti restano all'**avvocato** e, per gli
accertamenti tecnici, al **CTU**. **Non sostituisce** l'avvocato, il CTU né la lettura degli
articoli del Codice civile sull'usucapione e delle norme sulla prescrizione.
