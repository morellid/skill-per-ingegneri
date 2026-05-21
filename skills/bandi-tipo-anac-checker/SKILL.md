---
name: bandi-tipo-anac-checker
description: Verifica la conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) obbligatori per le stazioni appaltanti ai sensi del D.Lgs. 36/2023; identifica deroghe non giustificate, clausole mancanti e anomalie che espongono la procedura a rischio TAR. Use when an Italian RUP or stazione appaltante needs to check whether a disciplinare di gara is aligned with the applicable ANAC bando-tipo, or wants to identify non-standard clauses and deviations before publication.
license: MIT
area: appalti-opere-pubbliche
title: "Bandi-tipo ANAC - Checker disciplinare di gara"
summary: "Verifica la conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) obbligatori per le stazioni appaltanti; identifica deroghe non giustificate, clausole mancanti, riferimenti obsoleti (D.Lgs. 50/2016) e anomalie a rischio TAR prima della pubblicazione"
normative_refs:
  - "D.Lgs. 36/2023"
  - "Bandi-tipo ANAC (n. 1/2023, n. 2/2026 SIA)"
version: 0.2.0
status: alpha
tags:
  - anac
  - dlgs-36-2023
  - bandi-tipo
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

ANAC pubblica schemi di disciplinare articolati per tipo di contratto e criterio di aggiudicazione. Gli schemi verificati per questa skill sono:

| Tipo contratto | Criterio | Schema ANAC | Stato verifica |
|---------------|----------|-------------|----------------|
| Servizi e forniture (sopra soglia) | OEPV | **Bando tipo n. 1/2023 (agg. Delibera 148/2026)** | Confermato - efficace dal 30 maggio 2026 |
| **Servizi di ingegneria e architettura (SIA) (sopra soglia)** | **OEPV** | **Bando tipo n. 2/2026 (Delibera 153/2026)** | **Confermato - efficace dal 30 maggio 2026** |
| Servizi e forniture (sopra soglia) | Prezzo piu' basso | Da verificare su portale ANAC | - |
| Lavori (sopra soglia) | Prezzo piu' basso | Da verificare su portale ANAC | - |
| Lavori (sopra soglia) | OEPV | Da verificare su portale ANAC | - |

**Quale schema applicare**:
- Se l'oggetto e' un servizio o una fornitura **generici** (sopra soglia, OEPV) -> Bando tipo n. 1/2023.
- Se l'oggetto e' un **servizio di ingegneria o di architettura** (progettazione, direzione lavori, coordinamento sicurezza, verifica progetto, ecc.) sopra soglia OEPV -> **Bando tipo n. 2/2026** (specifico per SIA, regola importo 65/35 art. 41 c. 15-bis, requisiti BIM, equo compenso).

**Date di efficacia**: entrambi gli schemi attualmente vigenti (Delibere 148/2026 e 153/2026) sono pubblicati in GU Serie Generale n. 111 del 15 maggio 2026 e acquistano efficacia il quindicesimo giorno successivo, ovvero il **30 maggio 2026**. Per procedure indette prima di tale data si applica la versione precedente (Bando 1/2023 Delibera 365/2025); per i SIA sopra soglia bandite prima del 30 maggio 2026 non esisteva uno schema-tipo ANAC specifico.

Per le procedure sotto soglia: gli schemi sopra soglia si applicano come riferimento
con adattamenti motivati; verificare se ANAC ha pubblicato schemi specifici.

## Novita' principali Delibere 148/2026 e 153/2026

**Bando tipo n. 1/2023 (Delibera 148/2026)** - principali modifiche:
- **Paragrafo 15.1 / Domanda di partecipazione: clausole obbligatorie AI** (Reg. UE 2024/1689 + L. 132/2025 + GDPR), con versione separata per servizi intellettuali (art. 13 L. 132/2025).
- **Paragrafo 14 - Soccorso istruttorio**: integrato elenco casi sanabili (contratto di avvalimento, garanzia provvisoria).
- **Paragrafo 28 - Accesso atti**: clausola alternativa per inversione procedimentale (parere CdS 61/2026).
- Vari aggiustamenti recepiti dal parere del Consiglio di Stato n. 61 del 13/01/2026.

**Bando tipo n. 2/2026 (Delibera 153/2026)** - schema NUOVO per SIA:
- **Importo base 65/35** (art. 41 c. 15-bis Codice): 65% prezzo fisso non ribassabile + 35% ribassabile.
- **Tetto 30%** punteggio offerta economica (art. 41 c. 15-bis lett. b).
- **Calcolo importo base** ai sensi Allegato I.13 (DM 17.06.2016).
- **BIM obbligatorio** per progettazione lavori >2M euro (o soglia art. 14 c. 1 lett. a beni culturali).
- **Maggiorazione 10% compenso** su onorari per progettazione con BIM (Allegato I.13 art. 2 c. 5).
- **Figure professionali BIM** (UNI 11337-7): BIM Manager, BIM Coordinator, BIM Specialist, CDE Manager (paragrafo 6.1 lett. h-k).
- **Clausole AI** in versione "servizi intellettuali" + indicazione attivita' AI nell'offerta tecnica.
- **Offerta di gestione informativa digitale** come documento autonomo dell'offerta tecnica (se BIM).

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
- D.Lgs. 31 marzo 2023 n. 36 - Codice dei contratti pubblici (come modificato da D.Lgs. 209/2024), artt. 11, 41 c. 15-bis (SIA), 43 (BIM), 87, 90, 91, 94-96, 99-101, 104, 106, 117-119; Allegato I.9 (Capitolato informativo BIM); Allegato I.13 (corrispettivi SIA, DM 17.06.2016); Allegato II.12 (requisiti SIA).
- ANAC - Bando tipo n. 1/2023 testo consolidato (Delibera 148 del 1 aprile 2026), schema disciplinare servizi/forniture OEPV sopra soglia.
- ANAC - Bando tipo n. 2/2026 (Delibera 153 del 15 aprile 2026), schema disciplinare servizi di ingegneria e architettura sopra soglia OEPV.
- Regolamento UE 2024/1689 (AI Act); Legge 23 settembre 2025 n. 132 (norma italiana AI, art. 13 per professionisti).

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dlgs-36-artt-clausole-disciplinare.md`](references/estratti/dlgs-36-artt-clausole-disciplinare.md) - artt. 74, 87, 90, 94-103, 117-120.
- [`anac-bandi-tipo-struttura-2023.md`](references/estratti/anac-bandi-tipo-struttura-2023.md) - struttura e clausole obbligatorie degli schemi ANAC.
- [`anac-bandi-tipo-clausole-ai-l132-2025.md`](references/estratti/anac-bandi-tipo-clausole-ai-l132-2025.md) - clausole obbligatorie sull'uso di sistemi di IA (Reg. UE 2024/1689 + L. 132/2025).
- [`anac-bando-tipo-2-2026-sia-requisiti-bim.md`](references/estratti/anac-bando-tipo-2-2026-sia-requisiti-bim.md) - importo 65/35, maggiorazione BIM, figure professionali BIM e requisiti SIA.

## Limiti

Questa skill NON fa:
- Non redige documenti di gara (bando, disciplinare, capitolato) da zero
- Non verifica la congruenza tra il disciplinare e il capitolato tecnico specifico
- Non valuta la legittimita' della scelta della procedura (aperta, ristretta, negoziata)
- Non calcola soglie europee o importi di gara
- Non valuta l'anomalia dell'offerta
- Non conosce il testo aggiornato di ogni singolo schema ANAC: verifica la struttura e i requisiti normativi del D.Lgs. 36/2023; per il confronto puntuale con il testo degli schemi ANAC occorre avere il documento ANAC aggiornato
- Non sostituisce la revisione legale per procedure ad alto rischio o di importo rilevante
