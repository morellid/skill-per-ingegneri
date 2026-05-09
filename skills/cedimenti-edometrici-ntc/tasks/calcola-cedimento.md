# Calcola cedimento edometrico (NTC 2018 par. 6.2.4)

## Obiettivo

Stimare il cedimento edometrico Delta h di un singolo strato omogeneo sotto incremento uniforme di tensione, ai fini delle verifiche SLE NTC 2018 par. 6.2.4, usando il modulo code-driven `tasks/lib/cedimenti.py`.

## Input richiesti

Chiedi o ricava dall'utente:

| Campo         | Tipo   | Unita' | Note                                                                              |
|---------------|--------|--------|-----------------------------------------------------------------------------------|
| `h0`          | numero | m      | spessore iniziale dello strato compressibile                                      |
| `e0`          | numero | -      | indice dei vuoti iniziale, dalla relazione geotecnica                             |
| `Cc`          | numero | -      | indice di compressione (ramo vergine NC), dalla curva edometrica                  |
| `Cr`          | numero | -      | indice di ricompressione (ramo OC); tipicamente Cr / Cc in range 1/5 - 1/10       |
| `sigma_0`     | numero | kPa    | tensione efficace verticale media iniziale dello strato (geostatica)              |
| `sigma_p`     | numero | kPa    | tensione di preconsolidazione da prova edometrica (Casagrande / Janbu); >= sigma_0 |
| `delta_sigma` | numero | kPa    | incremento medio di tensione efficace verticale dovuto al carico applicato (>= 0) |

**Importante**: la skill **non stima i parametri edometrici**. Cc, Cr, e0, sigma_p' devono provenire dalla relazione geotecnica o da prove edometriche su campioni indisturbati. Se l'utente non li ha, NON inventarli: chiedere o segnalare la lacuna.

**Altra cura**: `delta_sigma` e' l'incremento di tensione efficace **medio** nel tratto considerato. Per fondazioni reali si calcola con sovrapposizione di Boussinesq / Steinbrenner / Mindlin a profondita'; questo calcolo e' fuori scope della skill e va fatto a parte.

## Schema JSON di input

```json
{
  "h0": 2.0,
  "e0": 0.8,
  "Cc": 0.30,
  "Cr": 0.05,
  "sigma_0": 100.0,
  "sigma_p": 150.0,
  "delta_sigma": 200.0
}
```

## Procedura

1. Acquisisci i campi sopra dall'utente. Se mancano, chiedi.
2. Salva il JSON in un file temporaneo.
3. Invoca il modulo:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/cedimenti.py --input-json /path/al/file.json
```

(in Codex / altri agent sostituisci `${CLAUDE_SKILL_DIR}` con il path assoluto della skill.)

4. Se il modulo solleva errore (campo mancante, Cr > Cc, sigma_p < sigma_0, delta_sigma < 0, input non finiti / negativi), riporta il messaggio bloccante e chiedi correzione all'utente. NON aggirare l'errore.
5. Riporta l'output del modulo nella forma:

```
Input
- Strato: h0 = ... m, e0 = ...
- Parametri edometrici: Cc = ..., Cr = ...
- Stato tensionale: sigma_0' = ... kPa, sigma_p' = ... kPa, Delta sigma' = ... kPa

Derivati
- sigma_f' = sigma_0' + Delta sigma' = ... kPa
- OCR = sigma_p' / sigma_0' = ...
- Ramo: ... (OC / NC / transizione)

Contributi
- Delta h (ramo OC) = ... m
- Delta h (ramo NC) = ... m

Output
- Delta h totale = ... m = ... mm
- epsilon medio = Delta h / h0 = ...
- Avvertenze: ...
```

6. Concludi con:

> Il cedimento e' una stima di pre-dimensionamento per singolo strato omogeneo, basata sulla formulazione classica della compressione monodimensionale (Terzaghi/Skempton). Per stratigrafie multilayer il progettista deve sommare i contributi strato per strato. Il confronto con il cedimento ammissibile (NTC par. 6.2.4) e la valutazione di cedimenti differenziali, distorsioni angolari e tempi di consolidazione restano in capo al progettista geotecnico firmatario.

## Casi particolari

- **Cr > Cc**: il modulo solleva ValueError. Riporta che il ramo di ricompressione deve avere indice <= ramo vergine; verificare i parametri edometrici.
- **OCR < 1 (sigma_p < sigma_0)**: il modulo solleva ValueError. Configurazione non fisicamente ammissibile; verificare la determinazione di sigma_p' (metodo Casagrande / Janbu).
- **Delta sigma = 0**: il modulo restituisce Delta h = 0 con avvertenza esplicita. Confermare con l'utente che e' il caso (es. controllo di consistenza pre-carico).
- **Delta sigma < 0 (scarico, rebound)**: il modulo solleva ValueError. La formula classica con Cr puo' essere applicata con segno opposto in scarico, ma la skill non lo copre per evitare ambiguita'; rinviare a calcolo specifico.
- **epsilon > 10%**: il modulo restituisce Delta h ma con avvertenza nel campo `output.avvertenze`. Riporta l'avvertenza chiaramente: per deformazioni elevate il metodo edometrico e' approssimato e va validato con prove specifiche o software dedicato.
- **Stratigrafia multilayer**: la skill copre singolo strato. Suggerire al progettista di ripetere il calcolo per ogni strato e sommare i contributi (Delta sigma' a profondita' calcolato separatamente con Boussinesq).

## Limiti del task

Vedi `SKILL.md` sezione "Limiti". In particolare la skill non copre stratigrafie multilayer, consolidazione 2D / 3D, cedimenti differenziali, cedimento immediato (elastico) o secondario (creep), scarichi, terreni granulari, terreni strutturati, tempi di consolidazione.
