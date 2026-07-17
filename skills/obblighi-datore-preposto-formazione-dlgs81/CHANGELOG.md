# CHANGELOG - obblighi-datore-preposto-formazione-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #293)
- Prima versione della skill di supporto alla **ripartizione degli obblighi** di sicurezza (datore di
  lavoro, dirigente, preposto) e alla **formazione** dei lavoratori, ai sensi del **D.Lgs. 9 aprile
  2008, n. 81** (artt. 18, 19, 37), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9 aprile 2008, n. 81** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 18 (grp3, v12), 19 (grp3, v2), 37 (grp6, v9) via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-artt-18-19-37.md`.
- Estratto operativo `references/estratti/obblighi-formazione-checklist.md`.
- Due task: `ripartisci-obblighi.md` e `inquadra-formazione.md`.
- Due esempi: ripartizione obblighi e non delegabili (artt. 17-18-19); formazione di neoassunti e
  preposto (art. 37).

### Contenuto ancorato al testo
- Art. 18 obblighi del datore/dirigente (medico competente, addetti emergenza, individuazione del
  preposto - lett. b-bis, DPI, sorveglianza sanitaria, informazione/formazione, consegna DVR/DUVRI al
  RLS, comunicazione INAIL infortuni entro 48 ore - lett. r); art. 19 obblighi del preposto (vigilanza,
  intervento e interruzione dell'attività, segnalazione - lett. a/f/f-bis, corsi ex art. 37); art. 37
  formazione (lavoratori, preposti in presenza e dirigenti, addestramento, orario di lavoro senza oneri,
  rinvio all'Accordo Stato-Regioni). Richiamato art. 17 (non delegabili: DVR e RSPP).

### Scope e limiti
- Non redige il DVR/DUVRI né verbali/attestati di formazione, non riproduce durate/contenuti
  dell'Accordo Stato-Regioni né gli obblighi settoriali, non valuta la delega di funzioni (art. 16) o le
  responsabilità. Distinta da `dvr-generico`, `duvri-interferenze-dlgs81`, `pos-allegato-xv-checker`,
  `coordinatori-sicurezza-cantieri-dlgs81`, `sorveglianza-sanitaria-medico-competente-dlgs81`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo hash) e
  rileggere gli artt. 18, 19, 37 (modifiche su preposto - D.L. 146/2021).
- Validazione Livello 2 con RSPP / consulente della sicurezza.
