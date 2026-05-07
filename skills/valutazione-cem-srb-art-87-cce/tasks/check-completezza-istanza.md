# Task - Check completezza istanza/SCIA art. 87 CCE

## Obiettivo

Verificare che una pratica autorizzativa per l'installazione (o modifica delle caratteristiche di emissione) di una infrastruttura per impianto radioelettrico ai sensi dell'art. 87 D.Lgs. 259/2003 contenga tutti gli elementi richiesti dalla norma, distinguendo tra **regime ordinario (Modello A)** e **regime SCIA (Modello B)** per impianti con potenza singola antenna <= 20 W.

L'output e' una checklist commentata, non e' un parere autorizzativo (che resta in capo al SUAP/Ente locale e ad ARPA per il parere tecnico CEM).

## Input richiesti

Chiedere all'utente:

1. **Tipo di impianto**: stazione radio base nuova, modifica impianto esistente, ripetitore, ponte radio, rete a radiofrequenza punto-multipunto, altro.
2. **Tecnologia e banda**: GSM/UMTS/LTE/5G NR FR1, banda di frequenza in MHz, eventuali bande aggiuntive in caso di co-siting.
3. **Potenza in singola antenna** (W): determinante per il regime (se <= 20 W -> SCIA Modello B; altrimenti Modello A).
4. **Comune e indirizzo dell'installazione**.
5. **Operatore richiedente** e abilitazione (titolo legittimante).
6. **Documentazione gia' predisposta**: elenco breve degli allegati (modello, relazione predittiva CEM, planimetrie, schema d'antenna, ecc.).
7. **Trasmissione ad ARPA gia' avvenuta?** (data di inoltro o "non ancora").

Se uno di questi input manca, **chiedere prima di procedere**: la check di completezza dipende dal regime applicabile.

## Fonti

- `references/estratti/dlgs-259-2003-art-87.md` (art. 87 CCE, commi 1-10).
- `references/estratti/dpcm-8-7-2003-limiti-cem.md` (DPCM 8/7/2003 art. 1-7, in particolare la base per la relazione predittiva CEM).
- `references/sources.yaml` (catalogo fonti con hash e licenza).

## Procedura

### A. Determinare il regime

- **Regime SCIA - Modello B Allegato 13**: applicabile se l'impianto ha **tecnologia UMTS od altre con potenza singola antenna <= 20 W** (art. 87 c. 3 CCE, ultimo periodo). Resta fermo il rispetto dei limiti, valori di attenzione e obiettivi di qualita' del DPCM 8/7/2003.
- **Regime ordinario - Modello A Allegato 13**: tutti gli altri casi (potenza singola antenna > 20 W, oppure tipologie non riconducibili al SCIA).
- **Regime speciale GSM-R**: se l'impianto e' GSM-R ferroviario su sedime o area immediatamente limitrofa (art. 87 c. 3-bis CCE) -> fuori scope di questa skill, segnalare e fermarsi.

### B. Checklist - elementi comuni a Modello A e Modello B

Per ciascun item: stato `OK` / `MANCANTE` / `DA VERIFICARE`, riferimento normativo puntuale, azione del professionista.

1. **Modello compilato** (A o B Allegato 13 al CCE) - art. 87 c. 3 CCE. In assenza di modello predisposto dall'Ente locale, vale il modello dell'allegato 13 (art. 87 c. 3 ultimo periodo).
2. **Indicazione del soggetto abilitato** richiedente (operatore titolare di autorizzazione generale o equipollente) - art. 87 c. 2.
3. **Documentazione tecnica del sito**: ubicazione, planimetria, prospetti, schema palo/traliccio/copertura.
4. **Caratteristiche radioelettriche dell'impianto**: tecnologia, banda, frequenza, potenza in singola antenna, guadagno, tilt, azimut, schema di radiazione, altezza del centro elettrico.
5. **Valutazione predittiva CEM** redatta secondo modelli predittivi conformi alla **norma CEI 211-7** (art. 87 c. 3 CCE: "modelli predittivi conformi alle prescrizioni della CEI"; DPCM 8/7/2003 art. 6: tecniche di misurazione e rilevamento secondo CEI 211-7). Per i contenuti specifici della relazione vedi `tasks/checklist-relazione-cem.md`.
6. **Verifica del rispetto** dei limiti di esposizione (Tabella 1 Allegato B DPCM 8/7/2003), valori di attenzione (Tabella 2), obiettivi di qualita' (Tabella 3), e somma dei contributi normalizzati < 1 in caso di esposizioni multiple (art. 5 + Allegato C DPCM).
7. **Indicazione di eventuali co-siting** (impianti gia' presenti sullo stesso sito o in prossimita') con relativa stima cumulativa.
8. **Trasmissione contestuale** dell'istanza/denuncia ad **ARPA/APPA** territorialmente competente (art. 87 c. 4 CCE): l'ARPA si pronuncia entro 30 giorni dalla comunicazione.
9. **Dati amministrativi**: ufficio SUAP destinatario, indicazione del responsabile del procedimento (che l'Ente locale comunica al richiedente al momento della presentazione - art. 87 c. 2).

### C. Specifica per Modello A (regime ordinario)

10. **Pubblicizzazione dell'istanza** da parte dello sportello locale, senza diffusione dei dati caratteristici dell'impianto (art. 87 c. 4): verificare che la pratica preveda questo passaggio.
11. **Eventuale richiesta di integrazione** entro 15 giorni dalla ricezione, una sola volta (art. 87 c. 5): non e' un allegato dell'istanza, ma il professionista deve essere pronto a rispondere.

### D. Specifica per Modello B (SCIA, impianti <= 20 W per singola antenna)

12. **Asseverazione tecnica** del rispetto dei limiti CEM (resta dovuta nonostante il regime SCIA - art. 87 c. 3 CCE: "fermo restando il rispetto dei limiti, dei valori di attenzione e degli obiettivi di qualita'").
13. **Verifica modello locale**: alcune amministrazioni hanno modelli SCIA propri; in assenza, vale il Modello B Allegato 13.

### E. Verifica del testo vigente

14. **Verifica su Normattiva** del testo consolidato dell'art. 87 D.Lgs. 259/2003 alla data di deposito (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-08-01;259). Modifiche post-2014 (D.L. 76/2020 conv. L. 120/2020, D.Lgs. 8 novembre 2021 n. 207) hanno introdotto puntualizzazioni che la fonte MIMIT catalogata in `sources.yaml` non riflette. **Demanda al firmatario.**

## Output

Tabella in markdown, una riga per item:

| # | Item | Riferimento normativo | Stato | Azione del professionista |
|---|------|------------------------|-------|---------------------------|

In coda al report:
- **Regime applicabile** identificato (Modello A / Modello B / GSM-R fuori scope).
- **Riepilogo BLOCCANTI** (item MANCANTI che impediscono il deposito).
- **Disclaimer**: "Questa check e' un supporto. La completezza giuridica della pratica e' verificata dal SUAP; la conformita' tecnica CEM dal parere ARPA art. 14 L. 36/2001. Verificare il testo vigente dell'art. 87 CCE su Normattiva."

## Limiti

- Non valuta la **conformita' numerica** del calcolo predittivo CEM (richiede software CEI 211-7).
- Non sostituisce la **pronuncia di ARPA** (art. 87 c. 4 CCE).
- Non identifica **vincoli urbanistici/paesaggistici/storico-artistici** locali (regolamenti comunali, PUC, vincoli ex D.Lgs. 42/2004): rinvia al SUAP e alle valutazioni del professionista.
- Non gestisce il **dissenso qualificato** ex art. 87 c. 8 (rimessione al Consiglio dei Ministri).
