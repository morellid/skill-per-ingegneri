---
name: stabilita-pendii-naturali-ntc
description: "Supporto documentale al progettista geotecnico e al geologo per l'inquadramento dello studio e della verifica di stabilita' dei pendii naturali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.3. Aiuta a inquadrare l'ambito (pendii naturali, anche in condizioni sismiche con rinvio al paragrafo 7.11.3.5, e interventi di stabilizzazione); le prescrizioni generali (osservazioni e rilievi di superficie, notizie storiche, movimenti in atto, dati idrogeologici, verifiche basate su specifiche indagini geotecniche); la modellazione geologica e geotecnica del pendio (rilievo plano-altimetrico esteso a monte e valle, successione stratigrafica, pressioni interstiziali, superficie o superfici di scorrimento, numero minimo di verticali di indagine, modello geotecnico di sottosuolo del paragrafo 6.2.2); la verifica di sicurezza con il coefficiente di sicurezza pari al rapporto fra la resistenza al taglio disponibile tau_f e la tensione di taglio agente tau lungo la superficie di scorrimento, impiegando i parametri geotecnici e le azioni al loro valore caratteristico (a differenza degli altri interventi geotecnici, per i pendii naturali NON si applicano i coefficienti parziali A1/A2, M ed R), con le verifiche lungo le superfici accertate per i pendii in frana o la ricerca della superficie critica a cui corrisponde il grado di sicurezza piu' basso negli altri casi, assumendo le condizioni piu' sfavorevoli per le pressioni interstiziali e con il margine di sicurezza accettabile giustificato dal progettista in base al livello di conoscenze, all'affidabilita' dei dati, al modello di calcolo e alle conseguenze di un'eventuale frana; gli interventi di stabilizzazione; e i controlli e il monitoraggio (spostamenti, pressioni interstiziali, soglie di attenzione e di allarme). Use when a geotechnical designer or geologist must frame the stability study and verification of natural slopes under the Italian NTC 2018 par. 6.3; it is a documentary aid and does NOT compute the factor of safety nor run the analyses, does NOT define the geological/geotechnical model nor design the stabilization works, does NOT cover the seismic slope stability (par. 7.11.3.5) nor the earthworks/excavation fronts (par. 6.8), and does NOT replace the designer/geologist or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Stabilità dei pendii naturali (NTC 2018 par. 6.3)"
summary: "Inquadra lo studio e la verifica di stabilita' dei pendii naturali (NTC 2018 par. 6.3): modellazione geologica/geotecnica, coefficiente di sicurezza F = tau_f/tau su valori caratteristici (senza coefficienti parziali), superficie critica/di frana, interventi e monitoraggio."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.3: F = tau_f/tau su valori caratteristici (no coefficienti parziali A1/A2/M/R), superficie critica o accertata (frana), margine dal progettista"
  - "NTC 2018 - par. 6.3.1-6.3.3 (indagini, modellazione geologica/geotecnica, modello 6.2.2), 6.3.5-6.3.6 (interventi, monitoraggio con soglie di attenzione/allarme); rinvio par. 7.11.3.5 (sismico)"
version: 0.1.0-alpha
status: alpha
tags:
  - stabilita-dei-pendii
  - geotecnica
  - ntc-2018
  - coefficiente-di-sicurezza
  - frane
---

# Stabilità dei pendii naturali (NTC 2018 par. 6.3)

## Quando usare questa skill

Usala quando un **progettista geotecnico** o un **geologo** deve **inquadrare lo studio e la verifica di
stabilità di un pendio naturale** (versante) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.3**:

- **prescrizioni generali** e **indagini** (§6.3.1);
- **modellazione geologica e geotecnica** (§6.3.2-6.3.3);
- **verifiche di sicurezza** (§6.3.4);
- **interventi di stabilizzazione** e **monitoraggio** (§6.3.5-6.3.6).

**Non è** uno strumento che calcola il coefficiente di sicurezza o esegue le analisi: è un **supporto
documentale** che inquadra criteri, modellazione e verifica. Complementa `opere-sostegno-ntc` (§6.5),
`tiranti-ancoraggio-ntc` (§6.6) e `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-stabilita-pendio` | Verifica di sicurezza: F = τf/τ su valori caratteristici (senza coefficienti parziali), superfici accertate/critiche, pressioni interstiziali, margine giustificato dal progettista (§6.3.4) |
| `inquadra-indagini-interventi-monitoraggio` | Prescrizioni e indagini, modellazione geologica/geotecnica, interventi di stabilizzazione e monitoraggio (§6.3.1-6.3.3, 6.3.5-6.3.6) |

## Punti chiave (verificati sul testo)

- **Ambito** (§6.3): pendii naturali, anche **sismici** (rinvio §7.11.3.5); interventi di stabilizzazione.
- **Indagini** (§6.3.1): rilievi di superficie, notizie storiche, movimenti in atto; verifiche su **specifiche
  indagini geotecniche**.
- **Modellazione** (§6.3.2-6.3.3): modello **geologico** e **geotecnico** (rilievo plano-altimetrico,
  stratigrafia, pressioni interstiziali, superfici di scorrimento, verticali minime, modello §6.2.2).
- **Verifica** (§6.3.4): **F = τf/τ** (resistenza al taglio disponibile / tensione agente) lungo la superficie
  di scorrimento, con **parametri e azioni al valore caratteristico**. **A differenza** di muri/fondazioni/
  tiranti, **non** si applicano i coefficienti parziali A1/A2, M, R. Pendii **in frana** → superfici
  accertate; **altri casi** → ricerca della **superficie critica** (grado di sicurezza più basso); pressioni
  interstiziali nelle **condizioni più sfavorevoli**. **Margine giustificato dal progettista** (conoscenze,
  dati, modello, conseguenze).
- **Interventi/monitoraggio** (§6.3.5-6.3.6): entità del miglioramento, altri meccanismi di collasso;
  monitoraggio di spostamenti e pressioni interstiziali, **soglie di attenzione e di allarme**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.3** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** il coefficiente di sicurezza né **esegue** le verifiche (equilibrio limite/metodi numerici);
  **non** definisce il modello geologico/geotecnico né **progetta** gli interventi.
- **Non tratta** la stabilità dei pendii in **condizioni sismiche** (§7.11.3.5) né le **opere in materiali
  sciolti / fronti di scavo** (§6.8).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/geologo, né la lettura del par. 6.3 delle NTC 2018 e della Circolare applicativa.**
