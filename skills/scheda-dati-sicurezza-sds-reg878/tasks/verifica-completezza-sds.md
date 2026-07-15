# Task: verifica-completezza-sds

Verifica la **completezza** e la **conformita' formale** di una SDS esistente
rispetto all'allegato II del REACH (Reg. UE 2020/878). Non entra nel merito
tecnico dei dati (classificazione, valori).

## Input

- SDS da verificare (sostanza o miscela).

## Procedura

1. **Sezioni presenti (1-16)**: verifica che tutte le 16 sezioni siano presenti,
   nell'ordine e con la numerazione dell'allegato II, e che le sotto-sezioni
   obbligatorie di ciascuna sezione siano compilate (vedi
   `references/estratti/sds-16-sezioni-checklist.md`).
2. **Prescrizioni generali (Parte A)**:
   - [ ] **data di compilazione** in prima pagina; se e' una revisione, presenza
     di "Revisione: (data)" + versione sostituita e modifiche in **sezione 16**
     (0.2.5);
   - [ ] assenza di **indicazioni minimizzanti** ("innocua", "sicura nella maggior
     parte...", "nessun effetto sulla salute") o non coerenti con la
     classificazione (0.2.4);
   - [ ] linguaggio chiaro/conciso (0.2.3-0.2.4).
3. **Coerenza incrociata**: classificazione (sez. 2) coerente con composizione
   (sez. 3) e con tossicologia/ecologia (sez. 11-12); DPI (sez. 8) coerenti con
   manipolazione (sez. 7) e primo soccorso (sez. 4); trasporto (sez. 14) coerente
   con i pericoli.
4. **Segnala** le sezioni/sotto-sezioni mancanti o incoerenti e le eventuali
   violazioni delle prescrizioni generali.

## Output

- Esito della verifica di completezza (sezioni/sotto-sezioni presenti/mancanti).
- Rilievi formali (datazione/revisione, indicazioni minimizzanti, incoerenze).

## Avvertenze

- La verifica e' **formale/di completezza**: non convalida i **valori** ne' la
  correttezza della **classificazione CLP** (competenza specialistica).
