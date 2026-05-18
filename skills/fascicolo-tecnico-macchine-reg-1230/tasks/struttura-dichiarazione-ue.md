# Task: struttura la dichiarazione UE di conformita' o di incorporazione

## Obiettivo

Costruire la struttura della **dichiarazione UE di conformita'** (per macchine e prodotti correlati, Allegato V parte A) o della **dichiarazione di incorporazione UE** (per quasi-macchine, Allegato V parte B) ai sensi del Reg. (UE) 2023/1230, con tutti i contenuti minimi previsti dall'allegato e dagli articoli 21 e 22.

## Input richiesti

Prerequisito: qualifica del prodotto (vedi `qualifica-prodotto.md`) e procedura di valutazione della conformita' (vedi `identifica-procedura-conformita.md`).

Chiedi all'utente:

- Tipologia: macchina/prodotto correlato vs quasi-macchina.
- Identificazione del prodotto: nome commerciale, tipo, modello, lotto o serie, eventuale immagine.
- Anagrafica fabbricante: ragione sociale, indirizzo, sito internet/contatti digitali (unico recapito ai sensi dell'art. 10 par. 6).
- Eventuale mandatario UE (nome, indirizzo).
- Per macchine di sollevamento installate permanentemente in edifici/strutture: indirizzo del luogo di utilizzazione (richiesto al punto 3 di All. V parte A).
- Procedura applicata (Modulo A/B+C/G/H) e dati dell'organismo notificato (nome, numero ON, certificato di esame UE del tipo se Modulo B).
- Elenco delle altre normative di armonizzazione UE applicabili (es. Reg. EMC 2014/30/UE, Reg. ATEX 2014/34/UE, ecc.) - rilevante per la dichiarazione unica ex art. 21 par. 3.
- Elenco norme armonizzate / specifiche comuni applicate, con date di pubblicazione in GUUE e indicazione di applicazione parziale.
- Per quasi-macchine: elenco esplicito dei **RES pertinenti applicati e rispettati** (sottoinsieme di All. III).

## Fonti

- `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md` sezioni 5 (All. V parte A) e 6 (All. V parte B); sezione 7 per marcatura CE.
- `references/fonti/reg-ue-2023-1230-macchine.md` art. 21 (dichiarazione UE conformita'), art. 22 (dichiarazione incorporazione UE), Allegato V parte A (10 voci) e parte B (9 voci), art. 24 (marcatura CE).

## Procedura

### Caso A - macchine e prodotti correlati - dichiarazione UE di conformita' (All. V parte A)

Costruisci una struttura con le 10 voci dell'Allegato V parte A:

1. **Identificazione**: prodotto, tipo, modello, lotto o numero di serie. Se il prodotto e' una macchina/prodotto correlato che ha subito modifiche sostanziali (art. 3 punto 16): indicarlo.
2. **Fabbricante**: nome e indirizzo. **Mandatario** (se applicabile): nome e indirizzo.
3. **Macchine di sollevamento installate permanentemente in edifici/strutture e non assemblabili presso il fabbricante**: indirizzo del luogo di utilizzazione.
4. Frase di **esclusiva responsabilita'** del fabbricante: "La presente dichiarazione di conformita' e' rilasciata sotto la responsabilita' esclusiva del fabbricante".
5. **Oggetto della dichiarazione**: identificazione che ne consenta la rintracciabilita'; se necessario, immagine a colori sufficientemente chiara.
6. **L'oggetto della dichiarazione e' conforme alla seguente normativa di armonizzazione dell'Unione**: elenco con riferimento puntuale (Reg. (UE) 2023/1230; eventuali altri atti UE pertinenti).
7. **Riferimenti alle norme armonizzate / specifiche comuni applicate**, con la **data di pubblicazione del riferimento nella GUUE** (per le armonizzate) o **data di adozione** (per le specifiche comuni); in caso di applicazione parziale, indicare le parti. Riferimenti a eventuali **altre specifiche tecniche** applicate, con data.
8. Se il prodotto e' stato sottoposto a procedura con ON: **nome e numero dell'ON**, riferimento al **certificato di esame UE del tipo** (Modulo B), seguito dall'indicazione del modulo applicato (C, G, H).
9. Se applicato il **Modulo A** (controllo interno della produzione): indicarlo.
10. **Informazioni supplementari**: luogo e data del rilascio; nome, cognome, funzione, firma di chi sottoscrive a nome e per conto del fabbricante.

Note operative:

- La dichiarazione e' **continuamente aggiornata** (art. 21 par. 2) e tradotta nelle lingue dello Stato membro di immissione/messa a disposizione/messa in servizio.
- Per piu' atti UE simultanei (es. EMC + ATEX) si compila un'**unica dichiarazione** che cita tutti gli atti (art. 21 par. 3).
- Il fabbricante con la dichiarazione si assume la **responsabilita'** della conformita' (art. 21 par. 4).
- La dichiarazione **accompagna** il prodotto (in originale o tramite indirizzo internet/codice ottico, accessibile online per almeno 10 anni - art. 10 par. 8).

### Caso B - quasi-macchine - dichiarazione di incorporazione UE (All. V parte B)

Costruisci una struttura con le 9 voci:

1. **Identificazione** della quasi-macchina: numero di prodotto, di tipo, di modello, di lotto o di serie.
2. **Fabbricante**: nome e indirizzo. **Mandatario** (se applicabile): nome e indirizzo.
3. Frase di **esclusiva responsabilita'** del fabbricante.
4. **Oggetto della dichiarazione**: identificazione tracciabile (eventuale immagine).
5. **Indicazione esplicita** di quali **RES dell'Allegato III sono applicati e rispettati** e che la **documentazione tecnica e' stata compilata in conformita' dell'Allegato IV parte B**. Se del caso: conformita' ad altra normativa di armonizzazione UE pertinente.
6. **Riferimenti alle norme armonizzate / specifiche comuni applicate** (con date di pubblicazione in GUUE e indicazione di applicazione parziale); oppure altre specifiche tecniche.
7. **Impegno a trasmettere**, su richiesta motivata delle autorita' nazionali, le informazioni pertinenti sulla quasi-macchina, con indicazione delle modalita' di trasmissione, lasciando impregiudicati i diritti di proprieta' intellettuale.
8. **Dichiarazione esplicita**: la quasi-macchina **non deve essere messa in servizio** finche' la macchina finale in cui sara' incorporata non e' stata dichiarata conforme al regolamento.
9. **Informazioni supplementari**: luogo, data, nome, cognome, funzione, firma.

Note operative:

- La quasi-macchina **non porta marcatura CE**.
- La dichiarazione di incorporazione UE accompagna le **istruzioni di assemblaggio** (All. XI) o e' accessibile tramite link/codice ottico (art. 11 par. 8).
- Conservazione almeno 10 anni (art. 11 par. 3).

## Output

Restituisci la struttura compilata in italiano, con i campi noti popolati e i campi mancanti marcati come `[DA COMPILARE - <indicazione>]`:

```
DICHIARAZIONE UE DI CONFORMITA' [oppure DICHIARAZIONE DI INCORPORAZIONE UE]
n. ... (numerazione opzionale)
ai sensi del Regolamento (UE) 2023/1230 - Allegato V parte <A / B>

1. Oggetto: <prodotto / tipo / modello / lotto / numero di serie>
   <eventuale frase "Macchina che ha subito modifica sostanziale ai sensi dell'art. 3 punto 16">

2. Fabbricante: <ragione sociale, indirizzo, sito internet/contatti digitali>
   Mandatario (se applicabile): <ragione sociale, indirizzo>

3. (Solo macchine di sollevamento installate permanentemente in edifici/strutture non assemblabili presso il fabbricante)
   Indirizzo del luogo di utilizzazione: <indirizzo>

4. "La presente dichiarazione e' rilasciata sotto la responsabilita' esclusiva del fabbricante."

5. Oggetto della dichiarazione: <descrizione tracciabile, immagine a colori se necessaria>

6. (Solo All. V parte A) L'oggetto della dichiarazione e' conforme alla seguente normativa di armonizzazione dell'Unione:
   - Regolamento (UE) 2023/1230 del Parlamento europeo e del Consiglio del 14 giugno 2023
   - <eventuali altri atti UE applicabili: Reg. EMC, Reg. ATEX, Reg. RED, Reg. LVD, ecc.>

   (Solo All. V parte B) - voce 5: Sono applicati e rispettati i seguenti RES dell'Allegato III:
   - <elenco esplicito dei RES applicati: es. 1.1.1, 1.1.2, 1.2.1, ...>
   - La documentazione tecnica e' stata compilata in conformita' dell'Allegato IV parte B.

7. Riferimenti alle norme armonizzate / specifiche comuni applicate:
   - <norma 1>, edizione <YYYY>, data pubblicazione GUUE <dd/mm/yyyy>, applicazione <integrale / parziale: parti ...>
   - <norma 2>, ...

   Riferimenti ad altre specifiche tecniche applicate:
   - <riferimento>, data ...

8. (Se applicabile per All. V parte A) L'organismo notificato:
   - Nome: <nome ON>, numero: <numero ON>
   - ha effettuato l'esame UE del tipo (Modulo B) e ha emesso il certificato n. <riferimento>
   - seguito da: <Modulo C / G / H>

9. (Solo All. V parte A, se applicabile) La procedura applicata e' il controllo interno della produzione (Modulo A, Allegato VI).

   (Solo All. V parte B) Impegno: il fabbricante si impegna a trasmettere, su richiesta motivata delle autorita' nazionali competenti, le informazioni pertinenti sulla quasi-macchina. Modalita' di trasmissione: <es. via PEC, supporto digitale, ecc.>. Rimangono impregiudicati i diritti di proprieta' intellettuale.

10. (Solo All. V parte A) Informazioni supplementari.
    Firmato a nome e per conto di: <ragione sociale>
    Luogo, data: <luogo>, <data>
    Nome, cognome: <nome>
    Funzione: <funzione>
    Firma: ___________________

(Solo All. V parte B - voce 8 dichiarazione speciale)
"La quasi-macchina di cui sopra NON deve essere messa in servizio finche' la macchina finale in cui sara' incorporata non sara' stata dichiarata conforme alle disposizioni del Regolamento (UE) 2023/1230."

(Solo All. V parte B - voce 9 informazioni supplementari)
Firmato a nome e per conto di: ...
Luogo, data: ...
Nome, cognome, funzione, firma: ...
```

Rinvii:
- La dichiarazione deve essere **continuamente aggiornata** (art. 21 par. 2 / art. 22 par. 2).
- Per immissione in piu' Stati membri: tradurre nelle lingue richieste (art. 21 par. 2 / art. 22 par. 2).
- La firma e' del legale rappresentante o di delegato avente potere di firma; la skill non valida la legittimazione interna.
- Conservazione almeno 10 anni dalla data di immissione/messa in servizio (art. 10 par. 3 / art. 11 par. 3).

## Limiti

- La skill non popola la voce 5 dell'All. V parte B (elenco RES applicati e rispettati): la matrice e' a cura del progettista.
- La skill non valida la **data di pubblicazione in GUUE** delle singole norme armonizzate: e' onere del fabbricante consultare le decisioni di esecuzione della Commissione che pubblicano la lista delle armonizzate in vigore per il Reg. 2023/1230.
- La skill non verifica la **legittimazione del firmatario** (procura, poteri di firma in visura camerale): rinvio alla verifica interna.
- La skill non offre una traduzione automatica nelle altre lingue degli Stati membri.
