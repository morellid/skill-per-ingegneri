---
name: combinazioni-carico-ntc
description: Genera e verifica matrici di combinazioni delle azioni per edifici civili e industriali correnti ai sensi NTC 2018 par. 2.5.3, con coefficienti psi della Tab. 2.5.I e coefficienti gamma della Tab. 2.6.I per profili EQU/A1/A2. Produce combinazioni SLU fondamentali, SLE rara/frequente/quasi permanente, sismica ed eccezionale a partire da azioni permanenti, precompressione e azioni variabili. Implementazione code-driven, deterministica e riproducibile. Use when an Italian structural engineer asks to build, audit, or export NTC 2018 load combinations for ordinary civil/industrial buildings.
license: MIT
area: strutture-geotecnica
title: "Combinazioni Carico NTC"
summary: "Generazione/verifica code-driven delle combinazioni delle azioni SLU/SLE/sismiche/eccezionali per edifici civili e industriali correnti"
normative_refs:
  - "NTC 2018 par. 2.5.3"
  - "Tab. 2.5.I"
  - "Tab. 2.6.I"
version: 0.1.1-alpha
status: alpha
tags:
  - ntc-2018
  - slu
  - sle
---

# Combinazioni di carico NTC 2018 (par. 2.5.3)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve generare o controllare la matrice delle combinazioni delle azioni per edifici civili e industriali correnti secondo NTC 2018 par. 2.5.3. La skill accetta azioni permanenti `G1`/`G2`, eventuale precompressione `P`, azioni variabili classificate secondo Tab. 2.5.I, e opzionalmente azione sismica `E` o eccezionale `Ad`.

Non usare per ponti, opere geotecniche specialistiche, strutture con azioni definite in capitoli specifici NTC, o casi in cui i coefficienti siano governati da norme settoriali/proprietarie non incluse negli estratti.

## Avvertenza

Questa skill e' uno strumento di supporto alla generazione/verifica di combinazioni di carico. **Non sostituisce il giudizio del progettista strutturale firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce relazioni di calcolo pronte al deposito o alla firma e non decide quali azioni fisiche debbano essere considerate nel modello strutturale.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Genera matrice combinazioni**: l'utente chiede "crea le combinazioni NTC", "fammi la matrice SLU/SLE", "esporta le combinazioni per questi carichi" -> leggi [`tasks/genera-matrice-combinazioni.md`](tasks/genera-matrice-combinazioni.md)
- **Verifica matrice esistente**: l'utente fornisce una matrice gia' prodotta da software/foglio Excel e chiede controllo di coefficienti, azione principale o accompagnamento -> leggi [`tasks/verifica-matrice-combinazioni.md`](tasks/verifica-matrice-combinazioni.md)

Se la richiesta e' generica, chiedi se l'utente vuole generare una matrice da elenco azioni o verificare una matrice esistente.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule di combinazione e le tabelle di coefficienti sono implementate nel modulo Python [`tasks/lib/combinazioni.py`](tasks/lib/combinazioni.py). La test suite [`tasks/lib/test_combinazioni.py`](tasks/lib/test_combinazioni.py) copre coefficienti psi/gamma, permutazione dell'azione variabile principale, SLE, combinazione sismica/eccezionale e serializzazione CLI.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni output numerico o matrice di combinazioni devi invocare il modulo Python via Bash. Non ricostruire le combinazioni "a mano" nel testo della risposta: la skill e' code-driven per rendere l'output riproducibile e ispezionabile dal progettista.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/combinazioni.py --help
```

In Codex e altri agent compatibili AGENTS.md, se la variabile non e' risolta, usa il path assoluto della directory che contiene questo `SKILL.md`.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il task file specifico in `tasks/`.
3. Acquisisci dall'utente l'elenco azioni: permanenti `G1`/`G2`, valore caratteristico o nominale, effetto favorevole/sfavorevole per SLU, eventuale `P`, variabili con categoria NTC Tab. 2.5.I, eventuale `E` o `Ad`.
4. Prepara un JSON conforme allo schema indicato nel task e invoca `tasks/lib/combinazioni.py`.
5. Riporta la matrice generata o il report di verifica con i riferimenti normativi essenziali.
6. Evidenzia eventuali assunzioni: profilo gamma usato (`A1` default), trattamento dei `G2` compiutamente definiti, categorie variabili non presenti in Tab. 2.5.I, azioni favorevoli escluse per gamma pari a zero.
7. Concludi sempre con rinvio alla verifica del progettista strutturale.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Estratti in [`references/estratti/ntc2018-par-2-5-2-6.md`](references/estratti/ntc2018-par-2-5-2-6.md).

Fonte primaria: DM 17/01/2018 (NTC 2018), par. 2.5.3, Tab. 2.5.I, Tab. 2.6.I, pubblicato in Gazzetta Ufficiale n. 42 del 20/02/2018, Suppl. Ord. n. 8.

## Limiti

- Non decide quali azioni fisiche debbano essere modellate; l'elenco delle azioni resta responsabilita' del progettista.
- Non copre coefficienti specifici di ponti, geotecnica, opere provvisionali, apparecchiature, serbatoi, o capitoli NTC diversi dal quadro generale par. 2.5/2.6.
- Non incorpora norme UNI/EN o documenti proprietari.
- Non calcola sollecitazioni, inviluppi FEM, verifiche di resistenza, spostamenti o deformazioni.
- Non gestisce automaticamente combinazioni alternative per segno dell'azione sismica: se servono `+E` e `-E`, l'utente deve fornire due casi o usare il flag del software di calcolo a valle.
- Non sostituisce la firma del progettista strutturale sulle relazioni di calcolo.
