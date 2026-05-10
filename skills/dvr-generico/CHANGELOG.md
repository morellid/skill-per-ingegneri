# CHANGELOG - dvr-generico

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### fix(source-grounding) - 2026-05-10

- Sostituito `references/sources.yaml` da template placeholder a fonte reale:
  `dlgs-81-2008-art-17-28-29-normattiva` con URL normattiva.it vigente.
- Creato `references/fonti/dlgs-81-2008-art-17-28-29.md`: trascrizione verbatim
  degli artt. 17, 28 e 29 di D.Lgs. 81/2008 letti direttamente da normattiva.it
  il 2026-05-10 (testo vigente).
- Aggiornato header estratto `dlgs-81-art-17-28-29.md`: riferimento a nuovo id
  fonte e URL normattiva.it.
- Corretto errore semantico in `dlgs-81-art-17-28-29.md` par. 1-bis: "Obbligo
  dal 31/12/2010" sostituito con "a fare data dal 1 agosto 2010" (testo vigente
  art. 28 co. 1-bis normattiva.it: "a fare data dal 1 agosto 2010").

### Da fare
- Validazione Livello 1 con `scripts/validate.sh`
- Validazione Livello 2 da RSPP esterno (potenziale validatore: Vitale per profilo RSPP)
- Test su DVR reale di una PMI (con consenso datore di lavoro)
- Esempi aggiuntivi per settori specifici:
  - `dvr-manifattura/` - PMI metalmeccanica con rumore + chimico + MMC
  - `dvr-sanita-studio-medico/` - studio medico/dentistico con biologico + chimico
  - `dvr-ristorazione/` - ristorante con microclima + tagli + ustioni
  - `check-dvr-incompleto/` - DVR con carenze tipiche
- Catalogare e integrare riferimenti specifici INAIL OIRA
- Estratti normativi da aggiungere per Titoli specifici (rumore, MMC, VDT) man mano che la skill copre settori

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold via `scripts/new-skill.sh`
- `SKILL.md` con frontmatter, routing a 4 task files, disclaimer art. 55 sanzioni
- 1 estratto normativo:
  - `references/estratti/dlgs-81-art-17-28-29.md` - testo + tassonomia rischi tipici + 6 contenuti minimi
- 4 task files:
  - `tasks/draft-dvr.md` - stesura completa o procedure standardizzate per < 50 lav
  - `tasks/check-dvr.md` - verifica conformita' 6 elementi + formali + Titoli specifici
  - `tasks/valuta-aggiornamento.md` - 4 causali esplicite art. 29 co. 3 + casi di prassi
  - `tasks/mappa-rischi-mansione.md` - tabella rischi per 12 profili tipici (ufficio, magazzino, produzione, edilizia, sanita', servizi, ristorazione, trasporti, pulizie, insegnamento, commercio, sicurezza)
- `references/sources.yaml` con hash SHA256 reuso da `pos-allegato-xv-checker` (stessa fonte)
- 1 esempio:
  - `examples/dvr-pmi-ufficio/` - PMI 25 dipendenti settore IT con uffici + smart working strutturale. DVR completo con 12 rischi identificati, programma miglioramento concreto, sezione smart working, stress lavoro-correlato Fase 1, differenze, autoverifica completezza.

### Note di sviluppo
- Skill considerata draft finche' non passa Livello 2 (RSPP esterno)
- Validatore di dominio target: RSPP con esperienza multi-settore
- Sinergica con: `pos-allegato-xv-checker` (cantieri), `gdpr-registro-dpia` (privacy lavoratori), `ai-act-compliance` (AI per HR)

### Sanzioni di riferimento
- Omessa redazione DVR: arresto 3-6 mesi o ammenda 2.949 - 7.532 EUR
- DVR senza lett. b/c/d (art. 28 co. 2): ammenda 2.847 - 5.695 EUR
- DVR senza lett. a primo periodo o f: ammenda 1.423 - 2.847 EUR
