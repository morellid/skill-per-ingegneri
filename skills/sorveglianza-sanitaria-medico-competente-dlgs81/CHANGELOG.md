# CHANGELOG - sorveglianza-sanitaria-medico-competente-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #263)
- Prima versione della skill di supporto alla **sorveglianza sanitaria** dei lavoratori e agli
  **obblighi del medico competente** (D.Lgs. 81/2008, artt. 25, 38-41), nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9 aprile 2008, n. 81** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831 (codice 008G0104).
    Artt. 25, 38, 39, 40, 41 (testo vigente) via `caricaArticolo`, trascritti verbatim in
    `references/fonti/dlgs-81-2008-sorveglianza.md`.
- Estratto operativo `references/estratti/sorveglianza-sanitaria-checklist.md`.
- Due task: `imposta-sorveglianza-sanitaria.md` e `gestisci-giudizio-idoneita-ricorso.md`.
- Due esempi: rientro dopo assenza > 60 giorni (art. 41 c.2 lett. e-ter); giudizio di idoneità con
  limitazioni e ricorso all'ASL (art. 41 cc. 6 e 9).

### Contenuto ancorato al testo
- Casi della sorveglianza (art. 41 c.1); tipi di visita (c.2: preventiva/preassuntiva, periodica di
  norma annuale, su richiesta, cambio mansione, cessazione, ripresa > 60 gg, alcol/sostanze);
  divieti (c.3) e spese a carico del datore (c.4); quattro giudizi di idoneità (c.6), forma scritta
  (c.6-bis), limiti temporali dell'inidoneità temporanea (c.7); ricorso all'ASL entro 30 giorni
  (c.9). Obblighi (art. 25), requisiti (art. 38), svolgimento (art. 39), rapporti con il SSN (art. 40).

### Scope e limiti
- Non esprime giudizi sanitari (esclusivi del medico competente), non definisce i protocolli
  sanitari, non riproduce gli Allegati 3A/3B (cartella sanitaria e di rischio). Non sostituisce il
  medico competente, l'RSPP né il datore di lavoro. Complementare a `dvr-generico`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo hash) e
  rileggere gli artt. 25, 38-41 (modifiche frequenti, es. L. 203/2024).
- Validazione Livello 2 con medico competente / RSPP.
