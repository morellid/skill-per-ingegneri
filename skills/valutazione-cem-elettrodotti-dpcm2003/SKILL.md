---
name: valutazione-cem-elettrodotti-dpcm2003
description: "Supporto alla verifica del rispetto dei limiti di esposizione ai campi elettrici e magnetici a frequenza di rete (50 Hz) generati dagli elettrodotti, ai sensi del D.P.C.M. 8 luglio 2003 (in attuazione della legge quadro 36/2001). Aiuta a distinguere le tre grandezze di riferimento e i relativi valori: limite di esposizione (100 microtesla per l'induzione magnetica e 5 kV/m per il campo elettrico, come valori efficaci - art. 3 c.1), valore di attenzione (10 microtesla, mediana dei valori nell'arco delle 24 ore, nelle aree gioco per l'infanzia, negli ambienti abitativi e scolastici e nei luoghi con permanenza non inferiore a quattro ore - art. 3 c.2) e obiettivo di qualita' (3 microtesla, mediana 24 ore, per la progettazione di nuovi elettrodotti in corrispondenza di tali aree e di nuove aree in prossimita' di linee esistenti - art. 4). Guida inoltre a inquadrare le tecniche di misura (norma CEI 211-6 - art. 5) e il quadro delle fasce di rispetto (riferimento all'obiettivo di qualita' e alla portata in corrente in servizio normale ex CEI 11-60 - art. 6). Use when an engineer must check whether a building/area near a 50 Hz power line complies with the Italian population-protection limits, or must frame a fasce di rispetto assessment; it is a documentary/consultation aid and does NOT compute the Distanza di Prima Approssimazione (DPA), whose calculation methodology is delegated to APAT/ISPRA and approved by DM 29/5/2008 (not reproduced), does not replace field measurements by ARPA/qualified technicians and does not cover high-frequency sources (radio base stations)."
license: MIT
area: ambiente-territorio-mobilita
title: "Verifica limiti CEM elettrodotti 50 Hz (D.P.C.M. 8/7/2003)"
summary: "Verifica dei limiti CEM a 50 Hz degli elettrodotti (DPCM 8/7/2003): limite 100 uT / 5 kV/m, valore di attenzione 10 uT, obiettivo di qualita' 3 uT, tecniche di misura (CEI 211-6) e quadro fasce di rispetto. Non calcola la DPA (metodologia DM 29/5/2008)."
normative_refs:
  - "D.P.C.M. 8 luglio 2003 (elettrodotti 50 Hz) - artt. 1-8 e Allegato A"
  - "Legge 22 febbraio 2001, n. 36 (legge quadro protezione da esposizioni a CEM)"
  - "DM Ambiente 29/5/2008 (metodologia fasce di rispetto/DPA - citato, non riprodotto)"
version: 0.1.0-alpha
status: alpha
tags:
  - cem
  - elettrodotti
  - dpcm-8-7-2003
  - campi-elettromagnetici
  - fasce-di-rispetto
---

# Verifica limiti CEM elettrodotti 50 Hz (D.P.C.M. 8/7/2003)

## Quando usare questa skill

Usala quando devi **verificare il rispetto dei limiti** di esposizione della
popolazione ai **campi elettrici e magnetici a 50 Hz** generati da **elettrodotti**
(linee, sottostazioni, cabine di trasformazione) ai sensi del **D.P.C.M. 8 luglio
2003** (attuazione della legge quadro 36/2001), tipicamente per:

- valutare un **edificio/area sensibile** in prossimita' di una linea elettrica;
- inquadrare una **fascia di rispetto** in fase urbanistica o progettuale;
- distinguere quale **grandezza di riferimento** si applica al caso.

## Le tre grandezze e i valori (da non confondere)

| Grandezza | Valore | Dove/quando si applica | Art. |
|---|---|---|---|
| **Limite di esposizione** | **100 µT** (induzione magnetica) e **5 kV/m** (campo elettrico), valori efficaci | Sempre, esposizione della popolazione | 3 c.1 |
| **Valore di attenzione** | **10 µT** (mediana 24 h) | Aree gioco per l'infanzia, ambienti abitativi e scolastici, luoghi con permanenza >= 4 ore giornaliere | 3 c.2 |
| **Obiettivo di qualita'** | **3 µT** (mediana 24 h) | Progettazione di **nuovi** elettrodotti presso quelle aree, e nuove aree/insediamenti in prossimita' di linee esistenti | 4 |

- La **mediana nelle 24 ore** si riferisce alle normali condizioni di esercizio.
- Le **tecniche di misura** sono quelle della norma **CEI 211-6** (art. 5); le
  procedure di determinazione sono a cura del sistema agenziale **APAT-ARPA**.

## Fasce di rispetto (quadro)

- Per la determinazione delle **fasce di rispetto** si fa riferimento all'**obiettivo
  di qualita' (3 µT)** e alla **portata in corrente in servizio normale** della linea
  (norma **CEI 11-60**), dichiarata dal gestore (art. 6 c.1).
- La **metodologia di calcolo** delle fasce e delle **Distanze di Prima
  Approssimazione (DPA)** e' **delegata all'APAT** (poi ISPRA) e approvata con **DM
  29/5/2008**: vedi "Cosa NON fa".

## Cosa NON fa (limiti)

- **Non calcola la DPA** ne' l'ampiezza numerica delle fasce di rispetto: la
  **metodologia** e' quella del **DM 29/5/2008** (delegato dall'art. 6 c.2), **non
  riprodotta**. La skill fornisce il quadro e la verifica dei limiti, non il calcolo.
- **Non sostituisce le misure** in campo: la determinazione dei livelli e la verifica
  spettano ad **ARPA/tecnici qualificati** con la strumentazione e le procedure CEI.
- **Non copre le alte frequenze** (stazioni radio base, impianti RF): per quelle vedi
  `valutazione-cem-srb-art-87-cce`.
- Non tratta l'**esposizione professionale** dei lavoratori (esclusa dall'art. 1 c.2;
  disciplina del Titolo VIII Capo IV D.Lgs 81/2008).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-limite-applicabile`](tasks/inquadra-limite-applicabile.md) | Dato il sito e l'uso (esistente vs nuovo, tipo di area/permanenza), individua quale grandezza si applica (limite/attenzione/qualita') e il relativo valore |
| [`imposta-verifica-fasce`](tasks/imposta-verifica-fasce.md) | Struttura la richiesta dei dati al gestore (portata in corrente CEI 11-60, geometria) e imposta la verifica rispetto all'obiettivo di qualita', rinviando al DM 29/5/2008 per il calcolo DPA |

## Riferimenti normativi

- **D.P.C.M. 8 luglio 2003** (elettrodotti 50 Hz) - artt. 1-8 e Allegato A (limiti,
  valori di attenzione, obiettivo di qualita', misura, fasce di rispetto, definizioni).
- **Legge 22 febbraio 2001, n. 36** (legge quadro sulla protezione dalle esposizioni a
  campi elettrici, magnetici ed elettromagnetici) - fonte primaria delegante.
- **DM Ambiente 29/5/2008** (metodologia fasce di rispetto/DPA) - **citato, non
  riprodotto**.

Dettaglio in `references/sources.yaml`, `references/fonti/dpcm-8-7-2003.md`,
`references/estratti/limiti-cem-checklist.md`.

## Avvertenza

Skill di **supporto documentale/di consultazione**: i valori di campo effettivi, la
loro misura e la determinazione delle fasce di rispetto dipendono da dati del gestore,
dalla geometria della linea e da misure/metodologie ufficiali.
La skill **non sostituisce** ARPA, il tecnico misuratore, ne' il calcolo delle fasce di rispetto secondo il DM 29/5/2008.
