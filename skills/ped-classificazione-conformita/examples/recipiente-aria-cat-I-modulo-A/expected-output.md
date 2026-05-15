# Esempio - output atteso (caso conforme)

## 1. Verifica ambito di applicabilita' (task `check-ambito-applicabilita.md`)

```
Verifica ambito PED - Serbatoio aria compressa, PS 11 bar, V 100 L

1. Soglia PS > 0,5 bar: SI (PS dichiarata: 11 bar)
2. Tipo: recipiente
3. Esclusioni potenzialmente applicabili: verificare apparecchi a pressione semplici
   (Dir. 2014/29/UE) - per serbatoi aria compressa di acciaio saldato in serie con
   parametri tipici, la verifica e' che ricadano nella Dir. 2014/29/UE (apparecchi
   a pressione semplici) o nel D.Lgs 26/2016 (PED). La distinzione e' fatta sulla
   base del prodotto PS x V e di altri criteri specifici della Dir. 2014/29/UE.
   Questa verifica e' a carico del fabbricante e non e' nello scope di questo task.
4. Operatore: fabbricante (societa' italiana, marchio proprio)
5. Disposizioni transitorie: non applicabili (immissione prevista 2026-09-01, post 19/7/2016)
6. Esito: VERIFICA PUNTUALE su esclusione apparecchi a pressione semplici, prima di
   procedere alla classificazione PED. Se conferma applicabilita' PED, proseguire con
   `tasks/classifica-fluido.md`.

Rinvio:
- Per la verifica puntuale dell'art. 1 e delle esclusioni si rimanda alla lettura del
  D.Lgs 93/2000 come modificato dal D.Lgs 26/2016 e alla Dir. 2014/29/UE per i serbatoi
  aria compressa di acciaio saldato.
- La classificazione finale e la responsabilita' procedurale restano del fabbricante
  (o del professionista firmatario).
```

**Nota di scenario**: per i fini di questo esempio si assume che il fabbricante abbia
verificato e concluso che il serbatoio ricade nel D.Lgs 26/2016 (PED) e non nella
Dir. 2014/29/UE.

## 2. Classificazione del fluido (task `classifica-fluido.md`)

```
Classificazione fluido - Aria atmosferica compressa

Stato fisico: gas/vapore
TS dichiarata: 60 gradi C
Punto di infiammabilita': non applicabile (gas non infiammabile)
Classi CLP applicabili: nessuna delle classi dell'art. 9 c. 1 lett. a)

Esiti dei test:
- Test TS > punto infiammabilita': non applicabile (fluido gas)
- Match con una delle 17 classi di pericolo art. 9 c. 1 lett. a): NO

Gruppo assegnato: gruppo 2

Note:
- L'aria atmosferica e' fluido di gruppo 2 (residuo, art. 9 c. 1 lett. b).

Rinvio:
- La classificazione CLP del fluido (categorie, classi di pericolo) e' di responsabilita'
  del produttore del fluido (scheda di sicurezza). La skill assume corretta tale
  classificazione e la riporta.
- Il fabbricante dell'attrezzatura resta responsabile della verifica finale.
```

## 3. Determinazione della categoria (task `determina-categoria.md`)

```
Determinazione categoria PED - Serbatoio aria compressa cilindrico

Input:
- Tipo: recipiente gas/vapore
- PS: 11 bar
- V: 100 litri
- Gruppo fluido: gruppo 2
- TS: 60 gradi C

Tabella applicabile: tabella 2 (recipienti per gas o vapori, fluidi gruppo 2)

Eccezioni testuali applicabili:
- nessuna

Categoria proposta:
- Nessuna eccezione si applica. La categoria va letta sul diagramma della tabella 2
  (assi PS/V) in funzione di PS = 11 bar e V = 100 L. La skill rinvia al PDF della
  GU n.53 del 04/03/2016 (`not_in_repo/dlgs-26-2016-gu53.pdf`, pagg. 23-26). La lettura
  puntuale del diagramma e' a carico dell'utente/professionista.

Note:
- Recipiente non multi-scomparto, non gas instabile, non estintore portatile, non bombola
  per apparecchi respiratori, non insieme acqua calda, non pentola a pressione: nessuna
  delle eccezioni testuali dell'Allegato II e' applicabile.

Rinvio:
- La lettura grafica della tabella e' a carico del fabbricante o del professionista firmatario.
```

**Nota di scenario**: per i fini di questo esempio si assume che la lettura del
diagramma della tabella 2 conduca alla **categoria I**. (Il valore puntuale dipende
dalla linea di demarcazione mostrata nel PDF.)

## 4. Scelta della procedura di valutazione della conformita' (task `scegli-procedura-conformita.md`)

```
Selezione procedura di valutazione della conformita' - Serbatoio aria compressa

Categoria PED: I
Eventuale eccezione applicata: nessuna

Moduli ammissibili per la categoria I (art. 10 c. 2 lett. a):
- modulo A (controllo interno della produzione)

Opzione categoria superiore (art. 10 c. 3): consentita, il fabbricante puo' optare per
moduli di categoria II (A2, D1, E1) o superiore, se ha interesse a coinvolgere un
organismo notificato.

Ruolo dell'organismo notificato per modulo:
- Modulo A: nessun organismo notificato. Il fabbricante esegue tutto in regime di
  controllo interno della produzione. Risposta diretta alla domanda dell'utente.

Cadenze e visite (art. 10 c. 4 e c. 5): non applicabili (categoria I).

Documentazione tecnica:
- Conservazione 10 anni (art. 4-bis c. 3).
- Elementi minimi previsti dall'Allegato III per il modulo A: descrizione generale
  dell'attrezzatura, disegni di progettazione e fabbricazione, descrizioni e spiegazioni,
  norme armonizzate applicate o, in mancanza, descrizione delle soluzioni adottate per
  i RES dell'Allegato I, risultati dei calcoli di progettazione, relazioni sulle prove
  effettuate. Conservazione per dieci anni dall'immissione sul mercato.

Insiemi: non applicabile (singolo recipiente).

Rinvio:
- La scelta del modulo e' del fabbricante. Per il modulo A non e' richiesto organismo
  notificato.
```

## 5. Checklist marcatura CE e dichiarazione UE (task `check-marcatura-ce-dichiarazione.md`)

```
Checklist marcatura CE e dichiarazione UE - Serbatoio aria compressa

Marcatura CE (art. 15):
- [DA APPORRE] Apposta in modo visibile, leggibile, indelebile sull'attrezzatura o targhetta
- [N.A.]       Affianco al CE: numero identificativo organismo notificato (modulo A: nessun ON)
- [DA APPORRE] Apposta prima dell'immissione sul mercato (2026-09-01)
- [DA VERIFICARE] Conformita' art. 30 reg. CE 765/2008 (uso del logo CE)

Dichiarazione UE (art. 5, Allegato VII):
- [DA REDIGERE] Identificazione fabbricante
- [DA REDIGERE] Oggetto della dichiarazione (numero tipo/lotto/serie del serbatoio)
- [DA REDIGERE] Riferimento a D.Lgs 26/2016 e Dir. 2014/68/UE
- [DA REDIGERE] Elenco norme armonizzate applicate (es. EN 13445 per recipienti a pressione
                non sottoposti a fiamma, se applicata) con riferimenti GUUE
- [DA REDIGERE] Modulo di valutazione applicato: A
- [N.A.]        Organismo notificato (modulo A)
- [DA REDIGERE] Firma per conto del fabbricante, luogo e data
- [SI]          Lingua italiana (mercato italiano)
- [VERIFICARE]  Dichiarazione unica per piu' direttive UE (se applicabili - es. macchine se
                il serbatoio fa parte di un quadro pneumatico in macchina)

Conservazione e tracciabilita':
- [10 anni] Conservazione documentazione tecnica + dichiarazione UE dalla data di immissione
- [DA APPORRE] Numero di tipo/lotto/serie sull'attrezzatura
- [DA APPORRE] Nome, marchio e indirizzo di contatto sull'attrezzatura o sull'imballaggio
- [DA APPORRE] Istruzioni e informazioni di sicurezza in italiano (art. 4-bis c. 7)

Anomalie rilevate:
- Nessuna anomalia: in modulo A il fabbricante svolge tutta la procedura in autonomia.
  Verificare in particolare che la documentazione tecnica sia completa e che le norme
  armonizzate eventualmente applicate coprano i RES applicabili.

Rinvio:
- La dichiarazione UE finale e' firmata dal fabbricante.
- Se il serbatoio viene incorporato in una macchina, valutare la dichiarazione unica
  ai sensi dell'art. 5 c. 5.
```
