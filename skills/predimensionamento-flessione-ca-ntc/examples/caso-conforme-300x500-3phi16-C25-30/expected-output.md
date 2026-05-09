# Output atteso - Caso conforme: trave 300x500 con 3 phi 16, C25/30 + B450C

## Input riportati

- Geometria: `b = 300 mm`, `h = 500 mm`, `d = 460 mm`
- Armatura tesa: `A_s = 603.19 mm^2` (3 phi 16)
- Materiali: `fck = 25 MPa` (C25/30), `fyk = 450 MPa` (B450C)
- Coefficienti: `alpha_cc = 0.85`, `gamma_c = 1.5`, `gamma_s = 1.15`, `Es = 200000 MPa`, `eps_cu = 0.0035`

## Materiali derivati

- `f_cd = 14.166667 MPa` (eq. 4.1.4 NTC: 0.85 * 25 / 1.5)
- `f_yd = 391.304348 MPa` (par. 4.1.2.1.1.3 NTC: 450 / 1.15)
- `eps_yd = 0.001957` (par. 4.1.2.1.1.2 NTC: f_yd / Es = 391.30 / 200000)

## Geometria interna

- `x = 69.420844 mm` (equilibrio: x = (A_s * f_yd) / (0.8 * b * f_cd))
- `x/d = 0.150915` (ben sotto 0.45)
- `eps_s = 0.019692` (>> eps_yd = 0.001957: acciaio snerva ampiamente)
- `z = d - 0.4 x = 432.231662 mm` (braccio leva)

## Output

- **M_Rd = 102020015.130857 Nmm = 102.020015 kNm** (par. 4.1.2.3.4.2 NTC: M_Rd = A_s * f_yd * z)
- Duttile snervamento acciaio: **true**
- Duttile x/d <= 0.45: **true**
- Avvertenze: nessuna

## Note

- L'output e' un pre-dimensionamento ai sensi di NTC par. 4.1.2.3.4.2. Il confronto `M_Ed <= M_Rd = 102 kNm` resta in capo al progettista, dopo aver calcolato le sollecitazioni di una combinazione SLU (vedi skill `combinazioni-carico-ntc`).
- La sezione e' ampiamente duttile (acciaio snerva con eps_s = 0.019692, ~ 10 volte eps_yd; x/d = 0.151 << 0.45 raccomandato).
- Restano da verificare separatamente: taglio (NTC par. 4.1.2.3.5), fessurazione e deformabilita' SLE (NTC par. 4.1.2.2), eventuali requisiti sismici (NTC par. 7.4.4 / 7.4.6 se zona sismica con q > 1.5).
- Verifica del progettista strutturale firmatario obbligatoria prima del deposito o asseverazione.
