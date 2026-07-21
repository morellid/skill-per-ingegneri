# CHANGELOG - ponteggi-fissi-pimus-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #352)
- Prima versione della skill di supporto al **tecnico**, all'**impresa/datore di lavoro** e al
  **preposto** per i **ponteggi fissi** e il **Pi.M.U.S.**, ai sensi del **D.Lgs. 9 aprile 2008, n.
  81, Titolo IV, Capo II, Sezione V, artt. 131-138**, nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e (codice 008G0104, idGruppo 23).
    Artt. 131-138 via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-131-138.md` (artt. 131-138 per intero).
- Estratto operativo `references/estratti/ponteggi-checklist.md`.
- Due task: `inquadra-progetto-documentazione.md` e `inquadra-pimus-montaggio.md`.
- Due esempi: ponteggio > 20 m e configurazione fuori schema (progetto firmato da ingegnere/architetto);
  ponteggio a schema-tipo in quota (Pi.M.U.S. dovuto comunque, sorveglianza del preposto e formazione).

### Contenuto ancorato al testo
- Autorizzazione ministeriale al fabbricante e relazione tecnica (artt. 131-132); progetto firmato per
  ponteggi > 20 m / fuori schema / opere provvisionali complesse (art. 133); documentazione in cantiere
  e modifiche sul disegno entro schema-tipo (art. 134); marchio del fabbricante (art. 135); Pi.M.U.S.,
  obblighi del datore di lavoro, sorveglianza del preposto e formazione teorico-pratica (art. 136);
  manutenzione e revisione del preposto (art. 137); norme particolari - parapetto 95 cm, fermapiede 15
  cm, distacco tavole 20 cm (art. 138).

### Scope e limiti
- Non redige il progetto/relazione/Pi.M.U.S., non esegue il calcolo di resistenza e stabilita', non
  rilascia l'autorizzazione ministeriale, non riproduce gli Allegati XVIII/XIX/XXI/XXII ne' le norme
  UNI EN 12810/12811/74. Non sostituisce il professionista abilitato, il datore di lavoro, il preposto
  o gli organi di vigilanza.

### Note di sviluppo
- Artt. 131, 136, 137, 138 modificati dal D.Lgs. 3 agosto 2009, n. 106 (testo vigente dal 20-8-2009):
  ad ogni aggiornamento riscaricare l'indice pinnato (nuovo hash) e rileggere gli artt. 131-138.
- Validazione Livello 2 con RSPP/coordinatore o esperto ponteggi.
