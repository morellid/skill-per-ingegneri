# CHANGELOG - coordinatori-sicurezza-cantieri-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #277)
- Prima versione della skill di supporto al regime dei **cantieri temporanei o mobili** (Titolo
  IV) e al ruolo dei **coordinatori per la sicurezza**, ai sensi degli **artt. 89-92 del D.Lgs.
  9 aprile 2008, n. 81**, nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9 aprile 2008, n. 81** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831
    (codice 008G0104). Artt. 89-92 via `caricaArticolo` (idGruppo 18).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-titolo4-artt-89-92.md`: artt. 89,
    90, 91, 92 per intero (testo vigente, con i blocchi (( )) dei provvedimenti successivi).
- Estratto operativo `references/estratti/coordinatori-cantieri-checklist.md`.
- Due task: `verifica-obbligo-coordinatori.md` e `obblighi-committente-cantiere.md`.
- Due esempi: ristrutturazione con due imprese (nomina CSP/CSE); piccolo lavoro privato
  < 100.000 euro (esonero c. 11).

### Contenuto ancorato al testo
- Art. 89 definizioni (cantiere, committente, responsabile lavori, CSP, CSE con incompatibilita',
  imprese affidataria/esecutrice, POS). Art. 90 committente: nomina CSP/CSE quando piu' imprese
  (c. 3-5), verifica idoneita'/DURC/patente (c. 9), notifica preliminare art. 99, sospensione
  del titolo (c. 10), esonero < 100.000 euro (c. 11). Art. 91 CSP: PSC + fascicolo. Art. 92 CSE:
  vigilanza su PSC/POS, contestazione e proposta di sospensione, sospensione diretta.

### Scope e limiti
- Non nomina i coordinatori ne' verifica i requisiti (art. 98). Non redige PSC/POS/fascicolo ne'
  riproduce gli allegati (X, XV, XVI, XVII): rinvio agli atti e a `pos-allegato-xv-checker`. Non
  sostituisce committente, CSP, CSE ne' organo di vigilanza. Non tratta gli obblighi delle
  imprese/lavoratori (artt. 95-97) se non come richiamo.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo hash)
  e verificare le modifiche (es. patente a crediti art. 27; testo tra `(( ))`).
- Validazione Livello 2 con CSP/CSE esperto / RSPP di settore edile.
