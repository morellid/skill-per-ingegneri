---
name: verifica-liquefazione-sismica-ntc
description: "Supporto documentale al progettista geotecnico/strutturale per inquadrare la verifica di stabilita' del sito nei confronti della liquefazione del terreno in condizioni sismiche secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.11.3.4. Aiuta a inquadrare: le generalita' e la definizione di liquefazione (perdita di resistenza al taglio o accumulo di deformazioni plastiche in terreni saturi prevalentemente sabbiosi, sollecitati da azioni cicliche e dinamiche in condizioni non drenate) e le conseguenze (interventi di consolidamento del terreno o trasferimento del carico a strati non suscettibili; per le fondazioni profonde valutazione della riduzione della capacita' portante e degli incrementi di sollecitazione nei pali); le condizioni di esclusione della verifica, che consentono di ometterla quando si verifica almeno una tra: accelerazione massima attesa al piano campagna in campo libero minore di 0,1 g, profondita' media stagionale della falda superiore a 15 m con piano campagna sub-orizzontale e fondazioni superficiali, sabbie pulite con resistenza penetrometrica normalizzata (N1)60 maggiore di 30 oppure qc1N maggiore di 180 (SPT e CPT normalizzate a una tensione efficace verticale di 100 kPa), oppure distribuzione granulometrica esterna ai fusi della Fig. 7.11.1 (a per Uc minore di 3,5 e b per Uc maggiore di 3,5); e i metodi di analisi quando nessuna condizione di esclusione e' soddisfatta, con il coefficiente di sicurezza definito dal rapporto tra la resistenza disponibile alla liquefazione e la sollecitazione indotta dal terremoto di progetto, valutato con metodologie di tipo storico-empirico e con adeguatezza del margine motivata dal progettista. Use when a geotechnical or structural designer must frame the soil liquefaction check under the Italian NTC 2018 par. 7.11.3.4; it is a documentary aid, does NOT compute the safety factor (CRR/CSR and correlations come from the literature and in-situ/laboratory tests, not from the NTC), does NOT design the ground-improvement works, and does NOT replace the geotechnical engineer. It is distinct from the static slope-stability skill (par. 6.3) and the geotechnical ULS skill (par. 6.2.4)."
license: MIT
area: strutture-geotecnica
title: "Verifica alla liquefazione sismica del terreno (NTC 2018 par. 7.11.3.4)"
summary: "Inquadra la verifica di liquefazione del terreno (NTC 2018 par. 7.11.3.4): definizione, condizioni di esclusione (a_max<0,1g; falda>15 m; (N1)60>30 o qc1N>180; granulometria fuori Fig. 7.11.1) e metodi di analisi (coeff. di sicurezza = resistenza/sollecitazione)."
normative_refs:
  - "NTC 2018 - par. 7.11.3.4: liquefazione; esclusione se a_max<0,1g / falda>15 m / (N1)60>30 o qc1N>180 / granulometria fuori Fig. 7.11.1; coeff. sicurezza = resistenza/sollecitazione"
  - "Rinvio (fuori scope): calcolo CRR/CSR con metodi di letteratura e prove in sito/laboratorio; § 7.11.3.5 (pendii sismica) e § 6.3 (pendii statica); § 3.2.2-3.2.3 (sottosuolo e azione sismica)"
version: 0.1.0-alpha
status: alpha
tags:
  - liquefazione
  - geotecnica-sismica
  - ntc-2018
  - relazione-geotecnica
  - fondazioni
---

# Verifica alla liquefazione sismica del terreno (NTC 2018 par. 7.11.3.4)

## Quando usare questa skill

Usala quando un **progettista geotecnico o strutturale** deve **inquadrare la verifica di stabilità del sito
nei confronti della liquefazione** in condizioni sismiche secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 7.11.3.4** (nell'ambito del par. 7.11 «Opere e sistemi geotecnici»):

- **generalità** e definizione del fenomeno (§7.11.3.4.1);
- **condizioni di esclusione** della verifica (§7.11.3.4.2);
- **metodi di analisi** e coefficiente di sicurezza (§7.11.3.4.3).

È un **supporto documentale**: inquadra i criteri di esclusione e la struttura della verifica; **non** calcola
il coefficiente di sicurezza (CRR/CSR: metodi storico-empirici da letteratura e prove), **non** progetta gli
interventi di consolidamento. È **distinta** da `stabilita-pendii-naturali-ntc` (§6.3, statica) e da
`verifiche-geotecniche-slu-ntc` (§6.2.4); usa `categorie-sottosuolo-topografiche-ntc` (§3.2.2) e
`spettro-risposta-ntc` (§3.2.3) per l'azione sismica di riferimento.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `valuta-esclusione-verifica-liquefazione` | Verifica se ricorre almeno una delle 4 condizioni di esclusione della verifica a liquefazione (§7.11.3.4.2), con la definizione e le conseguenze (§7.11.3.4.1) |
| `inquadra-metodo-coefficiente-sicurezza` | Inquadra i metodi di analisi quando nessuna condizione di esclusione è soddisfatta: coefficiente di sicurezza = resistenza/sollecitazione (§7.11.3.4.3) |

## Punti chiave (verificati sul testo/immagine)

- **Definizione** (§7.11.3.4.1): liquefazione = **perdita di resistenza al taglio** / **accumulo di
  deformazioni plastiche** in **terreni saturi prevalentemente sabbiosi**, sotto **azioni cicliche/dinamiche**
  in **condizioni non drenate**. Se suscettibile e rilevante → **consolidamento** o **trasferimento del
  carico** a strati non suscettibili; con **fondazioni profonde** → valutare **riduzione della capacità
  portante** e **incrementi nei pali**.
- **Esclusione** (§7.11.3.4.2, basta **una** circostanza):
  1. **a_max** al piano campagna in **campo libero < 0,1 g**;
  2. **falda** media stagionale **> 15 m** (piano campagna sub-orizzontale, **fondazioni superficiali**);
  3. **sabbie pulite** con **(N₁)₆₀ > 30** oppure **q_c1N > 180** (SPT/CPT normalizzate a **100 kPa**);
  4. **granulometria esterna** ai fusi di **Fig. 7.11.1(a)** per **U_c < 3,5** e **(b)** per **U_c > 3,5**.

  Se la **condizione 1 non è soddisfatta**, le indagini devono determinare i parametri per le condizioni 2, 3, 4.
- **Metodi di analisi** (§7.11.3.4.3): quando **nessuna** condizione è soddisfatta e vi sono **strati estesi/
  lenti spesse di sabbie sciolte sotto falda**, valutare il **coefficiente di sicurezza** alle profondità dei
  terreni liquefacibili. Con metodi **storico-empirici**: **coeff. di sicurezza = resistenza disponibile alla
  liquefazione / sollecitazione indotta dal terremoto di progetto**; resistenza da **prove in sito o cicliche
  di laboratorio**; sollecitazione da **a_max alla profondità di interesse**. **Margine motivato dal
  progettista**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.11.3.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 284-285 (pedici e disuguaglianze).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** il coefficiente di sicurezza alla liquefazione (rapporti **CRR/CSR**, correlazioni con
  **(N₁)₆₀ / q_c1N**, magnitudo): sono **metodi di letteratura e prove**, non riprodotti dalle NTC.
- **Non progetta** gli **interventi di consolidamento** del terreno né le fondazioni profonde; **non** valuta
  la riduzione di capacità portante o gli incrementi nei pali.
- **Non tratta** la **stabilità dei pendii** sismica (§7.11.3.5) o statica (§6.3, → skill dedicata), né
  l'azione sismica di dettaglio (§3.2.3) e le categorie di sottosuolo (§3.2.2, → skill dedicate).

**La skill è un supporto documentale: non sostituisce il progettista geotecnico né la lettura del par. 7.11.3.4 delle NTC 2018 e delle metodologie di verifica alla liquefazione adottate.**
