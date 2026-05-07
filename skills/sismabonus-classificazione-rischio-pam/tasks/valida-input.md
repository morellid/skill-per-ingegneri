# Task: validazione input edificio

## Obiettivo

Verificare che i valori TR_C, PGA_C e PGA_D forniti dall'utente per l'edificio siano fisicamente coerenti e adatti al calcolo PAM/IS-V ai sensi del DM 58/2017 Allegato A. Segnalare anomalie PRIMA di eseguire `calcola-classificazione.md`.

## Input richiesti

Stessi del task `calcola-classificazione.md`: per ciascuno stato (fatto / progetto) e per ciascuno dei 4 SL NTC, TR_C, PGA_C e PGA_D.

## Fonti

- `../references/estratti/dm-58-2017-allegato-a-formula-pam.md` - punto 2.1 sull'ordinamento naturale dei SL e sulla Curva di Individuazione

## Procedura

### Check 1 - tipi e segno (delegato al modulo)

Tutti i valori di TR_C e PGA devono essere:
- numeri reali finiti (no NaN, no Infinity, no stringhe, no boolean)
- TR_C, PGA_C, PGA_D > 0

Il modulo Python `sismabonus.py` rifiuta automaticamente input non validi e ritorna codice di uscita 2 con messaggio su stderr. Se l'utente fornisce input via JSON, il modulo segnala la chiave problematica.

### Check 2 - monotonia di lambda (atteso fisico)

In condizioni "ben condizionate", al crescere della severita' del SL il TR_C deve aumentare (lambda diminuisce):

  TR_C(SLO) <= TR_C(SLD) <= TR_C(SLV) <= TR_C(SLC)

equivalentemente:

  lambda(SLID) >= lambda(SLO) >= lambda(SLD) >= lambda(SLV) >= lambda(SLC)

Se non e' rispettato, il modulo segnala `monotona: false` ma calcola comunque. Il professionista deve verificare:
- errore di analisi (LC sbagliato, FC sbagliato, modello incoerente);
- edificio realmente non duttile, dove SLD e' raggiunto a livelli di azione piu' bassi di SLO (raro ma fisicamente possibile per costruzioni esistenti molto rigide e fragili);
- necessita' di "capping" coerente con DM 58/2017 Allegato A (cap. 2.1) - es. porre TR_C(SLO) = TR_C(SLD) se SLO uscirebbe dal modello con TR maggiore. La regola di capping NON e' applicata automaticamente dalla skill: e' responsabilita' del progettista.

### Check 3 - ordine di grandezza (sanity)

Per edifici esistenti tipici:
- TR_C(SLO): 5-200 anni
- TR_C(SLD): 10-500 anni
- TR_C(SLV): 30-2000 anni
- TR_C(SLC): 50-5000 anni
- PGA_C: 0.01 - 1.0 g (al di fuori segnala possibile errore)
- PGA_D: 0.02 - 0.5 g per zone sismiche italiane

Valori molto fuori range sono possibili (es. siti a pericolosita' molto bassa, edifici nuovi assimilati) ma vanno verificati con l'utente.

### Check 4 - coerenza PGA_C / TR_C

Esiste una relazione monotona tra PGA_C e TR_C tramite lo spettro di pericolosita' al sito (PGA_C(SL) corrisponde a un certo TR_C nel reticolo INGV). Se i due trend non sono coerenti (es. PGA_C piu' alta a TR_C piu' basso, monotonia inversa rispetto a quanto atteso), segnalare al progettista.

Questa skill NON ricalcola TR_C da PGA_C: e' un check qualitativo, basato sul fatto che entrambi sono output dell'analisi e devono essere coerenti tra loro.

### Check 5 - PGA_D positiva e crescente con severita' SL

PGA_D e' la PGA al sito alla domanda di ciascun SL. Per il sito (NTC 2018 par. 3.2 + Allegato A) deve risultare:

  PGA_D(SLO) <= PGA_D(SLD) <= PGA_D(SLV) <= PGA_D(SLC)

(eventi piu' rari hanno PGA piu' alta). Se non e' rispettato, c'e' verosimilmente un errore di trascrizione.

### Check 6 - PGA_D di fatto = PGA_D di progetto

PGA_D dipende dal SITO, non dall'edificio. Non puo' cambiare tra stato di fatto e stato di progetto a meno che l'intervento non comporti spostamento del fabbricato (caso limite). Segnalare se l'utente fornisce PGA_D diverse tra fatto e progetto.

## Output atteso

Un report di validazione con:
- check 1-6 con esito PASS / WARN / FAIL
- per ogni WARN/FAIL: descrizione dell'anomalia, riferimento al DM 58/2017 / NTC 2018, raccomandazione (verifica analisi, capping, ricontrollo trascrizione)
- decisione: "input pronti per calcolo" oppure "rivedere input prima del calcolo"

Se tutti PASS, suggerire all'utente di proseguire con il task `calcola-classificazione.md`.
