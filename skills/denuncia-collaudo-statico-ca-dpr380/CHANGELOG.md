# CHANGELOG - denuncia-collaudo-statico-ca-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #354)
- Prima versione della skill di supporto al **progettista strutturale**, al **direttore dei lavori** e
  al **collaudatore statico** per le **opere in c.a./c.a.p. e a struttura metallica**, ai sensi del
  **D.P.R. 6 giugno 2001, n. 380, Parte II, Capo I, artt. 64-67**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **DPR 380/2001** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f (codice 001G0429, idGruppo 12).
    Artt. 64-67 via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dpr-380-2001-64-67.md` (artt. 64-67 per intero).
- Estratto operativo `references/estratti/denuncia-collaudo-statico-checklist.md`.
- Due task: `inquadra-denuncia-lavori.md` e `inquadra-collaudo-statico.md`.
- Due esempi: denuncia e adempimenti per nuova struttura in c.a.; collaudo statico (nuovo edificio) vs
  dichiarazione di regolare esecuzione (intervento locale).

### Contenuto ancorato al testo
- Progettazione/direzione da tecnico abilitato iscritto all'albo e responsabilita' di progettista,
  direttore dei lavori e costruttore (64); denuncia dei lavori allo sportello unico via PEC prima
  dell'inizio, allegati (progetto + relazione sui materiali), varianti, relazione a struttura ultimata
  entro 60 giorni con certificati dei laboratori ex art. 59, dati del c.a.p. e prove di carico,
  attestazione di deposito e trasmissione all'ufficio tecnico regionale (65); documenti in cantiere e
  giornale dei lavori (66); collaudo statico obbligatorio da ingegnere/architetto iscritto da almeno 10
  anni e indipendente, nomina contestuale alla denuncia, terna dell'ordine, 60 giorni dalla copertura,
  certificato via PEC equivalente al certificato di rispondenza ex art. 62, dichiarazione di regolare
  esecuzione del DL per interventi locali/riparazioni (67).

### Scope e limiti
- Non redige il progetto/relazione/certificato di collaudo, non esegue il calcolo ne' il collaudo, non
  riproduce le NTC 2018 ne' gli artt. 53/59/62/94-bis se non nei richiami. Non sostituisce il tecnico
  abilitato, il direttore dei lavori, il collaudatore ne' gli uffici competenti.

### Note di sviluppo
- Distinta da `denuncia-autorizzazione-sismica-dpr380` (artt. 93-94, zone sismiche).
- Ad ogni aggiornamento riscaricare l'indice pinnato del DPR 380/2001 (nuovo hash) e rileggere gli
  artt. 64-67. Validazione Livello 2 con collaudatore statico/strutturista.
