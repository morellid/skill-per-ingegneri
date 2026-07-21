# Output atteso - Inquadramento delle verifiche SLE (frecce e kdef)

## 1. Classe di servizio (§4.4.5, Tab. 4.4.II)

Ambiente interno riscaldato con umidità relativa dell'aria ≤ 65% (salvo poche settimane/anno): **classe di
servizio 1** (Tab. 4.4.II).

## 2. Coefficiente kdef (§4.4.7, Tab. 4.4.V)

Per il **legno massiccio** in **classe di servizio 1**, la Tab. 4.4.V fornisce **kdef = 0,60**. (In classe
2 sarebbe 0,80; in classe 3, 2,00.)

## 3. Deformazione istantanea e a lungo termine (§4.4.7)

- La **deformazione istantanea** si calcola con i **valori medi** dei moduli elastici delle membrature (e
  il modulo di scorrimento istantaneo dei collegamenti).
- La **deformazione a lungo termine** si calcola riducendo i moduli elastici medi mediante il fattore
  **1/(1 + kdef) = 1/(1 + 0,60) = 1/1,60**, per tener conto dell'aumento di deformabilità nel tempo
  (viscosità e umidità).

La freccia netta è la somma della freccia dovuta ai soli carichi permanenti e di quella dovuta ai soli
carichi variabili, dedotta l'eventuale controfreccia.

## 4. Limiti di freccia raccomandati (§4.4.7)

Con **L = 4,50 m = 4500 mm** (requisiti minimi indicativi):

- **freccia istantanea** dovuta ai soli carichi variabili (combinazione rara): **< L/300 = 4500/300 = 15
  mm**;
- **freccia finale**: **< L/200 = 4500/200 = 22,5 mm**.

(Per le mensole, al posto di L si usa il doppio dello sbalzo.) Limitazioni più severe possono essere
necessarie in relazione a elementi portati non strutturali (rivestimenti, pavimenti, tramezzi).

## Avvertenza

La skill **inquadra** la classe di servizio, il kdef e i limiti di freccia; **non calcola** le frecce
effettive (che dipendono da carichi, moduli elastici del §11.7 e schema statico) e **non decide** l'esito
della verifica. Il calcolo resta compito del progettista strutturale, che deve leggere il §4.4 e il §11.7
delle NTC 2018.
