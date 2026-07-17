# CHANGELOG - autorizzazione-integrata-ambientale-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #289)
- Prima versione della skill di supporto all'**Autorizzazione Integrata Ambientale (AIA/IPPC)**, ai
  sensi del **D.Lgs. 3 aprile 2006, n. 152, Parte II, Titolo III-bis** (artt. 29-ter, 29-quater,
  29-sexies, 29-octies, 29-decies), nell'area `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 3 aprile 2006, n. 152** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: c2175fe5c9313db1087d444b07e71d727154140d579ffcf6357ababa5d57b45c
    (codice 006G0171). Artt. 29-ter/quater/sexies/octies/decies (idGruppo 9) via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-152-2006-aia-titolo3bis.md`.
- Estratto operativo `references/estratti/aia-checklist.md`.
- Due task: `inquadra-domanda-aia.md` e `verifica-condizioni-controlli.md`.
- Due esempi: assoggettabilità, domanda e procedura (artt. 29-ter, 29-quater); controlli e
  inosservanze (art. 29-decies).

### Contenuto ancorato al testo
- Art. 29-ter domanda (contenuti a-m, relazione di riferimento, completezza 30 gg); art. 29-quater
  procedura (avvio 30 gg, pubblicazione 15 gg, osservazioni 30 gg, conferenza di servizi, integrazioni
  ≤ 90 gg, determinazione 150 gg, coordinamento VIA); art. 29-sexies contenuto/condizioni (VLE su BAT
  senza obbligo di tecnica specifica, BAT-AEL, monitoraggio, deroghe); art. 29-octies rinnovo/riesame
  (nuove conclusioni sulle BAT; 10 anni; gestore 30-180 gg); art. 29-decies controlli (ISPRA/ARPA;
  ispezioni 1/3 anni, 6 mesi dopo grave inosservanza; inosservanze: diffida/sospensione/revoca-chiusura).

### Scope e limiti
- Non redige la domanda/AIA, non individua le BAT, non riproduce gli Allegati VIII/XII (attività IPPC)
  né i BREF, non tratta le sanzioni (art. 29-quattuordecies). Distinta da AUA (`aua-dpr59-dossier`),
  autorizzazioni singole (`scarichi-emissioni-dlgs152`) e VIA (`via-screening-sia-dlgs152`).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 152/2006 pinnato (nuovo hash) e
  rileggere gli articoli del Titolo III-bis.
- Validazione Livello 2 con tecnico ambientale / autorità competente o ARPA.
