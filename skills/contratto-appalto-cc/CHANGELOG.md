# CHANGELOG - contratto-appalto-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #337)
- Prima versione della skill di supporto all'inquadramento del **contratto di appalto** di diritto
  privato nel **Codice civile** (R.D. 16 marzo 1942, n. 262), Libro IV, Titolo III, **Capo VII
  (Dell'appalto)**, artt. 1655-1666 e 1671, nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice civile (R.D. 262/1942)** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (codice 042U0262). Artt. 1655-1666 e 1671 via `caricaArticolo` (versione 1, idGruppo 208).
  - Trascrizione verbatim in `references/fonti/cc-appalto-1655-1671.md` (13 articoli).
- Estratto operativo `references/estratti/contratto-appalto-checklist.md`.
- Due task: `inquadra-contratto-appalto.md` e `gestisci-variazioni-recesso.md`.
- Due esempi: qualificazione appalto vs contratto d'opera e accettazione tacita; variazioni oltre il
  sesto, revisione oltre il decimo e recesso del committente.

### Contenuto ancorato al testo
- Nozione con organizzazione dei mezzi e gestione a proprio rischio (1655); subappalto previa
  autorizzazione (1656); corrispettivo (1657); materia (1658); variazioni concordate (1659),
  necessarie con soglia del sesto (1660), ordinate dal committente entro il sesto (1661); verifica
  in corso d'opera e risoluzione (1662); difetti della materia (1663); onerosita'/difficolta' con
  revisione oltre il decimo ed equo compenso per difficolta' geologiche/idriche (1664); verifica e
  pagamento con accettazione anche tacita (1665); singole partite (1666); recesso unilaterale del
  committente (1671).

### Scope e limiti
- Non redige il contratto ne' gli atti, non quantifica importi, non tratta la responsabilita' per
  difformita'/vizi/rovina (1667-1669, skill `responsabilita-appaltatore-rovina-cc`) ne' l'appalto
  pubblico (D.Lgs. 36/2023). Gli artt. 1668, 1670, 1672-1677 e l'art. 2222 (contratto d'opera) sono
  citati come rinvio.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del Codice civile pinnato (nuovo hash) e
  rileggere gli artt. 1655-1666 e 1671.
- Validazione Livello 2 con avvocato civilista / esperto di contrattualistica.
