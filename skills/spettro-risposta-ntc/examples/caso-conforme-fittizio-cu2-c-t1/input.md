# Input - caso conforme fittizio (CU II, C, T1)

> NB: i parametri di pericolosita' sono **fittizi** (non corrispondono a un sito reale del reticolo INGV). Sono scelti per essere ordinati e leggibili e coincidono con i valori usati come dataset di confronto della test suite.

## Dati committente

- Costruzione residenziale ordinaria, cinque piani fuori terra.
- Localizzazione: sito generico in zona sismica medio-bassa (esempio didattico).

## Parametri di calcolo

| Parametro                    | Valore     |
|------------------------------|------------|
| Vita nominale V_N            | 50 anni    |
| Classe d'uso                 | II (C_U=1.0) |
| Categoria di sottosuolo      | C          |
| Categoria topografica        | T1         |
| Smorzamento viscoso xi       | 5%         |
| Stati limite richiesti       | TUTTI      |
| Periodi di tabulazione       | 0:4:0.1 s (output sintetico) |

## Parametri di pericolosita' al sito

File JSON da fornire al modulo Python:

```json
{
  "tr_anni": [30, 50, 72, 101, 140, 201, 475, 975, 2475],
  "ag_g":    [0.030, 0.045, 0.061, 0.080, 0.105, 0.135, 0.218, 0.297, 0.420],
  "F0":      [2.50,  2.55,  2.60,  2.62,  2.65,  2.68,  2.72,  2.74,  2.76],
  "Tc_star": [0.20,  0.22,  0.24,  0.26,  0.28,  0.30,  0.32,  0.34,  0.36]
}
```

## Comando

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py \
    --tr-riferimento /tmp/params-fittizio.json \
    --vn 50 --classe-uso II \
    --cat-sottosuolo C --cat-topografica T1 \
    --stato-limite TUTTI \
    --tabula 0:4:0.1
```
