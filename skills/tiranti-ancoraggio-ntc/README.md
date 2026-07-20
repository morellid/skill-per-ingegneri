# tiranti-ancoraggio-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico/strutturista da completare)

Skill di **supporto documentale** al **progettista geotecnico e strutturale** per l'**inquadramento del
progetto e della verifica dei tiranti di ancoraggio** secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 6.6**: criteri di progetto, verifica SLU a sfilamento, aspetti costruttivi e prove di carico.

**Non calcola** la resistenza allo sfilamento né **dimensiona** il tirante, **non esegue** le prove e **non
sostituisce** il progettista: fornisce i criteri, la procedura di verifica (Ed ≤ Rad, Rad = Rak/γR), i fattori
di correlazione (Tab. 6.6.II/III) e le regole delle prove di carico.

## Target

Ingegneri geotecnici e strutturisti che devono inquadrare il progetto e la verifica dei tiranti di ancoraggio
(anche a servizio di paratie/muri) secondo le NTC 2018 par. 6.6.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-sfilamento-tiranti` | Verifica SLU a sfilamento: Ed ≤ Rad, Rad = Rak/γR (Tab. 6.6.I), Rak da prove/calcolo (Tab. 6.6.II/III), combinazione A1+M1+R3 (§6.6.2) |
| `inquadra-criteri-prove-tiranti` | Criteri di progetto (§6.6.1), aspetti costruttivi (§6.6.3) e prove di carico di progetto e in corso d'opera (§6.6.4) |

Nucleo: **verifica a sfilamento** (Ed ≤ Rad), **Rad = Rak/γR** (γR 1,1/1,2), **Rak** da prove (Tab. 6.6.II) o
calcolo (Tab. 6.6.III), combinazione **A1+M1+R3**, e **prove di carico** (di progetto e in corso d'opera a
1,2·Pd) (§6.6).

## Relazione con altre skill

- **Complementa** `opere-sostegno-ntc` (§6.5): le paratie/muri tirantati richiedono la verifica degli
  ancoraggi, che il §6.6 disciplina. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** la resistenza allo sfilamento né **dimensiona** il tirante o la sua armatura; **non** valuta
  Ra,m/Ra,c al posto del progettista.
- **Non esegue** né **interpreta** le prove di carico; **non riproduce** i sistemi di ancoraggio come prodotti
  (§11.5.2) né la progettazione strutturale dell'armatura.
- **Non tratta** le **paratie/muri** (§6.5, skill `opere-sostegno-ntc`) né la **progettazione sismica** (Cap.
  7); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.6 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
