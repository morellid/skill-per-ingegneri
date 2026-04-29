# Esempi - modulistica-edilizia-unificata

Esempi sintetici creati per test e validazione della skill. Nomi di immobili, indirizzi, anni, importi e localizzazioni sono fittizi e non riconducibili a interventi reali.

## Casi disponibili

### `manutenzione-frazionamento-cila/`
Inquadramento: manutenzione straordinaria di un appartamento di 92 mq SU in zona B di un Comune toscano, con frazionamento in due UI distinte, **senza opere su parti strutturali**, immobile non vincolato, stato legittimo accertato.
Esito atteso: regime **CILA** (art. 6-bis DPR 380), modulo CILA della modulistica unificata 2025, elenco allegati base + dichiarazione stato legittimo, no notifica preliminare (cantiere mono-impresa stimato sotto soglia D.Lgs. 81).

### `cambio-uso-salva-casa-scia/`
Inquadramento: cambio destinazione d'uso da residenziale (cat. a) a turistico-ricettivo (cat. a-bis - foresteria lombarda con 5 camere ai sensi art. 27 LR Lombardia 27/2015, fino a 6 camere e 14 posti letto), unita' singola di 110 mq SU in zona B di Milano, fuori centro storico, **senza opere edilizie strutturali** (solo aggiunta di un bagno con allacci esistenti), immobile non vincolato.
Esito atteso: regime **SCIA** ex art. 19 L. 241/1990 ai sensi dell'art. 23-ter co. 1-ter + 1-quinquies DPR 380 post Salva Casa (la SCIA del cambio uso assorbe la CILA delle opere accessorie); modulo SCIA della modulistica unificata 2025; allegati base + verifica condizioni regionali e comunali; **non sono dovuti** standard urbanistici ne' parcheggi minimi (art. 23-ter co. 1-quater); resta eventuale contributo per oneri di urbanizzazione secondaria. Avvertenza: oltre alla SCIA edilizia servono SCIA SUAP turismo ex art. 27 LR 27/2015 e codice CIN ai sensi L. 191/2023.

### `sanatoria-semplificata-art36bis/`
Inquadramento: parziale difformita' rispetto agli elaborati grafici di una SCIA del 2013 (ristrutturazione interna eseguita nel 2014); spostamento di un tramezzo non portante che ha modificato la dimensione del bagno e dell'antibagno; SU complessiva, numero UI, destinazione d'uso e parametri esterni invariati; appartamento di 75 mq in zona B di Brescia, immobile non vincolato. L'abuso ricade nel regime art. 37 DPR 380 (parziale difformita' da SCIA art. 22).
Esito atteso (verifica primaria): inquadramento come **tolleranza esecutiva** ex art. 34-bis co. 2 DPR 380 (Salva Casa), che NON richiede sanatoria. Esito atteso (verifica subordinata, se il SUE contesta la tolleranza): **SCIA in sanatoria art. 36-bis** (doppia conformita' alleggerita); termine art. 19 co. 6-bis L. 241/1990 (30 gg per i poteri inibitori in materia edilizia). NON e' applicabile l'art. 36 (riservato a opere PdC/SCIA-alternativa-dovute in assenza/totale difformita'); NON e' applicabile l'art. 6-bis co. 5 (riservato a CILA omessa, qui c'era SCIA 2013 regolare). Allegati: relazione tecnica asseverata + documentazione probante 2014 (foto, fatture, atti, fine lavori SCIA 2013) + sanzione pecuniaria graduata + stato legittimo della parte assentita.

## Convenzione struttura

Ogni caso e' organizzato come:

```
examples/<caso>/
|-- input.md           # dati di input forniti all'agent
|-- expected-output.md # output atteso (determinazione regime + allegati)
`-- note.md            # commenti di dominio sul caso
```
