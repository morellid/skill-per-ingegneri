# Task: compila-sds

Struttura le 16 sezioni della Scheda di Dati di Sicurezza secondo l'allegato II
del REACH (Reg. UE 2020/878). Supporto documentale: non classifica la sostanza/
miscela ne' fornisce i dati di merito.

## Input

- Tipo di prodotto: **sostanza** o **miscela**.
- Classificazione CLP gia' disponibile (dato di input, non calcolato qui).
- Dati disponibili (fornitore, proprieta', tossicologia, ecotossicologia,
  trasporto).

## Procedura

1. **Prescrizioni generali (Parte A)**: assicurati che la SDS sia compilata da
   **persona competente**, con linguaggio chiaro, **senza indicazioni
   minimizzanti** ("innocua", "sicura...", ecc.) non coerenti con la
   classificazione, e con **data di compilazione** in prima pagina (0.2).
2. **Compila le 16 sezioni** nell'ordine e con la numerazione dell'allegato II:
   1) identificazione (1.1 identificatore, 1.2 usi pertinenti/sconsigliati, 1.3
   fornitore, 1.4 tel. emergenza); 2) pericoli (2.1 classificazione, 2.2 elementi
   etichetta, 2.3 altri pericoli); 3) composizione (3.1 sostanze / 3.2 miscele);
   4) primo soccorso (4.1-4.3); 5) antincendio (5.1-5.3); 6) rilascio accidentale
   (6.1-6.4); 7) manipolazione/immagazzinamento (7.1-7.3); 8) controlli
   esposizione/DPI (8.1-8.2); 9) proprieta' fisiche e chimiche (9.1-9.2); 10)
   stabilita' e reattivita' (10.1-10.6); 11) tossicologiche (11.1-11.2); 12)
   ecologiche (12.1-12.7); 13) smaltimento (13.1); 14) trasporto (14.1-14.7); 15)
   regolamentazione (15.1-15.2); 16) altre informazioni.
3. **Coerenza tra sezioni**: la classificazione (sez. 2) deve essere coerente con
   composizione (sez. 3), tossicologia/ecologia (sez. 11-12) ed etichetta (sez.
   2.2); i DPI (sez. 8) coerenti con manipolazione (sez. 7) e primo soccorso
   (sez. 4).
4. **Sezione 16**: riporta le modifiche rispetto alla versione precedente, la
   legenda di abbreviazioni/acronimi, le fonti dei dati e (miscele) il metodo di
   valutazione ai fini della classificazione.

## Output

- Struttura completa delle 16 sezioni/sotto-sezioni da popolare.
- Nota sulle prescrizioni generali (persona competente, datazione, revisioni).
- Rinvio ai dati/analisi mancanti (che la skill non fornisce).

## Avvertenze

- La **classificazione CLP** e la **valutazione della sicurezza chimica** sono a
  monte e non sono svolte qui.
- L'**obbligo** di fornire la SDS e le sue condizioni sono nell'**art. 31 REACH**
  (rinvio).
