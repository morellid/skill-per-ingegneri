---
name: opere-sotterraneo-gallerie-ntc
description: "Supporto documentale al progettista geotecnico e strutturale per l'inquadramento della progettazione e della verifica delle opere in sotterraneo (gallerie, caverne, pozzi) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.7. Aiuta a inquadrare l'ambito (opere costruite nel sottosuolo mediante scavo del terreno o della roccia, stabilizzazione della cavita' a breve e lungo termine e rivestimento finale); le prescrizioni generali (modello geologico e geotecnico; elementi da specificare e giustificare: geometria, ubicazione e tracciato, metodi e tecniche di scavo tradizionale o meccanizzato, interventi di stabilizzazione e strutture di rivestimento di prima fase e definitive, opere di protezione agli imbocchi, intercettazione delle acque e controllo delle pressioni interstiziali, provvedimenti antifrana, sicurezza per gas tossici o esplosivi, cavita' e venute d'acqua, messa a dimora dei materiali di risulta) (6.7.1); la caratterizzazione geologica (litotipi, faglie e discontinuita', sismotettonica, franosita', cavita' carsiche, idrogeologia) (6.7.2) e geotecnica (indagini in sito e in laboratorio, potenzialita' spingenti e rigonfianti, pressioni interstiziali, modello geotecnico, metodo osservazionale) (6.7.3); i criteri di progetto (previsione quantitativa degli effetti indotti al contorno e in superficie, in particolare per gallerie poco profonde in ambienti urbanizzati; dimensionamento dei rivestimenti; opere di protezione agli imbocchi; stabilita' globale dei pendii in zona di versante) (6.7.4); le analisi progettuali e le verifiche di sicurezza (stati limite ultimi GEO per la resistenza del terreno o dell'ammasso e STR per gli elementi di stabilizzazione e rivestimento; effetti sui manufatti esistenti; stati limite idraulici UPL e HYD; stabilita' di versanti e fronti agli imbocchi con i criteri dei paragrafi 6.3 e 6.8; Approccio 1 con Combinazione 1 A1+M1+R1 e Combinazione 2 A2+M2+R2 e coefficienti gamma_R dei gruppi R1 e R2 pari all'unita'; verifiche strutturali con i valori caratteristici secondo il paragrafo 6.2.4.1.3 e verifiche idrauliche secondo il paragrafo 6.2.4.2; metodo osservazionale con convergenza radiale, deformazione longitudinale del fronte e spostamenti di superficie) (6.7.5); e il controllo e il monitoraggio (6.7.6). Use when a geotechnical or structural designer must frame the design or verification of underground works (tunnels, caverns, shafts) under the Italian NTC 2018 par. 6.7; it is a documentary aid and does NOT compute the verifications nor size the works or the linings, does NOT define the geological/geotechnical model, does NOT cover the workers' safety underground nor the seismic design, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Opere in sotterraneo: gallerie, caverne, pozzi (NTC 2018 par. 6.7)"
summary: "Inquadra progetto e verifica delle opere in sotterraneo (gallerie, caverne, pozzi) - NTC 2018 par. 6.7: caratterizzazione geologica/geotecnica, criteri di progetto, verifiche SLU GEO/STR/UPL/HYD in Approccio 1 (Comb. 1 e 2, gamma_R = 1,0 per R1/R2), metodo osservazionale."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.7: verifiche SLU GEO/STR/UPL/HYD in Approccio 1 con Comb. 1 (A1+M1+R1) e Comb. 2 (A2+M2+R2), gamma_R dei gruppi R1 e R2 pari all'unita' (Tab. 6.2.I/6.2.II)"
  - "NTC 2018 - par. 6.7.1-6.7.4/6.7.6: modello geologico/geotecnico, criteri di progetto, rivestimenti, monitoraggio; metodo osservazionale (convergenza radiale, deformazione fronte); rinvio par. 6.3/6.8"
version: 0.1.0-alpha
status: alpha
tags:
  - opere-in-sotterraneo
  - gallerie
  - geotecnica
  - ntc-2018
  - metodo-osservazionale
---

# Opere in sotterraneo: gallerie, caverne, pozzi (NTC 2018 par. 6.7)

## Quando usare questa skill

Usala quando un **progettista geotecnico** o **strutturale** deve **inquadrare la progettazione o la verifica**
di un'**opera in sotterraneo** (galleria, caverna, pozzo) secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 6.7**:

- **prescrizioni generali** e **caratterizzazione geologica/geotecnica** (§6.7.1-6.7.3);
- **criteri di progetto** (§6.7.4);
- **analisi e verifiche di sicurezza** (§6.7.5);
- **controllo e monitoraggio** (§6.7.6).

**Non è** uno strumento che calcola le verifiche o dimensiona l'opera: è un **supporto documentale** che inquadra
caratterizzazione, criteri, verifiche e monitoraggio. Complementa `stabilita-pendii-naturali-ntc` (§6.3),
`opere-materiali-sciolti-scavi-ntc` (§6.8) e `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifiche-opere-sotterraneo` | Analisi e verifiche SLU/SLE: stati limite GEO/STR/UPL/HYD, Approccio 1 con Comb. 1 (A1+M1+R1) e Comb. 2 (A2+M2+R2), γR = 1,0 per R1/R2, verifiche strutturali (§6.2.4.1.3) e idrauliche (§6.2.4.2), metodo osservazionale (§6.7.5) |
| `inquadra-caratterizzazione-progetto-monitoraggio` | Prescrizioni generali, caratterizzazione geologica/geotecnica, criteri di progetto e monitoraggio (§6.7.1-6.7.4, 6.7.6) |

## Punti chiave (verificati sul testo)

- **Ambito** (§6.7): gallerie, caverne, pozzi costruiti nel sottosuolo (scavo, stabilizzazione della cavità,
  rivestimento finale).
- **Prescrizioni generali** (§6.7.1): modello geologico e geotecnico; elementi da specificare/giustificare
  (tracciato, metodi di scavo, interventi di stabilizzazione e rivestimenti, imbocchi, acque, antifrana,
  sicurezza gas/cavità/venute d'acqua, materiali di risulta).
- **Caratterizzazione** (§6.7.2-6.7.3): modello geologico (litotipi, faglie, sismotettonica, franosità, carsismo,
  idrogeologia) e geotecnico (potenzialità spingenti/rigonfianti, pressioni interstiziali, metodo osservazionale).
- **Criteri di progetto** (§6.7.4): previsione quantitativa degli effetti indotti al contorno e in superficie
  (gallerie poco profonde in ambienti urbanizzati); dimensionamento dei rivestimenti; imbocchi; stabilità dei
  pendii in versante.
- **Verifiche** (§6.7.5): SLU **GEO** e **STR**, effetti sui manufatti esistenti, SLU idraulici **UPL** e **HYD**;
  stabilità di versanti e fronti agli imbocchi con §6.3 e §6.8; **Approccio 1** con **Comb. 1 (A1+M1+R1)** e
  **Comb. 2 (A2+M2+R2)**, **γR dei gruppi R1 e R2 pari all'unità (1,0)**; verifiche strutturali con valori
  caratteristici (§6.2.4.1.3) e idrauliche (§6.2.4.2); metodo osservazionale (convergenza radiale, deformazione
  longitudinale del fronte, spostamenti di superficie).
- **Monitoraggio** (§6.7.6): validità delle previsioni; comportamento di terreno/ammasso, rivestimenti e
  manufatti esistenti; fenomeni franosi (tensioni, spostamenti, pressioni interstiziali).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le verifiche né **dimensiona** l'opera, i rivestimenti o gli interventi di stabilizzazione;
  **non** definisce il modello geologico/geotecnico.
- **Non tratta** la **sicurezza dei lavoratori** in sotterraneo, le **macchine di scavo (TBM)** come prodotti né
  la **progettazione sismica** (Cap. 7).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.7 delle NTC 2018 e della Circolare applicativa.**
