# Esempi - modulistica-edilizia-unificata

Esempi sintetici creati per test e validazione della skill. Nomi di immobili, indirizzi, anni, importi e localizzazioni sono fittizi e non riconducibili a interventi reali.

## Casi disponibili

### `manutenzione-frazionamento-cila/`
Inquadramento: manutenzione straordinaria di un appartamento di 92 mq SU in zona B di un Comune toscano, con frazionamento in due UI distinte, **senza opere su parti strutturali**, immobile non vincolato, stato legittimo accertato.
Esito atteso: regime **CILA** (art. 6-bis DPR 380), modulo CILA della modulistica unificata 2025, elenco allegati base + dichiarazione stato legittimo, no notifica preliminare (cantiere mono-impresa stimato sotto soglia D.Lgs. 81).

### `cambio-uso-salva-casa-scia/`
Inquadramento: cambio destinazione d'uso da residenziale (cat. a) a turistico-ricettivo (cat. a-bis - B&B con piu' di 4 camere), unita' di 110 mq SU in zona B, fuori centro storico, **senza opere edilizie**, immobile non vincolato.
Esito atteso: regime **SCIA** post Salva Casa (art. 23-ter + art. 22 DPR 380), modulo SCIA della modulistica unificata 2025, allegati base + dichiarazione di compatibilita' urbanistica + verifica dotazione standard. Avvertenza: oltre alla SCIA edilizia servono SCIA SUAP turismo e codice CIN ai sensi L. 191/2023.

### `sanatoria-semplificata-art36bis/`
Inquadramento: difformita' parziale rispetto a SCIA del 2010 - veranda chiusa di 8 mq aggiunta in autonomia nel 2014 senza titolo, su unita' di 75 mq SU in zona B di un Comune lombardo, immobile non vincolato. L'opera, all'epoca, sarebbe stata assoggettabile a **CILA** (manutenzione straordinaria con opere strutturali leggere).
Esito atteso: applicabilita' **art. 36-bis** Salva Casa (doppia conformita' alleggerita), modulo "Sanatoria semplificata" della modulistica unificata 2025. Verifica conformita' urbanistica oggi (PRG vigente) + edilizia all'epoca (DPR 380 versione 2014). Allegati: relazione tecnica asseverata + documentazione probante 2014 (foto, atti) + sanzione pecuniaria graduata + stato legittimo della parte regolare.

## Convenzione struttura

Ogni caso e' organizzato come:

```
examples/<caso>/
|-- input.md           # dati di input forniti all'agent
|-- expected-output.md # output atteso (determinazione regime + allegati)
`-- note.md            # commenti di dominio sul caso
```
