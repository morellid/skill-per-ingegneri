# Input - Caso problematico: quota a_s > 1500 m

## Scenario

Rifugio alpino in alta quota: a_s = 2000 m s.l.m., zona vento 1, copertura a falde con alpha = 30 deg, zona neve I-Alpina, esposizione "battuta dai venti" (sito molto esposto in cresta).

## Parametri vento (input utente)

- `v_b_0 = 25.0 m/s` (Tab. 3.3.I zona 1)
- `a_0 = 1000 m` (Tab. 3.3.I zona 1)
- `k_s = 0.40` (Tab. 3.3.I zona 1)
- `a_s = 2000 m`     <-- FUORI DOMINIO della skill
- `categoria_esposizione = III`
- `z = 5.0 m`
- `c_p = 1.0`, `c_d = 1.0`, `c_t = 1.0`, `t_r_anni = 50`

## Parametri neve (input utente)

- `zona = I-Alpina`
- `a_s = 2000 m`
- `alpha_deg = 30`
- `classe_esposizione = battuta_dai_venti`
- `c_t = 1.0`

## Cosa ci si attende

- Per il vento: la skill deve **rifiutare** il calcolo perche' `a_s > 1500 m` e NTC par. 3.3.2 richiede indagine specifica (il modulo Python solleva ValueError).
- Per la neve: la skill esegue il calcolo (NTC par. 3.4 non ha limite superiore di altitudine), restituendo valori elevati di `q_sk` e `q_s` come e' lecito attendersi a 2000 m.
