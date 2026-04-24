---
name: pos-allegato-xv-checker
description: Verifica la completezza e coerenza di un Piano Operativo di Sicurezza (POS) italiano rispetto ai contenuti minimi previsti dall'Allegato XV del D.Lgs. 9 aprile 2008 n. 81 e s.m.i. Use when the user needs to validate a POS document for Italian construction safety compliance, check for missing mandatory sections, verify consistency between risk analysis and mitigation measures, or review safety cost computation. Target users are Italian civil engineers, coordinatori per la sicurezza (CSE/CSP), and safety professionals.
---

# POS Allegato XV Checker

## Quando usare questa skill

Usare quando un ingegnere o coordinatore per la sicurezza chiede di:
- Verificare che un Piano Operativo di Sicurezza (POS) contenga tutte le voci obbligatorie previste dall'Allegato XV D.Lgs. 81/2008
- Controllare la coerenza tra analisi dei rischi e misure di prevenzione/protezione
- Validare il computo dei costi per la sicurezza non soggetti a ribasso
- Revisionare la parte sul coordinamento con altre imprese e gestione interferenze

**Non usare** se l'utente chiede:
- Redazione di un POS da zero (questa skill verifica, non redige)
- Valutazioni legali sulla responsabilita' del coordinatore
- Calcoli strutturali o dimensionamenti di opere provvisionali
- Verifiche di congruita' rispetto al PSC (richiede skill dedicata, futura)

## Avvertenza

Questa skill e' uno strumento di supporto alla verifica di un POS. **Non sostituisce il giudizio del coordinatore per la sicurezza in fase di esecuzione (CSE) o del datore di lavoro dell'impresa esecutrice.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non certifica la conformita' del POS ne' produce documenti pronti al deposito. Ogni output della skill richiede revisione e firma del professionista.

## Sotto-attivita' disponibili

Questa skill supporta quattro verifiche distinte. In base alla richiesta dell'utente, carica il task file appropriato:

- **Verifica completezza voci Allegato XV**: l'utente chiede "e' completo?", "mancano voci?", "verifica i contenuti minimi" → leggi [`tasks/check-completezza.md`](tasks/check-completezza.md)
- **Coerenza rischi - misure**: l'utente chiede "le misure sono adeguate ai rischi?", "c'e' coerenza?", "matching rischi/misure" → leggi [`tasks/check-coerenza-rischi.md`](tasks/check-coerenza-rischi.md)
- **Costi sicurezza**: l'utente chiede "verifica i costi", "sono giusti i costi non soggetti a ribasso?" → leggi [`tasks/check-costi-sicurezza.md`](tasks/check-costi-sicurezza.md)
- **Coordinamento e interferenze**: l'utente chiede "coordinamento con altre imprese", "gestione interferenze" → leggi [`tasks/check-coordinamento.md`](tasks/check-coordinamento.md)

Se la richiesta e' generica ("verifica questo POS"), **esegui tutte e quattro in sequenza**, producendo un report integrato.

## Processo generale

1. Chiedi all'utente di fornire il POS (testo completo, PDF estratto, o sezioni rilevanti).
2. Chiedi se vuole una verifica specifica o completa.
3. Carica il/i task file necessari.
4. Applica la procedura descritta in ciascun task.
5. Produci un report strutturato con:
   - **Esito** (conforme / non conforme / dubbio)
   - **Problemi rilevati** (con citazione normativa precisa)
   - **Raccomandazioni** (cosa rivedere, dove)
   - **Limiti della verifica** (cosa la skill non ha potuto controllare)
6. Concludi sempre con rinvio alla verifica del CSE/CSP o del datore di lavoro.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 9 aprile 2008 n. 81, in particolare art. 96, 100, Allegato XV
- Linee guida CNI/INAIL su redazione POS (dove pubbliche)

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non valuta la congruita' del POS con il PSC del cantiere specifico (serve confronto incrociato)
- Non verifica la formazione effettiva dei lavoratori citati nel POS
- Non controlla la validita' delle certificazioni e DPI elencati
- Non sostituisce il sopralluogo in cantiere del CSE
- Non produce il POS stesso, solo lo verifica
- Non giudica l'adeguatezza delle attrezzature scelte rispetto a specificita' del cantiere

**Ogni verifica prodotta dalla skill e' supporto al professionista, non sostituzione.**
