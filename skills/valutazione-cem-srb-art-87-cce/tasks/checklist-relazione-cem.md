# Task - Checklist relazione predittiva CEM

## Obiettivo

Verificare che la **relazione di valutazione predittiva CEM** allegata alla pratica art. 87 D.Lgs. 259/2003 contenga gli elementi previsti dal **DPCM 8 luglio 2003** (limiti di esposizione, valori di attenzione, obiettivi di qualita') e sia redatta con **modelli predittivi conformi alla norma CEI 211-7** richiamata dall'art. 6 del DPCM e dall'art. 87 c. 3 CCE ("modelli predittivi conformi alle prescrizioni della CEI").

L'output e' una checklist commentata. La skill **non calcola** valori numerici di campo: i valori di E (V/m), H (A/m), S (W/m^2) sono determinati dal software predittivo dell'utente sulla base dei valori delle Tabelle 1, 2, 3 dell'Allegato B del DPCM, che sono pubblicate come immagine in GU e non sono riprodotte testualmente in questa skill.

## Input richiesti

1. **Tipo impianto e tecnologia**: SRB GSM/UMTS/LTE/5G NR, ripetitore, ponte radio, ecc.
2. **Banda(e) di frequenza** (MHz) - rilevante per la riga di Tabella 1, 2, 3 Allegato B applicabile.
3. **Potenza in singola antenna** (W).
4. **Configurazione antenne**: numero, modello, guadagno (dBi), tilt elettrico/meccanico, azimut, altezza centro elettrico.
5. **Co-siting**: presenza di altri impianti sullo stesso sito o in prossimita' (per il calcolo di esposizione multipla).
6. **Contesto urbanistico**: edifici con permanenza >= 4 ore nelle vicinanze (residenze, scuole, ospedali, uffici), aree intensamente frequentate all'aperto.
7. **Software predittivo utilizzato** (con dichiarazione di conformita' alla CEI 211-7).
8. **Bozza della relazione CEM** (testo o estratto) da verificare.

## Fonti

- `references/estratti/dpcm-8-7-2003-limiti-cem.md` (DPCM 8/7/2003 art. 1-7).
- `references/estratti/dlgs-259-2003-art-87.md` (in particolare art. 87 c. 3, sull'obbligo di modelli predittivi conformi CEI).

## Procedura

Per ciascun item: stato `OK` / `MANCANTE` / `DA VERIFICARE`, riferimento puntuale, azione del professionista.

### A. Identificazione dell'impianto e del contesto

1. **Anagrafica del sito**: indirizzo, coordinate, particella catastale, foto del contesto.
2. **Caratteristiche radioelettriche** complete (banda, frequenza, potenza in singola antenna, guadagno, tilt, azimut, schema di radiazione orizzontale e verticale, altezza del centro elettrico).
3. **Inventario co-siting** con caratteristiche radioelettriche degli impianti gia' presenti.
4. **Mappatura ricettori sensibili** nel volume di rispetto: edifici con permanenza >= 4 ore (DPCM art. 3 c. 2: "edifici adibiti a permanenze non inferiori a quattro ore giornaliere, e loro pertinenze esterne, che siano fruibili come ambienti abitativi quali balconi, terrazzi e cortili esclusi i lastrici solari"); aree intensamente frequentate all'aperto (DPCM art. 4 c. 2).

### B. Modello predittivo e tecnica di calcolo

5. **Conformita' CEI 211-7**: la relazione dichiara esplicitamente l'uso di modelli predittivi conformi alla norma CEI 211-7 (e Appendici applicabili, in particolare per SRB la Guida CEI 211-7/E) - art. 87 c. 3 CCE; DPCM art. 6.
6. **Software** identificato per nome, versione, ente sviluppatore.
7. **Ipotesi di calcolo**: condizioni di emissione massima, fattore di carico (alpha 24h), ostacoli, scenari di calcolo.
8. **Volume di rispetto / sagoma di rispetto**: dichiarato e cartografato in 2D (sezioni orizzontali) e/o 3D, riferito alla soglia (limite di esposizione, valore di attenzione, obiettivo di qualita') applicabile.

### C. Mediazione spaziale e temporale

9. **Mediazione temporale**: i valori di campo sono mediati su qualsiasi intervallo di **6 minuti** (DPCM art. 3 c. 3 e art. 4 c. 1).
10. **Mediazione spaziale**: i valori sono riferiti a un'**area equivalente alla sezione verticale del corpo umano** (DPCM art. 3 c. 3 e art. 4 c. 1).

### D. Confronto con le soglie

11. **Limite di esposizione** (DPCM art. 3 c. 1, **Tabella 1 Allegato B**): rispettato ovunque al di fuori dell'antenna.
12. **Valore di attenzione** (DPCM art. 3 c. 2, **Tabella 2 Allegato B**): rispettato all'interno di edifici con permanenza >= 4 ore e loro pertinenze fruibili (balconi, terrazzi, cortili) esclusi i lastrici solari. La relazione deve identificare i ricettori applicabili e mostrare il rispetto in quei punti.
13. **Obiettivo di qualita'** (DPCM art. 4, **Tabella 3 Allegato B**): rispettato all'aperto in aree intensamente frequentate (superfici edificate o attrezzate permanentemente per bisogni sociali, sanitari, ricreativi).
14. **Esposizioni multiple** (DPCM art. 5 + Allegato C): in caso di co-siting, la **somma dei contributi normalizzati** e' < 1 nei punti di esposizione potenziale; in caso contrario la relazione descrive la procedura di **riduzione a conformita'**.

> AVVERTENZA. I valori numerici di Tabella 1, 2, 3 Allegato B sono pubblicati come **immagine** nella GU n. 199 del 28 agosto 2003 e questa skill **non li riproduce**. Il professionista verifica direttamente sulla GU (o sulla versione consolidata su Normattiva) la riga di tabella applicabile alla banda di frequenza dell'impianto. La skill segnala se nella relazione manca la citazione esplicita di Tabella 1/2/3 Allegato B con la riga della banda pertinente.

### E. Esclusioni e casi speciali

15. **Lavoratori esposti per ragioni professionali**: il DPCM 8/7/2003 NON si applica (art. 1 c. 2). Se la relazione li tratta, deve farlo separatamente con riferimento al D.Lgs. 81/2008 Titolo VIII Capo IV (fuori scope di questa skill).
16. **Esposizioni medico-diagnostiche**: il DPCM 8/7/2003 NON si applica (art. 1 c. 2).
17. **Impianti radar / esposizioni pulsate**: non rientrano in DPCM 8/7/2003 (art. 1 c. 3); sono regolati da successivo DPCM dedicato. Se l'impianto in esame e' un radar, segnalare e fermarsi.

### F. Asseverazione e firma

18. **Sottoscrizione** della relazione da tecnico abilitato/competente CEM.
19. **Asseverazione di conformita'** (esplicita) ai limiti di esposizione, valori di attenzione, obiettivi di qualita' del DPCM 8/7/2003.
20. **Coerenza con il Modello A o B Allegato 13** trasmesso al SUAP.

## Output

Tabella in markdown:

| # | Item | Riferimento | Stato | Azione |
|---|------|-------------|-------|--------|

In coda al report:
- **Sintesi BLOCCANTI** (item MANCANTI critici per l'asseverazione).
- **Sintesi DA VERIFICARE** (item che richiedono accesso ai numeri di Tabella 1/2/3 Allegato B - rinvio al firmatario).
- **Disclaimer obbligatorio**: "Questa check non riproduce i valori numerici delle Tabelle 1, 2, 3 dell'Allegato B DPCM 8/7/2003 (pubblicate come immagine in GU). La conformita' numerica e' verificata esclusivamente dal software predittivo CEI 211-7 dell'utente e asseverata dal tecnico firmatario. La relazione e' soggetta al parere ARPA art. 14 L. 36/2001 (art. 87 c. 1, c. 4 D.Lgs. 259/2003)."

## Limiti

- **Non calcola valori di campo** (V/m, A/m, W/m^2). Demanda al software CEI 211-7.
- **Non riproduce le Tabelle** dell'Allegato B (immagine in GU).
- **Non valuta** la conformita' della Guida CEI 211-7/E specifica per SRB: l'utente dichiara l'aderenza, la skill non la verifica numericamente.
- **Non gestisce** esposizioni dei lavoratori, esposizioni medicodiagnostiche, impianti radar (esposizioni pulsate).
- **Non sostituisce** il parere tecnico ARPA (vincolante ai sensi dell'art. 87 c. 1 e c. 4 CCE).
