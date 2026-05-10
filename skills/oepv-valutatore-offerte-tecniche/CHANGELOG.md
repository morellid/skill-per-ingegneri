# CHANGELOG - oepv-valutatore-offerte-tecniche

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-05-10

### fix(source-grounding)

- Scaricato e verificato SHA256 di `not_in_repo/dlgs-36-2023-gu87-so14.pdf` (SHA256: b139f0515a8aa018a25b7a31acce39fc39329cdc07aedd17e870dd9dc91025ff) e di `not_in_repo/anac-lg-n2-delibera-424-2018.pdf` (SHA256: 719e06f3ec3ce5b36d1f606adaa874377438a83f92fc2e47bf9c6dde7c93d1f8). Aggiornati i valori in `references/sources.yaml`.
- Creato `references/fonti/dlgs-36-2023-artt93-107-108.md`: trascrizione verbatim di art. 93 (7 commi), art. 107 (3 commi), art. 108 (12 commi) dalla GU 2023 letta. Pagine 80-81 e 96-98 del Supplemento Ordinario n. 14 GU n. 87 del 13/04/2023.
- Creato `references/fonti/anac-lg-n2-delibera-424-2018.md`: trascrizione verbatim di Sezione III (riparametrazione), Sezione IV (formule quantitative), Sezione V (elementi qualitativi), Sezione VI cap. 1 (metodo aggregativo-compensatore) del PDF ANAC Delibera 424/2018.
- Riscritto `references/estratti/dlgs-36-art93.md`: art. 93 aveva contenuto non corrispondente alla GU 2023. Errori corretti: (a) co. 1 gia' include la regola "nomina dopo scadenza offerte" - non esiste un co. 9 separato; (b) numero massimo componenti e' cinque (non "da tre a cinque"); (c) co. 3 riguarda qualifiche, non incompatibilita'; (d) co. 5 ha tre cause di ineleggibilita' (non le 10 elencate nell'estratto precedente); (e) l'art. 93 ha 7 commi (non 10+).
- Riscritto `references/estratti/dlgs-36-art107-108.md`: corretti due errori materiali: (a) art. 107 nella GU 2023 si intitola "Principi generali in materia di selezione" e non disciplina i criteri OEPV; (b) art. 108 co. 2 ha 6 fattispecie (a-f), non 8 come nell'estratto precedente (lettere g e h non esistono nel testo GU 2023); (c) ERRORE MATERIALE CORRETTO: l'art. 108 co. 7 impone esplicitamente solo il criterio parita' di genere (art. 46-bis D.Lgs. 198/2006) come obbligatorio - CO2 e welfare aziendale NON sono obbligatori nel co. 7 del testo GU 2023.
- Riscritto `references/estratti/anac-lg-n2-metodologia-oepv.md`: corretti errori nella descrizione delle formule: (a) la formula economica nel PDF ANAC e' in termini di ribasso (sconto), non di prezzo assoluto; (b) le formule per parametri crescenti/decrescenti non compaiono nel PDF ANAC LG n.2 in quella forma; (c) l'esempio numerico precedente era elaborazione dell'agent, non contenuto del PDF.
- Corretti `SKILL.md`, `tasks/costruisci-matrice-criteri.md`, `tasks/check-matrice-criteri.md`: rimosso l'errore che classificava basse emissioni CO2 e welfare aziendale come criteri "sempre obbligatori" ai sensi dell'art. 108 co. 7. Solo la parita' di genere e' esplicitamente obbligatoria. CO2 e welfare sono reclassificati come criteri premiali facoltativi.
- Corretta la lista OEPV obbligatorio in SKILL.md e tasks: rimosso "trasporto scolastico" e "DPR 328" che non compaiono nel co. 2 della GU 2023 originale.
- Aggiunto `md_path` in sources.yaml per le due fonti scaricate.
- Nota: il D.Lgs. 209/2024 correttivo non e' stato scaricabile (redirect GU non funzionante). Il testo riportato e' quello originale GU 2023. La voce correttivo in sources.yaml e' mantenuta con sha256: null e md_path: null come pending.

## [0.1.0-alpha] - 2026-05-02

### Added
- SKILL.md: entry point con routing ai 3 task, verifica OEPV obbligatorio, limiti punteggio economico, limiti
- Task `costruisci-matrice-criteri.md`: guida alla costruzione della matrice criteri/sottocriteri conforme all'art. 108 D.Lgs. 36/2023
- Task `valuta-offerta-tecnica.md`: calcolo punteggi con metodo aggregativo-compensatore (ANAC LG n.2)
- Task `check-matrice-criteri.md`: verifica conformita' matrice e segnalazione rischi TAR/CdS
- `references/sources.yaml`: 4 fonti (D.Lgs. 36/2023, correttivo 209/2024, ANAC LG n.2, D.Lgs. 198/2006 art. 46-bis)
- Estratti testuali: art. 93 (commissione giudicatrice), artt. 107-108 (criteri aggiudicazione), metodologia ANAC LG n.2
- Esempio conforme: servizi architettura/ingegneria >= 140k EUR (OEPV obbligatorio) con matrice completa
- Esempio non conforme: matrice lavori con criteri soggettivi, formula assente, bonus parita' di genere mancante
- README.md, AGENTS.md, agents/openai.yaml

### Note normative
- L'issue #5 citava "Allegato II.4 D.Lgs. 36/2023" come fonte per OEPV: quel riferimento e' errato (Allegato II.4 = qualificazione SA). La fonte corretta e' l'art. 108 D.Lgs. 36/2023. Corretto nella skill con nota in sources.yaml.
- ANAC Linea Guida n. 2 (Delibera 424/2018): non piu' formalmente vincolante sotto D.Lgs. 36/2023 ma ancora di riferimento operativo per la metodologia aggregativo-compensatore. Usata come fonte metodologica con questa avvertenza.

### Known issues / TODO v0.2
- Aggiungere esempio con calcolo completo (task `valuta-offerta-tecnica`) su 3 offerenti con dati reali
- Aggiungere gestione OEPV costo/efficacia (lifecyle costing, art. 110 D.Lgs. 36/2023)
- Validazione Livello 2 da effettuare con RUP esperto in appalti PA
- Verificare allineamento con eventuali nuove linee guida ANAC post-2023 se emesse
