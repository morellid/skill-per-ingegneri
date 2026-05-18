# Task: verifica completezza del fascicolo tecnico

## Obiettivo

Eseguire un **audit puntuale di completezza** del fascicolo tecnico di una macchina, prodotto correlato o quasi-macchina rispetto ai contenuti minimi dell'Allegato IV (parte A o B) del Reg. (UE) 2023/1230. Per ogni lettera dell'allegato indicare se il documento e' presente, parziale o mancante, e produrre un punch list dei gap. Includere anche i requisiti collegati (identificazione sul prodotto art. 10 par. 5-6 / art. 11 par. 5-6, istruzioni d'uso o di assemblaggio, conservazione decennale, accompagnamento della dichiarazione UE).

## Input richiesti

Prerequisito: indice del fascicolo gia' definito (vedi `struttura-fascicolo-tecnico.md`). L'utente deve avere il fascicolo gia' raccolto.

Chiedi all'utente di fornire:

- Tipologia del prodotto (macchina o prodotto correlato vs quasi-macchina).
- Procedura di valutazione della conformita' applicata (per capire quali sezioni saranno verificate anche dall'ON).
- L'elenco dei documenti presenti nel fascicolo, con descrizione sintetica e data.
- Le istruzioni per l'uso o di assemblaggio (presenza, lingua, formato cartaceo o digitale, eventuale URL/QR code).
- La dichiarazione UE di conformita' o di incorporazione (presenza, riferimenti).
- L'identificazione sul prodotto (marca/modello, anno di costruzione, lotto/serie, nome e contatti del fabbricante).
- La data di immissione sul mercato/messa in servizio prevista (per verificare il termine di conservazione decennale).

## Fonti

- `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md` sezioni 3, 4, 5, 6, 7, 8.
- `references/fonti/reg-ue-2023-1230-macchine.md` Allegato IV parte A (lett. a-o), Allegato IV parte B (lett. a-m), Allegato V parte A (10 voci), Allegato V parte B (9 voci), art. 10 par. 3 + 5-8 (macchine), art. 11 par. 3 + 5-8 (quasi-macchine), Allegato XI (istruzioni di assemblaggio).

## Procedura

### Caso A - macchine e prodotti correlati

Verifica voce per voce:

1. **All. IV parte A lett. a-o**: per ogni lettera, segna PRESENTE / PARZIALE / MANCANTE / N.A.
   - a) descrizione completa e uso previsto;
   - b) valutazione del rischio (procedura, elenco RES, misure di protezione, rischi residui);
   - c) disegni e schemi;
   - d) descrizioni/spiegazioni;
   - e) riferimenti a norme armonizzate / specifiche comuni applicate (con date di pubblicazione e indicazione di applicazione parziale);
   - f) altre specifiche tecniche;
   - g) relazioni/risultati di calcoli, prove, ispezioni, esami;
   - h) mezzi di produzione (non oggetto di esame ON, ma parte del fascicolo);
   - i) copia istruzioni per l'uso + informazioni All. III punto 1.7.4;
   - j) dichiarazione UE di incorporazione + istruzioni di assemblaggio All. XI di eventuali quasi-macchine incorporate;
   - k) copie dichiarazioni UE di conformita' di prodotti incorporati;
   - l) misure interne per produzione in serie;
   - m) codice sorgente/logica software sicurezza (tenuto a disposizione, non parte standard del fascicolo trasmesso all'ON);
   - n) sensori/remoto/autonomo: descrizione del sistema, dati, sviluppo, prove, convalida (se applicabile);
   - o) ricerche/prove per montaggio e messa in servizio in sicurezza.

2. **Dichiarazione UE di conformita' (All. V parte A)**: 10 voci. Verifica:
   - 1) identificazione del prodotto (prodotto, tipo, modello, lotto, serie), inclusa eventuale dichiarazione di modifica sostanziale;
   - 2) nome e indirizzo del fabbricante + mandatario;
   - 3) per macchine di sollevamento installate permanentemente in edifici/strutture non assemblabili presso il fabbricante: indirizzo del luogo di utilizzazione;
   - 4) dichiarazione di esclusiva responsabilita' del fabbricante;
   - 5) oggetto della dichiarazione (identificazione tracciabile);
   - 6) elenco della normativa di armonizzazione UE applicata;
   - 7) riferimenti a norme armonizzate/specifiche comuni applicate, con date di pubblicazione in GUUE; parti se parziale;
   - 8) se applicabile, dettagli dell'ON e numero del certificato di esame UE del tipo, modulo (C, G, H);
   - 9) se applicabile (Modulo A), dicitura "controllo interno della produzione";
   - 10) luogo, data, nome/funzione/firma.

3. **Marcatura CE (art. 24)**:
   - Apposta in modo visibile, leggibile, indelebile (par. 1).
   - Apposta **prima** dell'immissione sul mercato/messa in servizio (par. 2).
   - Se procedura con ON -> seguita dal numero di identificazione dell'ON (par. 3).

4. **Identificazione sul prodotto (art. 10 par. 5-6)**:
   - Designazione modello/serie/tipo;
   - Anno di costruzione;
   - Eventuale numero di lotto/serie;
   - Nome del fabbricante, denominazione/marchio, indirizzo postale, sito internet/contatti digitali (unico recapito).

5. **Istruzioni per l'uso (art. 10 par. 7)**:
   - Lingua dello Stato membro di immissione/messa in servizio;
   - Formato cartaceo o digitale (con accessibilita' online almeno 10 anni e disponibilita' cartacea gratis su richiesta entro un mese);
   - Per utilizzatori non professionali: informazioni di sicurezza essenziali in cartaceo;
   - Conformi alle informazioni di All. III punto 1.7.4.

6. **Conservazione (art. 10 par. 3)**:
   - Documentazione tecnica + dichiarazione UE a disposizione delle autorita' per almeno 10 anni;
   - Codice sorgente / logica programmazione disponibile su richiesta motivata.

### Caso B - quasi-macchine

Verifica voce per voce:

1. **All. IV parte B lett. a-m**: PRESENTE / PARZIALE / MANCANTE / N.A. per ciascuna delle 13 lettere.

2. **Dichiarazione di incorporazione UE (All. V parte B)**: 9 voci. Verifica in particolare:
   - 5) elenco esplicito dei **RES applicati e rispettati** e attestazione che la documentazione tecnica e' stata compilata in conformita' all'All. IV parte B;
   - 7) **impegno** del fabbricante a trasmettere informazioni pertinenti sulle quasi-macchine alle autorita' nazionali su richiesta motivata;
   - 8) dichiarazione che la **quasi-macchina non deve essere messa in servizio** finche' la macchina finale non e' dichiarata conforme.

3. **Marcatura CE**: **assente** sulla quasi-macchina (segnala se erroneamente apposta).

4. **Identificazione sulla quasi-macchina (art. 11 par. 5-6)**: designazione, anno di costruzione, modello/tipo, lotto/serie eventuale, nome e contatti fabbricante.

5. **Istruzioni di assemblaggio (art. 11 par. 7 e All. XI)**: verifica le voci a-n dell'All. XI (descrizione generale, disegni, avvertenze su usi vietati, istruzioni di montaggio/installazione/collegamento, rumore/vibrazioni, RES applicabili, utensili, stabilita'/trasporto, infortunio/avaria, regolazione/manutenzione, pezzi di ricambio, versione delle istruzioni). Verifica anche che le istruzioni di assemblaggio includano o linkino la dichiarazione di incorporazione UE.

6. **Conservazione (art. 11 par. 3)**: documentazione tecnica + dichiarazione di incorporazione UE per almeno 10 anni.

## Output

Restituisci un report strutturato in italiano:

```
Audit completezza fascicolo tecnico - Reg. (UE) 2023/1230 - <prodotto>
Tipologia: <macchina/prodotto correlato/quasi-macchina>
Procedura applicata: <Modulo A/B+C/G/H>
Data immissione prevista: <data>

A. Documentazione tecnica (All. IV parte <A/B>)
   - lett. a: <PRESENTE/PARZIALE/MANCANTE/N.A.> - nota: <descrizione>
   - lett. b: ...
   - ...
   - lett. <o oppure m>: ...

B. Dichiarazione UE (All. V parte <A/B>)
   - voce 1: <stato>
   - voce 2: <stato>
   - ...
   - voce 9 o 10: <stato>

C. Marcatura CE / numero ON (solo macchine/prodotti correlati)
   - apposta: <SI/NO/N.A.>
   - prima dell'immissione: <SI/NO>
   - numero ON corretto: <SI/NO/N.A.>

D. Identificazione sul prodotto
   - designazione modello/serie/tipo: <stato>
   - anno di costruzione: <stato>
   - lotto/serie: <stato>
   - nome/contatti fabbricante: <stato>

E. Istruzioni per l'uso (macchine) o di assemblaggio (quasi-macchine)
   - presenza: <SI/NO>
   - lingua: <stato>
   - formato: <cartaceo/digitale/entrambi>
   - conformita' al contenuto: <stato>
   - per quasi-macchine: dichiarazione di incorporazione UE inclusa o linkata: <SI/NO>

F. Conservazione
   - durata pianificata: <anni> (min 10)
   - codice sorgente disponibile su richiesta motivata: <SI/NO/N.A.>

PUNCH LIST GAP:
- BLOCKER (impediscono l'immissione sul mercato): <elenco>
- MAJOR (devono essere chiusi prima della dichiarazione UE): <elenco>
- MINOR (consigliato risolvere ma non bloccante): <elenco>

Rinvii:
- La firma della dichiarazione UE e la responsabilita' della conformita' restano del fabbricante.
- Per gap su valutazione del rischio o matrice RES, intervento del progettista.
```

## Limiti

- La skill non legge i contenuti dei documenti per validarne la qualita' tecnica: si limita a verificare la presenza e la struttura (es. che esista un documento "valutazione del rischio", non che la valutazione sia corretta).
- La skill non verifica la **qualifica dell'organismo notificato** ne' la **validita' del certificato di esame UE del tipo**: rinvia alla consultazione del database NANDO della Commissione e al certificato originale (validita' max 5 anni).
- La skill non controlla la coerenza dei dati anagrafici (es. ragione sociale identica su dichiarazione UE e marca/etichetta).
- La skill non sostituisce la verifica formale del professionista firmatario o dell'auditor interno qualita'.
