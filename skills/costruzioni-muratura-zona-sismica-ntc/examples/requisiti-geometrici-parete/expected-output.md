# Esempio — Output atteso: verifica dei requisiti geometrici di una parete (Tab. 7.8.I)

> Supporto documentale (NTC 2018, par. 7.8.1.4). Il rispetto della Tab. 7.8.I è una **condizione geometrica
> necessaria**, non una verifica di resistenza dei pannelli (§§ 7.8.2-7.8.4, fuori scope).

## Riga pertinente della Tab. 7.8.I

Muratura **ordinaria, elementi artificiali**, sito con agS > 0,15g → riga **base**:
**t_min = 240 mm**; **(h0/t)_max = 12**; **(l/h')_min = 0,4**.

## Calcoli e confronto

| Requisito | Formula | Valore | Limite (Tab. 7.8.I) | Esito |
|---|---|---|---|---|
| Spessore | t | 250 mm | ≥ 240 mm | ✅ |
| Snellezza | λ = h0/t = 3000/250 | 12,0 | ≤ 12 | ✅ (al limite) |
| Snellezza della parete | l/h' = 1,60/2,20 | 0,73 | ≥ 0,4 | ✅ |

- **t = 250 mm ≥ 240 mm** → verificato.
- **λ = h0/t = 3000/250 = 12,0 ≤ 12** → verificato (esattamente al limite: qualsiasi aumento di h0 o
  riduzione di t renderebbe la parete non conforme).
- **l/h' = 1,60/2,20 = 0,73 ≥ 0,4** → verificato.

## Distanza tra i solai (§7.8.1.4)

- Interpiano **3,20 m ≤ 5 m** → **conforme** al requisito «distanza massima tra due solai successivi ≤ 5 m».

## Sintesi

La parete **rispetta** tutti i requisiti geometrici della **Tab. 7.8.I** (t, h0/t, l/h') per la muratura
ordinaria in elementi artificiali, e l'interpiano è entro i 5 m. La snellezza è **al limite** (12,0): attenzione
in caso di varianti su h0 o t.

**Fuori scope**: le verifiche di **resistenza** dei maschi murari (pressoflessione nel piano e fuori piano,
taglio) restano a carico del progettista (§7.8.2). La skill non sostituisce il progettista.
