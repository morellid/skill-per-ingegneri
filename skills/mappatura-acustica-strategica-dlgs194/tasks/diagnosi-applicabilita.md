# Task: Diagnosi di applicabilita' e obblighi (D.Lgs. 194/2005)

## Obiettivo

Dato un elemento (agglomerato, asse stradale/ferroviario, aeroporto), determinare
se rientra nel D.Lgs. 194/2005, quale soggetto e' obbligato, quali deliverable
(mappe/piani) e quali scadenze si applicano.

## Input richiesti

- tipo di elemento: agglomerato / asse stradale / asse ferroviario / aeroporto;
- dati dimensionali: **popolazione** (agglomerato), **veicoli/anno** (strada),
  **treni/anno** (ferrovia), **movimenti/anno** (aeroporto);
- interesse **nazionale / di piu' regioni / locale** (per il livello di
  competenza e di trasmissione);
- ruolo di chi chiede: autorita' regionale/comunale / gestore infrastruttura.

## Fonti da leggere

- `references/estratti/mappatura-acustica-checklist.md` sezioni 1-4
- se serve conferma: `references/fonti/dlgs-194-2005.md` (artt. 2-4)

## Procedura

### Passo 1 - Soglie di applicabilita' (art. 2)
- Agglomerato: **> 100.000 abitanti** (per la prima tornata art. 3 c. 1: > 250.000);
- Asse stradale principale: **> 3.000.000 veicoli/anno** (prima tornata: > 6.000.000);
- Asse ferroviario principale: **> 30.000 treni/anno** (prima tornata: > 60.000);
- Aeroporto principale: **> 50.000 movimenti/anno**.
Se sotto soglia: l'elemento non e' soggetto agli obblighi del D.Lgs. 194/2005
(fermi restando gli obblighi ordinari della L. 447/1995).

### Passo 2 - Soggetto obbligato (artt. 3-4)
- Agglomerati: **autorita' individuata dalla regione/PA**;
- Assi/aeroporti principali: **societa'/enti gestori**;
- Infrastrutture di interesse nazionale/piu' regioni: trasmissione al **Ministero
  dell'ambiente** e alle regioni/PA competenti.

### Passo 3 - Deliverable
- **Mappa acustica strategica / mappatura acustica** (art. 3), requisiti minimi
  allegato 4, dati allegato 6;
- **Piano d'azione** (art. 4), requisiti minimi allegato 5.

### Passo 4 - Scadenze (quinquennali)
- Mappe: 30/6/2007 (prima tornata > 250k) -> 30/6/2017 -> 31/3/2022 -> ogni 5 anni;
- Piani: 18/7/2008 (prima tornata) -> 18/7/2018 -> 18/4/2024 -> ogni 5 anni;
- riesame delle mappe **almeno ogni 5 anni**; riesame dei piani in caso di
  **sviluppi sostanziali**.

## Output atteso

- esito di applicabilita' (soglia superata? quale) con la citazione dell'art. 2;
- **soggetto obbligato** e livello di competenza/trasmissione (artt. 3-4);
- **deliverable** dovuti (mappe e/o piani) con i relativi allegati;
- **scadenze** applicabili;
- avvertenza: la skill non produce le mappe/piani ne' esegue la modellazione
  acustica; la determinazione definitiva spetta all'autorita' competente e al
  tecnico acustico.
