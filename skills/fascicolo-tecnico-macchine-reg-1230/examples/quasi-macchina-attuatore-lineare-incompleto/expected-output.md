# Output atteso - Attuatore lineare AL-2000

Esempio di output in cui la skill **corregge** la convinzione errata dell'utente e indirizza correttamente verso il regime "quasi-macchina".

## 1. Qualificazione prodotto (task `qualifica-prodotto.md`)

```
Qualificazione prodotto - Reg. (UE) 2023/1230 - Attuatore lineare AL-2000

1. Calendario applicazione: immissione febbraio 2027 -> coperta dal Reg. 2023/1230.
2. Esclusioni ex art. 2 par. 2: nessuna pertinente.
3. Qualifica:
   - Macchina (art. 3 punto 1): NO. L'attuatore da solo non esegue un'applicazione determinata: e' un sottosistema destinato ad essere incorporato in una macchina del cliente.
   - Prodotto correlato (art. 2 par. 1): da verificare. NON e' un dispositivo amovibile di trasmissione meccanica, un accessorio di sollevamento, una catena/fune/cinghia. Non si configura come componente di sicurezza ex art. 3 punto 3 (non e' progettato per espletare una funzione di sicurezza il cui guasto mette a repentaglio la sicurezza delle persone).
   - Quasi-macchina (art. 3 punto 10): SI. Insieme con almeno un componente mobile (asta lineare), sistema di azionamento (motore brushless), che da solo non costituisce una macchina completa perche' non esegue un'applicazione specifica e deve essere incorporato in una macchina o quasi-macchina.
   - Componente di sicurezza autonomo: NO.
4. Apprendimento automatico per funzioni di sicurezza: NO.
5. Categoria All. I: non applicabile alle quasi-macchine (l'art. 6 e l'art. 25 riguardano macchine e prodotti correlati). La procedura di valutazione della conformita' non si applica alle quasi-macchine.
6. Modifica sostanziale: non pertinente.
7. Operatore: fabbricante (art. 3 punto 18).

Esito: l'AL-2000 RICADE nel Reg. (UE) 2023/1230 come QUASI-MACCHINA. Regime documentale: All. IV parte B + All. V parte B + istruzioni di assemblaggio (All. XI). NESSUNA marcatura CE sulla quasi-macchina.
```

## 2. Risposta alle domande dell'utente

```
DOMANDA 1: Possiamo apporre la marcatura CE sull'AL-2000 e redigere la dichiarazione UE di conformita' "standard"?

RISPOSTA: NO. Le quasi-macchine NON portano marcatura CE. La marcatura CE attesta la conformita' del prodotto a un regolamento UE che, per le quasi-macchine come prodotto autonomo, non si applica nella sua interezza (l'art. 11 obbliga il fabbricante della quasi-macchina solo ai PERTINENTI RES dell'Allegato III, non a tutti i RES applicabili a una macchina completa).
La dichiarazione corretta e' la DICHIARAZIONE DI INCORPORAZIONE UE ai sensi dell'art. 22 e dell'Allegato V parte B (9 voci), non la dichiarazione UE di conformita' dell'Allegato V parte A. Vedi task `struttura-dichiarazione-ue.md` Caso B.

DOMANDA 2: Il fornitore ci ha detto di redigere il fascicolo "normale" come per una macchina completa. E' corretto?

RISPOSTA: NO. Per la quasi-macchina si applica l'Allegato IV PARTE B (13 lettere a-m), non l'Allegato IV parte A (15 lettere a-o). Differenze chiave:
- elenca solo i RES PERTINENTI (non tutti);
- prevede istruzioni di ASSEMBLAGGIO ex All. XI, non istruzioni d'uso ex art. 10 par. 7;
- non include la lett. j (quasi-macchine incorporate) ne' la lett. k (dichiarazioni UE di altri prodotti incorporati) dell'Allegato IV parte A (le rispettive lettere parte B non esistono o hanno scope diverso).
Vedi task `struttura-fascicolo-tecnico.md` Caso B.

DOMANDA 3: Quali documenti dobbiamo consegnare al cliente integratore?

RISPOSTA: La quasi-macchina deve essere accompagnata da:
- ISTRUZIONI DI ASSEMBLAGGIO ai sensi dell'art. 11 par. 7 e dell'Allegato XI (descrizione generale, disegni, avvertenze su usi vietati, istruzioni di montaggio/installazione/collegamento, rumore/vibrazioni, RES applicabili, utensili, stabilita'/trasporto, infortunio/avaria, regolazione/manutenzione, pezzi di ricambio, versione delle istruzioni);
- DICHIARAZIONE DI INCORPORAZIONE UE ai sensi dell'art. 22 e Allegato V parte B, oppure indirizzo internet/codice ottico per accedervi.
La dichiarazione deve esplicitare che la quasi-macchina NON DEVE essere messa in servizio finche' la macchina finale (del cliente) non sara' dichiarata conforme al Regolamento (UE) 2023/1230 (punto 8 di All. V parte B).
Su richiesta motivata delle autorita' nazionali, il fabbricante della quasi-macchina si impegna a trasmettere le informazioni pertinenti (punto 7 di All. V parte B).

DOMANDA 4: Possiamo fornire solo un PDF online, senza cartaceo?

RISPOSTA: L'art. 11 par. 7 ammette il formato digitale per le istruzioni di assemblaggio, con le stesse cautele dell'art. 10 par. 7 per le macchine (accesso, scaricabilita', accessibilita' online per almeno 10 anni; su richiesta cartaceo gratuito entro un mese). Per il vostro caso (cliente integratore professionale), il formato digitale e' ammissibile. La dichiarazione di incorporazione UE puo' essere accessibile via link/codice ottico ai sensi dell'art. 11 par. 8.

Conservazione: il fabbricante della quasi-macchina conserva la documentazione tecnica e la dichiarazione di incorporazione per almeno 10 anni dall'immissione sul mercato (art. 11 par. 3).
```

## 3. Indice fascicolo tecnico (task `struttura-fascicolo-tecnico.md`)

```
Indice fascicolo tecnico - Reg. (UE) 2023/1230 - Attuatore lineare AL-2000
Allegato IV parte B (QUASI-MACCHINA)

B1. Descrizione completa della quasi-macchina e della funzione prevista ove incorporata (lett. a)
    - Tipologia "attuatore lineare elettrico", modello AL-2000, motore brushless 1,5 kW, corsa max 800 mm, forza 5 kN, velocita' max 0,5 m/s.
    - Funzioni previste ove incorporata: movimentazione lineare in linee di confezionamento, cartiere, sistemi di manipolazione.

B2. Valutazione del rischio (lett. b)
    - Elenco RES PERTINENTI (non tutti) dell'Allegato III: principalmente i RES che il fabbricante della quasi-macchina puo' soddisfare in autonomia (resistenza meccanica della struttura, sicurezza del motore e del cablaggio interno, ecc.). Esclusi i RES che dipendono dall'integrazione finale.
    - Misure di protezione + rischi residui delegati all'integratore.

B3. Disegni e schemi (lett. c).
B4. Descrizioni e spiegazioni (lett. d).
B5. Riferimenti a norme armonizzate / specifiche comuni (lett. e).
B6. Altre specifiche tecniche (lett. f).
B7. Relazioni e risultati di calcoli/prove/ispezioni/esami (lett. g).
B8. Mezzi di produzione (lett. h).
B9. Copia istruzioni di assemblaggio ex All. XI (lett. i).
B10. Misure interne per produzione in serie (lett. j).
B11. Codice sorgente / logica software sicurezza (lett. k) - su richiesta motivata.
B12. Sistema basato su sensori/remoto/autonomo (lett. l) - se applicabile.
B13. Risultati di ricerche/prove per montaggio e incorporazione in sicurezza (lett. m).

Note operative:
- NIENTE marcatura CE sulla quasi-macchina.
- Dichiarazione = DICHIARAZIONE DI INCORPORAZIONE UE (All. V parte B), non di conformita'.
- Conservazione 10 anni dalla data di immissione.
- La quasi-macchina NON puo' essere messa in servizio finche' la macchina finale non e' dichiarata conforme.
- Istruzioni di assemblaggio (All. XI) contengono o linkano la dichiarazione di incorporazione UE.

Rinvii:
- I RES PERTINENTI da elencare nella dichiarazione (B2 e All. V parte B punto 5) sono a cura del progettista, leggendo l'All. III.
- L'integratore di sistema, una volta incorporato l'AL-2000 nella macchina finale, applica autonomamente l'art. 10 e l'art. 25 per la macchina completa (e cita la dichiarazione di incorporazione dell'AL-2000 nel proprio fascicolo, All. IV parte A lett. j).
```
