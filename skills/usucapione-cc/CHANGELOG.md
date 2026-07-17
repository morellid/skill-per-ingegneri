# CHANGELOG - usucapione-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #333)
- Prima versione della skill di supporto documentale all'inquadramento dell'usucapione
  (acquisto della proprietà e dei diritti reali di godimento per possesso continuato),
  Codice civile (R.D. 262/1942), Libro III, Titolo VIII.
- Fonte scaricata, hashata e letta (Regola zero):
  - Codice civile (R.D. 16/3/1942 n. 262) - testo su Normattiva, pagina indice pinnata
    `!vig=2026-07-17` SHA256:
    f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (riproducibile, doppio download; codice redazionale 042U0262, stesso indice delle altre
    skill sul Codice civile). Artt. 1158 (immobili), 1159 (decennale), 1159-bis (piccola
    proprietà rurale), 1160 (universalità di mobili), 1161 (mobili), 1162 (mobili
    registrati), 1163 (vizi del possesso), 1164 (interversione), 1165 (prescrizione), 1166
    (terzo possessore) e 1167 (interruzione) letti via AJAX (caricaArticolo, idGruppo 144) e
    trascritti verbatim in `references/fonti/cc-usucapione-1158-1167.md`.
- Estratto operativo `references/estratti/usucapione-checklist.md` con la tabella dei termini
  per tipo di bene, i requisiti del possesso, il rapporto con la prescrizione e
  l'interruzione.
- Due task: `inquadra-usucapione.md` (tipo e termine) e `verifica-requisiti-possesso.md`
  (vizi, interversione, prescrizione, interruzione).
- Due esempi: usucapione ordinaria vs abbreviata di un immobile (artt. 1158-1159); detenzione,
  interversione e interruzione (artt. 1164, 1167).

### Nota di source-grounding (#333)
La skill e' source-grounded sul **testo vigente degli artt. 1158-1167 del Codice civile letto
da Normattiva** (fonte ufficiale). Le **norme generali sulla prescrizione** (artt. 2934 ss.,
2942, richiamate dagli artt. 1165-1166) e la **legge speciale** sulla piccola proprietà
rurale (art. 1159-bis) sono **citate come rinvio e non riprodotte**. La **mediazione** quale
condizione di procedibilità per l'usucapione (art. 5 D.Lgs. 28/2010) è coperta dalla skill
`mediazione-civile-conciliazione-dlgs28`. L'art. 1159-bis è rubricato su Normattiva come "Art.
1159." (idSottoArticolo 2) e riportato come tale in fonte.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati.
- Validazione Livello 2 da effettuare con avvocato civilista/CTU.
- Possibili estensioni future: possesso e azioni possessorie (artt. 1140 ss., 1168 ss.) e
  raccordo con la trascrizione della domanda giudiziale (art. 2653).
