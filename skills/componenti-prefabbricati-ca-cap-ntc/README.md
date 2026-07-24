# componenti-prefabbricati-ca-cap-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista / Direttore tecnico di stabilimento di prefabbricati da completare)

Skill di **supporto documentale** al **progettista strutturale**, al **Direttore dei Lavori** e ai **produttori**
per la **qualificazione**, il **controllo di produzione** e l'**accettazione** dei componenti prefabbricati in c.a.
e c.a.p. secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 11.8**: generalità e metodi di dichiarazione,
requisiti degli stabilimenti, controllo di produzione (cls/acciaio) e marchiatura, procedure di qualificazione
serie dichiarata/controllata, documenti di accompagnamento e accettazione in cantiere.

**Non esegue** il progetto degli elementi prefabbricati né le verifiche (§4.1.10) e **non sostituisce** il
progettista né il Direttore dei Lavori: inquadra i metodi di dichiarazione, il controllo di produzione, la
marchiatura, le procedure di qualificazione e i documenti di accompagnamento. È **distinta** da
`costruzioni-calcestruzzo-ntc` (§4.1, progetto), `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3,
accettazione generale) e `denuncia-collaudo-statico-ca-dpr380` (DPR 380).

## Target

Ingegneri strutturisti, Direttori dei Lavori e produttori/Direttori tecnici di stabilimento che devono inquadrare
la qualificazione, il controllo di produzione e l'accettazione dei componenti prefabbricati in c.a./c.a.p. secondo
le NTC 2018 par. 11.8.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-qualificazione-e-controllo-produzione` | Generalità/metodi 1-2-3 (§11.8.1), requisiti stabilimenti (§11.8.2), controllo di produzione e materiali di serie (§11.8.3), procedure di qualificazione serie dichiarata/controllata (§11.8.4) |
| `verifica-marchiatura-e-documenti-accettazione` | Marchiatura (§11.8.3.4) e documenti di accompagnamento/accettazione del Direttore dei Lavori (§11.8.5) |

Nucleo: **Metodi 1/2/3** di dichiarazione e **art. 58 DPR 380** (§11.8.1); **controllo di produzione** cls
(controllo tipo A/B, tarature annuali, registri 10 anni) e acciaio (**piegatura 3/90 t**, **trazione 3/10 rotoli**)
solo per prodotti privi di marcatura CE (§11.8.3); **marchiatura > 8 kN** (§11.8.3.4); **serie dichiarata/
controllata** con validità **quinquennale** (§11.8.4); **certificato d'origine** e verifica marchiatura (§11.8.5).

## Relazione con altre skill

- Copre la **qualificazione/controllo di produzione/accettazione dei componenti prefabbricati** (§11.8, Cap. 11).
  **Distinta** da `costruzioni-calcestruzzo-ntc` (§4.1, progetto), `controlli-accettazione-cls-acciaio-ntc`
  (§11.2/§11.3) e `denuncia-collaudo-statico-ca-dpr380` (DPR 380). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.8** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 355-357.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** il **progetto** degli elementi prefabbricati né le **verifiche** (§4.1.10).
- **Non tratta** i **controlli di accettazione generali** di cls/acciaio (§§11.2/11.3, → skill
  `controlli-accettazione-cls-acciaio-ntc`) né la **denuncia/collaudo statico** (DPR 380, → skill
  `denuncia-collaudo-statico-ca-dpr380`); non sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.8 delle NTC 2018 e della relativa Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
