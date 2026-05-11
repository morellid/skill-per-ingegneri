# Input - Caso problematico: sezione sovra-armata

## Scenario

Stessa trave 300 x 500 mm, `d = 460 mm`, ma con armatura tesa molto elevata: ipoteticamente `A_s = 3500 mm^2` (es. 7 phi 25 o equivalente). Calcestruzzo C25/30, acciaio B450C.

Questa configurazione produce un asse neutro `x` cosi' profondo che l'acciaio teso non raggiunge lo snervamento prima che il calcestruzzo collassi (`eps_s < eps_yd`): la sezione e' **sovra-armata**.

## Parametri (input modulo)

```json
{
  "b": 300,
  "h": 500,
  "d": 460,
  "As": 3500,
  "fck": 25,
  "fyk": 450
}
```

## Cosa ci si attende

La skill deve **rifiutare** il calcolo: il modulo solleva `ValueError` con messaggio esplicito che cita "sovra-armata" e suggerisce le possibili soluzioni (aumentare b/h, ridurre A_s, sezione doppiamente armata fuori scope skill v0.1). L'agent deve riportare il messaggio bloccante senza aggirarlo.
