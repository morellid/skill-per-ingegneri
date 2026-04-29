# Input - caso conforme fittizio (CU II, C, T1)

> **Fonte autoritativa machine-readable:** [`input.json`](input.json). Tutti i parametri di calcolo (V_N, classe d'uso, categorie sottosuolo/topografica, smorzamento, stati limite, periodi di tabulazione) e tutti i parametri di pericolosita' al sito (ag/F0/Tc* ai 9 TR di riferimento) sono lì. Questa pagina e' un sommario umano del JSON; in caso di discrepanza prevale il JSON.

> **Anti-drift attivo.** Il test `TestEsempioConforme.test_match_expected_json` (in `tasks/lib/test_spettro.py`) carica `input.json`, invoca il modulo, e verifica che lo stdout coincida bit-per-bit con [`expected.json`](expected.json). Il test `TestCLI.test_input_json_equivalente_ai_flag_scalari` aggiunge il check sul comando di riproduzione documentato qui sotto. Modificare `input.json` senza rigenerare `expected.json` fa fallire i test.

> **NB:** i parametri di pericolosita' sono **fittizi** (non corrispondono a un sito reale del reticolo INGV). Sono scelti per essere ordinati e leggibili.

## Dati committente

- Costruzione residenziale ordinaria, cinque piani fuori terra.
- Localizzazione: sito generico in zona sismica medio-bassa (esempio didattico).

## Sommario parametri (estratti da `input.json`)

`parametri_calcolo`: V_N=50 anni, classe d'uso II, categoria sottosuolo C, categoria topografica T1, smorzamento xi=5%, stati limite TUTTI (SLO+SLD+SLV+SLC), tabulazione 0:4:0.1 s.

`parametri_pericolosita_sito`: 9 valori di ag/F0/Tc* per i TR di riferimento {30, 50, 72, 101, 140, 201, 475, 975, 2475} anni. Vedi `input.json` per i numeri esatti.

## Comando di riproduzione

Il modulo Python supporta il flag `--input-json` per leggere tutto da un singolo file (eliminando la duplicazione di parametri):

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py \
    --input-json ${CLAUDE_SKILL_DIR}/examples/caso-conforme-fittizio-cu2-c-t1/input.json \
    --json
```

Lo stdout coincide bit-per-bit con [`expected.json`](expected.json).
