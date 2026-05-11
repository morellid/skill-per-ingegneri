# CHANGELOG - nis2-self-assessment

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed (source-grounding remediation - PR #154)
- aggiunto `references/fonti/acn-det-164179-2025-allegato2.md` per la fonte storica `acn-det-164179-2025-allegato2`, cosi' da rispettare la Regola zero Step 3 anche per l'allegato superato mantenuto a catalogo come riferimento storico
- aggiornato `references/sources.yaml` con `md_path` per `acn-det-164179-2025-allegato2`

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
