# CHANGELOG - modulistica-edilizia-unificata

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4-alpha] - 2026-05-18

### Changed (recepimento DL 66/2026 Piano Casa e DPR 73/2026 paesaggio - issue #167)

- **references/sources.yaml**: aggiornato `last_verified` a 2026-05-18. Aggiunte due nuove fonti
  con SHA256 verificato:
  - `dl-66-2026-piano-casa`: PDF GU n. 104 del 07/05/2026 scaricato
    (SHA256: be6c7748f4c89740769cc9c39d21c55f5e839dbf340364748cf7b7a1ea1a6d05).
  - `dpr-73-2026-paesaggio-dpr31-2017`: PDF GU n. 108 del 12/05/2026 scaricato
    (SHA256: ceca0ebe69b9c4646049eabfa731b951ececaffc29f0b2938bb732cd963392db).
  - `dpr-31-2017-paesaggistica-semplificata`: aggiunta nota sulle modifiche dal DPR 73/2026.
- **references/fonti/dl-66-2026-piano-casa.md** (NUOVO): trascrizione di artt. 1, 8, 9 del
  DL 66/2026 letti dal PDF GU n. 104/2026 via pdftotext. Art. 8 co. 1: rinvio a DL 76/2020
  art. 10 co. 7-ter per SCIA in luogo di PdC per demolizione/ricostruzione ERP. Art. 9: verifica
  che NON modifica artt. 10 o 22 DPR 380/2001 ne' Tabella A D.Lgs. 222/2016.
- **references/fonti/dpr-73-2026-paesaggio-dpr31-2017.md** (NUOVO): trascrizione integrale di
  art. 1 del DPR 73/2026 letto dal PDF GU n. 108/2026 via pdftotext. Modifiche a lettera A.27
  Allegato A (esclusione autorizzazione paesaggistica per caravan/case mobili/autocaravan in
  strutture ricettive all'aperto gia' autorizzate) e B.26 Allegato B (procedura semplificata
  per infrastrutture a rete in strutture ricettive all'aperto).
- **references/estratti/dl-66-2026-piano-casa.md** (NUOVO): estratto mirato con matrice di
  impatto sui regimi edilizi, inclusa la verifica negativa su art. 9 (no modifica TUE).
- **references/estratti/dpr-73-2026-paesaggio.md** (NUOVO): estratto mirato con sintesi delle
  modifiche a A.27 e B.26 e impatto per la skill.
- **tasks/determina-regime-edilizio.md**: aggiunta eccezione Piano Casa a Branch F
  (ristrutturazione edilizia) e Branch H (ristrutturazione urbanistica) con nota su SCIA per
  demolizione/ricostruzione ERP. Aggiornato passo 3 (pre-requisiti) con nota su DPR 73/2026
  per strutture ricettive all'aperto.
- **SKILL.md**: aggiornata `description` con riferimento a DL 66/2026 e DPR 73/2026;
  aggiornata sezione "Fonti normative" con le due nuove fonti e i nuovi estratti.

## [Unreleased]

### Fixed (source-grounding remediation - PR #154)
- `references/sources.yaml`: valorizzati gli SHA256 mancanti per le tre fonti residue con artefatti ufficiali verificati: snapshot HTML Normattiva congelata al `2026-05-11` per `dpr-380-2001-testo-unico-edilizia`, PDF GU ufficiale per `dlgs-222-2016-scia-2-tabella-a`, PDF istituzionale Funzione Pubblica/Allegato 1 per `modulistica-unificata-salva-casa-2025`.
- `references/fonti/dpr-380-2001-testo-unico-edilizia.md`: aggiornata la provenance sullo snapshot ufficiale Normattiva effettivamente hashato.
- `references/fonti/dlgs-222-2016-scia-2-tabella-a.md`: rimossa la dipendenza dal PDF non ufficiale e riallineata la fonte al PDF originale della Gazzetta Ufficiale.
- `references/fonti/modulistica-unificata-salva-casa-2025.md`: sostituita la limitazione "ZIP non letto" con la lettura diretta del PDF ufficiale `moduli_clean.pdf`.
- `references/estratti/dlgs-222-2016-tabella-a.md`, `references/estratti/dpr-380-2001-regimi-edilizi.md`, `references/estratti/modulistica-unificata-2025.md`: riallineati gli header di provenance agli artefatti ufficiali effettivamente verificati.

### Changed (source-grounding remediation - issue #102)
- **references/fonti/dl-69-2024-salva-casa.md** (NUOVO): trascrizione fedele dell'art. 1 del DL 69/2024 (lett. a-i) letto dal PDF della Gazzetta Ufficiale n. 124 del 29/05/2024 (SHA256: 2d228d11a11c1bff95ce71baaee04246ea329ef14b12785cf24aba6cd7677a05). Include il testo letterale delle modifiche a: art. 6 co. 1 lett. b-ter (tende/pergotende), art. 9-bis co. 1-bis (stato legittimo), art. 23-ter co. 1-bis/ter/quater/quinquies (cambio uso), art. 34-bis co. 1-bis/ter/2-bis/3-bis/ter (tolleranze), art. 36 (rubrica e ambito), art. 36-bis (sanatoria semplificata), art. 37.
- **references/fonti/dpr-380-2001-testo-unico-edilizia.md** (NUOVO): trascrizione degli articoli chiave del DPR 380/2001 vigente (artt. 3, 6, 6-bis, 9-bis, 10, 22, 23, 23-ter, 34-bis, 36, 36-bis) letti su Normattiva, integrata con il testo delle modifiche dal DL 69/2024. Nota: il PDF del testo consolidato non e' stato scaricato; articoli letti via Normattiva singolarmente.
- **references/fonti/dlgs-222-2016-scia-2-tabella-a.md** (NUOVO): trascrizione degli articoli 1-2 del D.Lgs. 222/2016 letti su Normattiva. LIMITAZIONE: la Tabella A sezione Edilizia (voci numerate) non e' stata letta perche' il PDF della GU 2016 non e' risultato scaricabile e il portale Normattiva non ha esposto il testo delle voci via WebFetch. Il file documenta la limitazione per il reviewer.
- **references/fonti/modulistica-unificata-salva-casa-2025.md** (NUOVO): trascrizione del contenuto dell'accordo Conferenza Unificata n. 35/CU del 27 marzo 2025 letto da statoregioni.it e funzionepubblica.gov.it. LIMITAZIONE: il file ZIP con i moduli editabili non e' stato aperto.
- **references/sources.yaml**: aggiornati `accessed`, `md_path` per le 4 fonti principali; aggiornato SHA256 per `dl-69-2024-salva-casa` (hash del PDF GU n. 124/2024 scaricato); aggiornata URL per `dl-69-2024-salva-casa` con URL diretto GU; aggiornato titolo e URL per `modulistica-unificata-salva-casa-2025`.
- **references/estratti/*.md**: aggiornati gli header di tutti e 4 gli estratti per referenziare i fonti/ creati, con note sulle limitazioni di accesso al testo sorgente.
- **Nota sulla tolleranza 6% (art. 34-bis co. 1-bis)**: documentato che la soglia SU < 60 mq = 6% e' stata aggiunta dalla L. 105/2024 (conversione) e non era nel DL 69/2024 originale.

### Planned
- Esempi aggiuntivi: ristrutturazione "pesante" con SCIA alternativa al PdC, intervento in zona vincolata paesaggistica con DPR 31/2017 All. B.
- Estensione con scheda specifica per **sanatoria a "doppia conformita' alleggerita"** (art. 36-bis) e differenze procedurali rispetto all'art. 36.
- Integrazione del **glossario opere di edilizia libera** (DM 2/3/2018) come tabella di lookup per le voci ricorrenti.

## [0.1.3-alpha] - 2026-04-29

### Fixed (revisione adversarial Codex - round 3, residui documentali)
- **`examples/README.md`**: sostituite le descrizioni vecchie del cambio uso "B&B 5 camere" con la versione coerente "foresteria lombarda art. 27 LR 27/2015" e dell'esempio sanatoria con la versione coerente "parziale difformita' rispetto a SCIA 2013, regime art. 37 -> art. 36-bis con verifica primaria di tolleranza esecutiva ex art. 34-bis co. 2".
- **`references/sources.yaml`**: corretta la nota sul Salva Casa che descriveva l'art. 36-bis come "sanatoria CILA/SCIA"; ora distingue art. 36-bis (parziali difformita' art. 34, variazioni essenziali art. 32, abusi SCIA art. 22) da art. 36 (assenza/totale difformita' PdC) e art. 6-bis co. 5 (CILA omessa).
- **`README.md`**: aggiornata versione da 0.1.0-alpha a 0.1.3-alpha.
- **Tolleranze esecutive negli esempi**: aggiunta esplicita la clausola "purche' non alterino la volumetria complessiva" (art. 34-bis co. 2) in `examples/sanatoria-semplificata-art36bis/{expected-output,note}.md`.
- **Tabella A "stessa categoria con opere"**: chiarito l'assorbimento del regime CILA-art. 6-bis nella SCIA del cambio uso ex co. 1-quinquies in `references/estratti/dlgs-222-2016-tabella-a.md`.

## [0.1.2-alpha] - 2026-04-29

### Fixed (revisione adversarial Codex - round 2)
- **Art. 19 co. 6-bis L. 241/1990 in materia edilizia**: corretto il termine inibitorio per la SCIA edilizia (30 gg, non 60 gg). Il co. 6-bis riduce il termine generale di 60 gg del co. 3.
- **Residui CILA -> art. 36-bis**: rimossi i riferimenti residui in `dpr-380-2001-regimi-edilizi.md`, `tasks/verifica-salva-casa.md`, `tasks/genera-elenco-allegati.md`, `references/estratti/modulistica-unificata-2025.md`, `tasks/determina-regime-edilizio.md`, `AGENTS.md`. Per CILA omessa vale solo art. 6-bis co. 5 (sanzione).
- **Art. 34-bis tolleranze esecutive**: corretto il riferimento al **co. 2** (non co. 1-bis). Il co. 1-bis disciplina le soglie graduate dimensionali, il co. 2 disciplina le tolleranze esecutive (mancata realizzazione elementi architettonici, irregolarita' geometriche, finiture, impianti, vani interni).
- **Art. 23-ter co. 1-bis**: chiarito che il mutamento all'interno della stessa categoria, sebbene "sempre consentito", richiede comunque il titolo SCIA ex art. 19 L. 241/1990 ai sensi del co. 1-quinquies (salvo condizioni regionali e comunali).
- **Foresteria lombarda**: corretto riferimento da "art. 38" a **art. 27** LR Lombardia 27/2015. Corretta la qualifica come attivita' **imprenditoriale** (non non-imprenditoriale come precedentemente indicato). Aggiunto limite 6 camere/14 posti letto.
- **Tabella A: tettoie e pergolati**: rimosso il residuo "tettoie/pergolati di limitate dimensioni e amovibili - edilizia libera". Sostituito con: tende, tende a pergola e pergotende (lett. b-ter) e VEPA (lett. b-bis); le tettoie stabili restano CILA/SCIA/PdC.

## [0.1.1-alpha] - 2026-04-29

### Fixed (revisione adversarial Codex)
- **Art. 36-bis**: corretto regime di silenzio (silenzio-**assenso** a 45 gg per il PdC in sanatoria; per la SCIA in sanatoria si applica il termine art. 19 co. 6-bis L. 241/1990) - estratto DPR 380, DL 69/2024, task `verifica-salva-casa.md`.
- **Art. 36-bis**: corretto ambito applicativo (parziali difformita' art. 34, variazioni essenziali art. 32, abusi del regime SCIA art. 22 ex art. 37; CILA omessa segue art. 6-bis co. 5; opere PdC/SCIA-alternativa-dovute in assenza/totale difformita' restano in art. 36).
- **Art. 34-bis**: corrette le soglie graduate per SU (`<60`, `<100`, `100-300`, `300-500`, `>500`) con riferimento agli interventi realizzati entro il 24 maggio 2024 e calcolo SU su superficie assentita (co. 1-ter).
- **Art. 23-ter**: riformulato il decision tree post Salva Casa secondo i commi 1-bis, 1-ter, 1-quater, 1-quinquies (zone A/B/C ammesse, categorie a/a-bis/b/c, esclusione obblighi standard/parcheggi minimi, titolo SCIA ex art. 19 L. 241/1990).
- **Art. 6**: rimossa la liberalizzazione generica delle "tettoie"; distinte VEPA (lett. b-bis) e tende/pergotende (lett. b-ter); le tettoie stabili restano CILA/SCIA/PdC.
- **Tabella A D.Lgs. 222/2016**: rimossi i fittizi gruppi A-I e sostituiti con i nomi delle tipologie ufficiali; chiarito che la citazione formale richiede il numero di voce della Tabella A vigente.
- **Notifica preliminare cantiere**: corretta la soglia art. 99 co. 1 D.Lgs. 81/2008 (200 uomini-giorno per unica impresa, non 500; cantieri ex art. 90 co. 3 con piu' imprese anche non contemporanee).
- **Esempio Brescia veranda**: riscritto il caso come parziale difformita' rispetto a SCIA 2013 (regime art. 37 -> art. 36-bis), con verifica primaria di tolleranza esecutiva ex art. 34-bis co. 1-bis. Corretti i termini procedimentali (60 gg art. 19 co. 6-bis per SCIA in sanatoria).
- **Esempio Milano cambio uso**: rinominato "B&B" come "foresteria lombarda" (LR 27/2015 art. 38) per coerenza con il limite di 4 camere del B&B in Lombardia (art. 29). Rimossi gli obblighi di standard/parcheggi minimi (esclusi dal co. 1-quater). Chiarita l'efficacia immediata della SCIA art. 19 (60 gg = termine inibitorio, non termine di efficacia).

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill Modulistica edilizia unificata + Salva Casa
- Task files: `determina-regime-edilizio.md`, `genera-elenco-allegati.md`, `verifica-salva-casa.md`
- Fonti normative consultate: DPR 380/2001 (Testo Unico Edilizia), D.Lgs. 222/2016 Tabella A sez. II Edilizia, DL 69/2024 conv. L. 105/2024 (Salva Casa), Modulistica unificata Conferenza Unificata 27/3/2025
- Estratti testuali strutturati: `dpr-380-2001-regimi-edilizi.md`, `dlgs-222-2016-tabella-a.md`, `dl-69-2024-salva-casa.md`, `modulistica-unificata-2025.md`
- Esempi: 1 caso CILA/SCIA borderline (manutenzione straordinaria con frazionamento) + 1 cambio destinazione d'uso post Salva Casa + 1 sanatoria semplificata art. 36-bis
- Documentazione dual-agent (Claude Code + OpenAI Codex)

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1: autore-driven, fonti pubbliche).
- Da considerare draft finche' non passa validazione Livello 2 con un ingegnere edile / architetto / geometra esperto in pratiche edilizie post Salva Casa o un operatore SUE/SUAP comunale (vedi `methodology/validazione.md`). Validazione tipica prevista: 10 interventi reali, confronto modulo proposto vs scelta corretta dello sportello SUE.
- I PDF delle fonti (DPR 380/2001 consolidato, D.Lgs. 222/2016, DL 69/2024 conv., modulistica 2025) non sono stati scaricati automaticamente: i campi `sha256` in `sources.yaml` sono `null`. Per popolarli eseguire manualmente `scripts/fetch-sources.sh modulistica-edilizia-unificata` (richiede permessi di rete) e committare sources.yaml aggiornato.
- Issue di riferimento: GitHub issue #1 ([P1] CT.3 Modulistica edilizia unificata + Salva Casa DL 69/2024).
