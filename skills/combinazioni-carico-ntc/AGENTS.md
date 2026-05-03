# AGENTS.md - combinazioni-carico-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Questa skill copre la generazione e verifica delle combinazioni delle azioni per edifici civili e industriali correnti secondo NTC 2018 par. 2.5.3. Il target e' il progettista strutturale che deve impostare matrici SLU/SLE/sismiche/eccezionali in fogli di calcolo o software FEM.

## Fonti autoritative

- `ntc2018-dm-17-01-2018` in `references/sources.yaml` - DM 17/01/2018, NTC 2018, GU n. 42 del 20/02/2018.

Estratti pertinenti gia' preparati in `references/estratti/`:

- `ntc2018-par-2-5-2-6.md` - Tab. 2.5.I coefficienti psi, par. 2.5.3 combinazioni, Tab. 2.6.I coefficienti gamma.

## Punti chiave

- **NTC 2018 par. 2.5.3**: definisce combinazione fondamentale SLU, SLE rara, SLE frequente, SLE quasi permanente, sismica ed eccezionale.
- **NTC 2018 Tab. 2.5.I**: coefficienti `psi0`, `psi1`, `psi2` per azioni variabili in edifici civili e industriali correnti.
- **NTC 2018 Tab. 2.6.I**: coefficienti parziali `gamma` per verifiche SLU nei profili `EQU`, `A1`, `A2`.

## Convenzioni specifiche

### Cosa non fare

- Non inventare coefficienti per categorie non precaricate, in particolare coperture praticabili o usi speciali da valutare caso per caso.
- Non calcolare matrici a mano quando e' disponibile il modulo `tasks/lib/combinazioni.py`.
- Non estendere automaticamente la skill a ponti, geotecnica o azioni speciali governate da capitoli NTC successivi.

### Cosa fare

- Eseguire il modulo Python per ogni matrice numerica.
- Dichiarare sempre profilo gamma (`A1` default, `A2` o `EQU`) e trattamento dei `G2` compiutamente definiti.
- Citare almeno par. 2.5.3 e, quando si discutono coefficienti, Tab. 2.5.I o Tab. 2.6.I.
- Concludere con il rinvio alla verifica del progettista strutturale firmatario.

## Validatori

- Non ancora identificato validatore di dominio terzo.

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1 automatizzato
- Task files: `genera-matrice-combinazioni.md`, `verifica-matrice-combinazioni.md`
- Esempi: 1 caso ordinario + 1 caso problematico
