# CHANGELOG - autorizzazione-paesaggistica-ordinaria-dlgs42

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #350)
- Prima versione della skill di supporto al **progettista** per l'**autorizzazione paesaggistica
  ordinaria** e la **relazione paesaggistica**, ai sensi del **D.Lgs. 22 gennaio 2004, n. 42, artt.
  146 e 167**, nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 42/2004** (Codice dei beni culturali e del paesaggio) - indice Normattiva pinnato
    `!vig=2026-07-17` SHA256: 3693219b8efd59011035c112a0558a8cb5f2f4d2ec61a27cef03347a71b6a230
    (codice 004G0066). Art. 146 (versione 8, idGruppo 26) e art. 167 (versione 4, idGruppo 29) via
    `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-42-2004-146-167.md` (art. 146 per intero, cc.
    1-16; art. 167 cc. 1-6).
- Estratto operativo `references/estratti/autorizzazione-paesaggistica-checklist.md`.
- Due task: `inquadra-procedura-ordinaria.md` e `inquadra-accertamento-compatibilita.md`.
- Due esempi: ampliamento in zona vincolata (iter, parere del soprintendente, efficacia); opere già
  realizzate (accertamento di compatibilità ammesso per tinteggiatura difforme vs escluso per nuovo
  volume).

### Contenuto ancorato al testo
- Obbligo di autorizzazione preventiva e astensione dai lavori (146 cc. 1-2); documentazione/relazione
  paesaggistica, schemi con DPCM (c. 3); atto autonomo e presupposto al permesso di costruire, niente
  sanatoria salvo art. 167 cc. 4-5, efficacia 5 anni + 1 (c. 4); parere del soprintendente vincolante/
  obbligatorio, 45 giorni (cc. 5, 8); competenza regione e delega ai comuni (c. 6); procedura con
  verifica in 40 giorni, relazione tecnica illustrativa e proposta (c. 7); silenzio 60 giorni e potere
  sostitutivo (cc. 9-10); accertamento di compatibilità postumo per interventi minori con decisione in
  180 giorni, parere vincolante soprintendenza in 90 giorni, sanzione pecuniaria o rimessione in
  pristino (167 cc. 4-5).

### Scope e limiti
- Non redige la relazione paesaggistica né il progetto, non rilascia l'autorizzazione né il parere,
  non riproduce gli schemi della documentazione (DPCM 12/12/2005), la procedura semplificata (DPR
  31/2017, skill `autorizzazione-paesaggistica-semplificata-dpr31`), l'art. 149 né la disciplina
  penale (art. 181). Non sostituisce il progettista né gli enti competenti.

### Note di sviluppo
- Scartato in fase di selezione il DPCM 5/12/1997 (requisiti acustici passivi): atto numberless, URN
  non risolvibile su Normattiva (pagina di errore) -> non ancorabile in modo riproducibile.
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 42/2004 pinnato (nuovo hash) e
  rileggere gli artt. 146 e 167.
- Validazione Livello 2 con architetto / esperto di beni paesaggistici.
