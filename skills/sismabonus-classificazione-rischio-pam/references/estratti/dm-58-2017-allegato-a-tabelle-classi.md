# DM 58/2017 Allegato A punto 2.3 - Tabelle classi PAM e IS-V + classe finale

> Fonte: DM 58/2017 Allegato A (testo aggiornato dal DM 65/2017, DM 24/2020, DM 329/2020).
> Consultata su: https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017
> Cross-check con output di software certificato: ClaSS 2017 di S.I.S. (Esempio_ClaSS_SIS.pdf, accesso 2026-05-07).
> Data accesso: 2026-05-07
> Licenza: dominio pubblico (atto normativo italiano)

## Tabella classi PAM (8 classi)

| Classe | Intervallo PAM (frazione del costo di ricostruzione)        |
|:------:|:------------------------------------------------------------:|
| A+     | PAM <= 0,50%                                                 |
| A      | 0,50% < PAM <= 1,0%                                          |
| B      | 1,0%  < PAM <= 1,5%                                          |
| C      | 1,5%  < PAM <= 2,5%                                          |
| D      | 2,5%  < PAM <= 3,5%                                          |
| E      | 3,5%  < PAM <= 4,5%                                          |
| F      | 4,5%  < PAM <= 7,5%                                          |
| G      | PAM > 7,5%                                                   |

## Tabella classi IS-V (7 classi - non esiste classe G per IS-V)

| Classe | Intervallo IS-V |
|:------:|:----------------:|
| A+     | IS-V > 100%      |
| A      | 80% <= IS-V <= 100% |
| B      | 60% <= IS-V <  80%  |
| C      | 45% <= IS-V <  60%  |
| D      | 30% <= IS-V <  45%  |
| E      | 15% <= IS-V <  30%  |
| F      | IS-V < 15%       |

## Regola classe finale

> La classe di rischio sismico finale dell'edificio e' attribuita come la **classe peggiore** (ovvero quella corrispondente al rischio maggiore) tra la classe associata al parametro PAM e quella associata al parametro IS-V.

In termini di graduatoria (A+ = miglior risultato, G = peggior risultato):

```
classe_finale = max_in_graduatoria(classe_PAM, classe_IS-V)
```

## Note operative

1. **Bordi inclusi/esclusi PAM**: la tabella usa la convenzione "<=" per il limite superiore dell'intervallo (es. classe A+ include esattamente PAM = 0.50%).
2. **Bordi inclusi/esclusi IS-V**: la classe A include sia il limite inferiore (80%) sia il limite superiore (100%) - intervallo chiuso. La classe A+ richiede IS-V STRETTAMENTE > 100%. Le altre classi (B, C, D, E) hanno limite inferiore incluso e limite superiore escluso. La classe F include IS-V = 0.
3. **Classe G non per IS-V**: la peggior classe di IS-V e' F. La classe G compare solo per PAM (PAM > 7.5%) o come risultato della regola "classe finale = peggiore" se classe_PAM = G.
4. **Implementazione**: la convenzione di bordo e' nel modulo `sismabonus.py`, funzioni `classifica_PAM` e `classifica_IS_V`. Test unitari sui bordi in `test_sismabonus.py` (`TestClassiPAMBoundary`, `TestClassiISVBoundary`).

## Riferimenti puntuali

- DM 58/2017 Allegato A punto 2.3 (testo coordinato DM 329/2020): tabelle classi e regola classe finale
- ClaSS 2017 attestato di esempio (S.I.S. Software Ingegneria Strutturale) - cross-check qualitativo dei bordi tabella, accessibile su `infowebsrl.it/Newsletter/SIS_ingegneria/1/Pdf/Esempio_ClaSS_SIS.pdf`
