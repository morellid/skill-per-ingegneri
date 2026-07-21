# Output atteso - Conseguenze della non regolarità in altezza (§7.3.1, §7.3.3.1)

## Fattore di comportamento (§7.3.1)

Il limite superiore del fattore di comportamento allo SLV è **q_lim = q0 · KR**, dove il fattore **KR** dipende
dalla regolarità **in altezza**:

- **KR = 1** per costruzioni regolari in altezza;
- **KR = 0,8** per costruzioni **non regolari in altezza**.

Poiché l'edificio è **non regolare in altezza**, si applica **KR = 0,8**: il fattore di comportamento di base q0
va **ridotto del 20%** (q_lim = 0,8·q0). Ne consegue una **maggiore domanda sismica** di progetto. Il valore di
q0 (Tab. 7.3.II, in funzione di classe di duttilità e tipologia) resta da determinare a cura del progettista.

## Metodo di analisi (§7.3.3.1)

L'**analisi lineare statica** può essere effettuata **a condizione che**:

1. T1 non superi **2,5 TC o TD**; **e**
2. la costruzione sia **regolare in altezza**.

Qui la condizione 1 è soddisfatta (T1 ≈ 0,9 s ≤ 2,5 TC), ma la condizione 2 **non** lo è (edificio non regolare
in altezza). Pertanto l'**analisi lineare statica non è ammessa**: si deve ricorrere all'**analisi lineare
dinamica** (modale con spettro di risposta) o all'analisi non lineare.

## Avvertenza

La skill **inquadra** le conseguenze normative (KR e ammissibilità dell'analisi statica). La determinazione di q0
e l'esecuzione dell'analisi restano compito del progettista; la stima e i limiti di T1 sono trattati dalla skill
`periodo-proprio-t1-ntc` (§7.3.3.2).
