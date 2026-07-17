# CHANGELOG - mediazione-civile-conciliazione-dlgs28

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #286)
- Prima versione della skill di supporto alla **mediazione civile e commerciale** finalizzata alla
  conciliazione, ai sensi del **D.Lgs. 4 marzo 2010, n. 28** (artt. 5, 8, 11, 12; testo vigente post
  riforma Cartabia), nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 4 marzo 2010, n. 28** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: e09c1d946fd7e45485d81af5e5085e9c4a9968ab6c68cca64c7ab511a36a7ce0
    (codice 010G0050). Artt. 5, 8, 11, 12 (grp2) via `caricaArticolo`.
  - Trascrizione verbatim (commi operativi) in `references/fonti/dlgs-28-2010-artt-5-8-11-12.md`.
- Estratto operativo `references/estratti/mediazione-checklist.md`.
- Due task: `verifica-condizione-procedibilita.md` e `inquadra-procedimento-esito.md`.
- Due esempi: condizione di procedibilità in materia condominiale (art. 5); verbale/accordo ed
  efficacia esecutiva (artt. 11, 12).

### Contenuto ancorato al testo
- Art. 5 condizione di procedibilità e materie (condominio, diritti reali, divisione, successioni,
  locazione, responsabilità medica, ecc.), improcedibilità entro la prima udienza, condizione
  avverata col primo incontro senza accordo, esclusioni, cautelari non preclusi; art. 8 procedimento
  (primo incontro 20-40 gg, prescrizione/decadenza, partecipazione personale, assistenza avvocati,
  esperti); art. 11 conclusione (verbale con accordo, proposta e 7 gg, valore, deposito, conservazione
  triennale, autentica art. 2643 c.c.); art. 12 efficacia esecutiva (titolo esecutivo con avvocati /
  omologazione del presidente del tribunale).

### Scope e limiti
- Non svolge la mediazione, non redige il verbale/accordo, non fornisce il merito tecnico né la
  valutazione legale, non sostituisce mediatore/organismo/avvocato/giudice. Articoli richiamati (2,
  5-bis/ter/quater, 6, 8-bis, 13, 17) citati e non trascritti; tariffe (DM parametri) non riprodotte.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 28/2010 pinnato (nuovo hash) e
  rileggere gli articoli (materia soggetta a riforme frequenti).
- Validazione Livello 2 con avvocato/mediatore o organismo di mediazione.
