# Task: Verifica coerenza rischi - misure

> **Stato**: scaffold. Contenuto normativo e metodologico da popolare in sessione dedicata.

## Obiettivo

Verificare che per ogni rischio identificato nel POS sia prevista almeno una misura di prevenzione/protezione coerente, e viceversa che ogni misura faccia riferimento a un rischio concreto.

## Input richiesti

- Sezione del POS relativa all'analisi dei rischi specifici
- Sezione del POS relativa alle misure di prevenzione e protezione
- Eventualmente: DPI elencati e procedure operative

## Fonti

Riferimento normativo primario:
- Allegato XV punto 3.2.1 lettere d), f) (analisi rischi e misure)
- D.Lgs. 81/2008 Titolo IV Capo II (cantieri temporanei o mobili)
- Linee guida INAIL su analisi rischi cantiere (se embedabili)

## Procedura

**[Da completare con criteri metodologici validati da un CSE di dominio.]**

Struttura attesa:

1. Estrazione dei rischi dichiarati nel POS (parole chiave, tabelle)
2. Estrazione delle misure dichiarate
3. Matrice di matching rischio → misura(e)
4. Identificazione:
   - Rischi senza misure corrispondenti (grave)
   - Misure senza rischi chiari (sospetta boilerplate)
   - Coppie incoerenti (misura inadeguata al rischio)
5. Valutazione qualitativa della coerenza (con limite dichiarato)

## Output atteso

```markdown
## Verifica coerenza rischi - misure

### Sintesi
- Rischi dichiarati: N
- Misure dichiarate: M
- Matching completo: % rischi con misura

### Rischi senza misure identificate
- Rischio X (pag. Y del POS)
  - Misura attesa (tipologia)
  - Rinvio al redattore

### Misure senza rischio chiaro
- Misura Z (pag. W)
  - Possibile boilerplate copia-incolla
  - Verificare se applicabile al cantiere

### Coppie sospette
- Rischio A + Misura B
  - Problema di coerenza

### Raccomandazioni
- ...

Rinvio obbligatorio: "La valutazione di adeguatezza tecnica delle misure rispetto al cantiere specifico spetta al CSE e al datore di lavoro."
```

## Limiti di questo task

- Non valuta l'**efficacia** delle misure, solo la loro presenza e plausibile coerenza
- Non tiene conto di specificita' del cantiere reale (solo documento)
- Metodologia basata su keyword matching e analisi semantica - non sostituisce revisione esperta

## Placeholder - da completare

- [ ] Tassonomia standard dei rischi cantiere (fall, elettrici, chimici, movimentazione, ecc.)
- [ ] Tabelle di corrispondenza tipiche rischio → misure attese
- [ ] Pattern di riconoscimento per rischi e misure in POS italiani
- [ ] Criteri per distinguere coerenza "accettabile" da "sospetta"
- [ ] Validazione da CSE con POS reali
