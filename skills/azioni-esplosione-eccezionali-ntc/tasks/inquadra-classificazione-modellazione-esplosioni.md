# Task - Inquadra la classificazione e la modellazione delle esplosioni (§3.6.2.2-3.6.2.3)

## Obiettivo

Inquadrare la **classificazione** delle azioni dovute alle esplosioni e la loro **modellazione** come pressioni
statiche equivalenti, secondo le NTC 2018 §3.6.2.2-3.6.2.3.

## Input richiesti

- tipo di ambiente (presenza di miscele esplosive di polveri/gas o materiali esplosivi);
- categoria di azione attesa (1/2/3) in funzione degli effetti;
- per la Categoria 2: presenza e caratteristiche dei **pannelli di sfogo** (pv, area Av, volume V).

## Procedura (ancorata al testo)

1. **Ambito** (§3.6.2.1). Verificare che si tratti di esplosioni **interne** (miscele di polveri/gas o
   materiali esplosivi); le esplosioni **esterne** sono escluse.

2. **Classificazione** (§3.6.2.2, Tab. 3.6.I). Individuare la **categoria**: 1 (effetti trascurabili), 2
   (localizzati), 3 (generalizzati).

3. **Modellazione** (§3.6.2.3):
   - **Categoria 1**: **nessuna verifica**.
   - **Categoria 2** (con pannelli di sfogo): calcolare la pressione statica equivalente nominale pd [kN/m²]
     come **valore maggiore** fra **pd = 3 + pv** [3.6.5a] e **pd = 3 + pv/2 + 0,04/(Av/V)²** [3.6.5b], con pv
     pressione di cedimento delle aperture, Av area, V volume. Verificare il vincolo **0,05 m⁻¹ ≤ Av/V ≤ 0,15
     m⁻¹** [3.6.6] e la validità per **volume ≤ 1.000 m³**; la pressione agisce **simultaneamente su tutte le
     pareti**. Per gli **elementi chiave** e le connessioni assumere **pd = 20 kN/m²** da ogni direzione.
   - **Categoria 3**: **studi più approfonditi**.

## Output

Una nota che indichi: la **categoria** di azione, l'eventuale **pd** (max fra [3.6.5a] e [3.6.5b]) con la
verifica del vincolo [3.6.6] e del volume, e la pressione di **20 kN/m²** per gli elementi chiave. **La skill
inquadra la modellazione; non calcola le sollecitazioni né verifica gli elementi.**
