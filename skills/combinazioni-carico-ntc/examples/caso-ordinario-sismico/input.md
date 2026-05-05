# Input

Richiesta: genera la matrice combinazioni NTC 2018 con profilo gamma A1.

```json
{
  "gamma_profile": "A1",
  "permanent_actions": [
    {"name": "G1", "kind": "G1", "value": 10.0, "effect": "sfavorevole"},
    {"name": "G2", "kind": "G2", "value": 2.0, "effect": "sfavorevole", "well_defined": false}
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
