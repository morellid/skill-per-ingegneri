# Task: Simulazione semplificata di autoconsumo condiviso e flussi economici

Stima in modo trasparente e parametrico l'**energia condivisa annua** della CACER, la **TIP** ex art. 7 DM 7/12/2023, la **TR** del TIAD ARERA 727/2022/R/eel e l'eventuale **contributo PNRR** ex art. 8 DM 7/12/2023.

## Obiettivo

Produrre una **scheda di simulazione** che riporti, in maniera trasparente:

- ipotesi di calcolo (potenza, producibilita', profili, fattore di condivisione);
- energia immessa annua, energia prelevata annua, energia condivisa stimata;
- TIP stimata (parte fissa per fascia di potenza + indicazione di applicabilita' del correttivo zonale);
- TR stimata (sulla base del livello di tensione e del valore vigente ARERA, da verificare);
- contributo PNRR stimato, se Comune < 50.000 ab. (regime vigente post DM 127/2025);
- riduzione TIP per cumulo PNRR, se applicabile;
- avvertenze esplicite sui limiti.

La simulazione e' **parametrica**: il calcolo definitivo e' del GSE su dati di misura.

## Input richiesti

### Impianto/i FER
- Tecnologia (FV, eolico, idro, biomassa).
- Potenza nominale (kW) per ciascun impianto.
- **Producibilita' attesa** in kWh/kWp/anno o equivalente fattore di carico annuo: il valore va **fornito dall'utente** (sulla base di stime PVGIS / studio di producibilita' sito-specifico, dato storico, dichiarazione del progettista). La skill non assume valori "tipici" non sourceati.
- Livello di tensione di connessione (BT / MT).
- Comune e popolazione (per verifica condizione PNRR).

### Profilo dei consumatori CACER
- Consumo annuo aggregato (kWh) dei membri.
- Tipologia profilo (residenziale, terziario, PMI, mista).
- Se disponibili, profili orari o monthly load profile.
- Se profili orari **non disponibili**, l'utente deve **dichiarare un fattore di condivisione** `eta_share` (frazione dell'energia immessa che si stima diventi energia condivisa) e la fonte/ragionamento alla base del valore. La skill non propone un default: senza dato, la simulazione resta parziale.

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

Il valore di `h_eq` (ore equivalenti annue) deve essere **fornito dall'utente** o dal progettista, con esplicita dichiarazione della fonte (PVGIS, studio anemologico, idrologia di sito, dichiarazione del costruttore, dato storico). La skill non assume valori "tipici" per FV, eolico, idro o biomassa: indicare `DA FORNIRE` se non disponibile e proseguire con quel campo aperto.

Sommare tra impianti per ottenere `E_imm_CACER`.

Se l'impianto serve in parte autoconsumo "fisico" (es. produzione e prelievo allo stesso POD, prima della rete), considerare solo la quota **immessa in rete** ai fini CACER.

### Passo 2 - Stima dell'energia prelevata annua

Sommare i consumi annui dichiarati dai POD partecipanti -> `E_prel_CACER`.

### Passo 3 - Stima dell'energia condivisa

La definizione operativa, ai sensi del TIAD ARERA 727/2022/R/eel, e':

```
E_cond(h) = min( E_imm_CACER(h) ,  E_prel_CACER(h) )
E_cond_annua = sum_h E_cond(h)
```

con aggregazione oraria su 8.760 (o 8.784 per anni bisestili) ore.

In presenza di profili orari, applicare direttamente la formula sopra.

In assenza di profili orari, la skill **non assume un fattore di condivisione di default**: l'utente o il progettista devono dichiarare un valore `eta_share` con relativa motivazione/fonte (es. studio sito-specifico, simulazione di scenario, riferimento bibliografico). La skill registra il valore dichiarato come ipotesi e lo riporta esplicitamente nelle avvertenze.

Formula di stima parametrica (quando l'utente fornisce `eta_share`):

```
E_cond_annua ~ eta_share * min( E_imm_CACER , E_prel_CACER )
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

Solo se l'impianto e' situato in Comune con popolazione **< 50.000 ab.** (regime vigente post DM MASE 127/2025; il DM 414/2023 originario fissava la soglia a 5.000 ab.):

```
Contributo_PNRR [EUR] = min( 0.40 * costo_ammissibile ,  massimale_PNRR_applicabile )
```

Considerare:

- riduzione della parte fissa della TIP secondo il meccanismo previsto dal DM 7/12/2023;
- vincoli di spesa ammissibile e cronoprogramma PNRR;
- **scadenze (post DL 19/2026 art. 27)**: stipula degli accordi di concessione lato GSE entro il 30 giugno 2026; entrata in esercizio entro 24 mesi dalla comunicazione dell'accordo di concessione e comunque non oltre il 31 dicembre 2027;
- **erogazione in tre fasi**: anticipazione fino al 30% del contributo massimo erogabile, quota intermedia pari al 40% (post-40% delle spese ammissibili sostenute e comunicato l'avvio dei lavori), saldo finale;
- adempimenti DNSH (rinvio alla skill `dnsh-pnrr-checker`).

### Passo 7 - Componi la scheda di simulazione

Output strutturato come sotto.

## Output

```markdown
# Simulazione semplificata CACER

## 1. Ipotesi di calcolo
- Tecnologia impianto: [...]
- Potenza nominale: [...] kW
- Producibilita' attesa: [...] kWh/kWp/anno (FONTE DICHIARATA DALL'UTENTE: PVGIS / studio sito-specifico / dato storico / dichiarazione progettista)
- Livello di tensione: BT / MT
- Comune: [Nome] - popolazione: [N]
- Profilo utenze: [residenziale / terziario / misto]
- Fattore di condivisione `eta_share`: [valore dichiarato dall'utente, con fonte/motivazione] - se profili orari disponibili, indicare "calcolo orario diretto"
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
| Contributo PNRR (una tantum) | [...] | solo se Comune < 50.000 ab.; regime vigente al 2026-05-07 (DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27): stipula accordi di concessione 30/6/2026 + esercizio entro 24 mesi dalla comunicazione dell'accordo (max 31/12/2027); anticipazione 30% + quota intermedia 40% + saldo; riduce parte fissa TIP |

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
