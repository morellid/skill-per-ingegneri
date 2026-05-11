---
name: cedimenti-edometrici-ntc
description: Supporta il controllo di completezza di una verifica dei cedimenti in ambito NTC 2018/Circolare 7-2019. Aiuta a verificare che il progettista abbia esplicitato prestazioni attese, spostamenti compatibili, metodo di interazione terreno-struttura e confronto SLE, senza sostituire il calcolo geotecnico con formule non presenti nelle fonti ufficiali lette.
license: MIT
---

# Verifica documentale dei cedimenti geotecnici - NTC 2018

## Quando usare questa skill

Usala quando devi rivedere una relazione o un calcolo geotecnico e vuoi controllare se la verifica dei cedimenti e' impostata in modo coerente con NTC 2018 e Circolare 7/2019.

## Avvertenza

Questa skill e' uno strumento di supporto e **non sostituisce** il giudizio del professionista firmatario. Non calcola automaticamente il cedimento edometrico: le fonti ufficiali lette non forniscono una formula chiusa da implementare come calcolatore normativo.

## Sotto-attivita'

- verifica completezza della relazione / nota di calcolo -> `tasks/calcola-cedimento.md`

## Cosa la skill puo' fare

- controllare se sono dichiarati spostamenti o cedimenti compatibili;
- controllare se il metodo di analisi terreno-struttura e' esplicitato;
- controllare se il report distingue stato finale e andamento nel tempo;
- evidenziare dati mancanti da richiedere al progettista.

## Cosa la skill non fa

- non sceglie al posto del progettista il metodo geotecnico;
- non implementa formule da letteratura non presenti nelle fonti ufficiali lette;
- non sostituisce prove edometriche, modellazione geotecnica o relazione geologica.