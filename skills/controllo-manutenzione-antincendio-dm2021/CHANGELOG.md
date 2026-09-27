# CHANGELOG - controllo-manutenzione-antincendio-dm2021

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0-alpha] - 2026-09-27

### Changed (closes #502)
- Trigger normativo: **D.M. 22 settembre 2026** (GU Serie Generale n. 222 del 24/09/2026, cod. 26A05078), che
  inserisce l'**art. 6-bis** (disposizioni transitorie) nel D.M. 1/9/2021. Recepiti anche i precedenti decreti di
  modifica non ancora presenti nella skill: D.M. 15/9/2022 (GU n. 224/2022), D.M. 31/8/2023 (GU n. 212/2023), D.M.
  13/9/2024 (GU n. 219/2024), D.M. 15/7/2025 (GU n. 190/2025). PDF scaricati con `scripts/fetch-sources.sh`, SHA256 in
  `references/sources.yaml`, operativo trascritto in
  `references/fonti/dm-modifiche-2022-2026-controllo-manutenzione-antincendio.md`.
- Fonte base aggiornata al testo consolidato: art. 6 c.1-bis (art. 4 sulla qualificazione in vigore dal **25/9/2026**),
  art. 6-bis, All. II punto 1 c.5 e punto 4 c.4 (testo D.M. 13/9/2024), punto 5 c.5-bis, Prospetti 3.8.1/3.8.2/3.14,
  denominazione della Direzione centrale.
- `verifica-qualificazione-manutentori`: obbligo di qualifica dal 25/9/2026; art. 6-bis (chi ha presentato istanza
  entro il 25/9/2026 prosegue per le tipologie dell'istanza fino all'esito e comunque non oltre il 31/3/2027);
  qualifica per tipologia di impianto.

### Fixed
- Esonero dal corso per chi ha ≥3 anni di attività: la skill diceva che il soggetto "deve comunque sottoporsi alla
  valutazione", mentre il testo (sia originario sia sostituito dal D.M. 13/9/2024) dice che "può richiedere" la
  valutazione (semplificata); l'attestazione resta subordinata a valutazione positiva (All. II punto 1 c.6).
  Corretti task, checklist, AGENTS.md ed esempio `periodicita-e-manutentore`.

### Note
- La issue #502 ipotizzava la fine netta del transitorio e l'invalidità dei "NOT (Nulla Osta Transitori)": il testo del
  D.M. 22/9/2026 introduce invece una disciplina transitoria fino al 31/3/2027 e non menziona alcun "NOT"; la skill
  segue il testo della GU.

## [0.1.0-alpha] - 2026-07-25

### Added (closes #482)
- Prima versione della skill di supporto documentale per il **controllo e la manutenzione degli impianti, attrezzature
  ed altri sistemi di sicurezza antincendio** nei luoghi di lavoro secondo il **D.M. 1° settembre 2021** (attuativo
  dell'**art. 46 c. 3 lett. a) punto 3 del D.Lgs 81/2008**), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.M. 1° settembre 2021** — GU Serie Generale n. 230 del 25/09/2021 — SHA256
    560643c7e75e6c459159f15dfbfceba055269f2bd6907149d28516b4d47eb749 (doppio download riproducibile).
  - Decreto (artt. 1-6) e Allegati I-II estratti con `pdftotext -layout` (impaginazione a due colonne ricomposta a
    mano) e trascritti in `references/fonti/dm-1-9-2021-controllo-manutenzione-antincendio.md`.
- Estratto operativo `references/estratti/controllo-manutenzione-checklist.md`.
- Due task: `inquadra-registro-e-livelli-controllo.md` e `verifica-qualificazione-manutentori.md`.
- Due esempi: registro dei controlli per un'attività; periodicità/norma di riferimento e verifica del manutentore.

### Contenuto ancorato al testo
- Tre livelli di attività (art. 1): sorveglianza (controlli visivi tra due controlli periodici, effettuabile dal
  lavoratore istruito), controllo periodico (verifica della completa e corretta funzionalità con frequenza non
  superiore a quella indicata), manutenzione (mantenere in efficienza ed in buono stato). Registro dei controlli (All.
  I punto 1): predisposto dal datore di lavoro, annota controlli periodici e interventi di manutenzione secondo le
  cadenze da norme/specifiche/manuale, aggiornato e disponibile per gli organi di controllo. Tabella 1 (All. I): norme
  UNI di riferimento per tipologia (estintori UNI 9994-1; reti di idranti UNI 10779/EN 671-3/EN 12845; sprinkler UNI
  EN 12845; IRAI UNI 11224; EVAC UNI ISO 7240-19 o CEN/TS 54-32; evacuazione fumo e calore UNI 9494-3; ecc.);
  presunzione di conformità ma applicazione volontaria (art. 3 c.2). Tecnici manutentori qualificati (art. 4 + All.
  II): manutenzione e controllo periodico eseguiti da tecnici qualificati (formazione + valutazione + attestazione del
  Corpo nazionale dei vigili del fuoco); qualifica valida su tutto il territorio nazionale; regime transitorio per chi
  ha ≥3 anni di attività alla data di entrata in vigore (esonero dal corso, non dalla valutazione). Entrata in vigore
  dal 25/9/2022 (art. 6); abrogati art. 3 c.1 lett. e), art. 4 e allegato VI del D.M. 10/3/1998 (art. 5).

### Scope e limiti
- Non fissa le periodicità puntuali dei controlli (rinvio alle norme UNI di prodotto, non trascritte per diritto
  d'autore); non rilascia/attesta la qualifica del manutentore (è del Corpo nazionale dei vigili del fuoco); non
  certifica il registro. Non tratta la gestione dell'emergenza (D.M. 2/9/2021), la progettazione antincendio (D.M.
  3/9/2021), il DPR 151/2011 né il carico d'incendio (D.M. 9/3/2007).

### Note di sviluppo
- Distinta da `piano-emergenza-antincendio-dm2021` (D.M. 2/9/2021), `prevenzione-incendi-attivita-procedimenti-dpr151`
  (DPR 151/2011), `carico-incendio-classe-resistenza-dm` (D.M. 9/3/2007) e `resistenza-fuoco-strutture-ntc`.
  Validazione Livello 2 con tecnico/professionista antincendio abilitato.
