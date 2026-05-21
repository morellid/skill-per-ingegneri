---
name: pfte-allegato-i7-checker
description: Genera la checklist degli elaborati obbligatori e verifica la completezza di un Progetto di Fattibilita' Tecnico-Economica (PFTE) e di un progetto esecutivo ai sensi dell'art. 41 e dell'Allegato I.7 del D.Lgs. 31 marzo 2023 n. 36 (Codice dei contratti pubblici), come integrato dal correttivo D.Lgs. 209/2024. Use when the user needs to know which documents are mandatory for a PFTE given the type of intervention (new construction, ordinary or extraordinary maintenance, restauro, ristrutturazione, lavori su beni culturali), check that a submitted PFTE folder contains all required elaborati, or validate consistency between a PFTE and the related progetto esecutivo for Italian public works tendering. Target users are Italian civil engineers, RUP (Responsabili Unici del Procedimento), stazioni appaltanti, and consulting professionals working on opere pubbliche under the new Codice 2023.
license: MIT
area: appalti-opere-pubbliche
title: "PFTE Allegato I.7 Checker"
summary: "Checklist e verifica completezza degli elaborati di un PFTE / progetto esecutivo di lavori pubblici, integrato dal correttivo 2024"
normative_refs:
  - "D.Lgs. 36/2023 art. 41"
  - "Allegato I.7"
  - "D.Lgs. 209/2024"
version: 0.2.0
status: alpha
tags:
  - pfte
  - dlgs-36-2023
  - lavori-pubblici
---

# PFTE Allegato I.7 Checker

## Quando usare questa skill

Usare quando un ingegnere civile, un RUP o una stazione appaltante chiede di:
- Conoscere quali **elaborati sono obbligatori** per un PFTE in funzione di tipologia opera, importo, modalita' di affidamento e regime applicabile (BIM, espropri, VIA, manutenzione)
- **Verificare la completezza** di un PFTE gia' redatto rispetto all'art. 41 + Allegato I.7
- **Verificare la coerenza** fra PFTE e progetto esecutivo nello stesso procedimento (art. 41 co. 8)
- Identificare se l'intervento ricade nel **regime semplificato** per manutenzioni (art. 41 co. 5 / 5-bis correttivo 2024)
- Capire se occorrono **elaborati aggiuntivi** in caso di appalto integrato su PFTE (art. 21 Allegato I.7)

**Non usare** se l'utente chiede:
- Redazione "ex novo" del contenuto tecnico di un singolo elaborato (relazioni, calcoli strutturali, computo metrico): la skill lista gli elaborati richiesti, non li redige.
- Valutazione dell'**adeguatezza tecnica** dei contenuti (e' giudizio del progettista firmatario).
- Verifica della progettazione ai sensi dell'art. 42 del Codice (attivita' del verificatore qualificato, non della skill).
- Pareri in materia di gara, esclusione, ricorsi TAR (servono skill PR.2 / PR.3 dedicate, non ancora rilasciate).
- Stima del corrispettivo professionale (Allegato I.13): la skill richiama la regola, non calcola.

**Nota BIM e Bando Tipo n. 2/2026**: per le gare di servizi di ingegneria e architettura (SIA) di importo pari o superiore alla soglia europea, il Bando Tipo n. 2/2026 ANAC (Delibera 153/2026, in vigore dal 30 maggio 2026) codifica l'obbligo BIM ex art. 43 D.Lgs. 36/2023 come clausola strutturale del bando (> 2 milioni di euro, o alla soglia art. 14 c.1 lett. a per beni culturali). La skill gestisce il check sugli elaborati BIM del PFTE (voci g e p dell'art. 6 co. 7 Allegato I.7); per la conformita' dell'intero set documentale di gara con il Bando Tipo n. 2/2026 usare la skill `bandi-tipo-anac-checker`.

## Avvertenza

Questa skill e' uno strumento di supporto alla **verifica di completezza documentale** di un PFTE/esecutivo rispetto al Codice dei contratti pubblici. **Non sostituisce il giudizio del progettista firmatario, del RUP, ne' del verificatore della progettazione (art. 42 D.Lgs. 36/2023).** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non certifica la conformita' del progetto, non sostituisce la verifica di cui all'art. 42, non valida l'adeguatezza tecnica dei contenuti, e non produce documenti pronti al deposito o all'avvio della procedura di gara. Ogni output della skill richiede revisione e firma del professionista competente.

## Sotto-attivita' disponibili

Questa skill supporta tre sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Generazione checklist elaborati PFTE**: l'utente chiede "quali documenti servono per il PFTE?", "elenco elaborati", "cosa serve depositare" -> leggi [`tasks/genera-checklist-pfte.md`](tasks/genera-checklist-pfte.md)
- **Verifica completezza PFTE**: l'utente chiede "verifica questo PFTE", "controlla se e' completo", "manca qualcosa rispetto all'Allegato I.7" -> leggi [`tasks/verifica-completezza-pfte.md`](tasks/verifica-completezza-pfte.md)
- **Verifica coerenza PFTE / esecutivo**: l'utente chiede "verifica che l'esecutivo sia coerente con il PFTE", "controlla la coerenza fra i due livelli" -> leggi [`tasks/verifica-coerenza-esecutivo.md`](tasks/verifica-coerenza-esecutivo.md)

Se la richiesta non e' chiara, chiedi all'utente quale delle tre sotto-attivita' vuole eseguire e raccogli le **variabili di inquadramento** (categoria intervento, importo, espropri, BIM, VIA, modalita' di affidamento) prima di procedere.

## Processo generale

1. **Inquadra l'intervento**: chiedi all'utente le variabili minime - tipologia opera, importo stimato, espropri si/no, VIA si/no, BIM si/no, modalita' di affidamento (appalto integrato su PFTE oppure base di gara su esecutivo), regime manutenzione si/no.
2. **Identifica la sotto-attivita'**: usa il routing della sezione "Sotto-attivita' disponibili".
3. **Carica il task file** corrispondente.
4. **Applica la procedura** descritta nel task.
5. **Produci l'output** strutturato (checklist o report di completezza/coerenza) con citazione precisa dell'articolo o lettera (es. "art. 6 co. 7 lett. h Allegato I.7") per ogni voce.
6. **Concludi** sempre con:
   - elenco di **elementi non automaticamente verificabili** dalla skill (adeguatezza tecnica, qualita' progettuale, conformita' alle norme di settore)
   - rinvio alla **verifica del progettista firmatario** e, dove ricorra, del **verificatore ex art. 42** del Codice

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 31 marzo 2023 n. 36 - Codice dei contratti pubblici, art. 41 e Allegato I.7
- D.Lgs. 31 dicembre 2024 n. 209 - Decreto correttivo (modifiche all'art. 41, Allegato I.7, art. 43 BIM, art. 225-bis regime transitorio)
- ANAC Bando Tipo n. 2/2026 (Delibera 153/2026, GU n. 111 del 15/05/2026, in vigore dal 30/05/2026) - codificazione obbligo BIM e clausola AI per SIA sopra soglia
- MIT Linee Guida GID 2026 (20 febbraio 2026) - attuazione art. 43 BIM per stazioni appaltanti, processo PFTE-GID Schema 2, soglie e regime transitorio

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dlgs-36-art-41.md`](references/estratti/dlgs-36-art-41.md) - testo strutturato art. 41 (commi 1-15-quater)
- [`allegato-i7-pfte.md`](references/estratti/allegato-i7-pfte.md) - struttura Allegato I.7 + elenco elaborati PFTE (art. 6 co. 7)
- [`allegato-i7-esecutivo.md`](references/estratti/allegato-i7-esecutivo.md) - elenco elaborati progetto esecutivo (art. 22 co. 4)
- [`dlgs-209-2024-modifiche.md`](references/estratti/dlgs-209-2024-modifiche.md) - sintesi modifiche del correttivo
- [`anac-bando-tipo-n2-2026-bim-ai.md`](references/estratti/anac-bando-tipo-n2-2026-bim-ai.md) - clausole BIM e AI del Bando Tipo n. 2/2026 per gare SIA sopra soglia
- [`mit-gid-2026-bim-pfte.md`](references/estratti/mit-gid-2026-bim-pfte.md) - MIT Linee Guida GID: obbligo BIM, soglie, regime transitorio, elaborati BIM nel PFTE

## Limiti

Questa skill NON fa:
- Non e' la **verifica della progettazione ex art. 42** del Codice: quella richiede soggetto qualificato, indipendenza dal progettista, formale rilascio del rapporto di verifica.
- Non valuta la **adeguatezza tecnica** dei contenuti dei singoli elaborati (qualita' delle scelte progettuali, accuratezza dei calcoli, idoneita' delle soluzioni proposte).
- Non sostituisce il giudizio del **RUP** sulla congruita' del PFTE rispetto al DIP da lui redatto.
- Non valuta la **conformita' con norme di settore** (NTC 2018, prevenzione incendi, accessibilita', acustica, energia) - quelle sono oggetto di altre skill o del giudizio del progettista.
- Non produce **bandi di gara** o documentazione di gara (usare `bandi-tipo-anac-checker`).
- Non valuta la **legittimita' delle scelte di affidamento** (procedura aperta, ristretta, negoziata, soglie).
- Non integra automaticamente le **norme regionali** o speciali (es. opere di interesse strategico, beni culturali ex D.Lgs. 42/2004 - rinvio a normativa specifica).
- Non aggiorna automaticamente i **prezzari regionali** o le **tabelle del Ministero del Lavoro** per i costi di manodopera (art. 41 co. 13).
- Non gestisce la versione **pre-correttivo** del Codice (D.Lgs. 36/2023 v. 1 aprile 2023): le procedure avviate prima del 31/12/2024 possono ricadere in regime transitorio - rinvio al RUP.

**Ogni verifica prodotta dalla skill e' supporto al professionista, non sostituzione.**
