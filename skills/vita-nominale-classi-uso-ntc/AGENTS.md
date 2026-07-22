# AGENTS.md - vita-nominale-classi-uso-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) par. 2.4**, la
scelta dei tre parametri di base di ogni progetto strutturale:

- **vita nominale di progetto V_N** (§2.4.1, Tab. 2.4.I);
- **classe d'uso** (§2.4.2);
- **periodo di riferimento per l'azione sismica V_R = V_N · C_U** (§2.4.3, formula [2.4.1], Tab. 2.4.II).

**Non** definisce lo spettro di risposta, **non** calcola i periodi di ritorno T_R o le probabilità di superamento
degli stati limite (§3.2), **non** tratta le opere esistenti né le combinazioni delle azioni (§2.5), **non**
sostituisce il progettista né la Circolare 21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **par. 2.4.1-2.4.3**, p. 36-37.
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-2-4.md`; parafrasi operativa in
  `references/estratti/vita-nominale-classi-uso-checklist.md`.
- La formula **[2.4.1]** e le tabelle **2.4.I/2.4.II** sono state verificate anche sull'**immagine** renderizzata
  della pagina PDF 41 (`pdftoppm -r 150 -png`), perché `pdftotext` perde l'operatore di moltiplicazione.

## Costanti da non alterare (ancorate al testo)

- **V_N minimi** (Tab. 2.4.I): temporanee/provvisorie **10**, prestazioni ordinarie **50**, prestazioni elevate
  **100** anni; fase di costruzione V_N **≥ P_N** e **≥ 5 anni**; esonero verifiche sismiche se condizione **< 2
  anni**.
- **C_U** (Tab. 2.4.II): classe I/II/III/IV = **0,7 / 1,0 / 1,5 / 2,0**; **> 2** per rischio di incidente
  rilevante.
- **Formula**: **V_R = V_N · C_U** [2.4.1].

Ogni numero e la formula devono restare rintracciabili in `references/fonti/ntc2018-par-2-4.md`. Non introdurre
valori "a memoria".

## Task

- `tasks/inquadra-vita-nominale-classe-uso.md` - fissa V_N (Tab. 2.4.I) e la classe d'uso I-IV (§2.4.1, §2.4.2).
- `tasks/inquadra-periodo-riferimento-vr.md` - ricava V_R = V_N · C_U con C_U (Tab. 2.4.II) e rinvia al §3.2
  (§2.4.3).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
