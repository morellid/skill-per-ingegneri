# CHANGELOG - trasporto-rifiuti-fir-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #65)
- Prima versione della skill di supporto documentale agli obblighi del trasporto
  dei rifiuti (D.Lgs. 152/2006, Parte quarta): formulario di identificazione
  (FIR), iscrizione all'Albo nazionale gestori ambientali, sanzioni.
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 3/4/2006 n. 152 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    af54f5e0c6fa3d0a6d3dc5cf6d33ece0be7969be086dd93a24980e11b053b9fe
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 193 (formulario FIR), 212 (Albo gestori ambientali) e 258
    (sanzioni) letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dlgs-152-2006.md`.
- Estratto operativo `references/estratti/trasporto-rifiuti-checklist.md` con FIR,
  Albo (semplificazioni) e sanzioni.
- Due task: `inquadra-obblighi.md` (FIR e Albo) e `checklist-fir.md` (gestione del
  formulario e sanzioni).
- Due esempi: trasporto rifiuti per conto terzi (Albo ordinario); officina che
  trasporta i propri rifiuti pericolosi sotto soglia (semplificazione Albo, FIR
  comunque dovuto).

### Nota di source-grounding (#65)
La scheda #65 (TR.2) chiedeva un "piano sicurezza trasporto rifiuti" ai sensi del
D.Lgs. 152/2006, segnalando un perimetro **residuale** e sovrapposto a TR.1 (ADR)
e al MUD, da definire. Poiche' il D.Lgs. 152/2006 **non prevede un "piano di
sicurezza del trasporto rifiuti" come istituto autonomo**, la skill e'
source-grounded sugli **obblighi documentali effettivi del trasporto dei rifiuti**
letti dal testo vigente su Normattiva: **formulario di identificazione (art.
193)**, **iscrizione all'Albo gestori ambientali (art. 212)** e **sanzioni (art.
258)** - cio' che e' realmente citabile nel decreto. Il modello del formulario e
il **RENTRI** (art. 188-bis), le categorie/classi dell'Albo e la disciplina **ADR**
per i pericolosi (cfr. skill consulente-adr-dlgs40 e trasporti-eccezionali) sono
citati come riferimento e non riprodotti, per non sconfinare in fonti non lette o
in un "piano" non normato.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati; seguire l'entrata a regime del RENTRI (art.
  188-bis) per il modello del formulario.
- Validazione Livello 2 da effettuare con esperto rifiuti/Albo.
- Possibili estensioni future: registri di carico/scarico (art. 190), raccordo con
  il MUD e con l'ADR per i rifiuti pericolosi.
