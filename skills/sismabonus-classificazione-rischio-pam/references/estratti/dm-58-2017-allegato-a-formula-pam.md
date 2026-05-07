# DM 58/2017 Allegato A punto 2.1 - PAM e Curva di Individuazione

> Fonte: DM 58/2017 Allegato A, sostituito dal DM 65/2017 (testo coordinato vigente per le procedure di classificazione).
> Consultata letteralmente su: https://www.mit.gov.it/nfsmitgov/files/media/normativa/2017-03/DM%2065%20del%2007-03-2017%20All%20A.pdf (PDF ufficiale MIT)
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

## Capping prescritto dall'Allegato A (passo 3 della procedura)

Il decreto **prescrive** una correzione obbligatoria sui TR_C:

> "per il calcolo del tempo di ritorno TrC associato al raggiungimento degli stati limite di esercizio (SLD ed SLO) e' necessario assumere il valore minore tra quello ottenuto per tali stati limite e quello valutato per lo stato limite di salvaguardia della vita. Si assume, di fatto, che non si possa raggiungere lo stato limite di salvaguardia della vita senza aver raggiunto gli stati limite di operativita' e danno."

Operativamente:

```
TR_C(SLO) := min(TR_C(SLO), TR_C(SLV))
TR_C(SLD) := min(TR_C(SLD), TR_C(SLV))
```

equivalentemente in lambda:

```
lambda_SLO := max(lambda_SLO, lambda_SLV)
lambda_SLD := max(lambda_SLD, lambda_SLV)
```

Il modulo `sismabonus.py` applica questo capping di **default** (flag `capping=True` in `costruisci_curva_individuazione`); puo' essere disabilitato via `--no-capping` per validazione vs software che applicano il capping a monte (input gia' capped) o per analisi avanzate. L'output del modulo riporta sempre i valori originali e quelli effettivamente usati (`CappingApplicato`), per piena tracciabilita'.

NB: il decreto NON disciplina esplicitamente il caso TR_C(SLO) > TR_C(SLD) (SLO meno frequente di SLD). Il modulo segnala comunque la non monotonia residua via flag `monotona: false`.

## Verifica numerica vs decreto

L'Allegato A nella nota a Tab. 1 dichiara esplicitamente: "una costruzione con periodo di riferimento V_R pari a 50 anni, le cui prestazioni siano puntualmente pari ai minimi di quelle richieste dalle vigenti Norme Tecniche per le Costruzioni per un edificio di nuova costruzione [...] ha un valore di PAM che la colloca in Classe PAM B (il valore di PAM e', in questo caso, pari a 1,13%)".

Per V_R=50 anni ai minimi NTC: TR_D = {30, 50, 475, 975} per {SLO, SLD, SLV, SLC}; capacita' = domanda; SLID conv. TR=10. Calcolando con la formula trapezoidale e abs():

```
SLID->SLO: |1/30 - 1/10| * (0 + 0.07)/2     = 0.0667 * 0.035  = 0.00233
SLO->SLD:  |1/50 - 1/30| * (0.07 + 0.15)/2  = 0.01333 * 0.11  = 0.00147
SLD->SLV:  |1/475 - 1/50| * (0.15 + 0.50)/2 = 0.01789 * 0.325 = 0.00582
SLV->SLC:  |1/975 - 1/475| * (0.50 + 0.80)/2 = 0.00108 * 0.65 = 0.00070
coda SLR:  1/975 * 1.0                                       = 0.00103
PAM totale                                                    = 0.01134 = 1.13%
```

**Coincide esattamente con il valore dichiarato dal decreto (1,13%).** Questo e' il check di consistenza piu' importante della skill, implementato come `test_pam_riferimento_decreto_VR_50` in `test_sismabonus.py`.

## Note operative

1. **Verso di sommatoria e abs()**: letta letteralmente con i segni (lambda decrescente per i crescente: lambda_SLID > lambda_SLO > ... > lambda_SLC), la sommatoria nel testo del decreto produrrebbe valore NEGATIVO, da cui PAM negativo dopo l'aggiunta della coda - in contraddizione con il significato fisico ("perdita annua media", sempre positiva) e con il valore di riferimento 1.13% dichiarato dal decreto stesso. L'interpretazione consolidata in letteratura tecnica italiana (Cosenza et al. 2018) e nei software certificati e' geometrica (area sotto la spezzata, sempre positiva), da cui l'uso del valore assoluto della differenza di lambda. Questa scelta e' verificata dal test sopra (1.13%).

2. **Conversione %**: nella formula i CR sono frazioni adimensionali (0.07 per SLO, 0.15 per SLD, ...). Il PAM risultante e' frazione adimensionale; per ottenere la percentuale richiesta dalla Tab. 1 classi PAM moltiplicare per 100.

3. **Curva monotona dopo il capping**: dopo l'applicazione del capping prescritto, lambda_SLO >= lambda_SLV e lambda_SLD >= lambda_SLV. Se l'input e' fisicamente coerente (TR_C(SLO) <= TR_C(SLD) <= TR_C(SLV) <= TR_C(SLC)) la curva e' monotona; altrimenti il modulo segnala `monotona: false` come avvertenza per il progettista.

## Riferimenti puntuali

- DM 58/2017 Allegato A punto 2.1 (testo coordinato DM 329/2020): definizione PAM, Curva di Individuazione, formula
- DM 58/2017 Allegato A punto 2.3: tabella classi PAM (vedi `dm-58-2017-allegato-a-tabelle-classi.md`)
- NTC 2018 par. 3.2.1 + Tab. 3.2.I: P_VR e TR_D di domanda per SLO/SLD/SLV/SLC (utili al progettista per derivare PGA_D al sito; non direttamente la TR_C)
