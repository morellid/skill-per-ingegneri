# CHANGELOG - piano-emergenza-antincendio-dm2021

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #242)
- Prima versione della skill di supporto all'**obbligo e alla struttura del piano di
  emergenza ed evacuazione** nei luoghi di lavoro (art. 46 D.Lgs 81/2008 + DM 2/9/2021),
  nell'area `sicurezza-lavoro-cantieri`.
- Candidata emersa dalla ricerca sistematica sul catalogo (scheda SL.4).
- Fonti scaricate/lette e trascritte verbatim (Regola zero):
  - **D.Lgs. 81/2008 art. 46** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831
    (codice 008G0104). Articolo via caricaArticolo.
  - **DM 2 settembre 2021** - pagina ELI di Gazzetta Ufficiale (riferimento solo-online,
    `sha256: null`, `binary_path: null`; codice 21A05748, GU SG n. 237 del 4/10/2021).
    Artt. 1-8 via caricaArticolo.
  - Trascrizioni in `references/fonti/piano-emergenza.md`.
- Estratto operativo `references/estratti/piano-emergenza-checklist.md`.
- Due task: `determina-obbligo-piano.md` e `struttura-piano-e-addetti.md`.
- Due esempi: ufficio con 8 dipendenti (piano non obbligatorio, misure nel DVR); negozio al
  pubblico con > 50 persone (piano obbligatorio nonostante < 10 lavoratori).

### Contenuto ancorato al testo
- Obbligo del piano (art. 2 c.2 DM: >= 10 lavoratori; > 50 persone al pubblico; attivita'
  DPR 151/2011), alternativa DVR se non obbligatorio (c.4), contenuti (c.3), designazione e
  formazione addetti (artt. 4-5), base e delega (art. 46 D.Lgs 81/2008), transitorie
  (sostituisce DM 10/3/1998; in vigore dal 4/10/2022).

### Scope e limiti
- Non esegue la valutazione del rischio incendio; non riproduce integralmente gli allegati
  I-II-III; non certifica il piano ne' sostituisce il progetto antincendio o le pratiche VV.F.

### Note di sviluppo
- Normattiva/GU: ad ogni aggiornamento riscaricare l'indice del D.Lgs 81/2008 (nuovo hash) e
  rileggere l'art. 46; rileggere il DM 2/9/2021 (codice 21A05748) e verificare gli allegati.
- Validazione Livello 2 con tecnico antincendio / RSPP.
