# Task: Simulazione semplificata di autoconsumo condiviso e flussi economici

Stima in modo trasparente e parametrico l'**energia condivisa annua** della CACER, la **TIP** ex art. 7 DM 7/12/2023, la **TR** del TIAD ARERA 727/2022/R/eel e l'eventuale **contributo PNRR** ex art. 8 DM 7/12/2023.

## Obiettivo

Produrre una **scheda di simulazione** che riporti, in maniera trasparente:

- ipotesi di calcolo (potenza, producibilita', profili, fattore di condivisione);
- energia immessa annua, energia prelevata annua, energia condivisa stimata;
- TIP stimata (parte fissa per fascia di potenza + indicazione di applicabilita' del correttivo zonale);
- TR stimata (sulla base del livello di tensione e del valore vigente ARERA, da verificare);
- contributo PNRR stimato, se Comune < 5.000 ab.;
- riduzione TIP per cumulo PNRR, se applicabile;
- avvertenze esplicite sui limiti.

La simulazione e' **parametrica**: il calcolo definitivo e' del GSE su dati di misura.

## Input richiesti

### Impianto/i FER
- Tecnologia (FV, eolico, idro, biomassa).
- Potenza nominale (kW) per ciascun impianto.
- Producibilita' attesa (kWh/kWp/anno) per impianti FV: tipicamente 1.000-1.300 a seconda della latitudine; per altre tecnologie va dichiarato il fattore di carico annuo.
- Livello di tensione di connessione (BT / MT).
- Comune e popolazione (per verifica condizione PNRR).

### Profilo dei consumatori CACER
- Consumo annuo aggregato (kWh) dei membri.
- Tipologia profilo (residenziale, terziario, PMI, mista).
- Se disponibili, profili orari o monthly load profile; altrimenti si applica un **fattore di condivisione** parametrico.

### Parametri economici
- Valore atteso TIP parte fissa per fascia (richiamare il DM 7/12/2023 art. 7, riportare i valori vigenti come ipotesi - **NON inventare**).
- Valore atteso TR (ultima delibera ARERA, **da verificare**).
- Maggiorazione zonale, se applicabile.

## Fonti

Leggere prima:

- [`../references/estratti/dm-mase-414-2023.md`](../references/estratti/dm-mase-414-2023.md)
- [`../references/estratti/tiad-arera-727-2022.md`](../references/estratti/tiad-arera-727-2022.md)
- [`../references/estratti/gse-regole-operative-cacer.md`](../references/estratti/gse-regole-operative-cacer.md)

## Procedura

### Passo 1 - Stima dell'energia immessa annua

Per ogni impianto FER:

- `E_imm_annua [kWh] = P [kW] * h_eq [h/anno]`
  - per FV: `h_eq` = 1.000-1.300 in funzione della latitudine (Nord/Centro/Sud);
  - per eolico, idro, biomassa: dichiarare il fattore di carico (es. 2.500 h/anno biomassa cogen, 1.800 h/anno idro fluente, 2.000-2.500 h/anno eolico onshore di buona qualita').

Sommare tra impianti per ottenere `E_imm_CACER`.

Se l'impianto serve in parte autoconsumo "fisico" (es. produzione e prelievo allo stesso POD, prima della rete), considerare solo la quota **immessa in rete** ai fini CACER.

### Passo 2 - Stima dell'energia prelevata annua

Sommare i consumi annui dichiarati dai POD partecipanti -> `E_prel_CACER`.

### Passo 3 - Stima dell'energia condivisa

Senza profili orari, usare un **fattore di condivisione** `eta_share` tale che:

- `E_cond_annua ~ eta_share * min(E_imm_CACER, E_prel_CACER)`

con `eta_share` parametrico (dichiarare il valore scelto):

- `0.30 - 0.40` per impianti FV su utenze prevalentemente residenziali senza accumulo (consumi serali, produzione diurna);
- `0.40 - 0.55` per CACER con utenze terziarie/PMI con consumi diurni allineati alla produzione FV;
- `0.55 - 0.70` con sistemi di accumulo dimensionati o profili molto diurni;
- ridurre se l'energia immessa supera in modo significativo i consumi totali (situazione di sovra-produzione).

L'agent deve esplicitare il valore scelto e la motivazione.

Se sono disponibili **profili orari**, calcolare invece direttamente:

```
E_cond_annua = sum_h min( E_imm_CACER(h) ,  E_prel_CACER(h) )
```

### Passo 4 - Stima della TIP

Schema:

```
TIP_annua [EUR] = E_cond_annua * (T_fissa(P) + correttivo_zonale_medio_annuo)
```

dove:

- `T_fissa(P)` e' il valore vigente del DM 7/12/2023 per la fascia di potenza dell'impianto (l'agent dichiara la fascia: < 200 kW, 200-600 kW, 600-1000 kW; il valore numerico va richiamato dalla pubblicazione vigente, **non inventato**);
- `correttivo_zonale_medio_annuo` e' positivo se il prezzo zonale annuo medio e' inferiore alla soglia, nullo o negativo (con tetto) se superiore.

Per impianti situati nelle Regioni con maggiorazione zonale prevista dal DM, applicare la maggiorazione (segnalare nel report).

Durata: **20 anni** dalla data di entrata in esercizio dell'impianto.

### Passo 5 - Stima della TR

Schema:

```
TR_annua [EUR] = E_cond_annua * tr_unitaria
```

dove `tr_unitaria` (EUR/kWh) e' il valore vigente per la tensione di connessione (MT vs BT) secondo l'ultima delibera ARERA applicabile al TIAD.

### Passo 6 - Stima del contributo PNRR (se applicabile)

Solo se l'impianto e' situato in Comune con popolazione < 5.000 ab.:

```
Contributo_PNRR [EUR] = min( 0.40 * costo_ammissibile ,  massimale_PNRR_applicabile )
```

Considerare:

- riduzione della parte fissa della TIP secondo il meccanismo previsto dal DM 7/12/2023;
- vincoli di spesa ammissibile e cronoprogramma PNRR;
- adempimenti DNSH (rinvio alla skill `dnsh-pnrr-checker`).

### Passo 7 - Componi la scheda di simulazione

Output strutturato come sotto.

## Output

```markdown
# Simulazione semplificata CACER

## 1. Ipotesi di calcolo
- Tecnologia impianto: [...]
- Potenza nominale: [...] kW
- Producibilita' attesa: [...] kWh/kWp/anno (fonte: ipotesi parametrica)
- Livello di tensione: BT / MT
- Comune: [Nome] - popolazione: [N]
- Profilo utenze: [residenziale / terziario / misto]
- Fattore di condivisione `eta_share`: [valore] (con motivazione)
- Valori TIP e TR: ipotizzati sui valori pubblicati vigenti, DA VERIFICARE su pubblicazione GSE/ARERA

## 2. Bilancio energetico annuo (stima)
| Voce | Valore [kWh/anno] |
|---|---|
| Energia immessa CACER | [...] |
| Energia prelevata CACER | [...] |
| Energia condivisa stimata | [...] |

## 3. Flussi economici (stima parametrica)
| Voce | Valore [EUR/anno] | Note |
|---|---|---|
| TIP | [...] | T_fissa(P) + correttivo zonale, durata 20 anni |
| TR | [...] | tariffa restituzione, livello tensione [...] |
| Contributo PNRR (una tantum) | [...] | solo se Comune < 5.000 ab.; riduce parte fissa TIP |

## 4. Avvertenze
- I valori sono stime parametriche su ipotesi dichiarate.
- Il calcolo ufficiale dell'energia condivisa e dei flussi e' del GSE su dati di
  misura validati ai sensi del TIAD.
- I valori della TIP e della TR vanno aggiornati con le pubblicazioni GSE e
  ARERA vigenti alla data della qualifica.
- Il contributo PNRR richiede una procedura separata e il rispetto del DNSH:
  rinvio alla skill `dnsh-pnrr-checker`.
- Verifiche residue: [...]

## 5. Disclaimer
Documento di supporto, non costituisce promessa di flussi economici futuri.
```

## Limiti del task

- Non e' un calcolo certificato GSE.
- Non considera variazioni di prezzo zonale orario; usa una media annua.
- Non valuta il rischio operativo (downtime impianto, manutenzione, autoconsumo fisico vs immesso).
- Non gestisce l'accumulo elettrochimico in dettaglio: se presente, dichiarare il dimensionamento e usare un `eta_share` piu' alto in modo motivato.
