# AGENTS.md - verifiche-geotecniche-slu-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) par. 6.2.4** (con
il valore caratteristico del §6.2.2), il **framework semiprobabilistico delle verifiche geotecniche agli SLU**:

- stati limite **EQU / STR / GEO** (§6.2.4.1);
- **approcci progettuali** 1 e 2 e **coefficienti parziali** su azioni (A1/A2, Tab. 6.2.I), parametri geotecnici
  (M1/M2, Tab. 6.2.II) e resistenze (R1/R2/R3);
- **valore caratteristico** dei parametri (§6.2.2).

**Non** esegue le verifiche, **non** riproduce i coefficienti **γR** specifici di ciascuna opera (§6.3-6.11, che
stanno nelle skill d'opera), **non** tratta in dettaglio le SLE (§6.2.4.2), **non** sostituisce il progettista né
la Circolare 21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **par. 6.2.2 e 6.2.4** (p. 185-186 GU).
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-6-2-4.md`; parafrasi operativa in
  `references/estratti/verifiche-geotecniche-slu-checklist.md`.
- Le **Tab. 6.2.I e 6.2.II** sono state verificate anche sull'**immagine** renderizzata della pagina PDF 190
  (`pdftoppm -r 150 -png`), perché `pdftotext` altera pedici, operatori e la notazione delle combinazioni.

## Costanti da non alterare (ancorate al testo)

- **SLU**: EQU → **Einst,d ≤ Estb,d** (colonna EQU Tab. 6.2.I); STR/GEO → **Ed ≤ Rd** [6.2.1].
- **Approcci**: Approccio 1 (due combinazioni), Approccio 2 (una); default SLU non trattati §6.3-6.11: **Approccio 1
  con (A1+M1+R1) e (A2+M2+R2)**; **R1 sempre unitari**, **R2 ≥ 1**.
- **Tab. 6.2.I** (azioni, EQU/A1/A2): G1 fav 0,9/1,0/1,0, sfav **1,1/1,3/1,0**; G2 fav 0,8/0,8/0,8, sfav
  **1,5/1,5/1,3**; Q fav 0,0, sfav **1,5/1,5/1,3**.
- **Tab. 6.2.II** (parametri, M1/M2): tan φ'k **1,0/1,25**; c'k **1,0/1,25**; cuk **1,0/1,4**; γ **1,0/1,0**.
- **Rd** analitico da **Xk/γM** (Tab. 6.2.II) con i **γR** per opera; **valore caratteristico** = stima ragionata e
  cautelativa per ogni SL.

Ogni numero e le tabelle devono restare rintracciabili in `references/fonti/ntc2018-par-6-2-4.md`. Non introdurre
valori "a memoria".

## Task

- `tasks/inquadra-approcci-progettuali-slu.md` - SLU EQU/STR/GEO, approcci 1/2, default (A1+M1+R1)+(A2+M2+R2),
  coefficienti azioni Tab. 6.2.I (§6.2.4.1).
- `tasks/inquadra-coefficienti-parametri-geotecnici.md` - coefficienti M1/M2 (Tab. 6.2.II), Rd e valore
  caratteristico (§6.2.4.1.2, 6.2.2).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
