# Note di dominio - caso `coerenza-incoerente-boilerplate`

## Cosa stiamo testando

Che la skill rilevi le tre patologie tipiche del POS boilerplate:
1. Rischi dichiarati in forma generica (senza magnitudo, fase, specificita')
2. Misure elencate senza riferimento al rischio
3. Rinvii generici a PSC/DVR invece di misure integrative concrete

## Scelte progettuali del caso

- **Stesso tipo di cantiere del caso "coerenza-buona"**: demolizione parziale condominio. Questo permette un confronto diretto tra POS ben fatto e POS boilerplate sullo stesso scenario.
- **Rischi appiattiti a parole chiave**: "rischio di caduta", "rumore", "polveri" senza contesto. Tipico dei template scaricati da internet.
- **Misure in lista numerata indipendente**: 15 misure elencate in sequenza, senza match con i rischi. La struttura stessa del testo segnala il problema.
- **Rinvio al PSC/DVR come surrogato**: "DPI previsti dal DVR", "rispetto cronoprogramma PSC" - comune escamotage per apparire conformi senza scrivere misure reali.
- **DPI elencati genericamente**: "elmetto, scarpe, guanti, occhiali, mascherine" senza classi ne' norme. Test classico di boilerplate.

## Output atteso

`INCOERENZE SIGNIFICATIVE` con:
- 4-5 rischi senza misura chiaramente corrispondente
- 10+ misure senza rischio agganciato (boilerplate massivo)
- Coefficiente boilerplate stimato: 60-70%
- Raccomandazione di **riscrittura integrale** della sezione rischi/misure

## Cose che la skill DEVE catturare

- **Genericita' dei rischi**: "rumore" senza soglia non e' valutabile.
- **Disaccoppiamento tra lista rischi e lista misure**: il POS non dice quale misura e' per quale rischio. La skill deve riconoscere questa struttura come problematica e fare il matching IPOTETICO (con caveat).
- **"Mascherine" vs FFP3**: ogni volta che un POS dice "mascherine" per polveri di demolizione, la skill deve flaggare la sotto-specificazione.
- **"Imbracature" senza classe**: stesso pattern per DPI anticaduta.
- **"DPI previsti dal DVR/PSC"**: non e' misura, e' delega. Va flaggato.
- **Misure che sembrano elementi di cantiere standard** (recinzione, segnaletica, vie di fuga) ma non agganciate a rischi specifici: sono requisiti minimi, non misure integrative.

## Cose che la skill NON deve fare

- **Trattare la lista numerata come "coerente perche' ordinata"**: l'ordine non implica coerenza.
- **Essere troppo indulgente su "rischio chimico"**: per demolizione anni '60/'70 non e' implausibile che ci siano amianto, vernici al piombo, fibre pericolose. Assenza totale di misure va flaggata.
- **Considerare "formazione generica" come misura adeguata**: "i lavoratori sono formati" non e' misura, e' premessa.

## Ambiguita' da gestire

- **Boilerplate vs requisiti minimi**: recinzioni, segnaletica, vie di fuga, estintori sono requisiti minimi di cantiere. Non sono "integrative". La skill puo' segnalarli come "OK come requisito minimo ma non soddisfano la richiesta di misure integrative art. g)".
- **"Passerelle pedonali"**: potrebbero essere giustificate se il cantiere ha accessi che attraversano aree non sicure. Senza contesto, la skill segnala "misura senza rischio agganciato" ma lascia l'interpretazione al CSE.

## Cosa imparare

- POS boilerplate sono la maggioranza dei POS in circolazione (stima di mercato, non verificata). La skill deve essere calibrata per questa realta'.
- Il valore aggiunto della skill sta nel segnalare sistematicamente il boilerplate: un occhio umano puo' skip-ignorare 15 misure generiche, la skill le vede una per una.
- Un POS con 15 misure ma 0-2 coppie coerenti e' peggio di un POS con 5 misure tutte agganciate a rischi specifici.

## Fonte della struttura

POS fittizio, ispirato a pattern tipici di POS boilerplate osservabili nei template online. Nessun riferimento a imprese reali.
