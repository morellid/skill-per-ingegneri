# Esempi

Casi d'uso per testare e validare la skill. Da preparare in sessione dedicata.

## Strutture attese

### Caso conforme
`conforme-cantiere-piccolo/`
- POS di una piccola impresa per cantiere residenziale
- Output atteso: "Conforme con note minori"

### Caso problematico
`incompleto-voci-mancanti/`
- POS con alcune voci obbligatorie omesse
- Output atteso: "Incompleto, rilevate N lacune"

### Caso borderline (opzionale)
`borderline-costi-a-corpo/`
- POS con costi sicurezza calcolati "a corpo" generico
- Output atteso: "Dubbio, richiede chiarimenti"

## Come preparare un esempio

Ogni esempio ha struttura:
```
examples/<nome-caso>/
├── input.md              # POS semplificato o estratto (anonimizzato)
├── expected-output.md    # cosa la skill dovrebbe produrre
└── note.md               # commenti di dominio, cosa testiamo
```

## Privacy

- Nessun dato reale di imprese o cantieri senza consenso esplicito
- Anonimizzazione completa (nomi imprese, indirizzi, persone fisiche)
- Se un esempio viene da un caso reale: consenso scritto del professionista firmatario
