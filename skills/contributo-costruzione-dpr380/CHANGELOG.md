# CHANGELOG - contributo-costruzione-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #257)
- Prima versione della skill di supporto all'inquadramento del **contributo di costruzione**
  dovuto per il permesso di costruire (oneri di urbanizzazione + costo di costruzione, riduzioni,
  esoneri, convenzione-tipo, opere non residenziali), ai sensi del **D.P.R. 380/2001 (T.U.
  Edilizia), artt. 16-19**, nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 6 giugno 2001, n. 380** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 98a209dab2743964d5eddeca5321261f5b12225c140367e17c53705e5b95acb2 (codice 001G0429).
    Artt. 16, 17, 18, 19 (testo vigente) via `caricaArticolo`, trascritti verbatim in
    `references/fonti/dpr-380-2001-artt16-19.md`.
- Estratto operativo `references/estratti/contributo-costruzione-checklist.md`.
- Due task: `inquadra-contributo.md` e `gestisci-oneri-scomputo.md`.
- Due esempi: ampliamento <= 20% di edificio unifamiliare (esonero art. 17, c. 3, lett. b);
  capannone industriale (art. 19).

### Contenuto ancorato al testo
- Art. 16 (contributo = oneri di urbanizzazione + costo di costruzione; rateizzazione, scomputo
  con esecuzione diretta, costo di costruzione in corso d'opera entro 60 gg, tabelle regionali);
  art. 17 (riduzione per convenzionata/prima abitazione; esoneri; immobili dello Stato/manutenzione
  straordinaria con aumento del carico urbanistico); art. 18 (convenzione-tipo); art. 19 (opere non
  residenziali: industriali/artigianali; turistiche/commerciali/direzionali con quota <= 10%).

### Scope e limiti
- Non calcola gli **importi** (tabelle parametriche degli oneri, valori del costo di costruzione),
  demandati a regioni e comuni. Non sostituisce l'ufficio tecnico comunale (SUE). Non copre la
  disciplina regionale/comunale di dettaglio (rateizzazione, garanzie, monetizzazioni, SCIA onerosa).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 380/2001 pinnato (nuovo hash) e
  rileggere gli artt. 16-19 (soggetti a modifiche frequenti - verificare le versioni vigenti).
- Validazione Livello 2 con funzionario SUE / esperto oneri edilizi.
