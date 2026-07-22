# AGENTS.md - categorie-sottosuolo-topografiche-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) par. 3.2.2**, la
**classificazione sismica del sito**:

- **categoria di sottosuolo** A-E (approccio semplificato su Vs,eq, Tab. 3.2.II);
- **categoria topografica** T1-T4 (Tab. 3.2.III).

**Non** calcola lo spettro né i coefficienti di amplificazione stratigrafica SS/CC e topografica ST (§3.2.3.2),
**non** esegue analisi di risposta sismica locale (§7.11.3), **non** determina i valori di VS o la stratigrafia
(§6.2.2), **non** sostituisce il geologo/geotecnico/progettista né la Circolare 21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **par. 3.2.2** (p. 46-47 GU).
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-3-2-2.md`; parafrasi operativa in
  `references/estratti/categorie-sottosuolo-topografiche-checklist.md`.
- La formula **[3.2.1]** e le **Tab. 3.2.II/3.2.III** sono state verificate anche sull'**immagine** renderizzata
  delle pagine PDF 50-51 (`pdftoppm -r 150 -png`), perché `pdftotext` perde la frazione, la sommatoria e gli
  operatori ≤, >.

## Costanti da non alterare (ancorate al testo)

- **Formula**: **Vs,eq = H / Σ(hi/Vs,i)** [3.2.1]; substrato con **VS ≥ 800 m/s**; per **H > 30 m** si usa
  **VS,30** (H = 30 m).
- **Categorie di sottosuolo** (Tab. 3.2.II): **A** VS > 800 (copertura scadente ≤ 3 m); **B** 360-800; **C**
  180-360 (substrato > 30 m); **D** 100-180 (substrato > 30 m); **E** C/D con substrato ≤ 30 m.
- **Categorie topografiche** (Tab. 3.2.III): **T1** i ≤ 15°; **T2** i > 15°; **T3** 15° ≤ i ≤ 30° (cresta
  stretta); **T4** i > 30° (cresta stretta); da considerare se **altezza > 30 m**.
- **Piani di riferimento**: fond. superficiali → piano di imposta; pali → testa pali; opere di sostegno di terreni
  naturali → testa opera; muri di terrapieni → piano di imposta fondazione.

Ogni numero e la formula devono restare rintracciabili in `references/fonti/ntc2018-par-3-2-2.md`. Non introdurre
valori "a memoria".

## Task

- `tasks/classifica-categoria-sottosuolo.md` - categoria A-E via Vs,eq (Tab. 3.2.II), substrato, regola dei 30 m,
  piani di riferimento (§3.2.2).
- `tasks/classifica-categoria-topografica.md` - categoria T1-T4 (Tab. 3.2.III) per altezze > 30 m (§3.2.2).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
