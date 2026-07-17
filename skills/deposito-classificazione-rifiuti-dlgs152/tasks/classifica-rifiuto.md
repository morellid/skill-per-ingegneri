# Task: classifica-rifiuto

Classifica un **rifiuto** secondo l'**origine** (urbano/speciale) e la **pericolosita'**
(pericoloso/non pericoloso), secondo l'**art. 184 del D.Lgs. 152/2006**, con il rinvio all'**EER**
e alle **Linee guida**.

## Input richiesti

- **Attivita' di origine** del rifiuto (agricola, costruzione e demolizione, industriale,
  artigianale, commerciale, servizi, sanitaria, ecc.) e **descrizione** del materiale.
- Eventuali **caratteristiche di pericolo** note o **schede di sicurezza**/analisi delle sostanze
  contenute.

## Procedura

1. **Origine** (art. 184, c. 1-3): stabilire se il rifiuto e' **urbano** (art. 183, c. 1 lett.
   b-ter) o **speciale** (tra cui: **costruzione e demolizione**; industriale; artigianale;
   commerciale; da servizi; da recupero/smaltimento e depurazione; sanitario; **veicoli fuori uso**).
2. **Pericolosita'** (c. 1, 4): stabilire se il rifiuto e' **pericoloso** (presenta le
   caratteristiche di pericolo dell'**allegato I**) o **non pericoloso**.
3. **Codice EER** (c. 5): individuare il **codice** nell'**elenco dei rifiuti (allegato D)**;
   l'elenco e' **vincolante** per la determinazione dei pericolosi. L'**attribuzione** del codice e
   delle caratteristiche di pericolo e' a **cura del produttore**, sulla base delle **Linee guida**
   (SNPA). Per i codici **"a specchio"** puo' essere necessaria la **caratterizzazione analitica**.
4. **Divieto di declassificazione** (c. 5-ter): non e' ammesso passare da pericoloso a non
   pericoloso tramite **diluizione o miscelazione** che riduca le concentrazioni sotto le soglie.

## Output atteso

- Classificazione del rifiuto: **urbano/speciale** e **pericoloso/non pericoloso**, con il rinvio
  al **codice EER** (allegato D) e alle **Linee guida** per l'attribuzione, evidenziando gli
  eventuali passaggi analitici a carico del **produttore**.

## Avvertenze

- L'**elenco EER (allegato D)** e le **caratteristiche di pericolo (allegato I)** non sono
  riprodotti: la skill rinvia agli allegati e alle Linee guida.
- L'**attribuzione dei codici** e la **caratterizzazione** restano del **produttore/detentore** e
  del consulente: la skill inquadra il metodo, non certifica la classificazione.
