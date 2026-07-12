# Note - caso problematico: OCR < 1

## Perche' questo esempio e' importante

- Fissa il comportamento di sicurezza del modulo sul dato sospetto piu' classico (sigma_p' < sigma_0'): **rifiuto di default con messaggio esplicito**, mai un numero calcolato in silenzio.
- Rispetto alla versione pre-remediation (che trattava OCR < 1 solo come "fisicamente non ammissibile"), la fonte FHWA (par. 7.5.2.3, trascritto) chiarisce che la **sottoconsolidazione e' una condizione reale** (consolidazione ancora in corso): il modulo quindi la ammette, ma SOLO dietro dichiarazione esplicita (`--sottoconsolidato`), applicando l'eq. [7-6] e avvertendo che ignorarla sottostima il cedimento totale.
- Il percorso decisionale (dati errati vs sottoconsolidazione giustificata) resta in capo al progettista: la skill non sceglie.

## Cosa insegna

- La differenza tra "input rifiutato" e "caso normativo diverso che richiede una dichiarazione consapevole".
- Come la lettura integrale della fonte (7.5.2.3) migliora il comportamento della skill rispetto a una regola inventata.
