# CHANGELOG - fascicolo-opera-manutenzione-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #480)
- Prima versione della skill di supporto al **coordinatore per la sicurezza (CSP/CSE)** e al **committente** per la
  **predisposizione**, l'**aggiornamento** e la **verifica di completezza** del **Fascicolo con le caratteristiche
  dell'opera** secondo il **D.Lgs 81/2008**, **art. 91 comma 1 lett. b)**, art. 92 e **Allegato XVI**, nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs 9 aprile 2008 n. 81** - Testo coordinato Edizione gennaio 2025 (INL) - SHA256
    f593e1806de920dc16def37920c5623cda2450075ed56051852f2caf6045899a (doppio download riproducibile, stesso file usato
    dalle skill pos-allegato-xv-checker e psc-piano-sicurezza-coordinamento-dlgs81).
  - Artt. 91-92 e Allegato XVI estratti con `pdftotext -layout` (testo legale in prosa; le schede sono moduli) e
    trascritti in `references/fonti/dlgs-81-2008-art-91-92-allegato-xvi.md`.
- Estratto operativo `references/estratti/fascicolo-checklist.md`.
- Due task: `inquadra-struttura-e-schede-fascicolo.md` e `imposta-misure-per-interventi-successivi.md`.
- Due esempi: struttura di un fascicolo per un edificio; misure in dotazione/ausiliarie per la manutenzione della
  copertura.

### Contenuto ancorato al testo
- Titolarità/ciclo di vita: il CSP predispone il fascicolo (art. 91 c.1 lett. b), il CSE lo adegua all'evoluzione dei
  lavori (art. 92 c.1 lett. b), il committente lo aggiorna a seguito delle modifiche nella vita dell'opera; non è
  predisposto per i lavori di manutenzione ordinaria (art. 3 c.1 lett. a DPR 380); accompagna l'opera per tutta la sua
  durata di vita; per le opere pubbliche tiene conto del piano di manutenzione. Struttura (Allegato XVI): 3 capitoli.
  Cap. I descrizione sintetica dell'opera e soggetti coinvolti (scheda I). Cap. II individuazione dei rischi e delle
  misure preventive/protettive in dotazione dell'opera (incorporate) e ausiliarie (richieste ai datori/lavoratori
  autonomi dei lavori successivi) per gli interventi successivi prevedibili (manutenzioni ordinarie/straordinarie),
  schede II-1/II-2/II-3; sette elementi (accessi; sicurezza luoghi; impianti alimentazione/scarico; approvvigionamento/
  movimentazione materiali; approvvigionamento/movimentazione attrezzature; igiene; interferenze e protezione terzi);
  informazioni per utilizzare le misure in sicurezza e mantenerle nel tempo (verifiche, interventi manutentivi,
  periodicità); tavole con portanza/resistenza di solai e strutture, percorso/ubicazione impianti e sottoservizi. Cap.
  III riferimenti alla documentazione di supporto esistente (schede III-1/III-2/III-3).

### Scope e limiti
- Non redige il fascicolo al posto del coordinatore né progetta le misure concrete (linee vita/ganci — norme UNI); non
  compila le schede. Non tratta il PSC (art. 100 + Allegato XV), il POS (Allegato XV punto 3.2), i ruoli/obblighi CSP/
  CSE (artt. 89-92) né la notifica preliminare (art. 99). Non sostituisce il coordinatore firmatario.

### Note di sviluppo
- Distinta da `psc-piano-sicurezza-coordinamento-dlgs81` (PSC), `pos-allegato-xv-checker` (POS) e
  `coordinatori-sicurezza-cantieri-dlgs81` (artt. 89-92). Condivide la fonte (Testo coordinato INL del D.Lgs 81/2008).
  Validazione Livello 2 con coordinatore per la sicurezza CSP/CSE abilitato.
