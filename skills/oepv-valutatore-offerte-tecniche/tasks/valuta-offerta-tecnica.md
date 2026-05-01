# Task: Valutazione offerte tecniche con metodo aggregativo-compensatore

Applica il metodo aggregativo-compensatore alle offerte tecniche ed economiche dei concorrenti, producendo il prospetto punteggi e la classifica finale.

## Obiettivo

Produrre:
- Tabella punteggi per criterio/sottocriterio per ciascun offerente
- Calcolo del punteggio complessivo Pi = Sigma(Wj x V(aij))
- Classifica finale con punteggio tecnico, punteggio economico e punteggio totale
- Note su eventuali anomalie di punteggio o situazioni da segnalare alla commissione

## Input richiesti

1. **Matrice criteri/sottocriteri** completa (criteri, pesi, metodo di valutazione per ognuno)
2. **Elenco offerenti** con, per ciascuno:
   - Per criteri **tabellari**: il valore dichiarato (es. anni esperienza, certificazioni possedute si/no)
   - Per criteri **discrezionali**: i coefficienti gia' attribuiti da ciascun commissario (o i punteggi medi se gia' elaborati dalla commissione)
   - Per criteri a **formula quantitativa**: il valore numerico offerto (es. giorni di consegna, percentuale di riduzione)
   - Per il **prezzo**: l'importo offerto in EUR

Se i coefficienti discrezionali non sono ancora stati attribuiti, la skill spiega la procedura che la commissione deve seguire (Passo 2 sotto) prima di procedere al calcolo.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art107-108.md`
- `references/estratti/dlgs-36-art93.md`
- `references/estratti/anac-lg-n2-metodologia-oepv.md`

## Procedura

### Passo 1 - Verifica completezza input

Verificare che siano disponibili per ogni offerente tutti i dati necessari per ogni criterio. Segnalare le lacune prima di procedere. Se mancano dati per criteri discrezionali, passare al Passo 2.

### Passo 2 - Procedura di attribuzione coefficienti discrezionali (da seguire PRIMA del calcolo)

Per i criteri con metodo discrezionale, la commissione deve seguire questa procedura (art. 93 D.Lgs. 36/2023 + ANAC LG n.2):

1. **Seduta collegiale riservata**: i commissari esaminano singolarmente ogni offerta tecnica
2. **Attribuzione individuale e simultanea**: ciascun commissario assegna un coefficiente da 0 a 1 per ciascun criterio discrezionale, **senza consultarsi con gli altri commissari** prima dell'attribuzione
3. **Rivelazione simultanea**: i coefficienti individuali vengono comunicati e verbalizzati tutti contemporaneamente
4. **Calcolo media**: per ogni criterio e ogni offerente, la media aritmetica dei coefficienti individuali diventa il coefficiente provvisorio
5. **Riproporzionamento** (Passo 3): il coefficiente finale e' ri-proporzionato rispetto al miglior offerente

Segnalare alla commissione che l'attribuzione individuale silenziosa e la rivelazione simultanea sono essenziali per evitare influenze reciproche tra commissari (rischio di annullamento TAR per "condizionamento della valutazione").

### Passo 3 - Calcolo coefficienti per criterio

Per ogni criterio applicare il metodo specificato nella matrice:

**Tabellare on/off**:
- Requisito soddisfatto: V = 1 (coefficiente pieno)
- Requisito non soddisfatto: V = 0
- Es. certificazione parita' genere: si -> V=1; no -> V=0

**Tabellare a scala discreta** (es. anni esperienza con soglie):
- Mappare il valore dichiarato sulla scala prevista nel disciplinare
- Es. < 5 anni: 0; 5-10 anni: 0.5; > 10 anni: 1

**Discrezionale** (con riproporzionamento):
- Calcolare media_i = media coefficienti commissari per offerente i
- V(ai) = media_i / max(media_k per tutti k)
- Il miglior offerente per quel criterio ottiene sempre V=1

**Formula quantitativa (parametro crescente, migliore = maggiore)**:
- V(ai) = Ra_i / Ra_max
- Dove Ra_max = valore massimo tra tutte le offerte

**Formula quantitativa (parametro decrescente, migliore = minore, es. giorni)**:
- V(ai) = Ra_min / Ra_i
- Dove Ra_min = valore minimo tra tutte le offerte

**Offerta economica (formula lineare)**:
- Pe_i = Vmax_economica × (Prezzo_min / Prezzo_i)
- Dove Prezzo_min = offerta economica piu' bassa tra gli ammessi

### Passo 4 - Calcolo punteggi per criterio

Per ogni criterio j e ogni offerente i:
- Punteggio_ij = Peso_j × V(aij)

### Passo 5 - Calcolo punteggio totale

Per ogni offerente i:
- Punteggio_totale_i = Sigma(Punteggio_ij per tutti i criteri j)
- = P_tecnico_i + Pe_i

### Passo 6 - Output

```markdown
# Prospetto valutazione OEPV
**Gara**: [oggetto]
**Data valutazione**: [data]
**Commissione**: [presidente + [n] commissari]

---

## Punteggi per criterio

| Criterio | Peso | Offerente A | Offerente B | Offerente C | ... |
|----------|------|-------------|-------------|-------------|-----|
| A1 - [nome] | XX | V=x.xx -> Px=XX | ... | ... | |
| A2 - [nome] | XX | ... | | | |
| ... | | | | | |
| **Subtotale tecnico** | **XX** | **XX.X** | **XX.X** | **XX.X** | |
| **Offerta economica** | **XX** | **XX.X** | **XX.X** | **XX.X** | |
| **TOTALE** | **100** | **XX.X** | **XX.X** | **XX.X** | |

---

## Dettaglio calcoli per criterio discrezionale

### Criterio A1 - [nome] (peso XX, metodo discrezionale)

| Offerente | Comm.1 | Comm.2 | Comm.3 | Media | V(a) | Punteggio |
|-----------|--------|--------|--------|-------|------|-----------|
| A | x.x | x.x | x.x | x.xx | 1.000 | XX.X |
| B | x.x | x.x | x.x | x.xx | 0.xxx | XX.X |
| C | x.x | x.x | x.x | x.xx | 0.xxx | XX.X |

Riproporzionamento: miglior media = [x.xx] (Offerente [X]) -> V(best) = 1.000

---

## Calcolo offerta economica

| Offerente | Prezzo offerto (EUR) | V(a) = Prezzomin/Prezzoofferto | Punteggio (x/XX) |
|-----------|----------------------|-------------------------------|------------------|
| A | [prezzo] | [ratio] | [punti] |
| B | [prezzo] | [ratio] | [punti] |
| C | [prezzo] | [ratio] | [punti] |

Prezzo minimo ammesso: EUR [Prezzomin] (Offerente [X])
Formula applicata: Pe_i = [Vmax] × (Prezzomin / Prezzo_i)

---

## Classifica finale

| Posizione | Offerente | P. Tecnico | P. Economico | P. Totale |
|-----------|-----------|------------|--------------|-----------|
| 1 | [nome] | XX.X | XX.X | **XX.X** |
| 2 | [nome] | XX.X | XX.X | **XX.X** |
| 3 | [nome] | XX.X | XX.X | **XX.X** |

---

## Note e segnalazioni

[Eventuali anomalie, offerte con punteggio molto basso su un singolo criterio, parità da risolvere, ecc.]

---

## Rinvio alla commissione

Questo prospetto e' prodotto come supporto al calcolo. La commissione deve:
1. Verificare la correttezza dei dati di input utilizzati
2. Approvare collegialmente i risultati e verbalizzarli
3. Procedere alle eventuali verifiche di anomalia (offerte con punteggio totale >= [soglia Allegato II.2])
4. Comunicare la proposta di aggiudicazione al RUP
```

## Casi limite da gestire

### Parita' di punteggio
Se due offerenti hanno lo stesso punteggio totale, indicarlo nel report e rinviare alla commissione per la procedura di spareggio prevista nel disciplinare (di solito sorteggio o preferenza per il punteggio tecnico piu' alto).

### Coefficiente discrezionale zero per tutti i commissari
Se tutti i commissari assegnano 0 a un offerente per un criterio discrezionale: il coefficiente e' 0. Il riproporzionamento si applica sul miglior offerente che ha almeno uno score > 0.

### Offerta economica nulla o anomala
Non calcolare il punteggio economico per offerte con prezzo zero (offerte anomale evidenti). Segnalare alla commissione per il sub-procedimento di anomalia.

### Criterio con solo un offerente valutabile
Se per un criterio tabellare solo un offerente soddisfa il requisito, V=1 per quell'offerente e V=0 per gli altri. Non e' un errore, ma segnalarlo alla commissione come possibile punto di contestazione.

### Dati discrezionali non ancora disponibili
Se i coefficienti discrezionali non sono stati ancora attribuiti, fornire il template della Passo 2 e indicare che il calcolo non puo' essere completato prima che la commissione abbia svolto le valutazioni individuali.

## Limiti di questo task

- Il calcolo e' corretto solo se i dati di input (coefficienti discrezionali, valori tabellari, prezzi) sono corretti
- Non si valuta se le offerte tecniche sono conformi ai requisiti minimi del capitolato (la commissione lo verifica separatamente)
- Non si gestisce l'esclusione per offerte irregolari o inammissibili: si assume che tutte le offerte fornite siano gia' state ammesse
- Non si calcola la soglia di anomalia (Allegato II.2 D.Lgs. 36/2023): quella e' una procedura separata
- Il report non e' un verbale di gara ufficiale: la commissione deve verbalizzare autonomamente

## Esempi

Vedi `examples/`:
- `conforme-servizi-architettura/` - calcolo OEPV per servizi di progettazione con 3 offerenti
