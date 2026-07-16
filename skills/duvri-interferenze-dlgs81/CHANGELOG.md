# CHANGELOG - duvri-interferenze-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #241)
- Prima versione della skill di supporto agli **obblighi del committente negli appalti** e
  alla redazione del **DUVRI** (art. 26 D.Lgs 81/2008), nell'area `sicurezza-lavoro-cantieri`.
- Candidata emersa dalla ricerca sistematica sul catalogo (scheda SL.2), con fonte ufficiale
  gratuita non ancora coperta da skill esistenti.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008 art. 26** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831
    (codice 008G0104). Articolo via caricaArticolo, trascritto verbatim in
    `references/fonti/dlgs-81-art-26.md`.
- Estratto operativo `references/estratti/duvri-checklist.md`.
- Due task: `verifica-idoneita-e-informazione.md` e `imposta-duvri.md`.
- Due esempi: appalto di pulizie in stabilimento (DUVRI dovuto); mera fornitura (esclusione
  c.3-bis e suo limite).

### Contenuto ancorato al testo
- c.1 (idoneita' tecnico-professionale; informazione sui rischi), c.2 (cooperazione e
  coordinamento), c.3/3-bis (DUVRI, esclusioni, incaricato nei settori a basso rischio),
  c.5 (costi non ribassabili), c.8 (tessera), responsabilita' solidale.

### Scope e limiti
- Non valuta i rischi specifici dell'appaltatore; non quantifica i costi; non copre i
  cantieri Titolo IV (PSC/POS) ne' il DVR del committente (art. 28-29).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs 81/2008 (nuovo hash) e
  rileggere l'art. 26.
- Validazione Livello 2 con RSPP / esperto sicurezza sul lavoro.
