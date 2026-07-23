# AGENTS.md - requisiti-acustici-passivi-edifici-dpcm

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo il **DPCM 5 dicembre 1997** (Determinazione dei
requisiti acustici passivi degli edifici, attuazione L. 447/1995):

- la **classificazione** dell'ambiente abitativo in categorie (Tab. A);
- le **grandezze e gli indici** di valutazione (Allegato A: R'w, D2m,nT,w, L'n,w, LASmax, LAeq);
- i **valori limite** per categoria (Tab. B) e i limiti del **rumore degli impianti** tecnologici.

**Non** esegue misure/calcoli acustici né il collaudo in opera, **non** riproduce le norme UNI/ISO citate, **non**
sostituisce il **tecnico competente in acustica** (L. 447/1995).

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Serie Generale n. 297 del 22/12/1997, in cui è
  pubblicato il **DPCM 5 dicembre 1997** (pagine 4-7 della G.U.).
- `not_in_repo/dpcm-5-12-1997-gu297.pdf`, SHA256
  `5a8ae1f4cadb54d2b630ee3001b83f1ab736008d06dacf78226d001a15ed1f51`, **riproducibile via doppio download** dallo
  stesso URL eli (`https://www.gazzettaufficiale.it/eli/gu/1997/12/22/297/sg/pdf`); hash verificabile dalla CI.
- Testo trascritto verbatim in `references/fonti/dpcm-5-12-1997.md`; parafrasi operativa in
  `references/estratti/requisiti-acustici-passivi-checklist.md`.
- **Modalità di lettura**: il PDF è una scansione GURITEL (immagine) in cui `pdftotext` non estrae testo; articoli,
  Allegato A, Tab. A e Tab. B sono stati letti **renderizzando le pagine in immagine** (`pdftoppm -r 150/160 -png`)
  e trascritti verbatim. Ogni futura modifica ai valori deve ripartire dalla stessa lettura per immagine.

## Costanti da non alterare (ancorate al testo/immagine)

- **Tab. A** categorie: A residenza; B uffici; C alberghi/pensioni; D ospedali/cliniche/case di cura; E
  scolastiche; F ricreative/culto; G commerciali.
- **Tab. B** (R'w / D2m,nT,w / L'n,w / LASmax / LAeq): **D** 55/45/58/35/25; **A,C** 50/40/63/35/35; **E**
  50/48/58/35/25; **B,F,G** 50/42/55/35/35. R'w e D2m,nT,w = valori **minimi**; L'n,w/LASmax/LAeq = valori
  **massimi**. R'w tra due distinte unità immobiliari.
- **Allegato A**: D2m,nT = D2m + 10 log(T/T0), **T0 = 0,5 s**; impianti **35 dB(A) LASmax** (discontinuo) / **25
  dB(A) LAeq** (continuo); indici da UNI 8270:1987 Parte 7 (§5.1 R'w e D2m,nT,w; §5.2 L'n,w).

Ogni numero e tabella devono restare rintracciabili in `references/fonti/dpcm-5-12-1997.md`. Non introdurre valori
"a memoria".

## Task

- `tasks/classifica-ambiente-e-valori-limite.md` - categoria (Tab. A) e valori limite (Tab. B).
- `tasks/inquadra-grandezze-e-rumore-impianti.md` - grandezze/indici (Allegato A) e limiti impianti tecnologici.

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Il DPCM 5/12/1997 è vigente; per applicazioni edilizie recenti si vedano anche la UNI 11367 (classificazione
  acustica, fuori scope) e le norme UNI EN ISO 717 (indici), non riprodotte qui.
