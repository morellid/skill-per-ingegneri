# CHANGELOG - segnaletica-salute-sicurezza-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #348)
- Prima versione della skill di supporto al **tecnico** (datore di lavoro, RSPP, coordinatore
  sicurezza) per la **segnaletica di salute e sicurezza sul luogo di lavoro**, ai sensi del **D.Lgs.
  9 aprile 2008, n. 81, Titolo V (artt. 161-165)**, nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 161-165 via `caricaArticolo` (idGruppo 28-29; formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-segnaletica-161-165.md` (artt. 161-165 per
    intero; art. 166 abrogato riportato come nota).
- Estratto operativo `references/estratti/segnaletica-checklist.md`.
- Due task: `inquadra-obbligo-segnaletica.md` e `inquadra-informazione-formazione-sanzioni.md`.
- Due esempi: carrelli elevatori in magazzino (obbligo residuale, tipi di segnale, traffico interno);
  segnali gestuali per manovre di gru (formazione obbligatoria e sanzioni).

### Contenuto ancorato al testo
- Campo di applicazione ed esclusione della segnaletica del traffico (161); definizioni dei tipi di
  segnaletica e di segnale (162); obbligo residuale del datore di lavoro conformemente agli allegati
  XXIV-XXXII, situazioni non previste, traffico interno (163); informazione di RLS/lavoratori e
  formazione sul significato dei segnali, specie con gesti/parole (164); sanzioni a datore di lavoro e
  dirigente - arresto 3-6 mesi o ammenda 2.500-6.400 euro per l'art. 163 e arresto 2-4 mesi o ammenda
  750-4.000 euro per l'art. 164, con regola di cumulo (165). Art. 166 abrogato (D.Lgs. 106/2009).

### Scope e limiti
- Non progetta il piano di segnaletica né redige il DVR (art. 28), non riproduce gli allegati
  XXIV-XXXII (requisiti specifici di cartelli, colori, segnali), non tratta la segnaletica stradale di
  cantiere (CdS/DM 10/7/2002). Non sostituisce il datore di lavoro, l'RSPP né il CSE.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo hash) e
  rileggere gli artt. 161-165 e l'evoluzione degli allegati XXIV-XXXII.
- Validazione Livello 2 con RSPP / coordinatore per la sicurezza.
