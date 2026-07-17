# AGENTS.md - denuncia-collaudo-statico-ca-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale**, al **direttore dei lavori** e al **collaudatore
statico** per le **opere in conglomerato cementizio armato** (normale e precompresso) **e a struttura
metallica**: soggetti e responsabilita', **denuncia dei lavori** allo sportello unico, documenti in
cantiere, **relazione a struttura ultimata** e **collaudo statico**, ai sensi del **D.P.R. 6 giugno
2001, n. 380, Parte II, Capo I, artt. 64-67**. Target: progettisti, direttori dei lavori, collaudatori,
uffici tecnici.

**E' una skill documentale per il tecnico**: inquadra obblighi, soggetti, documenti e termini; **non
redige** il progetto/relazione/certificato di collaudo, **non esegue** il calcolo ne' il collaudo.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Distinta da `denuncia-autorizzazione-sismica-dpr380` (artt. 93-94:
denuncia/autorizzazione nelle **zone sismiche**): questa copre gli adempimenti sulle **opere in c.a./
acciaio** (denuncia lavori, collaudo statico) validi in generale. Complementare a `segnalazione-
agibilita-dpr380` (il certificato di collaudo correda la SCA) e alle skill NTC (spettro, combinazioni,
periodo proprio) per la parte di calcolo.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-64-67**: DPR 380/2001, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `bac3f7b1...`; codice 001G0429, idGruppo 12). Artt. 64 (v1), 65 (v4), 66 (v1), 67 (v3) caricati via
  `caricaArticolo` (formato AKN) e trascritti verbatim.

Trascrizione in `references/fonti/dpr-380-2001-64-67.md`; estratto operativo in
`references/estratti/denuncia-collaudo-statico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Soggetti** (art. 64): progetto e direzione a **tecnico abilitato iscritto all'albo**;
  responsabilita' di progettista (c. 4), direttore dei lavori e costruttore (c. 5).
- **Denuncia** (art. 65): dal **costruttore** allo sportello unico via **PEC** prima dell'inizio, con
  progetto e relazione sui materiali (c. 3); varianti (c. 5); **relazione a struttura ultimata** del DL
  entro **60 giorni** con certificati dei laboratori **art. 59** (c. 6).
- **Documenti in cantiere** (art. 66): atti + **giornale dei lavori**, responsabilita' del DL.
- **Collaudo statico** (art. 67): obbligatorio (c. 1); **ingegnere/architetto iscritto da 10 anni** e
  **indipendente** (c. 2); nomina contestuale alla denuncia (c. 3) o **terna** dell'ordine (c. 4); **60
  giorni** dalla copertura (c. 5); certificato via PEC = certificato di rispondenza NTC (art. 62, c. 7);
  **dichiarazione di regolare esecuzione** del DL per interventi locali/riparazioni (cc. 8-bis, 8-ter).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il progetto strutturale, la relazione o il **certificato di collaudo**; non
  **eseguire** il calcolo di resistenza/stabilita' ne' il collaudo.
- Non riprodurre le **NTC 2018** (D.M. 17/1/2018) ne' gli artt. **53/59/62/94-bis**: rinvio.
- Non **qualificare** un intervento come "locale/di riparazione" al posto del progettista/DL: e' una
  valutazione tecnica secondo le NTC (rileva per gli artt. 65 c. 8-bis e 67 cc. 8-bis/8-ter).

### Cosa fare
- Inquadrare soggetti e responsabilita' (64), denuncia e allegati e relazione a struttura ultimata (65),
  documenti in cantiere (66), obbligo/requisiti/nomina/termini/certificato del collaudo (67).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del DPR 380/2001 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 64-67, verificando le modifiche dei doppi tondi `(( ))`.

## Validatori

- Non ancora assegnato (Livello 2 con collaudatore statico/strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #354)
- Task files: 2 (`inquadra-denuncia-lavori.md`, `inquadra-collaudo-statico.md`)
- Esempi: 2 (denuncia e adempimenti per nuova struttura in c.a.; collaudo statico vs dichiarazione di
  regolare esecuzione per intervento locale)
