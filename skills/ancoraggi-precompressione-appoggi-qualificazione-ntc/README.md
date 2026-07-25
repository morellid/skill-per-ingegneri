# ancoraggi-precompressione-appoggi-qualificazione-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista / Direttore dei Lavori esperto di prodotti da costruzione da completare)

Skill di **supporto documentale** al **progettista strutturale** e al **Direttore dei Lavori** per la
**qualificazione** e i **controlli di accettazione in cantiere** di **ancoranti per uso strutturale**, **giunti di
dilatazione stradale**, **sistemi di precompressione a cavi post-tesi**, **tiranti di ancoraggio per uso geotecnico**
e **appoggi strutturali** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafi 11.4, 11.5 e 11.6**.

**Non esegue** il progetto né le verifiche dei prodotti e **non sostituisce** il progettista, il Direttore dei Lavori
né le Linee guida/norme europee: inquadra il **percorso di qualificazione** (punti A/C del §11.1, ETA/ETAG/CVT, UNI EN
1337) e la **verifica del Direttore dei Lavori**. È **distinta** da `tiranti-ancoraggio-ntc` (§6.6, progetto/verifiche
geotecniche) e da `dispositivi-antisismici-qualificazione-ntc` (§11.9, dispositivi antisismici UNI EN 15129).

## Target

Ingegneri strutturisti e Direttori dei Lavori che devono qualificare e accettare in cantiere ancoranti (tasselli),
giunti, sistemi di post-tensione, tiranti geotecnici e appoggi strutturali secondo le NTC 2018 par. 11.4-11.6.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-ancoranti-e-giunti` | Ancoranti per uso strutturale (ETAG 001, categoria sismica C2) e giunti di dilatazione stradale (ETAG 032) (§11.4) |
| `inquadra-precompressione-tiranti-e-appoggi` | Precompressione post-tesi e tiranti geotecnici (punto C, CVT/ETA, prove ETAG 013) (§11.5); appoggi strutturali (punto A, UNI EN 1337 + CE / caso C) (§11.6) |

Nucleo: **ancoranti** qualificati su **ETAG 001**, in zona sismica **categoria C2** per tutte le classi d'uso (§11.4.1);
**giunti** su **ETAG 032** (§11.4.2); **precompressione** e **tiranti** via **punto C del §11.1** (CVT/ETA, prove ETAG
013) con verifica del **Direttore dei Lavori** (§11.5); **appoggi** su **UNI EN 1337 + Marcatura CE** con **Sistema VVCP
1** o **caso C** (§11.6).

## Relazione con altre skill

- Copre la **qualificazione/accettazione** di ancoranti, giunti, precompressione, tiranti e appoggi (§11.4-11.6, Cap.
  11). **Distinta** da `tiranti-ancoraggio-ntc` (§6.6, progetto/verifiche), `dispositivi-antisismici-qualificazione-ntc`
  (§11.9, UNI EN 15129) e dalle skill materiali del Cap. 11. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.4-11.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con i riferimenti
  (C2, VVCP 1, ETAG 001/032/013, UNI EN 1337) verificati sull'immagine della pagina PDF 348.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** il **progetto/verifiche** dei prodotti (progetto appoggi, verifiche ancoranti, progetto cavi
  post-tesi, verifiche geotecniche dei tiranti al §6.6).
- **Non riproduce** il **dettaglio delle prove** delle Linee guida/norme europee (ETAG 001/013/032, UNI EN 1337), che
  restano la fonte per procedure e valori; non sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura dei par. 11.4-11.6 delle NTC 2018 e delle Linee guida/norme europee applicabili (ETAG, UNI EN 1337).**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
