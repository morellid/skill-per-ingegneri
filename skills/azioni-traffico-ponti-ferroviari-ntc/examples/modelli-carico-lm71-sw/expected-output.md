# Output atteso

## Modello di carico LM 71 (NTC 2018 §5.2.2.2.1.1)

Schematizza il **traffico ferroviario normale**:

- **4 assi da Q_vk = 250 kN**, disposti a interasse di **1,60 m** (schema interassi 0,8-1,6-1,6-1,6-0,8 m);
- **carico distribuito q_vk = 80 kN/m** in entrambe le direzioni, a partire da **0,8 m** dagli assi
  d'estremità e per lunghezza illimitata;
- **eccentricità** rispetto all'asse del binario dal rapporto **Q_V2/Q_V1 = 1,25** [5.2.1], pari a **s/18**
  (s = 1435 mm), nella direzione più sfavorevole;
- **coefficiente di adattamento α = 1,1** (ferrovie ordinarie).

## Modelli di carico SW (NTC 2018 §5.2.2.2.1.2, Tab. 5.2.I)

| Tipo | Traffico | q_vk [kN/m] | a [m] | c [m] | α |
|---|---|---|---|---|---|
| **SW/0** | normale (travi continue, se più sfavorevole dell'LM71) | **133** | **15,0** | **5,3** | **1,1** |
| **SW/2** | **pesante** | **150** | **25,0** | **7,0** | **1,0** |

## Sintesi

| Modello | Valore caratteristico | α (ferrovie ordinarie) |
|---|---|---|
| LM 71 | 4×250 kN @ 1,60 m + 80 kN/m | 1,1 |
| SW/0 | 133 kN/m (a 15,0 m, c 5,3 m) | 1,1 |
| SW/2 | 150 kN/m (a 25,0 m, c 7,0 m) | 1,0 |
| Treno scarico | 10,0 kN/m | — |

## Note

- Nel seguito i riferimenti ai modelli LM71, SW/0 e SW/2 si intendono **pari al prodotto** dei valori
  caratteristici per il coefficiente di adattamento **α**.
- Il **treno scarico** (10,0 kN/m) si usa per alcune verifiche particolari; i **marciapiedi** non aperti al
  pubblico si schematizzano con 10 kN/m² (non contemporaneo ai convogli).
- Gli **effetti dinamici** (Φ2/Φ3) e le **azioni orizzontali** (centrifuga, serpeggio, avviamento/frenatura)
  sono trattati nel task `inquadra-effetti-dinamici-azioni-orizzontali`. La skill inquadra i carichi; **non**
  esegue le combinazioni né le verifiche.
