# Task: struttura il fascicolo tecnico (documentazione tecnica)

## Obiettivo

Costruire l'**indice strutturato del fascicolo tecnico** (documentazione tecnica) da redigere prima dell'immissione sul mercato/messa in servizio del prodotto. Per macchine e prodotti correlati si applica **Allegato IV parte A** (lettere a-o); per quasi-macchine si applica **Allegato IV parte B** (lettere a-m). L'indice deve riportare per ogni voce: contenuto atteso, formato consigliato, riferimento normativo, e responsabile della redazione.

## Input richiesti

Prerequisito: prodotto qualificato (vedi `qualifica-prodotto.md`) e procedura di conformita' identificata (vedi `identifica-procedura-conformita.md`).

Chiedi all'utente:

- Qualificazione confermata: macchina, prodotto correlato, quasi-macchina.
- Procedura scelta (Modulo A, B+C, G, H) e organismo notificato (se previsto).
- Eventuali **quasi-macchine incorporate** nel prodotto finale (necessario per la lett. j dell'All. IV parte A).
- Eventuali altri prodotti CE incorporati (es. componenti coperti da Reg. EMC, Reg. ATEX, ecc.) - necessario per la lett. k.
- Se il prodotto e' **alimentato da sensori, azionato da remoto o autonomo** (rilevante per la lett. n dell'All. IV parte A e lett. l dell'All. IV parte B).
- Se il prodotto integra **software relativo alla sicurezza** (rilevante per la lett. m).
- Se la produzione e' in **serie** (rilevante per le lett. l e h).

## Fonti

- `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md` sezione 3 (All. IV parte A - macchine/prodotti correlati) e sezione 4 (All. IV parte B - quasi-macchine).
- `references/fonti/reg-ue-2023-1230-macchine.md` Allegato IV parte A (lett. a-o testuali) e parte B (lett. a-m testuali); art. 10 (obblighi fabbricanti macchine), art. 11 (obblighi fabbricanti quasi-macchine).

## Procedura

### Caso A - macchine e prodotti correlati (All. IV parte A)

Costruisci un indice con 15 sezioni, una per ogni lettera a-o:

- **A1. Descrizione completa del prodotto e dell'uso previsto** (lett. a). Includere: tipo, modello, varianti, destinazione d'uso prevista e prevedibilmente errata.
- **A2. Valutazione del rischio** (lett. b):
  - **A2.1 Procedura seguita** (es. UNI EN ISO 12100 - segnalata come norma armonizzata di metodo, non riprodotta).
  - **A2.2 Elenco dei RES applicabili** dall'Allegato III (matrice prodotta dal progettista).
  - **A2.3 Misure di protezione attuate per ogni RES applicabile** + indicazione dei **rischi residui** comunicati nelle istruzioni.
- **A3. Disegni e schemi** di progettazione e fabbricazione del prodotto, dei componenti, dei sottoinsiemi e dei circuiti (lett. c). Tipicamente: assieme generale, disegni di dettaglio dei componenti di sicurezza, schemi elettrici, schemi pneumatici/idraulici.
- **A4. Descrizioni e spiegazioni** per la comprensione dei disegni e del funzionamento (lett. d). Relazioni tecniche di accompagnamento.
- **A5. Riferimenti alle norme armonizzate / specifiche comuni applicate** (lett. e). Per ciascuna: numero, edizione, data di pubblicazione in GUUE. Indicare le parti se l'applicazione e' parziale.
- **A6. Altre specifiche tecniche** (lett. f). Soluzioni adottate dove norme armonizzate/specifiche comuni non sono state usate o lo sono state solo parzialmente.
- **A7. Relazioni e risultati** dei calcoli di progettazione, delle prove, ispezioni, esami (lett. g). Es. calcoli di resistenza meccanica, prove di tipo, prove di tenuta, prove EMC, ecc.
- **A8. Mezzi usati durante la produzione per assicurare la conformita'** (lett. h). Procedure di fabbricazione, controlli in linea, criteri di accettazione.
- **A9. Copia delle istruzioni per l'uso** e delle informazioni di cui all'Allegato III punto 1.7.4 (lett. i). Vedi anche art. 10 par. 7 per regole di lingua, formato cartaceo/digitale, accessibilita' decennale.
- **A10. Dichiarazione UE di incorporazione + istruzioni di assemblaggio (All. XI)** delle eventuali **quasi-macchine incorporate** (lett. j). Indicare il fabbricante della quasi-macchina e il riferimento alla dichiarazione.
- **A11. Copie delle dichiarazioni UE di conformita'** di macchine, prodotti correlati o prodotti coperti da altre normative di armonizzazione UE **incorporati** (lett. k). Es. componenti EMC, ATEX, RED, LVD.
- **A12. Misure interne in caso di produzione in serie** (lett. l). Documentazione delle modalita' di controllo che garantiscono la riproducibilita' della conformita'.
- **A13. Codice sorgente / logica di programmazione del software di sicurezza** (lett. m). Tenuto a disposizione delle autorita' nazionali su **richiesta motivata**; NON e' parte standard del fascicolo trasmesso all'ON.
- **A14. Sistema basato su sensori / remoto / autonomo** (lett. n). Solo se rilevante: descrizione delle caratteristiche generali, capacita', limitazioni del sistema, dati, sviluppo, prove, convalida dei processi.
- **A15. Risultati di ricerche e prove** su componenti/accessori/macchina per stabilire l'idoneita' al montaggio e alla messa in servizio in sicurezza (lett. o).

Segnala esplicitamente che:
- Le lett. **h)** (mezzi di produzione) ed **l)** (misure interne in serie) sono **escluse** dall'esame dell'ON nei Moduli B e H (cfr. All. VII punto 4 e All. IX punto 3.1).
- La lett. **m)** (codice sorgente) e' tenuta a disposizione solo su richiesta motivata dell'autorita'.

### Caso B - quasi-macchine (All. IV parte B)

Costruisci un indice con 13 sezioni (lett. a-m):

- **B1. Descrizione completa della quasi-macchina** e della **funzione prevista ove incorporata o assemblata** (lett. a).
- **B2. Valutazione del rischio**: elenco RES applicabili (sottoinsieme di All. III pertinenti), misure di protezione attuate, rischi residui (lett. b).
- **B3. Disegni e schemi** di progettazione e fabbricazione (lett. c).
- **B4. Descrizioni e spiegazioni** per la comprensione (lett. d).
- **B5. Riferimenti a norme armonizzate / specifiche comuni** applicate (lett. e). Indicare le parti se parziali.
- **B6. Altre specifiche tecniche** alternative (lett. f).
- **B7. Relazioni e risultati** di calcoli, prove, ispezioni, esami (lett. g).
- **B8. Mezzi usati durante la produzione** per assicurare la conformita' (lett. h).
- **B9. Copia delle istruzioni di assemblaggio** ex All. XI (lett. i). Vedi task `struttura-dichiarazione-ue.md` per i contenuti minimi.
- **B10. Misure interne** in caso di serie (lett. j).
- **B11. Codice sorgente / logica software di sicurezza** (lett. k) - su richiesta motivata dell'autorita'.
- **B12. Sistema basato su sensori / remoto / autonomo** (lett. l) - se rilevante.
- **B13. Risultati di ricerche/prove** per il montaggio e l'incorporazione in sicurezza (lett. m).

Segnala esplicitamente che:
- Per la quasi-macchina si valutano solo i **RES pertinenti** (non tutti i RES dell'All. III, ma quelli effettivamente nelle mani del fabbricante della quasi-macchina); va dichiarato esplicitamente quali sono nella dichiarazione di incorporazione (All. V parte B punto 5).
- La quasi-macchina **non porta marcatura CE** (la marcatura CE attesta conformita' a un regolamento UE che, per la quasi-macchina come prodotto autonomo, non si applica).
- La quasi-macchina **non puo' essere messa in servizio** finche' la macchina finale in cui sara' incorporata non e' dichiarata conforme al regolamento (All. V parte B punto 8).

## Output

Restituisci un indice strutturato in italiano:

```
Indice fascicolo tecnico - Reg. (UE) 2023/1230 - <prodotto>
Allegato IV parte <A / B>

<Numerazione progressiva con titolo, contenuto atteso, formato, riferimento, responsabile>

1. <Titolo voce>
   - Contenuto: <descrizione>
   - Formato consigliato: <relazione, disegni, schemi, foglio Excel, ecc.>
   - Riferimento: All. IV parte <A/B> lett. <x>; eventuali rinvii a articoli (art. 10/11, art. 20)
   - Responsabile: <progettista, ufficio qualita', produzione>

2. ...

Note operative:
- Lingua: italiana (per immissione sul mercato in Italia) + traduzione nelle lingue degli Stati membri di destinazione.
- Conservazione: almeno 10 anni dalla data di immissione sul mercato / messa in servizio (art. 10 par. 3 / art. 11 par. 3).
- Lett. m) - codice sorgente: tenuto a disposizione su richiesta motivata.
- Lett. h) ed l): non oggetto dell'esame ON nei Moduli B e H, ma parte del fascicolo per la vigilanza del mercato.

Rinvii:
- Compilazione e firma restano del fabbricante (o mandatario nei limiti del mandato).
- L'elenco dei RES applicabili (voce A2.2 o B2) richiede lettura diretta dell'Allegato III, fuori dal perimetro di questa skill.
- Per la dichiarazione UE corrispondente vedi task `struttura-dichiarazione-ue.md`.
- Per audit di completezza vedi task `check-completezza-fascicolo.md`.
```

## Limiti

- La skill non popola i contenuti delle voci: produce solo l'indice strutturato e i riferimenti normativi.
- La skill non valida la **matrice RES** ne' le scelte di misure di protezione: e' competenza del progettista.
- La skill non fornisce template editabili (Word/Excel) per ogni voce.
- La skill non controlla la coerenza temporale dei documenti (es. data della valutazione del rischio vs data dei disegni vs data delle prove): rinvio al task `check-completezza-fascicolo.md`.
