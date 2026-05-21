---
name: gdpr-registro-dpia
description: Supporta la stesura e verifica del Registro delle attivita' di trattamento (art. 30 GDPR) e della Valutazione d'Impatto sulla protezione dei dati - DPIA (art. 35 GDPR). Use when the user needs to draft a GDPR processing register, verify its completeness, decide whether a DPIA is required for a specific processing activity, or structure a DPIA. Target users are Italian data controllers, processors, DPO, and IT engineers building systems that process personal data, with reference to the Italian Garante Privacy provisions.
license: MIT
area: software-dati-cybersecurity
title: "GDPR Registro + DPIA"
summary: "Registro delle attivita' di trattamento e Valutazione d'Impatto (DPIA)"
normative_refs:
  - "GDPR art. 30, 35, 36"
  - "provv. Garante"
version: 0.1.1
status: alpha
tags:
  - gdpr
  - dpia
  - garante-privacy
---

# GDPR Registro trattamenti + DPIA

## Quando usare questa skill

Usare quando un titolare/responsabile del trattamento, DPO o ingegnere chiede di:
- Redigere o aggiornare il Registro delle attivita' di trattamento (art. 30 GDPR)
- Verificare la completezza di un Registro esistente
- Valutare se un trattamento richiede una DPIA (art. 35 GDPR + Provv. Garante 467/2018)
- Strutturare una DPIA secondo i contenuti minimi dell'art. 35 par. 7

**Non usare** quando l'utente chiede:
- Pareri legali su singole interpretazioni del GDPR (richiede legale specializzato)
- Risposte a richieste di esercizio diritti degli interessati (skill futura dedicata)
- Analisi di trasferimenti dati extra-UE in assenza di una specifica valutazione (skill dedicata futura)
- Stesura di privacy policy verso interessati (art. 13/14 - skill dedicata futura)

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documentazione di compliance privacy. **Non sostituisce il giudizio del DPO, del titolare del trattamento o del consulente legale.** Output orientativo che richiede revisione e firma del responsabile della compliance. Sanzioni amministrative ex art. 83 GDPR (fino a 20M euro o 4% del fatturato globale annuo) si applicano in caso di violazione - la skill non fornisce difesa legale.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Stesura Registro trattamenti**: l'utente chiede "redigi il registro", "compila il registro art. 30" -> leggi [`tasks/draft-registro-trattamenti.md`](tasks/draft-registro-trattamenti.md)
- **Verifica Registro esistente**: l'utente chiede "controlla questo registro", "e' completo?" -> leggi [`tasks/check-registro-trattamenti.md`](tasks/check-registro-trattamenti.md)
- **Valutazione soglia DPIA**: l'utente chiede "serve una DPIA?", "e' obbligatoria la valutazione di impatto?" -> leggi [`tasks/valuta-soglia-dpia.md`](tasks/valuta-soglia-dpia.md)
- **Stesura/verifica DPIA**: l'utente chiede "struttura la DPIA", "verifica questa DPIA" -> leggi [`tasks/draft-dpia.md`](tasks/draft-dpia.md)

Se la richiesta e' generica ("aiutami con il GDPR"), chiedi all'utente quale delle quattro azioni vuole svolgere.

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il task file specifico.
3. Acquisisci dagli input dell'utente i dati necessari (organizzazione, finalita', categorie dati, ecc.).
4. Applica la procedura del task.
5. Produci output strutturato (registro, checklist, valutazione, struttura DPIA).
6. Concludi sempre con rinvio alla revisione del DPO o consulente legale.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- Reg. UE 2016/679 (GDPR), in particolare art. 30, 35, 36
- Provvedimento Garante Privacy n. 467/2018 - Allegato 1 - 12 tipologie soggette a DPIA
- WP248 rev. 01 - Linee guida DPIA (Article 29 Working Party, endorsed EDPB)
- D.Lgs. 196/2003 come modificato dal D.Lgs. 101/2018

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non fornisce consulenza legale; l'output e' di supporto, non vincolante
- Non analizza le specifiche misure tecniche di sicurezza (rinvio art. 32)
- Non valuta trasferimenti extra-UE caso per caso (richiede analisi adeguatezza Paese o SCC)
- Non produce documenti pronti al deposito presso il Garante senza revisione DPO/legale
- Non sostituisce la designazione del DPO ove obbligatorio (art. 37)

**Ogni documento prodotto richiede revisione del DPO o del consulente legale prima dell'adozione formale.**
