# CHANGELOG - nis2-self-assessment

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0-alpha] - 2026-07-11

### Added (issue #197 - Det. ACN 155238/2026, categorizzazione attivita' e servizi)
- Nuovo task `tasks/categorizza-attivita-servizi.md` per la preparazione
  dell'elenco categorizzato delle attivita' e dei servizi ex art. 30
  D.Lgs. 138/2024 secondo il modello della Det. ACN 155238/2026: selezione
  allegato 1 vs allegato 2, identificazione delle attivita'/servizi
  (top-down / bottom-up / combinato), mappatura 1:1 nelle 10 macro-aree,
  attribuzione della categoria di rilevanza (default pre-assegnata, deroga
  ex art. 3 co. 3 con valutazione documentata, criteri Appendice B della
  Guida), casi speciali (Regolamento Cloud PA, PSNC, esenzione DORA),
  trasmissione nella finestra annuale 1 maggio - 30 giugno tramite il
  "Servizio NIS/Categorizzazione" e verifiche a campione ex art. 21
  Det. 127437/2026
- Nuovo estratto `references/estratti/acn-det-155238-2026-categorizzazione.md`
  che copre Det. 155238/2026 + allegati 1-2 + Guida alla categorizzazione
  v1.0 + Capo V (artt. 20-21) Det. 127437/2026
- Nuove trascrizioni verbatim PDF in `references/fonti/`:
  - `acn-det-155238-2026.md` - determinazione firmata 13/04/2026,
    prot. 155238 del 20/04/2026, premesse + artt. 1-8
  - `acn-det-155238-2026-allegato-1.md` e `acn-det-155238-2026-allegato-2.md` -
    tabelle delle 10 macro-aree con categorie pre-assegnate (unica
    differenza: Logistica, impatto basso vs minimo)
  - `acn-modello-categorizzazione-guida.md` - Guida alla lettura v1.0
    (aprile 2026), capp. 1-2 + Appendici A-B
- Nuove voci in `references/sources.yaml` completate con note di contenuto:
  - `acn-det-155238-2026` con SHA256 `7db5fd25e9020f68a8417eed2035d9cfa89f4a7f2b5b97b2ed978392c2dc4d2d`
  - `acn-det-155238-2026-allegato-1` con SHA256 `3d8c9965b8c02e98c15f05bc7e5cc62d4d3d9542f2dfa94d9d4b28f5da3c55eb`
  - `acn-det-155238-2026-allegato-2` con SHA256 `071fe9a5b012114b3828c60bb3bbb69a6d27ce95b19dcd5e8c151ed1c3a750bc`
  - `acn-modello-categorizzazione-guida` con SHA256 `c2ccc470a07ce0bd01f94276667f18e82a79de13bd498d5861b5a8f1ba72bd1b`

### Changed
- `SKILL.md`: description e summary del frontmatter estese con l'elenco
  categorizzato ex art. 30; aggiunta "Det. ACN 155238/2026" a
  `normative_refs`; nuova sotto-attivita' `categorizza-attivita-servizi.md`
  nel routing (sei azioni); sezione "Fonti normative" aggiornata
- `AGENTS.md`: dominio a sei angoli; nuove voci "Fonti autoritative"
  (Det. 155238/2026 + allegati, Guida); nuovi bullet "Articoli e punti
  chiave" (art. 30 + modello di categorizzazione; Capo V Det. 127437/2026);
  stato attuale aggiornato (6 task, 13 estratti)
- `README.md` di skill: allineato allo stato corrente (6 sotto-attivita',
  fonti consultate aggiornate, versione)
- `references/sources.yaml`: aggiunto `excerpt_paths` per le 4 nuove fonti
  e per `acn-det-127437-2026`; `last_verified` aggiornato a 2026-07-11
- `README.md` di root: riga della skill aggiornata con la
  Det. ACN 155238/2026
- `agents/openai.yaml`: short_description allineata alle sei
  sotto-attivita' (era ferma a quattro, non aggiornata in 0.2.0-alpha)

### Note
- Versione: minor (0.2.1 -> 0.3.0) per aggiunta di funzionalita' nuova
  retro-compatibile (nuovo task + nuove fonti), secondo
  `methodology/update-cycle.md`
- Chiude la voce "fuori scope" annotata nella release 0.2.0-alpha
  (GitHub issue #197)

## [0.2.1-alpha] - 2026-07-11

### Fixed (allineamento metadata - issue #194)
- `SKILL.md`: aggiunte "Det. ACN 127437/2026" e "Det. ACN 127434/2026" a
  `normative_refs`: erano gia' coperte dai contenuti della 0.2.0-alpha
  (task `elenco-fornitori-rilevanti.md`, estratti, sources.yaml) ma non
  dichiarate nel frontmatter; `summary` aggiornata con l'elenco fornitori
  rilevanti
- `README.md` di root: riga della skill allineata (descrizione e colonna
  riferimenti normativi)
- Verifica punto per punto della issue #194: i tre punti segnalati
  (istruzioni operative per la piattaforma ACN "NIS/Aggiornamento annuale
  informazioni", ricorrenza annuale della finestra 15 aprile - 31 maggio,
  criteri di rilevanza ex art. 1 co. 1 lett. ll) Det. ACN 127437/2026)
  risultano gia' coperti da `tasks/elenco-fornitori-rilevanti.md` e
  `references/estratti/acn-det-127437-2026-art18-fornitori.md` introdotti
  in 0.2.0-alpha (issue #169); nessuna modifica di contenuto necessaria

### Fixed (source-grounding remediation - PR #154)
- aggiunto `references/fonti/acn-det-164179-2025-allegato2.md` per la fonte storica `acn-det-164179-2025-allegato2`, cosi' da rispettare la Regola zero Step 3 anche per l'allegato superato mantenuto a catalogo come riferimento storico
- aggiornato `references/sources.yaml` con `md_path` per `acn-det-164179-2025-allegato2`

## [0.2.0-alpha] - 2026-05-17

### Added (issue #169 - determinazioni ACN del 13 aprile 2026)
- Nuovo task `tasks/elenco-fornitori-rilevanti.md` per la compilazione dell'elenco dei fornitori rilevanti NIS richiesto dall'art. 18 della Determinazione ACN 127437/2026, comunicato tramite la piattaforma ACN nella finestra annuale 15 aprile - 31 maggio (prima applicazione: 2026). Copre il censimento dei fornitori, l'applicazione dei 2 criteri di rilevanza ex art. 1 lett. ll) (fornitura ICT Allegato I p.8-9 / fornitura non fungibile), la raccolta dei 5 campi obbligatori (denominazione, CF, Paese, codici CPV Reg. CE 2195/2002, criterio applicato) e la trasmissione finale.
- Nuovi estratti normativi in `references/estratti/`:
  - `acn-det-127437-2026-art18-fornitori.md` - art. 1 lett. ll), art. 16 co. 1 (finestra), art. 16 co. 3 lett. g), art. 18 (5 informazioni), art. 24 co. 3 (applicazione 15/04/2026)
  - `acn-det-127434-2026-scadenze-nuovi-soggetti.md` - art. 1 (termini per nuovi soggetti 2026), art. 2 (DNS/registrar), art. 5 (entrata in vigore 30/04/2026)
- Nuove trascrizioni verbatim PDF in `references/fonti/`:
  - `acn-det-127437-2026.md` - 19 pagine, 24 articoli (Definizioni + 6 capi), trascrizione integrale
  - `acn-det-127434-2026.md` - 3 pagine, 5 articoli, trascrizione integrale
- Nuove voci in `references/sources.yaml`:
  - `acn-det-127437-2026` con SHA256 `4a12bb3d728ea559ad1627dc5dcd61fc91b23b75f66d674281a8bd9aae8d5e1a`
  - `acn-det-127434-2026` con SHA256 `84709af41c8e017885d007fffc57d333b77f02d6416552028839ad6b364bd20a`

### Changed
- `SKILL.md`: aggiornata description del frontmatter per includere l'obbligo fornitori rilevanti e i termini speciali nuovi soggetti 2026; aggiunta nuova sotto-attivita' `elenco-fornitori-rilevanti.md`; aggiornata sezione "Fonti normative" con le 2 nuove determinazioni
- `AGENTS.md`: aggiornata sezione "Dominio" (5 angoli invece di 4); aggiunte voci per `acn-det-127437-2026` e `acn-det-127434-2026` nella sezione "Fonti autoritative"; aggiunti 2 nuovi bullet nella sezione "Articoli e punti chiave" (art. 1 lett. ll + artt. 16/18 Det. 127437/2026; termini speciali Det. 127434/2026); aggiornato stato attuale (5 task, 12 estratti)
- `tasks/valuta-perimetro.md`: aggiunta sezione finale "Rinvio a task successivi" che cita esplicitamente il task fornitori rilevanti e la specialita' delle scadenze 2026
- `tasks/gap-analysis-misure.md`: aggiunta nota sulle scadenze speciali per i soggetti inseriti per la prima volta nel 2026 (31/07/2027 misure + 01/01/2027 notifica)
- `tasks/verifica-incidente-significativo.md`: aggiunta nota sul differimento dell'obbligo operativo di notifica al 01/01/2027 per i soggetti 2026

### Note
- Versione: minor (0.1.0 -> 0.2.0) per l'aggiunta di funzionalita' nuova retro-compatibile (nuovo task + estensione description)
- L'entry `Unreleased` resta aperta per i fix source-grounding precedenti (PR #154) ancora da rilasciare separatamente
- Det. ACN 155238/2026 (categorizzazione attivita' e servizi - Capo V Det. 127437/2026) **fuori scope** di questa release: la skill non copre ancora il processo di categorizzazione. Da valutare per release successiva

## [0.1.0-alpha+fix.source-grounding] - 2026-05-10

### Fixed (source-grounding remediation - issue #103)

- Aggiunto `references/fonti/` con trascrizioni verbatim delle fonti PDF:
  - `fonti/dlgs-138-2024.md` - art. 1, 2 (def.), 3 (ambito), 6 (essenziali/importanti),
    7 (registrazione), 23 (governance), 24 (misure), 25 (notifica), 38 (sanzioni)
    da PDF GU (pagg. 2-9, 20-22, 26-27).
  - `fonti/acn-det-379907-2025.md` - tutti gli artt. 1-9 della determinazione vigente
    (5 pagine integrali lette dal PDF).
  - `fonti/acn-allegato-1-v2.md` - funzioni GOVERN e IDENTIFY pagg. 1-5/13
    dal PDF Allegato 1 Det. 379907/2025.
  - `fonti/acn-allegato-2-v2.md` - funzioni GOVERN e IDENTIFY pagg. 1-5/16
    dal PDF Allegato 2 Det. 379907/2025, con nota delle differenze rispetto all'Allegato 1.
  - `fonti/acn-allegato-3-v2.md` - tabella IS-1..3 completa (1 pagina integrale).
  - `fonti/acn-allegato-4-v2.md` - tabella IS-1..4 completa (1 pagina integrale).
- `sources.yaml` aggiornato:
  - Aggiunto campo `md_path` per ogni fonte con file in `fonti/`.
  - Corretti `binary_path: null` per dir-2022-2555-nis2, reg-ese-2024-2690 e
    acn-det-164179-2025: i binari non erano mai stati scaricati (placeholder errati).
  - `last_verified` aggiornato a 2026-05-10.

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill `nis2-self-assessment`
- 4 task files:
  - `valuta-perimetro` - classificazione essenziale/importante/fuori ambito (art. 3, 6 D.Lgs. 138/2024)
  - `gap-analysis-misure` - gap analysis sui 10 elementi art. 24 + sottocategorie Framework Nazionale Cybersecurity
  - `verifica-incidente-significativo` - art. 25 e codici IS-1..4 della Det. ACN 379907/2025 (Allegati 3-4)
  - `check-obblighi-governance` - art. 23 obblighi del CdA
- 10 estratti normativi:
  - `dlgs-138-2024-perimetro.md` (art. 3, 6, 7 + note dimensionali Racc. 2003/361/CE)
  - `dlgs-138-2024-misure-art23.md` (art. 23 + art. 24 con i 10 elementi minimi)
  - `dlgs-138-2024-incident-art25.md` (art. 25 + tempistiche)
  - `dlgs-138-2024-sanzioni-art38.md` (art. 38 + tabelle di sintesi sanzionatorie)
  - `dlgs-138-2024-allegati-i-iv.md` (settori e tipologie)
  - `acn-det-379907-articoli.md` (artt. 1-9 della Det. ACN vigente)
  - `acn-misure-base-essenziali.md` (Allegato 2 Det. 379907/2025 - 43 sottocategorie)
  - `acn-misure-base-importanti.md` (Allegato 1 Det. 379907/2025 - 37 sottocategorie)
  - `acn-incidenti-significativi.md` (Allegati 3-4 Det. 379907/2025: codici IS-1..4 + soglie telco art. 6 co. 2)
  - `reg-ese-2024-2690-ambito.md` (ambito Reg. UE 2024/2690)
- Fonti primarie catalogate in `sources.yaml` con SHA256 per i binari scaricati:
  - D.Lgs. 138/2024 (PDF GU)
  - Det. ACN 379907/2025 firmata + Allegati 1, 2, 3, 4 (PDF)
- Cataloga inoltre come riferimento storico la Det. ACN 164179/2025 (sostituita) e DL 105/2019 (PSNC) come fonte non binaria.
- 2 esempi: utility energetica essenziale + PMI manifattura importante (input + expected-output + note di dominio).
- Compatibilita' dual-agent: Claude Code (SKILL.md) + OpenAI Codex (`agents/openai.yaml`)
- AGENTS.md con convenzioni di dominio, citazioni di articoli e best practice

### Fixed (durante adversarial review pre-merge)
- Logica della size-cap rule corretta: gli operatori AND/OR della Raccomandazione 2003/361/CE non sono simmetrici. NON-piccola = (occupati >= 50) OR (entrambi i valori finanziari > 10M); NON-PMI/grande = (occupati >= 250) OR (fatturato > 50M AND bilancio > 43M).
- Determinazione ACN 379907/2025 (sostitutiva di 164179/2025 dal 15/01/2026) effettivamente scaricata e catalogata con SHA256: il documento principale + 4 allegati. Estratti aggiornati al testo verbatim del documento vigente.
- Codici IS-1, IS-2, IS-3 (importanti) e IS-1..IS-4 (essenziali) degli Allegati 3-4 sostituiscono le soglie quantitative ipotizzate in pre-revisione: la Det. ACN NON impone soglie nazionali quantitative per la generalita' dei soggetti; solo per gli operatori telco (art. 6 co. 2) ci sono soglie durata-utenti.
- Calcolo sanzioni art. 38 corretto: max(importo fisso edittale; percentuale fatturato), non min.
- Articoli D.Lgs. 138/2024 nelle note di sources.yaml: art. 23 = Organi di amministrazione, art. 24 = Misure (la confusione e' frequente in fonti secondarie).
- Scala di maturita' 0-4 nel task gap-analysis dichiarata come **rubric interna non normativa**.
- Caso "MSP piccola impresa in ambito via art. 3 co. 5/co. 10" rimosso: art. 3 co. 5 lett. b si applica ai fornitori di reti/servizi di comunicazione elettronica, art. 3 co. 10 richiede impresa collegata che soddisfi i criteri specifici a-d.

### Note di sviluppo
- Skill **non ancora validata da dominio terzo** (Livello 2). Profilo target validatore: CISO o consulente cybersecurity con esperienza diretta su mandati NIS2 attivi.
- Esempi limitati a 2 (perimetro): casi di valutazione incidente significativo da aggiungere in iterazioni successive.
- Le linee guida ENISA tecniche sul Reg. UE 2024/2690 NON sono catalogate come fonte primaria in v0.1.0-alpha; affermazioni che le richiamano sono marcate come "non verificate".
- Da considerare draft fino a validazione Livello 2 (vedi `../../methodology/validazione.md`).

### Limiti noti per la versione 0.1.0-alpha
- Calcolo dimensionale per gruppi/imprese collegate (art. 6 par. 2 Racc. 2003/361/CE): rinvio strutturale, non automatizzato.
- DL 105/2019 (PSNC): catalogato come fonte ma senza estratto verbatim dedicato. Le affermazioni di assolvenza notifica derivano dall'art. 44 D.Lgs. 138/2024 gia' riportato negli estratti.
- Non produce moduli di registrazione precompilati per la piattaforma ACN.
- Le specifiche di sicurezza tecnica del Reg. UE 2024/2690 + ENISA technical guidance sono fuori scope di questa alpha.
