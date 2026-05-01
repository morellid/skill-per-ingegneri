# CHANGELOG - oepv-valutatore-offerte-tecniche

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
