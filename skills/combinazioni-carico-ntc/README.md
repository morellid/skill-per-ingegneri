# combinazioni-carico-ntc

Skill code-driven per generare e verificare matrici di combinazioni delle azioni secondo NTC 2018 par. 2.5.3 per edifici civili e industriali correnti.

## Target

Ingegneri strutturisti che devono impostare, controllare o documentare combinazioni SLU/SLE/sismiche in modelli di calcolo o fogli di verifica.

## Cosa fa

- Genera combinazioni SLU fondamentali con profili gamma `EQU`, `A1`, `A2`
- Genera combinazioni SLE rara, frequente e quasi permanente
- Genera combinazioni sismiche ed eccezionali quando sono forniti `E` o `Ad`
- Usa coefficienti psi Tab. 2.5.I e gamma Tab. 2.6.I tramite modulo Python deterministico
- Esporta output JSON o tabella Markdown

## Fonti consultate

DM 17/01/2018 (NTC 2018), par. 2.5.2, 2.5.3 e 2.6.1. Dettaglio completo in `references/sources.yaml`.

## Limiti noti

La skill non decide l'elenco delle azioni da modellare, non calcola sollecitazioni o inviluppi FEM, e non sostituisce la verifica del progettista strutturale firmatario.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
