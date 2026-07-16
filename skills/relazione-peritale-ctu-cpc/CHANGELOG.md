# CHANGELOG - relazione-peritale-ctu-cpc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #41)
- Prima versione della skill di supporto alla **struttura della relazione peritale**
  e alle **operazioni** del CTU nel processo civile (c.p.c. artt. 191-201), con
  inquadramento nell'**albo CTU** (D.M. 109/2023).
- Skill nell'**area di catalogo `forense`** (CTU & ingegneria forense), la seconda
  dell'area dopo `compensi-ctu-dpr115`.
- Fonti scaricate/lette e trascritte verbatim (Regola zero):
  - **c.p.c. artt. 191-201** - pagina indice Normattiva pinnata a `!vig=2026-07-16`
    SHA256: 7a53e745448ed3657d629b49a9f4c2e18eb08bfaa19f55e815e046793788c655
    (riproducibile, doppio download; codice 040U1443). Articoli caricati via
    caricaArticolo (idGruppo=28) e trascritti in
    `references/fonti/codice-procedura-civile-artt-191-201.md`.
  - **D.M. 109/2023** - pagina ELI di Gazzetta Ufficiale (riferimento solo-online,
    `sha256: null`, `binary_path: null`). Artt. 1-12 e settori della categoria
    INGEGNERIA (Allegato A) letti via caricaArticolo e trascritti in
    `references/fonti/dm-109-2023.md`.
- Estratto operativo `references/estratti/struttura-relazione-checklist.md`.
- Due task: `struttura-relazione.md` e `verbale-operazioni-peritali.md`.
- Due esempi: nomina/quesiti/termini con giuramento a firma digitale; verbale del
  primo sopralluogo con CTP presenti.

### Limite di fonte e scope
- La skill copre la **struttura e la procedura** (relazione, quesiti, verbale,
  termini) e l'**inquadramento nell'albo**; **non fornisce il contenuto tecnico/di
  merito** della perizia (rilievi, calcoli, conclusioni), che dipende dallo specifico
  quesito e dalla disciplina applicabile.
- L'**Allegato A** del D.M. 109/2023 e' una tabella con celle a capo multi-riga:
  trascritti verbatim solo i settori della categoria **INGEGNERIA**; per le altre
  categorie ingegneristiche si rinvia all'Allegato A.
- Non copre la **perizia penale** (c.p.p.) ne' la **liquidazione del compenso** (skill
  `compensi-ctu-dpr115`).

### Note di sviluppo
- Fonte Normattiva: ad ogni aggiornamento riscaricare la pagina pinnata (nuovo hash) e
  rileggere gli artt. 191-201 (versioni per articolo). Testo aggiornato da D.Lgs.
  149/2022 (Cartabia) e D.Lgs. 164/2024.
- Validazione Livello 2 con CTU/avvocato esperto di processo civile.
