# CHANGELOG - edilizia-libera-cila-scia-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #325)
- Prima versione della skill di supporto documentale ai regimi del titolo edilizio
  diversi dal permesso di costruire (edilizia libera, CILA, SCIA, SCIA in alternativa al
  PdC), Titolo II del DPR 380/2001.
- Fonte scaricata, hashata e letta (Regola zero):
  - D.P.R. 6/6/2001 n. 380 - testo su Normattiva, pagina indice pinnata `!vig=2026-07-17`
    SHA256: bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f
    (riproducibile, doppio download; codice redazionale 001G0429, stesso indice delle
    altre skill DPR 380). Artt. 6 (attività edilizia libera), 6-bis (CILA), 22 (SCIA) e 23
    (SCIA in alternativa al permesso di costruire) letti via AJAX (caricaArticolo, idGruppo
    2 per 6/6-bis, idGruppo 6 per 22/23) e trascritti verbatim in
    `references/fonti/dpr-380-2001-6-6bis-22-23.md` (incluse lettere/commi abrogati e
    aggiornamenti 29, 66, 69).
- Estratto operativo `references/estratti/titoli-edilizi-checklist.md` con edilizia libera,
  CILA, SCIA, SCIA alternativa e una sintesi decisionale.
- Due task: `scegli-titolo-edilizio.md` (scelta del regime dalla categoria art. 3) e
  `imposta-scia-alternativa.md` (adempimenti SCIA/SCIA alternativa: relazione, termini,
  contributo, efficacia, collaudo).
- Due esempi: CILA vs SCIA per manutenzione straordinaria (discrimine parti strutturali);
  edilizia libera (serra mobile, vasca acque meteoriche) e SCIA alternativa al PdC in
  attuazione di piano attuativo.

### Nota di source-grounding (#325)
La skill e' source-grounded sul **testo vigente degli artt. 6, 6-bis, 22, 23 del DPR
380/2001 letto da Normattiva** (fonte ufficiale). La **qualificazione dell'intervento**
(art. 3) e il **permesso di costruire** (art. 10, 20) sono coperti da skill dedicate
(`definizioni-interventi-edilizi-dpr380`, `permesso-costruire-dpr380`) e qui citati come
rinvio. Il **glossario dell'edilizia libera** (DM 2/3/2018) e la **modulistica unificata**
(skill `modulistica-edilizia-unificata`) non sono riprodotti. Gli artt. 16, 37, 44 e
l'art. 19 della L. 241/1990 sono citati. Il testo tra doppi tondi `(( ))` e le note di
abrogazione sono riportati come da fonte.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati (il DPR 380 è oggetto di frequenti correttivi, es. D.Lgs. 190/2024,
  D.Lgs. 178/2025).
- Validazione Livello 2 da effettuare con tecnico abilitato/esperto edilizia.
- Possibili estensioni future: raccordo con la disciplina sanzionatoria (artt. 37, 44,
  skill `vigilanza-sanzioni-abusi-edilizi-dpr380`) e con la modulistica regionale.
