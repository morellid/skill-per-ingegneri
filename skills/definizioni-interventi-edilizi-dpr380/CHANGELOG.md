# CHANGELOG - definizioni-interventi-edilizi-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #309)
- Prima versione della skill di supporto alla **qualificazione dell'intervento
  edilizio** secondo le definizioni dell'**art. 3 del D.P.R. 380/2001**, nell'area
  `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 6/6/2001 n. 380** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f
    (codice 001G0429). Art. 3 versione 11, idGruppo 1, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-380-2001-art-3.md`.
- Estratto operativo `references/estratti/definizioni-interventi-checklist.md`.
- Due task: `qualifica-intervento.md` e `distingui-nuova-costruzione.md`.
- Due esempi: frazionamento vs demolizione-ricostruzione (lett. b/d); pertinenza oltre
  il 20% del volume (lett. e.6).

### Contenuto ancorato al testo
- Art. 3 c. 1: manutenzione ordinaria (a), manutenzione straordinaria (b, incl.
  frazionamento/accorpamento e modifiche ai prospetti per agibilita'/accesso), restauro
  e risanamento conservativo (c), ristrutturazione edilizia (d, incl. demolizione e
  ricostruzione con diversi sagoma/sedime salvo vincoli D.Lgs. 42/2004 e zone A, e
  ripristino di crollati), nuova costruzione (e, sottocasi e.1-e.7: manufatti/ampliamenti
  fuori sagoma, urbanizzazioni, infrastrutture, torri/tralicci, manufatti leggeri,
  pertinenze > 20%, depositi/impianti produttivi), ristrutturazione urbanistica (f); c.
  2 prevalenza delle definizioni sugli strumenti urbanistici.

### Scope e limiti
- Non seleziona il titolo (CILA/SCIA/PdC - rinvio a modulistica-edilizia-unificata), non
  redige la pratica, non applica il Salva Casa ne' valuta lo stato legittimo (art.
  9-bis), non tratta il mutamento d'uso (art. 23-ter) ne' i vincoli D.Lgs. 42/2004, non
  sostituisce il progettista o il Comune. D.Lgs. 42/2004, DM 1444/1968 e D.Lgs. 490/1999
  citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del DPR 380/2001 pinnato (nuovo
  hash) e rileggere l'art. 3 (testo tra `(( ))`, es. Salva Casa DL 69/2024 conv. L.
  105/2024).
- Validazione Livello 2 con tecnico comunale / esperto di diritto edilizio.
