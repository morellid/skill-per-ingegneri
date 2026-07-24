# Esempio — Output atteso: materiali, tipologia e q0 di un telaio composto

> Supporto documentale (NTC 2018, par. 7.6). Non è una verifica strutturale: le verifiche di membrature e
> collegamenti (§§ 7.6.4-7.6.8) restano a carico del progettista.

## 1. Requisiti dei materiali (§7.6.1)

| Requisito (§7.6.1) | Limite | Valore proposto | Esito |
|---|---|---|---|
| Classe del calcestruzzo | ≥ C20/25 (LC20/22) e ≤ C40/50 (LC40/44) | C25/30 | ✅ |
| Acciaio per c.a. | B450C (B450A solo casi §7.4.2.2) | B450C | ✅ |
| Acciaio strutturale | qualità §7.5 e §11.3.4 | S355 | ✅ |

- **C25/30** è compreso tra C20/25 e C40/50 → **ammesso**.
- **B450C** è il tipo richiesto → **conforme**.
- **Requisiti dei materiali soddisfatti.**

## 2. Tipologia strutturale e fattore di comportamento (§7.6.2)

- Lo schema a telai rientra nelle **strutture intelaiate** (tipologia a); il funzionamento è quello descritto al
  §7.5.2.
- Il valore massimo di **q0** si ricava dalla **Tab. 7.3.II** (con le prescrizioni del §7.5.2 e a condizione di
  rispettare le regole del capitolo 7.6); nel framework generale **q = q0·KR** (§7.3.1).

## 3. Rigidezza della sezione composta (§7.6.3)

- Per le sezioni con **calcestruzzo in compressione**, la rigidezza elastica si valuta con il **coefficiente di
  omogeneizzazione n = Ea/Ecm = 7**; il momento d'inerzia **non fessurato I1** include la porzione di soletta
  nella larghezza efficace.
- Per le sezioni con **cls in trazione** si usa il momento d'inerzia **fessurato I2** (cls non reagente).

## Sintesi

- Materiali **conformi** al §7.6.1 (C25/30, B450C, S355).
- Tipologia **intelaiata**; **q0** da Tab. 7.3.II.
- Rigidezza con **n = 7** (cls compresso).

**Fuori scope**: verifiche RES/DUT, q0 numerico, requisiti statici §4.3, regole sismiche dell'acciaio §7.5 e
fattore q §7.3.1 (skill dedicate). Non sostituisce il progettista.
