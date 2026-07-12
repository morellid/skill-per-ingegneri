# Task: Verifica documentale di una stima dei cedimenti

## Obiettivo

Controllare se la relazione o nota di calcolo esplicita gli elementi richiesti dal quadro NTC/Circolare per una verifica SLE dei cedimenti.

## Input richiesti

- estratto della relazione geotecnica o nota di calcolo
- metodo usato dal progettista per stimare il cedimento
- valore di cedimento/spostamento risultante
- limite di accettabilita' adottato nel progetto, se presente

## Fonti da leggere

- `references/estratti/ntc2018-par-6-2.md`
- `references/estratti/circ-7-2019-c-6-2.md`

## Checklist di verifica

1. Il report dichiara quali prestazioni attese deve garantire l'opera?
2. Il report dichiara un valore limite di spostamento/cedimento compatibile?
3. Il metodo di interazione terreno-struttura e' descritto?
4. E' chiaro se il controllo riguarda il termine della costruzione e/o l'andamento nel tempo?
5. Sono esplicitati i dati principali usati dal progettista (azioni, parametri geotecnici, combinazioni)?
6. Il risultato finale e' confrontato con un limite dichiarato?

## Output

```markdown
# Esito verifica documentale cedimenti
- Prestazioni attese: presenti / mancanti
- Limite di cedimento o spostamento: presente / mancante
- Metodo di analisi terreno-struttura: presente / mancante
- Andamento nel tempo: trattato / non trattato
- Confronto SLE finale: chiaro / non chiaro
- Richieste integrative al progettista: [...]
```

## Regola importante

Se l'utente chiede di "calcolare" il cedimento di consolidazione primaria, usa il task [`calcola-cedimento-edometrico.md`](calcola-cedimento-edometrico.md): il calcolo e' implementato con le equazioni del FHWA NHI-06-088 par. 7.5.2, fonte pubblica trascritta in `references/fonti/fhwa-nhi-06-088.md` e citata come "altro codice internazionale" ai sensi del cap. 12 NTC 2018. Formule diverse da quelle trascritte restano fuori ambito.