# CHANGELOG - trasporti-eccezionali-cds-art10

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #66)
- Prima versione della skill di supporto documentale al regime dei veicoli e dei
  trasporti eccezionali (art. 10 del Codice della Strada, D.Lgs. 285/1992).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 30/4/1992 n. 285 (Codice della Strada) - testo multivigente su
    Normattiva, pagina indice pinnata `!vig=2026-07-14` SHA256:
    fbc10b72e4f07b603f1a2f915dd6a14317932c8643909e7d33b243115539870f
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    L'articolo 10 (versione 37) e' letto via AJAX (caricaArticolo) e trascritto
    verbatim in `references/fonti/dlgs-285-1992.md`.
- Estratto operativo `references/estratti/trasporti-eccezionali-checklist.md` con
  inquadramento, obbligo di autorizzazione, tipi, presupposti, prescrizioni e
  sanzioni.
- Due task: `inquadra-eccezionalita.md` (eccezionalita', autorizzazione, ente,
  tipo) e `checklist-autorizzazione.md` (presupposti, prescrizioni, sanzioni).
- Due esempi: trave prefabbricata fuori sagoma (eccezionale, autorizzazione
  multipla/periodica) e autoarticolato entro i limiti (non eccezionale).

### Nota di source-grounding (#66)
La scheda #66 (TR.5) citava l'art. 10 del Codice della Strada e le Linee guida MIT
sui trasporti eccezionali (2022, PDF). La skill e' source-grounded sul **testo
vigente dell'art. 10 del D.Lgs. 285/1992 letto da Normattiva** (fonte ufficiale),
con la pagina indice pinnata a data di vigenza per hash riproducibile e la
trascrizione verbatim dell'art. 10 (definizioni, autorizzazione, tipi, sanzioni).
Gli articoli richiamati (61 sagoma, 62 massa, 13 autorizzazioni, 54 categorie) e
le **Linee guida MIT** (2022) e il decreto attuativo del comma 10-bis sono citati
come riferimento e **non riprodotti**: il perimetro distingue cio' che e'
nell'art. 10 (obbligo, tipi, ente, sanzioni) da cio' che richiede la lettura di
altri articoli o delle linee guida operative.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere l'art. 10 (verificare la versione piu' alta; ora v. 37).
- Validazione Livello 2 da effettuare con esperto di autotrasporto.
- Possibili estensioni future: raccordo con gli artt. 61 e 62 (limiti) e con le
  Linee guida MIT per la procedura operativa e la modulistica.
