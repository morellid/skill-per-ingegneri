# dispositivi-antisismici-qualificazione-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di isolamento sismico / collaudatore da completare)

Skill di **supporto documentale** al **progettista strutturale**, al **Direttore dei Lavori** e al **collaudatore**
per la **qualificazione** e i **controlli di accettazione in cantiere** dei **dispositivi antisismici e di controllo
delle vibrazioni** (isolatori elastomerici e a scorrimento, dissipatori lineari/non lineari/viscosi, dispositivi di
vincolo a fusibile/provvisori) secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 11.9**: requisiti generali,
tipologie, qualificazione (UNI EN 15129 + Marcatura CE), accettazione demandata al Direttore dei Lavori, prove e
limiti prestazionali per tipo.

**Non esegue** il progetto delle costruzioni con isolamento/dissipazione né **dimensiona** i dispositivi (§7.10) e
**non sostituisce** il progettista, il Direttore dei Lavori né il laboratorio ex art. 59: inquadra il percorso di
qualificazione e la procedura di accettazione. È **distinta** da `isolamento-sismico-ntc` (§7.10, progetto), che
rinvia esplicitamente al §11.9 come fuori scope.

## Target

Ingegneri strutturisti, Direttori dei Lavori e collaudatori che devono qualificare e accettare in cantiere i
dispositivi antisismici (isolatori, dissipatori) secondo le NTC 2018 par. 11.9.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-e-qualificazione` | Requisiti generali (vita servizio, temperatura, UNI EN 15129) e tipologie (§11.9-11.9.1); procedura di qualificazione (UNI EN 15129 + CE / caso C del §11.1) (§11.9.2) |
| `imposta-accettazione-e-prove-per-tipo` | Procedura di accettazione del Direttore dei Lavori (§11.9.3) e prove/limiti per tipo (§11.9.4-11.9.10): numerosità ≥ 20% e ≥ 4, Tab. 11.9.I-IV, prova quasi statica |

Nucleo: **vita di servizio > 10 anni** e temperatura **−15/+45 °C** (§11.9); qualificazione **UNI EN 15129 + Marcatura
CE** o **caso C** (§11.9.2); accettazione **del Direttore dei Lavori** con **campionamento sui lotti del cantiere** e
prove **laboratorio art. 59** (§11.9.3); prove **≥ 20% e ≥ 4** e limiti **Tab. 11.9.I-IV** (§11.9.4-11.9.10).

## Relazione con altre skill

- Copre la **qualificazione/accettazione dei dispositivi antisismici** (§11.9, Cap. 11). **Distinta** da
  `isolamento-sismico-ntc` (§7.10, progetto) e dalle skill materiali del Cap. 11
  (`controlli-accettazione-cls-acciaio-ntc` §11.2/§11.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.9** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con **tutti i
  valori numerici verificati sull'immagine** delle pagine PDF 358-364.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** il **progetto** delle costruzioni con isolamento/dissipazione né **dimensiona** i dispositivi
  (§7.10, → skill `isolamento-sismico-ntc`).
- **Non tratta** la qualificazione dei **materiali** del Cap. 11 (cls/acciaio §§11.2/11.3, → skill dedicate); non
  sostituisce il progettista, il Direttore dei Lavori né il laboratorio ex art. 59.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.9 delle NTC 2018, della UNI EN 15129 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
