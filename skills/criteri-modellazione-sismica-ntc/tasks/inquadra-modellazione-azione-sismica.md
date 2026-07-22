# Task: inquadra-modellazione-azione-sismica

Inquadra i **criteri di modellazione dell'azione sismica** secondo le **NTC 2018 par. 7.2.6**, con particolare
riguardo all'**eccentricità accidentale** e ai limiti per la risposta sismica locale / interazione
terreno-struttura. Supporto documentale: **non** esegue l'analisi.

## Quando usarla

Il progettista deve impostare la rappresentazione dell'azione sismica (spettri/storie temporali), l'eccentricità
accidentale e i limiti dell'interazione terreno-struttura. Per la modellazione della struttura (rigidezze,
orizzontamenti) usa `inquadra-modellazione-struttura`.

## Passi

1. **Rappresentazione dell'azione** (§7.2.6): l'azione sismica puo' essere modellata con **forze statiche
   equivalenti**, **spettri di risposta** o **storie temporali** del moto del terreno opportunamente selezionate.
2. **Risposta sismica locale (RSL) e interazione terreno-struttura (ITS)** (§7.2.6): la domanda puo' considerare
   l'interazione terreno-struttura (inerziale e cinematica) e la RSL, con metodi di comprovata validità; valgono
   le limitazioni:
   - lo **spettro di risposta elastico** (con **5% di smorzamento**) ottenuto da RSL/ITS deve essere **almeno pari
     al 70%** di quello per **sottosuolo di tipo A** (§3.2.3.2);
   - la **risultante di taglio e sforzo normale** trasmessa all'estradosso della fondazione deve essere **almeno
     pari al 70%** di quella ottenuta con lo stesso modello a **vincoli fissi** e input per sottosuolo A;
   - **non e' ammesso** l'uso di **storie temporali artificiali** (o con componenti artificiali) per le analisi di
     RSL e per le ITS con legami costitutivi isteretici del sottosuolo (§3.2.3.6).
3. **Eccentricità accidentale** (§7.2.6): per tenere conto della **variabilità spaziale del moto** e di eventuali
   incertezze, si attribuisce al **centro di massa** un'eccentricità accidentale rispetto alla posizione di
   calcolo. Per i **soli edifici** e in assenza di determinazioni piu' accurate:
   - **e_a >= 0,05 volte la dimensione media** dell'edificio misurata **perpendicolarmente** alla direzione di
     applicazione dell'azione sismica;
   - l'eccentricità e' **assunta costante**, per entita' e direzione, su **tutti gli orizzontamenti**.

Usa la checklist in `../references/estratti/modellazione-checklist.md` (sezione 2).

## Output atteso

Un inquadramento che indichi: le modalità di rappresentazione dell'azione, i limiti del 70% per RSL/ITS (spettro
e reazioni alla fondazione) con il 5% di smorzamento, e il calcolo dell'eccentricità accidentale (>= 0,05 x
dimensione media perpendicolare, costante su tutti i piani), con **rinvio al paragrafo** NTC. Nessuna analisi.

## Cosa NON fare

- Non eseguire l'analisi ne' la risposta sismica locale (§3.2.3.6); non determinare q.
- Non trattare la modellazione della **struttura** (usa l'altro task) ne' le **fondazioni miste** (§6.4.3).
