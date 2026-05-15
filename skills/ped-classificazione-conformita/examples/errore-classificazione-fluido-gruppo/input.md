# Esempio - input (caso problematico: classificazione errata del fluido)

## Descrizione attrezzatura

Serbatoio di accumulo per **propano liquido** in impianto di stoccaggio
industriale fisso:

- Tipo: recipiente cilindrico orizzontale.
- Pressione massima ammissibile **PS** = 18 bar (relativi).
- Volume proprio **V** = 5.000 litri.
- Fluido contenuto: **propano** (C3H8, CAS 74-98-6).
- Stato fisico operativo: liquido in pressione (sopra il punto di
  ebollizione standard, contenuto in pressione - GPL).
- Temperatura massima ammissibile **TS** = 50 gradi C; temperatura minima
  ammissibile -20 gradi C.
- Scheda di sicurezza del fluido (estratto): propano e' classificato CLP
  come **gas infiammabile categoria 1** (H220 "gas estremamente
  infiammabile"). Punto di infiammabilita': non applicabile (gas).
- Destinazione: stoccaggio per uso industriale.
- Produzione: pezzo unico su specifica del cliente.
- Data prevista di immissione sul mercato: 2026-10-15.
- Fabbricante: societa' italiana.

## Richiesta dell'utente (con errore implicito)

> "Devo classificare questo serbatoio di propano. Il propano e' un GPL,
> mi pare di ricordare che e' un fluido di gruppo 2 perche' lo trattiamo
> come gas comune in officina. Volume 5.000 litri, PS 18 bar, ricado in
> categoria II o III? Per la categoria II posso usare il modulo A2 o D1,
> giusto? Vorrei evitare il modulo H."

## Tipo di errore atteso

L'utente assume erroneamente che il propano sia fluido di **gruppo 2**.
La skill deve rilevare l'errore, ri-classificare il fluido in **gruppo 1**
(perche' il propano e' classificato CLP "gas infiammabile categoria 1",
una delle 17 classi di pericolo dell'art. 9 c. 1 lett. a del D.Lgs
26/2016), e ri-eseguire da capo la determinazione di categoria sulla
**tabella 1** (recipienti gas/vapori gruppo 1) e non sulla tabella 2.
Cio' modifica radicalmente la categoria attesa e i moduli ammissibili.
