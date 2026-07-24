# ponti-zona-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista esperto di ponti da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle regole generali**
dei **ponti in zona sismica** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 7.9**: campo di
applicazione, criteri dissipativo/non dissipativo, fattore di comportamento e requisiti dell'analisi.

**Non esegue** le verifiche (duttilità/resistenza delle pile) né **progetta** i dettagli costruttivi e **non
sostituisce** il progettista: fornisce i criteri, i valori di q0/νk/λ(α), la regolarità KR e i requisiti
dell'analisi. È **distinta** dalle skill sui **carichi da traffico** dei ponti (`azioni-traffico-ponti-stradali-ntc`
§5.1.3, `azioni-traffico-ponti-ferroviari-ntc` §5.2.2) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1, edifici).

## Target

Ingegneri strutturisti e infrastrutturali che devono impostare la progettazione sismica di un ponte a pile e
travate secondo le NTC 2018 par. 7.9.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-fattore-comportamento` | Campo di applicazione (§7.9.1), criteri dissipativo/non dissipativo (§7.9.2) e valori del fattore di comportamento q0/νk/λ(α) (§7.9.2.1) |
| `verifica-regolarita-requisiti-analisi` | Regolarità KR (§7.9.2.1), modello strutturale e requisiti dell'analisi statica lineare (§7.9.3-7.9.4.1) |

Nucleo: **dissipazione limitata alle pile** (§7.9.2); **q0 = 1,0** (non diss.) e **q0/νk/λ(α)** (diss.); **νk ≤
0,3/0,6** e [7.9.1]; **regolarità KR** (r̃<2 → 1; r̃≥2 → 2/r̃); ponti irregolari **q = 1,5/3,5**; **analisi statica
lineare** (massa efficace pila ≤ 1/5; eccentricità ≤ 5%).

## Relazione con altre skill

- Copre le **regole generali** per i ponti in zona sismica (§7.9). **Distinta** dalle skill sui carichi da
  traffico (§5.1.3/§5.2.2) e da `fattore-comportamento-q-sismica-ntc` (§7.3.1). Condivide la fonte GU con le altre
  skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.9** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 269-271.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **verifiche** di duttilità/resistenza delle pile e dei dispositivi né i **metodi di analisi
  non lineare** (§§ 7.9.4-7.9.6).
- **Non progetta** i **dettagli costruttivi** (§7.9.6) né calcola il **q0** numerico (Tab. 7.3.II).
- **Non tratta** i **carichi da traffico** (§§ 5.1.3/5.2.2, → skill dedicate) né il **fattore q** per gli edifici
  (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.9 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
