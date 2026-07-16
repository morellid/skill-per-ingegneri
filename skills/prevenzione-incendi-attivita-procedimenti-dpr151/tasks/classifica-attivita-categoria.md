# Task: classifica-attivita-categoria

Verifica se un'attivita' e' **soggetta ai controlli di prevenzione incendi** e in quale
**categoria (A, B, C)**, secondo il **D.P.R. 151/2011** (art. 2 e Allegato I).

## Input richiesti

- **Descrizione dell'attivita'** (tipo, settore, sostanze/impianti, dimensioni/soglie
  rilevanti: es. potenzialita', superfici, numero di presenze, quantitativi).

## Procedura

1. **Cerca l'attivita' nell'Allegato I**: se non e' elencata (e non ha specifiche regole
   tecniche di prevenzione incendi) -> **non soggetta** al procedimento del D.P.R. 151/2011.
2. **Individua la categoria** sulla riga dell'attivita' (colonne **A / B / C**): la categoria
   dipende da dimensione, settore, presenza di regole tecniche ed esigenze di pubblica
   incolumita'. Molte attivita' compaiono in **piu' categorie** in base alle soglie.
   **La categoria esatta va letta sulla tabella dell'Allegato I** (la resa testuale non
   conserva l'allineamento delle colonne).
3. **Deduci i procedimenti** conseguenti:
   - **A**: nessuna valutazione del progetto; **SCIA** + eventuali controlli (art. 4);
   - **B**: **valutazione del progetto** (art. 3) + **SCIA** + controlli (art. 4);
   - **C**: **valutazione del progetto** (art. 3) + **SCIA** + visite tecniche + **CPI**
     (certificato di prevenzione incendi) (art. 4).

## Output atteso

- Esito: attivita' **soggetta/non soggetta**; se soggetta, la **categoria** (con il numero
  della voce dell'Allegato I) e l'elenco dei **procedimenti** applicabili.

## Avvertenze

- La **categoria esatta** va **letta sull'Allegato I** dell'atto: la skill non riproduce la
  classificazione puntuale.
- Un'attivita' puo' ricadere in **piu' numeri** dell'Allegato I: valutarli tutti.
