# azioni-traffico-ponti-ferroviari-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista di ponti da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle azioni da
traffico sui ponti ferroviari** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 5.2.2**: modelli
di carico verticali, coefficiente di adattamento α, effetti dinamici e azioni orizzontali.

**Non esegue** le combinazioni, l'**analisi dinamica** con treni reali né le **verifiche** e **non
sostituisce** il progettista: fornisce i modelli di carico (LM71, SW/0, SW/2, treno scarico, marciapiedi), i
coefficienti Φ2/Φ3 e le azioni orizzontali. È **distinta** dalla skill sui **ponti stradali** (§5.1.3).

## Target

Ingegneri strutturisti che progettano ponti ferroviari e devono definire le azioni da traffico secondo le NTC
2018 par. 5.2.2.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-modelli-carico-verticali-ferroviari` | Modelli di carico verticali LM71, SW/0, SW/2, treno scarico, marciapiedi e coefficiente di adattamento α (§5.2.2.2.1-5.2.2.2.2) |
| `inquadra-effetti-dinamici-azioni-orizzontali` | Effetti dinamici (Φ2/Φ3, L_φ) e azioni orizzontali: centrifuga, serpeggio, avviamento/frenatura (§5.2.2.2.3, §5.2.2.3) |

Nucleo: **LM71** (4×250 kN a 1,60 m + 80 kN/m), **SW/0** (133 kN/m) e **SW/2** (150 kN/m), **treno scarico**
(10 kN/m), **α**, **Φ2 = 1,44/(√L_φ − 0,2) + 0,82** / **Φ3 = 2,16/(√L_φ − 0,2) + 0,73**, e azioni orizzontali
(centrifuga, **serpeggio** 100 kN, **avviamento/frenatura**).

## Relazione con altre skill

- Copre le **azioni da traffico dei ponti ferroviari** (§5.2.2). È **distinta** da
  `azioni-traffico-ponti-stradali-ntc` (§5.1.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 5.2.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 168 (LM71) e 171 (Φ).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le **combinazioni** delle azioni, l'**analisi dinamica** con treni reali (V > 200 km/h o
  tipologie non convenzionali) né le **verifiche** (SLU/SLE, fatica, interazione statica binario-struttura).
- **Non riproduce** la **Tab. 5.2.II** completa (L_φ per ciascun elemento) né i criteri progettuali/manutentivi
  (§5.2.1).
- **Non** riguarda i **ponti stradali** (→ skill `azioni-traffico-ponti-stradali-ntc`); non sostituisce il
  progettista strutturale.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 5.2.2 delle NTC 2018 e delle relative specifiche tecniche ferroviarie.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
