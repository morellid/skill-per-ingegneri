# CHANGELOG - ambienti-confinati-dpr177

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #44)
- Prima versione della skill di supporto documentale alla qualificazione delle
  imprese/lavoratori autonomi e alle procedure di sicurezza per i lavori in
  ambienti sospetti di inquinamento o confinati (DPR 177/2011, artt. 1-4).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.P.R. 14/9/2011 n. 177 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    f2163e0860182df00ebf74ce6df356f24a2089e0b66c3829cddb4638229f1b8b
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 1-4 letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dpr-177-2011.md`.
- Estratto operativo `references/estratti/ambienti-confinati-checklist.md` con i
  requisiti di qualificazione e le procedure di appalto.
- Due task: `verifica-qualificazione.md` (requisiti art. 2) e
  `checklist-procedure-appalto.md` (adempimenti art. 3).
- Due esempi: appalto per pulizia di un serbatoio (requisiti + procedure +
  subappalto) e lavoratore autonomo senza esperienza triennale (non qualificabile).

### Nota di source-grounding (#44)
La scheda citava il DPR 177/2011 (GU) e il manuale del Ministero del lavoro. La
skill e' source-grounded sul **testo vigente del DPR 177/2011 letto da
Normattiva** (fonte ufficiale), con la pagina indice pinnata a data di vigenza per
hash riproducibile e la trascrizione verbatim degli articoli 1-4. Il D.Lgs.
81/2008 (artt. 26, 66, 121, allegato IV punto 3) e il manuale del Ministero del
lavoro (guida non normativa) sono citati come riferimento, non riprodotti.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con RSPP / esperto sicurezza.
- Possibili estensioni future: trascrizione mirata degli artt. 66, 121 e
  dell'allegato IV punto 3 del D.Lgs. 81/2008 (definizioni e obblighi tecnici);
  raccordo con le buone prassi validate.
