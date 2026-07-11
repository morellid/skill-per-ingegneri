# Task: Check di completezza della relazione geotecnica

## Obiettivo

Controllare che una relazione geotecnica contenga il contenuto minimo
fissato dalle NTC 2018 (par. 6.1.2) e gli elementi indicativi della
Circolare 7/2019 (par. C6.2.2.5), inclusi valori caratteristici,
certificati di laboratorio e quadro delle verifiche.

## Input richiesti

- testo (o estratto significativo) della relazione geotecnica;
- tipo di opera o intervento e fase progettuale;
- indicazione se e' stato impiegato il metodo osservazionale (par. 6.2.5
  NTC), se non deducibile dal documento.

## Fonti da leggere

- `references/estratti/ntc2018-cap6-relazioni.md`
- `references/estratti/circ-7-2019-c6-relazioni.md` (sezioni "Indagini e
  caratterizzazione geotecnica", "Valori caratteristici", "Relazione
  geotecnica", "Fasi costruttive e verifiche")
- `references/estratti/circ-7-2019-c9-c10-ruoli-elaborati.md` (sezione "Chi
  firma cosa")

## Checklist di verifica

Per ogni punto: esito "presente / carente / assente", con citazione del
passaggio del documento esaminato e riferimento normativo.

### A. Contenuto minimo del DM (NTC par. 6.1.2)

1. scelte progettuali (tipologia dell'opera/intervento in rapporto ai
   problemi geotecnici);
2. programma e risultati delle indagini;
3. caratterizzazione e modellazione geotecnica (par. 6.2.2);
4. analisi per il dimensionamento geotecnico delle opere;
5. descrizione delle fasi e modalita' costruttive.

### B. Contenuti indicativi della Circolare (C6.2.2.5, dodici voci)

descrizione di sito/opere/interventi; pericolosita' ambientale (stabilita'
del territorio in condizioni statiche e sismiche); risposta sismica locale;
problemi geotecnici e scelte tipologiche; stati limite identificati e
metodi di analisi; programma delle indagini e prove; caratterizzazione
fisico-meccanica e valori caratteristici; modelli geotecnici di sottosuolo
con valori caratteristici e di progetto; risultati delle analisi; confronto
con le prestazioni previste; prescrizioni sulle modalita' costruttive;
eventuale piano di monitoraggio. Le voci assenti vanno segnalate chiedendo
se la modulazione e' motivata da fase progettuale/tipo di opera (l'elenco
e' dichiarato indicativo).

### C. Corredo documentale

1. planimetria con ubicazione delle indagini, incluse quelle storiche o di
   esperienza locale se utilizzate (Circ. C6.2.2.5);
2. documentazione delle indagini in sito e in laboratorio (Circ. C6.2.2.5;
   elementi di dettaglio in C6.2.2.1);
3. numero adeguato di sezioni stratigrafiche con profili delle grandezze
   misurate (Circ. C6.2.2.5).

### D. Modello geotecnico e valori caratteristici

1. il volume significativo e' individuato (NTC par. 6.2.2);
2. il modello geotecnico e' uno schema in unita' omogenee
   fisico-meccaniche con regime delle pressioni interstiziali (NTC par.
   6.2.2; Circ. C6.2.2);
3. i valori caratteristici sono definiti come stima ragionata e cautelativa
   per ogni stato limite considerato (NTC par. 6.2.2) e la loro scelta e'
   giustificata (parametri appropriati al meccanismo; valori prossimi ai
   medi o ai minimi con motivazione: Circ. C6.2.2.4);
4. per ammassi rocciosi/terreni a struttura complessa e' specificato se la
   resistenza caratteristica si riferisce alle discontinuita' o
   all'ammasso (NTC par. 6.2.2);
5. quote piezometriche e pressioni interstiziali con variabilita' spaziale
   e temporale considerata (NTC par. 6.2.2).

### E. Prove e certificati

1. le prove di laboratorio sono certificate da laboratori ex art. 59 DPR
   380/2001 e i certificati sono presenti o richiamati (NTC par. 6.2.2;
   Circ. C9.1 lett. g);
2. in alternativa, se l'opera e' di modesta rilevanza in zona ben
   conosciuta: le indagini preesistenti utilizzate sono documentate e la
   responsabilita' del progettista su ipotesi e scelte e' esplicita (NTC
   par. 6.2.2).

### F. Verifiche della sicurezza e delle prestazioni

1. gli stati limite ultimi pertinenti sono identificati (EQU, STR, GEO,
   UPL, HYD: Circ. C6.2.4.1) e l'approccio progettuale/combinazioni di
   coefficienti sono dichiarati (NTC par. 6.2.4.1);
2. per le verifiche di stabilita' globale e' usata la combinazione
   A2+M2+R2 dell'Approccio 1 (Circ. C6.2.4.1);
3. per gli SLE sono esplicitati spostamenti compatibili e prestazioni
   attese, con confronto Ed <= Cd (NTC par. 6.2.4.3);
4. le fasi esecutive sono individuate con i connessi stati limite, anche
   temporanei (NTC par. 6.2.3; Circ. C6.2.3).

### G. Metodo osservazionale e monitoraggio (se pertinenti)

1. se e' impiegato il metodo osservazionale: limiti di accettabilita',
   dimostrazione di accettabilita' della soluzione, soluzioni alternative
   con oneri, sistema di monitoraggio con piani di controllo (NTC par.
   6.2.5); soluzioni alternative con verifiche, parametri di controllo e
   piano di monitoraggio con strumentazione e procedure (Circ. C6.2.2.5);
2. se e' previsto il monitoraggio: il programma e' definito e illustrato
   nella relazione geotecnica (NTC par. 6.2.6).

## Output

```markdown
# Esito check relazione geotecnica - [identificativo documento]

| Sez. | Requisito | Riferimento | Esito | Evidenza / nota |
|------|-----------|-------------|-------|-----------------|
| A.1 | Scelte progettuali | NTC par. 6.1.2 | ... | ... |
| ... | ... | ... | ... | ... |

## Carenze rilevate
- [requisito, riferimento normativo, cosa manca]

## Voci indicative assenti da motivare
- [voci C6.2.2.5 assenti, con domanda sulla modulazione]

## Richieste integrative suggerite
- [...]

## Avvertenza
Esito documentale, da sottoporre alla verifica del professionista
firmatario; non costituisce validazione delle analisi geotecniche.
```

## Limiti

- Il check non rifa' i calcoli ne' giudica l'adeguatezza dei parametri
  geotecnici adottati: controlla presenza, giustificazione e coerenza
  documentale.
- I valori numerici dei coefficienti parziali (Tabb. 6.2.I-6.2.III NTC) non
  sono coperti: la verifica sull'approccio si ferma alla dichiarazione di
  approccio/combinazione.
- La risposta sismica locale e le azioni sismiche (NTC parr. 3.2, 7.11)
  sono verificate solo come presenza della voce, non nel merito.
