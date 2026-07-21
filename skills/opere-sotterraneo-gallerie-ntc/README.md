# opere-sotterraneo-gallerie-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico/strutturista da completare)

Skill di **supporto documentale** al **progettista geotecnico e strutturale** per l'**inquadramento della
progettazione e della verifica delle opere in sotterraneo** (gallerie, caverne, pozzi) secondo le **NTC 2018**
(D.M. 17 gennaio 2018), **paragrafo 6.7**: prescrizioni generali, caratterizzazione geologica e geotecnica,
criteri di progetto, analisi e verifiche di sicurezza, controllo e monitoraggio.

**Non calcola** le verifiche né **dimensiona** l'opera o i rivestimenti, **non definisce** il modello
geologico/geotecnico e **non sostituisce** il progettista: fornisce gli elementi da giustificare, gli stati
limite (GEO/STR/UPL/HYD) e la procedura di verifica (Approccio 1 con Comb. 1 e Comb. 2, γR = 1,0 per R1/R2).

## Target

Ingegneri geotecnici e strutturisti che devono inquadrare la progettazione o la verifica di una galleria,
caverna o pozzo secondo le NTC 2018 par. 6.7.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifiche-opere-sotterraneo` | Analisi e verifiche SLU/SLE: stati limite GEO/STR/UPL/HYD, Approccio 1 con Comb. 1 (A1+M1+R1) e Comb. 2 (A2+M2+R2), γR = 1,0 per R1/R2, verifiche strutturali (§6.2.4.1.3) e idrauliche (§6.2.4.2), metodo osservazionale (§6.7.5) |
| `inquadra-caratterizzazione-progetto-monitoraggio` | Prescrizioni generali, caratterizzazione geologica/geotecnica, criteri di progetto e monitoraggio (§6.7.1-6.7.4, 6.7.6) |

Nucleo: **stati limite GEO/STR/UPL/HYD**, **Approccio 1** con **entrambe** le combinazioni (**Comb. 1 A1+M1+R1**
e **Comb. 2 A2+M2+R2**, **γR = 1,0** per R1/R2), stabilità di versanti/imbocchi con §6.3 e §6.8, e **metodo
osservazionale** (convergenza radiale, deformazione del fronte, spostamenti di superficie) (§6.7).

## Relazione con altre skill

- **Complementa** `stabilita-pendii-naturali-ntc` (§6.3, stabilità dei versanti) e
  `opere-materiali-sciolti-scavi-ntc` (§6.8, fronti agli imbocchi), richiamati dal §6.7.5, e
  `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le verifiche né **dimensiona** l'opera, i rivestimenti o gli interventi di stabilizzazione;
  **non** definisce il modello geologico/geotecnico.
- **Non tratta** la **sicurezza dei lavoratori** in sotterraneo, le **macchine di scavo (TBM)** come prodotti né
  la **progettazione sismica** (Cap. 7).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.7 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
