---
name: opere-materiali-sciolti-scavi-ntc
description: "Supporto documentale al progettista geotecnico per l'inquadramento della progettazione e della verifica delle opere di materiali sciolti (rilevati, argini di difesa, rinfianchi, rinterri, terrapieni, colmate) e dei fronti di scavo secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.8. Aiuta a inquadrare l'ambito (manufatti di materiali sciolti e opere con funzioni di drenaggio, filtro, transizione, fondazione, tenuta o protezione; esclusi gli sbarramenti di ritenuta idraulica); i criteri generali di progetto (requisiti prestazionali, terreni di fondazione, scelta e qualificazione dei materiali naturali o di provenienza diversa, posa in opera con spessore massimo degli strati, grado di compattazione e deformabilita') (6.8.1); le verifiche di sicurezza allo stato limite ultimo con la condizione 6.2.1 e la Combinazione 2 (A2+M2+R2) dell'Approccio 1, impiegando i coefficienti parziali delle Tabelle 6.2.I (azioni), 6.2.II (parametri geotecnici) e 6.8.I (coefficiente parziale sulle resistenze gamma_R uguale a 1,1 per il gruppo R2), con lo studio della stabilita' globale dell'insieme manufatto-terreno di fondazione nelle diverse fasi costruttive, a fine costruzione e in esercizio, le verifiche locali sugli elementi di rinforzo, l'influenza dei manufatti su pendii e, per le opere di ritenuta idraulica, la stabilita' dei paramenti con attenzione al sifonamento e all'erosione (6.8.2); le verifiche di esercizio sugli spostamenti (6.8.3); gli aspetti costruttivi (posa in strati, geosintetici certificati secondo norme europee armonizzate) (6.8.4); i controlli e il monitoraggio (spostamenti e pressioni interstiziali) (6.8.5); e i fronti di scavo (indagini geotecniche in funzione di profondita', ampiezza, destinazione e carattere permanente o provvisorio; profilo di scavo; influenza su pendii, pressioni interstiziali e costruzioni preesistenti; obbligo di una struttura di sostegno delle pareti per scavi in trincea a fronte verticale di altezza superiore ai 2 m con permanenza di personale o in prossimita' di manufatti esistenti, con verifiche SLU e SLE) (6.8.6). Use when a geotechnical designer must frame the design or verification of earthworks (embankments, levees, fills) or excavation fronts under the Italian NTC 2018 par. 6.8; it is a documentary aid and does NOT compute the verifications nor size the earthwork/excavation, does NOT cover water-retaining embankments (earth dams), the workers' safety in excavations (D.Lgs 81/2008 Title IV) nor the seismic design, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Opere di materiali sciolti e fronti di scavo (NTC 2018 par. 6.8)"
summary: "Inquadra progetto e verifica delle opere di materiali sciolti (rilevati, argini, terrapieni) e dei fronti di scavo (NTC 2018 par. 6.8): SLU in Combinazione 2 (A2+M2+R2), Tab. 6.8.I gamma_R = 1,1, stabilita' globale, sostegno per fronti verticali oltre 2 m con personale."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.8: verifiche SLU in Combinazione 2 (A2+M2+R2), Tab. 6.2.I/6.2.II/6.8.I (gamma_R = 1,1 per R2), stabilita' globale manufatto-terreno nelle diverse fasi"
  - "NTC 2018 - par. 6.8.6 fronti di scavo: struttura di sostegno per trincee a fronte verticale > 2 m con personale o vicino a manufatti (verifiche SLU/SLE); rinvio par. 6.2.2/6.2.4"
version: 0.1.0-alpha
status: alpha
tags:
  - materiali-sciolti
  - fronti-di-scavo
  - geotecnica
  - ntc-2018
  - rilevati
---

# Opere di materiali sciolti e fronti di scavo (NTC 2018 par. 6.8)

## Quando usare questa skill

Usala quando un **progettista geotecnico** deve **inquadrare la progettazione o la verifica** di un'**opera in
materiali sciolti** (rilevato, argine di difesa, terrapieno, colmata, rinterro) o di un **fronte di scavo**
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.8**:

- **criteri generali di progetto** (§6.8.1);
- **verifiche di sicurezza SLU** e **SLE** (§6.8.2-6.8.3);
- **aspetti costruttivi**, **controlli e monitoraggio** (§6.8.4-6.8.5);
- **fronti di scavo** (§6.8.6).

**Non è** uno strumento che calcola le verifiche o dimensiona l'opera: è un **supporto documentale** che inquadra
criteri, verifiche e aspetti costruttivi. Complementa `opere-sostegno-ntc` (§6.5), `stabilita-pendii-naturali-ntc`
(§6.3) e `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-materiali-sciolti` | Criteri, verifiche SLU (Combinazione 2 A2+M2+R2, Tab. 6.8.I gamma_R = 1,1, stabilità globale nelle varie fasi), SLE, aspetti costruttivi e monitoraggio dei manufatti di materiali sciolti (§6.8.1-6.8.5) |
| `inquadra-fronti-scavo` | Indagini, profilo di scavo e verifiche dei fronti di scavo; struttura di sostegno per fronti verticali > 2 m con personale o in prossimità di manufatti (§6.8.6) |

## Punti chiave (verificati sul testo)

- **Ambito** (§6.8): manufatti di materiali sciolti (rilevati, argini di difesa, rinfianchi, rinterri,
  terrapieni, colmate, scavi per piazzali/trincee) e opere con funzioni di drenaggio/filtro/transizione/
  fondazione/tenuta/protezione. **Esclusi** gli sbarramenti di ritenuta idraulica (dighe in terra).
- **Verifiche SLU** (§6.8.2): condizione [6.2.1] con valori di progetto; **Combinazione 2 (A2+M2+R2)**
  dell'Approccio 1; coefficienti Tab. 6.2.I (azioni), 6.2.II (parametri), **Tab. 6.8.I (γR = 1,1, R2)**.
  **Stabilità globale** manufatto-terreno nelle **diverse fasi costruttive**, a **fine costruzione** e in
  **esercizio**; verifiche locali sugli elementi di rinforzo; ritenuta idraulica → sifonamento/erosione.
- **SLE** (§6.8.3): spostamenti del manufatto e del terreno, compatibili con funzionalità e manufatti adiacenti.
- **Costruttivi/monitoraggio** (§6.8.4-6.8.5): posa in strati; geosintetici certificati; monitoraggio di
  spostamenti e pressioni interstiziali.
- **Fronti di scavo** (§6.8.6): indagini (profondità, ampiezza, destinazione, permanente/provvisorio); verifica
  analoga ai materiali sciolti; **struttura di sostegno** per **scavi in trincea a fronte verticale > 2 m con
  permanenza di personale** o **in prossimità di manufatti** (verifiche SLU e SLE); azioni nelle condizioni più
  sfavorevoli.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.8** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; Tab. 6.8.I e soglia dei 2 m verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le verifiche né **dimensiona** il manufatto, il fronte di scavo o la struttura di sostegno;
  **non** definisce il modello geotecnico.
- **Non tratta** gli **sbarramenti di ritenuta idraulica** (dighe in terra), la **sicurezza dei lavoratori**
  negli scavi (**D.Lgs 81/2008 Titolo IV**, skill `sicurezza-scavi-fondazioni-dlgs81`) né le **terre e rocce da
  scavo** come sottoprodotti (DPR 120/2017).
- **Non riproduce** la **Circolare 21/1/2019 n. 7** né tratta la progettazione sismica (Cap. 7).

**La skill è un supporto documentale: non sostituisce il progettista geotecnico, né la lettura del par. 6.8 delle NTC 2018 e della Circolare applicativa.**
