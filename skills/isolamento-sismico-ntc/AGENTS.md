# AGENTS.md - isolamento-sismico-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) par. 7.10**, il
progetto di **costruzioni con isolamento e/o dissipazione sismica** (edifici e ponti a isolamento alla base):

- scopo, strategie e requisiti (§7.10.1-7.10.3);
- indicazioni progettuali e dispositivi (§7.10.4);
- modellazione, analisi e verifiche SLE/SLV/SLC (§7.10.5-7.10.6); manutenzione/collaudo (§7.10.7-7.10.8).

**Non** esegue l'analisi né le verifiche, **non** progetta né qualifica i dispositivi (§11.9), **non** riproduce le
formule di dettaglio [7.10.1]-[7.10.5], **non** sostituisce il progettista né la Circolare 21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **par. 7.10** (p. 273-278 GU).
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-7-10.md`; parafrasi operativa in
  `references/estratti/isolamento-sismico-checklist.md`.
- Le **soglie numeriche e le formule** sono state verificate anche sull'**immagine** delle pagine PDF 279 e 281
  (`pdftoppm -r 150 -png`), perché `pdftotext` altera operatori, pedici e radici.

## Costanti da non alterare (ancorate al testo/immagine)

- **Requisiti**: sovra/sottostruttura in campo elastico (particolari come per **agS ≤ 0,075g**); dispositivi
  conformi al **§11.9**; **V ≥ 0** (se V<0 trazione **< min(2G, 1 MPa)**); diaframma rigido sopra/sotto; elementi
  verticali **< 1/20** dello spostamento relativo.
- **Modellazione**: deformabilità verticale se **KV/Kesi < 800**; iterazione **< 5%**; valori medi se estremi entro
  **20%**; velocità **±30%**; modello lineare equivalente se rigidezza **≥ 50%** (secante al **20%**), smorzamento
  **< 30%**, variazione forza-spostamento **< 10%**, incremento forza **≥ 2,5%** del peso.
- **Analisi**: **no push-over**; statica lineare se **Tis ∈ [3·Tbf, 3,0 s]**, **KV ≥ 800·Kesi**, **TV = 2π√(M/KV) <
  0,1 s**, edifici **≤ 20 m e ≤ 5 piani**, sottostruttura **T ≤ 0,05 s**, pianta **< 50 m**, eccentricità **≤ 3%**;
  dinamica lineare con spettro ridotto per **T ≥ 0,8·Tis**.
- **Verifiche**: SLD sovrastruttura interpiano **< 2/3** dei limiti §7.3.6.1; SLV **q ≤ 1,50 (edifici)** / **q = 1
  (ponti)**, sottostruttura rigida se **T < 0,05 s** (M × agS), coeff. sicurezza **≥ 1,5**; SLC spostamenti **d2**
  (+ maggiore tra residuo SLD e **50%** per non lineari).

Ogni numero e soglia devono restare rintracciabili in `references/fonti/ntc2018-par-7-10.md`. Non introdurre valori
"a memoria".

## Task

- `tasks/inquadra-scopo-requisiti-dispositivi.md` - scopo/strategie, requisiti, dispositivi (§7.10.1-7.10.4).
- `tasks/inquadra-modellazione-analisi-verifiche.md` - modellazione, analisi, verifiche SLE/SLV/SLC (§7.10.5-7.10.8).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
