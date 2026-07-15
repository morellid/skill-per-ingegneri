# Task: inquadra-eccezionalita

Determina se un veicolo o un trasporto e' eccezionale (art. 10 CdS), se serve
l'autorizzazione alla circolazione e chi la rilascia, e il tipo di autorizzazione.

## Input richiesto

- Dimensioni (sagoma) e massa del veicolo/complesso e del carico.
- Numero di assi del veicolo/complesso.
- Tipo di carico (cosa indivisibile? generi tipizzati del c. 2 lett. b?).
- Rete stradale interessata (autostrade/statali/militari vs restante rete).
- Ripetitivita' del trasporto (percorsi ripetuti con sagome simili).

## Procedura

1. **Eccezionalita' (art. 10 c. 1-2)**:
   - **Veicolo eccezionale** se supera i limiti di **sagoma (art. 61)** o **massa
     (art. 62)** (c. 1).
   - **Trasporto in condizioni di eccezionalita'** se trasporta **cose
     indivisibili** eccedenti la sagoma nel rispetto della massa (c. 2 lett. a),
     oppure eccede **congiuntamente** sagoma e massa dei generi tipizzati (c. 2
     lett. b) con massa complessiva fino a **38/48/86/108 t** secondo gli assi.
   - **Non eccezionale**: veicolo del c. 1 che circola entro i limiti (c. 11);
     traino di veicoli in avaria entro i limiti (c. 12). **Esclusi**: macchine
     agricole/operatrici eccezionali (c. 26).
   - **La skill non calcola sagoma/massa**: rinvia agli artt. 61 e 62 per i valori.

2. **Serve l'autorizzazione? (c. 6, 7, 11, 15)**:
   - **Sì** in generale (c. 6): autorizzazione alla circolazione.
   - **No/particolari**: mezzi d'opera art. 54 c. 1 lett. n) che eccedono la sola
     massa a certe condizioni (c. 7); veicoli entro i limiti (c. 11); mai per i
     motoveicoli (c. 15).

3. **Chi la rilascia (c. 6)**: **ente proprietario o concessionario** per
   autostrade, strade statali e militari; **regioni** per la restante rete
   (secondo il rispettivo ordinamento).

4. **Tipo di autorizzazione (c. 9, 2-bis)**: **singola** (volta per volta),
   **multipla** (piu' transiti) o **periodica** (periodi di tempo); per i percorsi
   ripetitivi con sagome simili -> **periodica** ex art. 13 semplificata (c. 2-bis).

## Output

- Esito: veicolo/trasporto eccezionale sì/no, con il comma.
- Necessita' di autorizzazione e **ente competente** (in via generale, senza
  individuare il singolo ente).
- Tipo di autorizzazione consigliato (singola/multipla/periodica).
- Avvertenza: i limiti di sagoma/massa e l'ente/il percorso vanno verificati sugli
  artt. 61/62 e con l'ente competente.

## Regole

- Non calcolare sagoma/massa: rinviare agli artt. 61 e 62.
- Citare il comma dell'art. 10; distinguere veicolo (c. 1) e trasporto (c. 2).
- Non individuare nel merito il singolo ente/percorso.
