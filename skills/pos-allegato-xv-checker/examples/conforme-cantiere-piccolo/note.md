# Note di dominio - caso `conforme-cantiere-piccolo`

## Cosa stiamo testando

Che la skill riconosca come **conforme** un POS ben redatto per un piccolo cantiere di ristrutturazione, senza falsi positivi su voci correttamente compilate.

## Scelte progettuali del caso

- **Cantiere piccolo**: 3 dipendenti, importo EUR 45k, 60gg. Scenario tipico di piccola impresa edile italiana. Deliberatamente semplice per non indurre il modello a falsi positivi su complessita' gestionale.
- **Ruoli combinati**: Luigi Bianchi fa sia direttore tecnico che capocantiere. Questo e' **legittimo** per cantiere piccolo ma il modello dovrebbe segnalarlo come nota di verifica al CSE (non come violazione). Test importante: distingue "legittimamente semplificato" da "inadeguatamente semplificato".
- **Subappalto**: ElettroLivorno per impianto elettrico, rinvio a POS separato. Test: il modello non deve pretendere che un POS copra tutti i lavori, se alcuni sono subappaltati con POS proprio.
- **Rinvio al DVR per rumore**: la voce f) rinvia al DVR aziendale. Il modello deve accettarlo come pratica standard, ma segnalare la verifica che il DVR copra effettivamente le lavorazioni del cantiere.
- **Allegati referenziati**: il POS cita Allegati A-H ma non li include. Il modello non puo' verificare il contenuto degli allegati, deve esplicitare questo limite.

## Output atteso

`CONFORME CON NOTE MINORI` con 2 note di priorita' bassa, entrambe legittime. Nessun problema bloccante.

## Cose che il modello NON dovrebbe fare

- **Falso positivo per ruoli combinati**: classificare come "non conforme" il doppio ruolo direttore tecnico/capocantiere. Questo e' ammissibile per cantiere di questa dimensione.
- **Falso positivo per rinvio al DVR**: pretendere che la valutazione rumore sia ripetuta integralmente nel POS. Il rinvio al DVR e' prassi consolidata.
- **Falso positivo per subappalto non coperto**: segnalare come mancante l'assenza di dettagli sull'impresa subappaltatrice oltre al rinvio. L'impresa esecutrice ha POS proprio.

## Cose che il modello DOVREBBE fare

- Riconoscere i 7 sotto-punti della voce a) come tutti presenti.
- Accettare la motivazione per le SDS non richieste (tinte a base acqua).
- Riconoscere la natura "integrativa" (non duplicativa) delle misure specifiche.
- Segnalare come nota (non errore) il ruolo combinato e la dipendenza dal DVR.

## Cosa imparare da questo caso

- Il POS non deve essere lungo per essere conforme. Un POS di 3-5 pagine ben compilate e' migliore di 40 pagine di boilerplate.
- Il rinvio a documenti esterni (DVR, PSC, POS di subappaltatori) e' legittimo e comune.
- La struttura tabellare per i DPI e' una buona pratica che rende facile la verifica.

## Fonte della struttura

POS fittizio creato per test. Struttura ispirata alla pratica comune italiana per piccole imprese edili. Nessun riferimento a imprese, persone o indirizzi reali.
