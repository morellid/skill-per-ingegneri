# AGENTS.md - azioni-traffico-ponti-ferroviari-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle azioni da traffico sui ponti
ferroviari** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 5.2.2**: modelli di carico verticali
(LM71, SW/0, SW/2, treno scarico, marciapiedi), coefficiente di adattamento α, effetti dinamici (Φ2/Φ3, L_φ)
e azioni orizzontali (centrifuga, serpeggio, avviamento/frenatura). Target: ingegneri strutturisti di ponti.

**È una skill documentale per il tecnico**: fornisce i modelli di carico, i coefficienti e le azioni; **non**
esegue le combinazioni, l'analisi dinamica con treni reali né le verifiche.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre il compito di **definizione delle azioni da traffico dei ponti
ferroviari** (§5.2.2). È **distinta** da `azioni-traffico-ponti-stradali-ntc` (§5.1.3, ponti stradali):
modelli di carico (LM71/SW vs schemi di carico stradali), coefficienti e azioni sono completamente diversi.
Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori
scope: i criteri progettuali/manutentivi (§5.2.1), le combinazioni, l'analisi dinamica con treni reali, la
Tab. 5.2.II completa (L_φ) e le verifiche (SLU/SLE, fatica, interazione statica binario-struttura).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-5-2**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 5.2.2 (pagine PDF 167-174) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
  150`) delle pagine PDF 168 (LM71) e 171 (Φ) per valori dei carichi, pedici e formule.

Trascrizione in `references/fonti/ntc2018-par-5-2.md`; estratto operativo in
`references/estratti/azioni-ferroviari-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **LM71**: 4 assi da 250 kN a interasse 1,60 m + 80 kN/m; α = 1,1.
- **SW/0** (133 kN/m, a 15,0, c 5,3; α 1,1) e **SW/2** (150 kN/m, a 25,0, c 7,0; α 1,0) - Tab. 5.2.I; treno
  scarico 10 kN/m; marciapiedi 10 kN/m².
- **Φ2 = 1,44/(√L_φ − 0,2) + 0,82** (1,00-1,67) [5.2.6]; **Φ3 = 2,16/(√L_φ − 0,2) + 0,73** (1,00-2,00) [5.2.7].
- **Serpeggio** 100 kN; **avviamento** 33 kN/m·L ≤ 1000 kN; **frenatura** 20 kN/m·L ≤ 6000 kN (LM71/SW0),
  35 kN/m·L (SW/2); forza centrifuga [5.2.9]-[5.2.10].

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le combinazioni delle azioni, l'analisi dinamica con treni reali (V > 200 km/h) né le
  verifiche (SLU/SLE, fatica, interazione binario-struttura).
- Non **riprodurre** la Tab. 5.2.II completa (L_φ per ogni elemento) né i criteri progettuali/manutentivi
  (§5.2.1); non trattare i **ponti stradali** (→ skill §5.1.3).

### Cosa fare
- Fornire i modelli di carico, il coefficiente α, i coefficienti Φ e le azioni orizzontali, sempre con rinvio
  al paragrafo/tabella/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 5.2.2. Verificare sull'immagine i valori LM71 (250 kN, 1,60 m, 80 kN/m), la Tab. 5.2.I
(SW) e le formule Φ2/Φ3 (√L_φ − 0,2).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista di ponti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #448)
- Task files: 2 (`inquadra-modelli-carico-verticali-ferroviari.md`, `inquadra-effetti-dinamici-azioni-orizzontali.md`)
- Esempi: 2 (valori del modello LM71 e dei modelli SW con α; coefficiente dinamico Φ2/Φ3 per una trave
  appoggiata data L_φ)
