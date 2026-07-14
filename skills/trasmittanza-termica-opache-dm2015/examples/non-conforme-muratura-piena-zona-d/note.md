# Note - muratura piena, zona D (non conforme + incremento +30%)

## Perche' questo esempio e' importante

- Mostra il caso "non conforme" e, soprattutto, il meccanismo dell'**incremento
  +30%** dei limiti dell'Appendice B per isolamento dall'interno o in
  intercapedine (Cap. 5 par. 5.2 del DM 26/06/2015): un dettaglio spesso
  trascurato e direttamente rilevante per gli interventi su edifici storici dove
  il cappotto esterno non e' ammesso.
- Fissa che l'incremento **non e' un'esenzione**: il limite maggiorato va
  comunque rispettato.

## Cosa insegna

- Come lo stato di fatto (muratura piena non isolata) sia strutturalmente
  lontano dai limiti, e come il modulo si usi iterando sulla stratigrafia di
  progetto per dimensionare l'isolante.
- Il flag `--isolamento-interno` si applica solo al regime `riqualificazione`
  (Appendice B): il modulo rifiuta l'incremento sul regime
  `edificio_riferimento`.
- L'avvertenza sui ponti termici e' particolarmente pregnante con l'isolamento
  dall'interno (solai e pilastri restano non isolati).
