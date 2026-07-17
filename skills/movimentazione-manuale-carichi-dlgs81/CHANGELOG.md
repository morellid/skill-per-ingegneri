# CHANGELOG - movimentazione-manuale-carichi-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #313)
- Prima versione della skill di supporto all'inquadramento degli obblighi in materia di
  **movimentazione manuale dei carichi (MMC)**, ai sensi del **D.Lgs. 81/2008, Titolo
  VI** (artt. 167-169), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9/4/2008 n. 81** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 167, 168, 169, idGruppo 30, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-mmc.md`.
- Estratto operativo `references/estratti/mmc-checklist.md`.
- Due task: `inquadra-obblighi-mmc.md` e `imposta-informazione-formazione.md`.
- Due esempi: obblighi del datore per una mansione di magazzino (artt. 167-168);
  informazione, formazione e addestramento (art. 169).

### Contenuto ancorato al testo
- Art. 167 campo di applicazione e definizioni (MMC come trasporto/sostegno con
  sollevare/deporre/spingere/tirare/portare/spostare; patologie da sovraccarico
  biomeccanico dorso-lombari, osteoarticolari/muscolo-tendinee/nervo-vascolari); art. 168
  obblighi del datore (evitare con attrezzature meccaniche; se non evitabile, misure
  tenendo conto dell'allegato XXXIII: organizzazione posti, valutazione anche in
  progettazione, riduzione rischi per fattori individuali/ambiente/esigenze, sorveglianza
  sanitaria art. 41; norme tecniche come criteri); art. 169 informazione (peso/
  caratteristiche), formazione (rischi/esecuzione) e addestramento (corrette manovre e
  procedure).

### Scope e limiti
- Non calcola l'indice di sollevamento né la massa di riferimento (Allegato XXXIII, ISO
  11228-1/2/3 - non riprodotti), non redige il DVR-MMC né la relazione ergonomica, non
  esprime giudizi di sorveglianza sanitaria (art. 41), non sostituisce il datore di
  lavoro, l'RSPP o il medico competente. Allegato XXXIII, ISO 11228 e art. 41 citati e
  non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato
  (nuovo hash) e rileggere gli artt. 167-169 (testo tra `(( ))`).
- Validazione Livello 2 con RSPP / medico competente / ergonomo.
