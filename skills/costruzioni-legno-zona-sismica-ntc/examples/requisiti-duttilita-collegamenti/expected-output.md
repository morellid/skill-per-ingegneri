# Esempio — Output atteso: requisiti di duttilità di un collegamento legno-acciaio (§7.7.3.1)

> Supporto documentale (NTC 2018, par. 7.7). Il rispetto delle prescrizioni geometriche del §7.7.3.1 è
> condizione per considerare la zona dissipativa: non è una verifica di resistenza (fuori scope).

## Regola applicabile

Collegamento **legno-acciaio** con mezzi a gambo cilindrico → si applica la **regola a) del §7.7.3.1**:
diametro **d ≤ 12 mm** e spessore delle membrature lignee collegate **≥ 10d**.

## Calcoli e confronto

| Requisito (§7.7.3.1 a) | Limite | Valore | Esito |
|---|---|---|---|
| Diametro dei mezzi di unione | d ≤ 12 mm | d = 10 mm | ✅ |
| Spessore membrature lignee | ≥ 10d = 10 × 10 = 100 mm | 90 mm | ❌ (< 100 mm) |

- **d = 10 mm ≤ 12 mm** → verificato.
- **Spessore richiesto per la regola piena: 10d = 100 mm**; disponibile **90 mm** → **non** soddisfa il requisito
  «pieno» per la CD "A".
- **Requisito alternativo (§7.7.3.1)**: se è comunque assicurato lo spessore minimo **≥ 8d = 80 mm** (caso a), la
  zona dissipativa è da considerare in **CD "B"**. Qui **90 mm ≥ 80 mm** → **ammissibile in CD "B"**.

## 2. Classe di duttilità risultante

- Con **spessore 90 mm** (tra 8d = 80 mm e 10d = 100 mm) il collegamento **non** raggiunge il requisito «pieno» e
  quindi la zona dissipativa **non può essere assunta in CD "A"** su questa base: risulta ammissibile in **CD "B"**.
- Per la **CD "A"** occorrerebbe portare lo spessore delle membrature ad **almeno 100 mm** (10d), oppure ridurre
  d, o giustificare la duttilità con la via prestazionale prevista dal §7.7.3.1 (cerniera plastica nel gambo,
  evidenze sperimentali).

## 3. Regola di dettaglio (§7.7.7.1)

- **d = 10 mm ≤ 16 mm** → rispetta il limite: perni/bulloni con **d > 16 mm** non sono ammessi nei collegamenti
  legno-legno/legno-acciaio (salvo come elementi di chiusura). **Nessun problema.**

## Sintesi

- Regola a) del §7.7.3.1: **d = 10 mm OK**, ma **spessore 90 mm < 10d (100 mm)**.
- Con **90 mm ≥ 8d (80 mm)** la zona dissipativa è ammissibile in **CD "B"**, non in CD "A" su base geometrica.
- Diametro entro il limite di dettaglio (d ≤ 16 mm).

**Fuori scope**: la verifica di resistenza/duttilità del collegamento, il q0 numerico e la relativa capacità
dissipativa restano a carico del progettista (RES §7.3.6.1, con resistenza ridotta del 20%). Non sostituisce il
progettista.
