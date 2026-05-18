# Task: qualifica il prodotto ai sensi del Reg. (UE) 2023/1230

## Obiettivo

Determinare se l'oggetto descritto dall'utente ricade nell'ambito di applicazione del Regolamento (UE) 2023/1230 e, in caso affermativo, classificarlo come **macchina**, **prodotto correlato**, **quasi-macchina**, oppure come oggetto **escluso**. Indicare inoltre se rilevano la qualifica di **modifica sostanziale** e se l'utente operi come **fabbricante**, **mandatario** o **altro operatore economico**. Questa qualificazione orienta tutte le sotto-attivita' successive (procedura di valutazione, contenuti del fascicolo, dichiarazione UE).

## Input richiesti

Chiedi all'utente:

- Descrizione generale dell'oggetto (uso previsto, funzione, parti mobili, sorgente di energia).
- Componenti mobili e relativa fonte di azionamento (motore elettrico, idraulico, pneumatico, termico, forza umana diretta).
- Se l'oggetto e' autonomo (esegue da solo un'applicazione specifica) oppure destinato ad essere **incorporato/assemblato** in un'altra macchina o apparecchio.
- Eventuale presenza di **componenti di sicurezza** venduti separatamente o destinati ad essere venduti separatamente.
- Eventuale presenza di **funzioni di sicurezza** affidate a **apprendimento automatico** (machine learning autoevolutivo).
- Settore d'uso: industriale, agricolo, edile, sollevamento persone/cose, lavorazione legno/metalli/plastica/gomma, alimentare, ecc.
- Stato del progetto: nuova immissione sul mercato dopo il 14/01/2027, oppure prodotto gia' immesso, oppure modifica di prodotto esistente.
- Ruolo dell'utente: fabbricante, mandatario, importatore, distributore, integratore di sistema, soggetto che esegue una modifica.

## Fonti

- `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md` sezioni 1 (ambito, definizioni), 9 (operatori).
- `references/fonti/reg-ue-2023-1230-macchine.md` art. 2 (ambito ed esclusioni), art. 3 (definizioni: macchina, prodotto correlato, componente di sicurezza, funzione di sicurezza, quasi-macchina, fabbricante, mandatario, modifica sostanziale).

## Procedura

1. **Calendario di applicazione**: verifica la data prevista di immissione sul mercato/messa in servizio.
   - Se prevista prima del 14/01/2027: la skill avvisa che si applica la direttiva 2006/42/CE (regime transitorio art. 52 del Reg. 2023/1230) e si ferma, perche' questa skill copre solo il regime del nuovo regolamento.
   - Se prevista a partire dal 14/01/2027: prosegui.
2. **Esclusioni esplicite**: confronta la descrizione contro l'elenco dell'art. 2 par. 2 lett. a-q (componenti di sicurezza ricambio identici, parchi giochi, nucleare, armi, mezzi di trasporto coperti da altri regolamenti, navi marittime, militare/ordine pubblico, ricerca temporanea in laboratorio, ascensori miniera, spostamento artisti, prodotti elettrici/elettronici coperti da 2014/35/UE o 2014/53/UE in modo esclusivo, prodotti elettrici alta tensione). Se ricade in una esclusione, segnalalo come **VERIFICA PUNTUALE** rinviando alla lettura diretta dell'art. 2 par. 2.
3. **Qualificazione di prodotto**:
   - **Macchina** (art. 3 punto 1): insieme con almeno un componente mobile, sistema di azionamento diverso dalla forza umana o animale diretta, per applicazione determinata. Le lett. a-f coprono varianti: insieme equipaggiato (a); senza elementi di collegamento al sito o alle fonti di energia (b); pronto per installazione su trasporto/edificio (c); **insieme di macchine** disposto e comandato per funzionamento solidale (d); insieme per sollevamento pesi con sola forza umana diretta (e); insieme cui manca solo il caricamento del software specifico (f).
   - **Prodotto correlato** (art. 2 par. 1): attrezzatura intercambiabile, componente di sicurezza ex art. 3 punto 3, accessorio di sollevamento, catena/fune/cinghia, dispositivo amovibile di trasmissione meccanica.
   - **Quasi-macchina** (art. 3 punto 10): insieme che non costituisce ancora una macchina perche' da solo non esegue un'applicazione specifica; destinato ad essere incorporato/assemblato in macchine o apparecchi.
   - Se l'oggetto si presenta come **componente di sicurezza** venduto separatamente che espleta una funzione di sicurezza il cui guasto puo' mettere a repentaglio la sicurezza delle persone, classificalo come **prodotto correlato (componente di sicurezza)**, art. 3 punto 3.
4. **Categoria ad alto rischio (All. I)**: indica se la descrizione e' compatibile con una delle categorie di Allegato I parte A (6 categorie) o parte B (19 categorie). Vedi estratto sez. 2.1 e 2.2. **Non concludere**: lascia la verifica di categoria al task `identifica-procedura-conformita.md`.
5. **Apprendimento automatico** per funzioni di sicurezza (componenti o sistemi integrati): segnala che, se confermato, il prodotto ricade in Allegato I parte A (categoria 5 o 6) -> procedure art. 25 par. 2.
6. **Modifica sostanziale** (art. 3 punto 16): se l'oggetto e' una modifica successiva all'immissione sul mercato di una macchina esistente, valuta se la modifica:
   - incide sulla sicurezza creando un nuovo pericolo o aumentando un rischio esistente, **E**
   - richiede aggiunta di ripari/dispositivi di protezione con modifica del sistema di controllo di sicurezza, **OPPURE** misure di protezione supplementari per stabilita'/resistenza meccanica.
   - Se entrambe le condizioni sono presenti, **la modifica e' sostanziale**: chi la esegue diventa fabbricante ai sensi dell'art. 10 (o 11 se quasi-macchina). Avviso esplicito all'utente.
7. **Operatore**: distingui fabbricante (art. 3 punto 18: progetta/fabbrica/commercializza con proprio nome o usa per uso proprio), mandatario (art. 3 punto 19: stabilito UE, mandato scritto), altri operatori (importatore, distributore, integratore). Avvisa l'utente che se immette sul mercato con proprio marchio assume gli obblighi di fabbricante.

## Output

Restituisci un report strutturato in italiano:

```
Qualificazione prodotto - Reg. (UE) 2023/1230 - <descrizione sintetica>

1. Calendario applicazione: <prima del 14/01/2027 -> NON COPERTO da questa skill / dal 14/01/2027 -> coperto>
2. Esclusioni ex art. 2 par. 2: <nessuna / segnalata: lett. <x>, verifica puntuale>
3. Qualifica:
   - Macchina (art. 3 punto 1 lett. <a/b/c/d/e/f>): <SI / NO>
   - Prodotto correlato (art. 2 par. 1): <SI - <tipo> / NO>
   - Quasi-macchina (art. 3 punto 10): <SI / NO>
   - Componente di sicurezza autonomo (art. 3 punto 3): <SI / NO>
4. Apprendimento automatico per funzioni di sicurezza: <SI - All. I parte A cat. 5 o 6 / NO>
5. Categoria All. I (preliminare, da approfondire in task "identifica-procedura-conformita.md"):
   - All. I parte A: <potenziale categoria n. <X> / nessuna>
   - All. I parte B: <potenziale categoria n. <Y> / nessuna>
   - Non in All. I: <SI / NO>
6. Modifica sostanziale ex art. 3 punto 16: <NON pertinente / pertinente: chi modifica diventa fabbricante>
7. Operatore: <fabbricante / mandatario ex art. 3 punto 19 / importatore / distributore / integratore>

Esito complessivo:
- Il prodotto RICADE / NON ricade / RICHIEDE VERIFICA PUNTUALE nel Reg. (UE) 2023/1230.
- Regime documentale applicabile:
  - se macchina/prodotto correlato -> All. IV parte A + All. V parte A + marcatura CE (art. 24);
  - se quasi-macchina -> All. IV parte B + All. V parte B + istruzioni di assemblaggio (All. XI), niente marcatura CE.

Rinvii:
- Per la verifica puntuale delle esclusioni: art. 2 par. 2 del regolamento.
- Per la procedura di valutazione della conformita': task `identifica-procedura-conformita.md`.
- La qualifica finale, la firma e la responsabilita' restano del fabbricante/professionista.
```

## Limiti

- La skill non legge il testo integrale di tutti i regolamenti settoriali richiamati dalle esclusioni (Reg. 2018/1139 aeronautica, Reg. 2018/858 veicoli a motore, Reg. 167/2013 trattori, Reg. 168/2013 due/tre ruote, dir. 2014/35/UE e 2014/53/UE per elettrici): se l'utente menziona uno di questi settori, la skill segnala l'esclusione potenziale e rinvia alla verifica puntuale.
- La distinzione macchina vs quasi-macchina puo' essere borderline (es. macchine "incomplete" vendute per integrazione finale presso il cliente): la skill propone la qualifica piu' coerente con la descrizione, ma la decisione spetta al fabbricante.
- La skill non verifica i contratti di mandato (art. 3 punto 19) ne' i contratti di subfornitura: si limita a registrare il ruolo dichiarato dall'utente.
