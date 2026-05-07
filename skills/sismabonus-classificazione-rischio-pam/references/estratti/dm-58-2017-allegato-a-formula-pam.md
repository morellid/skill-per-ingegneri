# DM 58/2017 Allegato A punto 2.1 - PAM e Curva di Individuazione

> Fonte: DM 58/2017 Allegato A (testo aggiornato dal DM 65/2017, DM 24/2020, DM 329/2020).
> Consultata su: https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017 (decreto istitutivo) e versione coordinata DM 65/2017 reperita pubblicamente
> Data accesso: 2026-05-07
> Licenza: dominio pubblico (atto normativo italiano)

## Definizione PAM

La **Perdita Annuale Media (PAM)** rappresenta il costo di riparazione dei danni causati dagli eventi sismici che si manifestano nel corso della vita della costruzione, ripartito annualmente ed espresso come percentuale del costo di ricostruzione (CR).

E' valutato come l'**area sottesa alla Curva di Individuazione** che rappresenta le perdite economiche dirette in funzione della frequenza media annua di superamento (lambda) degli eventi sismici associati ai diversi Stati Limite.

## Stati Limite considerati e %CR associati

I 4 Stati Limite NTC (per cui il progettista esegue l'analisi di vulnerabilita'):

| Stato Limite | %CR (Costo di Ricostruzione) |
|-------------:|:-----------------------------:|
| SLO (Operativita')                 | 7%   |
| SLD (Danno)                        | 15%  |
| SLV (salvaguardia della Vita)      | 50%  |
| SLC (prevenzione del Collasso)     | 80%  |

Stati Limite convenzionali aggiunti dall'Allegato A:

| Stato Limite | TR (anni) | %CR  |
|:------------:|:---------:|:----:|
| SLID (Inizio Danno) | **10 anni** convenzionale | **0%** |
| SLR (Ricostruzione) | stesso TR di SLC          | **100%** |

## Frequenza media annua di superamento

Per ciascuno SL si pone:

```
lambda(SL) = 1 / TR_C(SL)
```

dove TR_C(SL) e' il periodo di ritorno di **capacita'** dell'evento che porta l'edificio a quel SL (output dell'analisi di vulnerabilita' NTC 2018 cap. 8).

## Formula PAM

La formula trapezoidale che approssima l'area sottesa alla Curva di Individuazione e' (con la convenzione SL_1 = SLID, SL_2 = SLO, SL_3 = SLD, SL_4 = SLV, SL_5 = SLC):

```
PAM = sum_{i=2}^{5} [lambda(SL_i) - lambda(SL_{i-1})] * [CR(SL_i) + CR(SL_{i-1})] / 2
      + lambda(SLC) * CR(SLR)
```

L'addendo finale `lambda(SLC) * CR(SLR)` rappresenta il **termine di coda**: la curva sale verticalmente da CR=80% a CR=100% al lambda di SLC (Stato di Ricostruzione), contribuendo all'integrale con il rettangolo di base lambda(SLC) e altezza CR(SLR)=100%.

## Note operative

1. **Curva di Individuazione monotona**: in condizioni "ben condizionate" l'analisi produce TR_C tali che la curva sia monotona crescente (lambda decrescente per severita' crescente del SL). Se non e' rispettato (es. TR_C(SLO) > TR_C(SLD)), l'Allegato A prevede una correzione di "capping" che e' responsabilita' del progettista. Questa skill non applica capping automatico ma SEGNALA la non monotonia tramite il flag `monotona: false` nell'output.

2. **Conversione %**: nella formula i CR sono frazioni adimensionali (0.07 per SLO, 0.15 per SLD, ...). Il PAM risultante e' frazione adimensionale; per ottenere la percentuale richiesta dalla Tab. classi PAM (Allegato A punto 2.3) moltiplicare per 100.

3. **Verifica geometrica**: trattandosi di area di un poligono nel piano (lambda, CR) con vertici noti, una buona implementazione produce sempre PAM > 0 indipendentemente dal verso di sommatoria. Il modulo `sismabonus.py` usa il valore assoluto della differenza di lambda per garantire questa proprieta' (coerentemente con il significato geometrico).

## Riferimenti puntuali

- DM 58/2017 Allegato A punto 2.1 (testo coordinato DM 329/2020): definizione PAM, Curva di Individuazione, formula
- DM 58/2017 Allegato A punto 2.3: tabella classi PAM (vedi `dm-58-2017-allegato-a-tabelle-classi.md`)
- NTC 2018 par. 3.2.1 + Tab. 3.2.I: P_VR e TR_D di domanda per SLO/SLD/SLV/SLC (utili al progettista per derivare PGA_D al sito; non direttamente la TR_C)
