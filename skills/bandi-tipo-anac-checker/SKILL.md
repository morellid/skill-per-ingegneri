---
name: bandi-tipo-anac-checker
description: Verifica la conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) obbligatori per le stazioni appaltanti ai sensi del D.Lgs. 36/2023; identifica deroghe non giustificate, clausole mancanti e anomalie che espongono la procedura a rischio TAR. Use when an Italian RUP or stazione appaltante needs to check whether a disciplinare di gara is aligned with the applicable ANAC bando-tipo, or wants to identify non-standard clauses and deviations before publication.
license: MIT
---

# Bandi-tipo ANAC - Checker disciplinare di gara

## Quando usare questa skill

Usare quando un RUP o una stazione appaltante chiede di:
- **Verificare un disciplinare di gara**: controllare che il disciplinare sia conforme allo schema ANAC applicabile (tipo contratto, criterio aggiudicazione) e segnalare deroghe non giustificate
- **Identificare anomalie**: analizzare un disciplinare alla ricerca di clausole mancanti, clausole non conformi al testo standard, riferimenti normativi obsoleti (D.Lgs. 50/2016 invece di D.Lgs. 36/2023) o deroghe rischiose

**Non usare** se l'utente chiede:
- Costruire una matrice criteri/sottocriteri OEPV: usa skill [`oepv-valutatore-offerte-tecniche`](../oepv-valutatore-offerte-tecniche/SKILL.md)
- Verificare gli elaborati progettuali (PFTE, esecutivo): usa skill [`pfte-allegato-i7-checker`](../pfte-allegato-i7-checker/SKILL.md)
- Redigere da zero un disciplinare di gara completo: questa skill verifica, non redige il documento intero
- Valutare la legittimita' di provvedimenti gia' adottati (aggiudicazione, esclusione): richiede parere legale

## Avvertenza

Questa skill e' uno strumento di supporto alla **verifica formale e strutturale** del disciplinare di gara rispetto agli schemi ANAC.
**Non sostituisce il giudizio del RUP ne' la revisione legale del disciplinare.**
L'output della skill non e' un atto amministrativo, non certifica la legittimita' della procedura e non esclude il rischio di impugnativa.
Ogni esito richiede revisione, approvazione e firma del responsabile competente.

## Sotto-attivita' disponibili

Questa skill supporta due sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Verifica conformita' al bando-tipo**: l'utente chiede "il mio disciplinare e' conforme allo schema ANAC?", "sto usando il bando-tipo giusto?", "cosa manca rispetto al template?", "ci sono deroghe non giustificate?" -> leggi [`tasks/check-conformita-disciplinare.md`](tasks/check-conformita-disciplinare.md)
- **Identificazione anomalie e rischi**: l'utente chiede "trovami le clausole anomale", "controlla i riferimenti normativi", "ci sono rischi TAR?", "ho aggiornato il disciplinare dal vecchio codice?" -> leggi [`tasks/identifica-anomalie-clausole.md`](tasks/identifica-anomalie-clausole.md)

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' vuole eseguire e raccogli le **variabili di inquadramento** prima di procedere.

## Processo generale

1. **Inquadra la procedura**: tipo di contratto (lavori / servizi / forniture), importo, criterio di aggiudicazione (prezzo piu' basso o OEPV), soglia (sopra/sotto soglia europea)
2. **Identifica il bando-tipo applicabile**: in base a tipo contratto + criterio aggiudicazione, determina quale schema ANAC deve essere usato come riferimento
3. **Identifica la sotto-attivita'**: usa il routing della sezione "Sotto-attivita' disponibili"
4. **Carica il task file** corrispondente e applica la procedura
5. **Produci il report** con citazione precisa degli articoli e commi per ogni regola applicata
6. **Concludi** sempre con:
   - elenco delle **deroghe identificate** con valutazione del rischio (bassa / media / alta)
   - rinvio alla **revisione del RUP e della funzione legale** prima della pubblicazione

## Schemi ANAC applicabili (D.Lgs. 36/2023)

ANAC pubblica schemi di disciplinare per il nuovo codice articolati per tipo di contratto e criterio di aggiudicazione. Il documento verificato e' il **Bando tipo n. 1/2023** (aggiornato Delibera ANAC n. 365/2025) per servizi/forniture OEPV sopra soglia. Per gli altri schemi, verificare sempre il portale ANAC prima dell'utilizzo:

| Tipo contratto | Criterio | Schema ANAC | Stato verifica |
|---------------|----------|-------------|----------------|
| Servizi e forniture (sopra soglia) | OEPV | Bando tipo n. 1/2023 | Confermato (Delibera 365/2025) |
| Servizi e forniture (sopra soglia) | Prezzo piu' basso | Da verificare su portale ANAC | - |
| Lavori (sopra soglia) | Prezzo piu' basso | Da verificare su portale ANAC | - |
| Lavori (sopra soglia) | OEPV | Da verificare su portale ANAC | - |

Per le procedure sotto soglia: gli schemi sopra soglia si applicano come riferimento
con adattamenti motivati; verificare se ANAC ha pubblicato schemi specifici.

## Aree di verifica principali

Le principali aree di controllo in un disciplinare rispetto allo schema ANAC:
- **Struttura e sezioni obbligatorie**: presenza di tutte le sezioni previste dallo schema
- **Clausole sociali** (art. 11 D.Lgs. 36/2023): CCNL applicabile, parita' di trattamento economico
- **Cause di esclusione** (artt. 94-96 D.Lgs. 36/2023): conformita' al nuovo codice, non basate su D.Lgs. 50/2016
- **Requisiti partecipazione** (art. 100 D.Lgs. 36/2023): DGUE (art. 91), FVOE (art. 99)
- **Soccorso istruttorio** (art. 101 D.Lgs. 36/2023): disciplina corretta, termine 5-10 giorni
- **Subappalto** (art. 119 D.Lgs. 36/2023): nessun limite percentuale generale
- **Garanzia provvisoria** (art. 106 D.Lgs. 36/2023): 2% con riduzioni per certificazioni
- **Garanzia definitiva** (art. 117 D.Lgs. 36/2023): 10% importo contrattuale con incrementi per ribasso
- **Comunicazioni e accesso agli atti** (artt. 22, 88, 90 D.Lgs. 36/2023)
- **Criteri aggiudicazione** (art. 108 D.Lgs. 36/2023): conformita' gia' verificata da skill OEPV

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 31 marzo 2023 n. 36 - Codice dei contratti pubblici, artt. 11, 87, 90, 91, 94-96, 99-101, 104, 106, 117-119
- ANAC - Bando tipo n. 1/2023 (Delibera 365/2025), schema disciplinare servizi/forniture OEPV sopra soglia

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dlgs-36-artt-clausole-disciplinare.md`](references/estratti/dlgs-36-artt-clausole-disciplinare.md) - artt. 74, 87, 90, 94-103, 117-120
- [`anac-bandi-tipo-struttura-2023.md`](references/estratti/anac-bandi-tipo-struttura-2023.md) - struttura e clausole obbligatorie degli schemi ANAC

## Limiti

Questa skill NON fa:
- Non redige documenti di gara (bando, disciplinare, capitolato) da zero
- Non verifica la congruenza tra il disciplinare e il capitolato tecnico specifico
- Non valuta la legittimita' della scelta della procedura (aperta, ristretta, negoziata)
- Non calcola soglie europee o importi di gara
- Non valuta l'anomalia dell'offerta
- Non conosce il testo aggiornato di ogni singolo schema ANAC: verifica la struttura e i requisiti normativi del D.Lgs. 36/2023; per il confronto puntuale con il testo degli schemi ANAC occorre avere il documento ANAC aggiornato
- Non sostituisce la revisione legale per procedure ad alto rischio o di importo rilevante
