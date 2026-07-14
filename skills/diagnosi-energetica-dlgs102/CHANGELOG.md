# CHANGELOG - diagnosi-energetica-dlgs102

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #45)
- Prima versione della skill di supporto documentale all'obbligo di diagnosi
  energetica delle grandi imprese e delle imprese a forte consumo di energia
  (art. 8 D.Lgs. 102/2014, attuazione della direttiva 2012/27/UE).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 4/7/2014 n. 102 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    ffce506352fbd03eac2612180cf70adc7502336cf829e48429bc13aefb89810d
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 2 (definizioni), 8 (diagnosi energetiche) e 16 (sanzioni) letti via
    AJAX (caricaArticolo) e trascritti verbatim in `references/fonti/dlgs-102-2014.md`.
- Estratto operativo `references/estratti/diagnosi-energetica-checklist.md` con
  soggetti obbligati, esenzioni, periodicita', ENEA, controlli e sanzioni.
- Due task: `verifica-obbligo.md` (applicabilita' ed esenzioni) e
  `checklist-adempimento.md` (completezza degli adempimenti).
- Due esempi: grande impresa manifatturiera obbligata (400 dip., 90 mln, 800 tep)
  e grande impresa di servizi esente per consumi < 50 tep.

### Nota di source-grounding (#45)
La scheda citava il D.Lgs. 102/2014 (su Normattiva) e il DM 100/2023. La skill e'
source-grounded sul **testo vigente del D.Lgs. 102/2014 letto da Normattiva**
(fonte ufficiale), con la pagina indice pinnata a data di vigenza per hash
riproducibile e la trascrizione verbatim degli artt. 2, 8, 16. Come rilevato dalla
scheda, il perimetro e' definito distinguendo cio' che e' nel decreto (obbligo,
soggetti, scadenze, sanzioni) da cio' che e' nelle norme tecniche a pagamento
(allegato 2, UNI CEI 11352/11339, ISO 50001), non riprodotte. Il DM 100/2023
(certificati bianchi/TEE) esula dal nucleo dell'art. 8 e non e' trattato in questa
prima versione.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con EGE / energy manager.
- Possibili estensioni future: trascrizione mirata dell'allegato 2 (criteri minimi
  delle diagnosi); raccordo con il DM MiSE 21/12/2017 (energivore) e con i TEE.
