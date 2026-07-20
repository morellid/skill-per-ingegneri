# resistenza-fuoco-strutture-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista/professionista antincendio da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della resistenza al
fuoco delle strutture** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 3.6.1 (Incendio)**:
definizioni, richieste di prestazione, classi, procedura di analisi e verifiche.

**Non calcola** il carico d'incendio né **esegue** le analisi termiche/meccaniche e **non sostituisce** il
progettista: fornisce le definizioni (R/E/I), la struttura del carico d'incendio [3.6.1], i livelli (Tab.
3.5.IV), le classi (15-360) e le curve nominali. È **distinta** dalla skill sui procedimenti antincendio (DPR
151/2011).

## Target

Ingegneri strutturisti e professionisti antincendio che devono inquadrare la resistenza al fuoco delle
strutture secondo le NTC 2018 par. 3.6.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-prestazioni-classi-fuoco` | Definizioni (R/E/I), carico d'incendio qf,d [3.6.1], livelli di prestazione (Tab. 3.5.IV) e classi 15-360 (§3.6.1.1-3.6.1.3) |
| `inquadra-analisi-verifica-fuoco` | Procedura di analisi: incendio di progetto (curve nominali [3.6.2]-[3.6.4]), evoluzione temperatura, comportamento meccanico e verifiche (§3.6.1.5) |

Nucleo: **definizioni** R/E/I, **carico d'incendio** qf,d = qf·δq1·δq2·δn, **livelli** I-V, **classi** 15-360
min, **curve nominali** (standard θg = 20 + 345·log10(8t+1)) e **verifica** sul tempo pari alla classe in
combinazione eccezionale (§3.6.1).

## Relazione con altre skill

- Copre la **progettazione strutturale in caso di incendio** rinviata dal §3.6.1 dalle "costruzioni di X"
  (§4.x). È **distinta** da `prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti amministrativi
  VVF). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** il carico d'incendio (fattori δni nel **DM 9/3/2007**) né esegue le **analisi
  termiche/meccaniche**; **non** fornisce le proprietà dei materiali ad alta temperatura (**Eurocodici parte
  1-2**).
- **Non stabilisce** le classi/livelli specifici delle regole tecniche VVF (**D.Lgs 139/2006**, DM 3/8/2015
  RTO); **non** tratta i procedimenti antincendio (DPR 151/2011).
- **Non sostituisce** il progettista strutturale né il professionista antincendio.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né il professionista antincendio, né la lettura del par. 3.6.1 delle NTC 2018 e delle regole tecniche di prevenzione incendi.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
