# Note di dominio - caso `incompleto-voci-mancanti`

## Cosa stiamo testando

Che la skill riconosca come **incompleto/non conforme** un POS con carenze sostanziali tipiche dei "POS boilerplate" poco curati, senza falsi negativi (cioe' senza classificare come conforme qualcosa che non lo e').

## Carenze deliberate inserite nel POS

### Assenze totali
1. **Addetto antincendio ed evacuazione** - voce a.3 parzialmente: presenti solo PS e RLS
2. **Medico competente** - voce a.4: assente (e' quasi certamente obbligatorio per lavoratori edili)
3. **Direttore tecnico di cantiere** - voce a.6: presente solo il capocantiere
4. **Mansioni specifiche di sicurezza** - voce b: non descritte per ruolo
5. **Valutazione rumore** - voce f: zero menzione

### Presenze inadeguate (formule generiche)
6. **Descrizione attivita'** - voce c: fasi elencate ma senza durata/orari/turni
7. **Attrezzature** - voce d: citate genericamente, no marche/modelli/Pi.M.U.S.
8. **SDS sostanze** - voce e: sostanze elencate, SDS non allegate
9. **Misure integrative** - voce g: dichiarazione generica "come da PSC", solo 2 rischi citati
10. **DPI** - voce i: "DPI previsti dalla normativa (elmetti, scarpe, guanti, ecc.)"
11. **Formazione** - voce l: "formazione prevista dalla legge" senza specifiche

### Presenze adeguate (controllo che non generiamo falsi positivi)
- Dati impresa essenziali (ragione sociale, indirizzo, P.IVA)
- RSPP (DdL)
- Numero lavoratori con qualifiche
- RLS nominato

## Output atteso

`INCOMPLETO - NON CONFORME` con:
- 2/10 voci complete
- 5/10 voci inadeguate
- 3/10 voci assenti
- Sanzione art. 159 co. 1 formalmente applicabile

Almeno 11 problemi rilevati in tabella riassuntiva, distribuiti tra priorita' Alta (6-7) e Media (3-4).

## Cose che il modello DEVE catturare

- **Assenza medico competente** come problema sostanziale per cantiere edile, non solo formale. Il POS qui sembra per impresa piccola ma i rischi edili (movimentazione, rumore, polveri, vibrazioni, sostanze) sono multipli - medico competente e' praticamente obbligatorio.
- **Formule boilerplate**: "DPI previsti dalla normativa" e "formazione prevista dalla legge" sono classici del POS mal fatto. Il modello deve riconoscerli come **inadeguati** anche se formalmente la voce e' "presente".
- **Sostanze senza SDS**: citare "cemento, malta, calce, vernici" senza SDS e' violazione diretta della lettera e).
- **Mancanza Pi.M.U.S.**: il POS cita un ponteggio metallico per fabbricato intero senza riferimento al Piano di Montaggio, Uso e Smontaggio (obbligatorio ex art. 136).
- **Valutazione rumore assente**: nessuna menzione, ne' rinvio al DVR. Carenza totale.

## Cose che il modello NON deve fare

- **Dichiarare conforme** un POS cosi' carente. Il POS ha SOLO 2 voci complete su 10 - e' un caso flagrante di non-conformita'.
- **Attribuire responsabilita'** oltre il documento: puo' segnalare le carenze, ma la decisione finale su proseguire/sospendere i lavori e' del CSE.
- **Essere eccessivamente generoso**: "la dichiarazione generica di formazione potrebbe essere sufficiente se supportata da attestati" - no. Se gli attestati non sono citati ne' allegati, la voce e' inadeguata.

## Ambiguita' da gestire

- **Voce h (procedure complementari PSC)**: non e' verificabile senza accesso al PSC. Modello deve esplicitarlo, non inventare.
- **Obbligatorieta' medico competente**: dipende da esposizione specifica. La skill non puo' decidere, ma deve segnalare "molto probabilmente obbligatorio" data l'attivita'.
- **Sotto-appaltatori**: il POS non menziona lavoratori autonomi subaffidatari. Se assenti, OK. Se presenti e non menzionati, carenza. Modello deve chiedere o segnalare l'ambiguita'.

## Cosa imparare da questo caso

- I POS veri spesso hanno carenze esattamente di questo tipo: boilerplate su voci complesse (DPI, formazione), assenze silenziose (medico competente), rinvii generici al PSC.
- La skill aggiunge valore **soprattutto** su questi casi - un POS veramente ben fatto verrebbe riconosciuto come tale anche senza la skill.
- Il giudizio severo ("INCOMPLETO - NON CONFORME") e' giustificato: la lista di problemi e' lunga e include voci sostanziali (medico, rumore, DPI, formazione).

## Fonte della struttura

POS fittizio creato ad hoc per test. Struttura realistica, simula errori comuni nei "POS fatti in fretta". Nessun riferimento a imprese, persone o indirizzi reali.
