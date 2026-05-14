# Esempio - output atteso (caso problematico: rilevazione errore fluido)

## 1. Verifica ambito di applicabilita' (task `check-ambito-applicabilita.md`)

```
Verifica ambito PED - Serbatoio propano, PS 18 bar, V 5.000 L

1. Soglia PS > 0,5 bar: SI (PS dichiarata: 18 bar)
2. Tipo: recipiente
3. Esclusioni potenzialmente applicabili: nessuna apparente. Il serbatoio
   non e' apparecchio a pressione semplice (Dir. 2014/29/UE escluso per
   GPL: gli apparecchi a pressione semplici riguardano aria/azoto). Non e'
   rete di distribuzione GPL: e' un serbatoio di accumulo per stoccaggio.
4. Operatore: fabbricante (societa' italiana, pezzo unico su specifica).
5. Disposizioni transitorie: non applicabili (immissione prevista
   2026-10-15, post 19/7/2016).
6. Esito: rientra nell'ambito del D.Lgs 26/2016. Proseguire con
   `tasks/classifica-fluido.md`.

Rinvio:
- La verifica puntuale dell'art. 1 e delle esclusioni resta del fabbricante.
```

## 2. Classificazione del fluido (task `classifica-fluido.md`)

```
Classificazione fluido - Propano (C3H8)

ATTENZIONE: l'utente ha indicato gruppo 2 ma la classificazione corretta e' gruppo 1.

Stato fisico: gas (in pressione anche in fase liquida; alla TS ammissibile
              il propano e' sopra il proprio punto di ebollizione a pressione
              atmosferica)
TS dichiarata: 50 gradi C
Punto di infiammabilita': non applicabile (gas)
Classi CLP applicabili (da scheda di sicurezza): gas infiammabile categoria 1
                                                  (H220 "gas estremamente
                                                  infiammabile")

Esiti dei test:
- Test TS > punto infiammabilita': non applicabile (fluido gas)
- Match con una delle 17 classi di pericolo art. 9 c. 1 lett. a): SI
  (gas infiammabile, prima classe dell'elenco)

Gruppo assegnato: GRUPPO 1

Note:
- L'assunzione iniziale dell'utente ("propano e' gruppo 2") e' errata. Il
  propano e' espressamente fluido di gruppo 1 perche' "gas infiammabile" e'
  la prima delle classi di pericolo dell'art. 9 c. 1 lett. a (cfr. anche
  H220 "gas estremamente infiammabile" - categoria 1 della classe gas
  infiammabili Reg. CLP 1272/2008).
- Conseguenza: la classificazione di categoria va ri-eseguita usando la
  tabella 1 (recipienti gas/vapori gruppo 1), non la tabella 2.

Rinvio:
- La classificazione CLP del fluido (scheda di sicurezza) e' del produttore
  del fluido. La skill assume corretta tale classificazione e la riporta.
```

## 3. Determinazione della categoria (task `determina-categoria.md`) - RI-ESEGUITA

```
Determinazione categoria PED - Serbatoio propano cilindrico (rivista dopo
correzione del gruppo)

Input (rivisti):
- Tipo: recipiente gas/vapore (propano e' gas, contenuto in pressione)
- PS: 18 bar
- V: 5.000 litri
- Gruppo fluido: GRUPPO 1 (corretto - non gruppo 2 come inizialmente
  ipotizzato dall'utente)
- TS: 50 gradi C

Tabella applicabile: TABELLA 1 (recipienti per gas o vapori, fluidi gruppo 1)
                    [NON tabella 2]

Eccezioni testuali applicabili:
- Verifica gas instabile: il propano e' gas infiammabile ma non e'
  "instabile" nel senso del decreto (non e' un gas che decompone
  spontaneamente o polimerizza, come ad es. acetilene non stabilizzato).
  L'eccezione "gas instabili -> cat. III minima" NON si applica.
- Nessun'altra eccezione testuale applicabile (non e' estintore, non e'
  bombola apparecchi respiratori, non e' insieme acqua calda, non e' pentola
  a pressione).

Categoria proposta:
- La categoria va letta sul diagramma della tabella 1 (assi PS/V) in
  funzione di PS = 18 bar e V = 5.000 L. La skill rinvia al PDF della
  GU n.53 del 04/03/2016 (`not_in_repo/dlgs-26-2016-gu53.pdf`, pag. 23).
  La lettura puntuale del diagramma e' a carico dell'utente/professionista.
- ATTESA: con valori di PS = 18 bar e V = 5.000 L su tabella 1 (gruppo 1)
  la fascia e' significativamente piu' alta della categoria II che l'utente
  aveva ipotizzato su tabella 2.

Note:
- Differenza chiave dal caso "gruppo 2": la tabella 1 ha linee di
  demarcazione piu' restrittive (categorie piu' alte a parita' di PS/V)
  perche' il fluido e' piu' pericoloso.
- Recipiente non multi-scomparto, non gas instabile.

Rinvio:
- La lettura grafica della tabella e' a carico del fabbricante o del
  professionista firmatario.
```

**Nota di scenario**: la lettura della tabella 1 per recipienti gas/vapori
gruppo 1 con PS = 18 bar e V = 5.000 L tipicamente conduce a una categoria
**III o IV**, non II. Cio' modifica radicalmente i moduli ammissibili.

## 4. Scelta della procedura di valutazione della conformita' (task `scegli-procedura-conformita.md`)

```
Selezione procedura di valutazione della conformita' - Serbatoio propano

ATTENZIONE: l'utente aveva chiesto di valutare i moduli A2 / D1 / E1 (cat. II)
ed esclusione del modulo H. Questa richiesta era basata sulla classificazione
errata (gruppo 2 -> tabella 2). Con il gruppo corretto (1) e la tabella 1,
i moduli ammissibili cambiano: per categoria III o IV i moduli A2/D1/E1 NON
sono ammissibili.

Categoria PED (ipotesi III, da verificare sul diagramma): III

Moduli ammissibili per la categoria III (art. 10 c. 2 lett. c):
- B (tipo di progetto) + D
- B (tipo di progetto) + F
- B (tipo di produzione) + E
- B (tipo di produzione) + C2
- H (garanzia totale qualita')

Opzione categoria superiore (art. 10 c. 3): consentita verso moduli di cat. IV
(B(tipo di produzione)+D, B(tipo di produzione)+F, G, H1).

Esito sulla domanda dell'utente:
- I moduli A2 / D1 / E1 sono ammissibili solo per la categoria II. Per la
  categoria III (e a maggior ragione IV) NON sono ammissibili. La richiesta
  dell'utente di evitare il modulo H non e' un problema in se': restano gli
  altri moduli di cat. III (B+D, B+F, B(prod)+E, B(prod)+C2). Ma in tutti i
  casi e' obbligatorio il coinvolgimento di un organismo notificato.

Ruolo dell'organismo notificato:
- Cat. III: l'organismo notificato e' sempre coinvolto. Per i moduli B(progetto)
  esamina il progetto e rilascia certificato di esame UE del progetto. Per
  B(produzione) esamina un campione di produzione. Successivamente, secondo
  il modulo abbinato, fa prove sui prodotti (C2, F), o sorveglia il sistema
  qualita' (D, E).
- Per il modulo H l'organismo notificato approva e sorveglia il sistema di
  garanzia totale della qualita'.

Cadenze e visite (art. 10 c. 4): per i moduli di garanzia qualita' (D, E, H)
applicati a categoria III su recipienti di art. 3 c. 1 lett. a) punto 1) -
ipotesi applicabile ai serbatoi GPL - sono previste visite senza preavviso,
almeno due visite nel primo anno di fabbricazione, e prelievo di campione
per la valutazione finale.

Produzione in unico esemplare (art. 10 c. 5): se l'utente sceglie il modulo H
per un recipiente di categoria III prodotto in pezzo unico, l'organismo
notificato compie o fa compiere la valutazione finale ex Allegato I punto 3.2
per ciascun esemplare; il fabbricante deve comunicare il calendario di
produzione.

Documentazione tecnica:
- Conservazione 10 anni (art. 4-bis c. 3).
- Elementi minimi previsti dall'Allegato III per il modulo scelto.

Rinvio:
- La scelta del modulo e' del fabbricante. Per categoria III/IV e' obbligatorio
  l'organismo notificato (verifica nella banca dati NANDO).
- Per modulo B (tipo di progetto), il metodo di progettazione sperimentale
  (Allegato I punto 2.2.4) non puo' essere usato.
```

## 5. Checklist marcatura CE e dichiarazione UE (task `check-marcatura-ce-dichiarazione.md`)

```
Checklist marcatura CE e dichiarazione UE - Serbatoio propano

Marcatura CE (art. 15):
- [DA APPORRE] Apposta in modo visibile, leggibile, indelebile sull'attrezzatura
  o targhetta
- [DA APPORRE] Affianco al CE: NUMERO IDENTIFICATIVO ORGANISMO NOTIFICATO
  (modulo di cat. III o IV: coinvolgimento ON sempre necessario)
- [DA APPORRE] Apposta prima dell'immissione sul mercato (2026-10-15)
- [DA VERIFICARE] Conformita' art. 30 reg. CE 765/2008 (uso del logo CE)

Dichiarazione UE (art. 5, Allegato VII):
- [DA REDIGERE] Identificazione fabbricante
- [DA REDIGERE] Oggetto della dichiarazione (numero di tipo/lotto/serie)
- [DA REDIGERE] Riferimento a D.Lgs 26/2016 e Dir. 2014/68/UE
- [DA REDIGERE] Elenco norme armonizzate applicate (es. EN 13445) con
                riferimenti GUUE
- [DA REDIGERE] Modulo di valutazione applicato (es. B(progetto)+D)
- [DA REDIGERE] Organismo notificato: numero a 4 cifre + riferimento al
                certificato di esame UE del progetto (o equivalente)
- [DA REDIGERE] Firma per conto del fabbricante, luogo e data
- [SI]          Lingua italiana (mercato italiano)
- [VERIFICARE]  Dichiarazione unica per piu' direttive UE (se applicabili - es.
                direttiva ATEX se il serbatoio fa parte di un impianto in zona
                pericolosa)

Conservazione e tracciabilita':
- [10 anni] Conservazione documentazione tecnica + dichiarazione UE
- [DA APPORRE] Numero di tipo/lotto/serie sull'attrezzatura
- [DA APPORRE] Nome, marchio e indirizzo di contatto
- [DA APPORRE] Istruzioni e informazioni di sicurezza in italiano

Anomalie rilevate:
- L'utente aveva originariamente chiesto moduli di cat. II (A2/D1/E1) escludendo
  il coinvolgimento dell'organismo notificato. Questa richiesta non e'
  compatibile con la categoria corretta del serbatoio (III o IV), che richiede
  obbligatoriamente l'organismo notificato.
- Verificare l'eventuale applicabilita' della direttiva ATEX 2014/34/UE e della
  direttiva macchine 2006/42/CE se il serbatoio e' parte di un impianto piu'
  ampio. In tal caso, dichiarazione unica multi-direttiva ai sensi dell'art. 5
  c. 5.

Rinvio:
- La dichiarazione UE finale e' firmata dal fabbricante.
- La validita' del certificato di esame UE del progetto/tipo dipende
  dall'organismo notificato e dalle successive modifiche di progetto.
```

## Riepilogo - cosa la skill ha corretto rispetto alla richiesta utente

| Aspetto                | Richiesta utente (errata)   | Risposta skill (corretta)     |
|------------------------|-----------------------------|-------------------------------|
| Gruppo fluido          | gruppo 2                    | gruppo 1 (gas infiammabile)   |
| Tabella applicabile    | tabella 2                   | tabella 1                     |
| Categoria attesa       | II                          | III o IV (lettura PDF)        |
| Moduli A2 / D1 / E1    | proposti dall'utente        | non ammissibili per cat. III  |
| Organismo notificato   | si voleva evitare           | obbligatorio                  |
| Modulo H               | rifiutato a priori          | ammissibile (uno dei modi)    |
