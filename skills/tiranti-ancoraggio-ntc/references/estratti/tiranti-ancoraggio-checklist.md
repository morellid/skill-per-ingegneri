# Estratto operativo - Tiranti di ancoraggio (NTC 2018 §6.6)

> Parafrasi ancorata a `references/fonti/ntc2018-par-6-6.md`. Ogni voce cita il paragrafo/tabella/formula NTC.
> La skill **inquadra** criteri, verifica SLU a sfilamento e prove di carico; **non** calcola la resistenza,
> **non** dimensiona il tirante né la sua armatura.

## 1. Definizione e criteri di progetto (§6.6, §6.6.1)

- **Tiranti di ancoraggio** = elementi strutturali collegati al terreno che sostengono **trazione**.
- Classificazione: **provvisori / permanenti**; **attivi (presollecitati) / passivi (non presollecitati)**.
- Nel progetto vanno indicati: **orientazione, lunghezza, numero** degli ancoraggi, tecnica e tolleranze,
  **resistenza di progetto Rad**, eventuale **programma di tesatura**, manutenzione e monitoraggio.
- Evitare la sovrapposizione tra la **zona passiva** dell'ancoraggio e la **zona attiva** a tergo dell'opera di
  sostegno.
- **La conferma sperimentale con prove di trazione in sito (in progetto e in corso d'opera) è sempre
  necessaria.**

## 2. Verifica di sicurezza SLU - sfilamento (§6.6.2)

- Condizione **[6.2.1]**: **Ed ≤ Rad** rispetto allo stato limite di **sfilamento** della fondazione
  dell'ancoraggio.
- Combinazione di verifica: **A1+M1+R3** (coefficienti Tab. 6.2.I, 6.2.II e **6.6.I**).
- **Resistenza di progetto**: **Rad = Rak / γR** con **Tab. 6.6.I**:

| Ancoraggio | γR |
|---|---|
| **Temporaneo** | **1,1** |
| **Permanente** | **1,2** |

### Resistenza caratteristica Rak
- **(a) da prove di progetto** [6.6.1]: **Rak = Min{ Ra,m,medio / ξa1 ; Ra,m,min / ξa2 }** con ξ da **Tab.
  6.6.II**:

| Numero ancoraggi di prova | 1 | 2 | > 2 |
|---|---|---|---|
| ξa1 | 1,5 | 1,4 | 1,3 |
| ξa2 | 1,5 | 1,3 | 1,2 |

- **(b) da calcolo analitico** [6.6.2]: **Rak = Min{ Ra,c,medio / ξa3 ; Ra,c,min / ξa4 }** con ξ da **Tab.
  6.6.III**:

| Numero profili di indagine | 1 | 2 | 3 | 4 | ≥ 5 |
|---|---|---|---|---|---|
| ξa3 | 1,80 | 1,75 | 1,70 | 1,65 | 1,60 |
| ξa4 | 1,80 | 1,70 | 1,65 | 1,60 | 1,55 |

- Nella valutazione **analitica** non si applicano γ ai parametri di resistenza del terreno → si usa **M1**.

## 3. Aspetti costruttivi (§6.6.3)

- Ancoraggi attivi: **sistemi qualificati** (§11.5.2); durabilità, compatibilità e protezione dalla corrosione
  **documentate**.
- **Diametro dei fori ≥ diametri nominali** di progetto.
- **Tesatura** in conformità al programma, non prima che siano esauriti presa e indurimento della fondazione.

## 4. Prove di carico (§6.6.4)

- **Prove di progetto** su ancoraggi preliminari (non riutilizzabili), stesso sistema/sito/condizioni; numero
  minimo (§6.6.4.1):

| Numero ancoraggi | < 30 | 31-50 | 51-100 | 101-200 | 201-500 | > 500 |
|---|---|---|---|---|---|---|
| N° minimo prove di progetto | 1 | 2 | 3 | 7 | 8 | 10 |

- **Prove in corso d'opera** su **tutti** gli ancoraggi (§6.6.4.2): ciclo semplice carico/scarico con forza
  pari a **1,2·Pd** (Pd = azione di progetto per le verifiche SLE), controllando gli allungamenti.

## Cosa la skill NON fa

- **Non calcola** la resistenza allo sfilamento né **dimensiona** il tirante o la sua armatura; **non** valuta
  Ra,m/Ra,c al posto del progettista.
- **Non riproduce** le procedure di dettaglio delle prove di carico, i **sistemi di ancoraggio come prodotti**
  (§11.5.2), le **paratie/muri** (§6.5, skill `opere-sostegno-ntc`) né la **progettazione sismica** (Cap. 7).
- **Non sostituisce** il progettista geotecnico/strutturale né la lettura del §6.6 delle NTC 2018 e della
  Circolare applicativa.
