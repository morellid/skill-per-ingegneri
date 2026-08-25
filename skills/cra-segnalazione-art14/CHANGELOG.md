# CHANGELOG - cra-segnalazione-art14

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-08-25

Prima versione alpha. Closes #494.

### Added
- `SKILL.md` con instradamento alle quattro sotto-attivita', avvertenza professionale e
  regola di prudenza sui termini.
- Quattro task: `qualifica-evento-segnalabile`, `costruisci-sequenza-notifiche`,
  `individua-csirt-coordinatore`, `check-prerequisiti-interni`.
- Trascrizioni verbatim in `references/fonti/`: Reg. (UE) 2024/2847 (artt. 3, 13, 14, 15,
  16, 17, 64, 71, allegato I parte II), dir. (UE) 2022/2555 (art. 6 punti 5-6, art. 12
  par. 1), D.Lgs. 138/2024 (artt. 2, 15, 16).
- Estratti operativi `cra-art14-obblighi-e-termini.md` e
  `csirt-coordinatore-e-canale-italiano.md`.
- Due esempi: caso conforme (vulnerabilita' attivamente sfruttata su gateway IoT, due
  catene parallele) e caso problematico (PoC pubblico scambiato per sfruttamento attivo,
  ransomware sulla catena di build, cascata dell'art. 14 par. 7).
- `references/sources.yaml` con i campi `accept` / `accept_language` per le due fonti
  CELLAR (necessari per ottenere l'XHTML in italiano invece di RDF).

### Note di sviluppo

Tre precisazioni rispetto al testo della issue #494, tutte fondate sul testo letto:

- La relazione finale sull'incidente e' dovuta **entro un mese dalla trasmissione** della
  notifica delle 72 ore (art. 14, par. 4, lett. c), non entro 30 giorni.
- L'art. 71, par. 2, anticipa all'11 settembre 2026 **solo** l'art. 14 e il capo IV.
  L'art. 16 (piattaforma unica di segnalazione) e l'art. 64 (sanzioni) non sono fra le
  disposizioni anticipate. La skill riporta la lettura letterale, dichiara che non
  significa assenza di conseguenze e non la usa per suggerire rinvii.
- L'art. 64, par. 10, lett. a), esonera micro e piccole imprese per il solo mancato
  rispetto del **termine delle 24 ore**, ma deroga "ai paragrafi da 3 a 9" mentre l'art. 14
  e' sanzionato dal paragrafo 2. La skill riporta il disallineamento senza risolverlo.

Limiti noti, rinviati a versioni successive:

- Procedura di registrazione e accesso alla piattaforma dell'art. 16: fuori scope in v0.1
  perche' non disciplinata dalle fonti lette.
- Atto delegato (art. 14, par. 9) e atto di esecuzione (art. 14, par. 10): questa skill
  non ha verificato ne' letto eventuali atti adottati in base a quei paragrafi. Se
  esistono o quando saranno adottati, gli output vanno riletti alla loro luce.
- Politica nazionale CVD ex art. 16, c. 4, D.Lgs. 138/2024: non letta.
- Designazioni dei CSIRT coordinatori di Stati membri diversi dall'Italia: non lette.

Skill non ancora validata da dominio terzo. Da considerare draft finche' non passa la
validazione di Livello 2 (vedi `methodology/validazione.md`).
