# Task: Verifica completezza voci Allegato XV

> **Stato**: scaffold. Contenuto normativo da popolare in sessione dedicata con D.Lgs. 81/2008 Allegato XV alla mano.

## Obiettivo

Verificare che il POS fornito dall'utente contenga tutte le voci obbligatorie previste dal punto 3.2 dell'Allegato XV del D.Lgs. 81/2008 (contenuti minimi del POS).

## Input richiesti

- Testo completo del POS (o sezioni rilevanti) in forma leggibile (markdown, testo, estratto PDF)
- Eventuale indicazione della natura del cantiere (edilizia civile, demolizioni, scavi, ecc.) per contestualizzare

## Fonti

Riferimento normativo primario: estratto in `references/estratti/allegato-xv-testo.md` (da preparare).

Punti di riferimento nel testo normativo:
- Punto 3.2.1 lettere a) - l) dell'Allegato XV

## Procedura

**[Da completare con documento Allegato XV alla mano.]**

Struttura attesa della procedura:

1. Per ogni voce obbligatoria definita dal punto 3.2 Allegato XV:
   - Identificare la sezione del POS in cui dovrebbe comparire
   - Verificare la presenza e minima sostanza
   - Classificare: presente / assente / inadeguata

2. Produrre output strutturato:

```markdown
## Verifica completezza POS - Allegato XV

### Voci presenti
- [ ] a) Dati identificativi impresa esecutrice
- [ ] b) Specifiche mansioni svolte in cantiere
- [ ] ...

### Voci assenti
- [ ] Voce X - riferimento normativo
  - Impatto: obbligatorio / raccomandato
  - Dove dovrebbe comparire

### Voci inadeguate
- [ ] Voce Y - presente ma carente
  - Problema specifico
  - Cosa andrebbe integrato
```

## Output atteso

Report markdown strutturato con:
- Esito sintetico (completo / incompleto / con lacune minori)
- Elenco voci con stato per ognuna
- Raccomandazioni specifiche per le voci mancanti o carenti
- **Rinvio obbligatorio**: "La presente verifica non sostituisce la revisione del CSE o del datore di lavoro firmatario del POS."

## Limiti di questo task

- Verifica **formale** sulla presenza delle voci, non sulla loro adeguatezza tecnica rispetto al cantiere specifico
- Non valuta l'effettiva applicabilita' delle misure descritte
- Non sostituisce l'analisi del cantiere fisico

## Placeholder - da completare

Nella sessione di sviluppo dei contenuti:
- [ ] Elenco completo voci obbligatorie 3.2 lettere a) - l)
- [ ] Sinonimi e varianti terminologiche comuni in POS italiani
- [ ] Criteri per distinguere "presente ma inadeguata" da "presente"
- [ ] Esempi di testo tipico per ogni voce (riconoscimento automatico)
- [ ] Gestione di cantieri con particolarita' (es. piccole imprese, subappaltatori)
