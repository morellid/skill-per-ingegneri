# CHANGELOG - comunione-ordinaria-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Riformulazione dell'inquadramento per **centrare il ruolo dell'ingegnere/geometra/CTU** (area
  *CTU & ingegneria forense*): il fulcro e' il **compito tecnico della divisione** (comoda
  divisibilità e progetto di divisione in natura, art. 1114; attribuzione/vendita se non
  divisibile, art. 1116). Aggiornati `description`, `summary`, `title`, README, AGENTS, openai.yaml
  per esplicitare che la skill serve al **tecnico** e non da' consulenza legale.

## [0.1.0-alpha] - 2026-07-17

### Added (closes #341)
- Prima versione della skill di supporto all'inquadramento della **comunione ordinaria**
  (comproprietà di beni) nel **Codice civile** (R.D. 16 marzo 1942, n. 262), Libro III, Titolo VII,
  **Capo I (Della comunione in generale)**, artt. 1100-1116, nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice civile (R.D. 262/1942)** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (codice 042U0262). Artt. 1100-1116 via `caricaArticolo` (versione 1, idGruppo 139).
  - Trascrizione verbatim in `references/fonti/cc-comunione-1100-1116.md` (17 articoli).
- Estratto operativo `references/estratti/comunione-ordinaria-checklist.md`.
- Due task: `inquadra-uso-amministrazione.md` e `inquadra-scioglimento-divisione.md`.
- Due esempi: uso del cortile comune, innovazione a 2/3 e vendita all'unanimità; scioglimento, patto
  di indivisione ridotto a 10 anni e bene non comodamente divisibile.

### Contenuto ancorato al testo
- Norme regolatrici (1100); quote presunte eguali (1101); uso senza alterare la destinazione né
  impedire il pari uso (1102); disposizione della quota (1103); spese con rinunzia liberatoria e
  solidarietà del cessionario (1104); amministrazione a maggioranza per valore delle quote (1105);
  regolamento e amministratore anche estraneo (1106); impugnazione del regolamento a 30 giorni
  (1107); innovazioni/atti eccedenti a 2/3 del valore e consenso unanime per alienazioni/diritti
  reali/locazioni ultra-novennali (1108); impugnazione delle deliberazioni a 30 giorni a pena di
  decadenza (1109); rimborso spese (1110); scioglimento sempre domandabile e patto di indivisione
  max 10 anni (1111); cose non divisibili (1112); intervento dei creditori (1113); divisione in
  natura (1114); obbligazioni solidali (1115); rinvio alla divisione ereditaria (1116).

### Scope e limiti
- Non redige atti (regolamento, delibere, domanda di divisione), non quantifica quote/spese/
  conguagli, non tratta il condominio negli edifici (artt. 1117 ss., skill dedicata) né la comunione
  legale tra coniugi (artt. 177 ss.). Le norme sulla divisione ereditaria (artt. 713 ss., art. 1116)
  sono rinvio non riprodotto. Non sostituisce l'avvocato/CTU.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del Codice civile pinnato (nuovo hash) e
  rileggere gli artt. 1100-1116.
- Validazione Livello 2 con avvocato civilista / esperto di diritti reali.
