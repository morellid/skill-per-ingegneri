# Esempi - transizione-5-0-asseverazione

Casi d'uso illustrativi per la skill di asseverazione tecnica del Piano Transizione 5.0.

| Esempio | Scopo | Esito |
|---|---|---|
| [`conforme-investimento-3-2-mln/`](conforme-investimento-3-2-mln/) | PMI manifatturica meccanica con investimento 3,2 mln EUR (CNC + robot + MES + FV + formazione), processo interessato, riduzione 10,05% sul processo. Mostra l'output atteso di tutti i task (verifica ammissibilita', calcolo riduzione, struttura ex ante). | **Ammissibile, fascia 3** |
| [`non-conforme-cogenerazione-fossili/`](non-conforme-cogenerazione-fossili/) | Industria alimentare con investimento 3,13 mln EUR su cogeneratore a gas naturale + SCADA + FV. Riduzione consumi 8,9% sulla struttura, ma esclusa per DNSH. Mostra come la skill arresta correttamente l'iter al rilevamento della violazione DNSH. | **Non ammissibile (DNSH)** |

## Struttura di ogni esempio

- `input.md`: dati di input (contesto, soggetto, investimenti, perimetro, dati di consumo, certificatore).
- `expected-output.md`: output atteso del task pertinente (verifica ammissibilita', calcolo riduzione, bozza certificazione).
- `note.md`: commenti di dominio, punti critici, riferimenti normativi, validatori.

## Stato di validazione

Entrambi gli esempi sono al **Livello 1** (autore-driven, fonti pubbliche). Per il **Livello 2** servono validatori EGE/ESCo o ingegneri con esperienza diretta in asseverazioni Transizione 5.0 gia' presentate al GSE.
