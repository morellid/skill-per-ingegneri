# AGENTS.md - verifica-liquefazione-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico / strutturale** per l'**inquadramento della verifica di
stabilità del sito nei confronti della liquefazione** in condizioni sismiche secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafo 7.11.3.4**: generalità/definizione, condizioni di esclusione della verifica,
metodi di analisi (coefficiente di sicurezza). Target: ingegneri geotecnici e strutturisti che redigono la
relazione geotecnica per siti sismici.

**È una skill documentale per il tecnico**: fornisce la definizione del fenomeno, le quattro condizioni di
esclusione e la struttura della verifica (coefficiente di sicurezza = resistenza/sollecitazione); **non**
calcola il coefficiente di sicurezza (CRR/CSR, correlazioni con (N₁)₆₀ / q_c1N), **non** progetta gli
interventi di consolidamento.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre il compito di **verifica alla liquefazione** (§7.11.3.4), nell'ambito
del §7.11 «Opere e sistemi geotecnici». È **distinta** da `stabilita-pendii-naturali-ntc` (§6.3, stabilità
statica dei pendii) e da `verifiche-geotecniche-slu-ntc` (§6.2.4, approcci progettuali SLU); si appoggia a
`categorie-sottosuolo-topografiche-ntc` (§3.2.2) e `spettro-risposta-ntc` (§3.2.3) per l'azione sismica di
riferimento (a_max, S). Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n.
42/2018). Restano fuori scope: il calcolo del coefficiente di sicurezza con metodi di letteratura/prove, la
progettazione degli interventi di consolidamento e la stabilità dei pendii sismica (§7.11.3.5).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-11-3-4**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill
  NTC). Par. 7.11.3.4 (pagine PDF 284-285) estratto con `pdftotext -layout` e verificato sull'immagine
  (`pdftoppm -r 150`) per pedici e disuguaglianze.

Trascrizione in `references/fonti/ntc2018-par-7-11-3-4.md`; estratto operativo in
`references/estratti/verifica-liquefazione-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **Definizione** (§7.11.3.4.1): perdita di resistenza al taglio / deformazioni plastiche in terreni saturi
  prevalentemente sabbiosi, azioni cicliche/dinamiche in condizioni non drenate; conseguenze (consolidamento /
  trasferimento del carico; fondazioni profonde → riduzione capacità portante e incrementi nei pali).
- **Esclusione** (§7.11.3.4.2, basta una): a_max < 0,1 g (campo libero); falda > 15 m; (N₁)₆₀ > 30 o q_c1N > 180
  (100 kPa); granulometria fuori Fig. 7.11.1 (U_c < 3,5 / > 3,5).
- **Metodi** (§7.11.3.4.3): coeff. di sicurezza = resistenza disponibile / sollecitazione indotta; metodi
  storico-empirici; margine motivato dal progettista.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** il coefficiente di sicurezza (CRR/CSR, correlazioni con (N₁)₆₀ / q_c1N, magnitudo): sono
  metodi di letteratura/prove, non nelle NTC.
- Non **progettare** gli interventi di consolidamento né le fondazioni profonde; non **trattare** la stabilità
  dei pendii (§7.11.3.5 / §6.3) né l'azione sismica di dettaglio (§3.2.3).

### Cosa fare
- Fornire definizione, condizioni di esclusione e struttura della verifica, sempre con rinvio al
  paragrafo/figura NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.11.3.4. Verificare sull'immagine le costanti delle condizioni di esclusione (0,1 g,
15 m, (N₁)₆₀ > 30, q_c1N > 180, 100 kPa, U_c 3,5).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #446)
- Task files: 2 (`valuta-esclusione-verifica-liquefazione.md`, `inquadra-metodo-coefficiente-sicurezza.md`)
- Esempi: 2 (sito escluso dalla verifica per falda profonda / (N₁)₆₀ elevato; inquadramento del coefficiente
  di sicurezza quando nessuna condizione di esclusione è soddisfatta)
