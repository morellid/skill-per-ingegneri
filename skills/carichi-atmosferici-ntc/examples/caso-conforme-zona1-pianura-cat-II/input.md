# Input - Caso conforme: zona 1, pianura, categoria esposizione II

## Scenario

Edificio industriale a un piano in pianura piemontese (zona vento 1, zona neve I-Alpina), copertura a due falde simmetriche con inclinazione 20 deg. Sito a 350 m s.l.m., aperta campagna senza ostacoli rilevanti (categoria di esposizione II), 8 km dalla costa (non rilevante - sito interno). Quota di riferimento dell'elemento (intradosso copertura): 8 m. Periodo di ritorno standard 50 anni.

## Parametri vento (da NTC Tab. 3.3.I per zona 1, dichiarati dall'utente)

- `v_b_0 = 25.0 m/s`
- `a_0 = 1000 m`
- `k_s = 0.40`
- `a_s = 350 m`
- `categoria_esposizione = II`
- `z = 8.0 m`
- `c_p = 0.8` (parete sopravento, valore dell'utente da CNR-DT 207 / par. 3.3.8 NTC)
- `c_d = 1.0` (struttura ordinaria, par. 3.3.9 NTC)
- `c_t = 1.0`
- `t_r_anni = 50`

## Parametri neve (da NTC par. 3.4)

- `zona = I-Alpina`
- `a_s = 350 m`
- `alpha_deg = 20`
- `classe_esposizione = normale`
- `c_t = 1.0`

## Cosa ci si attende

Calcolo deterministico di pressione vento `p` e carico neve `q_s`, entrambi diversi da zero, con citazione dei paragrafi NTC.
