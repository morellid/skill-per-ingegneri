---
name: diagnosi-energetica-dlgs102
description: "Supporto documentale all'obbligo di diagnosi energetica delle grandi imprese e delle imprese a forte consumo di energia ai sensi dell'art. 8 del D.Lgs. 102/2014 (attuazione della direttiva 2012/27/UE). Aiuta a determinare se un'impresa e' obbligata (grande impresa: oltre 250 occupati e fatturato oltre 50 milioni di euro, oppure bilancio oltre 43 milioni; energivore indipendentemente dalla dimensione), le esenzioni (consumi annui sotto 50 tep, sistema ISO 50001 con diagnosi conforme), la periodicita' quadriennale, i soggetti che la eseguono (ESCo o EGE certificati UNI CEI 11352/11339), la comunicazione all'ENEA, i controlli e le sanzioni (da 4.000 a 40.000 euro per mancata diagnosi). Use when an Italian company or energy consultant needs to know whether the D.Lgs. 102/2014 energy audit obligation applies, its deadlines and who can carry it out; it is a documentary aid and does not perform the audit."
license: MIT
area: energia-incentivi
title: "Diagnosi energetica obbligatoria - D.Lgs. 102/2014 art. 8"
summary: "Obbligo di diagnosi energetica delle grandi imprese ed energivore (D.Lgs. 102/2014 art. 8): chi e' obbligato, esenzioni (< 50 tep, ISO 50001), periodicita' quadriennale, ESCo/EGE certificati, comunicazione ENEA e sanzioni. Supporto documentale, non esegue la diagnosi"
normative_refs:
  - "D.Lgs. 4/7/2014 n. 102 (testo vigente) - artt. 2, 8, 16 (attuazione dir. 2012/27/UE)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-102-2014
  - diagnosi-energetica
  - efficienza-energetica
  - grandi-imprese
  - enea
---

# Diagnosi energetica obbligatoria - D.Lgs. 102/2014 art. 8

## Quando usare questa skill

Usala quando devi orientarti sull'obbligo di **diagnosi energetica** ai sensi
dell'art. 8 del D.Lgs. 102/2014:

- determinare se un'impresa e' **obbligata** (grande impresa o energivora);
- verificare le **esenzioni** (consumi < 50 tep; ISO 50001);
- ricostruire la **periodicita' quadriennale** e le scadenze;
- sapere **chi** puo' eseguire la diagnosi (ESCo/EGE certificati) e gli obblighi
  verso l'**ENEA**;
- conoscere i **controlli** e le **sanzioni**.

Target: energy manager, EGE, ESCo, consulenti energetici, imprese obbligate.

## Avvertenza

Questa skill e' un **supporto documentale** basato sul testo vigente del D.Lgs.
102/2014. **Non esegue** la diagnosi energetica, **non calcola** consumi o
risparmi, **non riproduce** l'allegato 2 ne' le norme tecniche (UNI CEI 11352/
11339, ISO 50001, a pagamento) e **non stabilisce** nel merito se una specifica
impresa sia "energivora" (rinvio al DM MiSE 21/12/2017). Non sostituisce l'impresa
ne' l'auditor certificato.

## Sotto-attivita' disponibili

- **Diagnosi di obbligo ed esenzioni**: dato il profilo dell'impresa, determina se
  la diagnosi e' obbligatoria, le esenzioni e le scadenze ->
  `tasks/verifica-obbligo.md`
- **Checklist di adempimento**: verifica gli adempimenti (esecuzione, soggetto
  certificato, comunicazione ENEA, interventi per le energivore) ->
  `tasks/checklist-adempimento.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input (dimensione/fatturato/bilancio, consumi in tep, ISO 50001,
   energivora, date delle diagnosi).
4. Applica la regola **citando l'articolo preciso** (artt. 2, 8, 16).
5. Chiudi con il rinvio all'ENEA/auditor certificato e all'impresa.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dlgs-102-2014.md` (testo vigente da Normattiva, pagina indice
pinnata `!vig=2026-07-14`), estratto operativo in
`references/estratti/diagnosi-energetica-checklist.md`.

## Limiti

Cosa questa skill NON fa:
- non esegue la diagnosi energetica ne' calcola consumi/risparmi;
- non riproduce l'allegato 2 (criteri minimi) ne' le norme UNI CEI 11352/11339 e
  ISO 50001 (a pagamento);
- non stabilisce nel merito se un'impresa sia "energivora" (DM MiSE 21/12/2017);
- non copre gli altri istituti del D.Lgs. 102/2014 (contatori/fatturazione art. 9,
  certificati bianchi/TEE) oltre ai richiami.
