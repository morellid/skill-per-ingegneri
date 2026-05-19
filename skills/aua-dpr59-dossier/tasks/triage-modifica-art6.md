# Task - Triage modifica sostanziale / non sostanziale (art. 6)

## Obiettivo

Classificare una modifica proposta dal gestore (di attivita' o di
impianto) rispetto all'art. 6 del D.P.R. 59/2013 e determinare il
flusso procedurale corretto:

- modifica **non sostanziale** -> comunicazione all'autorita' competente
  (art. 6 co. 1);
- modifica **sostanziale** -> nuova domanda di AUA ex art. 4 (art. 6
  co. 2 se ex ante; art. 6 co. 3 se l'autorita' lo ordina entro 30 gg
  dalla comunicazione del gestore).

## Input richiesti dall'utente

Chiedere all'utente:

1. **Descrizione tecnica della modifica** (cosa cambia rispetto allo
   stato autorizzato: layout, cicli, sostanze, capacita', sorgenti
   emissive, scarichi, ecc.).
2. **Quale titolo incorporato nell'AUA e' interessato** dalla modifica
   (scarichi, emissioni, rifiuti, acustica, fanghi, radiazioni, ecc.).
3. **Quantificazione** delle variazioni: portate, potenze, capacita',
   numero sorgenti, soglie.
4. **Documentazione tecnica** prodotta per la modifica (relazione
   tecnica, valutazione di impatto delle modifiche, planimetrie).
5. **Posizione del professionista firmatario** sulla classificazione
   (gia' istruita o no).
6. **Regione/Provincia Autonoma**: alcune Regioni hanno definito ulteriori
   criteri di classificazione (art. 6 co. 4).

## Fonti

- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 5 (Modifiche).
- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 10 (Glossario:
  modifica sostanziale).
- `references/fonti/dpr-59-2013-articoli-1-12.md` art. 6 e art. 2 co. 1
  lett. g (definizione modifica sostanziale).

## Procedura

### Step 1 - Rinvio alle normative di settore

La definizione di "modifica sostanziale" nell'AUA (art. 2 co. 1 lett. g)
rinvia espressamente alle **normative di settore** dei singoli titoli
incorporati: "ogni modifica considerata sostanziale ai sensi delle
normative di settore [...] in quanto possa produrre effetti negativi
e significativi sull'ambiente".

Quindi per la classificazione preliminare, **non** esiste un criterio
unico AUA: bisogna chiedersi, per ciascun titolo coinvolto:

- **Scarichi** (art. 124 D.Lgs. 152/2006 e regolamenti regionali): cambio
  di recettore? aumento significativo della portata? introduzione di
  nuovi inquinanti?
- **Emissioni in atmosfera** (art. 269 co. 8 D.Lgs. 152/2006): variazione
  delle emissioni che comporta un aumento o variazione qualitativa che
  pregiudica gli obiettivi di qualita'?
- **Rifiuti** (artt. 215, 216 e disciplina settoriale): variazione tipologie
  CER trattate, variazione delle operazioni R/D, superamento delle
  soglie previste per il regime semplificato?
- **Acustica** (L. 447/1995): superamento dei valori limite di immissione
  o di emissione precedentemente rispettati?
- **Fanghi** (D.Lgs. 99/1992): cambio del piano di utilizzo, dei
  terreni destinatari, delle caratteristiche del fango?
- **Radiazioni ionizzanti** (D.Lgs. 101/2020): variazione di pratica
  ex art. 26 (autorizzazione) o ex art. 24 (notifica)?

La skill non determina autonomamente la qualifica: indica i criteri,
rinvia al professionista per la verifica nel testo di settore.

### Step 2 - Decisione del gestore prima della comunicazione

Il gestore puo' seguire due strade:

**Strada A** - intende la modifica come **non sostanziale**: applica
l'art. 6 co. 1. Comunica la modifica all'autorita' competente e:

- attende **30 giorni** entro i quali l'autorita' competente puo'
  riqualificare la modifica come sostanziale e ordinare nuova domanda
  ex art. 4 (art. 6 co. 3);
- in assenza di riqualificazione entro 30 giorni, decorrono ulteriori
  30 giorni (totale 60 giorni dalla comunicazione) entro cui l'autorita'
  competente puo' comunque pronunciarsi sulla modifica;
- decorsi **60 giorni** dalla comunicazione senza pronuncia, il gestore
  procede con la modifica (silenzio-assenso, art. 6 co. 1 ultima parte);
- l'autorita' competente, **ove necessario**, aggiorna l'autorizzazione
  in atto; l'aggiornamento **non incide sulla durata** dell'AUA
  (art. 6 co. 1).

**Strada B** - intende la modifica come **sostanziale** ex ante: applica
l'art. 6 co. 2. Presenta direttamente nuova domanda di AUA ex art. 4
all'autorita' competente, senza passare dalla comunicazione del co. 1.
La modifica non puo' essere eseguita fino al rilascio della nuova
autorizzazione.

### Step 3 - Tabella decisione

Per ciascun titolo incorporato coinvolto, classificare la modifica
nelle quattro caselle:

|                                              | Modifica certamente non sostanziale | Modifica dubbia | Modifica certamente sostanziale |
|----------------------------------------------|-------------------------------------|-----------------|---------------------------------|
| Strada operativa raccomandata                | Strada A (comunicazione)            | Strada A con pronuncia anticipata di "non sostanzialita'" o consulenza pre-istanza | Strada B (nuova domanda art. 4) |
| Documentazione                               | Comunicazione + relazione tecnica   | Comunicazione + relazione tecnica con analisi sostanzialita' | Documentazione completa art. 4 |
| Esercizio                                    | Procedere dopo 60 gg di silenzio    | Attendere risposta (rischio art. 6 co. 3) | Sospendere fino a nuova autorizzazione |
| Termini                                      | 30 gg riqualifica + 60 gg pronuncia | come Strada A   | 30/90/120/150 gg ex art. 4 (vedi `tasks/pianifica-termini.md`) |

### Step 4 - Verifica criteri regionali (art. 6 co. 4)

Le Regioni e Province Autonome possono:

- definire **ulteriori criteri** per qualificare le modifiche come
  sostanziali;
- indicare **modifiche per cui non sussiste l'obbligo** di comunicazione.

La skill non conosce le discipline regionali specifiche; invitare
l'utente a consultare la legge regionale o le linee guida operative
AUA della propria Regione/PA.

### Step 5 - Aggiornamento documentale dell'AUA

A valle di una modifica non sostanziale (strada A), l'autorita'
competente puo' aggiornare il provvedimento AUA. L'aggiornamento non
incide sulla durata: la scadenza dei 15 anni resta calcolata dalla
data di rilascio originario (art. 3 co. 6 + art. 6 co. 1).

A valle di una modifica sostanziale (strada B), viene rilasciata una
**nuova AUA** con propria data: la durata di 15 anni decorre dalla
nuova data di rilascio (interpretazione operativa dell'art. 3 co. 6
combinato con art. 6 co. 2-3; consultare l'autorita' competente in
caso di dubbio).

## Output

Un report sintetico (Markdown):

```
# Triage modifica AUA art. 6 - [nome impianto]

## Modifica proposta
- Descrizione: [...]
- Titolo/titoli incorporati interessati: [...]
- Quantificazione: [...]

## Classificazione preliminare
- Strada raccomandata: A (comunicazione non sostanziale) / B (nuova
  domanda sostanziale) / dubbia
- Motivazione: rinvio ai criteri di settore del titolo coinvolto:
  scarichi -> art. 124 D.Lgs. 152/2006; emissioni in atmosfera ->
  art. 269 co. 8 D.Lgs. 152/2006; rifiuti -> artt. 215 e 216 D.Lgs.
  152/2006; acustica -> L. 447/1995; fanghi -> D.Lgs. 99/1992 art. 9;
  radiazioni -> D.Lgs. 101/2020 artt. 24 e 26. Indicare nel report
  l'articolo specifico applicato al caso.
- Verifica regionale (art. 6 co. 4): da effettuare in [Regione / PA]

## Flusso procedurale (se Strada A)
- Comunicazione all'autorita' competente: T0
- Decorrenza riqualifica (30 gg, art. 6 co. 3): T0 + 30
- Decorrenza silenzio-assenso (60 gg, art. 6 co. 1): T0 + 60
- Effetto sulla durata AUA: nessuno (art. 6 co. 1)

## Flusso procedurale (se Strada B)
- Nuova domanda ex art. 4: T0
- Termine atteso rilascio: vedi `tasks/pianifica-termini.md`
- Effetto sulla durata: nuova AUA con propria scadenza 15 anni
- Modifica non eseguibile fino al rilascio

## Avvertenza
La qualificazione finale e' di competenza dell'autorita' competente.
La skill propone una classificazione preliminare basata sui criteri
del regolamento e delle normative di settore richiamate. Una
classificazione errata della modifica come "non sostanziale" puo'
comportare il blocco dell'esercizio per ordine ex art. 6 co. 3.
Quando la qualificazione e' dubbia e l'investimento e' rilevante,
valutare una pre-consulenza con l'autorita' competente o procedere
ex art. 6 co. 2 (nuova domanda) per evitare il rischio.
```

## Limiti del task

- Non determina autonomamente la qualifica di "sostanzialita'": la
  decisione richiede interpretazione delle norme di settore di ciascun
  titolo incorporato.
- Non sostituisce la consulenza preventiva con l'autorita' competente
  per casi di dubbia interpretazione (la prassi delle Province/ARPA
  varia per regione e per tipologia di impianto).
- Non valuta gli aspetti edilizio-urbanistici o di sicurezza che
  possono accompagnare una modifica impiantistica (titolo edilizio,
  CPI, sicurezza lavoratori): la skill copre solo il versante ambientale
  AUA.
- Non considera la disciplina di subingresso o di volturazione del
  titolo, che e' altro istituto.
