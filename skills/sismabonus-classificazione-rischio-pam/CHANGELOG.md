# CHANGELOG - sismabonus-classificazione-rischio-pam

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1-alpha] - 2026-05-10

### fix(source-grounding): remediation semantica (closes #110)

#### Fonti scaricate e lette

- **dm-65-2017-all-a** (DM MIT 7/3/2017 n. 65 Allegato A): PDF testuale scaricato,
  testo estratto integralmente via `pdftotext`, trascritto in
  `references/fonti/dm-65-2017-all-a.md`. SHA256 confermato:
  `8392e1dddd5ff99de3fab805e86414bd61ac8fc022a95ba2731c485a48fa5878`.
- **dm-58-2017** (DM MIT 28/2/2017 n. 58): PDF scaricato ma scansionato (non testuale),
  SHA256 calcolato: `4b03025c0c9c0a81860ad454e3448ec325569002e8b3332d3abf20ae78851267`.
  Il contenuto rilevante (Allegato A) e' sostituito integralmente dal DM 65/2017.
- **dm-24-2020** (DM MIT 9/1/2020 n. 24): PDF scaricato ma scansionato, SHA256 calcolato:
  `028d77270f06f7a6985b12bf0d42aae0558e9211508fb4c3083c10b2592517ff`.
- **ntc-2018**: pagina MIT risponde HTTP 404; sha256 impostato a null (fonte di contesto,
  non citata direttamente nei calcoli della skill).
- **circ-7-2019**: PDF non scaricato (supplemento GU di grandi dimensioni); sha256 a null
  (fonte di contesto, non citata direttamente nei calcoli della skill).

#### Verifiche semantiche effettuate

Tutti i valori seguenti sono stati verificati letteralmente contro il testo del PDF
`dm-65-2017-all-a` estratto via `pdftotext`:

1. **Tabella 3 - %CR per stato limite** (pag. 4 PDF): SLID=0%, SLO=7%, SLD=15%,
   SLV=50%, SLC=80%, SLR=100% - CONFERMATI. Coincidono con i valori in `sismabonus.py`.
2. **TR convenzionale SLID = 10 anni** (passo 4, pag. 4 PDF): CONFERMATO.
3. **TR convenzionale SLR = TR(SLC)** (passo 5, pag. 4 PDF): CONFERMATO.
4. **Formula PAM** (passo 7, pag. 4 PDF): formula trapezoidale con termine di coda
   lambda(SLC)*CR(SLR) - CONFERMATA.
5. **Capping SLD/SLO** (passo 3 + nota 6, pag. 3-4 PDF): obbligo di assumere
   TR_C(SLO/SLD) := min(TR_C(SLO/SLD), TR_C(SLV)) - CONFERMATO.
6. **Valore PAM 1,13%** per V_R=50 anni ai minimi NTC (nota a Tabella 1, pag. 2-3 PDF):
   CONFERMATO testualmente nel PDF.
7. **Tabella 1 classi PAM** (pag. 2-3 PDF): 8 classi A+..G con soglie 0.5/1.0/1.5/
   2.5/3.5/4.5/7.5% - CONFERMATA. Ambiguita' al bordo 7.5% documentata correttamente.
8. **Tabella 2 classi IS-V** (pag. 3 PDF): 7 classi A+..F con soglie 100/80/60/45/
   30/15% - CONFERMATA. Ambiguita' al bordo IS-V=100% documentata correttamente.
9. **Classe finale = peggiore tra PAM e IS-V** (passo 11, pag. 4 PDF): CONFERMATO.
10. **Salto classi - sezione 3.1** (pag. 8 PDF): valutazione pre/post intervento con
    stesso metodo - CONFERMATO.

#### Nessuna modifica al codice Python

Tutti i valori costanti verificati contro il PDF corrispondono esattamente a quanto
implementato in `sismabonus.py`. I test (55/55 OK) non sono stati modificati.
Aggiunti commenti di tracciabilita' nel codice con riferimento alla pagina/tabella del PDF.

#### Estratti aggiornati

Tutti i 5 estratti in `references/estratti/` aggiornati con:
- Header fonte aggiornato con SHA256 e riferimento a `references/fonti/dm-65-2017-all-a.md`
- Sezione "Verifiche semantiche effettuate vs PDF" con stato CONFERMATO per ogni affermazione
- Riferimenti puntuali aggiornati con numero di pagina del PDF

## [0.1.0-alpha] - 2026-05-07

### Added
- Prima versione alpha della skill (issue #12 del repo).
- Modulo di calcolo Python `tasks/lib/sismabonus.py` con:
  - costruzione Curva di Individuazione (5 punti SLID/SLO/SLD/SLV/SLC + termine SLR)
  - **capping prescritto dall'Allegato A passo 2.1.3** applicato di default: TR_C(SLO/SLD) := min(TR_C(SLO/SLD), TR_C(SLV)). Disattivabile via flag CLI `--no-capping` per validazione vs software che applicano il capping a monte.
  - calcolo PAM con formula trapezoidale a 4 termini + coda lambda(SLC)*CR(SLR), DM 58/2017 Allegato A punto 2.1
  - calcolo IS-V = PGA_C(SLV)/PGA_D(SLV), Allegato A punto 2.1 passo 9
  - attribuzione classe PAM (8 classi A+..G) e IS-V (7 classi A+..F) **coerenti col testo letterale dell'Allegato A** (Tab. 1 e Tab. 2 rispettivamente; per l'IS-V: lower bound incluso, upper bound escluso per A..E; bordo IS-V=100% formalmente non coperto -> interpretazione conservativa = A)
  - regola classe finale = peggiore tra le due
  - calcolo salto classi tra fatto e progetto
  - **gestione strict di PGA_D in `progetto`**: o tutte e 4 le chiavi PGA_D_*, o nessuna (eredita da `fatto`); chiavi parziali -> errore esplicito (no fallback silenzioso su typo)
  - segnalazione `monotona: false` su curve non monotone residue dopo il capping
  - tracciabilita' del capping nel campo `CappingApplicato` dell'output (TR_C originali e capped + flag SLO_modificato/SLD_modificato)
  - validazione input hardening (NaN/inf/string/bool/negativi) + RFC 8259 su JSON
  - CLI `--input-json` con error handling friendly
- Test suite `tasks/lib/test_sismabonus.py`: **55 test** su consistenza interna + verifica numerica vs valore di riferimento del decreto:
  - **`test_pam_riferimento_decreto_VR_50`**: produce PAM = 1.13% per il caso V_R=50 ai minimi NTC, esattamente come dichiarato dall'Allegato A nota a Tab. 1. Calcolato a mano:
    ```
    SLID->SLO: |1/30 - 1/10| * (0 + 0.07)/2     = 0.00233
    SLO->SLD:  |1/50 - 1/30| * (0.07 + 0.15)/2  = 0.00147
    SLD->SLV:  |1/475 - 1/50| * (0.15 + 0.50)/2 = 0.00582
    SLV->SLC:  |1/975 - 1/475| * (0.50 + 0.80)/2 = 0.00070
    coda SLR:  1/975 * 1.0                       = 0.00103
    PAM totale                                    = 0.01134 = 1.13% ✓
    ```
  - test su capping passo 2.1.3 (default attivo, --no-capping disattivante, no-op su input gia' monotono)
  - test sui bordi delle tabelle classi PAM e IS-V coerenti col testo letterale del decreto
  - test su PGA_D progetto strict (parziale -> errore; assente -> eredita; tutte e 4 -> override)
  - test CLI con `tempfile.TemporaryDirectory` (fs read-only safe)
- Task files: `calcola-classificazione.md`, `valida-input.md`, `run-test-suite.md`.
- Estratti normativi in `references/estratti/`: art. 3 DM 58, Allegato A punto 2.1 (PAM con capping passo 3), 2.1 passo 9 (IS-V), tabelle classi (con caveat sui bordi ambigui), salto classi.
- Fonti catalogate in `references/sources.yaml` con SHA256 reali per i PDF effettivamente fetched (DM 65/2017 Allegato A, DM 329/2020, esempio ClaSS 2017).
- Esempi: `caso-conforme-fittizio` (smoke test, salto classi B->A) e `caso-non-monotono` (caso patologico dove il capping del decreto non risolve, warning richiesto).
- AGENTS.md con convenzioni di dominio.

### Changed
- **DM 329/2020**: corretta la citazione in tutti i documenti. Il DM 329/2020 modifica art. 3 del DM 58/2017 (commi 4-bis, 4-ter, 4-quater su super-sismabonus 110%) e SOSTITUISCE l'Allegato B (modello di asseverazione). NON modifica l'Allegato A. La precedente versione della documentazione lo citava erroneamente come "aggiornamento Allegato A".
- **Boundary IS-V** allineato al testo letterale dell'Allegato A Tab. 2 (DM 65/2017): A: `80% <= IS-V < 100%` (era `80% <= IS-V <= 100%`); per IS-V = 100% esatto si applica l'interpretazione conservativa `-> A` come nei software certificati ClaSS 2017 e MasterSap-SismiClass.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2). Test interni: 55/55 OK.
- Modifiche introdotte da review adversariale Codex pre-merge (PR #84): correzione boundary IS-V vs testo letterale, implementazione capping prescritto, citazione corretta DM 329/2020, gestione strict PGA_D, test riferimento decreto 1.13%, tempfile per filesystem read-only.
- **Validazione di campo (Livello 2)** richiesta prima del release stabile: confronto numerico vs software certificati (ClaSS S.I.S., CDM Win STS, EdiSis Newsoft, MasterSap-SismiClass AMV) su almeno 10 edifici reali. Piano dettagliato in `tasks/run-test-suite.md`.
- Metodo SEMPLIFICATO per edifici in muratura (Allegato A punto 2.2, tabella tipologie x numero piani) **fuori scope** della v0.1.0-alpha. Pianificato per v0.2.0.
- Generazione Allegato B / B-bis (asseverazione tecnica) **fuori scope** della skill: la skill produce numeri, l'asseverazione formale e' a cura del professionista firmatario.
- Aliquote di detrazione fiscale sismabonus (50/70/75/80/85/super-110%) **fuori scope** della skill: dipendono da legge finanziaria vigente, demandate al commercialista.

### Hash sorgenti
SHA256 calcolati al primo fetch (2026-05-07) per i PDF accessibili:
- DM 65/2017 Allegato A: `8392e1dddd5ff99de3fab805e86414bd61ac8fc022a95ba2731c485a48fa5878`
- DM 329/2020: `9031321161c6d7e3eaa71228a9f9c333f2f1f08d209ad7d6bb73fcd0438837a5`
- ClaSS 2017 esempio: `5a9ceccf7fd37529da7a3e894fde31cc52720ceadea833484b19378cefe3f985`

Altre fonti (DM 58/2017 originale, DM 24/2020, NTC 2018, Circ. 7/2019) non scaricate
nella v0.1.0-alpha; non bloccanti per la procedura di calcolo della skill (il testo
vigente di riferimento e' DM 65/2017 Allegato A, gia' verificato). SHA256 per DM 58/2017
originale e DM 24/2020 calcolati nella v0.1.1-alpha (documenti scansionati, non testuali).
