# CHANGELOG - fascicolo-tecnico-macchine-reg-1230

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-18

### Added

- Prima versione alpha della skill per la redazione/verifica del fascicolo tecnico secondo il Regolamento (UE) 2023/1230.
- Catalogazione della fonte normativa unica (Reg. UE 2023/1230, GU UE L 165 del 29/06/2023) in `references/sources.yaml`, con SHA256 del PDF Eur-Lex.
- Trascrizione fedele in italiano dei paragrafi rilevanti del regolamento in `references/fonti/reg-ue-2023-1230-macchine.md` (art. 1, 2, 3, 6, 10, 11, 20, 21, 22, 23, 24, 25, 51, 52, 54; All. I parti A+B; All. III a livello strutturale; All. IV parti A+B; All. V parti A+B; All. VI, VII, VIII, IX, X; All. XI).
- Estratto operativo orientato al workflow in `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md`.
- Cinque task files:
  - `qualifica-prodotto.md` - qualifica macchina/quasi-macchina/prodotto correlato/esclusione.
  - `identifica-procedura-conformita.md` - art. 25 + All. I + Moduli A/B+C/G/H.
  - `struttura-fascicolo-tecnico.md` - indici All. IV parte A (lett. a-o) e parte B (lett. a-m).
  - `check-completezza-fascicolo.md` - audit voce per voce.
  - `struttura-dichiarazione-ue.md` - All. V parte A (10 voci) e parte B (9 voci).
- Due esempi:
  - `pressa-piegatrice-allegato-i-parte-b/` - caso conforme (categoria 9 All. I parte B, Modulo A condizionato).
  - `quasi-macchina-attuatore-lineare-incompleto/` - caso problematico (utente confonde quasi-macchina con macchina, vorrebbe marcatura CE).

### Note di sviluppo

- Skill non ancora validata da dominio terzo (Livello 2).
- Da considerare draft finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
- Le norme armonizzate UNI/CEN richiamate dal regolamento (es. UNI EN ISO 12100, UNI EN ISO 13849-1, UNI EN 60204-1, UNI EN 12622) sono proprietary-paid e non incluse come fonti: la skill ne usa solo rinvii strutturali (numero, ambito), in coerenza con la regola generale del repo.
- L'Allegato III (RES) non e' trascritto: la skill rinvia alla lettura diretta del regolamento per la matrice RES applicabili al caso concreto.
- Il regime transitorio della direttiva 2006/42/CE (prodotti immessi sul mercato prima del 14/01/2027) non e' coperto: skill dedicata da creare.
