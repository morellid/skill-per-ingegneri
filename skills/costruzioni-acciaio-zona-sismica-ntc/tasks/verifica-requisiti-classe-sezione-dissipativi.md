# Task — Verifica classe della sezione e requisiti degli elementi dissipativi (NTC 2018 §7.5.3, Tab. 7.5.I)

Supporto documentale per confrontare gli elementi dissipativi di una struttura in acciaio in zona sismica con le
**regole generali** del par. 7.5.3 delle NTC 2018 (DM 17/1/2018), in particolare la **classe della sezione
trasversale** (Tab. 7.5.I) e il limite sullo sforzo normale delle colonne dei telai. **Non** sostituisce le
verifiche di resistenza/duttilità.

Fonte: `../references/fonti/ntc2018-par-7-5.md`; checklist: `../references/estratti/acciaio-sismica-checklist.md`.

## Input tipico

- Classe di duttilità adottata (**CD "A"** o **CD "B"**) e **valore di base q0** utilizzato in progetto.
- Sezioni degli **elementi dissipativi** (profili) e loro **classe di sezione** (1, 2, 3, 4) secondo il §4.2.3.1.
- Per le **colonne primarie** dei telai con zone dissipative: **NEd** (domanda a sforzo normale) e **Npl,Rd**.
- (Facoltativo) capacità del collegamento in zona dissipativa Rj,d e capacità plastica Rpl,Rd della membratura.

## Passi

1. **Zone dissipative e capacity design (§7.5.3)**
   - Le zone dissipative sono **localizzate nelle membrature**: i **collegamenti** e le componenti non dissipative
     devono avere **adeguata capacità**.
   - Capacity design del collegamento in zona dissipativa: **Rj,d ≥ 1,1·γov·Rpl,Rd** [7.5.1].
   - Duttilità locale **μ = θu/θy**; la capacità al collasso θu si valuta alla **riduzione del 15%** della
     resistenza massima dell'elemento.

2. **Classe della sezione trasversale (Tab. 7.5.I)** — confronta CD e q0 con la classe della sezione:

   | Classe di duttilità | Valore di base q0 | Classe di sezione richiesta |
   |---|---|---|
   | CD "B" | 2 < q0 ≤ 4 | Classe 1 o 2 |
   | CD "A" | q0 > 4 | Classe 1 |

   - Verifica che la classe delle sezioni degli elementi dissipativi sia **compatibile** con la riga pertinente.

3. **Colonne primarie dei telai (§7.5.3)**
   - Per le sezioni delle **colonne primarie** dei telai in cui si prevede la formazione di zone dissipative:
     **NEd/Npl,Rd ≤ 0,3** [7.5.3].

4. **Output**: tabella elemento-per-elemento con classe di sezione richiesta (Tab. 7.5.I) ed esito, più l'esito
   del limite NEd/Npl,Rd ≤ 0,3 per le colonne dei telai. Segnala che il rispetto di Tab. 7.5.I e del limite è
   **condizione necessaria** per la duttilità, non una verifica di resistenza.

## Cosa NON fare

- Non confondere Tab. 7.5.I (**classe della sezione**) con le **verifiche** RES/DUT di membrature e collegamenti
  e con le regole specifiche per tipologia (§§ 7.5.3.1-7.5.3.2, 7.5.4-7.5.6): restano fuori scope.
- Non applicare la riga CD "A" (q0 > 4) o CD "B" (2 < q0 ≤ 4) senza aver individuato la classe di duttilità e il
  q0 effettivamente adottati.
- Non inventare valori: ogni limite deve essere rintracciabile in `../references/fonti/ntc2018-par-7-5.md`.
