# CHANGELOG - denuncia-autorizzazione-sismica-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #330)
- Prima versione della skill di supporto documentale agli adempimenti per le costruzioni in
  zone sismiche (denuncia dei lavori, autorizzazione preventiva e classificazione degli
  interventi strutturali), Parte II Capo IV del DPR 380/2001.
- Fonte scaricata, hashata e letta (Regola zero):
  - D.P.R. 6/6/2001 n. 380 - testo su Normattiva, pagina indice pinnata `!vig=2026-07-17`
    SHA256: bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f
    (riproducibile, doppio download; codice redazionale 001G0429, stesso indice delle altre
    skill DPR 380). Artt. 93 (denuncia dei lavori e presentazione dei progetti), 94
    (autorizzazione per l'inizio dei lavori) e 94-bis (disciplina degli interventi
    strutturali in zone sismiche) letti via AJAX (caricaArticolo, idGruppo 18) e trascritti
    verbatim in `references/fonti/dpr-380-2001-93-94-94bis.md` (incluse le sigle (R)/(L) e le
    modifiche del D.L. 32/2019 tra doppi tondi).
- Estratto operativo `references/estratti/sismica-checklist.md` con prerequisito
  (classificazione sismica), denuncia/deposito (art. 93), autorizzazione (art. 94),
  classificazione degli interventi e regime (art. 94-bis).
- Due task: `inquadra-denuncia-autorizzazione.md` (preavviso/deposito e autorizzazione) e
  `classifica-intervento-sismico.md` (rilevante/minore/privo di rilevanza e regime).
- Due esempi: nuova costruzione ordinaria in zona 2 (minore rilevanza, deroga); adeguamento
  di edificio strategico in zona 1 (rilevante, autorizzazione) vs riparazione locale in zona
  3 (minore rilevanza).

### Nota di source-grounding (#330)
La skill e' source-grounded sul **testo vigente degli artt. 93, 94, 94-bis del DPR 380/2001
letto da Normattiva** (fonte ufficiale). Le **linee guida MIT** (DM 30/4/2018) sulla
classificazione degli interventi e le **elencazioni/procedure regionali** sono **citate come
rinvio e non riprodotte**. La **classificazione sismica** del sito (zone 1-4, art. 83), la
**denuncia delle opere in c.a./acciaio** (art. 65, skill
`denuncia-opere-strutturali-l1086`), il **collaudo statico** (art. 67) e le **NTC** (DM
17/1/2018, calcolo) sono citati come rinvio. Il testo tra doppi tondi `(( ))` e le sigle
(R)/(L) sono riportati come da fonte.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati.
- Validazione Livello 2 da effettuare con ingegnere strutturista/ufficio sismica regionale.
- Possibili estensioni future: raccordo con la denuncia opere in c.a. (art. 65), il collaudo
  statico (art. 67) e trascrizione mirata dell'art. 83 (classificazione sismica).
