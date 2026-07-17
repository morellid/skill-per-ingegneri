---
name: servitu-coattive-prediali-cc
description: "Supporto documentale all'inquadramento delle servitù prediali coattive di più diretto interesse tecnico secondo il Codice civile (R.D. 262/1942), Libro III, Titolo VI. Aiuta a inquadrare la nozione di servitù prediale come peso imposto su un fondo per l'utilità di un altro fondo di diverso proprietario (art. 1027), i modi di costituzione (coattiva, volontaria, per usucapione o destinazione del padre di famiglia; art. 1031) e la costituzione coattiva con sentenza o atto amministrativo, con determinazione di modalità e indennità e opposizione prima del pagamento (art. 1032), l'acquedotto coattivo ossia l'obbligo di dare passaggio alle acque per i bisogni della vita o usi agrari/industriali con le esenzioni (art. 1033), il passaggio coattivo a favore del fondo intercluso con i criteri di localizzazione - accesso più breve e minor danno, sottopassaggio, ampliamento per i veicoli (art. 1051), il passaggio coattivo a favore del fondo non intercluso con accesso inadatto o insufficiente e i presupposti, inclusa l'estensione della Corte costituzionale per l'accessibilità dei portatori di handicap (art. 1052), l'indennità proporzionata al danno (art. 1053), la cessazione dell'interclusione (art. 1055), l'elettrodotto coattivo (art. 1056) e le vie funicolari/teleferiche (art. 1057). Use when a technician, surveyor, engineer, lawyer or CTU must frame a compulsory predial easement (right of way, water conduit, power line) under the Italian Civil Code; it is a documentary aid, does not draft deeds or judicial claims, does not quantify the indemnity and does not replace the lawyer or the court-appointed expert."
license: MIT
area: forense
title: "Servitù coattive - passaggio, acquedotto, elettrodotto (c.c. artt. 1027-1057)"
summary: "Inquadra le servitù coattive (Codice civile): nozione (1027), costituzione con sentenza e indennità (1031-1032), acquedotto coattivo (1033), passaggio del fondo intercluso/non intercluso (1051-1052), indennità e cessazione (1053, 1055), elettrodotto (1056), vie funicolari (1057)."
normative_refs:
  - "Codice civile (R.D. 16/3/1942 n. 262) - artt. 1027, 1031, 1032, 1033 (nozione, costituzione, acquedotto coattivo)"
  - "Codice civile (R.D. 16/3/1942 n. 262) - artt. 1051, 1052, 1053, 1055, 1056, 1057 (passaggio, indennità, cessazione, elettrodotto, vie funicolari)"
version: 0.1.0-alpha
status: alpha
tags:
  - codice-civile
  - servitu-prediali
  - passaggio-coattivo
  - elettrodotto
  - acquedotto-coattivo
  - forense
---

# Servitù prediali coattive - passaggio, acquedotto, elettrodotto (c.c. artt. 1027-1057)

## Quando usare questa skill

Usala quando devi **inquadrare una servitù prediale coattiva** (legale) di interesse
tecnico e ancorarla al **Codice civile, Libro III, Titolo VI**:

- **nozione** - **art. 1027**: la servitù prediale è il **peso imposto sopra un fondo**
  per l'**utilità di un altro fondo** appartenente a diverso proprietario (fondo
  **servente** e fondo **dominante**);
- **costituzione** - **art. 1031**: coattiva, volontaria, per **usucapione** o per
  **destinazione del padre di famiglia**;
- **modi di costituzione coattiva** - **art. 1032**: in mancanza di contratto, con
  **sentenza** (o **atto amministrativo** nei casi di legge); la sentenza fissa
  **modalità** e **indennità**; prima del pagamento il fondo servente può **opporsi**
  all'esercizio;
- **acquedotto coattivo** - **art. 1033**: obbligo di dare **passaggio alle acque** per
  i bisogni della vita o usi agrari/industriali; **esenti** case, cortili, giardini, aie;
- **passaggio coattivo (fondo intercluso)** - **art. 1051**: fondo circondato da fondi
  altrui senza uscita sulla via pubblica; localizzazione con **accesso più breve** e
  **minor danno** (anche **sottopassaggio**); ampliamento per il transito dei **veicoli**;
- **passaggio coattivo (fondo non intercluso)** - **art. 1052**: accesso **inadatto o
  insufficiente** non ampliabile; concesso dal giudice per esigenze di
  **agricoltura/industria** e - per Corte cost. **167/1999** - di **accessibilità** degli
  edifici abitativi per i portatori di handicap;
- **indennità** - **art. 1053**: proporzionata al **danno**; valore della zona occupata;
- **cessazione dell'interclusione** - **art. 1055**: soppressione quando il passaggio non
  è più necessario;
- **elettrodotto coattivo** - **art. 1056** e **vie funicolari/teleferiche** - **art.
  1057**: passaggio in conformità alle **leggi speciali** in materia.

**Non è una skill di calcolo/redazione**: non redige atti o domande giudiziali, non
quantifica l'indennità e non sostituisce l'avvocato o il CTU.

## Cosa NON fa (limiti)

- Non **redige** l'atto costitutivo, la domanda giudiziale o la CTU di stima.
- Non **quantifica l'indennità** (art. 1053, che rinvia all'art. 1038): la inquadra.
- Non riproduce le **leggi speciali** su acque ed elettrodotti (T.U. R.D. 1775/1933 e
  norme sugli elettrodotti) richiamate dagli artt. 1033/1056/1057: rinvio.
- Non tratta la **servitù di elettrodotto amministrativa** (asservimento coattivo in sede
  espropriativa, DPR 327/2001): distinta e fuori perimetro.
- Non tratta le **distanze legali** (artt. 873 ss., skill `distanze-legali-costruzioni-cc`).

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`inquadra-passaggio-coattivo`](tasks/inquadra-passaggio-coattivo.md) | Verifica i presupposti del passaggio coattivo (fondo intercluso art. 1051 o non intercluso art. 1052), i criteri di localizzazione, l'indennità (art. 1053) e la cessazione (art. 1055) |
| [`inquadra-servitu-acque-elettrodotto`](tasks/inquadra-servitu-acque-elettrodotto.md) | Inquadra l'acquedotto coattivo (art. 1033), l'elettrodotto coattivo (art. 1056) e le vie funicolari (art. 1057), con i modi di costituzione e l'indennità (artt. 1031-1032) |

## Riferimenti normativi

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - Libro III, Titolo VI (Delle servitù
  prediali) - artt. **1027** (nozione), **1031-1032** (costituzione), **1033**
  (acquedotto coattivo), **1051-1053** e **1055** (passaggio coattivo e indennità),
  **1056** (elettrodotto coattivo), **1057** (vie funicolari); richiamato l'art. **1038**
  (misura dell'indennità).

Dettaglio in `references/sources.yaml`,
`references/fonti/cc-servitu-coattive.md`,
`references/estratti/servitu-coattive-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la scelta dell'azione, la redazione degli atti, la
stima dell'indennità e la valutazione dei presupposti in concreto restano all'**avvocato**
e, per la stima, al **CTU**. **Non sostituisce** l'avvocato, il CTU né la lettura degli
articoli del Codice civile e delle leggi speciali richiamate.
