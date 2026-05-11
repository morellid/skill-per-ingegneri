# Task: Stima parametrica prudente dei flussi

## Obiettivo

Restituire una stima non ufficiale di energia condivisa e flussi economici, chiarendo limiti e ipotesi.

## Input minimi

- produzione annua stimata o ore equivalenti dichiarate dall'utente
- consumo annuo aggregato
- eventuale fattore di condivisione dichiarato dall'utente
- interesse o meno al PNRR

## Fonti da leggere

- `references/estratti/gse-regole-operative-cacer.md`
- `references/estratti/tiad-arera-727-2022.md`
- `references/estratti/dm-mase-414-2023.md`

## Procedura

1. Chiedi sempre da dove arrivano produzione e profilo di consumo.
2. Se mancano profili orari, dichiara che la stima e' parametrica.
3. Calcola solo grandezze semplici e trasparenti: energia immessa annua, energia prelevata annua, energia condivisa stimata come minimo energetico corretto da un fattore dichiarato dall'utente.
4. Presenta TIP e contributo di valorizzazione solo come voci da valorizzare con i valori GSE/ARERA vigenti; non inventare tariffe unitarie.
5. Per il PNRR usa solo il pre-check: comune < 50.000 abitanti, soglia 1 MW, cronoprogramma letto nelle Regole.

## Output

```markdown
# Stima parametrica
- Energia immessa annua: [...]
- Energia prelevata annua: [...]
- Energia condivisa stimata: [...]
- Voci economiche da valorizzare con dati vigenti GSE: tariffa premio, contributo di valorizzazione, eventuale contributo PNRR
- Avvertenze: il calcolo ufficiale resta del GSE
```