# opere-materiali-sciolti-scavi-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico da completare)

Skill di **supporto documentale** al **progettista geotecnico** per l'**inquadramento della progettazione e
della verifica delle opere di materiali sciolti** (rilevati, argini di difesa, terrapieni, colmate, rinterri) e
dei **fronti di scavo** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 6.8**: criteri generali,
verifiche SLU/SLE, aspetti costruttivi, controlli e monitoraggio, e disciplina dei fronti di scavo.

**Non calcola** le verifiche né **dimensiona** il manufatto o il fronte di scavo, **non definisce** il modello
geotecnico e **non sostituisce** il progettista: fornisce i criteri, la procedura di verifica (Combinazione 2
A2+M2+R2, Tab. 6.8.I con γR = 1,1, stabilità globale nelle varie fasi) e la regola della struttura di sostegno
dei fronti di scavo.

## Target

Ingegneri geotecnici che devono inquadrare la progettazione o la verifica di un'opera in terra (rilevato,
argine, terrapieno) o di un fronte di scavo secondo le NTC 2018 par. 6.8.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-materiali-sciolti` | Criteri, verifiche SLU (Combinazione 2 A2+M2+R2, Tab. 6.8.I γR = 1,1, stabilità globale nelle varie fasi), SLE, aspetti costruttivi e monitoraggio dei manufatti di materiali sciolti (§6.8.1-6.8.5) |
| `inquadra-fronti-scavo` | Indagini, profilo di scavo e verifiche dei fronti di scavo; struttura di sostegno per fronti verticali > 2 m con personale o in prossimità di manufatti (§6.8.6) |

Nucleo: **verifiche SLU** in **Combinazione 2 (A2+M2+R2)** dell'Approccio 1, coefficienti **Tab. 6.2.I/6.2.II/
6.8.I** (**γR = 1,1**), **stabilità globale** manufatto-terreno nelle diverse fasi, e per i **fronti di scavo** la
**struttura di sostegno** obbligatoria oltre i 2 m di fronte verticale con permanenza di personale (§6.8).

## Relazione con altre skill

- **Complementa** `opere-sostegno-ntc` (§6.5), `stabilita-pendii-naturali-ntc` (§6.3) e
  `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12).
- **Distinta e complementare** rispetto a `sicurezza-scavi-fondazioni-dlgs81` (sicurezza dei lavoratori negli
  scavi, D.Lgs 81/2008 Titolo IV) e `terre-rocce-scavo-dpr120` (terre e rocce come sottoprodotti, DPR 120/2017).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.8** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; Tab. 6.8.I e soglia dei 2 m verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le verifiche né **dimensiona** il manufatto, il fronte di scavo o la struttura di sostegno;
  **non** definisce il modello geotecnico.
- **Non tratta** gli **sbarramenti di ritenuta idraulica** (dighe in terra), la **sicurezza dei lavoratori**
  negli scavi (**D.Lgs 81/2008 Titolo IV**) né le **terre e rocce da scavo** come sottoprodotti (DPR 120/2017).
- **Non riproduce** la **Circolare 21/1/2019 n. 7** né tratta la **progettazione sismica** (Cap. 7).

**La skill è un supporto documentale: non sostituisce il progettista geotecnico, né la lettura del par. 6.8 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
