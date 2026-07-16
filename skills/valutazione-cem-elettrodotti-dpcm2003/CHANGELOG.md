# CHANGELOG - valutazione-cem-elettrodotti-dpcm2003

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #61)
- Prima versione della skill di supporto alla **verifica dei limiti CEM a 50 Hz** degli
  elettrodotti (D.P.C.M. 8/7/2003), nell'area `ambiente-territorio-mobilita`.
- Fonte letta e trascritta verbatim (Regola zero):
  - **D.P.C.M. 8 luglio 2003** - pagina ELI di Gazzetta Ufficiale (riferimento
    solo-online, `sha256: null`, `binary_path: null`; codice 03A09749). Artt. 1-8 e
    Allegato A letti via `caricaArticolo` e trascritti in
    `references/fonti/dpcm-8-7-2003.md`.
- Estratto operativo `references/estratti/limiti-cem-checklist.md`.
- Due task: `inquadra-limite-applicabile.md` e `imposta-verifica-fasce.md`.
- Due esempi: nuova scuola presso linea 220 kV (obiettivo di qualita' 3 µT); abitazione
  esistente presso linea 132 kV (limite 100 µT e attenzione 10 µT).

### Valori di riferimento (dal testo)
- Limite di esposizione: **100 µT** (induzione magnetica), **5 kV/m** (campo elettrico)
  - valori efficaci (art. 3 c.1).
- Valore di attenzione: **10 µT**, mediana 24 h, in aree gioco/abitativi/scolastici e
  luoghi con permanenza >= 4 h (art. 3 c.2).
- Obiettivo di qualita': **3 µT**, mediana 24 h, per nuovi elettrodotti/nuove aree (art. 4).

### Limite di fonte e scope
- La **metodologia di calcolo** delle fasce di rispetto e delle **DPA** (art. 6 c.2) e'
  approvata con **DM Ambiente 29/5/2008**, **non trascritto** (codice GU non risolto in
  questo ambiente al 2026-07-16): la skill copre il **quadro e la verifica dei limiti**,
  non il calcolo numerico della DPA.
- Non copre le **alte frequenze** (SRB/RF) ne' l'**esposizione professionale**.

### Note di sviluppo
- Fonte GU: rileggere via `caricaArticolo` (codice 03A09749) ad ogni aggiornamento.
  Verificare la reperibilita' del DM 29/5/2008 per aggiungere il calcolo delle fasce.
- Validazione Livello 2 con tecnico ARPA / esperto CEM.
