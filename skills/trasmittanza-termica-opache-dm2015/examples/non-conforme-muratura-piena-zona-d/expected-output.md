# Output atteso - muratura piena, zona D (non conforme)

Comando (con flag isolamento interno, che alza il limite del 30%):

```bash
python3 tasks/lib/trasmittanza.py \
  --strato "intonaco_int:0.015:0.70" --strato "muratura_piena:0.30:0.72" \
  --strato "intonaco_est:0.020:0.90" \
  --rsi 0.13 --rse 0.04 --zona D --regime riqualificazione --anno 2021 \
  --isolamento-interno
```

## Risultato

- **U = 1,587 W/(m2 K)** (R_tot = 0,630 m2 K/W): la muratura piena senza
  isolamento ha resistenza bassissima.
- **Limite base DM** (Appendice B, Tab. 1, zona D, 2021): **0,32 W/(m2 K)**.
- Con **isolamento dall'interno o in intercapedine** il limite e' incrementato
  del **+30%** (Cap. 5 par. 5.2 DM 26/06/2015): **0,32 x 1,30 = 0,416 W/(m2 K)**.
- **Esito: 1,587 > 0,416 -> VERIFICA NON SODDISFATTA** anche col limite maggiorato.

## Interpretazione

- Lo stato di fatto e' lontanissimo dal limite: per rispettare 0,416 W/(m2 K)
  (limite maggiorato) o meglio 0,32 (limite base) serve uno strato isolante
  significativo. Esempio: aggiungendo all'interno ~6-8 cm di isolante con
  lambda ~0,032 la parete puo' rientrare - il progettista dimensiona lo spessore
  con il modulo iterando sulla stratigrafia di progetto.
- L'incremento +30% e' un'agevolazione prevista dal DM proprio perche'
  l'isolamento dall'interno riduce lo spessore utile e comporta piu' ponti
  termici; non e' un'esenzione: qui il limite maggiorato resta comunque non
  rispettato allo stato di fatto.

## Avvertenze (da riportare integralmente)

- Il limite del DM include i ponti termici; la U 1D no: verifica preliminare.
  Con l'isolamento dall'interno i ponti termici (solai, pilastri) sono
  particolarmente critici e vanno verificati a parte (UNI EN ISO 14683/10211).
- lambda e R_si/R_se sono dati dell'utente; la skill non li stima.
- La skill non sostituisce la relazione tecnica ex art. 8 D.Lgs. 192/2005.
