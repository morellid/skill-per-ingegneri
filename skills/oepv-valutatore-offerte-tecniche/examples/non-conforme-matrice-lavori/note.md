# Note - esempio non conforme matrice OEPV lavori

## Perche' questo esempio e' importante

Mostra il task `check-matrice-criteri` su una matrice prodotta da un RUP senza specifica formazione in OEPV. Contiene gli errori piu' frequenti nelle gare OEPV dei committenti pubblici di medie dimensioni (ASL, Comuni, enti locali), tutti ricorrenti nei ricorsi TAR:

1. **Criteri soggettivi all'impresa invece che sull'offerta**: solidita' economica e referenze sono i requisiti di partecipazione mascherati da criteri OEPV - errore comune, illegittimo per costante giurisprudenza
2. **Criterio discrezionale senza descrittori**: "qualita' dell'offerta tecnica" senza sub-elementi e' la fonte principale di contenziosi TAR su OEPV
3. **Formula economica assente**: "proporzionale al ribasso" non e' una formula - errore che rende la gara non trasparente
4. **Bonus parita' di genere dimenticato**: l'obbligo e' perentorio ("sempre previsto") ma spesso ignorato dai RUP

## Aspetti degni di nota

- **Il punteggio economico al 50% e' problematico anche senza il limite esplicito**: per appalti di lavori non banali, un punteggio economico del 50% svilisce fortemente la componente qualitativa e segnala alla SA che privilegia il risparmio su qualita' e sicurezza. La prassi prudente e' max 30-40% per lavori complessi.
- **Il limite del 30% per alta intensita' di manodopera**: in un appalto di costruzione con finiture e impianti, il costo della manodopera supera spesso il 50% del totale. Il RUP deve fare questa verifica esplicitamente; se il limite scatta, il 50% economico viola l'art. 108 co. 4.
- **L'Allegato II.4 come pre-requisito**: la verifica della qualificazione della SA (Allegato II.4 D.Lgs. 36/2023) e' un pre-requisito procedurale prima ancora della matrice OEPV. La skill lo menziona in nota finale.

## Limitazioni note dell'esempio

- La soglia "alta intensita' di manodopera" (>= 50% costo lavoro su importo totale) richiede un'analisi della composizione del costo specifica per ogni contratto - la skill non la calcola ma segnala il rischio
- La giurisprudenza citata (Cons. Stato, TAR) e' indicativa della tendenza consolidata; sentenze successive possono aver precisato o modificato alcuni principi
- L'esempio non include il calcolo dei punteggi con offerte concrete (quello e' il task `valuta-offerta-tecnica`)
