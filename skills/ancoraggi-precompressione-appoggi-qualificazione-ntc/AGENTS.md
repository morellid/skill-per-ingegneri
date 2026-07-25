# AGENTS.md - ancoraggi-precompressione-appoggi-qualificazione-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** e al **Direttore dei Lavori** per la **qualificazione** e i
**controlli di accettazione in cantiere** di **ancoranti per uso strutturale**, **giunti di dilatazione stradale**,
**sistemi di precompressione a cavi post-tesi**, **tiranti di ancoraggio per uso geotecnico** e **appoggi
strutturali** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 11.4, 11.5 e 11.6** (Cap. 11 «Materiali e
prodotti per uso strutturale»).

**È una skill documentale per il tecnico**: inquadra il percorso di qualificazione (punti A/C del §11.1, ETA/ETAG/CVT,
UNI EN 1337) e la verifica del Direttore dei Lavori; **non** esegue il progetto né le verifiche dei prodotti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **qualificazione/accettazione** di prodotti/sistemi strutturali «speciali»
(§11.4-11.6, Cap. 11). È **distinta** da:
- `tiranti-ancoraggio-ntc` (§6.6, **progetto e verifiche geotecniche** dei tiranti — aderenza, sfilamento, stati
  limite): il §11.5.2 riguarda solo la **qualificazione** del prodotto;
- `dispositivi-antisismici-qualificazione-ntc` (§11.9, dispositivi **antisismici** — isolatori/dissipatori — norma
  **UNI EN 15129**): gli **appoggi ordinari** del §11.6 seguono la serie **UNI EN 1337**;
- le altre skill materiali del Cap. 11 (`controlli-accettazione-cls-acciaio-ntc` §11.2/§11.3, ecc.).
Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-11-4-11-6**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 11.4-11.6 (pagina PDF 348 = GU 344) estratto con `pdftotext -layout`; i riferimenti (categoria **C2**, **VVCP
  1**, sigle **ETAG 001/032/013**, serie **UNI EN 1337**) verificati sull'immagine (`pdftoppm -r 150`) della pagina
  PDF 348.

Trascrizione in `references/fonti/ntc2018-par-11-4-11-6.md`; estratto operativo in
`references/estratti/ancoraggi-appoggi-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§11.4.1** ancoranti: qualificazione **punto C del §11.1**, base **ETAG 001** (anche prove di accettazione); in
  azioni sismiche, per **tutte le classi d'uso** (§2.4.2) categoria minima **C2** (Annesso E, tab. 1.1, §1.2 ETAG 001).
- **§11.4.2** giunti di dilatazione stradale: **punto C del §11.1**, base **ETAG 032**.
- **§11.5.1** precompressione post-tesi: **punto C del §11.1**; **CVT** (Linea Guida CSLP); fornitura con CVT o CE su
  ETA + manuale; il **DL** verifica, rifiuta le forniture prive, verifica la posa e le prove di accettazione;
  modalità prove → **ETAG 013**.
- **§11.5.2** tiranti geotecnici (attivi/passivi): **punto C del §11.1**; per i **tipo attivo** CVT (Linea Guida CSLP).
- **§11.6** appoggi strutturali: **punto A del §11.1** → **UNI EN 1337 + Marcatura CE**, **Sistema VVCP 1** per
  applicazioni critiche; se non ricadenti → **caso C del §11.1**.

## Convenzioni specifiche

### Cosa NON fare
- Non **progettare/verificare** i prodotti (progetto appoggi, verifiche ancoranti, progetto cavi post-tesi, verifiche
  geotecniche dei tiranti al §6.6).
- Non **riprodurre** il dettaglio delle prove delle Linee guida/norme europee (ETAG 001/013/032, UNI EN 1337): sono
  la fonte per procedure e valori; questa skill inquadra il percorso.
- Non inventare valori: ogni riferimento deve essere rintracciabile in
  `references/fonti/ntc2018-par-11-4-11-6.md`.

### Cosa fare
- Fornire, per ciascun prodotto/sistema, la **via di qualificazione** (punto A/C del §11.1, ETA/ETAG/CVT/UNI EN 1337)
  e i **compiti del Direttore dei Lavori** (documentazione, rifiuto forniture prive, prove di accettazione), con
  rinvio al sotto-paragrafo NTC; per gli ancoranti in zona sismica, la **categoria C2** obbligatoria.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e riestrarre
i par. 11.4-11.6. Verificare sull'immagine i riferimenti (C2; VVCP 1; ETAG 001/032/013; UNI EN 1337; punti A/C del
§11.1).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista / Direttore dei Lavori esperto di prodotti da
  costruzione).

## Stato attuale

- Versione: 0.1.0-alpha (closes #472)
- Task files: 2 (`inquadra-ancoranti-e-giunti.md`, `inquadra-precompressione-tiranti-e-appoggi.md`)
- Esempi: 2 (accettazione di ancoranti in zona sismica con categoria C2; accettazione di appoggi strutturali per un
  ponte UNI EN 1337)
