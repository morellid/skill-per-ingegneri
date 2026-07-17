# CHANGELOG - dpi-protezione-individuale-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #343)
- Prima versione della skill di supporto all'inquadramento degli obblighi in materia di
  **dispositivi di protezione individuale (DPI)**, ai sensi del **D.Lgs. 9 aprile 2008, n. 81**,
  Titolo III, **Capo II (artt. 74-79)**, nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 74-79 via `caricaArticolo` (idGruppo 16; formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-dpi-74-79.md` (artt. 74-79 per intero).
- Estratto operativo `references/estratti/dpi-checklist.md`.
- Due task: `inquadra-scelta-dpi.md` e `inquadra-formazione-addestramento.md`.
- Due esempi: imbracatura anticaduta e otoprotettori (uso residuale, requisiti e addestramento
  indispensabile); obblighi del lavoratore che modifica/non usa/non segnala il DPI.

### Contenuto ancorato al testo
- Definizione di DPI ed esclusioni (74); obbligo d'uso residuale rispetto alla protezione collettiva
  (75); requisiti - conformità al reg. UE 2016/425, adeguatezza/ergonomia/compatibilità (76);
  obblighi del datore - scelta con valutazione dei rischi, condizioni d'uso, fornitura, manutenzione/
  igiene, informazione, formazione e addestramento, con addestramento indispensabile per DPI di
  terza categoria e protettori dell'udito (77); obblighi dei lavoratori (78); criteri e rinvio ad
  allegato VIII e decreto ministeriale, in attesa DM 2 maggio 2001 (79).

### Scope e limiti
- Non redige il DVR né la valutazione dei rischi, non seleziona/classifica in concreto il DPI, non
  riproduce l'allegato VIII, il regolamento (UE) 2016/425, il D.Lgs. 475/1992 né il DM 2 maggio 2001.
  Non sostituisce il datore di lavoro, l'RSPP né il medico competente.

### Note di sviluppo
- Due microartefatti di estrazione (una spaziatura e un a-capo interni al testo AKN) normalizzati
  senza alterare il contenuto.
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo hash) e
  rileggere gli artt. 74-79 (modifiche segnalate dai doppi tondi `(( ))`).
- Validazione Livello 2 con RSPP / esperto di sicurezza sul lavoro.
