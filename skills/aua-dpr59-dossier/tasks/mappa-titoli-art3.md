# Task - Mapping titoli abilitativi incorporabili nell'AUA

## Obiettivo

Dato un impianto con titoli ambientali attivi o da richiedere, individuare
quali confluiscono nell'AUA ex art. 3 co. 1 lett. a-g, g-bis, g-ter del
D.P.R. 59/2013 e quali eventualmente restano fuori dal perimetro
(autorizzazioni rifiuti ex art. 208 D.Lgs. 152/2006, AIA, atti edilizi,
ecc.).

## Input richiesti dall'utente

Chiedere all'utente, in ordine:

1. **Descrizione tecnica delle attivita'** dello stabilimento (cicli
   produttivi, sostanze utilizzate).
2. **Titoli ambientali in essere** con identificativo (numero autorizzazione,
   data di rilascio, scadenza, ente che l'ha rilasciato).
3. **Titoli da richiedere ex novo** in occasione dell'AUA.
4. **Tipo di scarichi** prodotti (acque reflue industriali, domestiche
   assimilate, meteoriche dilavanti) e recettore (corpo idrico
   superficiale, suolo, pubblica fognatura).
5. **Tipo di emissioni in atmosfera**: convogliate, diffuse, da impianto
   termico, riconducibili a tipologie dell'Allegato I del D.P.R. 59/2013
   (autorizzazione di carattere generale ex art. 272 D.Lgs. 152/2006).
6. **Attivita' di gestione rifiuti** in autosmaltimento/recupero
   (artt. 215-216 D.Lgs. 152/2006: procedure semplificate)
   o in regime ordinario (art. 208 D.Lgs. 152/2006).
7. **Utilizzo di fanghi di depurazione in agricoltura** (D.Lgs. 99/1992).
8. **Sorgenti rumorose** rilevanti: presenza di obbligo di documentazione
   acustica ex L. 447/1995 art. 8 co. 4 (nuove attivita') o co. 6
   (autorizzazioni in deroga ai valori limite).
9. **Utilizzazione agronomica di effluenti** zootecnici/agricoli
   (D.Lgs. 152/2006 art. 112).
10. **Sorgenti di radiazioni ionizzanti** ex D.Lgs. 101/2020 (artt. 24, 26).

## Fonti

- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 2 (Perimetro:
  i 9 titoli abilitativi sostituiti).
- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 6
  (Autorizzazioni di carattere generale).
- `references/fonti/dpr-59-2013-articoli-1-12.md` art. 3 e art. 7.

## Procedura

### Step 1 - Mappatura titolo per titolo

Per ciascun titolo ambientale dichiarato dall'utente, costruire una riga
della tabella di mapping con queste colonne:

| Titolo                                | Lettera art. 3 co. 1 | Incorporato in AUA |
|---------------------------------------|----------------------|--------------------|
| Autorizzazione scarichi industriali   | a                    | si                 |
| Comunicazione utiliz. agronomica      | b                    | si                 |
| Autorizz. emissioni in atmosfera      | c                    | si                 |
| Autorizz. generale art. 272           | d                    | si (o opt-out)     |
| Documentaz./nulla osta acustico       | e                    | si                 |
| Autorizz. fanghi agricoltura          | f                    | si                 |
| Comunicazione rifiuti art. 215/216    | g                    | si                 |
| Autorizz. radiazioni ionizzanti       | g-bis                | si (dal 2022)      |
| Notifica pratica radiazioni           | g-ter                | si (dal 2022)      |
| **Autorizzazione rifiuti art. 208**   | **fuori perimetro**  | **no**             |
| **AIA art. 29-ter D.Lgs. 152/2006**   | **fuori perimetro**  | **no - escluso art. 1 co. 1** |
| **Atti edilizi / urbanistici**        | **fuori perimetro**  | **no**             |
| **Autorizzazioni paesaggistiche**     | **fuori perimetro**  | **no**             |

### Step 2 - Verifica perimetro regionale ampliato (art. 3 co. 2)

Avvisare l'utente che la propria Regione/Provincia Autonoma puo' aver
**ampliato** il perimetro (es. comunicazioni rifiuti specifiche, atti
in materia di acque non centralmente disciplinati): la lista del co. 1
e' la lista statale minima. La skill non conosce le discipline regionali
specifiche; rinvio alla legge regionale e alle delibere di Giunta.

### Step 3 - Opt-out su autorizzazioni di carattere generale (art. 3 co. 3)

Se nella lista compare un'**autorizzazione di carattere generale ex
art. 272 D.Lgs. 152/2006** (Allegato I del D.P.R. 59/2013), segnalare
all'utente la possibilita' di **non avvalersi dell'AUA** per quella sola
attivita': la pratica passa comunque per il SUAP ma resta nella forma
prevista dall'autorizzazione generale (art. 7 co. 1 del regolamento).

### Step 4 - Identificazione del titolo "dominante" per i termini

Verificare se almeno uno dei titoli incorporati ha **termine procedurale
> 90 giorni** nella normativa di settore (tipicamente: scarichi
industriali, emissioni in atmosfera ex art. 269, rifiuti recupero). In
caso affermativo, il procedimento AUA seguira' il termine di 120 giorni
con conferenza di servizi (art. 4 co. 5 del regolamento, vedi
`tasks/pianifica-termini.md`).

### Step 5 - Identificazione dei titoli "esclusi"

Elenco esplicito dei titoli **non** incorporabili nell'AUA su cui
l'utente dovra' procedere con istanza separata:

- **AIA** ex art. 29-ter D.Lgs. 152/2006: se applicabile, l'impianto e'
  fuori perimetro AUA ex art. 1 co. 1 del regolamento.
- **Autorizzazione rifiuti ordinaria art. 208 D.Lgs. 152/2006**: non
  rientra nelle lett. a-g (lett. g cita solo gli artt. 215-216).
- **Concessione/derivazione idrica** (R.D. 1775/1933): non e' un titolo
  ambientale di scarico, non incorporato.
- **Autorizzazione paesaggistica** (D.Lgs. 42/2004 art. 146): titolo
  urbanistico-paesaggistico, non ambientale.
- **Permesso di costruire / SCIA edilizia**: titolo edilizio, non
  ambientale.

## Output

Un report sintetico (Markdown) con la struttura seguente:

```
# Mapping titoli AUA - [nome impianto]

## Titoli incorporati nell'AUA (art. 3 co. 1 D.P.R. 59/2013)

| Titolo | Lettera art. 3 | Stato attuale | Note |
|--------|----------------|---------------|------|
| ... | ... | ... | ... |

## Titoli soggetti a opt-out facoltativo (art. 3 co. 3)

[Eventuali autorizzazioni di carattere generale ex art. 272 D.Lgs. 152/2006
per cui valutare se restare in regime art. 7 invece di AUA.]

## Titoli fuori perimetro AUA

| Titolo | Motivo esclusione |
|--------|-------------------|
| ... | ... |

## Perimetro regionale

- Regione/PA: [...]
- Da verificare: ampliamenti perimetro AUA ex art. 3 co. 2 nella legge
  regionale o nelle delibere di Giunta.

## Titolo "dominante" per stima termini

- Almeno un titolo con termine > 90 giorni: si / no
- Termine AUA atteso (vedi `tasks/pianifica-termini.md`): 90 / 120 / 150
  giorni.

## Avvertenza
Mapping preliminare. La determinazione formale della incorporabilita' di
ciascun titolo e della disciplina di settore applicata e' del SUAP e
dell'autorita' competente. Le norme di settore di ogni titolo (Codice
Ambiente, L. 447/1995, D.Lgs. 99/1992, D.Lgs. 101/2020) si applicano nel
merito anche dopo l'incorporazione nell'AUA.
```

## Limiti del task

- Non valuta il merito tecnico dei singoli titoli (es. limiti di emissione,
  valori di scarico, classificazione CER): la skill aggrega, non calcola.
- Non interpreta le discipline regionali di ampliamento del perimetro.
- Non gestisce la situazione di un impianto che combina attivita' AUA e
  attivita' AIA in modo non separabile: in tal caso la verifica e' di
  competenza dell'autorita' AIA.
- L'Allegato I del D.P.R. 59/2013 contiene tabelle in formato grafico
  per le singole tipologie di impianto soggette ad autorizzazione di
  carattere generale: per la classificazione puntuale di una tipologia
  consultare direttamente la GU n.124 del 29-05-2013 S.O. n.42.
