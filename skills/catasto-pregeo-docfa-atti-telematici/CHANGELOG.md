# CHANGELOG - catasto-pregeo-docfa-atti-telematici

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1-alpha] - 2026-05-11

### Fixed - source-grounding remediation (issue #95)

- Creati i file `references/fonti/` per le tre fonti con `binary_path` presente
  e `md_path` mancante:
  - `references/fonti/ade-circolare-3-2009-pregeo10.md`: trascrizione fedele
    dei paragrafi rilevanti letti dal PDF (`sha256: 580012be...`).
    Verificati: par. 2.1-2.9 (indice di affidabilita', estratto di mappa,
    tipologie atti, dati censuari, deformazione, relazione tecnica strutturata,
    controlli topo-cartografici, distanze PF, congruenza cartografica),
    par. 4 (modalita' di presentazione), par. 5 (tipologie escluse
    dall'approvazione automatica), par. 6 (criteri di approvazione a-d),
    par. 9.5-9.6 (particelle con superfici reali, F6), par. 10 (decorrenza).
  - `references/fonti/ade-risoluzione-40-2025-deposito-telematico.md`:
    trascrizione fedele letta dal PDF (`sha256: 8b39d6...`).
    Verificati: testo del comma 5-bis art. 30 DPR 380/2001 cosi' come citato
    nella Risoluzione; ambito oggettivo FR/FM/SC; nota 4 (invalidita' del
    deposito comunale post 1/7/2025 per FR/FM/SC); nota 5 (respingimento
    atti con versione Pregeo errata); versione obbligatoria 10.6.5 APAG 2.15;
    PEC unica depositofrazionamenticatastali@pec.agenziaentrate.it; art. 5
    DPR 650/1972 sul secondo originale; disciplina residuale per atti non
    telematici; nota 11 (Provv. 11/3/2015 e Provv. 28/1/2021).
  - `references/fonti/ade-vademecum-docfa-v1.md`: trascrizione fedele letta
    dal PDF (`sha256: 7ee7fb...`).
    Verificati: premessa; cap. 1.1.1 (definizione UIU ex art. 2 DM 28/1998);
    cap. 1.1.2-1.1.4 (BCC/BCNC, immobili non inventariabili); cap. 1.2.1-1.2.4
    (quadro generale categorie, prospetti A/B/C/D/E/F con denominazioni
    ufficiali); destinazioni d'uso codificate Gruppi D ed E (Prospetti 1.6-1.14);
    cap. 2.2.1.4-2.2.1.5 (causali Quadro A, tipologie documento); cap.
    2.3.1.5-2.3.1.6 (causali Quadro B, tipologie documento); cap. 2.4.2
    (Quadro D, formule standardizzate); cap. 3.1.1-3.1.3 (EP, ES, ET); cap.
    3.2 (planimetria); cap. 3.3.1 (superficie catastale DPR 138/1998).
- Aggiunto `md_path` in `references/sources.yaml` per i tre ID sopra.
- Estratti in `references/estratti/` verificati: le affermazioni normative
  contenute in `circolare-3-2009-pregeo10.md`, `risoluzione-40-2025-deposito-
  telematico.md`, `vademecum-docfa-categorie-causali.md` e `vademecum-docfa-
  elaborato-planimetrico.md` corrispondono al testo letto nei PDF.

## [0.1.0-alpha] - 2026-05-01

### Added
- Prima versione alpha della skill di assistenza alla redazione e check
  pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni
  (Pregeo 10) e del Catasto Fabbricati (Docfa 4).
- Cinque task files:
  - `scelta-tipo-pregeo-e-check.md` - tassonomia atti Pregeo, riga 9 libretto,
    deposito telematico ex art. 30 co. 5-bis DPR 380/2001 (Risoluzione AdE
    40/E del 9/6/2025), tolleranze pre-invio.
  - `scelta-causale-categoria-docfa.md` - albero decisionale fra Quadro A
    (accatastamento) e Quadro B (variazione), causali codificate, scelta
    della categoria catastale (A/B/C ordinarie, D/E speciali, F fittizie).
  - `check-pre-trasmissione-docfa.md` - checklist Quadro D, Elaborato
    Planimetrico, Elenco Subalterni, Entita' Tipologiche, planimetrie.
  - `diagnosi-rifiuti-telematici.md` - mapping messaggio Ufficio -> causa
    probabile -> correzione, per Pregeo e Docfa.
  - `workflow-pregeo-docfa.md` - sequenza Tipo Mappale Pregeo ->
    iscrizione automatica F/6 -> Docfa di accatastamento -> voltura.
- Fonti normative consultate (cfr. `references/sources.yaml`):
  primarie con SHA256 verificato (Vademecum Docfa v1.0, Circ. 3/2009 Pregeo,
  Risoluzione 40/E 2025); secondarie via URL (Normattiva, pagine AdE).
- Estratti testuali in `references/estratti/`:
  `dpr-380-2001-art-30.md`, `dm-28-1998-uiu.md`, `circolare-3-2009-pregeo10.md`,
  `risoluzione-40-2025-deposito-telematico.md`, `vademecum-docfa-categorie-causali.md`,
  `vademecum-docfa-elaborato-planimetrico.md`.
- Esempi: un caso conforme (Tipo Mappale Pregeo per nuovo fabbricato + Docfa
  di accatastamento di villetta in A/7 con autorimessa C/6) e un caso
  problematico (Docfa di variazione errato per ristrutturazione totale di un
  appartamento dichiarato in F/4 invece che in F/3 / variazione planimetrica).

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2 della metodologia,
  vedi `methodology/validazione.md`).
- Da considerare draft finche' un geometra o un ingegnere edile abilitato
  alla redazione di atti Pregeo/Docfa non ne valida l'output su almeno un
  caso reale.
- Il software Pregeo (vigente: 10.6.5 - APAG 2.15 dal 1/7/2025) e Docfa
  (vigente: 4.00.5 da luglio 2019) sono soggetti a aggiornamenti frequenti.
  Verificare il `last_verified` di `references/sources.yaml` prima di
  applicare la skill su un caso reale.
- Le destinazioni d'uso codificate per le UIU di Gruppo D ed E (Vademecum
  Docfa Prospetti 1.6 - 1.24) sono citate ma non riprodotte: si rinvia al
  PDF del Vademecum per l'elenco completo.
