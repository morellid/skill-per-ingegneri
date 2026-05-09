# Input - Caso conforme: trave 300x500 con 3 phi 16, C25/30 + B450C

## Scenario

Trave in c.a. di edificio civile ordinario non sismico. Sezione rettangolare 300 mm x 500 mm, copriferro netto 30 mm + staffe phi 8 + barra principale phi 16 -> altezza utile `d ~= 500 - 30 - 8 - 16/2 = 454 mm`; per il pre-dimensionamento si assume `d = 460 mm` (margine prudenziale).

Armatura tesa: 3 barre phi 16 al lembo inferiore -> `A_s = 3 * pi * 16^2 / 4 = 603.19 mm^2`.

Materiali: calcestruzzo C25/30 (fck = 25 MPa), acciaio B450C (fyk = 450 MPa). Coefficienti parziali standard SLU PERS: `alpha_cc = 0.85`, `gamma_c = 1.5`, `gamma_s = 1.15`.

## Parametri (input modulo)

```json
{
  "b": 300,
  "h": 500,
  "d": 460,
  "As": 603.19,
  "fck": 25,
  "fyk": 450
}
```

(I coefficienti `alpha_cc`, `gamma_c`, `gamma_s`, `Es`, `eps_cu` sono lasciati ai default.)

## Cosa ci si attende

Sezione duttile (acciaio snerva, x/d << 0.45), M_Rd dell'ordine di 100 kNm. Output con citazione paragrafi NTC e nessuna avvertenza di duttilita'.
