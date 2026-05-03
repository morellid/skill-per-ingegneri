# Genera matrice combinazioni

## Obiettivo

Produrre una matrice di combinazioni delle azioni secondo NTC 2018 par. 2.5.3, usando il modulo code-driven `tasks/lib/combinazioni.py`.

## Input richiesti

Chiedi o ricava dall'utente:

- azioni permanenti: `name`, `kind` (`G1` o `G2`), `value`, effetto SLU (`favorevole` o `sfavorevole`);
- per ogni `G2`, se il carico permanente non strutturale e' compiutamente definito (`well_defined: true`) oppure no;
- eventuale precompressione `P`;
- azioni variabili: `name`, `category`, `value`, effetto SLU (`sfavorevole` default);
- profilo gamma SLU: `A1` default, oppure `EQU`/`A2`;
- eventuale `E` per combinazione sismica;
- eventuale `Ad` per combinazione eccezionale;
- formato output: `markdown` default, oppure `json`.

Categorie variabili supportate: `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `VENTO`, `NEVE_LE_1000`, `NEVE_GT_1000`, `TERMICA`.

## Schema JSON di input

```json
{
  "gamma_profile": "A1",
  "permanent_actions": [
    {"name": "G1", "kind": "G1", "value": 10.0, "effect": "sfavorevole"},
    {"name": "G2_pavimenti", "kind": "G2", "value": 2.0, "effect": "sfavorevole", "well_defined": false}
  ],
  "prestress": 0.0,
  "variable_actions": [
    {"name": "Q_A", "category": "A", "value": 3.0, "effect": "sfavorevole"},
    {"name": "Neve", "category": "NEVE_LE_1000", "value": 1.2, "effect": "sfavorevole"},
    {"name": "Vento", "category": "VENTO", "value": 0.8, "effect": "sfavorevole"}
  ],
  "seismic_action": 4.5,
  "exceptional_action": null
}
```

## Procedura

1. Prepara il JSON input in un file temporaneo.
2. Invoca il modulo:

```bash
python3 /path/assoluto/skills/combinazioni-carico-ntc/tasks/lib/combinazioni.py input.json --format markdown
```

3. Se il modulo segnala una categoria non supportata o un dato non numerico, chiedi correzione all'utente.
4. Riporta la tabella prodotta e una breve sezione "Assunzioni".

## Output atteso

Includi:

- profilo gamma usato;
- numero di combinazioni generate per tipo;
- tabella con `id`, `tipo`, `azione principale`, espressione e valore risultante;
- note su `G2` compiutamente definiti, variabili favorevoli, categorie non supportate;
- avvertenza finale: verifica del progettista strutturale.

## Limiti

Non convertire automaticamente i valori di carico tra unita' diverse. La skill preserva le unita' dell'input: se l'utente inserisce kN/m2, l'output resta in kN/m2 come combinazione scalare simbolica.
