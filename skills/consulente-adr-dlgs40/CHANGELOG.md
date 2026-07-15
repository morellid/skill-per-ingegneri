# CHANGELOG - consulente-adr-dlgs40

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #48)
- Prima versione della skill di supporto documentale agli obblighi relativi al
  consulente per la sicurezza dei trasporti di merci pericolose (DGSA) ai sensi
  del D.Lgs. 40/2000.
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 4/2/2000 n. 40 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    369d13494a52b29b29c9f96794a9ed08b94579e8529767dc09c348c035c894f4
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 2 (campo di applicazione), 3 (obblighi del capo dell'impresa), 4
    (obblighi del consulente), 5 (qualificazione) e 6 (sanzioni) letti via AJAX
    (caricaArticolo) e trascritti verbatim in
    `references/fonti/dlgs-40-2000.md`.
- Estratto operativo `references/estratti/consulente-adr-checklist.md` con
  ambito, esenzioni, obblighi, qualificazione e sanzioni.
- Due task: `verifica-obbligo-nomina.md` (obbligo/esenzioni) e
  `checklist-adempimenti.md` (adempimenti e sanzioni).
- Due esempi: impresa di autotrasporto obbligata; officina con trasporti
  occasionali sotto soglia (esente).

### Nota di source-grounding (#48)
La scheda #48 (TR.1) citava il D.Lgs. 40/2000 e l'Accordo ADR 2025 (UNECE). La
skill e' source-grounded sul **testo vigente del D.Lgs. 40/2000 letto da
Normattiva** (fonte ufficiale), con la pagina indice pinnata a data di vigenza per
hash riproducibile e la trascrizione verbatim degli artt. 2-6. Il **formato della
relazione annuale** e il merito tecnico sono definiti dall'**ADR, capitolo 1.8.3**
(UNECE), richiamato dal **D.Lgs. 35/2010** (dir. 2008/68/CE): citati come
riferimento e non riprodotti. Il perimetro distingue cio' che e' nel D.Lgs.
40/2000 (obbligo di nomina, adempimenti, sanzioni) da cio' che e' nell'ADR
(contenuto tecnico della relazione e delle regole di trasporto).

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati; verificare il raccordo con il D.Lgs. 35/2010
  e l'ADR vigente.
- Gli importi delle sanzioni dell'art. 6 sono espressi in lire nel testo (importi
  originari): eventuale conversione in euro secondo il tasso di legge.
- Validazione Livello 2 da effettuare con consulente DGSA.
