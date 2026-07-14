# CHANGELOG - trasmittanza-termica-opache-dm2015

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #29)
- Prima versione della skill code-driven per la trasmittanza termica U di
  strutture opache e la verifica dei limiti per zona climatica del DM 26/06/2015.
- Fonte scaricata, hashata e letta (Regola zero):
  - DM 26/06/2015 (MiSE, "requisiti minimi"), GU n. 162/2015 S.O. 39 (codice
    15A05198) SHA256: b69e130fd335b013e3ab817d03f8d93b9c36c547edf03155669d3bc33b10bb03
    (riproducibile, doppio download; host gazzettaufficiale.it; testo estraibile
    via pdftotext) -> trascrizione di Allegato 1 par. 5.2, Appendice A Tab. 1-5,
    Appendice B Tab. 1-4 in `references/fonti/dm-26-06-2015-requisiti-minimi.md`.
- Estratto operativo `references/estratti/dm-2015-limiti-trasmittanza.md` con le
  tabelle dei limiti e i caveat normativi.
- Modulo deterministico `tasks/lib/trasmittanza.py` (+ 19 test): calcolo
  U = 1/R_tot dalla stratigrafia e dalle resistenze superficiali fornite;
  lookup dei limiti per zona climatica, tipo, regime (Appendice B riqualificazione
  / Appendice A edificio di riferimento) e anno (2015/2021); incremento +30% per
  isolamento dall'interno o in intercapedine; verifica U <= limite.
- Task `tasks/calcola-trasmittanza.md`.
- Esempi: parete con cappotto EPS zona E (conforme, U = 0,213 <= 0,28) e muratura
  piena zona D con isolamento interno (non conforme anche col limite +30%).

### Nota di source-grounding (#29)
La scheda chiedeva "Uw + verifica DM 26/06/2015 (limiti per zona climatica)" e
segnalava il vincolo copyright sui lambda (norme UNI a pagamento). La skill e'
scoped di conseguenza:
- il DM 26/06/2015 (fonte ufficiale, pubblico) fornisce **solo i valori limite
  di U**, che sono stati trascritti dalle Appendici A e B del PDF;
- il **metodo** U = 1/R_tot e' fisica tecnica di pubblico dominio;
- i **lambda dei materiali** e le **resistenze superficiali R_si/R_se** (UNI/TS
  11300, UNI EN ISO 6946, a pagamento) NON sono riprodotti: sono input
  dell'utente, e il modulo rifiuta di procedere senza di essi. Nessun valore di
  norma UNI a pagamento e' committato.

### Note di sviluppo
- Verifica in regime 1D: i limiti del DM includono i ponti termici, il calcolo no
  -> sempre segnalata come preliminare.
- Validazione Livello 2 da effettuare con termotecnico (confronto con software di
  calcolo energetico, casi UNI/TS 11300).
- Possibili estensioni future: fattori di correzione per ambienti non
  climatizzati (con la relativa fonte), lookup lambda da database pubblici
  gratuiti (se disponibili e citabili), verifica dei serramenti su Uw dichiarata.
