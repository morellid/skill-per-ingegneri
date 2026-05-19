# Task - Pianificazione dei termini procedurali AUA

## Obiettivo

Stimare i termini del procedimento AUA applicabili al caso concreto
(30 / 90 / 120 / 150 giorni), verificare se scatta l'obbligo di
conferenza di servizi e produrre un cronoprogramma di massima per il
gestore.

## Input richiesti dall'utente

Chiedere all'utente:

1. **Data prevista di presentazione dell'istanza** al SUAP.
2. **Mapping titoli incorporati** (output di `tasks/mappa-titoli-art3.md`)
   o, se non disponibile, elenco dei titoli da incorporare.
3. Per ciascun titolo, il **termine procedurale di settore** (es. art. 269
   D.Lgs. 152/2006 sulle emissioni in atmosfera prevede 120 giorni; gli
   artt. 215-216 in materia di rifiuti prevedono procedure 90 giorni;
   ecc.). Se l'utente non lo conosce, segnalarlo come "da verificare nelle
   norme di settore".
4. **Regione/Provincia Autonoma**: alcune regioni hanno fissato termini
   regionali differenti (art. 3 co. 2 e art. 4 nelle parti che rinviano
   alla legislazione regionale).
5. Eventuale presenza di **integrazioni documentali** gia' richieste o
   prevedibili.

## Fonti

- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 3 (Procedura
  per il rilascio).
- `references/fonti/dpr-59-2013-articoli-1-12.md` art. 4 (commi 1-7).

## Procedura

### Step 1 - Verifica formale (art. 4 co. 3)

Dalla data di presentazione al SUAP, l'autorita' competente (e i
soggetti coinvolti) hanno **30 giorni** per la verifica formale della
domanda. In assenza di comunicazione di irregolarita' entro 30 giorni,
l'istanza si intende correttamente presentata e il termine di rilascio
decorre.

Se viene chiesta **integrazione documentale**, il termine fissato nella
richiesta sostituisce il decorso ordinario fino al deposito delle
integrazioni; al deposito, il termine riprende a decorrere.

### Step 2 - Stima del termine di rilascio

In base ai termini procedurali di settore dei titoli incorporati:

- **90 giorni** dalla presentazione della domanda (art. 4 co. 4): se
  **tutti** i titoli incorporati hanno termine di conclusione ≤ 90
  giorni nella normativa di settore.
- **120 giorni** dal ricevimento della domanda (art. 4 co. 5): se
  **almeno uno** dei titoli incorporati ha termine > 90 giorni nella
  normativa di settore. In tal caso il SUAP, entro 30 giorni dal
  ricevimento, **indice la conferenza di servizi** ex art. 7 D.P.R.
  160/2010.
- **150 giorni** dal ricevimento della domanda (art. 4 co. 5): se in
  corso d'istruttoria viene chiesta integrazione documentale ai sensi
  dell'**art. 14-ter co. 8 della L. 241/1990**. La proroga e' applicabile
  una sola volta.

Caso particolare (art. 4 co. 7): se la domanda implica esclusivamente
l'AUA e non altri titoli SUAP, la procedura passa direttamente
all'autorita' competente; i termini sopra restano applicabili.

### Step 3 - Conferenza di servizi

La conferenza di servizi e' **obbligatoria** quando l'AUA incorpora
almeno un titolo con termine > 90 giorni (art. 4 co. 5) ed e' indetta
**dal SUAP entro 30 giorni** dal ricevimento della domanda. Si svolge
secondo le regole degli artt. 14, 14-ter, 14-quinquies della L.
241/1990 e dell'art. 7 del D.P.R. 160/2010.

Per gli altri casi (titoli tutti ≤ 90 giorni), la conferenza di servizi
**puo'** essere indetta dal SUAP nei casi previsti dalla L. 241/1990 e
dalla normativa regionale, ma non e' automatica (art. 4 co. 4).

### Step 4 - Cronoprogramma sintetico

Costruire la tabella seguente, con T0 = data presentazione domanda al
SUAP:

| Evento                                          | Riferimento          | T (giorni da T0) |
|-------------------------------------------------|----------------------|------------------|
| Verifica formale conclusa                       | art. 4 co. 3         | T0 + 30          |
| Indizione conferenza di servizi (se >90gg)      | art. 4 co. 5         | T0 + 30          |
| Riunione/i conferenza di servizi                | L. 241/1990 art. 14-ter | T0 + 30 ... T0 + 120 |
| Termine ordinario rilascio (caso 90gg)          | art. 4 co. 4         | T0 + 90          |
| Termine ordinario rilascio (caso 120gg)         | art. 4 co. 5         | T0 + 120         |
| Termine massimo con integrazione (caso 150gg)   | art. 4 co. 5         | T0 + 150         |
| Decorso inutile - silenzio                      | art. 11 co. 1 / L. 241/1990 art. 2 co. 9-bis | dopo termine |

In caso di **inerzia dell'autorita' competente** oltre il termine di
rilascio, si applica la disciplina dei **poteri sostitutivi** ex art. 2
commi 9-bis a 9-quinquies della L. 241/1990 (art. 11 co. 1 del
regolamento).

## Output

Un report sintetico (Markdown):

```
# Cronoprogramma AUA - [nome impianto]

## Dati di base
- T0 (data di presentazione al SUAP): [data]
- Titoli incorporati: [elenco]
- Almeno un titolo con termine > 90 gg: si / no
- Integrazione documentale prevista: si / no

## Termini stimati
- Verifica formale (art. 4 co. 3): entro T0 + 30 gg
- Conferenza di servizi indetta: T0 + 30 gg (se art. 4 co. 5)
- Termine atteso rilascio: T0 + [90 / 120 / 150] gg
- Norma applicata: [art. 4 co. 4 / co. 5 / co. 5 con integrazione]

## Scadenze derivate
- Data prevista verifica formale: [T0 + 30]
- Data prevista rilascio: [T0 + termine]
- Inizio decorso poteri sostitutivi (art. 11 co. 1 e L. 241/1990 art. 2
  co. 9-bis): [T0 + termine + 1]

## Avvertenza
Il cronoprogramma e' indicativo. Eventuali sospensioni del termine
(integrazioni, sospensioni in conferenza di servizi, richieste di
chiarimenti) modificano la data effettiva di rilascio. Le Regioni e
Province Autonome possono aver fissato termini regionali differenti
ex art. 3 co. 2 del D.P.R. 59/2013.
```

## Limiti del task

- Non determina i termini di settore dei singoli titoli incorporati: la
  classificazione "≤ 90 gg" vs "> 90 gg" e' assunta sulla base
  dell'input utente e/o della normativa generale di settore.
- Non considera la sospensione dei termini per ferie estive (art. 6
  L. 742/1969 sui termini processuali NON si applica al procedimento
  amministrativo).
- Non sostituisce la verifica del calendario specifico fissato in
  conferenza di servizi (orari di convocazione, deadlines interni).
- Non considera le sospensioni eventualmente disposte dall'autorita'
  competente per acquisire pareri di soggetti terzi non programmati
  nella conferenza di servizi.
