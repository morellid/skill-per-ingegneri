# Task: individua-direttive

Dato un prodotto elettrico/elettronico, determina quale/i direttiva/e di prodotto
si applica/applicano (LVD, EMC, RED). Supporto documentale.

## Input

- Descrizione del prodotto: funzione, alimentazione/tensione, presenza di parti a
  radiofrequenza (trasmissione/ricezione radio), destinazione d'uso.

## Procedura

1. **LVD 2014/35/UE**: si applica se il prodotto e' **materiale elettrico** con
   **tensione nominale 50-1000 V ca** o **75-1500 V cc** (salvo esclusioni
   allegato II). Al di fuori di questi limiti la LVD non si applica (ma possono
   applicarsi altre discipline).
2. **EMC 2014/30/UE**: si applica agli **apparecchi** che possono **generare** o
   essere **influenzati** da perturbazioni elettromagnetiche; disciplina dedicata
   per gli **impianti fissi**.
3. **RED 2014/53/UE**: si applica alle **apparecchiature radio** (che emettono e/o
   ricevono onde radio per comunicazione o radiodeterminazione). La RED
   **incorpora** gli obiettivi di sicurezza della **LVD** (art. 3.1.a, senza
   limiti minimi di tensione) e i requisiti **EMC** (art. 3.1.b): per un'apparecchiatura
   radio non si applicano separatamente LVD ed EMC.
4. **Combinazioni**: un prodotto non radio puo' ricadere in **LVD + EMC**
   insieme (es. un alimentatore da rete). Verifica sempre le esclusioni e le altre
   direttive potenzialmente applicabili (macchine, ATEX, ErP, RoHS - solo rinvio).

## Output

- Elenco delle direttive applicabili e motivazione (tensione, funzione radio,
  emissione/immunita').
- Nota sull'assorbimento di LVD/EMC nella RED per le apparecchiature radio.

## Avvertenze

- La skill non individua le **norme armonizzate**: la scelta e' del fabbricante/
  laboratorio.
- Altre direttive (macchine, ATEX, ecc.) sono solo richiamate, non trattate.
