# Task: Check di coerenza tra relazione geologica e relazione geotecnica

## Obiettivo

Verificare che relazione geologica e relazione geotecnica dello stesso
progetto siano coerenti tra loro: il modello geologico deve essere il
riferimento da cui discendono problemi geotecnici, programma delle indagini
e modello geotecnico (NTC par. 6.2.1; Circ. C6 intro e nota 1). Se
disponibile, estendere il controllo alla correlazione con la relazione di
calcolo strutturale (Circ. C10.1).

## Input richiesti

- testo (o estratti significativi) di entrambe le relazioni;
- facoltativo: estratto della relazione di calcolo strutturale (descrizione
  del modello strutturale);
- tipo di opera e fase progettuale.

## Fonti da leggere

- `references/estratti/ntc2018-cap6-relazioni.md` (sezioni "Relazione
  geologica" e "Relazione geotecnica: definizioni e responsabilita'")
- `references/estratti/circ-7-2019-c6-relazioni.md` (sezione
  "Inquadramento")
- `references/estratti/circ-7-2019-c9-c10-ruoli-elaborati.md`

## Checklist di verifica

Per ogni punto: esito "coerente / incoerente / non riscontrabile", con le
evidenze testuali di entrambi i documenti.

1. **Presenza di entrambe le relazioni**: la documentazione comprende sia
   la relazione geologica (redatta da un Geologo) sia la relazione
   geotecnica (redatta dal Progettista)? (Circ. C9.1 lett. g)
2. **Propedeuticita'**: la relazione geotecnica richiama esplicitamente il
   modello geologico come elemento di riferimento per inquadrare i
   problemi geotecnici e per definire il programma delle indagini? (NTC
   par. 6.2.1; Circ. C6 intro)
3. **Coerenza stratigrafica**: le unita' omogenee del modello geotecnico
   sono riconducibili alle formazioni e ai tipi litologici del modello
   geologico? Discrepanze (unita' presenti in un documento e assenti
   nell'altro, spessori o quote incompatibili) sono motivate?
4. **Pericolosita' geologiche**: le pericolosita' individuate dalla
   relazione geologica (frane con stato/tipo di attivita', erosione,
   alluvionamento, effetti di sito sismoindotti: Circ. C6.2.1) trovano
   riscontro nella relazione geotecnica tra pericolosita' ambientale,
   problemi geotecnici e scelte tipologiche (Circ. C6.2.2.5)?
5. **Regime idrico**: lo schema di circolazione idrica superficiale e
   sotterranea (Circ. C6.2.1) e' coerente con il regime delle pressioni
   interstiziali e le quote piezometriche assunti nel modello geotecnico
   (NTC par. 6.2.2)?
6. **Indagini distinte e consequenziali**: il piano delle indagini
   geotecniche e' definito dal progettista (NTC par. 6.2.2) sulla base del
   quadro geologico (Circ. nota 1)? Le indagini geologiche non sono usate
   come surrogato di quelle geotecniche, avendo aree/volumi e finalita'
   diverse (Circ. nota 1)? Eventuali approfondimenti dello studio
   geologico richiesti dal progettista sono documentati (Circ. nota 1)?
7. **Volume significativo**: il volume significativo assunto dalla
   relazione geotecnica e' compatibile con l'assetto geologico descritto
   (profondita' delle unita', discontinuita', falda)?
8. **Correlazione con la relazione di calcolo** (se fornita): il modello
   strutturale e' descritto come correlato con quello geotecnico (Circ.
   C10.1)? I parametri geotecnici usati nel calcolo coincidono con i
   valori caratteristici/di progetto della relazione geotecnica?

## Output

```markdown
# Esito check coerenza geologica/geotecnica - [identificativo progetto]

| # | Aspetto | Riferimento | Esito | Evidenze (geologica vs geotecnica) |
|---|---------|-------------|-------|-------------------------------------|
| 1 | Presenza e ruoli | Circ. C9.1 lett. g | ... | ... |
| ... | ... | ... | ... | ... |

## Incoerenze rilevate
- [aspetto, documenti coinvolti, natura della discrepanza]

## Punti non riscontrabili con gli estratti forniti
- [...]

## Richieste integrative suggerite
- [...]

## Avvertenza
Esito documentale, da sottoporre alla verifica del professionista
firmatario; la valutazione di merito delle scelte geologiche e geotecniche
resta ai rispettivi redattori.
```

## Limiti

- Il confronto e' possibile solo sugli estratti forniti: segnalare sempre
  quali aspetti non sono riscontrabili per mancanza di testo.
- La skill non decide quale dei due documenti sia corretto in caso di
  discrepanza: la segnala e suggerisce la richiesta di allineamento.
- La coerenza numerica dei parametri e' un riscontro di uguaglianza o
  compatibilita' dichiarata, non una rivalidazione dei valori.
