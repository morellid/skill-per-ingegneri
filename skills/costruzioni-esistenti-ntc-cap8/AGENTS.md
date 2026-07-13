# AGENTS.md - costruzioni-esistenti-ntc-cap8

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Consultazione del **capitolo 8 delle NTC 2018** (costruzioni esistenti) e del
**capitolo C8 della Circolare 7/2019**: classificazione degli interventi
(riparazione/intervento locale, miglioramento, adeguamento), soglie del rapporto
zeta_E, casi di adeguamento obbligatorio, livelli di conoscenza (LC1/LC2/LC3) e
fattori di confidenza (FC), obblighi di valutazione della sicurezza e verifica
del sistema di fondazione. Target: ingegneri strutturisti e collaudatori.

**E' una skill di consultazione della norma, non di calcolo.** Non esegue
verifiche strutturali, non calcola zeta_E, non sceglie ne' dimensiona interventi.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **ntc2018-dm-17-01-2018**: NTC 2018 (hash reale, stesso PDF delle altre skill
  NTC del repo) - trascrizione integrale del cap. 8 (8.1-8.7.5) in
  `references/fonti/ntc2018-dm-17-01-2018.md`
- **circ-7-2019-mit**: Circolare 7/2019 (hash reale) - trascrizione C8.3, C8.4.x,
  C8.5.4.x + Tab. C8.5.IV in `references/fonti/circ-7-2019-mit.md`

Estratto operativo con tabelle: `references/estratti/ntc2018-cap8-costruzioni-esistenti.md`.

## Punti chiave (verificati sul testo)

- **Tre categorie (NTC 8.4)**: riparazione/locale (8.4.1), miglioramento (8.4.2),
  adeguamento (8.4.3). Solo miglioramento e adeguamento -> collaudo statico.
- **Adeguamento obbligatorio (NTC 8.4.3)**: casi a) sopraelevazione, b)
  ampliamento connesso, c) variazione d'uso con incremento carichi verticali in
  fondazione > 10%, d) trasformazione del sistema strutturale (o nuovi elementi
  verticali con >= 50% carichi/piano), e) modifica di classe verso III scolastica
  o IV. Soglie: **a,b,d -> zeta_E >= 1,0; c,e -> zeta_E >= 0,80**.
- **Miglioramento (NTC 8.4.2)**: zeta_E puo' essere < 1; classe III scolastica e
  IV -> **zeta_E >= 0,6**; restanti III e II -> **zeta_E incrementato di >= 0,1**;
  solo sistema di isolamento -> **zeta_E >= 1,0**.
- **zeta_E (Circ. C8.3)**: rapporto azione sismica sopportabile/di progetto;
  parametro di confronto ag*S. **zeta_V,i** per il sovraccarico verticale.
- **LC/FC**: LC1 -> **FC = 1,35**; LC2 -> **FC = 1,20**; LC3 -> **FC = 1,00**
  (Circolare C8.5.4 e Tab. C8.5.IV per c.a./acciaio). I valori FC **non** sono nel
  testo NTC: vengono dalla Circolare.
- **Uso FC (NTC 8.7.2)**: c.a./acciaio -> resistenze medie divise per FC (e per i
  coeff. parziali nei meccanismi fragili); muratura -> valori di tabella
  min/medi/aggiornati per LC (C8.5.4.1); materiali nuovi -> come nuove costruzioni.
- **Valutazione della sicurezza obbligatoria (NTC 8.3)**: elenco delle situazioni;
  esclusa la sola revisione normativa/di zonazione (C8.3).
- **Verifica fondazione obbligatoria (NTC 8.3)**: solo alle condizioni elencate
  (instabilita' globale, dissesti da cedimenti, ribaltamento/scorrimento,
  liquefazione); altrimenti il tecnico esplicita l'assenza in relazione.

## Convenzioni specifiche

### Cosa NON fare
- Non calcolare zeta_E, le capacita' degli elementi ne' eseguire analisi: la
  skill classifica e cita, non verifica.
- Non attribuire alle NTC i valori numerici di FC: citarli sempre come Circolare
  C8.5.4 / Tab. C8.5.IV.
- Non confondere le soglie: casi a/b/d -> 1,0; c/e -> 0,80 (adeguamento);
  miglioramento -> 0,6 / +0,1 secondo classe d'uso.
- Non dichiarare "intervento locale" un intervento senza la condizione della
  Circolare C8.4.1 (nessuna modifica significativa a rigidezza/resistenza/capacita'
  di deformazione): segnalare che la condizione va dimostrata dal progettista.
- Non fornire i valori di tabella dei parametri meccanici della muratura
  (C8.5.I/II/III): fuori ambito.
- Non spacciare la consultazione per valutazione della sicurezza (par. 8.3).

### Cosa fare
- Citare per ogni soglia/definizione il paragrafo preciso (NTC 8.x / Circ. C8.x /
  Tab. C8.5.IV).
- Distinguere sempre prescrizione cogente NTC da chiarimento/valore Circolare.
- Rimandare tra sotto-attivita' quando la domanda cambia natura.
- Chiudere con il rinvio alla valutazione della sicurezza e al progettista.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con ingegnere strutturista,
  confronto con casistica applicativa e con eventuali linee guida CSLLPP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #21)
- Task files: 3 (`classifica-intervento.md`, `determina-lc-fc.md`, `qa-cap8.md`)
- Esempi: 2 (cambio d'uso verso scuola -> adeguamento zeta_E >= 0,80 + LC1/FC 1,35;
  apertura vano -> intervento locale, no collaudo statico)
