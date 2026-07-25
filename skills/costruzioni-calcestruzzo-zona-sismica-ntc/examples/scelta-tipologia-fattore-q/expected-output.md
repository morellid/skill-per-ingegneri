# Output atteso — Scelta di tipologia e fattore di comportamento (NTC 2018 §7.4.3)

> Supporto documentale: inquadra tipologia, αu/α1 e classe di duttilità. **Non** calcola il valore numerico di q
> (§7.3.1).

## 1. Tipologia strutturale (§7.4.3.1)

- I telai assorbono alla base **~80% ≥ 65%** del taglio totale → la struttura è una **struttura a telaio** (resistenza
  alle azioni sia verticali sia orizzontali affidata principalmente ai telai spaziali).
- Non essendoci pareti significative, non ricorrono le tipologie a pareti o miste.

## 2. Fattore di sovraresistenza αu/α1 (§7.4.3.2)

- Struttura **regolare in pianta**, a telaio con **più piani e più campate** → **αu/α1 = 1,3** (voce a) del §7.4.3.2:
  «strutture a telaio con più piani e più campate»).
- (Per confronto: telaio di un piano 1,1; più piani e una sola campata 1,2.)

## 3. Classe di duttilità CD"A"/CD"B" (§7.4.3.2)

- In generale una struttura a telaio può essere progettata in **CD"A"** o **CD"B"**.
- **Attenzione alle travi a spessore**: le strutture aventi i telai resistenti all'azione sismica realizzati, **anche
  in una sola delle direzioni principali, con travi a spessore**, **devono essere progettate in CD"B"**, salvo che tali
  travi non si possano considerare elementi strutturali **«secondari»**.
- → Nel caso in esame la presenza di **travi a spessore** in una direzione impone la **CD"B"** (a meno di classificarle
  come secondarie ai sensi del §7.2.3).

## 4. Determinazione di q

- Il **valore numerico di q** si calcola secondo il **§7.3.1 e la Tab. 7.3.II** (q = q0·KR, con q0 funzione della
  tipologia e della CD, e KR per la regolarità in altezza), che sono **fuori scope** di questa skill → skill
  `fattore-comportamento-q-sismica-ntc`. Qui si fornisce l'ingrediente **αu/α1** (che entra in q0).

## 5. Sintesi

| Aspetto | Esito |
|---|---|
| Tipologia (§7.4.3.1) | **Struttura a telaio** (telai ≥ 65% del taglio) |
| αu/α1 (§7.4.3.2) | **1,3** (telaio, più piani e più campate) |
| Classe di duttilità (§7.4.3.2) | **CD"B"** obbligata dalle travi a spessore (salvo secondarie) |
| Valore di q | Da §7.3.1 / Tab. 7.3.II (skill `fattore-comportamento-q-sismica-ntc`) |

**Fuori scope**: calcolo di q (§7.3.1); verifiche e gerarchia delle resistenze (§7.4.4, task
`applica-gerarchia-delle-resistenze`); dettagli costruttivi (§7.4.6).

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
