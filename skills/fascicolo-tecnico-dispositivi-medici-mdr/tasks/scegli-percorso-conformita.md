# Task: scegli-percorso-conformita

Data la classe del dispositivo (I, Is/Im/Ir, IIa), individua il percorso di
valutazione della conformita' ai sensi dell'art. 52 MDR e il ruolo dell'organismo
notificato. Supporto documentale.

## Input

- Classe del dispositivo (input): **I** (base), **Is** (sterile), **Im** (funzione
  di misura), **Ir** (strumenti chirurgici riutilizzabili) o **IIa**.

## Procedura

1. **Classe I (base)** - art. 52 §7: **autodichiarazione**. Il fabbricante redige
   la **documentazione tecnica** (allegati II e III) e la **dichiarazione di
   conformita' UE** (art. 19). **Nessun organismo notificato**. Appone la marcatura
   CE.
2. **Classe I sterile / con funzione di misura / strumenti chirurgici
   riutilizzabili (Is/Im/Ir)** - art. 52 §7: oltre alla documentazione tecnica,
   procedure dell'allegato IX (capi I e III) o dell'allegato XI, parte A, ma
   l'**intervento dell'organismo notificato e' limitato**:
   - **Is**: agli aspetti dello **stato sterile**;
   - **Im**: ai **requisiti metrologici**;
   - **Ir**: agli aspetti del **riutilizzo** (pulizia, disinfezione,
     sterilizzazione, manutenzione, test funzionale, istruzioni per l'uso).
3. **Classe IIa** - art. 52 §6: **allegato IX** (capi I e III, con valutazione della
   documentazione tecnica di almeno un dispositivo rappresentativo per categoria)
   **oppure** documentazione tecnica (allegati II e III) + **allegato XI, punto 10 o
   18**. **Con organismo notificato**.
4. **Marcatura CE**: quando interviene l'organismo notificato, la marcatura CE e'
   accompagnata dal suo **numero di identificazione**.

## Output

- Percorso di conformita' applicabile e ruolo (eventuale e limitato) dell'organismo
  notificato.
- Elenco dei documenti richiesti (documentazione tecnica, dichiarazione UE,
  eventuali certificati dell'organismo notificato).

## Avvertenze

- La skill non **classifica** il dispositivo: la classe e' un input (all. VIII).
- La scelta e la responsabilita' della conformita' restano del fabbricante.
