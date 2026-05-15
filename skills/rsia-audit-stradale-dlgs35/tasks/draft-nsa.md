# Task: Redazione NSA (Valutazione della Sicurezza Stradale a Livello di Rete)

## Obiettivo

Supportare l'impostazione e la redazione della **Valutazione della Sicurezza Stradale a Livello di Rete (NSA - Network Safety Assessment)** ai sensi del nuovo art. 5 del D.Lgs 35/2011 (testo sostituito dall'art. 3 del D.Lgs 213/2021), su rete stradale aperta al traffico. La NSA sostituisce la "classificazione dei tratti ad elevata concentrazione di incidenti" prevista dal testo originale dell'art. 5 ed e' la procedura quinquennale per valutare il rischio di incidente e la gravita' dell'impatto sull'intera rete.

## Input richiesti

1. **Verifica preliminare ambito**: eseguita ai sensi di `check-ambito-applicazione.md`. La NSA si applica all'intera rete stradale aperta al traffico oggetto del decreto.
2. **Perimetro della rete oggetto della valutazione** (estensione km, classificazione delle tratte, eta' del tratto - le tratte aperte al traffico da oltre tre anni sono soggette a un esame specifico di incidentalita').
3. **Anno di prima esecuzione**: la prima NSA doveva essere eseguita entro e non oltre il **2024** (art. 5, comma 3 nuovo testo). Le successive sono effettuate **almeno ogni cinque anni**.
4. **Dati disponibili**: relazioni di incidente (art. 7), dati di traffico (TGM, composizione, motocicli/pedoni/biciclette osservati e stimati), caratteristiche di progettazione delle tratte (sezione tipo, allineamento, manto, segnaletica), dati pregressi di sicurezza, AINOP (segnalazioni spontanee ex art. 6-quinquies).
5. **Organo competente** che esegue la NSA (Stato, Regione, Provincia, concessionario autostradale, ecc., a seconda della rete).

## Fonti

- Estratto del nuovo art. 5 D.Lgs 35/2011 (testo introdotto dall'art. 3 D.Lgs 213/2021): `references/estratti/dlgs-213-2021.md` sezione "Art. 3".
- Estratto del nuovo art. 6-bis (Seguito delle procedure per le strade aperte al traffico, inserito dall'art. 5 D.Lgs 213/2021): `references/estratti/dlgs-213-2021.md` sezione "Art. 5 - Art. 6-bis".
- Estratto del nuovo Allegato III (sostituito dall'art. 13 D.Lgs 213/2021): `references/estratti/dlgs-213-2021.md` sezione "Art. 13".

## Procedura

### Step 1 - Definizione del perimetro e dei dati

L'NSA copre **l'intera rete stradale aperta al traffico oggetto del decreto** (art. 5, comma 1 nuovo testo). Verificare:

- l'inclusione di tutte le tratte di competenza dell'organo competente;
- l'aggiornamento dell'elenco delle strade dell'art. 1, comma 5 (autostrade, strade principali) trasmesso alla Commissione UE.

### Step 2 - Elementi della valutazione (art. 5, comma 2 nuovo testo)

La NSA si fonda su due elementi:

- **a) Indagine visiva** (in loco o con mezzi elettronici) delle caratteristiche di progettazione della strada al fine di valutarne la **sicurezza intrinseca**. Pianificare il programma di rilievo (manuale, video-monitoraggio, dati LiDAR, sopralluoghi mirati).
- **b) Analisi dei tratti aperti al traffico da oltre tre anni** in cui e' stato registrato un numero considerevole di **incidenti gravi in proporzione al flusso di traffico**. Definire la metrica (es. tasso incidenti gravi per veicoli-km, per intersezione).

### Step 3 - Componenti indicative (nuovo Allegato III)

La valutazione tiene conto delle **componenti indicative dell'Allegato III** (sostituito dall'art. 13 D.Lgs 213/2021). Le 11 macro-categorie sono:

1. **Aspetti generali**: tipo di strada, lunghezza tratto, zona (extraurbana/urbana), uso del suolo, densita' punti di accesso, strade di servizio, lavori, parcheggi.
2. **Volume di traffico**: TGM, volume motocicli, pedoni (lungo carreggiata o in attraversamento) e biciclette osservati, veicoli pesanti, flussi stimati pedoni/biciclette.
3. **Dati sugli incidenti**: numero, ubicazione e causa degli incidenti mortali e con feriti gravi per gruppo di utenti.
4. **Caratteristiche operative**: limite di velocita' (generale, motocicli, camion), velocita' di esercizio (85esimo percentile), gestione velocita', dispositivi STI (segnalatori code, pannelli a messaggio variabile), segnali presso scuole.
5. **Caratteristiche geometriche**: sezione trasversale (numero/tipo/larghezza corsie, banchine, mediane, piste, sentieri), curvatura orizzontale, grado e allineamento verticale, visibilita' e distanze di visibilita'.
6. **Oggetti, zone libere da ostacoli, sistemi stradali di contenimento**: ambiente al margine, ostacoli fissi (pali, alberi), distanza, densita', rallentatori acustici, sistemi di contenimento.
7. **Ponti e gallerie**: presenza, numero, informazioni pertinenti, rischi visivi.
8. **Incroci**: tipo, canalizzazione, qualita', volume, passaggi a livello.
9. **Manutenzione**: difetti manto, resistenza allo slittamento, condizioni banchine, condizioni segnaletica, condizioni sistemi di contenimento.
10. **Strutture per utenti vulnerabili**: passaggi pedonali/ciclabili (anche con separazione di livello), recinzioni pedoni, marciapiedi, strutture per biciclette, qualita' passaggi pedonali, strutture nelle diramazioni, percorsi alternativi.
11. **Sistemi pre/post urto e mitigazione gravita'**: centri operativi rete, meccanismi informazione utenti, AID (automatic incident detection), gestione incidenti, comunicazione servizi di soccorso.

### Step 4 - Classificazione e priorita' (art. 5, comma 5 nuovo testo)

L'organo competente, sulla base dei risultati, **classifica tutti i tratti della rete in almeno tre categorie in base al loro livello di sicurezza**. La classificazione e' funzionale a definire le priorita' delle ulteriori misure.

### Step 5 - Seguito delle procedure (art. 6-bis, inserito dall'art. 5 D.Lgs 213/2021)

Ai risultati della NSA fanno seguito:

- **Ispezioni di sicurezza stradale mirate** sui tratti prioritari (art. 6-bis, comma 1), eseguite da soggetti dell'elenco di cui all'art. 4, comma 7, tenendo conto delle componenti indicative dell'**Allegato II-bis** (inserito dall'art. 12 D.Lgs 213/2021).
- **Interventi correttivi diretti** quando necessari.
- **Piano d'azione in ordine di priorita' basato sul rischio** (art. 6-bis, comma 6), aggiornato almeno ogni cinque anni.

### Step 6 - Rendicontazione (art. 9-bis, inserito dall'art. 8 D.Lgs 213/2021)

Entro il **31 ottobre 2025** e successivamente ogni cinque anni, il Ministero delle infrastrutture e della mobilita' sostenibili trasmette alla Commissione europea una relazione sulla classificazione della sicurezza dell'intera rete valutata ai sensi dell'art. 5.

## Output

Bozza di **Documento di Valutazione della Sicurezza a Livello di Rete** strutturata in:

1. **Quadro normativo**: D.Lgs 35/2011 art. 5 nel testo introdotto dall'art. 3 D.Lgs 213/2021 e nuovo Allegato III.
2. **Identificazione dell'organo competente**.
3. **Perimetro della rete oggetto della valutazione**: elenco delle tratte con classificazione tecnica, km, eta', categoria.
4. **Metodologia di indagine visiva** (art. 5, comma 2 lett. a): tipologia di rilievo, strumentazione, copertura, soggetti coinvolti.
5. **Analisi incidentalita' tratti > 3 anni** (art. 5, comma 2 lett. b): metrica adottata, soglia di significativita', dati impiegati.
6. **Sezione 6 - Analisi per componenti dell'Allegato III**: una sotto-sezione per ogni macro-categoria (1-11).
7. **Classificazione dei tratti in almeno tre categorie** di livello di sicurezza (art. 5, comma 5).
8. **Tratti prioritari per ispezione mirata o intervento correttivo diretto** (input per art. 6-bis).
9. **Programmazione del piano d'azione quinquennale**.
10. **Indicazioni per la rendicontazione ai sensi dell'art. 9-bis** (MIMS verso Commissione UE).

## Limiti

- La NSA richiede un volume di dati di traffico, incidentalita' e caratteristiche infrastrutturali estesi all'intera rete: la skill puo' impostare la struttura del documento e la matrice di analisi per componenti, ma non sostituisce l'attivita' di rilievo e analisi dati.
- La definizione della metrica di "numero considerevole di incidenti gravi in proporzione al flusso di traffico" (art. 5, comma 2 lett. b) e' lasciata all'organo competente: la skill non fornisce soglie quantitative ufficiali.
- Per le tratte aperte al traffico da meno di tre anni, la lettera b dell'art. 5, comma 2 non si applica, ma resta l'obbligo dell'indagine visiva (lettera a).
- La NSA non sostituisce l'**ispezione di sicurezza stradale periodica** (art. 6 modificato) ne' l'**ispezione di sicurezza stradale mirata** (art. 6-bis): sono tre procedure distinte.
- L'inclusione di una specifica strada nell'elenco trasmesso alla Commissione UE (art. 1, comma 5) e' competenza del MIMS.
