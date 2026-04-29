# Task: Verifica obblighi organi di amministrazione (art. 23 D.Lgs. 138/2024)

Verifica che gli organi di amministrazione e direttivi del soggetto (essenziale o importante) adempiano agli obblighi specifici dell'art. 23 D.Lgs. 138/2024: approvazione delle modalita' di implementazione delle misure, sovrintendenza, formazione, informazione su incidenti.

## Pre-requisito

Il soggetto deve essere classificato come essenziale o importante (vedi task `valuta-perimetro`). Le misure di gestione del rischio (art. 24) devono essere state definite o in fase di definizione - vedi task `gap-analysis-misure`.

## Obiettivo

Produrre una **checklist strutturata** sugli obblighi dell'organo di amministrazione, con livello di adempimento per ciascun punto e raccomandazioni operative. L'output supporta il coordinamento fra Compliance, Legal, CdA e CISO sul governance NIS2.

## Input richiesti

- **Struttura di governance**: organo di amministrazione (CdA, amministratore unico, organo direttivo equivalente), composizione, frequenza riunioni.
- **Esistenza di un Comitato di sicurezza/IT/risk** che riporta al CdA?
- **Atti gia' adottati**:
  - Delibera CdA su politiche di sicurezza informatica?
  - Approvazione del piano di implementazione misure ex art. 24?
  - Designazione del punto di contatto NIS (art. 7)?
- **Formazione**:
  - Membri del CdA hanno seguito formazione cyber? Tipo, ente erogatore, data.
  - Programma di formazione per i dipendenti? Con quale frequenza?
- **Reporting**:
  - L'organo di amministrazione e' informato periodicamente su incidenti (art. 25-26)?
  - Quale cadenza (trimestrale, semestrale)? Esistono escalation immediate?

## Fonti

Leggere prima:
- `references/estratti/dlgs-138-2024-misure-art23.md` - art. 23 (governance) + art. 24 (misure)
- `references/estratti/acn-misure-base-essenziali.md` - sottocategorie GV.RR-02, GV.PO-01

## Procedura

### Passo 1 - Verifica obblighi sostanziali (art. 23 co. 1)

| # | Obbligo | Adempimento? | Evidenza | Gap? |
|---|---------|---------------|----------|-------|
| 1.a | L'organo di amministrazione **approva** le modalita' di implementazione delle misure di gestione dei rischi cyber (art. 24) | [SI/NO/PARZIALE] | [delibera, atto] | |
| 1.b | L'organo **sovrintende** all'implementazione degli obblighi del Capo IV (artt. 23-29) e della registrazione/aggiornamento ex art. 7 | [SI/NO/PARZIALE] | [report, agenda CdA] | |
| 1.c | L'organo e' consapevole della **responsabilita' personale** per le violazioni del decreto | [SI/NO/PARZIALE] | [attestato formazione, verbale CdA] | |

Note operative:
- Per il punto 1.a: serve atto formale del CdA (delibera) che approvi il documento "Piano di implementazione misure NIS2 art. 24" o equivalente. La sola adozione tecnica da parte del management IT non basta.
- Per il punto 1.b: il CdA deve ricevere periodicamente lo stato di implementazione e di registrazione sulla piattaforma ACN (es. report del CISO al CdA).
- Per il punto 1.c: la responsabilita' personale e' giuridica (art. 38 co. 5-6); deriva dal ruolo, non dall'opt-in.

### Passo 2 - Verifica formazione (art. 23 co. 2)

| # | Obbligo | Adempimento? | Evidenza | Gap? |
|---|---------|---------------|----------|-------|
| 2.a | I membri dell'organo di amministrazione e direttivi **seguono una formazione** in materia di sicurezza informatica | [SI/NO/PARZIALE] | [attestato per membro] | |
| 2.b | L'organizzazione **promuove l'offerta periodica** di formazione cyber per i dipendenti | [SI/NO/PARZIALE] | [piano formazione, registro presenze] | |

Note operative:
- Il decreto non specifica numero di ore o ente erogatore. Una pratica difendibile: corso annuale di awareness + briefing tematici quando emergono minacce/cambi normativi.
- La formazione del CdA deve essere documentata (attestato, registro presenze, programma).
- La formazione dei dipendenti deve essere periodica e adeguata al ruolo (PR.AT-01 base + PR.AT-02 per ruoli specializzati IT/sicurezza).

### Passo 3 - Verifica informazione (art. 23 co. 3)

| # | Obbligo | Adempimento? | Evidenza | Gap? |
|---|---------|---------------|----------|-------|
| 3.a | L'organo di amministrazione e' informato **su base periodica** degli incidenti e delle notifiche ex art. 25-26 | [SI/NO/PARZIALE] | [report periodico, sintesi] | |
| 3.b | L'organo e' informato **tempestivamente, se opportuno**, in caso di incidenti significativi | [SI/NO/PARZIALE] | [escalation procedure] | |

Note operative:
- Cadenza tipica: report trimestrale + escalation immediata per incidenti significativi (notificati al CSIRT Italia).
- Il report deve includere: numero incidenti, classificazione, esito notifiche al CSIRT, lessons learned, gap residui.
- Procedura di escalation deve essere documentata e approvata.

### Passo 4 - Mappatura ai requisiti ACN

Le sottocategorie del Framework Nazionale Cybersecurity (Det. ACN 379907/2025 Allegato 2) richiamano l'organo di amministrazione direttamente:

| Sottocategoria | Requisito ACN |
|----------------|----------------|
| GV.RR-02 | "L'organizzazione per la sicurezza informatica e' definita, **approvata dagli organi di amministrazione e direttivi** e resa nota". Riesame almeno biennale. |
| GV.PO-01 | "Le politiche di sicurezza informatica per i 16 ambiti obbligatori sono **approvate dagli organi di amministrazione e direttivi**". |
| GV.RR-04 | Gestione del personale autorizzato e amministratori di sistema con valutazione di esperienza, capacita', affidabilita'. Clausole contrattuali post-cessazione. |

Conformita' a queste sottocategorie e' verificabile via:
- Delibera CdA con approvazione politiche
- Documento di organizzazione per la sicurezza con designazione ruoli
- Procedure HR per vetting e clausole

### Passo 5 - Sintesi e output

```markdown
# Check obblighi governance NIS2 - [organizzazione]

**Data verifica**: [data]
**Soggetto**: [classificazione: essenziale/importante]
**Organo di amministrazione**: [composizione: N membri + Presidente + Amministratore delegato]

## Esito sintetico

| Area | Stato |
|------|-------|
| Approvazione misure (art. 23 co. 1 lett. a) | [Conforme / Parziale / Non conforme] |
| Sovrintendenza implementazione (art. 23 co. 1 lett. b) | [...] |
| Consapevolezza responsabilita' (art. 23 co. 1 lett. c) | [...] |
| Formazione organo (art. 23 co. 2 lett. a) | [...] |
| Formazione dipendenti (art. 23 co. 2 lett. b) | [...] |
| Informazione incidenti (art. 23 co. 3) | [...] |

## Gap rilevati

| ID | Gap | Priorita' | Effort | Owner | Scadenza |
|----|-----|-----------|--------|-------|----------|
| 1 | Politiche cyber non formalmente approvate dal CdA | Alta | M | Legal + CdA | T+3 mesi |
| 2 | Formazione cyber CdA mai erogata | Alta | M | HR + CISO | T+6 mesi |
| ... | ... | ... | ... | ... | ... |

## Raccomandazioni operative

### Atti formali da adottare
- Delibera CdA: approvazione politiche di sicurezza informatica per i 16 ambiti (GV.PO-01)
- Delibera CdA: approvazione organizzazione per la sicurezza, designazione ruoli e responsabilita' (GV.RR-02)
- Delibera CdA: approvazione piano di implementazione misure ex art. 24
- Delibera CdA: designazione del punto di contatto NIS e sostituto (art. 7)

### Programma di formazione
- **CdA**: corso introduttivo annuale + briefing su novita' normative + simulazioni di crisi cyber (table-top)
- **Top management**: corso annuale + scenario-based exercise
- **Dipendenti**: e-learning awareness annuale + phishing simulation periodica
- **Ruoli specializzati IT/sicurezza**: formazione tecnica continua (CISSP, CISM, CEH, ecc.)

### Reporting al CdA
- Report trimestrale: stato implementazione misure, incidenti, notifiche, gap residui
- Escalation immediata: incidenti significativi, scoperta di compromissioni, ispezioni ACN
- Riesame annuale: revisione politiche, organizzazione cyber, programma formazione

## Esposizione sanzionatoria

In caso di mancato adempimento art. 23, l'art. 38 co. 8 lett. a) richiama l'art. 23 fra le violazioni con sanzioni:
- **Soggetti essenziali (privati)**: fino a **10M EUR o 2% fatturato annuo mondiale**, se superiore. Minimo 1/20 del massimo.
- **Soggetti importanti (privati)**: fino a **7M EUR o 1.4% fatturato annuo mondiale**, se superiore. Minimo 1/30 del massimo.
- **PA Allegato III** essenziali: 25.000 - 125.000 EUR. Importanti: ridotti di 1/3.

Inoltre, ai sensi dell'art. 38 co. 5-6, le persone fisiche con ruolo di rappresentanza/decisione/controllo (incluso CdA, AD, rappresentante legale) possono essere ritenute responsabili per le violazioni e subire la **sanzione amministrativa accessoria di incapacita' a svolgere funzioni dirigenziali** se il soggetto non ottempera alla diffida.

## Limiti di questa verifica

- Verifica documentale: si basa sulle evidenze fornite (delibere, attestati, report). Non sostituisce un audit di conformita'.
- Non valuta la sostanza tecnica delle misure (per quella vedere `gap-analysis-misure.md`).
- Le pratiche raccomandate (frequenza formazione, struttura reporting) sono buone pratiche; il decreto non fissa parametri quantitativi rigidi.

## Rinvio al CISO / Legal / Compliance / Segreteria CdA

L'output e' di supporto. La predisposizione e tracciamento delle delibere, degli attestati di formazione e dei report al CdA spetta a Legal/Compliance/Segreteria CdA. Il CISO supporta il contenuto sostanziale. La verifica formale di adeguatezza puo' richiedere consulente legale specializzato in compliance cyber.
```

## Casi tipici (esempi orientativi)

| Caso | Stato governance | Esito |
|------|-------------------|-------|
| CdA che ha gia' approvato ISMS ISO 27001 + report trimestrale CISO | Maturo | Conforme con piccoli gap (verifica copertura 16 ambiti GV.PO-01) |
| PMI manifatturiera con AU (amministratore unico), no formazione, no policy formali | Iniziale | Gap critici - serve programma intensivo |
| Holding con CdA quotato, comitato sicurezza, CISO dedicato | Maturo | Tipicamente conforme; verificare evidenze formali |
| PA centrale con responsabile transizione digitale e RTD | Strutturata | Probabile conformita' se gia' allineata a Linee guida AgID; verificare integrazione con Legge 90/2024 |

## Limiti di questo task

- Non valida la sostanza tecnica delle misure (vedere `gap-analysis-misure.md`).
- Non sostituisce un audit di conformita'.
- Le sanzioni indicate sono indicative; per il calcolo concreto serve la lettura art. 38 (criteri di determinazione, riduzioni, accessorie).
- Per soggetti esteri stabiliti in Italia, l'art. 5 sulla giurisdizione e l'art. 38 co. 5 (rappresentante legale) richiedono valutazione specifica.

## Esempi

Vedi `examples/`:
- `essenziale-utility-energia/` - governance di utility con CdA strutturato
