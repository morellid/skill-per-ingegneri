# Output atteso - verifica coerenza rischi-misure

# Verifica coerenza rischi - misure

**Data verifica**: [data]
**POS analizzato**: Rapida Demolizioni Sas - cantiere demolizione condominio
**Contesto cantiere**: demolizione parziale, 30gg, 4 dipendenti

## Sintesi

- Rischi estratti dal POS: 7 (tutti in forma generica, senza magnitudo ne' fase)
- Misure estratte dal POS: 15 (in forma generica, in gran parte non agganciate a rischi specifici)
- Coppie rischio-misura coerenti: 2-3/7 (stima)
- Rischi senza misura chiaramente corrispondente: 4-5
- Misure senza rischio agganciato: 10+ (possibile boilerplate massivo)
- Coppie sospette per inadeguatezza: N/A (misure troppo generiche per valutarle)

**Esito**: INCOERENZE SIGNIFICATIVE

## Problemi strutturali prima del matching

Il POS presenta tre problemi metodologici che ostacolano la verifica:

1. **Rischi dichiarati in forma generica**: "rischio di caduta" senza altezza/fase, "rischio chimico" senza sostanza, "rumore" senza soglia esposizione. Non e' possibile valutare l'adeguatezza delle misure senza conoscere il rischio specifico.

2. **Misure elencate senza riferimento al rischio**: l'elenco numerato 1-15 non associa le misure ai rischi. Non e' chiaro quale misura affronta quale rischio - sembra una lista indipendente.

3. **Rinvio generico al PSC/DVR**: "DPI previsti dal DVR e dal PSC", "misure previste dalla normativa" - formule boilerplate che non costituiscono misure integrative concrete come richiesto dalla lettera g) dell'Allegato XV 3.2.1.

## Matrice rischi-misure (tentativo)

| Rischio (dal POS) | Misure inferibili dal POS | Esito | Note |
|-------------------|---------------------------|-------|------|
| "Rischio di caduta" (generico, senza altezza ne' fase) | "Imbracature di sicurezza per lavori in quota" (8); "rete di protezione" (9) | PARZIALE | Misure collettive e individuali genericamente citate ma senza specifiche di classe/norma EN |
| "Rischio di caduta oggetti dall'alto" | "Rete di protezione" (9, stessa misura sopra?) | GAP | Non sono previsti tettoie, segregazione area sottostante, protezione ingresso condominio |
| "Rischio chimico" | Nessuna misura specifica identificata | GAP | Cantiere di demolizione: rischio chimico plausibile per polveri pregressi, amianto potenziale, solventi. Assenza totale di SDS e misure specifiche |
| "Rumore" | "DPI previsti" (1) - non specificato | GAP | Per demolizioni (attese > 85 dB) servirebbero cuffie con SNR >= 30 dB, rotazione personale, segnaletica specifica. Nessuna di queste misure specifica |
| "Polveri" | "Mascherine" (DPI generico) | GAP | "Mascherine" non qualifica la classe. Per demolizioni servono FFP3 con valvola. Mancano misure di riduzione alla fonte (aspirazione, nebulizzazione) |
| "Rischio elettrico" | "Impianto elettrico a norma" (5) | PARZIALE | L'impianto a norma e' requisito minimo. Manca procedura pre-demolizione tramezzi (rilevamento tensione, disattivazione) |
| "Interferenze" | "Riunioni di coordinamento" (7) | PARZIALE | Riunioni genericamente citate. Mancano: orari con condomini, avvisi preventivi, referente telefonico, segregazione temporale |

## Misure senza rischio associato (boilerplate diffuso)

Le seguenti misure dichiarate nel POS non sono agganciate a un rischio specifico del cantiere e appaiono come elementi da template:

- "Recinzioni di cantiere" (2) - buona pratica ma non agganciata a R specifico
- "Segnaletica di sicurezza" (3) - generica
- "Formati" (4) - affermazione, non misura integrativa
- "Vie di fuga sgombre" (6) - requisito minimo, non integrativa
- "Rispetto cronoprogramma PSC" (12) - delega al PSC
- "Passerelle pedonali" (13) - non chiaro se servono qui
- "Estintori antincendio" (14) - buona pratica, ma rischio incendio non dichiarato
- "Zone di stoccaggio" (15) - non agganciata a rischio

**Stima boilerplate**: 8-10 misure su 15 sembrano boilerplate. Coefficiente boilerplate stimato: 60-70%.

## Incoerenze tecniche

Difficile valutarle per via della genericita'. Casi segnalabili:

| Rischio | Misura dichiarata | Problema | Raccomandazione |
|---------|------------------|----------|-----------------|
| Polveri in demolizione | "Mascherine" | Classe non specificata | Richiede FFP3 per demolizioni con presenza cementizia/polveri fini. Specificare marca/modello |
| Rumore > soglia | "DPI previsti" | DPI generico | Specificare classe SNR, marca, modello. Prevedere rotazione personale |
| Rischio chimico | Nessuna misura | Gap totale | Identificare le sostanze presenti (anche nelle polveri pregresse del tramezzo), allegare SDS, definire DPI chimici specifici |
| Caduta dall'alto | "Imbracature" | Classe non specificata | Specificare cat III EN 361 + cordino con assorbitore EN 355 se lavoro in sospensione; linea vita o ancoraggi se previsti |

## Misure duplicative del PSC

La voce "DPI previsti dal DVR e dal PSC" (1) e "rispetto del cronoprogramma PSC" (12) sono delega, non integrazione. La lettera g) dell'Allegato XV 3.2.1 richiede **misure integrative**, non rinvii.

## Raccomandazioni

Il POS va **riscritto** sulla parte analisi rischi / misure:

1. **Specificare i rischi**: ogni rischio con fase, magnitudo, probabilita'. Esempio: "Caduta dall'alto H=6m durante demolizione copertura piana" invece di "rischio di caduta".

2. **Agganciare ogni misura a un rischio specifico**: strutturare il testo come "relativamente a R1 (caduta dall'alto): misura A, B, C". Eliminare la lista indipendente.

3. **Qualificare tecnicamente le misure**: per ogni DPI, specificare classe, norma EN, marca/modello. Per ogni misura collettiva, specificare dimensioni e conformita'.

4. **Rimuovere il boilerplate**: misure che non corrispondono a rischi specifici vanno rimosse o giustificate. Ad esempio, le "passerelle pedonali" vanno o collegate a un rischio pedonale specifico, o rimosse.

5. **Aggiungere misure mancanti**:
   - Per rischio chimico: identificazione sostanze + SDS + DPI chimici specifici
   - Per rumore demolizioni: cuffie SNR >= 30dB + rotazione + segnaletica
   - Per polveri: aspirazione localizzata + nebulizzazione + FFP3
   - Per elettrocuzione pre-demolizione: procedura rilevamento tensione + disattivazione

6. **Sviluppare coordinamento con condomini**: orari concordati, avvisi preventivi, referente telefonico - non solo "riunioni di coordinamento" generiche.

## Limiti di questa verifica

- La genericita' del POS rende difficile la valutazione di adeguatezza. In pratica, serve la revisione del CSE + richiesta di integrazione al datore di lavoro.
- Non e' stato verificato il PSC - alcune misure apparentemente assenti potrebbero essere nel PSC. Ma la lettera g) richiede comunque misure **integrative** del POS, non delega.
- Non e' possibile valutare se il POS sia "boilerplate copiato da altro cantiere" o "semplicemente redatto male" - l'effetto pratico e' analogo.

## Rinvio al professionista firmatario

**Il CSE (ing. Martini, come dichiarato in altri esempi, o chi di competenza) dovrebbe richiedere una revisione integrale del POS prima dell'inizio lavori. Data la consistenza delle carenze (rischi generici + misure boilerplate), l'inizio lavori con questo POS espone a rischi di non conformita' art. 96 D.Lgs. 81/2008 e sanzioni connesse.**
