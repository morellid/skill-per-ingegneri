# Task: Determina il titolo edilizio in Toscana

## Obiettivo

Produrre un inquadramento preliminare e prudente tra edilizia libera, CILA, SCIA, SCIA alternativa e permesso di costruire.

## Input minimi

- descrizione dei lavori
- presenza o assenza di opere strutturali
- nuova costruzione / edificio esistente
- eventuale cambio d'uso
- comune

## Fonti da leggere

- `references/estratti/lr-65-2014-titoli-abilitativi.md`
- `references/estratti/dpr-380-2001-artt-zona-sismica.md`

## Procedura

1. Classifica l'intervento secondo l'art. 3 DPR 380/2001.
2. Se emerge sola manutenzione ordinaria o opera minore tipizzata, indica edilizia libera come ipotesi da confermare sul regolamento comunale.
3. Se l'intervento non interessa parti strutturali e non ricade negli artt. 6, 10 o 22 DPR 380/2001, indica la CILA come ipotesi coerente con l'art. 6-bis.
4. Se l'intervento interessa parti strutturali ma non appare riconducibile a nuova costruzione o ristrutturazione maggiore, orienta verso SCIA richiamando art. 22 DPR 380/2001 e art. 135 LR 65/2014.
5. Se l'intervento e' nuova costruzione o ristrutturazione piu' incisiva, orienta verso permesso di costruire richiamando art. 10 DPR 380/2001 e art. 134 LR 65/2014.
6. Se ci sono opere strutturali, aggiungi sempre: "verificare adempimenti sismici ai sensi degli artt. 93-94 DPR 380/2001 e del regolamento regionale 1/R/2022".
7. Se il comune non e' noto o la zona sismica non e' confermata, non inventarla: rinvia alla pagina regionale sulla classificazione sismica.

## Formato output

```markdown
# Inquadramento preliminare

- Titolo probabile: [...]
- Base normativa: [...]
- Ragione principale: [...]
- Verifiche obbligatorie residue:
  - regolamento edilizio / Piano Operativo comunale
  - zona sismica del comune su fonte regionale
  - eventuali atti di assenso esterni non trattati dalla skill
```

## Avvertenza finale

Specifica sempre che il risultato e' preliminare e richiede conferma del tecnico firmatario e del Comune.