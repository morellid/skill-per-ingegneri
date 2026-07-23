# Task: inquadra-grandezze-e-rumore-impianti

Inquadra le **grandezze e gli indici di valutazione** dei requisiti acustici passivi e i **limiti del rumore degli
impianti tecnologici** secondo il **DPCM 5 dicembre 1997 (Allegato A)**. Supporto documentale: **non** calcola gli
indici.

## Quando usarla

Il progettista/tecnico deve capire quali grandezze descrivono i requisiti acustici passivi e come si tratta il
rumore degli impianti. Per la categoria dell'ambiente e i valori limite della Tab. B usa
`classifica-ambiente-e-valori-limite`.

## Passi

1. **Grandezze di riferimento** (Allegato A):
   - **T** - tempo di riverberazione (ISO 3382:1975);
   - **R** - potere fonoisolante apparente di elementi di separazione fra ambienti (EN ISO 140-5:1996);
   - **D2m,nT** - isolamento acustico standardizzato di facciata, definito da

         D2m,nT = D2m + 10 log (T / T0)

     con D2m = L1,2m − L2 (differenza di livello), L1,2m livello esterno a 2 m dalla facciata, L2 livello medio
     nell'ambiente ricevente, T tempo di riverberazione dell'ambiente ricevente e **T0 = 0,5 s** (tempo di
     riferimento);
   - **L'n** - livello di rumore di calpestio di solai normalizzato (EN ISO 140-6:1996);
   - **LASmax** - livello massimo di pressione sonora ponderata A con costante di tempo slow;
   - **LAeq** - livello continuo equivalente di pressione sonora ponderata A.
2. **Indici di valutazione** (Allegato A): **R'w** (potere fonoisolante apparente di partizioni), **D2m,nT,w**
   (isolamento di facciata), **L'n,w** (calpestio). R'w e D2m,nT,w si calcolano secondo **UNI 8270:1987 Parte 7,
   para. 5.1**; L'n,w secondo **UNI 8270:1987 Parte 7, para. 5.2**. (Sono gli indici usati nella Tab. B.)
3. **Rumore degli impianti tecnologici** (Allegato A): la rumorosità prodotta dagli impianti non deve superare:
   - **35 dB(A) LASmax** (costante slow) per i **servizi a funzionamento discontinuo** (ascensori, scarichi
     idraulici, bagni, servizi igienici, rubinetteria — art. 2 c.3);
   - **25 dB(A) LAeq** per i **servizi a funzionamento continuo** (riscaldamento, aerazione, condizionamento —
     art. 2 c.4).
4. **Postazione di misura** (Allegato A): le misure vanno eseguite nell'**ambiente in cui il livello di rumore è
   più elevato**, che deve essere **diverso da quello in cui il rumore si origina**.

Usa la checklist in `../references/estratti/requisiti-acustici-passivi-checklist.md` (sezioni 1 e 2).

## Output atteso

Un inquadramento che indichi le grandezze/indici (R'w, D2m,nT,w con D2m,nT = D2m + 10 log(T/T0), L'n,w, LASmax,
LAeq) e i limiti del rumore degli impianti (35 dB(A) LASmax discontinuo, 25 dB(A) LAeq continuo) con la postazione
di misura, con **rinvio all'Allegato A** del DPCM. Nessun calcolo degli indici.

## Cosa NON fare

- Non **calcolare** gli indici (R'w, D2m,nT,w, L'n,w) né eseguire le misure: rinvia alle norme UNI/ISO citate e al
  tecnico competente in acustica.
- Non trattare i valori limite per categoria (Tab. B): usa `classifica-ambiente-e-valori-limite`.
