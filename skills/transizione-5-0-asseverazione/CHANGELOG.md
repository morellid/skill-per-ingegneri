# CHANGELOG - transizione-5-0-asseverazione

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-07-12

### Aggiornamento normativo (closes #196)
- **Trigger**: DL 27/3/2026 n. 38 art. 8 (GU n. 72 del 27/3/2026) come modificato dal DL 3/4/2026 n. 42 art. 1 (GU n. 78 del 3/4/2026) + avviso MIMIT 29/4/2026 "Pratiche tecnicamente ammissibili".
- Scaricate, hashate e lette le nuove fonti:
  - GU n. 72/2026 con DL 38/2026 SHA256: 1453625e5dcff27685791d0637d303863543996c04f86da354d90c1c06b4a80c
  - GU n. 78/2026 con DL 42/2026 SHA256: 9f512d7a8025066d6b1682090178b9f4bfff4c72e116c82a6b1cb58d33b6e051
  - Avviso MIMIT 29/4/2026 (HTML dinamico, hash non riproducibile: trascrizione committata, voce senza hash come le altre pagine di portale)
- Nuove trascrizioni in `references/fonti/`: `dl-38-2026-art-8.md` (art. 8 testo originario + artt. 18-19), `dl-42-2026-art-1-modifiche-dl-38.md` (testo vigente art. 8 co. 1, co. 3-bis, co. 4, co. 4-bis), `avviso-mimit-29-04-2026.md`
- Nuovo estratto `references/estratti/dl-38-42-2026-quadro-credito.md`: credito riconosciuto pari all'89,77% del richiesto nel limite di 1.302,3 mln EUR per il 2026, ricevute GSE dal 29/4/2026, compensazione F24 entro 31/12/2026 con codice tributo 7079, contributo co. 3-bis per FER e spese di certificazione, obblighi di conservazione quinquennale
- SKILL.md: descrizione, blocco vigenza normativa, fonti, limiti aggiornati al quadro 2026; nuova normative_ref "DL 38/2026 art. 8 (mod. DL 42/2026)"
- `tasks/verifica-ammissibilita.md` e `tasks/struttura-certificazione-ex-post.md`: nota sul quadro 2026 (finestre chiuse, uso del task per controlli e coerenza documentale)
- `sources.yaml`: aggiunte 3 fonti primarie + rinvio strutturale a L. 199/2025 art. 1 co. 770; fonti secondarie da monitorare (decreto MIMIT contributo co. 3-bis, decreto attuativo "Nuovo Piano Transizione 5.0", leggi di conversione); `last_verified: 2026-07-12`
- Il contenuto tecnico del calcolo dei risparmi (DM 24/7/2024 + circolare 25877/2024) resta invariato: l'art. 8 co. 3 DL 38/2026 lo richiama espressamente "anche ai fini delle attivita' di controllo"

## [0.2.0] - 2026-05-10

### Fixed (source-grounding remediation - closes #112)
- Scaricati e letti i 3 PDF primari su cui si basa la skill:
  - DM MIMIT-MEF 24 luglio 2024 (GU n.183/2024) SHA256: 6ceb304bbe503860ef73c978cc4eabcbdfe41d5c0a3521af6be09efb581e9b53
  - Circolare operativa MIMIT prot. 25877 del 16 agosto 2024 SHA256: 964798d9f97353cffe23a6327e479b09e7820401986e09869448ce405dd8e62f
  - FAQ MIMIT Transizione 5.0 aggiornamento 10 aprile 2025 SHA256: 6d051b5f18b64b1fd97f829f026e1677644ec552426cdc29625f8f70d559a6b3
- Aggiornato references/sources.yaml: sha256 reali inseriti per tutte e tre le fonti, md_path aggiunto per ciascuna, accessed aggiornato a 2026-05-10
- Creati references/fonti/ con trascrizioni verbatim dai PDF letti:
  - dm-24-07-2024-transizione50.md (artt. 1, 4, 9, 10, 12, 15, 16 verbatim dalla GU)
  - circolare-mimit-25877-2024.md (cap.1-2, tab.1-2, cap.2.1, Allegati III-IV-V verbatim)
  - faq-mimit-transizione50-10-04-2025.md (FAQ 2.3-2.15 verbatim)
- Corretto errore semantico in references/estratti/circolare-mimit-modelli-certificazioni.md:
  - Rimossa affermazione fabricata "3 anni precedenti" nella sezione Allegato III
  - La dichiarazione DICHIARA dell'Allegato III (pag.83 circolare) non contiene alcun periodo temporale: dichiara solo assenza di conflitto di interessi "ai sensi della vigente normativa in materia" e assenza di condanne penali
  - Testo sostituito con citazione verbatim dalla fonte letta

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill di asseverazione tecnica del Piano Transizione 5.0
- SKILL.md con frontmatter `license: MIT` e routing verso 4 task files
- agents/openai.yaml con metadata Codex
- 4 task files: `verifica-ammissibilita.md`, `calcola-riduzione-consumi.md`, `struttura-certificazione-ex-ante.md`, `struttura-certificazione-ex-post.md`
- references/sources.yaml con 11 fonti primarie e 3 fonti secondarie da valutare
- references/estratti/ con 6 estratti testuali strutturati:
  - `dl-19-2024-art-38.md`
  - `dm-24-07-2024-articoli-chiave.md`
  - `circolare-mimit-criteri-risparmio.md`
  - `circolare-mimit-modelli-certificazioni.md`
  - `faq-mimit-soggetti-certificatori.md`
  - `circolare-mise-2014-tep.md`
- 2 esempi (1 conforme manifatturiero meccanico 3,2 mln EUR + 1 non conforme cogenerazione gas naturale per violazione DNSH)
- AGENTS.md di dominio con convenzioni specifiche per la materia

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1)
- Da considerare draft finche' non passa validazione Livello 2 (vedi methodology/validazione.md)
- Validatore di Livello 2 da identificare: profilo EGE/ESCo con esperienza in asseverazioni T5.0 gia' presentate al GSE
- Verificare al prossimo aggiornamento: modifiche L. 207/2024 (Bilancio 2025) art. 1 co. 427-429, eventuali DM correttivi al DM 24/7/2024, FAQ MIMIT successive al 10/4/2025
- Hash SHA256 dei PDF normativi non popolati (campo `sha256: null` in sources.yaml): da popolare manualmente eseguendo `curl + shasum` come indicato nelle note di sources.yaml
