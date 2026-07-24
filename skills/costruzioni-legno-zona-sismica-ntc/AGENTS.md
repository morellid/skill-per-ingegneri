# AGENTS.md - costruzioni-legno-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle regole generali** delle
costruzioni di legno in zona sismica secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.7**: aspetti
concettuali/CD (§7.7.1), materiali e proprietà delle zone dissipative e pannelli di rivestimento (§7.7.2),
tipologie e fattori di comportamento q0 (§7.7.3), precisazioni sulla duttilità (§7.7.3.1), disposizioni
costruttive, verifiche e dettagli (§§7.7.4-7.7.7). Target: ingegneri strutturisti e progettisti di edifici in
legno (telaio leggero/platform frame, XLAM/CLT) in zona sismica.

**È una skill documentale per il tecnico**: fornisce comportamento, materiali, fattori q0 e requisiti di
duttilità; **non** esegue le verifiche (resistenza/duttilità di elementi e collegamenti) né progetta i
collegamenti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre le **regole generali per il legno in zona sismica** (§7.7). È **distinta**
da `costruzioni-legno-ntc` (§4.4, materiali/resistenze/collegamenti/verifiche **statiche**) e da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q): il §7.7 aggiunge i
requisiti sismici specifici del legno (zone dissipative nei collegamenti, CD"A"/CD"B", q0, precisazioni sulla
duttilità dei mezzi di unione). Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla
G.U. n. 42/2018). Restano fuori scope: le verifiche di resistenza/duttilità, il q0 numerico per tipologia
(Tab. 7.3.II), il dettaglio completo dei collegamenti (§7.7.7).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-7**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.7 (pagine PDF 258-260) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r 150`)
  per spessori dei pannelli, rapporti di duttilità, mezzi di unione e coefficienti.

Trascrizione in `references/fonti/ntc2018-par-7-7.md`; estratto operativo in
`references/estratti/legno-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.7.1**: dissipativo → **CD"A"/CD"B"**; zone dissipative nei **collegamenti**, membrature **elastiche**;
  sovraresistenza **ηRd** (Tab. 7.2.I), comunque **≥ 1,3 (A)** / **≥ 1,1 (B)**.
- **§7.7.2**: rinvio §4.4; **unioni incollate non dissipative**; pannelli **13/9/12/15 mm** (particelle/
  compensato/OSB coppia/OSB singolo); connettori §11.7.8.
- **§7.7.3 / §7.7.3.1**: **q0 Tab. 7.3.II** (giustificato dal Progettista); duttilità **≥ 4 (B)** / **≥ 6 (A)**,
  ≥ 3 cicli, ≤ 20% riduzione; **d ≤ 12 mm & ≥ 10d**; **chiodi d ≤ 3,1 mm & rivestimento ≥ 4d**; alt. **8d/3d** → B.
- **§§7.7.5-7.7.7**: vincoli impalcato-pareti **bilateri**; **giunti di carpenteria coeff. 1,3**; RES §7.3.6.1 con
  **resistenza -20%**; **d > 16 mm** esclusi nei collegamenti legno-legno/legno-acciaio.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche di resistenza/duttilità di elementi e collegamenti né calcolare il q0 numerico
  (Tab. 7.3.II).
- Non **progettare** i collegamenti né i dettagli (§7.7.7); non trattare i requisiti statici (§4.4, → skill
  dedicata) né il framework del fattore q (§7.3.1, → skill dedicata).

### Cosa fare
- Fornire aspetti concettuali/CD, materiali/pannelli, fattori q0 e requisiti di duttilità dei mezzi di unione,
  sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.7. Verificare sull'immagine i valori (pannelli 13/9/12/15 mm; duttilità 4/6; d 12/3,1/16 mm;
10d/4d/8d/3d; sovraresistenza 1,3/1,1; coeff. 1,3; riduzione 20%).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di strutture di legno).

## Stato attuale

- Versione: 0.1.0-alpha (closes #456)
- Task files: 2 (`inquadra-comportamento-materiali-fattore-q.md`, `verifica-requisiti-duttilita-dettagli.md`)
- Esempi: 2 (requisiti dei materiali/pannelli e comportamento dissipativo per una parete a telaio; requisiti di
  duttilità dei mezzi di unione di un collegamento legno-acciaio)
