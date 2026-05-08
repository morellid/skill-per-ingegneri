# Output atteso - Caso conforme: zona 1, pianura, categoria esposizione II

## Pressione vento (NTC par. 3.3)

### Input riportati
- `v_b_0 = 25.0 m/s`, `a_0 = 1000 m`, `k_s = 0.40` (Tab. 3.3.I, valori dichiarati dall'utente)
- `a_s = 350 m`
- Categoria esposizione: `II`
- `z = 8.0 m`, `c_p = 0.8`, `c_d = 1.0`, `c_t = 1.0`, `T_R = 50 anni`

### Valori intermedi
- `v_b = 25.0 m/s` (a_s <= a_0, eq. 3.3.2 NTC)
- `c_r = 1.0` (T_R = 50 anni, eq. 3.3.3 NTC)
- `v_r = 25.0 m/s`
- `q_r = 390.625 N/m^2` (eq. 3.3.4 NTC, rho = 1.25 kg/m^3)
- `c_e = 2.212338` (eq. 3.3.5 NTC con k_r=0.19, z_0=0.05, z_min=4.0 per cat. II)

### Output
- **p = 691.36 N/m^2 = 0.6914 kN/m^2** (eq. 3.3.1 NTC: p = q_r * c_e * c_p * c_d)

## Carico neve (NTC par. 3.4)

### Input riportati
- Zona: `I-Alpina`, `a_s = 350 m`
- `alpha = 20 deg`, classe esposizione: `normale`, `c_t = 1.0`

### Valori intermedi
- `q_sk = 1.711283 kN/m^2` (par. 3.4.2 NTC zona I-Alpina, a_s = 350 > 200 -> q_sk = 1.39 * [1 + (350/728)^2])
- `mu_1 = 0.8` (par. 3.4.5.2.1 NTC, alpha = 20 <= 30 deg)
- `c_E = 1.0` (Tab. 3.4.I, classe normale)

### Output
- **q_s = 1.369027 kN/m^2** (eq. 3.4.1 NTC: q_s = mu_1 * q_sk * c_E * c_t)

## Note

- L'output e' un valore caratteristico ai sensi di NTC par. 3.3 e par. 3.4. Va combinato con gli altri carichi (G1, G2, Q, eventuale E) tramite skill `combinazioni-carico-ntc` o software di calcolo strutturale.
- Per c_p = 0.8 il progettista ha implicitamente scelto una parete sopravento di edificio rettangolare (par. 3.3.8 NTC + CNR-DT 207); la skill non verifica questa scelta.
- Verifica del progettista strutturale firmatario obbligatoria prima del deposito.
