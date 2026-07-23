# Task — Verifica i requisiti geometrici delle pareti (NTC 2018 §7.8.1.4, Tab. 7.8.I)

Supporto documentale per confrontare la geometria delle pareti resistenti al sisma di un edificio in muratura
con i **criteri di progetto e i requisiti geometrici** del par. 7.8.1.4 delle NTC 2018 (DM 17/1/2018), in
particolare la **Tab. 7.8.I**. **Non** sostituisce le verifiche di resistenza dei pannelli.

Fonte: `../references/fonti/ntc2018-par-7-8-1.md`; checklist: `../references/estratti/muratura-sismica-checklist.md`.

## Input tipico

- Tipologia costruttiva: muratura **ordinaria (pietra squadrata / elementi artificiali)**, **armata**,
  **confinata**; per i casi speciali, agS di sito (≤ 0,15g o ≤ 0,075g) e tipo di elemento (semipieno/pieno).
- Per ogni parete resistente al sisma: **spessore t** (al netto dell'intonaco), **altezza di libera inflessione
  h0** (§4.5.6.2), **lunghezza l**, **altezza massima h'** delle aperture adiacenti.
- Schema di piano (compattezza/simmetria) e continuità delle pareti in elevazione; interpiano (distanza solai).

## Passi

1. **Criteri di progetto (§7.8.1.4, qualitativi)**
   - Piante **compatte e simmetriche** rispetto ai due assi ortogonali.
   - Pareti strutturali **continue in elevazione fino alla fondazione** (niente **pareti in falso**).
   - Orizzontamenti/coperture **non spingenti**; solai a funzione di **diaframma**.
   - **Distanza massima tra due solai successivi ≤ 5 m**.

2. **Requisiti geometrici delle pareti (Tab. 7.8.I)** — per ogni parete calcola:
   - **t** e confrontalo con **t_min**;
   - la **snellezza λ = h0/t** e confrontala con **(h0/t)_max**;
   - il **rapporto l/h'** e confrontalo con **(l/h')_min**.

   | Tipologia costruttiva | t_min | (h0/t)_max | (l/h')_min |
   |---|---|---|---|
   | Ordinaria, elementi in pietra squadrata | 300 mm | 10 | 0,5 |
   | Ordinaria, elementi artificiali | 240 mm | 12 | 0,4 |
   | Armata, elementi artificiali | 240 mm | 15 | Qualsiasi |
   | Confinata | 240 mm | 15 | 0,3 |
   | Ordinaria pietra squadrata, siti con agS ≤ 0,15g | 240 mm | 12 | 0,3 |
   | Artificiali semipieni, siti con agS ≤ 0,075g | 200 mm | 20 | 0,3 |
   | Artificiali pieni, siti con agS ≤ 0,075g | 150 mm | 20 | 0,3 |

3. **Output**: tabella parete-per-parete con t / λ=h0/t / l/h' calcolati, i limiti della riga pertinente e
   l'esito (rispettato / non rispettato). Segnala che il rispetto della Tab. 7.8.I è **condizione geometrica
   necessaria**, non una verifica di resistenza.

## Cosa NON fare

- Non confondere la Tab. 7.8.I (**geometria**) con le **verifiche** dei pannelli (§§ 7.8.2-7.8.4): queste ultime
  restano fuori scope.
- Non applicare la riga «agS ≤ 0,15g» o «agS ≤ 0,075g» senza aver verificato l'accelerazione di sito.
- Non inventare valori: ogni limite deve essere rintracciabile in `../references/fonti/ntc2018-par-7-8-1.md`.
