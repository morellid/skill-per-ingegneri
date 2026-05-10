# CHANGELOG - valutazione-impatto-clima-acustico-l-447

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Source-grounding remediation - hash dinamico GU.it (issue #113,
  seconda parte, closes #113):
  - Rimossi `binary_path` e `sha256` per le fonti `dpcm-14-11-1997-limiti`
    e `dm-16-03-1998-tecniche` (impostati a `null`). Il portale
    gazzettaufficiale.it serve HTML dinamico: lo stesso URL restituisce
    contenuto diverso ad ogni fetch (header, timestamp, metadati di
    sessione), rendendo impossibile archiviare un binario stabile con
    hash verificabile in CI. I file HTML locali in `not_in_repo/`
    presentavano hash diversi da quelli originariamente dichiarati in
    `sources.yaml` (dpcm: dichiarato `265982c3...`, locale
    `ead814fd...`; dm: dichiarato `76e067861...`, locale `ff1a5aa1...`),
    confermando l'instabilita' del contenuto servito.
  - Verificato che entrambi i `references/fonti/` siano trascrizioni
    fedeli dei testi ufficiali letti localmente:
    - `fonti/dpcm-14-11-1997-limiti.md`: testo integrale confermato
      rispetto a `not_in_repo/dpcm-14-11-1997-gu.txt`; artt. 1-10 e
      Tabelle A-D con tutti i valori dB corretti (es. Tabella B:
      Classe I 45/35 dB, Classe VI 65/65 dB; Tabella C: Classe I
      50/40 dB, Classe V-VI 70/70 dB; art. 4: differenziale 5 dB
      diurno / 3 dB notturno).
    - `fonti/dm-16-03-1998-tecniche.md`: testo integrale confermato
      rispetto a `not_in_repo/dm-16-03-1998-gu.txt`; artt. 1-4 e
      allegati A-D con tutte le definizioni, le norme tecniche, le
      metodologie di misura ferroviaria e stradale e il formato di
      presentazione dei risultati.
  - I `md_path` restano dichiarati e i file esistono: la Regola zero
    e' rispettata (la prova di lettura della fonte e' il file fonti
    committato, non il binario non archiviabile).

- Source-grounding remediation (issue #113, prima parte):
  - Creati 3 file `references/fonti/` con trascrizione fedele dei testi
    ufficiali letti dai binari in `not_in_repo/`:
    - `fonti/legge-447-1995-mase.md` (art. 2 cc. 1 e)-h), 3, 6-7;
      art. 4 c. 1 lett. l; art. 6 c. 1 lett. d; art. 8 cc. 1-6)
    - `fonti/dpcm-14-11-1997-limiti.md` (testo integrale: artt. 1-10
      + tabelle A, B, C, D)
    - `fonti/dm-16-03-1998-tecniche.md` (testo integrale: artt. 1-4
      + allegati A, B, C, D)
  - Aggiunto campo `md_path` in `references/sources.yaml` per le 3
    fonti con binario scaricato; impostato `md_path: null` per le
    2 fonti reference-only (Normattiva).
  - Corretto `sha256: ""` in `sha256: null` per le 2 fonti
    reference-only (legge-447-1995-normattiva, dlgs-42-2017-normattiva)
    che hanno `binary_path: null` e non sono scaricate come binario.

### Changed

- Hardening review-driven (Codex adversarial review):
  - aggiunta entry reference-only `dlgs-42-2017-normattiva` in
    `references/sources.yaml` (rinvio Normattiva al D.Lgs. 17/2/2017
    n. 42 art. 21 - TCAA), per ancorare le citazioni del decreto
    nelle parti dei task ed esempi che le richiamano;
  - rianchoraggio della firma TCAA come requisito bloccante su
    L. 447/1995 art. 2 cc. 6-7 (testo originario, presente
    nell'estratto di repo) + rinvio testo vigente D.Lgs. 42/2017
    art. 21 su Normattiva, in entrambi gli `expected-output.md`
    degli esempi;
  - `tasks/checklist-relazione-previsionale.md` C.1 e
    `tasks/check-completezza-clima-acustico.md` 6.2.3:
    posizionamento del microfono ora distinto per contesto di
    misura (ambienti abitativi: DM 16/3/1998 allegato B punto 5;
    esterno generico: allegato B punto 6; rumore stradale o
    ferroviario: allegato C);
  - `tasks/check-completezza-clima-acustico.md` 4.4: criterio
    differenziale chiarito come **di norma non applicabile** in
    fase previsionale di clima acustico (manca una sorgente
    specifica determinata gia' soggetta a valutazione di impatto
    autonoma), allineato con il commento corrispondente nelle
    note degli esempi.

## [0.1.0-alpha] - 2026-05-08

### Added

- Prima versione alpha della skill (Livello 1).
- `SKILL.md` con frontmatter dual-agent (`license: MIT`) e
  disclaimer professionale.
- `agents/openai.yaml` con `display_name`, `short_description` e
  `default_prompt`.
- 4 task files in `tasks/`:
  - `mappa-applicabilita-art-8.md` (c. 2 / c. 3 / c. 4 / c. 6 della
    L. 447/1995 art. 8)
  - `check-completezza-impatto-acustico.md`
  - `check-completezza-clima-acustico.md`
  - `checklist-relazione-previsionale.md`
- 3 estratti normativi in `references/estratti/`:
  - `legge-447-1995-art-8.md` (art. 8 cc. 1-6, art. 4 c. 1 lett. l,
    art. 6 c. 1 lett. d, art. 2 definizioni)
  - `dpcm-14-11-1997-valori-limite.md` (art. 1-8 + Tabelle A, B, C, D)
  - `dm-16-03-1998-tecniche-misurazione.md` (art. 1-2 + allegati A,
    B, C, D)
- 4 fonti registrate in `references/sources.yaml` (L. 447/1995 PDF
  MASE, DPCM 14/11/1997 HTML aggregato GU, DM 16/3/1998 HTML aggregato
  GU, L. 447/1995 Normattiva reference-only).
- 2 esempi in `examples/`:
  - `palestra-classe-iv-conforme/` (caso conforme con dettagli sul
    passaggio dal periodo diurno al notturno e sul differenziale)
  - `scuola-prossima-strada-incompleta/` (caso problematico:
    valutazione di clima acustico priva di firma TCAA, di misure e
    di rinvio al DPR 142/2004)
- `AGENTS.md` di skill con convenzioni di dominio specifiche.
- `README.md` di skill con target, sotto-attivita', fonti, limiti.

### Note di sviluppo

- Skill non ancora validata da dominio terzo.
- Da considerare draft finche' non passa validazione Livello 2 (vedi
  `methodology/validazione.md`).
- Rinvii strutturali a DPR 459/1998 (ferroviario) e DPR 142/2004
  (stradale) senza quotarne i numeri; valutare in v0.2 se aggiungere
  estratti dedicati di queste due fonti.
- Rinvio sempre alla **legge regionale** (art. 4 c. 1 lett. l) L.
  447/1995) e al **regolamento comunale** (art. 6 c. 2 L. 447/1995):
  la skill non quota i contenuti regionali/comunali.
