# Task: Verifica perimetro e prerequisiti GSE

## Obiettivo

Produrre un pre-check operativo sul fatto che la configurazione possa essere portata in domanda al GSE.

## Input minimi

- POD di produzione e consumo
- comune / indirizzo dei POD
- potenza impianto
- nominativo o ipotesi di referente
- interesse o meno al contributo PNRR

## Fonti da leggere

- `references/estratti/gse-regole-operative-cacer.md`
- `references/estratti/dm-mase-414-2023.md`

## Procedura

1. Verifica se l'utente ha gia' controllato la cabina primaria sul portale GSE.
2. Se non l'ha fatto, non dedurla offline: indica come azione obbligatoria il controllo sul portale GSE Autoconsumo.
3. Controlla la soglia di potenza: se il singolo impianto supera 1 MW, segnala che esce dal perimetro incentivante CACER letto nelle Regole.
4. Controlla se esiste o va individuato un referente.
5. Se l'utente punta al PNRR, segnala la necessita' di verificare comune sotto 50.000 abitanti e cronoprogramma GSE.

## Output

```markdown
# Pre-check operativo GSE
- Cabina primaria: verificata / da verificare sul portale GSE
- Potenza impianto: compatibile / non compatibile con soglia 1 MW
- Referente: individuato / da individuare
- PNRR: potenzialmente valutabile / non valutabile / da verificare
- Prossime azioni: [...]
```