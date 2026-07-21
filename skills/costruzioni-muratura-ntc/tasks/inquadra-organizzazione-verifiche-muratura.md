# Task - Inquadra l'organizzazione strutturale e le verifiche della muratura (§4.5.4, 4.5.6.2, 4.5.6.4)

## Obiettivo

Inquadrare i requisiti di **organizzazione strutturale** (spessori minimi, snellezza, collegamenti), le
**verifiche agli stati limite ultimi** e le **verifiche semplificate** per edifici semplici, secondo le
NTC 2018 §4.5.

## Input richiesti

- geometria dei muri (spessore t, altezza interpiano h) e tipo di muratura;
- condizioni di vincolo (muri trasversali di irrigidimento) e aperture;
- caratteristiche dell'edificio (numero di piani, regolarità in pianta, carichi variabili) per la via
  semplificata.

## Procedura (ancorata al testo)

1. **Organizzazione strutturale** (§4.5.4). Verificare il **comportamento scatolare** (cordoli di piano in
   c.a., ammorsamenti, incatenamenti). Rispettare gli **spessori minimi** dei muri portanti: artificiali
   **pieni 150**, **semipieni 200**, **forati 240 mm**; pietra **squadrata 240**, **listata 400**, **non
   squadrata 500 mm**. Controllare la **snellezza convenzionale λ = h0/t** [4.5.1]: **λ ≤ 20**.

2. **Verifiche SLU** (§4.5.6.2). Considerare: **pressoflessione fuori piano**, **pressoflessione nel
   piano**, **taglio nel piano**, **carichi concentrati**, travi di accoppiamento; trascurare la
   resistenza a trazione per flessione. Per i **carichi laterali**, con articolazione completa, è
   consentito il **metodo semplificato**: **fd,rid = Φ·fd** [4.5.4], con **Φ** dalla **Tab. 4.5.III** in
   funzione di **λ** e del coefficiente di eccentricità **m = 6 e/t**; **h0 = ρ·h** con ρ = 1 (muro
   isolato) o dalla **Tab. 4.5.IV**. Le **eccentricità** (es, **ea = h/200**, **ev = Mv/N**) si combinano
   in e1 ed e2, con **e1 ≤ 0,33 t** ed **e2 ≤ 0,33 t** [4.5.11].

3. **Verifiche semplificate** (§4.5.6.4). Ammesse per **edifici semplici** con **γM = 4,2** se: pareti
   continue; interpiano ≤ **3,5 m**; **≤ 3 piani** (ordinaria) / **4** (armata); rapporto fra i lati in
   pianta **≥ 1/3**; **snellezza ≤ 12**; carico variabile ≤ **3,00 kN/m²**; percentuali minime di parete
   (Tab. 7.8.II). Verifica: **σ = N/(0,65 A) ≤ fk/γM** [4.5.12] (N con γG = γQ = 1; A area dei muri
   portanti al piano).

4. **SLE** (§4.5.6.3). Generalmente non necessari se sono soddisfatti gli SLU.

## Output

Una nota che indichi: il rispetto degli **spessori minimi** e della **snellezza**; gli **SLU** da
verificare e l'eventuale **metodo semplificato** (Φ, ρ, eccentricità); l'applicabilità delle **verifiche
semplificate** (γM = 4,2) con i loro limiti. **La skill inquadra requisiti e metodi; non esegue le
verifiche né dimensiona la muratura.**
