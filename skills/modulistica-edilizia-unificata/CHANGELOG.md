# CHANGELOG - modulistica-edilizia-unificata

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
