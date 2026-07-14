# Note - parete con cappotto EPS, zona E (conforme)

## Perche' questo esempio e' importante

- Mostra il caso d'uso principale (Ecobonus): verifica U <= limite Appendice B
  del DM 26/06/2015 per una porzione di involucro riqualificata, con la citazione
  della tabella e zona precise.
- Espone il pattern del repo per le skill di calcolo: il modulo calcola dai dati
  dell'utente (lambda dalle schede, R_si/R_se da UNI EN ISO 6946) e verifica
  contro il limite normativo; **non inventa** i parametri fisici.

## Cosa insegna

- La resistenza e' dominata dallo strato isolante (l'EPS pesa per ~82%): la
  scelta e lo spessore dell'isolante determinano l'esito.
- Il limite corretto per il contesto Ecobonus e' l'**Appendice B** (edifici
  esistenti in riqualificazione), non l'Appendice A (edificio di riferimento).
- La verifica con U 1D e' **preliminare** perche' il limite del DM include i
  ponti termici: la skill lo dichiara sempre.
