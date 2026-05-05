---
name: piano-lavoro-amianto
description: Supporta il precheck, la redazione guidata e la verifica del piano di lavoro per demolizione o rimozione di amianto ai sensi dell'art. 256 del D.Lgs. 81/2008, nel testo aggiornato dal D.Lgs. 31 dicembre 2025 n. 213, con uso operativo del DM 6 settembre 1994 per misure tecniche, DPI, decontaminazione e bonifica. Use when an Italian datore di lavoro, RSPP, CSP/CSE, consulente HSE, tecnico amianto, or impresa specializzata needs to decide whether an art. 256 piano di lavoro is required, prepare a structured draft before transmission to ASL/ATS/SPSAL, or review an existing plan for completeness and consistency.
license: MIT
---

# Piano di Lavoro Amianto (art. 256 D.Lgs. 81/2008 + DM 6 settembre 1994)

## Quando usare questa skill

Usare questa skill quando un **datore di lavoro**, **RSPP**, **coordinatore sicurezza**, **consulente HSE** o **impresa specializzata** deve:
- capire se l'intervento ricade nel perimetro del **piano di lavoro ex art. 256**;
- predisporre una **bozza strutturata** del piano prima dell'invio all'organo di vigilanza;
- verificare se un piano gia' scritto copre i **contenuti minimi obbligatori** e le principali misure tecniche di bonifica.

La skill e' pensata per lavori di **demolizione o rimozione di amianto o materiali contenenti amianto** da edifici, strutture, apparecchi, impianti e mezzi di trasporto. Il testo di riferimento sugli articoli amianto e' quello risultante dalle modifiche del **D.Lgs. 31 dicembre 2025 n. 213**, pubblicato il **9 gennaio 2026** ed entrato in vigore il **24 gennaio 2026**.

**Non usare** questa skill come unico strumento quando l'utente chiede:
- sole attivita' di **censimento, campionamento o monitoraggio** senza demolizione/rimozione;
- pareri legali su sanzioni, responsabilita' o contenzioso;
- progettazione esecutiva di confinamenti dinamici, calcoli impiantistici o piani di monitoraggio strumentale di dettaglio;
- verifica di pratiche rifiuti, trasporto o Albo gestori oltre il rinvio puntuale all'art. 212 D.Lgs. 152/2006.

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito o alla firma.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Precheck obbligo e dati minimi**: quando l'utente chiede se serve il piano di lavoro, se basta la notifica o quali dati raccogliere prima di scriverlo -> leggi [`tasks/valuta-obbligo-e-precheck.md`](tasks/valuta-obbligo-e-precheck.md)
- **Redazione guidata del piano**: quando l'utente chiede di compilare o impostare il piano di lavoro -> leggi [`tasks/redigi-piano-lavoro.md`](tasks/redigi-piano-lavoro.md)
- **Verifica di un piano esistente**: quando l'utente chiede di controllare completezza e coerenza di un piano gia' scritto -> leggi [`tasks/verifica-piano-lavoro.md`](tasks/verifica-piano-lavoro.md)

Se la richiesta e' generica ("aiutami con il piano amianto"), parti da `valuta-obbligo-e-precheck.md`.

## Processo generale

1. Identifica se il caso riguarda davvero **demolizione o rimozione** di amianto.
2. Carica il task file specifico.
3. Richiedi solo i dati necessari per quella sotto-attivita':
   - luogo e natura dei lavori;
   - tipo, quantita' e stato del materiale contenente amianto;
   - impresa esecutrice, lavoratori, formazione e sorveglianza sanitaria;
   - misure previste per confinamento, decontaminazione, DPI, rifiuti, pulizia finale.
4. Applica la procedura del task.
5. Produci output strutturato con riferimenti puntuali ad **art. 251, 256, 258, 259 D.Lgs. 81/2008** e al **DM 6 settembre 1994**.
6. Chiudi sempre ricordando che il piano deve essere verificato e firmato dal soggetto responsabile prima della trasmissione.

## Fonti normative

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie usate dalla skill:

- **D.Lgs. 31 dicembre 2025 n. 213** (GU n. 6 del 9 gennaio 2026), che aggiorna il testo degli articoli amianto del D.Lgs. 81/2008.
- **DM 6 settembre 1994** del Ministero della sanita', con metodologie tecniche per valutazione del rischio, bonifica, DPI e decontaminazione.

Estratti operativi in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non produce documenti auto-firmati o pronti al deposito
- Non sostituisce sopralluogo, campionamenti, misure ambientali o valutazioni del medico competente
- Non assume automaticamente che qualunque lavoro su MCA richieda l'art. 256: nei casi dubbi segnala la necessita' di verifica specialistica
- Non determina in via autonoma la categoria Albo o l'intera filiera rifiuti
- Non interpreta normativa regionale o modulistica ASL/SPSAL locale se non fornita dall'utente
