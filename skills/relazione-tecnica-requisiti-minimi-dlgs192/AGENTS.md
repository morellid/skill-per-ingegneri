# AGENTS.md - relazione-tecnica-requisiti-minimi-dlgs192

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (progettista, direttore dei lavori) per la **relazione tecnica
di progetto attestante la rispondenza ai requisiti minimi di contenimento dei consumi energetici**
(la "relazione ex legge 10"): contenuto, deposito, sistemi alternativi, asseverazione a fine lavori,
controlli e sanzioni, ai sensi del **D.Lgs. 19 agosto 2005, n. 192, art. 8** (con l'art. 15 cc. 1,
3, 4). Target: ingegneri e architetti come progettisti o direttori dei lavori.

**E' una skill documentale per il tecnico**: inquadra l'adempimento e la sua collocazione; **non
redige** la relazione, **non esegue** i calcoli/verifiche, non sostituisce il progettista/DL.

## Nota sull'area e sulla complementarita'

Area **energia-incentivi**. Distinta da `attestato-prestazione-energetica-dlgs192` (APE, art. 6) e
complementare a `trasmittanza-termica-opache-dm2015` (verifiche numeriche del DM 26/6/2015). Questa
copre l'**adempimento della relazione tecnica** (art. 8).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-192-2005-art8-15**: D.Lgs. 192/2005, pagina indice Normattiva pinnata a `!vig=2026-07-17`
  (hash `bfaa5336...`; codice 005G0219 - stesso indice della skill APE, ripinnato a oggi). Art. 8
  (versione 5, idGruppo 1) e art. 15 (versione 4, idGruppo 3) caricati via `caricaArticolo` (formato
  AKN) e trascritti verbatim (dell'art. 15: cc. 1, 3, 4).
- **dlgs-5-2026-allegato-iii**: D.Lgs. 9 gennaio 2026, n. 5 (RED III), PDF del fascicolo integrale
  della **GU Serie generale n. 15 del 20 gennaio 2026** (hash `3d13cb9a...`; codice 26G00018).
  Trascritti verbatim l'art. 29 (pagg. GU 21-22), l'incipit dell'art. 30 (pag. GU 22) e il testo
  risultante dell'Allegato III del D.Lgs. 199/2021 dalle "Note all'art. 29" (pagg. GU 54-55).
  **Estrazione**: `pdftotext` **senza** `-layout` per il corpo (due colonne); `-layout` solo per le
  pagine "Note" a colonna singola. La forma di URL `/eli/id/.../sg/pdf` a livello di singolo atto
  risponde 404: usare `/eli/gu/YYYY/MM/DD/<numero>/sg/pdf`.
- **dlgs-5-2026-entrata-in-vigore**: scheda Normattiva del D.Lgs. 5/2026 pinnata `!vig=2026-08-09`
  (hash `1a675001...`). Serve a **una sola informazione**: "Entrata in vigore del provvedimento:
  04/02/2026". Il PDF di Gazzetta prova che il decreto non ha un articolo di entrata in vigore ma
  **non contiene la data**: senza questa fonte, la data sarebbe un'affermazione normativa priva di
  ancoraggio.

Trascrizioni in `references/fonti/dlgs-192-2005-art8-15.md`,
`references/fonti/dlgs-5-2026-allegato-iii.md` e
`references/fonti/dlgs-5-2026-entrata-in-vigore.md`; estratti operativi in
`references/estratti/relazione-tecnica-checklist.md` e
`references/estratti/obblighi-fer-allegato-iii.md`.

## Punti chiave (verificati sul testo)

- **Relazione** redatta dai **progettisti** (calcoli e verifiche), depositata dal **proprietario in
  doppia copia** con la DIA/titolo abilitativo (art. 8 c. 1); **esclusioni**: pompa di calore <= 15
  kW, sostituzione generatore sotto soglia DM 37/2008.
- **Sistemi alternativi** ad alta efficienza: valutazione di fattibilita' documentata per nuove
  costruzioni e ristrutturazioni importanti (c. 1-bis). **Attenzione**: e' un adempimento **diverso**
  dagli obblighi FER quantitativi dell'Allegato III, e non li assolve.
- **Obblighi FER** (Allegato III D.Lgs. 199/2021 come modificato dall'art. 29 del D.Lgs. 5/2026):
  quote 60%+60% (nuova costruzione), 40%+40% (ristrutturazione importante di primo livello), 15%
  (secondo livello), 15% (ristrutturazione dell'impianto termico); +5 punti e +10% sulla potenza per
  edifici pubblici; divieto di effetto Joule salvo classe B o superiore; k = 0,025 (esistenti) /
  0,05 (nuovi) per la potenza elettrica; esonero per teleriscaldamento efficiente a copertura
  integrale; deroga da motivare **nella relazione** con obbligo compensativo su EP H,C,W,nren
  limitato a nuovi e primo livello; copia della relazione al GSE e verifica dei Comuni.
- **Asseverazione + AQE** del **direttore dei lavori** a fine lavori, pena l'inefficacia della fine
  lavori (c. 2); **controlli** del Comune in corso d'opera o entro 5 anni (cc. 3-5).
- **Sanzioni**: dichiarazione sostitutiva di atto notorio (art. 15 c. 1); professionista 700-4200
  euro per relazione non conforme (c. 3); direttore dei lavori 1000-6000 euro per omessa
  asseverazione (c. 4).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la relazione tecnica ne' l'asseverazione/AQE.
- Non **eseguire** i calcoli/verifiche energetiche (DM 26/6/2015) ne' riprodurre gli **schemi** di
  relazione del decreto MiSE.
- Non trattare l'**APE** (art. 6), l'**esercizio impianti** (art. 7) ne' i commi 2 e 5-10 dell'art.
  15: rinvio.
- Non **qualificare** l'intervento come ristrutturazione importante di primo/secondo livello o come
  ristrutturazione dell'impianto termico: e' un input, definito dal DM 26/6/2015 come modificato dal
  DM MASE 28/10/2025 (rinvio).
- Non **ricostruire a memoria** la formula della potenza elettrica FER (Sezione B punto 3): e'
  pubblicata come immagine nel PDF e non e' estraibile come testo. Riportare i soli parametri
  descritti a parole (k, S) e rinviare all'originale.
- Non **affermare come certa** la decorrenza del 3 agosto 2026: la formula "decorsi centottanta
  giorni dall'entrata in vigore del presente decreto" e' inserita nell'Allegato III del D.Lgs.
  199/2021 ed e' testualmente ambigua. Segnalare l'incertezza.
- Non **derivare per ragionamento** la data di entrata in vigore del D.Lgs. 5/2026 dalla vacatio
  ordinaria di 15 giorni: e' un'affermazione normativa e la regola non sta nel decreto. Citare la
  scheda Normattiva registrata come fonte `dlgs-5-2026-entrata-in-vigore` (4 febbraio 2026); il
  passaggio ai 180 giorni e' invece aritmetica di calendario.
- Non descrivere l'art. 29 come una **riscrittura integrale** dell'Allegato III: e' una novella con
  sostituzioni puntuali. Sono integralmente sostituiti il punto 1 della Sezione A e il punto 1 della
  Sezione B; delle Sezioni C ed E e' sostituita la sola rubrica.

### Cosa fare
- Stabilire se la relazione e' dovuta (esclusioni), chi la redige, cosa contiene (incl. sistemi
  alternativi e obblighi FER), come/quando si deposita; inquadrare asseverazione a fine lavori,
  controlli e sanzioni, sui commi degli artt. 8 e 15.
- Per gli obblighi FER partire sempre dalla **categoria di intervento** e dalla **data di
  presentazione del titolo edilizio**: sono i due discriminanti dell'Allegato III, Sezione A.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 192/2005 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli artt. 8 e 15, verificando le modifiche segnalate dai doppi tondi `(( ))` (es. D.Lgs.
48/2020) e l'evoluzione del decreto attuativo MiSE sugli schemi di relazione.

Allegato III: la Sezione B punto 6 ne prevede la **rideterminazione almeno quinquennale** a decorrere
dal 1° gennaio 2026, e la Sezione C punto 4 prevede **linee guida CTI** con esempi e calcoli
numerici. Verificarne l'emanazione e riscaricare il testo consolidato del D.Lgs. 199/2021 prima di
aggiornare le percentuali.

## Validatori

- Non ancora assegnato (Livello 2 con termotecnico / certificatore energetico).

## Stato attuale

- Versione: 0.2.0-alpha (closes #488; iniziale #346)
- Task files: 3 (`inquadra-relazione-deposito.md`, `inquadra-asseverazione-sanzioni.md`,
  `verifica-obblighi-fer-edifici.md`)
- Esempi: 3 (relazione per nuova costruzione con sistemi alternativi ed esclusione PdC 12 kW; fine
  lavori senza asseverazione: inefficacia, sanzione al DL, controlli del Comune; sostituzione del
  generatore che fa scattare l'obbligo FER del 15%)
