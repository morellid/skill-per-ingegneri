# CHANGELOG - contabilizzazione-calore-dlgs102

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #311)
- Prima versione della skill di supporto all'inquadramento della **contabilizzazione
  del calore** e della **ripartizione delle spese** negli edifici/condomini con impianto
  centralizzato o teleriscaldamento, ai sensi del **D.Lgs. 102/2014, art. 9, comma 5**,
  nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 4/7/2014 n. 102** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: a98de115bcdf02e510241c305ff1903e64b83f2e76b62580cdc8857ef1b3c925
    (codice 14G00113). Art. 9 versione 8, idGruppo 2, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-102-2014-art-9.md`.
- Estratto operativo `references/estratti/contabilizzazione-calore-checklist.md`.
- Due task: `verifica-obbligo-contabilizzazione.md` e `imposta-ripartizione-spese.md`.
- Due esempi: obbligo di contabilizzazione ed esenzione con ripartitori (art. 9 c. 5
  a-c); ripartizione delle spese con quota >= 50% ai prelievi volontari (art. 9 c. 5 d).

### Contenuto ancorato al testo
- Art. 9 c. 5: contatore di fornitura (a, dal 30/6/2017), sotto-contatori per unita' ove
  tecnicamente possibile ed efficiente (b, UNI EN 15459, relazione tecnica per
  esenzioni), termoregolazione e contabilizzazione individuale in alternativa (c),
  ripartizione con quota >= 50% ai prelievi volontari e quota residua per millesimi/mq/
  mc/potenze (d, UNI 10200; prima stagione ai soli millesimi; facoltativa per edifici
  gia' provvisti); c. 5-bis lettura da remoto (post 25/10/2020; tutti entro 1/1/2027); c.
  5-ter nessuna deroga per nuove costruzioni; c. 5-quater guida ENEA per differenze di
  fabbisogno per mq > 50%.

### Scope e limiti
- Non calcola millesimi termici, quote o efficienza in termini di costi (UNI 10200/EN
  15459), non redige la relazione tecnica di esenzione ne' la tabella di ripartizione,
  non riproduce i provvedimenti ARERA (art. 9 cc. 1-4), non tratta la diagnosi energetica
  (art. 8) ne' il DPR 74/2013, non sostituisce il progettista/termotecnico o
  l'amministratore. Le norme UNI 10200 e UNI EN 15459 sono citate e non riprodotte.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 102/2014 pinnato
  (nuovo hash) e rileggere l'art. 9 (testo tra `(( ))`).
- Validazione Livello 2 con termotecnico / amministratore di condominio.
