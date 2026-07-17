# AGENTS.md - permesso-costruire-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al regime del **permesso di costruire**: caratteristiche del
titolo, presupposti per il rilascio, efficacia temporale e decadenza, procedimento e
termini, secondo il **D.P.R. 380/2001 (Testo unico edilizia), artt. 11, 12, 15, 20**.
Target: ingegneri/architetti (progettisti, tecnici SUE) e richiedenti del titolo.

**È una skill documentale**: inquadra presupposti, procedimento ed efficacia; **non
redige** la domanda/asseverazione, **non decide** il titolo (PdC vs SCIA/CILA), **non
calcola** il contributo, non sostituisce il SUE, il progettista o il Comune.

## Nota sull'area

Area **edilizia-urbanistica-catasto**. Distinta da `modulistica-edilizia-unificata`
(che seleziona il modulo/allegati per intervento e il titolo) e complementare alle
altre skill DPR 380 su agibilita', contributo di costruzione e vigilanza/abusi (che
coprono altri articoli): questa copre il **permesso di costruire** (artt. 11/12/15/20).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-permesso**: DPR 380/2001, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `bac3f7b1...`; codice 001G0429). Artt. 11, 12, 15 (idGruppo
  3) e 20 (idGruppo 5), flagTipoArticolo 0, caricati via `caricaArticolo` e trascritti
  verbatim.

Trascrizione in `references/fonti/dpr-380-2001-permesso.md`; estratto operativo in
`references/estratti/permesso-costruire-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 11**: legittimazione (proprietario/chi abbia titolo); trasferibilita' con
  l'immobile; irrevocabilita'; onerosita' (art. 16); non incide sulla proprieta' ne'
  limita i diritti dei terzi.
- **Art. 12**: conformita' agli strumenti urbanistici (c. 1); opere di urbanizzazione
  primaria esistenti/previste nel triennio/impegno (c. 2); misure di salvaguardia per
  strumenti adottati (c. 3-4).
- **Art. 15**: inizio 1 anno / ultimazione 3 anni (c. 1-2); decadenza di diritto salvo
  proroga (motivata; automatica c. 2-bis); nuovo permesso per la parte non ultimata
  (c. 3); decadenza per contrastanti previsioni urbanistiche salvo lavori iniziati e
  completati in 3 anni (c. 4).
- **Art. 20**: SUE e asseverazione (c. 1); responsabile del procedimento 10 gg (c. 2);
  istruttoria 60 gg (c. 3); modifiche/interruzione (c. 4-5); provvedimento 30 gg (40
  con 10-bis) (c. 6); raddoppio per progetti complessi (c. 7); silenzio-assenso e
  vincoli (c. 8); 75 gg per art. 22 c. 7 (c. 11); leggi regionali (c. 12); sanzioni
  per false attestazioni 1-3 anni (c. 13).

## Convenzioni specifiche

### Cosa NON fare
- Non **decidere** il titolo (PdC vs SCIA/CILA - art. 10): rinvio a
  `modulistica-edilizia-unificata`.
- Non **inventare** termini: usare 1 anno/3 anni (art. 15) e 60/30 giorni (art. 20).
- Non **redigere** domanda/asseverazione ne' calcolare il contributo (art. 16).

### Cosa fare
- **Verificare** presupposti e caratteristiche, **ricostruire** procedimento/termini
  ed **efficacia/decadenza**, con rinvio a progettista, SUE e Comune per l'istruttoria.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del DPR 380/2001 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere gli artt. 11, 12, 15, 20 (testo tra `(( ))` = modifiche successive, es.
Salva Casa DL 69/2024).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico SUE / esperto di diritto urbanistico).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-presupposti-caratteristiche.md`, `verifica-procedimento-termini-decadenza.md`)
- Esempi: 2 (presupposti/caratteristiche - artt. 11/12; termini, silenzio-assenso e decadenza - artt. 20/15)
