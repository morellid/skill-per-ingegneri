# Note al caso problematico

## Perche' questo caso e' "problematico"

Il caso mostra i **trabocchetti tipici** che un fabbricante PMI puo' incontrare nell'applicare il CRA:

1. **Tentativo di usare il modulo A senza applicazione integrale delle norme armonizzate per un PDE Classe I** (art. 32 par. 2): e' la trappola piu' frequente, perche' molti fabbricanti consumer presumono che il modulo A sia sempre disponibile come per la direttiva LVD/RED.
2. **Periodo di assistenza inferiore al minimo legale di 5 anni** (art. 13 par. 8): comune per prodotti consumer con cicli di vita brevi.
3. **SBOM in formato non leggibile da macchina**: viola l'obbligo dell'Allegato I parte II punto 1 e Allegato VII punto 8.
4. **Assenza di politica CVD e di canale di contatto dedicato** per le vulnerabilita': violazione esplicita dell'Allegato I parte II punti 5-6.
5. **DoC UE in formato vecchio**: redatta sul modello LVD/RED, non aggiornata ai contenuti minimi dell'Allegato V del CRA.

## Cosa l'agent **deve fare** in un caso problematico

- Etichettare chiaramente come **BLOCKER** le violazioni che impediscono l'immissione sul mercato (categoria modulo, periodo assistenza, DoC UE, SBOM).
- Suggerire le procedure ammesse alternative (B+C, H, certificazione europea), senza scegliere per il fabbricante: la scelta dipende da considerazioni industriali (sistema qualita', dimensione, costi).
- Ricordare i **benefici PMI** dell'art. 32 par. 6 e dell'art. 33 par. 5.
- Citare l'art. 71 par. 2: gli organismi notificati CRA non sono operativi prima dell'11 giugno 2026 - il fabbricante non puo' completare la valutazione prima di questa data, ma puo' avviare il dialogo preliminare.

## Cosa l'agent **non deve fare**

- Non concludere "il prodotto non puo' essere immesso sul mercato": il prodotto **puo'** esserlo dopo aver risolto i BLOCKER. Il giudizio binario "BLOCKER -> non immettere" e' diverso da "il prodotto e' irrimediabilmente non conforme".
- Non scegliere il modulo per il fabbricante (B+C vs H): segnala la matrice di ammissibilita' e i fattori di scelta.
- Non considerare il problema **risolvibile con un solo cambiamento**: il caso richiede un intervento sistemico (cambio modulo + riscrittura documentazione + riprogettazione processi di gestione vulnerabilita' + estensione periodo di assistenza). Va comunicato all'utente come tale.
- Non dichiarare "norma X applicabile": alla data 2026-05-17 non risultano ancora pubblicate in GUUE norme armonizzate per il CRA, e la skill non si pronuncia su prossime pubblicazioni.

## Trappole linguistiche tipiche del fabbricante

Frasi che l'agent **deve riconoscere come bandiere rosse**:

- "Tengo conto delle norme armonizzate" -> non equivale ad "applicazione integrale" (art. 32 par. 2).
- "Ho una SBOM" -> verificare il **formato leggibile da macchina** (PDF non e' sufficiente).
- "Faccio gia' i test di sicurezza" -> verificare che siano **documentati come test reports** dell'Allegato VII punto 6.
- "Diamo aggiornamenti quando servono" -> verificare che la **distribuzione sicura** sia descritta nella documentazione (Allegato I parte II punti 7-8) e che il fabbricante si impegni a fornire aggiornamenti **per il periodo di assistenza**.
