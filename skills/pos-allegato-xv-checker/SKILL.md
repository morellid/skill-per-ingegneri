---
name: pos-allegato-xv-checker
description: Guida la compilazione assistita e verifica la completezza e coerenza di un Piano Operativo di Sicurezza (POS) italiano rispetto ai contenuti minimi previsti dall'Allegato XV del D.Lgs. 9 aprile 2008 n. 81 e, se richiesto, secondo l'impostazione dei modelli semplificati del Decreto Interministeriale 9 settembre 2014. Use when the user needs to structure a POS draft, identify missing input data, validate a POS document for Italian construction safety compliance, check for missing mandatory sections, verify consistency between risk analysis and mitigation measures, or review safety cost computation. Target users are Italian civil engineers, coordinatori per la sicurezza (CSE/CSP), datori di lavoro di imprese esecutrici, and safety professionals.
license: MIT
---

# POS Allegato XV Checker

## Quando usare questa skill

Usare quando un ingegnere o coordinatore per la sicurezza chiede di:
- Impostare o compilare una **bozza assistita** di POS a partire dai dati di impresa, cantiere e lavorazioni
- Verificare che un Piano Operativo di Sicurezza (POS) contenga tutte le voci obbligatorie previste dall'Allegato XV D.Lgs. 81/2008
- Controllare la coerenza tra analisi dei rischi e misure di prevenzione/protezione
- Validare il computo dei costi per la sicurezza non soggetti a ribasso
- Revisionare la parte sul coordinamento con altre imprese e gestione interferenze

**Non usare** se l'utente chiede:
- Redazione automatica di un POS "pronto al deposito" senza dati completi, senza confronto col PSC e senza revisione professionale
- Valutazioni legali sulla responsabilita' del coordinatore
- Calcoli strutturali o dimensionamenti di opere provvisionali
- Verifiche di congruita' rispetto al PSC (richiede skill dedicata, futura)

## Avvertenza

Questa skill e' uno strumento di supporto alla **compilazione assistita e alla verifica** di un POS. **Non sostituisce il giudizio del coordinatore per la sicurezza in fase di esecuzione (CSE), del coordinatore in fase di progettazione (CSP) o del datore di lavoro dell'impresa esecutrice.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non certifica la conformita' del POS ne' produce documenti pronti al deposito. Ogni output della skill richiede revisione e firma del professionista.

## Sotto-attivita' disponibili

Questa skill supporta due flussi distinti: **compilazione assistita** e **verifica**. In base alla richiesta dell'utente, carica il task file appropriato:

- **Guida compilazione assistita POS**: l'utente chiede "aiutami a compilare il POS", "impostiamo il POS", "fammi una bozza sezione per sezione" → leggi [`tasks/guida-compilazione-pos.md`](tasks/guida-compilazione-pos.md)
- **Precheck bozza POS prima della firma**: l'utente chiede "controlla questa bozza POS prima di chiuderla", "fammi il precheck finale" → leggi [`tasks/precheck-bozza-pos.md`](tasks/precheck-bozza-pos.md)

- **Verifica completezza voci Allegato XV**: l'utente chiede "e' completo?", "mancano voci?", "verifica i contenuti minimi" → leggi [`tasks/check-completezza.md`](tasks/check-completezza.md)
- **Coerenza rischi - misure**: l'utente chiede "le misure sono adeguate ai rischi?", "c'e' coerenza?", "matching rischi/misure" → leggi [`tasks/check-coerenza-rischi.md`](tasks/check-coerenza-rischi.md)
- **Costi sicurezza**: l'utente chiede "verifica i costi", "sono giusti i costi non soggetti a ribasso?" → leggi [`tasks/check-costi-sicurezza.md`](tasks/check-costi-sicurezza.md)
- **Coordinamento e interferenze**: l'utente chiede "coordinamento con altre imprese", "gestione interferenze" → leggi [`tasks/check-coordinamento.md`](tasks/check-coordinamento.md)

Se la richiesta e' generica ("verifica questo POS"), **esegui tutte e quattro le verifiche in sequenza**, producendo un report integrato.
Se la richiesta e' "scriviamo il POS", **non inventare dati**: avvia prima la compilazione assistita e marca tutto cio' che manca come `DA COMPLETARE`.

## Processo generale

1. Chiedi all'utente se vuole **compilare** una bozza POS o **verificare** un POS/una bozza esistente.
2. Se deve compilare, raccogli i dati minimi di impresa, cantiere, lavorazioni, PSC, ruoli, attrezzature, sostanze, DPI, costi e subaffidi.
3. Se deve verificare, chiedi all'utente di fornire il POS (testo completo, PDF estratto, o sezioni rilevanti).
4. Carica il/i task file necessari.
5. Applica la procedura descritta in ciascun task.
6. Se stai guidando la compilazione, produci una **bozza strutturata** con:
   - campi confermati dall'utente
   - campi mancanti marcati `DA COMPLETARE`
   - note sui punti che richiedono confronto con PSC, DVR, PiMUS, nomine, attestati o allegati
7. Se stai facendo una verifica, produci un report strutturato con:
   - **Esito** (conforme / non conforme / dubbio)
   - **Problemi rilevati** (con citazione normativa precisa)
   - **Raccomandazioni** (cosa rivedere, dove)
   - **Limiti della verifica** (cosa la skill non ha potuto controllare)
8. Prima di consegnare una bozza compilata, esegui il task di precheck o, se l'utente non lo chiede, almeno segnala che e' raccomandato.
9. Concludi sempre con rinvio alla verifica del CSE/CSP o del datore di lavoro.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 9 aprile 2008 n. 81, in particolare art. 96, 100, Allegato XV
- Decreto Interministeriale 9 settembre 2014 sui modelli semplificati per POS, PSC, FO e PSS

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non valuta la congruita' del POS con il PSC del cantiere specifico (serve confronto incrociato)
- Non verifica la formazione effettiva dei lavoratori citati nel POS
- Non controlla la validita' delle certificazioni e DPI elencati
- Non sostituisce il sopralluogo in cantiere del CSE
- Non produce un POS definitivo e firmabile in autonomia: produce al massimo una bozza guidata da completare e validare
- Non giudica l'adeguatezza delle attrezzature scelte rispetto a specificita' del cantiere

**Ogni verifica prodotta dalla skill e' supporto al professionista, non sostituzione.**
