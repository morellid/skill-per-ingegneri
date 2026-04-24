# Note di dominio - caso `coerenza-buona-demolizioni`

## Cosa stiamo testando

Che la skill riconosca come **coerente** un POS che ha chiaramente associato ogni rischio a una o piu' misure specifiche, con tecnica adeguata alla magnitudo dichiarata. Controlla che non ci siano falsi positivi su POS ben strutturati.

## Scelte progettuali del caso

- **Cantiere demolizione** (non nuova costruzione): profilo di rischi piu' alto della media, rende il test significativo - 8 rischi distinti, ognuno con magnitudo dichiarata.
- **Misure multi-livello**: per ogni rischio, il POS dichiara misure a piu' livelli (collettive + individuali + organizzative + formative). Questo test verifica che la skill non sia troppo rigida ("1 rischio = 1 misura").
- **EN richiamate**: il POS cita norme specifiche (EN 361 imbracature, EN ISO 10819 guanti antivibrazione). La skill dovrebbe riconoscerle come segnale positivo, non fingere di verificarle.
- **Misure organizzative** (rotazioni, orari, referenti): per rischi non tecnici (interferenza condomini). Test: la skill non classifica come "debole" una misura organizzativa appropriata al rischio.

## Output atteso

`COERENTE` con 0 problemi rilevati, 3 raccomandazioni di completamento (non critiche).

## Cose che la skill DOVREBBE fare

- Riconoscere che ogni rischio ha **piu'** misure (approccio stratificato) - non segnalare ridondanza.
- Accettare richiami a EN specifiche come segnale di qualita'.
- Riconoscere misure **non-tecniche** (orari concordati, avvisi) come appropriate per rischi relazionali.
- Distinguere "misura integrativa del POS" da "rinvio generico al PSC".

## Cose che la skill NON dovrebbe fare

- **Falso positivo** per "troppe misure" su R1: le misure sono stratificate (ponteggio + linea vita + imbracatura + formazione), non ridondanti.
- **Falso negativo** su R8 per assenza di DPI: il rischio e' relazionale, non richiede DPI.
- **Pretendere di verificare** la correttezza delle EN richiamate (e' verifica tecnica che richiede conoscenza puntuale della norma).

## Cosa imparare

- Un buon POS mostra il matching rischio-misura in forma **esplicita** ("relativamente a R1...", "relativamente a R2...") - rende la verifica facile.
- Misure "stratificate" (collettive + individuali + organizzative + formative) sono il benchmark di qualita'.
- La skill puo' dare valore aggiunto principalmente dove il matching e' **implicito** o **assente** (vedi caso `coerenza-incoerente-boilerplate`).

## Fonte della struttura

POS fittizio creato per test. Ispirato alla pratica comune per cantieri di demolizione interna in edifici abitati.
