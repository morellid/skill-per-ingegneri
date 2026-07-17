# CHANGELOG - valutazione-rischio-vibrazioni-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #305)
- Prima versione della skill di supporto alla **valutazione del rischio da vibrazioni
  meccaniche** (mano-braccio e corpo intero), ai sensi del **D.Lgs. 81/2008, Titolo
  VIII, Capo III** (artt. 200-205), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9/4/2008 n. 81** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 200, 201, 202, 203, 204, 205, idGruppo 37,
    flagTipoArticolo 0, via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-vibrazioni.md`.
- Estratto operativo `references/estratti/rischio-vibrazioni-checklist.md`.
- Due task: `classifica-esposizione-vibrazioni.md` e
  `imposta-misure-sorveglianza-deroghe.md`.
- Due esempi: classificazione mano-braccio/corpo intero (art. 201); superamento del
  valore limite e deroga (artt. 203, 205, 204).

### Contenuto ancorato al testo
- Art. 200 definizioni (mano-braccio, corpo intero, A(8)); art. 201 valori limite
  mano-braccio 5 m/s² (breve 20)/azione 2,5, corpo intero 1,0 m/s² (breve 1,5)/azione
  0,5, con livello giornaliero massimo ricorrente; art. 202 valutazione e misurazione,
  allegato XXXV parti A/B, elementi da considerare; art. 203 programma di misure oltre
  i valori d'azione e misure immediate al superamento del limite; art. 204 sorveglianza
  sanitaria (obbligatoria oltre i valori d'azione, estesa secondo il medico); art. 205
  deroghe (navigazione, esposizioni occasionali - media 40 ore, organo di vigilanza max
  4 anni, sorveglianza intensificata).

### Scope e limiti
- Non misura né calcola i livelli di esposizione A(8), non redige il DVR-vibrazioni né
  la relazione tecnica, non tratta gli altri agenti fisici del Titolo VIII, non
  sostituisce il datore di lavoro, il tecnico competente o il medico competente. Artt.
  181, 182, l'allegato XXXV e le norme tecniche (UNI, ISO) citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato
  (nuovo hash) e rileggere gli artt. 200-205 (testo tra `(( ))`).
- Validazione Livello 2 con tecnico competente / medico competente.
