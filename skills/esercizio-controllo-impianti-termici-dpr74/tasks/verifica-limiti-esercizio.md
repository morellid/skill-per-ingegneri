# Task: verifica-limiti-esercizio

Verifica i **valori massimi di temperatura** e i **limiti di esercizio** di un impianto termico
per la climatizzazione, ai sensi del **D.P.R. 74/2013** (artt. 3-5).

## Input richiesti

- **Destinazione** dell'edificio (industriale/artigianale vs altri).
- **Zona climatica** del Comune (A-F) e stagione (invernale/estiva).
- Eventuali **ordinanze comunali** vigenti sui limiti di esercizio.

## Procedura

1. **Temperatura massima** (art. 3):
   - invernale: **18 C + 2 C** (industriale/artigianale) o **20 C + 2 C** (altri edifici);
   - estiva: non inferiore a **26 C - 2 C**.
2. **Periodo e orario di esercizio invernale** per zona climatica (art. 4):
   - A: 6 h/g (1 dic - 15 mar); B: 8 h/g (1 dic - 31 mar); C: 10 h/g (15 nov - 31 mar);
     D: 12 h/g (1 nov - 15 apr); E: 14 h/g (15 ott - 15 apr); F: nessuna limitazione.
   - Fuori periodo: attivazione **solo** se le condizioni climatiche la giustificano.
3. **Deroghe comunali** (art. 5): verificare **ordinanze del sindaco** che ampliano/riducono
   periodi, orari o temperature (es. per emergenze o qualita' dell'aria).

## Output atteso

- Prospetto: temperatura massima ammessa (con tolleranza), periodo e ore giornaliere di
  esercizio per la zona climatica, ed eventuali deroghe comunali applicabili.

## Avvertenze

- I limiti sono **minimi di legge**: la disciplina **regionale/comunale** puo' essere piu'
  restrittiva - verificarla.
- La skill inquadra i limiti; la conduzione e' del responsabile dell'impianto/terzo responsabile.
