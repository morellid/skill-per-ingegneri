# AGENTS.md - fattore-comportamento-q-sismica-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) par. 7.2.2 e
7.3.1**:

- la scelta del **comportamento strutturale** (dissipativo / non dissipativo), delle **classi di duttilità
  CD"A"/CD"B"** e della **progettazione in capacità** (§7.2.2);
- la determinazione del **fattore di comportamento q** allo SLV: **qlim = q0 · KR** [7.3.1], con q0 dalla Tab.
  7.3.II, KR = 1/0,8, riduzione kw, componente verticale q=1,5 (ponti 1) e non dissipativo [7.3.2] (§7.3.1).

**Non** calcola q né la domanda sismica, **non** definisce lo spettro di progetto (§3.2.3), **non** riproduce il
set completo delle Tab. 7.3.II per ogni materiale (§7.4-7.9), **non** sostituisce il progettista né la Circolare
21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **par. 7.2.2** (p. 210 GU) e **7.3.1** (p. 216-217 GU).
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-7-2-2-7-3-1.md`; parafrasi operativa in
  `references/estratti/fattore-comportamento-q-checklist.md`.
- Le formule **[7.3.1]**, **[7.3.2]** e la **Tab. 7.3.II** sono state verificate anche sull'**immagine**
  renderizzata delle pagine PDF 220-221 (`pdftoppm -r 150 -png`), perché `pdftotext` perde gli operatori ·, =,
  ≤, /.

## Costanti da non alterare (ancorate al testo)

- **Formula**: **qlim = q0 · KR** [7.3.1]; **KR = 1** (regolare in altezza) / **0,8** (non regolare).
- **Non dissipativo**: **1 ≤ qND = (2/3)·qCD"B" ≤ 1,5** [7.3.2].
- **Componente verticale**: **q = 1,5** (ponti **q = 1**).
- **kw**: 1,00 (telai/miste equivalenti a telai); (1+α0)/3 con **0,5 ≤ kw ≤ 1** (pareti).
- **Sovraresistenza globale γRd**: **almeno 1,25**.
- **q0 rappresentativi** (Tab. 7.3.II): c.a. a telaio CD"A" **4,5·αu/α1** / CD"B" **3,0·αu/α1**; acciaio
  intelaiate CD"A" **5,0·αu/α1** / CD"B" **4,0** (set completo §7.4-7.9).

Ogni numero e formula devono restare rintracciabili in `references/fonti/ntc2018-par-7-2-2-7-3-1.md`. Non
introdurre valori "a memoria".

## Task

- `tasks/inquadra-comportamento-strutturale.md` - comportamento dissipativo/non dissipativo, CD"A"/CD"B",
  progettazione in capacità (§7.2.2).
- `tasks/inquadra-fattore-comportamento-q.md` - fattore q allo SLV: qlim = q0·KR, q0, KR, αu/α1, kw, casi
  particolari (§7.3.1).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
