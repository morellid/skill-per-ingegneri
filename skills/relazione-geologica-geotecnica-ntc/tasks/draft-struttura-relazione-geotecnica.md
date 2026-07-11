# Task: Bozza di struttura (indice commentato) della relazione geotecnica

## Obiettivo

Produrre un indice commentato di relazione geotecnica conforme al contenuto
minimo di NTC 2018 par. 6.1.2 e ai contenuti indicativi di Circolare 7/2019
par. C6.2.2.5, modulato sul tipo di opera e sulla fase progettuale
dichiarati dall'utente. L'output e' una struttura di lavoro, non la
relazione.

## Input richiesti

- tipo di opera o intervento (es. edificio su fondazioni superficiali,
  opera di sostegno, rilevato);
- fase progettuale (fattibilita' / definitivo / esecutivo);
- impiego o meno del metodo osservazionale (par. 6.2.5 NTC);
- eventuali specificita' note (falda, terreni scadenti, opera in zona ben
  conosciuta di modesta rilevanza).

## Fonti da leggere

- `references/estratti/ntc2018-cap6-relazioni.md`
- `references/estratti/circ-7-2019-c6-relazioni.md` (sezioni "Relazione
  geotecnica" e "Indagini e caratterizzazione geotecnica")
- `references/estratti/circ-7-2019-c9-c10-ruoli-elaborati.md` (per il
  richiamo ai certificati di laboratorio e ai ruoli)

## Procedura

1. Parti dall'indice base sotto riportato, derivato dalle dodici voci di
   Circ. C6.2.2.5 e dal contenuto minimo di NTC par. 6.1.2.
2. Modula le sezioni sul tipo di opera e sulla fase progettuale (l'elenco
   della Circolare e' indicativo e va commisurato al contesto: Circ.
   C6.2.2.5). Motiva ogni sezione omessa.
3. Per ogni sezione, annota in una riga cosa deve contenere e il
   riferimento normativo.
4. Se l'utente ha dichiarato il metodo osservazionale, aggiungi le sezioni
   dedicate (soluzioni alternative con verifiche, parametri di controllo e
   limiti di accettabilita', piano di monitoraggio con strumentazione e
   procedure: NTC par. 6.2.5; Circ. C6.2.2.5).
5. Se l'opera e' di modesta rilevanza in zona ben conosciuta, prevedi la
   sezione che documenta le indagini preesistenti utilizzate e
   l'assunzione di piena responsabilita' del progettista (NTC par. 6.2.2).
6. Chiudi con l'elenco degli allegati minimi e l'avvertenza.

## Indice base (da modulare)

```markdown
# Relazione geotecnica - [opera] - [fase progettuale]

1. Premessa e descrizione del sito, delle opere e degli interventi
   [Circ. C6.2.2.5; scelte progettuali: NTC par. 6.1.2]
2. Inquadramento geologico di riferimento (sintesi dalla relazione
   geologica e rinvio ad essa) [NTC par. 6.2.1; Circ. C6 intro]
3. Valutazione della pericolosita' ambientale (stabilita' del territorio
   in condizioni statiche e sismiche) [Circ. C6.2.2.5]
4. Risposta sismica locale [Circ. C6.2.2.5]
5. Problemi geotecnici e scelte tipologiche [Circ. C6.2.2.5]
6. Stati limite considerati e metodi di analisi [Circ. C6.2.2.5;
   EQU/STR/GEO/UPL/HYD: Circ. C6.2.4.1]
7. Programma delle indagini e delle prove geotecniche (definito dal
   progettista) [NTC par. 6.2.2; Circ. C6.2.2.5; mezzi di indagine:
   Tabella C6.2.I, Circ. C6.2.2.1]
8. Risultati delle indagini e delle prove; certificati dei laboratori ex
   art. 59 DPR 380/2001 [NTC par. 6.2.2; Circ. C6.2.2.1-C6.2.2.2; Circ.
   C9.1 lett. g]
9. Caratterizzazione fisica e meccanica di terreni e rocce; valori
   caratteristici dei parametri geotecnici con relativa giustificazione
   (parametri appropriati, valori medi/minimi) [NTC par. 6.2.2; Circ.
   C6.2.2.3-C6.2.2.4]
10. Modelli geotecnici di sottosuolo: volume significativo, unita'
    omogenee, regime delle pressioni interstiziali, valori caratteristici
    e di progetto [NTC par. 6.2.2; Circ. C6.2.2.5]
11. Analisi e verifiche: SLU (approccio e combinazioni dichiarati; per
    stabilita' globale A2+M2+R2), SLU idraulici (UPL/HYD), SLE
    (spostamenti compatibili e prestazioni attese, Ed <= Cd) [NTC parr.
    6.2.4.1-6.2.4.3; Circ. C6.2.4.1-C6.2.4.3]
12. Confronto dei risultati con le prestazioni previste per le opere
    [Circ. C6.2.2.5]
13. Fasi e modalita' costruttive, con i connessi stati limite anche
    temporanei [NTC par. 6.2.3; Circ. C6.2.3]
14. Prescrizioni sulle modalita' costruttive [Circ. C6.2.2.5]
15. Piano di monitoraggio in corso d'opera e in esercizio (se previsto,
    definito e illustrato qui) [NTC par. 6.2.6; Circ. C6.2.2.5]

Allegati minimi [Circ. C6.2.2.5]:
- planimetria con ubicazione delle indagini (anche storiche/di esperienza
  locale se utilizzate)
- documentazione delle indagini in sito e in laboratorio
- sezioni stratigrafiche con profili delle grandezze misurate
```

## Output

L'indice modulato, con: le annotazioni per sezione, l'elenco delle sezioni
omesse con motivazione, l'elenco degli input ancora mancanti che il
progettista deve procurare, e l'avvertenza finale ("struttura di supporto:
la redazione e la firma della relazione geotecnica restano responsabilita'
del Progettista - Circ. C9.1 lett. g e C10.1").

## Limiti

- L'indice e' derivato da un elenco che la Circolare dichiara indicativo:
  non esiste un indice obbligatorio unico e la modulazione resta una scelta
  del progettista.
- Il task non compila i contenuti delle sezioni e non fornisce parametri,
  formule o coefficienti.
- I riferimenti ai livelli di progettazione (Codice dei contratti, art. 23)
  sono fuori scope: la modulazione per fase e' trattata solo nei termini
  del par. C6.2.2.5.
