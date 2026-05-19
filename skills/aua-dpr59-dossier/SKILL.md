---
name: aua-dpr59-dossier
description: Supporta la preparazione e l'autoverifica del dossier per l'Autorizzazione Unica Ambientale (AUA) ai sensi del D.P.R. 13 marzo 2013, n. 59. Use when l'utente prepara una nuova istanza AUA, un rinnovo o una comunicazione di modifica per impianti non soggetti ad AIA, oppure deve verificare quali titoli ambientali confluiscono nell'AUA e con quali termini procedurali.
license: MIT
area: ambiente-territorio-mobilita
title: "AUA - dossier ex D.P.R. 59/2013"
summary: "Preparazione e autoverifica del dossier AUA (D.P.R. 59/2013) per PMI e impianti non-AIA: perimetro art. 3 (9 titoli inclusi g-bis/g-ter), termini 90/120/150 gg + conferenza di servizi, rinnovo 15 anni, triage modifica sostanziale art. 6."
normative_refs:
  - "D.P.R. 13 marzo 2013, n. 59 (Regolamento AUA)"
  - "D.Lgs. 152/2006 (artt. 19, 20, 26, 108, 112, 215, 216, 269, 272)"
  - "L. 241/1990 (artt. 14-ter, 14-quinquies)"
version: 0.1.0-alpha
status: alpha
tags:
  - aua
  - dpr-59-2013
  - autorizzazione-ambientale
  - pmi
  - suap
---

# AUA - dossier ex D.P.R. 59/2013

## Quando usare questa skill

Questa skill aiuta tecnici e consulenti ambientali (PMI e impianti non-AIA)
a impostare il dossier per l'Autorizzazione Unica Ambientale ai sensi del
D.P.R. 13 marzo 2013, n. 59:

- impostare il **perimetro** dell'AUA (quali titoli sono compresi, quali no);
- verificare i **prerequisiti** (PMI, non-AIA, non-VIA assorbente);
- pianificare i **termini** procedurali (30/90/120/150 giorni, conferenza
  di servizi, durata 15 anni, rinnovo a 6 mesi dalla scadenza);
- distinguere fra **modifica sostanziale** e **non sostanziale** (art. 6).

La skill **non e' appropriata** per:

- impianti soggetti ad AIA (D.Lgs. 152/2006, Titolo III-bis Parte II);
- progetti con VIA assorbente (art. 26 co. 4 D.Lgs. 152/2006);
- predisposizione tecnica di singoli atti settoriali (es. calcolo
  scarichi, modelli di dispersione emissioni, valutazioni acustiche
  predittive): la skill copre l'aggregazione e la procedura AUA, non
  il merito tecnico dei titoli incorporati.

Target utente: ingegnere ambientale, consulente HSE, tecnico SUAP/Ente,
addetto ufficio ambiente PMI.

## Avvertenza

Questa skill e' uno strumento di supporto alla preparazione e all'autoverifica
del dossier AUA. **Non sostituisce il giudizio del professionista firmatario**
ne' l'istruttoria dell'autorita' competente. Le valutazioni di "modifica
sostanziale", l'applicabilita' di leggi regionali piu' restrittive o
ampliative, e la consultazione delle normative di settore di ciascun titolo
incorporato sono responsabilita' del tecnico. La skill non produce documenti
pronti al deposito o alla firma e non sostituisce la consultazione delle
discipline regionali AUA, che possono prevedere modulistica e termini
specifici.

## Sotto-attivita' disponibili

- **Verifica applicabilita' AUA**: prima di redigere il dossier, controllare
  se l'impianto rientra nell'ambito (PMI / non-AIA / non-VIA assorbente) e
  quali titoli abilitativi siano interessati. Caricare `tasks/check-applicabilita.md`.
- **Mapping titoli incorporabili**: dato un impianto con titoli ambientali
  attivi o da richiedere, individuare quali confluiscono nell'AUA ex art. 3
  co. 1 (lett. a-g, g-bis, g-ter) e quali eventualmente restano fuori.
  Caricare `tasks/mappa-titoli-art3.md`.
- **Pianificazione termini procedurali**: stimare i termini applicabili al
  procedimento (90, 120, 150 giorni), verificare l'attivazione della
  conferenza di servizi e produrre un cronoprogramma. Caricare
  `tasks/pianifica-termini.md`.
- **Pianificazione rinnovo**: a partire dalla data di rilascio dell'AUA,
  identificare la finestra dei 6 mesi prima della scadenza e preparare la
  checklist documentale per il rinnovo ex art. 5. Caricare
  `tasks/pianifica-rinnovo.md`.
- **Triage modifica sostanziale/non sostanziale**: classificare una
  modifica proposta (di attivita' o impianto) rispetto all'art. 6 e
  determinare il flusso procedurale corretto (comunicazione vs nuova
  istanza). Caricare `tasks/triage-modifica-art6.md`.

Se la richiesta dell'utente non rientra in queste cinque sotto-attivita',
chiedi quale tipo di supporto serve prima di procedere.

## Processo generale

1. Identifica la sotto-attivita' (tra le cinque sopra).
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi all'utente gli input minimi indicati nel task (tipologia attivita',
   titoli attualmente attivi, dimensione PMI, regione, ecc.).
4. Applica la procedura del task usando come fonte autoritativa il testo
   in `references/fonti/dpr-59-2013-articoli-1-12.md` e l'estratto guidato
   in `references/estratti/dpr-59-2013-aua-perimetro.md`.
5. Cita esplicitamente l'articolo e il comma del D.P.R. 59/2013 a fianco di
   ogni affermazione normativa (es. "art. 3 co. 1 lett. c"); per le
   normative collegate (Codice dell'Ambiente, L. 447/1995, D.Lgs. 101/2020,
   D.P.R. 160/2010, L. 241/1990) cita la norma con rinvio al testo Normattiva.
6. Concludi il report con un rinvio esplicito alla verifica del professionista
   e al controllo delle norme regionali applicabili (l'art. 3 co. 2 ammette
   ampliamenti del perimetro AUA da parte di Regioni e Province Autonome).

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Testo verbatim degli
articoli 1-12 in `references/fonti/dpr-59-2013-articoli-1-12.md`. Estratto
operativo in `references/estratti/dpr-59-2013-aua-perimetro.md`.

## Limiti

Cosa questa skill NON fa:

- Non sostituisce la modulistica regionale specifica (le Regioni adottano
  proprie modulistiche AUA spesso veicolate via SUAP).
- Non valuta nel merito i singoli titoli incorporati (es. non calcola
  portate scarichi, non verifica limiti di emissione settoriali, non
  classifica codici CER di un deposito rifiuti).
- Non fornisce stime di costo dei diritti istruttori (variano per regione
  e per ente; rinvio alle tariffe regionali ex art. 8).
- Non valuta l'applicabilita' a soggetti specifici di AIA o VIA: per
  questo si rimanda a strumenti dedicati e al D.Lgs. 152/2006.
- Non interpreta giurisprudenza amministrativa successiva al regolamento:
  l'estratto e' source-grounded sul testo del regolamento, non sulla
  prassi delle Regioni o sulle sentenze TAR/CdS.
