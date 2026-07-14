# Output atteso - parete con cappotto EPS, zona E (conforme)

Comando:

```bash
python3 tasks/lib/trasmittanza.py \
  --strato "intonaco_int:0.015:0.70" --strato "muratura_laterizio:0.25:0.40" \
  --strato "eps_grafitato:0.12:0.031" --strato "rasante:0.010:0.90" \
  --rsi 0.13 --rse 0.04 --zona E --regime riqualificazione --anno 2021
```

## Risultato

- **U = 0,213 W/(m2 K)** (R_tot = 4,699 m2 K/W = 0,13 + 4,529 + 0,04)
- Resistenza degli strati: intonaco int 0,021 + muratura 0,625 + EPS 3,871 +
  rasante 0,011 = 4,529 m2 K/W (il cappotto EPS pesa per l'82% della resistenza)
- **Limite DM 26/06/2015** (Appendice B, Tabella 1, strutture opache verticali,
  zona E, colonna 2021): **U <= 0,28 W/(m2 K)**
- **Esito: 0,213 <= 0,28 -> VERIFICA SODDISFATTA**

## Avvertenze (da riportare integralmente)

- Il limite del DM **include l'effetto dei ponti termici**; questa U e' calcolata
  in regime monodimensionale e **non** li include: la verifica e' **preliminare**.
  Con un margine di 0,067 W/(m2 K) rispetto al limite, un ponte termico moderato
  potrebbe erodere il margine ma difficilmente ribaltare l'esito; la verifica
  completa (UNI EN ISO 14683/10211) resta a carico del progettista.
- lambda e R_si/R_se sono dati forniti dall'utente (schede tecniche, UNI EN ISO
  6946): il modulo non li verifica ne' li stima.
- La skill non sostituisce la relazione tecnica ex art. 8 D.Lgs. 192/2005.
