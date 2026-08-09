# CHANGELOG - impianti-fer-regimi-autorizzativi-dlgs190

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-08-09

### Added (closes #489)
- Prima versione alpha della skill sui regimi amministrativi degli impianti FER.
- Fonti scaricate, verificate via SHA256 e trascritte:
  - `references/fonti/dlgs-190-2024-regimi.md` - D.Lgs. 25 novembre 2024, n. 190, testo consolidato
    Normattiva al 9 agosto 2026: artt. 1, 5, 6, 7, 8, 9 e Allegati A, B, C.
  - `references/fonti/dm-mase-223-2026.md` - D.M. MASE 15 luglio 2026, n. 223, trascrizione integrale
    del PDF firmato (premesse, artt. 1-3).
- Estratti operativi: `references/estratti/triage-regimi-amministrativi.md` e
  `references/estratti/modello-unico-parte-iii-suer.md`.
- Task `tasks/classifica-regime-amministrativo.md` (progetto unico, allegati A/B/C, filtri dell'art.
  7, termini e documentazione) e `tasks/adempi-modello-unico-parte-iii.md` (trasmissione a SUER,
  termine ordinario e transitorio).
- Esempi: `examples/fv-copertura-capannone-attivita-libera/` (conforme) e
  `examples/fv-terra-progetto-unico-frazionato/` (problematico).

### Contenuto ancorato al testo
- I tre regimi e la ripartizione di competenza (art. 6 cc. 1-2; art. 9 c. 2: Allegato C Sez. I
  regione, Sez. II MASE).
- Regola del **progetto unico** e somma delle potenze (art. 6 c. 3); contrasto all'artato
  frazionamento (art. 7 c. 3, art. 8 c. 3).
- Filtri che escludono l'attività libera: art. 7 cc. 2, 4-6 (autorizzazione paesaggistica, 30 giorni
  con parere Soprintendenza in 20), c. 7, c. 8 (interferenze con opere pubbliche, fascia di rispetto
  stradale, nuovi accessi), c. 9 (esenzioni sempre valide).
- PAS: termini di silenzio-assenso 30/45/60 giorni, documentazione dell'art. 8 c. 4 lett. a)-m),
  compensazioni 1-3% oltre 1 MW, decadenza 2/3 anni, autotutela 6 mesi, riduzione di un terzo dei
  termini per Allegato B sez. I lett. q) e sez. II lett. d).
- Autorizzazione unica: verifica di assoggettabilità a VIA preventiva entro 90 giorni, art. 27-bis
  D.Lgs. 152/2006 con termine di 2 anni, istruttoria 10/20/10/30 (+90) giorni, consultazione
  pubblica 30 giorni, conferenza in 120 giorni con sospensioni 90/60/120, garanzie entro 120 giorni,
  compensazioni 1-4%, efficacia non inferiore a 5 anni.
- Modello Unico Parte III: 5 giorni dall'entrata in esercizio, 6 mesi per gli impianti già in
  esercizio, modello su SUER entro 15 giorni dall'entrata in vigore, ambito di Parte I e II fino a
  200 kW (D.M. 223/2026 artt. 1-2).
- Adeguamento regionale in 180 giorni e applicazione della disciplina previgente nelle more (art. 1
  c. 3).

### Scope e limiti
- Nessuna presentazione di istanze, nessuna compilazione di moduli.
- L'**Allegato 1** al D.M. 223/2026 (il modulo Parte III) **non è contenuto nel PDF** pubblicato: i
  campi non sono riprodotti.
- La **data di entrata in vigore** del D.M. 223/2026 non è ricavabile dal decreto (art. 3 c. 1:
  giorno successivo alla pubblicazione sul sito MASE, senza data): i termini di 15 giorni e 6 mesi
  sono espressi in forma relativa.
- Fuori scope: aree idonee (art. 11-bis), zone di accelerazione (art. 12), Allegato C-bis, Allegato
  D, modelli unici PAS/AU del D.M. 441/2025, discipline regionali, soglie VIA del D.Lgs. 152/2006.

### Note di sviluppo
- Skill non ancora validata da dominio terzo.
- Da considerare draft finche' non passa validazione Livello 2 (vedi methodology/validazione.md).
- Il D.Lgs. 190/2024 e' in evoluzione (novellato tra l'altro dal D.Lgs. 178/2025): a ogni
  aggiornamento vanno riscaricate e ritrascritte le fonti prima di toccare estratti, task ed esempi.
