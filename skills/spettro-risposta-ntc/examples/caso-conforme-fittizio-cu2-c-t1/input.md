# Input - caso conforme fittizio (CU II, C, T1)

> NB: i parametri di pericolosita' sono **fittizi** (non corrispondono a un sito reale del reticolo INGV). Sono scelti per essere ordinati e leggibili e coincidono con i valori usati come dataset di confronto della test suite.

> **Fonte autoritativa machine-readable:** [`input.json`](input.json). Questa pagina e' una sintesi umana derivata dallo stesso file. Il test `TestEsempioConforme.test_match_expected_json` (in `tasks/lib/test_spettro.py`) **legge `input.json` ed esegue il modulo**, poi confronta lo stdout col fixture [`expected.json`](expected.json): drift fra i due fixture o fra i fixture e il modulo viene segnalato dal test.

## Dati committente

- Costruzione residenziale ordinaria, cinque piani fuori terra.
- Localizzazione: sito generico in zona sismica medio-bassa (esempio didattico).

## Parametri di calcolo

(estratti da `input.json` -> `parametri_calcolo`)

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

(estratti da `input.json` -> `parametri_pericolosita_sito`)

| TR (anni) | ag (g) | F0    | Tc* (s) |
|-----------|--------|-------|---------|
| 30        | 0.030  | 2.50  | 0.20    |
| 50        | 0.045  | 2.55  | 0.22    |
| 72        | 0.061  | 2.60  | 0.24    |
| 101       | 0.080  | 2.62  | 0.26    |
| 140       | 0.105  | 2.65  | 0.28    |
| 201       | 0.135  | 2.68  | 0.30    |
| 475       | 0.218  | 2.72  | 0.32    |
| 975       | 0.297  | 2.74  | 0.34    |
| 2475      | 0.420  | 2.76  | 0.36    |

## Comando di riproduzione

Per replicare l'esempio, estrai i parametri di pericolosita' da `input.json` in un file JSON allineato col formato richiesto dal modulo (chiavi `tr_anni`, `ag_g`, `F0`, `Tc_star`) e invoca:

```bash
# Opzione A: estrai con jq i parametri di pericolosita' nel formato del modulo
jq '.parametri_pericolosita_sito' \
   ${CLAUDE_SKILL_DIR}/examples/caso-conforme-fittizio-cu2-c-t1/input.json \
   > /tmp/params-fittizio.json

# Opzione B (no jq): copia manualmente le 4 chiavi tr_anni/ag_g/F0/Tc_star
#                    in un file JSON minimo. Vedi struttura attesa in
#                    tasks/lib/spettro.py (carica_parametri_riferimento).

python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py \
    --tr-riferimento /tmp/params-fittizio.json \
    --vn 50 --classe-uso II \
    --cat-sottosuolo C --cat-topografica T1 \
    --stato-limite TUTTI \
    --tabula 0:4:0.1
```

Lo stdout in `--json` mode coincide con [`expected.json`](expected.json). Modificare `input.json` (qualunque valore) e lasciare invariato `expected.json` fa fallire `TestEsempioConforme`: questo e' il comportamento desiderato.
