# CHANGELOG - valutazione-rischio-chimico-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #358)
- Prima versione della skill di supporto al **datore di lavoro**, all'**RSPP** e al **tecnico della
  sicurezza** per la **valutazione del rischio chimico**, ai sensi del **D.Lgs. 9 aprile 2008, n. 81,
  Titolo IX, Capo I, artt. 222-227**, nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e (codice 008G0104, idGruppo 41).
    Artt. 222-227 via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-222-227.md` (artt. 222-227 per intero).
- Estratto operativo `references/estratti/rischio-chimico-checklist.md`.
- Due task: `inquadra-valutazione-rischio-chimico.md` e `inquadra-misure-emergenze-formazione.md`.
- Due esempi: officina di verniciatura con solventi (valutazione e gerarchia delle misure); detergente
  in ufficio (deroga per rischio basso e irrilevante).

### Contenuto ancorato al testo
- Definizioni di agenti chimici e agenti chimici pericolosi (CLP Reg. CE 1272/2008), VLEP (Allegato
  XXXVIII), pericolo/rischio (222); valutazione dei rischi nel DVR (art. 28) con SDS REACH, esposizione,
  VLEP, effetto combinato, attivita' nuove preventive, aggiornamento (223); misure e principi generali
  con deroga per rischio basso e irrilevante che esclude gli artt. 225/226/229/230 (224); misure
  specifiche - sostituzione e gerarchia (controlli tecnici, collettive, DPI, sorveglianza sanitaria),
  misurazioni (Allegato XLI), superamento del VLEP e comunicazione all'organo di vigilanza, sostanze
  infiammabili/instabili (225); incidenti ed emergenze con procedure, esercitazioni, sistemi d'allarme e
  piano (226); informazione e formazione con schede di sicurezza ed etichettatura di contenitori e
  condutture (227).

### Scope e limiti
- Non redige il DVR ne' la valutazione del rischio chimico, non esegue misurazioni ne' algoritmi di
  stima (es. MoVaRisCh), non riproduce gli Allegati XXXVIII/XLI ne' i regolamenti CLP/REACH. Non
  sostituisce il datore di lavoro, l'RSPP, il medico competente ne' il chimico.

### Note di sviluppo
- Distinta da `scheda-dati-sicurezza-sds-reg878` (SDS lato fornitore) e `atex-luoghi-lavoro-dlgs81`.
- Artt. 222-223 aggiornati dal D.Lgs. 39/2016 (adeguamento al CLP). Validazione Livello 2 con
  RSPP/chimico.
