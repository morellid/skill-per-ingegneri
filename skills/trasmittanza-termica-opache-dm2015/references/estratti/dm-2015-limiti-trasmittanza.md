# Estratto operativo - DM 26/06/2015: limiti di trasmittanza U per zona climatica

Estratto curato per il calcolo/verifica. Ogni valore e' parafrasi/citazione
della trascrizione verificata in
`references/fonti/dm-26-06-2015-requisiti-minimi.md` (DM 26/06/2015, Allegato 1,
Appendici A e B). I valori sono citabili a una tabella precisa del PDF letto.

## 1. Calcolo della trasmittanza (metodo, NON dal decreto)

`U = 1 / R_tot`  con  `R_tot = R_si + sum(s_i / lambda_i) + R_se`  [W/(m2 K)]

- `s_i` = spessore dello strato i-esimo [m]; `lambda_i` = conducibilita' termica
  [W/(m K)] (dato dell'utente, da scheda tecnica / valore dichiarato);
- `R_si`, `R_se` = resistenze termiche superficiali interna ed esterna
  [m2 K/W] (dato dell'utente, da UNI EN ISO 6946).

> Il metodo (legge di Fourier) e' fisica tecnica di pubblico dominio. Il DM NON
> contiene ne' il metodo, ne' i lambda, ne' le R_si/R_se: la skill non li
> inventa. Il DM fornisce SOLO i valori limite qui sotto.

## 2. Obbligo di verifica (DM Allegato 1, par. 5.2)

Per gli edifici esistenti sottoposti a riqualificazione energetica, per la
porzione di involucro interessata, `U <= U_limite` (Appendice B):
- strutture opache verticali -> Tabella 1 (App. B);
- coperture opache orizzontali/inclinate -> Tabella 2 (App. B);
- pavimenti -> Tabella 3 (App. B);
- chiusure trasparenti/opache con infissi -> Tabella 4 (App. B).

**Incremento +30% (Cap. 5, par. 5.2):** per riqualificazione dell'involucro
opaco con **isolamento dall'interno** o **in intercapedine**, i limiti delle
tabelle 1-4 dell'Appendice B sono **incrementati del 30%**.

Per le nuove costruzioni e le ristrutturazioni importanti la verifica avviene
con il metodo dell'edificio di riferimento (Appendice A); i valori di U
dell'Appendice A sono riportati come riferimento.

## 3. Tabella 1 Appendice B - U MASSIMA strutture opache VERTICALI (riqualificazione)

| Zona climatica | 2015 [W/(m2 K)] | **2021** [W/(m2 K)] |
|---|---|---|
| A e B | 0,45 | **0,40** |
| C | 0,40 | **0,36** |
| D | 0,36 | **0,32** |
| E | 0,30 | **0,28** |
| F | 0,28 | **0,26** |

## 4. Tabella 2 Appendice B - U MASSIMA COPERTURE (riqualificazione)

| Zona | 2015 | **2021** |
|---|---|---|
| A e B | 0,34 | **0,32** |
| C | 0,34 | **0,32** |
| D | 0,28 | **0,26** |
| E | 0,26 | **0,24** |
| F | 0,24 | **0,22** |

## 5. Tabella 3 Appendice B - U MASSIMA PAVIMENTI (riqualificazione)

| Zona | 2015 | **2021** |
|---|---|---|
| A e B | 0,48 | **0,42** |
| C | 0,42 | **0,38** |
| D | 0,36 | **0,32** |
| E | 0,31 | **0,29** |
| F | 0,30 | **0,28** |

## 6. Tabella 4 Appendice B - U MASSIMA chiusure trasparenti/opache + infissi

| Zona | 2015 | **2021** |
|---|---|---|
| A e B | 3,20 | **3,00** |
| C | 2,40 | **2,00** |
| D | 2,10 | **1,80** |
| E | 1,90 | **1,40** |
| F | 1,70 | **1,00** |

## 7. Appendice A (edificio di riferimento) - U pareti opache verticali

Per nuove costruzioni / ristrutturazioni importanti (metodo edificio di
riferimento). Colonna (2): dal 1/1/2019 (edifici pubblici) / 1/1/2021 (altri).

| Zona | 2015 | 2019/2021 |
|---|---|---|
| A e B | 0,45 | 0,43 |
| C | 0,38 | 0,34 |
| D | 0,34 | 0,29 |
| E | 0,30 | 0,26 |
| F | 0,28 | 0,24 |

(coperture, pavimenti, chiusure trasparenti App. A: vedi la trascrizione.)

## 8. Caveat normativi (dal decreto) - da riportare sempre

- I valori limite delle tabelle **includono l'effetto dei ponti termici** (App.
  B nota: comprensivi dei ponti termici interni alla struttura e di meta' del
  ponte termico al perimetro). Un calcolo 1D della sola stratigrafia **NON**
  include i ponti termici: la verifica con U 1D e' **preliminare**; la verifica
  completa richiede il calcolo dei ponti termici (UNI EN ISO 14683/10211).
- Strutture verso ambienti **non climatizzati**: la U va divisa per il fattore
  di correzione (UNI/TS 11300-1) prima del confronto.
- Strutture **contro terra**: confronto con la trasmittanza equivalente (UNI EN
  ISO 13370), non con la U 1D.

## Fuori ambito di questa skill

- Non fornisce i lambda dei materiali (input utente) ne' le R_si/R_se (UNI EN
  ISO 6946): non riproduce norme UNI a pagamento.
- Non calcola i ponti termici, l'H'T, la prestazione energetica globale, l'APE.
- Non copre le condense (Glaser), la trasmittanza periodica YIE, l'inerzia.
