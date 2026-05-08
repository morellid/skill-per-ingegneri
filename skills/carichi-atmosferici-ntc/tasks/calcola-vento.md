# Calcola pressione vento (NTC 2018 par. 3.3)

## Obiettivo

Calcolare la pressione del vento `p` su un elemento dell'inviluppo dell'edificio, ai sensi di NTC 2018 par. 3.3, usando il modulo code-driven `tasks/lib/carichi_atmosferici.py` sotto-comando `vento`.

## Input richiesti

Chiedi o ricava dall'utente:

| Campo                   | Tipo    | Note                                                                                  |
|-------------------------|---------|---------------------------------------------------------------------------------------|
| `v_b_0`                 | numero  | velocita' base di riferimento (m/s) - da NTC Tab. 3.3.I per la zona del sito         |
| `a_0`                   | numero  | quota di riferimento (m) - da NTC Tab. 3.3.I                                          |
| `k_s`                   | numero  | coefficiente zonale - da NTC Tab. 3.3.I                                               |
| `a_s`                   | numero  | altitudine del sito (m s.l.m.); deve essere `<= 1500 m`                               |
| `categoria_esposizione` | stringa | `I`, `II`, `III`, `IV`, `V` - da NTC par. 3.3.7 / Tab. 3.3.III, dichiarata dall'utente |
| `z`                     | numero  | quota di riferimento dell'elemento (m)                                                |
| `c_p`                   | numero  | coefficiente di forma - dal progettista (par. 3.3.8 + CNR-DT 207)                     |
| `c_d`                   | numero  | coefficiente dinamico (default 1.0); != 1 solo per strutture sensibili (par. 3.3.9)   |
| `c_t`                   | numero  | coefficiente topografico (default 1.0)                                                |
| `t_r_anni`              | numero  | periodo di ritorno (default 50.0); intervallo valido `[5, 500]`                       |

**Importante**: la skill non incorpora Tab. 3.3.I e non assegna automaticamente la categoria di esposizione. Se l'utente non fornisce uno di questi valori, NON inventarli: chiedere o segnalare che il dato deve essere consultato sulla copia ufficiale di NTC.

## Schema JSON di input

```json
{
  "v_b_0": 25.0,
  "a_0": 1000.0,
  "k_s": 0.40,
  "a_s": 350.0,
  "categoria_esposizione": "II",
  "z": 10.0,
  "c_p": 0.8,
  "c_d": 1.0,
  "c_t": 1.0,
  "t_r_anni": 50.0
}
```

## Procedura

1. Acquisisci i campi sopra dall'utente. Se mancano, chiedi.
2. Salva il JSON in un file temporaneo.
3. Invoca il modulo:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/carichi_atmosferici.py vento --input-json /path/al/file.json
```

(in Codex / altri agent sostituisci `${CLAUDE_SKILL_DIR}` con il path assoluto della skill.)

4. Se il modulo solleva errore (campo mancante, `a_s > 1500 m`, `T_R` fuori intervallo, categoria invalida), riporta il messaggio bloccante e chiedi correzione all'utente. NON aggirare l'errore.
5. Riporta l'output del modulo nella forma:

```
Input
- Zona vento: v_b_0 = ..., a_0 = ..., k_s = ...    [NTC Tab. 3.3.I, valori dichiarati dall'utente]
- Altitudine sito a_s = ... m
- Categoria esposizione: ...                        [NTC Tab. 3.3.III, dichiarata dall'utente]
- Quota di riferimento z = ... m
- c_p = ..., c_d = ..., c_t = ..., T_R = ... anni

Valori intermedi
- v_b = ... m/s                  [eq. 3.3.2 NTC]
- c_r = ...                       [eq. 3.3.3 NTC, c_r = 1 per T_R = 50 anni]
- v_r = ... m/s
- q_r = ... N/m^2                 [eq. 3.3.4 NTC, rho = 1.25 kg/m^3]
- c_e = ...                       [eq. 3.3.5 NTC con k_r/z_0/z_min Tab. 3.3.II categoria ...]

Output
- p = ... N/m^2 = ... kN/m^2     [eq. 3.3.1 NTC]
```

6. Concludi con:

> L'output e' un valore caratteristico ai sensi di NTC par. 3.3. La combinazione SLU/SLE va eseguita a valle (vedi skill `combinazioni-carico-ntc`). c_p e' input dell'utente: la sua determinazione resta a carico del progettista (par. 3.3.8 + CNR-DT 207/2008). c_d = 1 e' valido solo per costruzioni di tipologia ricorrente (par. 3.3.9). Per strutture sensibili al vento o geometrie non correnti l'output va rivisto dal progettista strutturale firmatario.

## Casi particolari

- **a_s > 1500 m**: il modulo solleva ValueError. Riporta che NTC par. 3.3.2 richiede indagine specifica al sito; la skill non copre questa zona di altitudine.
- **T_R < 5 o > 500**: il modulo solleva ValueError. Riporta che la formula di c_r e' valida nell'intervallo dichiarato dalla Circolare C3.3; per periodi di ritorno fuori intervallo l'utente deve usare procedure specifiche.
- **Categoria di esposizione ambigua**: chiedi conferma all'utente o suggerisci di consultare NTC Tab. 3.3.III; non assegnare in autonomia.
- **z < z_min della categoria**: il modulo applica c_e(z_min) come da NTC eq. 3.3.5; e' comportamento corretto, comunicalo nella nota di output.

## Limiti del task

Vedi `SKILL.md` sezione "Limiti". In particolare la skill non calcola `c_p`, non fa analisi dinamica per `c_d`, non automatizza la classificazione della categoria di esposizione.
