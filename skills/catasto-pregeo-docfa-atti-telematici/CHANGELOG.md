# CHANGELOG - catasto-pregeo-docfa-atti-telematici

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
