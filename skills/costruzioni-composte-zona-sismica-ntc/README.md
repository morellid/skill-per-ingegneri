# costruzioni-composte-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di strutture composte da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle regole generali**
delle **costruzioni composte di acciaio-calcestruzzo in zona sismica** secondo le **NTC 2018** (D.M. 17 gennaio
2018), **paragrafo 7.6**: comportamenti, materiali, tipologie, fattori di comportamento, rigidezza e capacity design.

**Non esegue** le verifiche (resistenza/duttilità di membrature e collegamenti) né **progetta** i collegamenti e
**non sostituisce** il progettista: fornisce comportamenti, materiali, tipologie, q0, la rigidezza (n=7) e i
capisaldi del capacity design. È **distinta** da `costruzioni-composte-acciaio-cls-ntc` (§4.3, statica),
`costruzioni-acciaio-zona-sismica-ntc` (§7.5) e `fattore-comportamento-q-sismica-ntc` (§7.3.1).

## Target

Ingegneri strutturisti e progettisti di edifici/strutture composte acciaio-calcestruzzo che devono impostare una
struttura composta in zona sismica secondo le NTC 2018 par. 7.6.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-tipologie-fattore-q` | Comportamenti (§7.6), materiali (§7.6.1), tipologie e fattori q0 (§7.6.2) e rigidezza n=7 (§7.6.3) |
| `verifica-requisiti-capacity-design` | Criteri e capisaldi del capacity design per le strutture dissipative (§7.6.4: EU,Rd, Rj,d≥RU,Rd, NEd/Npl,Rd ≤ 0,3, μ) |

Nucleo: **comportamenti a/b/c** (§7.6); **materiali** (cls C20/25-C40/50, acciaio B450C); **tipologie** e **q0**
(Tab. 7.3.II); **rigidezza** n=Ea/Ecm=7; **capacity design** (EU,Rd=1,1·γov·Epl,Rd; NEd/Npl,Rd ≤ 0,3).

## Relazione con altre skill

- Copre le **regole generali** per le composte acciaio-cls in zona sismica (§7.6). **Distinta** da
  `costruzioni-composte-acciaio-cls-ntc` (§4.3, statica), `costruzioni-acciaio-zona-sismica-ntc` (§7.5) e
  `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 251-253.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche** di resistenza (RES) e di duttilità (DUT) di membrature e collegamenti né le
  regole specifiche per tipologia/elemento (§§ 7.6.4-7.6.8, Tab. 7.6.I-IV).
- **Non progetta** i **collegamenti** né calcola il **q0** numerico (Tab. 7.3.II).
- **Non tratta** i requisiti **statici** (§4.3, → skill dedicata), le regole sismiche dell'**acciaio** (§7.5, →
  skill dedicata) né il **fattore q** (§7.3.1, → skill dedicata); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.6 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
