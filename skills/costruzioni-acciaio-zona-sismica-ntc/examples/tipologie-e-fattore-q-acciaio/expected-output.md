# Esempio — Output atteso: tipologia, materiali e αu/α1 di un telaio in acciaio

> Supporto documentale (NTC 2018, par. 7.5). Non è una verifica strutturale: le verifiche di membrature e
> collegamenti (§§ 7.5.3.1-7.5.6) restano a carico del progettista.

## 1. Tipologia strutturale e zone dissipative (§7.5.2.1)

- Lo schema a telai momento-resistenti rientra nelle **strutture intelaiate** (tipologia a): resistono alle forze
  orizzontali con comportamento prevalentemente **flessionale**.
- Le **zone dissipative** sono principalmente collocate **alle estremità delle travi**, in prossimità dei
  collegamenti trave-colonna, dove si formano le cerniere plastiche (dissipazione per flessione ciclica plastica).

## 2. Fattore di sovraresistenza del materiale γov (§7.5.1)

- Per l'acciaio **S355**, il fattore di sovraresistenza del materiale è **γov = 1,25** (vale per S235, S275 ed
  S355; sarebbe 1,15 per S420 ed S460).
- L'acciaio deve essere conforme al **§11.3.4.9**.

## 3. Fattore di comportamento (§7.5.2.2)

- Trattandosi di **edificio a telaio con più piani e più campate**, regolare in pianta, si può adottare
  **αu/α1 = 1,3**.
- Il valore massimo di **q0** si ricava dalla **Tab. 7.3.II** per la tipologia «strutture intelaiate»; nel
  framework generale **q = q0·KR** (§7.3.1). Il valore di q0 è valido a patto di rispettare le regole di progetto
  e dettaglio dei §§ 7.5.3-7.5.6.

## Sintesi

- Tipologia: **strutture intelaiate**; zone dissipative **alle estremità delle travi**.
- **γov = 1,25** (S355).
- **αu/α1 = 1,3** (telaio più piani, più campate); **q0** da Tab. 7.3.II.

**Fuori scope**: verifiche RES/DUT di membrature e collegamenti, q0 numerico, requisiti statici §4.2 e framework
del fattore q §7.3.1 (skill dedicate). Non sostituisce il progettista.
