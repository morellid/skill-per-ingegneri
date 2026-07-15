# AGENTS.md - notifica-seveso-dlgs105

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi degli **stabilimenti a rischio di incidente
rilevante** (Seveso III, D.Lgs. 105/2015, attuazione dir. 2012/18/UE): ambito ed
esclusioni, classificazione soglia inferiore/superiore, notifica, politica di
prevenzione (PPIR), SGS, rapporto di sicurezza, sanzioni. Target: gestori,
RSPP/tecnici della sicurezza di processo, consulenti ambientali, CTR/ISPRA.

**E' una skill documentale**: non legge le soglie sostanza-specifiche, non
applica la regola della sommatoria, non redige RdS/PPIR/SGS ne' i piani di
emergenza.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-105-2015**: D.Lgs. 26/6/2015 n. 105, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile f117b299...,
  pattern della skill aua-dpr59-dossier). Articoli 2, 3, 13, 14, 15, 28 letti via
  AJAX (caricaArticolo) e trascritti verbatim in
  `references/fonti/dlgs-105-2015.md`.

Estratto operativo: `references/estratti/notifica-seveso-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 2): si applica agli stabilimenti con sostanze pericolose
  dell'allegato 1; **esclusioni** al c. 2 (militari, radiazioni ionizzanti,
  trasporto e deposito temporaneo intermedio connesso, condotte, miniere/cave,
  offshore, stoccaggio gas offshore, discariche).
- **Classificazione** (art. 3 lett. b-c): **soglia inferiore** = quantita' >=
  colonna 2 ma < colonna 3; **soglia superiore** = quantita' >= colonna 3
  (allegato 1, parti 1/2), con la **regola della sommatoria** (nota 4).
- **Notifica** (art. 13): gestore -> **CTR, Regione e soggetto designato, MASE
  tramite ISPRA, Prefettura, Comune, Comando provinciale VVF**; modulo allegato
  5; termini **180 gg prima** (costruzione nuovi) / **60 gg prima** (modifiche) /
  **1 anno** (altri); trasmissione telematica o **PEC firmata** (c. 5).
- **PPIR + SGS** (art. 14): TUTTI gli stabilimenti; linee guida allegato B;
  deposito presso lo stabilimento; termini 180 gg / 1 anno.
- **Rapporto di sicurezza** (art. 15): **solo soglia superiore**; elementi del
  c. 2 (allegato 3, scenari, piani d'emergenza interna, elementi al Prefetto).
- **Sanzioni** (art. 28): omessa notifica/RdS/PPIR **arresto fino a 1 anno o
  ammenda 15.000-90.000**; inadempimento prescrizioni RdS **6 mesi-3 anni +
  15.000-120.000**; **diffida (max 60 gg) -> sospensione (max 6 mesi) ->
  chiusura** (c. 8).

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre le **soglie** dell'allegato 1 ne' eseguire la **regola della
  sommatoria** (nota 4): rinviare all'allegato 1 e alla classificazione CLP.
- Non redigere RdS, PPIR, SGS ne' i piani di emergenza.
- Non citare "a memoria" termini/sanzioni: citare l'articolo (2, 3, 13, 14, 15,
  28).
- Non confondere il criterio di assoggettabilita' (art. 2/3) con gli obblighi
  conseguenti (artt. 13-15).

### Cosa fare
- Verificare prima le **esclusioni** (art. 2 c. 2), poi il superamento delle
  soglie (allegato 1), poi la classificazione (soglia inf./sup.).
- Distinguere gli obblighi comuni (notifica, PPIR/SGS) da quelli della sola
  soglia superiore (RdS).
- Citare destinatari, termini e sanzioni con l'articolo.
- Chiudere con il rinvio all'allegato 1/CLP e alle autorita' competenti.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto di sicurezza di
  processo / RIR).

## Stato attuale

- Versione: 0.1.0-alpha (closes #39)
- Task files: 2 (`verifica-assoggettabilita.md`, `checklist-adempimenti.md`)
- Esempi: 2 (deposito di soglia superiore soggetto; officina sotto soglia)
