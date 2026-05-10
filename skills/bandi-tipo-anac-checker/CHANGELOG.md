# CHANGELOG - bandi-tipo-anac-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha+fix.source-grounding] - 2026-05-10

### Fixed (source-grounding remediation semantica - issue #93)

- Aggiunto `references/fonti/` con trascrizioni verbatim delle fonti PDF:
  - `fonti/dlgs-36-2023-gu87-so14.md` - artt. 11, 74, 87, 90, 91, 94, 95, 96, 99,
    100, 101, 102, 104, 106, 117, 118, 119, 120 letti dal PDF GU n. 87/2023 SO n. 14
    (sha256: b139f0515a8aa018a25b7a31acce39fc39329cdc07aedd17e870dd9dc91025ff).
    Include sezione "CORREZIONI RISPETTO ALLA VERSIONE PRECEDENTE" con 10 errori critici
    trovati nella v0.1.0-alpha e corretti con il testo verbatim.
  - `fonti/anac-bando-tipo-n1-2023-delibera-365-2025.md` - struttura completa (30 sezioni)
    e clausole verbatim da PDF ANAC Bando tipo n. 1/2023 (Delibera 365/2025)
    (sha256: 8af1ec9dc5b645e1b2d88e700e44b5b65204c9582913eeb91a90afc665951241).
    Copre: ambito di applicazione, classificazione clausole (vincolante/facoltativa/alternativa),
    sezioni esclusioni, requisiti, avvalimento, subappalto, clausola sociale,
    garanzia provvisoria, soccorso istruttorio, garanzia definitiva.

- `sources.yaml` aggiornato:
  - SHA256 reali per dlgs-36-2023 e anac-bando-tipo-n1-2023 (erano placeholder).
  - Aggiunti campi `md_path` per le due fonti con file in `fonti/`.
  - `last_verified` aggiornato a 2026-05-10; `accessed` aggiornato a 2026-05-10.
  - URL corretto per ANAC bando tipo (URL diretto PDF).
  - Nota correttivo (D.Lgs. 209/2024): PDF non scaricabile alla data 2026-05-10; il bando
    tipo n. 1/2023 (Delibera 365/2025) recepisce gia' il correttivo, usato come riferimento.

- `references/estratti/dlgs-36-artt-clausole-disciplinare.md` riscritto integralmente:
  - Art. 74: corretto da "contenuto del bando" a "dialogo competitivo" (art. errato rimosso).
  - Art. 87: corretto da "DGUE" a "disciplinare di gara" (definizione e contenuto obbligatorio).
  - Art. 90: corretto da "comunicazioni durante la gara" a "informazioni ai candidati/offerenti
    post-aggiudicazione" (aggiudicazione, esclusione, nome aggiudicatario).
  - Art. 91: aggiunto come articolo autonomo (DGUE - compilato sulla PAD).
  - Art. 96 co. 6: self-cleaning correttamente attribuito ad Art. 96 co. 6 (non Art. 99).
  - Art. 99: corretto da "self-cleaning" a "verifica possesso requisiti (FVOE)".
  - Art. 102: corretto da "capacita' economica/finanziaria" a "impegni dell'operatore
    economico (stabilita' occupazionale, CCNL, pari opportunita')".
  - Art. 106: garanzia provvisoria al 2% (range 1-4%), riduzioni per certificazioni.
  - Art. 117: garanzia definitiva al 10% dell'importo contrattuale (non "5-10%").
  - Art. 118: corretto come "garanzie per lavori di particolare valore" (>100M EUR o
    contraente generale), non garanzia definitiva standard.
  - Art. 119: confermato nessun limite percentuale generale al subappalto.
  - Art. 120: corretto da "verifica requisiti subappaltatore" a "modifica contratti in
    corso di esecuzione".

- `references/estratti/anac-bandi-tipo-struttura-2023.md` riscritto integralmente:
  - Struttura corretta da 17 sezioni (errate) a 30 sezioni (reale del Bando tipo n. 1/2023).
  - Aggiunte classificazione clausole: vincolante, facoltativa, alternativa.
  - Tabella vecchio/nuovo codice aggiornata con righe aggiuntive ("art. 87 per DGUE",
    "garanzia definitiva 5-10%", "self-cleaning art. 99").
  - Aggiornata corrispondenza sezioni/articoli D.Lgs. 36/2023.

- `SKILL.md` corretto:
  - Sezione "Aree di verifica principali": artt. 94-98 corretti in artt. 94-96; art. 106
    per garanzia provvisoria; art. 117 per garanzia definitiva; art. 91 per DGUE.
  - Sezione "Fonti normative": lista articoli aggiornata.

- `tasks/check-conformita-disciplinare.md` corretto:
  - Passo 2: riferimenti articoli sezioni 5-8, 11, 15 corretti.
  - Passo 3: tabella indicatori aggiornata con righe "art. 87 per DGUE" e "5-10% definitiva".
  - Passo 4: clausole 4b, 4c, 4d, 4e corrette per riferimenti articoli e contenuto
    (PMI 20% in subappalto; tabella riduzioni garanzia provvisoria corretta).
  - Template report: aggiunta sezione "Garanzia definitiva (art. 117)".

- `tasks/identifica-anomalie-clausole.md` corretto:
  - Categoria A: tabella aggiornata con righe garanzia definitiva; DGUE da art. 87 a art. 91.
  - Pattern clausole mancanti: DGUE da art. 87 a art. 91.

## [0.1.0-alpha] - 2026-05-02 (rev 2 - post Codex adversarial review)

### Added
- SKILL.md: routing verso due sotto-attivita' (check-conformita', identifica-anomalie)
- AGENTS.md: convenzioni di dominio, articoli chiave D.Lgs. 36/2023, anti-pattern
- tasks/check-conformita-disciplinare.md: verifica strutturata con tabelle sezioni e clausole chiave
- tasks/identifica-anomalie-clausole.md: scansione anomalie per pattern (vecchio codice, subappalto, CCNL, ...)
- references/sources.yaml: D.Lgs. 36/2023 (originale + correttivo), 4 schemi ANAC 2023
- references/estratti/dlgs-36-artt-clausole-disciplinare.md: artt. 11, 74, 87, 90, 94-103, 117-120
- references/estratti/anac-bandi-tipo-struttura-2023.md: struttura schemi ANAC, tabella vecchio/nuovo codice
- examples/conforme-servizi-ppb/: disciplinare servizi informatici conforme SF-PPB
- examples/non-conforme-lavori-anomalie/: disciplinare lavori con 5 anomalie critiche tipiche
- agents/openai.yaml: metadata Codex (display_name, short_description, default_prompt)
- README.md: documentazione utente con installazione e limiti noti

### Fixed (post Codex adversarial review)
- Corretti articoli D.Lgs. 36/2023 errati: DGUE art. 87->91; garanzia provvisoria art. 117->106;
  garanzia definitiva art. 118->117; fatturato limit art. 102->100
- Chiarito che art. 87 D.Lgs. 36/2023 e' il disciplinare, NON il DGUE
- Aggiornate soglie europee a valori 2026: lavori 5.404.000; PA centrali 140.000;
  sub-centrali 216.000; settori speciali 432.000
- Ridotto catalogo schemi ANAC: rimossi 3 schemi non verificati; mantenuto solo Bando tipo n. 1/2023
  (Delibera n. 365/2025 confermato) per SF-OEPV; altri da verificare su portale ANAC
- Garanzia provvisoria: aggiunto range 1-4% (non solo 2%); nota su procedure sotto soglia
- Tabella vecchio/nuovo codice: aggiunta riga art. 85 D.Lgs. 50/2016 -> art. 91 D.Lgs. 36/2023 (DGUE)
- Aggiunto avvertenza su avvalimento (art. corretto da verificare su Normattiva)
- Aggiunto art. 57 (CAM), art. 58 (lotti), art. 60 (revisione prezzi) nella copertura

### Note di sviluppo
- Skill non ancora validata da RUP o consulente legale esterno
- Gli schemi ANAC non sono embedabili per intero: la skill verifica struttura e norme,
  non il testo verbatim degli schemi
- Numerazioni articoli D.Lgs. 36/2023 verificate nella revisione post-Codex ma occorre
  ulteriore verifica su Normattiva per gli articoli sull'avvalimento
- Closes GitHub issue #4
