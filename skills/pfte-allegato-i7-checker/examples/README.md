# Esempi - pfte-allegato-i7-checker

Esempi sintetici creati per test e validazione della skill. Nomi di amministrazioni, opere, importi e localizzazioni sono fittizi e non riconducibili a interventi reali.

## Casi disponibili

### `conforme-nuova-costruzione/`
Inquadramento: nuova costruzione di scuola primaria comunale, importo 4,5 mln EUR, espropri necessari, in verifica di assoggettabilita' VIA con esito "no VIA", BIM applicabile, modalita' di affidamento ad appalto integrato.
Esito atteso: checklist completa generata + esito di completezza COMPLETO CON RISERVA (schema di contratto da-verificare).

### `manutenzione-straordinaria-incompleto/`
Inquadramento: manutenzione straordinaria su edificio scolastico esistente, importo 380.000 EUR, no espropri, no VIA, no BIM, regime art. 41 co. 5-bis (correttivo 2024 - PFTE base di affidamento senza esecutivo).
Esito atteso: rilevamento di elaborati mancanti rispetto alla checklist ridotta per manutenzione.

## Convenzione struttura

Ogni caso e' organizzato come:

```
examples/<caso>/
|-- input.md           # dati di input forniti all'agent
|-- expected-output.md # output atteso (checklist o report)
`-- note.md            # commenti di dominio sul caso
```
