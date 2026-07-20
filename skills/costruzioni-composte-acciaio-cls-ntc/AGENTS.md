# AGENTS.md - costruzioni-composte-acciaio-cls-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione delle
costruzioni composte di acciaio-calcestruzzo** (travi con soletta collaborante, colonne composte; caso
**non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.3**: materiali e coefficienti
parziali, classificazione delle sezioni, resistenza delle sezioni composte, sistema di connessione a taglio
e colonne composte. Target: ingegneri strutturisti e progettisti.

**E' una skill documentale per il tecnico**: fornisce i coefficienti γC/γA/γS/γV, i criteri di
classificazione, i metodi di calcolo del momento resistente e le formule dei connettori (PRd,a, PRd,c);
**non calcola** le resistenze, **non esegue** le verifiche e **non dimensiona** la sezione né la connessione.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Completa** la famiglia "costruzioni di X" delle skill NTC insieme a
`costruzioni-calcestruzzo-ntc` (§4.1), `costruzioni-acciaio-ntc` (§4.2), `costruzioni-legno-ntc` (§4.4) e
`costruzioni-muratura-ntc` (§4.5). Il §4.3 rinvia esplicitamente ai §4.1 e §4.2 per quanto non specificato;
questa skill copre gli aspetti **propri del comportamento composto** (connessione, sezioni miste, colonne
composte). La progettazione **sismica** delle composte (§7.6) e i materiali (§11.2/11.3) restano fuori
scope. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-4-3**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 4.3 estratto con `pdftotext -layout` (pp. 114-127) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-4-3.md`; estratto operativo in
`references/estratti/costruzioni-composte-checklist.md`.

## Punti chiave (verificati sul testo)

- **Coefficienti** (§4.3.3): fd = fk/γM; SLU γC = 1,5, γA = 1,05, γS = 1,15, γV = 1,25; SLE/eccezionali
  γM = 1. Classe cls C20/25-C60/75.
- **Sezioni** (§4.3.2.1): classificate come per l'acciaio (§4.2.3); classi 1-2 plastiche/elastiche, 3-4
  elastiche; armatura B450C in classe 1-2 [4.3.1].
- **Flessione** (§4.3.4.2): elastico (fcd/fyd/fsd), plastico (cls 0,85·fcd), elasto-plastico; taglio
  verticale alla trave metallica.
- **Connessione** (§4.3.4.3): K = N/Nf; pioli PRd = min(0,8·ftk·(π·d²/4)/γV; 0,29·α·d²·√(fck·Ecm)/γV);
  ftk ≤ 500 MPa, d 16-25 mm, α = 0,2·(hsc/d+1) o 1,0; riduzioni lamiera grecata kl/kt.
- **Colonne composte** (§4.3.5): rivestite/riempite.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le resistenze né **eseguire** le verifiche; non **dimensionare** la sezione né la
  connessione.
- Non **riprodurre** le **Fig. 4.3.3/4.3.4** né la **Tab. 4.3.II** (figure/tabella figurata → norma/EC4) né
  i materiali dei **§11.2/11.3** né gli **Eurocodici** (UNI EN 1994).
- Non **trattare** la **progettazione sismica** (§7.6); non **riprodurre** la **Circolare 21/1/2019 n. 7**.

### Cosa fare
- Fornire i coefficienti, la classificazione, i metodi di calcolo del momento resistente, le formule dei
  connettori e i criteri delle colonne composte, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 4.3. Verificare i coefficienti (γC, γA, γS, γV), le formule dei connettori
(PRd,a/PRd,c, α) e i limiti (ftk, d, classe cls).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #392)
- Task files: 2 (`inquadra-materiali-sezioni-composte.md`, `inquadra-connessione-taglio-composte.md`)
- Esempi: 2 (coefficienti e metodo di calcolo per una trave composta di classe 2; resistenza di progetto di
  un piolo con testa)
