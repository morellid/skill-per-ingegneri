# Task: imposta-verifica-fasce

Struttura la **richiesta dati** e l'impostazione della verifica delle **fasce di
rispetto** dell'elettrodotto rispetto all'obiettivo di qualita' (art. 6 DPCM 8/7/2003),
rinviando al DM 29/5/2008 per il calcolo della DPA.

## Input richiesti

- **Elettrodotto**: tensione, tipologia, gestore.
- **Sito**: presenza di aree sensibili / nuovi insediamenti in prossimita'.

## Procedura

1. **Riferimento** (art. 6 c.1): la fascia di rispetto si determina rispetto
   all'**obiettivo di qualita' (3 µT)** e alla **portata in corrente in servizio
   normale** della linea (norma **CEI 11-60**).
2. **Dati da richiedere al gestore**: portata in corrente in servizio normale,
   geometria/altezza dei conduttori, configurazione della linea. Ricorda che il
   gestore dichiara i dati **al Ministero dell'ambiente** (linee > 150 kV) o alle
   **Regioni** (linee <= 150 kV).
3. **Imposta la verifica**: confronto tra la posizione del sito/edificio e la fascia
   di rispetto comunicata/calcolata; identifica se il sito ricade in fascia.
4. **Calcolo della DPA / ampiezza fascia**: rinvia esplicitamente alla **metodologia
   del DM 29/5/2008** (delegata all'APAT dall'art. 6 c.2). La skill **non esegue** il
   calcolo numerico.
5. **Esito**: se il sito ricade in fascia (o supera i valori), segnala la necessita'
   di approfondimento tecnico/misura ARPA e di verifica progettuale.

## Output atteso

- Elenco dei **dati da acquisire** dal gestore (portata CEI 11-60, geometria).
- Schema della **verifica** rispetto all'obiettivo di qualita' e alla fascia.
- Rinvio al **DM 29/5/2008** per il calcolo della DPA e ad ARPA per le misure.

## Avvertenze

- L'**ampiezza della fascia / DPA** dipende dalla metodologia ufficiale (DM 29/5/2008):
  la skill imposta la verifica ma **non fornisce il valore** della distanza.
- La skill **non sostituisce** il calcolo del gestore/ARPA ne' la misura in campo.
