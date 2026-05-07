# Input - CER su Comune piccolo con cumulo TIP + contributo PNRR

Caso: un piccolo Comune dell'Appennino tosco-emiliano con popolazione di circa 1.800 abitanti (sotto soglia PNRR sia nel regime originario DM 414/2023 a 5.000 ab. sia in quello esteso post DM 127/2025 a 50.000 ab.) vuole costituire una **CER** insieme a:

- 35 nuclei familiari residenti (persone fisiche);
- 4 PMI locali del settore turistico (B&B, ristorante, falegnameria) - per nessuna l'attivita' principale e' produzione di energia;
- il Comune stesso, attraverso 2 POD di edifici scolastici e 1 POD del municipio;
- la parrocchia (1 POD).

L'impianto previsto e' un **fotovoltaico da 350 kW** in copertura su un capannone comunale dismesso, gia' di proprieta' del Comune. Tutti i POD prelievo e il POD immissione ricadono nella stessa cabina primaria, secondo verifica fatta sul portale GSE.

Obiettivi dichiarati dai promotori:

- riduzione costi energia per le famiglie e le PMI;
- accesso al **contributo PNRR** per Comuni con popolazione inferiore alla soglia (sotto 5.000 ab. nel testo originario del DM 414/2023, sotto 50.000 ab. nel regime esteso post DM 127/2025; il presente caso rientra in entrambi);
- destinazione di una quota dei benefici a un fondo locale per la riduzione della poverta' energetica.

L'utente chiede di:

1. validare la configurazione (CER e' corretta?);
2. impostare lo statuto;
3. fare una simulazione di massima dei flussi economici;
4. preparare la lista documenti per il GSE.

Dati per la simulazione:

- producibilita' attesa: 1.150 kWh/kWp/anno (valore dichiarato dal progettista sulla base di simulazione PVGIS sito-specifica per il sito di copertura, inclinazione 15 gradi);
- consumi annui aggregati dichiarati: 320.000 kWh (somma dei consumi annui dei POD partecipanti);
- impianto in BT;
- comune attestato a popolazione 1.812 abitanti (ISTAT 31/12/2025);
- costo investimento totale stimato: 420.000 EUR;
- fattore di condivisione `eta_share` ipotizzato dal progettista: 0,45 (mix residenziale + PMI turismo, senza accumulo, supportato da analisi semplificata di sovrapposizione tra profilo di produzione FV e profilo aggregato di prelievo dei POD; valore da rivedere su profili orari).
