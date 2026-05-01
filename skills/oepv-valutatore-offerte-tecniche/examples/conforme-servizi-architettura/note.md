# Note - esempio conforme OEPV servizi architettura/ingegneria

## Perche' questo esempio e' importante

Dimostra il flusso del task `costruisci-matrice-criteri` per il caso piu' frequente di OEPV obbligatorio: servizi di architettura e ingegneria >= 140.000 EUR (art. 108 co. 2 lett. b D.Lgs. 36/2023). E' il tipo di gara piu' comune per RUP di enti locali che affidano progettazioni di opere pubbliche.

## Aspetti degni di nota

- **OEPV obbligatorio a 185.000 EUR**: la soglia di 140.000 EUR per i servizi tecnici e' fissa nell'art. 108 co. 2 lett. b, non indicizzata. Qualsiasi servizio di architettura/ingegneria sopra questa soglia richiede OEPV qualita'/prezzo, senza eccezioni.
- **Bonus parita' di genere come sottocriterio dedicato**: l'art. 108 co. 7 richiede di assegnare "il maggiore punteggio possibile" alle imprese con certificazione parita' di genere. Nella matrice e' un sottocriterio B3 da 5 punti, che equivale al punteggio massimo di un singolo sottocriterio. Questo e' il modo corretto di adempiere all'obbligo.
- **Criterio A3 a formula (tempi PFTE)**: per le SA con urgenza sulla progettazione, valorizzare la riduzione dei tempi e' legittimo e frequente. La formula decrescente V = T_min/T_i e' proporzionale e difendibile in sede di ricorso.
- **Descrittori obbligatori per criteri discrezionali**: i descrittori per A1 e A2 non sono opzionali - sono essenziali per la legittimita' della valutazione discrezionale. Una matrice che nomina solo il criterio senza descrittori e' ad alto rischio TAR.
- **30 punti economici per servizi tecnici**: la scelta di 30/100 e' una prassi consolidata per i servizi professionali tecnici. Con valori piu' bassi (es. 20 punti economici) si rischia di attirare offerte tecnicamente ottime ma economicamente insostenibili; con valori piu' alti (es. 40-50) si svilisce la componente qualitativa con rischio TAR.

## Nota sulla qualificazione della SA (Allegato II.4)

Il sistema di qualificazione delle stazioni appaltanti previsto dall'Allegato II.4 D.Lgs. 36/2023 (citato nell'issue #5 come fonte della skill - erroneamente - ma che e' reale e rilevante) stabilisce livelli di qualificazione per le SA. Un Comune piccolo potrebbe non avere la qualificazione per gestire autonomamente procedure sopra certe soglie e dover ricorrere a centrali di committenza (es. CONSIP, UREGA, ASMEL). Questa verifica e' fuori scope della skill ma dovrebbe essere segnalata al RUP nella nota finale.

## Limitazioni note dell'esempio

- I dati tecnici (numero contratti analoghi, soglie anni esperienza) sono plausibili ma devono essere calibrati sull'oggetto specifico
- Il tempo base contrattuale per A3 (60 giorni) e' indicativo: il RUP deve calcolarlo sulla base del DIP e della complessita' dell'opera
- I compensi professionali base di calcolo devono essere verificati con il DM tariffe (Allegato I.13 D.Lgs. 36/2023) per verificare che la base d'asta sia congrua
