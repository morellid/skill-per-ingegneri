# AGENTS.md - opere-sostegno-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale e geotecnico** per l'**inquadramento delle verifiche
delle opere di sostegno** - **muri di sostegno**, **paratie** e **strutture miste** - secondo le **NTC
2018** (DM 17 gennaio 2018), **paragrafo 6.5**. Target: ingegneri strutturisti e geotecnici, progettisti
di opere di sostegno e di scavi.

**E' una skill documentale per il tecnico**: inquadra tipologie, criteri di progetto, azioni, modello
geometrico, stati limite, approcci progettuali e coefficienti parziali; **non calcola** le spinte, le
verifiche o i coefficienti e **non dimensiona** l'opera.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Complementare alle altre skill NTC del repo, che condividono la stessa
fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018): `capacita-portante-fondazione-ntc` (§6.4.2),
`cedimenti-edometrici-ntc`, `combinazioni-carico-ntc`, `carichi-atmosferici-ntc`,
`costruzioni-esistenti-ntc-cap8`. Questa copre le **opere di sostegno** (§6.5): non ripete la capacità
portante delle fondazioni (§6.4.2, che è una delle verifiche richiamate qui) né la stabilità dei pendii
(§6.8) se non nei richiami.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-5**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 6.5 estratto con `pdftotext -layout` (pp. 194-197) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-5.md`; estratto operativo in
`references/estratti/opere-sostegno-checklist.md`.

## Punti chiave (verificati sul testo)

- **Tipologie** (§6.5): **muri** (peso proprio), **paratie** (resistenza a valle + ancoraggi/puntoni),
  **strutture miste**; sismico al **§7.11.6** (non trattato).
- **Criteri** (§6.5.1): riempimento a tergo costipato e drenante, drenaggio efficace nel tempo,
  monitoraggio della perdita di efficacia di drenaggi/tiranti/ancoraggi, effetti sulle costruzioni
  preesistenti, indagini estese alla stabilità locale e globale.
- **Azioni e modello** (§6.5.2): sovraccarichi a tergo (costruzioni, depositi, veicoli, apparecchi di
  sollevamento); **riduzione della quota di valle** = minore tra 10% dell'altezza, 10% della differenza
  di quota e 0,5 m; **falda** SLU non inferiore ai terreni con **k < 10⁻⁶ m/s**.
- **Muri - SLU** (§6.5.3.1.1): GEO (scorrimento, carico limite, ribaltamento, stabilità globale) e STR;
  **stabilità globale** → Approccio 1 Comb. 2 (A2+M2+R2); **rimanenti** → Approccio 2 (A1+M1+R3) con
  **Tab. 6.5.I** (capacità portante 1,4; scorrimento 1,1; ribaltamento 1,15; resistenza a valle 1,4).
  Scorrimento: in generale **no** resistenza passiva a valle (al più 50%, giustificata).
- **Paratie - SLU** (§6.5.3.1.2): GEO/UPL/HYD e STR; **stabilità globale** → Approccio 1 Comb. 2; **UPL/
  HYD** come §6.2.4.2; **rimanenti** → Approccio 1, Comb. 1 (A1+M1+R1) e Comb. 2 (A2+M2+R1) con R1 = 1;
  per δ > φ'/2 non planarità delle superfici nella resistenza passiva.
- **SLE** (§6.5.3.2): spostamenti compatibili con funzionalità e manufatti adiacenti; analisi di
  interazione per manufatti sensibili.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** spinte, verifiche o coefficienti, né **dimensionare** muro o paratia.
- Non **riprodurre** le Tabelle 6.2.I/6.2.II (azioni e parametri) né la Tab. 6.8.I (stabilità globale),
  che restano da leggere sul testo; qui si cita solo la **Tab. 6.5.I** (γR dei muri, gruppo R3).
- Non trattare il **caso sismico** (§7.11.6) né la stabilità dei pendii (§6.8) se non nei richiami.
- Non sostituire la **Circolare 21/1/2019 n. 7** (istruzioni applicative).

### Cosa fare
- Inquadrare tipologia, criteri, azioni e modello geometrico; per muri e paratie gli stati limite, gli
  approcci/combinazioni e (per i muri) i coefficienti della Tab. 6.5.I; le verifiche di esercizio.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.5. Verificare che la Tab. 6.5.I e le combinazioni degli approcci non
siano state modificate.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista/geotecnico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #368)
- Task files: 2 (`inquadra-criteri-azioni-sostegno.md`, `inquadra-verifiche-slu-sostegno.md`)
- Esempi: 2 (muro a mensola in c.a. - stati limite/approccio/coefficienti/resistenza passiva; paratia
  con tiranti - stati limite/approccio/combinazioni/stabilità globale/idraulici)
