# CHANGELOG - gdpr-registro-dpia

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Da fare
- Validazione Livello 1 con `scripts/validate.sh`
- Validazione Livello 2 da DPO esterno o ingegnere informazione/cybersecurity
- Test su Registro reale di una PMI italiana (con consenso titolare)
- Aggiungere esempio "registro-incompleto" per check
- Catalogare e citare il Codice di Deontologia sistemi informativi creditizi (Allegato A.5 Cod. Privacy) per casi fintech
- Aggiungere riferimenti a linee guida EDPB tematiche (videosorveglianza, AI, biometria, lavoro)

## [0.1.1] - 2026-05-10

### fix(source-grounding): remediation semantica (closes #101)

**Fonti scaricate e verificate** (2026-05-10):

- `gdpr-it-garante-2018`: SHA256 `16c0bb35...` verificato scaricando dalla URL aggiornata del Garante
  (l'URL originale in sources.yaml restituiva 404; aggiornato a `garante/document?ID=6264597`).
  Creato `references/fonti/gdpr-it-garante-2018.md` con trascrizione di art. 30 (pag. 66),
  art. 35 (pag. 70), art. 36 (pag. 71).
- `garante-prov-467-2018-allegato1`: SHA256 `6ece43c2...` verificato. Creato
  `references/fonti/garante-prov467-2018-allegato1.md` con trascrizione integrale delle 12 tipologie.
- `wp248-rev01-edpb`: scaricato da `ec.europa.eu/newsroom/just/document.cfm?doc_id=47711`.
  SHA256 `4de1ee2d...` calcolato. Creato `references/fonti/wp248-rev01.md` con trascrizione
  delle sezioni rilevanti (Sez. I, III.B.a pag. 9-11, III.D.c, III.E).

**Estratti riscritti / corretti**:

- `references/estratti/gdpr-art-35-36.md`: rimossa la tabella dei 9 criteri WP248 (pag. 9-11
  WP248), erroneamente attribuita alla fonte GDPR. Sostituita con rimando all'estratto dedicato
  `wp248-criteri.md`. Il contenuto GDPR (art. 35 par. 1-11, art. 36) era accurato e resta invariato.
- `references/estratti/garante-allegato1-prov467-2018.md`: rimosse le sezioni "Note interpretative
  del Garante" e "Tipologie per ingegneri" non presenti nel PDF sorgente (Allegato 1 Provv. 467/2018
  contiene solo l'elenco delle 12 tipologie, senza note interpretative aggiuntive). Il testo delle
  12 tipologie era accurato e resta invariato.
- Creato `references/estratti/wp248-criteri.md`: nuovo estratto con i 9 criteri tratti dal testo
  verificato di WP248 rev. 01, con riferimenti precisi a sezione e pagina.

**Aggiornamenti sources.yaml**:
- Aggiunto `md_path` per tutte e tre le fonti principali.
- Aggiunto SHA256 per `wp248-rev01-edpb`.
- Aggiunto `download_url` per `wp248-rev01-edpb`.
- Aggiornato `url` e `download_url` per `gdpr-it-garante-2018` (URL precedente 404).

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold completo della skill via `scripts/new-skill.sh`
- `SKILL.md` con frontmatter, routing a 4 task files (draft+check registro, valuta soglia DPIA, draft DPIA), disclaimer art. 83 GDPR
- 4 task files operativi:
  - `tasks/draft-registro-trattamenti.md` - stesura Registro guidata, 7 voci titolare / 4 responsabile
  - `tasks/check-registro-trattamenti.md` - verifica completezza con pattern di problemi comuni
  - `tasks/valuta-soglia-dpia.md` - 12 tipologie Garante + 9 criteri WP248 + art. 35 par. 3
  - `tasks/draft-dpia.md` - stesura DPIA con 4 contenuti minimi par. 7 e tabella rischi-misure
- 3 estratti normativi:
  - `references/estratti/gdpr-art-30.md` - testo art. 30 + sintesi 7 contenuti minimi
  - `references/estratti/gdpr-art-35-36.md` - testo art. 35-36 + 9 criteri WP248
  - `references/estratti/garante-allegato1-prov467-2018.md` - 12 tipologie italiane
- `references/sources.yaml` con hash SHA256 reali per:
  - GDPR italiano consolidato Garante (16c0bb35...)
  - Garante Allegato 1 Provv. 467/2018 (6ece43c2...)
- 2 esempi:
  - `examples/registro-pmi-base/` - PMI 50 dipendenti, 6 trattamenti tipici (HR, CRM, fornitori, marketing, videosorveglianza, sito web). Expected: CONFORME CON NOTE MINORI con T5 da chiarire e T2 da documentare.
  - `examples/dpia-soglia-app-scoring/` - sistema scoring credito con decisioni automatizzate. Expected: DPIA OBBLIGATORIA con 4 tipologie + 7 criteri attivati + lista 9 punti attenzione per la DPIA.

### Note di sviluppo
- Skill considerata draft finche' non passa Livello 1 di validazione (vedi `methodology/validazione.md`)
- Validatore di dominio target: DPO esperto o ingegnere informazione con esperienza compliance privacy
- Settori di applicazione tipici: SaaS B2B, fintech, app mobile, IoT, AI/ML systems
