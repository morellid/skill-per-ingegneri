# Task: inquadra-limite-applicabile

Dato il sito e l'uso, individua **quale grandezza** del D.P.C.M. 8/7/2003 si applica
(limite di esposizione / valore di attenzione / obiettivo di qualita') e il relativo
valore.

## Input richiesti

- **Sorgente**: tipo di elettrodotto (linea/sottostazione/cabina) e tensione (per
  capire chi riceve i dati: > 150 kV Ministero, <= 150 kV Regioni).
- **Sito**: destinazione d'uso (area gioco per l'infanzia, ambiente abitativo,
  ambiente scolastico, altro) e **tempo di permanenza** (>= 4 ore/die?).
- **Stato**: situazione **esistente** oppure **nuova** progettazione (nuovo
  elettrodotto o nuova area/insediamento presso linee esistenti).

## Procedura

1. **Verifica il campo di applicazione** (art. 1): sorgente a 50 Hz ed esposizione
   della popolazione (non professionale).
2. **Applica sempre il limite di esposizione** (art. 3 c.1): 100 µT (induzione
   magnetica) e 5 kV/m (campo elettrico), valori efficaci.
3. **Valore di attenzione 10 µT** (mediana 24 h) se il sito e' area gioco/abitativo/
   scolastico o con permanenza >= 4 h (art. 3 c.2).
4. **Obiettivo di qualita' 3 µT** (mediana 24 h) se si progetta un **nuovo**
   elettrodotto presso tali aree, o **nuove aree** presso linee esistenti (art. 4).
5. **Riepiloga** la grandezza applicabile, il valore e la base (articolo), segnalando
   che la **verifica numerica** richiede misure/calcoli ufficiali.

## Output atteso

- Grandezza applicabile (limite/attenzione/qualita') con valore e articolo.
- Note sul tipo di area e sullo stato (esistente/nuovo) che determinano la scelta.
- Rinvio a misura ARPA (CEI 211-6) e, per le fasce, al task `imposta-verifica-fasce`.

## Avvertenze

- Non confondere il **valore efficace** (limite) con la **mediana 24 h** (attenzione/
  qualita').
- La skill **non misura** il campo: la determinazione spetta ad ARPA/tecnici.
