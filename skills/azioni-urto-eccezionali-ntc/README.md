# azioni-urto-eccezionali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista/progettista di ponti da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle azioni
eccezionali da urto** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 3.6.3 (Urti)**:
classificazione, forze statiche equivalenti e punti di applicazione per urti da traffico veicolare (sotto e
sopra i ponti), ferroviario e (con rinvio) di imbarcazioni/aeromobili.

**Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi e **non sostituisce** il
progettista: fornisce le categorie (Tab. 3.6.II), le forze equivalenti (Tab. 3.6.III, formule [3.6.7]-[3.6.9])
e i punti/aree di applicazione.

## Target

Ingegneri strutturisti e progettisti di ponti che devono definire le azioni da urto per la verifica di
strutture esposte (piedritti/pile, elementi di sicurezza, strutture adiacenti a ferrovie, membrature in
autorimesse) secondo le NTC 2018 par. 3.6.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-urti-traffico-veicolare` | Classificazione (Tab. 3.6.II), forze equivalenti sotto ponti (Tab. 3.6.III, Fd,y=0,50 Fd,x, F=r Fd,x, carrelli F=5W) e sopra i ponti (100 kN) (§3.6.3.2-3.6.3.3) |
| `inquadra-urti-ferroviario-altri` | Urti da traffico ferroviario (forze per distanza d) e rinvio per imbarcazioni/aeromobili (§3.6.3.4-3.6.3.5) |

Nucleo: **classificazione** (categorie 1/2/3), **forze statiche equivalenti** sotto i ponti (Tab. 3.6.III;
Fd,y = 0,50·Fd,x; F = r·Fd,x; carrelli F = 5·W), **sopra i ponti** (100 kN) e da **traffico ferroviario** (per
distanza d) (§3.6.3).

## Relazione con altre skill

- Completa la famiglia delle **azioni eccezionali** (§3.6) con `resistenza-fuoco-strutture-ntc` (§3.6.1). È
  **distinta** da `azioni-traffico-ponti-stradali-ntc` (§5.1.3, carichi da traffico ordinari). Condivide la
  fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.3** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non riproduce** le **analisi di rischio** (ferrovia) né le procedure per **imbarcazioni/aeromobili** (Cap.
  12).
- **Non tratta** le **esplosioni** (§3.6.2) né l'**incendio** (§3.6.1, skill `resistenza-fuoco-strutture-ntc`).

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.6.3 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
