# CHANGELOG - verifiche-periodiche-ascensori-dpr162

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #43)
- Prima versione della skill di supporto documentale all'iter di esercizio,
  verifiche periodiche/straordinarie e manutenzione degli ascensori (DPR
  162/1999, artt. 12-16).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.P.R. 30/4/1999 n. 162 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    ad0fc818fb19458dba3133a7db828d1b57a4581b94a4163b23ca2eb922982d9b
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 12-16 letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dpr-162-1999.md` (testo in vigore dal 16-3-2017 /
    12-12-2017).
- Estratto operativo `references/estratti/verifiche-ascensori-checklist.md` con
  la sintesi delle periodicita' e degli adempimenti.
- Due task: `diagnosi-adempimenti.md` (adempimenti, periodicita', soggetti) e
  `checklist-esercizio.md` (completezza degli adempimenti).
- Due esempi: nuovo ascensore condominiale (messa in esercizio, comunicazione 60
  gg + matricola 30 gg, verifica biennale e soggetti) e verifica periodica con
  esito negativo (fermo dell'impianto e verifica straordinaria).

### Nota di source-grounding (#43)
La scheda citava il DPR 162/1999 su Normattiva. La skill e' source-grounded
esclusivamente sul **testo vigente del DPR 162/1999 letto da Normattiva** (fonte
ufficiale), con la pagina indice pinnata a data di vigenza per hash riproducibile
e la trascrizione verbatim degli articoli 12-16. Le norme tecniche UNI EN (a
pagamento) non sono riprodotte. Gli artt. 1-11 (immissione sul mercato / marcatura
CE dei componenti) sono fuori dallo scopo (verifiche periodiche) e non trascritti.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con tecnico verificatore / ditta di
  manutenzione ascensori.
- Possibili estensioni future: coordinamento con D.Lgs. 17/2010 (messa in
  servizio/marcatura CE); dettaglio degli obblighi del manutentore; modulistica
  comunale.
