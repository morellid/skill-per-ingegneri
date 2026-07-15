# CHANGELOG - specifiche-tecniche-ict-appalti-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #50)
- Prima versione della skill di supporto documentale alla redazione delle
  specifiche tecniche di una procedura d'appalto ICT della PA e alla fase
  preliminare di analisi comparativa delle soluzioni software.
- Fonti scaricate, hashate e lette (Regola zero):
  - **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - pagina indice
    Normattiva pinnata a `!vig=2026-07-15`
    SHA256: 992ae62296b09154497fe37c8d5913723875006758692a5b3d23b66f7d1a211a
    (riproducibile, doppio download). Artt. 79 (Specifiche tecniche), 80
    (Etichettature) e **allegato II.5** (Parte I definizioni - incl. "specifica
    tecnica comune" nel settore TIC; Parte II A specifiche tecniche punti 1-8, B
    etichettature punti 1-4) letti via `caricaArticolo` e trascritti verbatim in
    `references/fonti/dlgs-36-2023.md`.
  - **D.Lgs. 7/3/2005 n. 82 (CAD)** - pagina indice Normattiva pinnata a
    `!vig=2026-07-15`
    SHA256: 2eebfb960aaa6500fd04ebde4544fcf8c7c612977ec1a443615e2790af6460c5
    (riproducibile, doppio download). Artt. 68 (Analisi comparativa delle
    soluzioni) e 69 (Riuso delle soluzioni e standard aperti) trascritti verbatim
    in `references/fonti/dlgs-82-2005-cad.md`.
- Estratto operativo `references/estratti/specifiche-tecniche-ict-checklist.md`
  (analisi comparativa, riuso, modalita' di formulazione, "o equivalente",
  etichettature).
- Due task: `analisi-comparativa-soluzioni.md` (art. 68-69 CAD) e
  `formula-specifiche-tecniche.md` (art. 79-80 + allegato II.5).
- Due esempi: specifica tecnica con marchio senza "o equivalente" (non conforme,
  allegato II.5 punto 6) e analisi comparativa preventiva per l'acquisto di un
  gestionale (art. 68 CAD).

### Note di source-grounding e scope
- Gli artt. 79 e 80 del Codice sono norme di rinvio all'allegato II.5 (operativo
  art. 70 c. 3): la disciplina sostanziale e' nell'allegato, trascritto verbatim.
- I **criteri di aggiudicazione / OEPV** (art. 108 del Codice) NON sono trattati:
  sono coperti dalla skill `oepv-valutatore-offerte-tecniche`.
- Le **Linee guida AgID** (analisi comparativa, riuso, publiccode.yml) e le norme
  tecniche UNI/EN/ISO/IEC (a pagamento) sono citate come rinvio, non riprodotte.
- I regolamenti UE 305/2011 e 1025/2012 richiamati nell'allegato II.5 sono citati,
  non riprodotti (eur-lex).

### Note di sviluppo
- Fonti statali: ad ogni aggiornamento riscaricare le pagine indice pinnate a un
  nuovo `!vig=` (nuovo hash) e rileggere gli articoli/allegato modificati
  (verificare i correttivi al Codice e le novelle al CAD).
- Validazione Livello 2 da effettuare con esperto di appalti ICT / RUP.
