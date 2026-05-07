# DM 58/2017 Allegato A - Tabelle 1 e 2 + classe finale

> Fonte: DM 58/2017 Allegato A, sostituito dal DM 65/2017 (testo coordinato vigente per le procedure di classificazione).
> Consultata letteralmente su: https://www.mit.gov.it/nfsmitgov/files/media/normativa/2017-03/DM%2065%20del%2007-03-2017%20All%20A.pdf (PDF ufficiale MIT)
> Cross-check con output di software certificato: ClaSS 2017 di S.I.S. (Esempio_ClaSS_SIS.pdf, accesso 2026-05-07).
> Data accesso: 2026-05-07
> Licenza: dominio pubblico (atto normativo italiano)

## Tabella 1 classi PAM (8 classi)

> Testo letterale dell'Allegato A (Tab. 1):

| Classe | Intervallo PAM (frazione del costo di ricostruzione)        |
|:------:|:-----------------------------------------------------------:|
| A+     | PAM <= 0,50%                                                |
| A      | 0,50% < PAM <= 1,0%                                         |
| B      | 1,0%  < PAM <= 1,5%                                         |
| C      | 1,5%  < PAM <= 2,5%                                         |
| D      | 2,5%  < PAM <= 3,5%                                         |
| E      | 3,5%  < PAM <= 4,5%                                         |
| F      | 4,5%  < PAM <= 7,5%                                         |
| G      | 7,5% <= PAM                                                 |

**Convenzione bordi**: lower bound ESCLUSO, upper bound INCLUSO per A..F.

**Ambiguita' del decreto al bordo PAM = 7.5%**: il testo letterale pone F a `4.5% < PAM <= 7.5%` (incluso) e G a `7.5% <= PAM` (incluso). Il valore esatto PAM = 7.5% rientra letteralmente in entrambe. **Interpretazione conservativa adottata** (e coerente con la prassi dei software certificati): PAM = 7.5% e' classificato come F.

## Tabella 2 classi IS-V (7 classi - non esiste classe G per IS-V)

> Testo letterale dell'Allegato A (Tab. 2):

| Classe | Intervallo IS-V        |
|:------:|:-----------------------:|
| A+     | 100% < IS-V             |
| A      | 80%  <= IS-V <  100%    |
| B      | 60%  <= IS-V <  80%     |
| C      | 45%  <= IS-V <  60%     |
| D      | 30%  <= IS-V <  45%     |
| E      | 15%  <= IS-V <  30%     |
| F      | IS-V <= 15%             |

**Convenzione bordi**: lower bound INCLUSO, upper bound ESCLUSO per A..E. La classe F include IS-V = 15% nel suo upper bound.

**Ambiguita' del decreto al bordo IS-V = 100%**: il testo letterale pone A+ a `100% < IS-V` (esclusivo) e A a `80% <= IS-V < 100%` (esclusivo). Il valore esatto IS-V = 100% NON e' formalmente coperto da nessuna classe. **Interpretazione conservativa adottata da questa skill** (in linea con i software certificati ClaSS 2017 e MasterSap-SismiClass): IS-V = 100% e' classificato come A (la classe meno migliorativa tra A+ e A).

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
