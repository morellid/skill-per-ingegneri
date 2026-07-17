# Task: verifica-sottoprodotto

Inquadra se una sostanza od oggetto può essere qualificato **sottoprodotto e non rifiuto**
ai sensi dell'**art. 184-bis del D.Lgs. 152/2006**, verificando le **quattro condizioni
cumulative**. Non classifica in concreto il materiale: prepara l'inquadramento.

## Input

- Descrizione del materiale e del **processo di produzione** da cui origina.
- Destinazione d'uso prevista (chi lo usa, in quale processo) e trattamenti eventuali prima
  dell'uso.
- Requisiti di prodotto/salute/ambiente applicabili all'utilizzo previsto.

## Procedura

1. **Verifica delle quattro condizioni (art. 184-bis c. 1)** - devono ricorrere **tutte**:
   - **a)** il materiale è **originato da un processo di produzione** di cui è **parte
     integrante** e il cui **scopo primario non** è produrlo;
   - **b)** è **certo** (non solo probabile) che sarà **utilizzato**, nello stesso o in un
     successivo processo, dal produttore o da terzi;
   - **c)** è **utilizzabile direttamente** senza **alcun trattamento diverso dalla normale
     pratica industriale**;
   - **d)** l'utilizzo è **legale** (requisiti di prodotto, salute e ambiente; nessun
     impatto complessivo negativo).

2. **Esito**
   - Se **tutte** le condizioni ricorrono: il materiale è inquadrabile come
     **sottoprodotto** (fuori dalla disciplina rifiuti).
   - Se **anche una sola** manca: resta **rifiuto** (e può eventualmente accedere all'End of
     Waste dopo recupero, art. 184-ter → task `inquadra-end-of-waste`).

3. **Criteri di settore (art. 184-bis c. 2)**
   - Verifica se esiste un **DM di criterio** per la tipologia (es. **DM 264/2016**) che
     specifica come dimostrare le condizioni: rinvio, non riprodotto.

4. **Onere della prova e documentazione**
   - Segnala che la dimostrazione delle condizioni è **onere del produttore/detentore** e
     va supportata documentalmente (senza redigere l'atto).

## Output

Inquadramento condizione per condizione (a-d) con esito (sottoprodotto / resta rifiuto),
richiamo all'eventuale DM di criterio e all'onere probatorio. Rinvia la qualificazione in
concreto al produttore e all'autorità competente.

## Riferimenti

- `../references/fonti/dlgs-152-2006-184bis-184ter.md` (art. 184-bis)
- `../references/estratti/sottoprodotti-eow-checklist.md` (sez. 1-2)
