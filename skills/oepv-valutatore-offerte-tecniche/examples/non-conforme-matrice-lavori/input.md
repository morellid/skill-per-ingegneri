# Esempio: Appalto lavori - matrice OEPV con criticita'

## Contesto

Un'Azienda Sanitaria Locale ha pubblicato un appalto lavori per la realizzazione di una nuova palestra fisioterapica. Il RUP ha scelto di aggiudicare con OEPV (facoltativo per questo tipo di lavori) e ha predisposto la seguente matrice criteri nel disciplinare di gara.

## Dati di gara

**Tipo contratto**: Lavori
**Oggetto**: Realizzazione palestra fisioterapica - lotto funzionale A (struttura, impianti, finiture)
**Importo a base d'asta**: EUR 2.100.000 (IVA esclusa)
**Criterio di aggiudicazione**: OEPV qualita'/prezzo (scelto dalla SA)

## Matrice criteri come appare nel disciplinare di gara

---

**CRITERI DI VALUTAZIONE OFFERTE**

| N. | Criterio | Punteggio massimo |
|----|----------|-------------------|
| 1 | Qualita' dell'offerta tecnica | 30 |
| 2 | Solidita' economica dell'impresa | 10 |
| 3 | Referenze su lavori precedenti | 10 |
| 4 | Ribasso percentuale offerto | 50 |
| **TOTALE** | | **100** |

Per i criteri da 1 a 3 il punteggio e' attribuito dalla commissione in base alle informazioni fornite nell'offerta tecnica.

Per il criterio 4, il punteggio e' proporzionale al ribasso offerto.

---

## Dati aggiuntivi disponibili

- Il disciplinare non contiene descrittori per i criteri 1, 2 e 3
- Non e' specificato il metodo di riproporzionamento
- Per il criterio 4 non e' esplicitata la formula matematica
- La gara e' sopra la soglia europea per i lavori (2.100.000 EUR < soglia 5.382.000 EUR per lavori 2024, quindi non e' sopra soglia europea; e' invece nel range 1.000.000-5.382.000 EUR)

## Richiesta del task `check-matrice-criteri`

> "Ho preparato la matrice per la gara lavori. Puoi verificarla prima che pubblichiamo il bando?"
