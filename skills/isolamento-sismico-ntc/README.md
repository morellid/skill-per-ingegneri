# isolamento-sismico-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle costruzioni con
isolamento e/o dissipazione sismica** (edifici e ponti a isolamento alla base) secondo le **NTC 2018** (D.M. 17
gennaio 2018), **paragrafo 7.10**.

**Non esegue** l'analisi né le verifiche e **non progetta** i dispositivi (§11.9): fornisce scopo e strategie, i
requisiti, le indicazioni progettuali, le condizioni di modellazione/analisi e le verifiche SLE/SLV/SLC.

## Target

Ingegneri strutturisti che progettano o adeguano edifici/ponti con isolamento sismico alla base (ospedali, edifici
strategici, retrofit) e devono inquadrarne requisiti, modello, metodo di analisi e verifiche secondo le NTC 2018
par. 7.10.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-scopo-requisiti-dispositivi` | Scopo e strategie, requisiti generali (campo elastico, agS≤0,075g, §11.9) e indicazioni progettuali dei dispositivi (V≥0, diaframma rigido) (§7.10.1-7.10.4) |
| `inquadra-modellazione-analisi-verifiche` | Modellazione, condizioni del modello lineare equivalente, applicabilità dell'analisi statica/dinamica lineare e verifiche SLD/SLV/SLC (§7.10.5-7.10.8) |

Nucleo: le due **strategie** d'isolamento (allungare il periodo / limitare la forza), le condizioni del **modello
lineare equivalente**, i requisiti dell'**analisi statica lineare** (Tis ∈ [3·Tbf, 3,0 s], KV ≥ 800·Kesi, TV < 0,1
s, no push-over) e le **verifiche** SLD (interpiano < 2/3 §7.3.6.1), SLV (q ≤ 1,50 edifici / q = 1 ponti) e SLC
(spostamenti d2).

## Relazione con altre skill

- **Complementa** `spettro-risposta-ntc` (§3.2), `combinazione-componenti-sismiche-ntc` (§7.3.5),
  `fattore-comportamento-q-sismica-ntc` (§7.2.2-7.3.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e
  `criteri-modellazione-sismica-ntc` (§7.2.6). La qualificazione/prove dei dispositivi (§11.9) è fuori scope.
  Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto verbatim;
  le soglie verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** l'analisi né le verifiche; **non calcola** forze/spostamenti (formule [7.10.1]-[7.10.5]).
- **Non progetta** né qualifica i **dispositivi** di isolamento/dissipazione (§11.9).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.10 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
