# Task: Precheck bozza POS prima della firma

Esegue un controllo finale su una **bozza di POS** appena compilata, riusando in modo coordinato i quattro task di verifica gia' presenti nella skill.

## Obiettivo

Produrre un report sintetico che dica se la bozza:

- e' strutturalmente completa;
- ha lacune documentali ancora aperte;
- presenta incoerenze evidenti tra rischi, misure, costi e coordinamento;
- puo' passare a revisione umana finale oppure richiede integrazioni sostanziali.

## Input richiesti

- Bozza POS completa o quasi completa
- Se disponibili: PSC, estratti DVR, sezione costi sicurezza, elenco subappalti/allegati

## Fonti normative

Usare indirettamente, tramite i task dedicati:

- `tasks/check-completezza.md`
- `tasks/check-coerenza-rischi.md`
- `tasks/check-costi-sicurezza.md`
- `tasks/check-coordinamento.md`

## Procedura

### Passo 1 - Lancia i quattro check

Applicare in sequenza:

1. completezza;
2. coerenza rischi-misure;
3. costi sicurezza;
4. coordinamento e interferenze.

### Passo 2 - Collassa gli esiti

Sintetizzare i risultati in 4 blocchi:

- `Blocchi critici`
- `Lacune da completare`
- `Boilerplate o genericita' sospette`
- `Allegati / evidenze mancanti`

### Passo 3 - Decisione operativa

Classificare la bozza come:

- `Pronta per revisione umana finale`
- `Da integrare prima della revisione`
- `Troppo incompleta per la firma`

## Output atteso

```markdown
# Precheck bozza POS

## Esito complessivo
- Stato: [Pronta per revisione umana finale | Da integrare prima della revisione | Troppo incompleta per la firma]

## 1. Completezza Allegato XV
- ...

## 2. Coerenza rischi-misure
- ...

## 3. Costi sicurezza
- ...

## 4. Coordinamento e interferenze
- ...

## Blocchi critici
- ...

## Dati / allegati ancora mancanti
- ...

## Prossime azioni
1. ...
2. ...

## Avvertenza
Il precheck non equivale a validazione professionale del POS.
```

## Limiti

- Il precheck dipende dalla qualita' della bozza e degli allegati disponibili.
- Non sostituisce la revisione del CSE/CSP o del datore di lavoro.
