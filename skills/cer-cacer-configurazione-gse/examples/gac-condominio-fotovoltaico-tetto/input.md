# Input - GAC condominiale con FV in copertura (caso problematico)

Caso: l'amministratore di un **condominio urbano in una grande citta' metropolitana del Nord Italia** (popolazione del Comune ben superiore a 50.000 abitanti -> nessun accesso al contributo PNRR neanche nel regime esteso post DM MASE 127/2025) chiede di "fare una CER" sfruttando un impianto FV in copertura.

Caratteristiche dichiarate:

- Edificio plurifamiliare con 24 unita' abitative + 2 unita' commerciali al piano terra (un negozio di abbigliamento di proprieta' di **una grande catena nazionale di moda** e un bar di gestione familiare).
- Impianto FV in copertura, **80 kW**, da realizzare con investimento del condominio.
- POD prelievo: 24 utenze residenziali + 2 utenze commerciali, tutti connessi in BT, tutti nello stesso edificio.
- POD immissione: 1, lo stesso edificio.
- Il negozio di moda e' una **filiale di una catena con > 250 dipendenti** -> **grande impresa**.

L'amministratore vuole accedere alla TIP per ridurre le spese condominiali. Chiede:

1. confermare se la configurazione corretta e' "CER" (come gli e' stato proposto da un fornitore);
2. impostare lo statuto;
3. simulare i flussi economici.

Dati per la simulazione:

- producibilita': 1.250 kWh/kWp/anno (valore dichiarato dal progettista, sulla base di simulazione PVGIS sito-specifica - copertura piana con strutture a portrait, Pianura Padana);
- consumi annui aggregati dichiarati: 95.000 kWh;
- impianto in BT;
- Comune con popolazione molto superiore a 50.000 ab. -> niente contributo PNRR neanche nel regime esteso post DM 127/2025;
- fattore di condivisione `eta_share` ipotizzato dal progettista: 0,40 (mix residenziale + due attivita' commerciali diurne, no accumulo, valore da rivedere su profili orari).
