# Note - Caso conforme: strato argilla OC con transizione a NC

## Perche' e' un caso conforme

- Tutti gli input sono entro il dominio di validita' della skill: singolo strato, parametri edometrici da prove (e non a memoria), Delta sigma' > 0, OCR > 1, Cr < Cc.
- OCR = 1.5 e' un valore molto comune per argille naturali italiane (lievemente sovra-consolidate).
- Il rapporto Cr/Cc = 0.05/0.30 = 1/6 e' nel range tipico (1/5 - 1/10).
- Il caso transizione e' didatticamente significativo perche' attiva entrambe le formule e mostra la composizione dei contributi.

## Cosa la skill deve fare

1. Citare NTC par. 6.2.2 e 6.2.4 + formulazione classica come framework.
2. Mostrare il dispatch del ramo (transizione in questo caso).
3. Decomporre il cedimento in contributi OC + NC.
4. Concludere con rinvio: 110 mm e' una stima di pre-dim, va confrontato con cedimento ammissibile dichiarato dal progettista, e cedimenti differenziali / tempi di consolidazione restano fuori scope.

## Anti-pattern da NON commettere

- **Non riprodurre i numeri "a mano"** parafrasando le formule: usare il modulo Python.
- **Non dire "Cc = 0.30 e Cr = 0.05 sono valori tipici"** in modo generico per validare l'input: l'utente li deve avere dalla relazione geotecnica, e i valori "tipici" variano molto. La skill non sostituisce il giudizio sui parametri.
- **Non confondere ramo transizione con somma di due cedimenti indipendenti**: e' un'unica integrazione della curva edometrica e-log(sigma') a tratti, con continuita' a sigma_p'.
- **Non liquidare l'avvertenza sul cedimento ammissibile**: 110 mm e' un valore elevato e merita un commento esplicito. La skill non decide se e' ammissibile, ma deve far percepire l'ordine di grandezza al progettista.
- **Non aggiungere stima dei tempi di consolidazione**: fuori scope skill, non inventare Cv.
