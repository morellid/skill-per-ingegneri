---
name: azioni-urto-eccezionali-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento delle azioni eccezionali da urto secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.6.3 (Urti). Aiuta a inquadrare la classificazione delle azioni (Tab. 3.6.II: categoria 1 effetti trascurabili, 2 localizzati, 3 generalizzati; le azioni si applicano agli elementi con conseguenze di categoria 2 e 3); gli urti da traffico veicolare sotto ponti o altre strutture (le due componenti non simultanee parallela Fd,x e ortogonale Fd,y uguale a 0,50 Fd,x [3.6.7]; le forze statiche equivalenti della Tab. 3.6.III con 1000 kN per autostrade e strade extraurbane, 750 kN per le strade locali, 500 kN per le strade urbane, 50 kN per le automobili e 150 kN per i veicoli merci oltre 3,5 t nelle aree di parcheggio e autorimesse; i punti di applicazione sulle membrature verticali a 0,5 m per le automobili o 1,25 m sopra la superficie di marcia; per gli elementi orizzontali sopra la strada F uguale a r per Fd,x [3.6.8] con r uguale a 1,0 fino a 5 m di altezza del sottovia, decrescente linearmente da 1,0 a 0 fra 5 e 6 m e nullo oltre 6 m; per i carrelli elevatori F uguale a 5 W [3.6.9]); gli urti da traffico veicolare sopra i ponti con la forza orizzontale equivalente di 100 kN sugli elementi di sicurezza; gli urti da traffico ferroviario con le azioni statiche equivalenti in funzione della distanza d dall'asse del binario (4000 e 1500 kN per d fino a 5 m, 2000 e 750 kN per d fra 5 e 15 m, zero oltre 15 m, applicate a 1,80 m dal piano del ferro); e il rinvio per gli urti di imbarcazioni e aeromobili (Cap. 12). Use when a structural designer must frame the accidental impact actions under the Italian NTC 2018 par. 3.6.3; it is a documentary aid and does NOT compute the internal forces nor size or verify the members or their protection systems, does NOT perform the risk analysis (railway) nor the ship/aircraft procedures, does NOT cover explosions (par. 3.6.2) nor fire (par. 3.6.1, dedicated skill), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Azioni eccezionali da urto (NTC 2018 par. 3.6.3)"
summary: "Inquadra le azioni eccezionali da urto (NTC 2018 par. 3.6.3): classificazione (Tab. 3.6.II), forze statiche equivalenti sotto i ponti (Tab. 3.6.III, Fd,y=0,50 Fd,x, F=r Fd,x, carrelli F=5W), sopra i ponti (100 kN) e da traffico ferroviario (per distanza d)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.6.3 Urti: forze equivalenti sotto ponti (Tab. 3.6.III), Fd,y=0,50 Fd,x [3.6.7], F=r Fd,x [3.6.8], carrelli F=5W [3.6.9], sopra ponti 100 kN, classi Tab. 3.6.II"
  - "NTC 2018 - par. 3.6.3.4 urti da traffico ferroviario (4000/1500 kN per d<=5 m; 2000/750 kN per 5<d<=15 m; 0 oltre; a 1,80 m dal ferro); par. 3.6.3.5 imbarcazioni/aeromobili (rinvio Cap. 12)"
version: 0.1.0-alpha
status: alpha
tags:
  - azioni-da-urto
  - azioni-eccezionali
  - ntc-2018
  - ponti
  - collisioni
---

# Azioni eccezionali da urto (NTC 2018 par. 3.6.3)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le azioni eccezionali da urto** su strutture
esposte (piedritti/pile sotto ponti, elementi di sicurezza sui ponti, strutture adiacenti a ferrovie,
membrature in autorimesse) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.3 (Urti)**:

- **classificazione** delle azioni (Tab. 3.6.II) (§3.6.3.2);
- **urti da traffico veicolare** sotto e sopra i ponti (§3.6.3.3);
- **urti da traffico ferroviario** (§3.6.3.4);
- **urti di imbarcazioni/aeromobili** (rinvio) (§3.6.3.5).

**Non è** uno strumento che calcola le sollecitazioni o verifica gli elementi: è un **supporto documentale**
che inquadra categorie, forze statiche equivalenti e punti di applicazione. Completa la famiglia delle **azioni
eccezionali** (§3.6) insieme a `resistenza-fuoco-strutture-ntc` (§3.6.1); è distinta dalle azioni da traffico
dei ponti (§5.1.3).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-urti-traffico-veicolare` | Classificazione (Tab. 3.6.II), forze equivalenti sotto ponti (Tab. 3.6.III, Fd,y=0,50 Fd,x, F=r Fd,x, carrelli F=5W) e sopra i ponti (100 kN) (§3.6.3.2-3.6.3.3) |
| `inquadra-urti-ferroviario-altri` | Urti da traffico ferroviario (forze per distanza d) e rinvio per imbarcazioni/aeromobili (§3.6.3.4-3.6.3.5) |

## Punti chiave (verificati sul testo)

- **Classificazione** (Tab. 3.6.II): categoria **1** trascurabili, **2** localizzati, **3** generalizzati; si
  applicano per **categoria 2 e 3**.
- **Sotto ponti** (§3.6.3.3.1): **Fd,y = 0,50·Fd,x** [3.6.7] (non simultanee); Tab. 3.6.III: **1000** kN
  (autostrade/extraurbane), **750** (locali), **500** (urbane), **50** (automobili), **150** (merci > 3,5 t);
  applicazione a **0,5 m** (automobili) o **1,25 m** sopra la superficie.
- **Elementi orizzontali** (§3.6.3.3.1): **F = r·Fd,x** [3.6.8], r = **1,0** fino a 5 m, **1,0→0** tra 5 e 6 m,
  **0** oltre 6 m; intradosso a 10°, area 0,25×0,25 m.
- **Carrelli elevatori** (§3.6.3.3.1): **F = 5·W** [3.6.9] a 0,75 m dal piano di calpestio.
- **Sopra i ponti** (§3.6.3.3.2): forza orizzontale equivalente **100 kN** sugli elementi di sicurezza.
- **Ferroviario** (§3.6.3.4): **4000/1500 kN** (d ≤ 5 m), **2000/750 kN** (5 < d ≤ 15 m), **0** (d > 15 m), a
  1,80 m dal piano del ferro, non simultanee.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.3** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non riproduce** le **analisi di rischio** (ferrovia) né le procedure per **imbarcazioni/aeromobili** (Cap.
  12).
- **Non tratta** le **esplosioni** (§3.6.2) né l'**incendio** (§3.6.1, skill `resistenza-fuoco-strutture-ntc`);
  **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.6.3 delle NTC 2018 e della Circolare applicativa.**
