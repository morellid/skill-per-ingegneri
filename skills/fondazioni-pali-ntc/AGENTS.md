# AGENTS.md - fondazioni-pali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale e geotecnico** per l'**inquadramento delle verifiche
delle fondazioni su pali** (e delle **fondazioni miste** a platea su pali) secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafo 6.4.3**. Target: ingegneri strutturisti e geotecnici, progettisti di
fondazioni profonde.

**E' una skill documentale per il tecnico**: inquadra stati limite, approcci, coefficienti parziali,
fattori di correlazione, controlli d'integrita' e prove di carico; **non calcola** le resistenze o le
verifiche e **non dimensiona** i pali.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Complementare alle altre skill NTC del repo, che condividono la stessa
fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018): `capacita-portante-fondazione-ntc` (fondazioni
superficiali §6.4.2), `opere-sostegno-ntc` (§6.5), `cedimenti-edometrici-ntc`, `combinazioni-carico-ntc`,
`relazione-geologica-geotecnica-ntc`. Questa copre le **fondazioni su pali** (§6.4.3): non ripete la
capacita' portante delle fondazioni superficiali (§6.4.2) se non nel richiamo alla Tab. 6.4.I.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-4-3**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 6.4.3 estratto con `pdftotext -layout` (pp. 190-194) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-4-3.md`; estratto operativo in
`references/estratti/fondazioni-pali-checklist.md`.

## Punti chiave (verificati sul testo)

- **Impostazione** (§6.4.3): soli pali (§6.4.3.1-2) o fondazione mista (§6.4.3.3-4); azioni permanenti con
  peso proprio del palo e **attrito negativo** (γM del caso M1, Tab. 6.2.II); sisma §7.11.5.3.2.
- **SLU** (§6.4.3.1): GEO (carico limite assiale, trasversale, sfilamento in trazione, stabilità globale)
  e STR; **stabilità globale** → Approccio 1 Comb. 2 (A2+M2+R2); **rimanenti** → Approccio 2 (A1+M1+R3);
  negli STR il γR non si porta in conto.
- **Tab. 6.4.II** (γR, R3): base 1,15/1,35/1,3; laterale compr. 1,15; totale 1,15/1,30/1,25; laterale
  trazione 1,25 (infissi/trivellati/elica).
- **R_k** (§6.4.3.1.1): minore tra media e minimo con i **fattori di correlazione ξ** (Tab. 6.4.III prove
  statiche, 6.4.IV verticali indagate, 6.4.V prove dinamiche). Palificata: effetto di gruppo.
- **Carichi trasversali** (§6.4.3.1.2): γT = 1,3 (Tab. 6.4.VI).
- **SLE** (§6.4.3.2), **fondazioni miste** (§6.4.3.3-4), **controlli d'integrità** (§6.4.3.6: 5% min 2;
  grande diametro d≥80 cm con ≤4 pali → tutti), **prove di carico** (§6.4.3.7: progetto ≥2,5× SLE; in
  corso d'opera 1,5× o 1,2×).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** resistenze, verifiche o coefficienti, né **dimensionare** i pali o la palificata.
- Non **riprodurre** le Tabelle 6.2.I/6.2.II (azioni e parametri) né la Tab. 6.8.I (stabilità globale);
  qui si citano solo le **Tab. 6.4.II/6.4.III/6.4.IV/6.4.V/6.4.VI** dei pali.
- Non trattare il **caso sismico** (§7.11.5.3.2) né le fondazioni superficiali (§6.4.2) se non nei
  richiami.
- Non sostituire la **Circolare 21/1/2019 n. 7** (istruzioni applicative).

### Cosa fare
- Inquadrare impostazione, stati limite, approcci/combinazioni, coefficienti (Tab. 6.4.II/6.4.VI) e
  fattori di correlazione (Tab. 6.4.III/IV/V); fondazioni miste; controlli d'integrità e prove di carico.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.4.3. Verificare che le Tab. 6.4.II/6.4.VI e i fattori di correlazione
non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista/geotecnico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #372)
- Task files: 2 (`inquadra-verifiche-slu-sle-pali.md`, `inquadra-resistenza-caratteristica-prove.md`)
- Esempi: 2 (palificata di pali trivellati - stati limite/approccio/coefficienti/effetto gruppo/carichi
  trasversali; resistenza caratteristica da prove - fattori di correlazione, controlli d'integrità e prove
  di carico)
