# Task: scegli la procedura di valutazione della conformita' (modulo)

## Obiettivo

Elencare i moduli di valutazione della conformita' ammissibili per la categoria PED determinata e illustrare il ruolo dell'organismo notificato e gli adempimenti documentali, ai sensi dell'**art. 10 c. 2** e dell'**Allegato III** del D.Lgs 26/2016. La scelta finale del modulo e' del fabbricante.

## Input richiesti

Da `tasks/determina-categoria.md` (eseguito a monte): categoria PED (I, II, III, IV) e tipo di attrezzatura. Conferma all'utente:

- Categoria (I, II, III, IV) ed eventuale eccezione testuale che ha fissato la categoria (es. "gas instabili tabella 1 -> III").
- Tipo di attrezzatura: recipiente, tubazione, accessorio, insieme. Per gli insiemi: hai gia' valutato la categoria di integrazione e di protezione ex art. 10 c. 6?
- Volume produttivo previsto: pezzo unico, produzione in serie, prototipo.
- L'organizzazione del fabbricante dispone di un sistema di gestione della qualita' (es. ISO 9001) o di garanzia totale della qualita'? (rilevante per moduli H, H1, D, E e simili).
- Hai gia' un organismo notificato di riferimento? (vedi banca dati NANDO della Commissione europea per la verifica della notifica).

## Fonti

- `references/estratti/dlgs-26-2016-classificazione-moduli.md` sezione 5 (art. 10 c. 2) e sezione 6 (descrizione moduli).
- `references/fonti/dlgs-26-2016.md` art. 10 e Allegato III (12 moduli).

## Procedura

1. **Mappatura categoria -> moduli ammissibili** (testuale art. 10 c. 2):
   - **Categoria I**: modulo **A** (controllo interno della produzione - **senza** organismo notificato).
   - **Categoria II**: modulo **A2** (controllo interno + prove a intervalli casuali, con organismo notificato), oppure modulo **D1** (garanzia qualita' processo produzione), oppure modulo **E1** (garanzia qualita' ispezione/prova finale).
   - **Categoria III**: moduli **B (tipo di progetto) + D**, oppure **B (tipo di progetto) + F**, oppure **B (tipo di produzione) + E**, oppure **B (tipo di produzione) + C2**, oppure modulo **H** (garanzia totale qualita').
   - **Categoria IV**: moduli **B (tipo di produzione) + D**, oppure **B (tipo di produzione) + F**, oppure modulo **G** (verifica dell'unita'), oppure modulo **H1** (garanzia totale qualita' con controllo della progettazione).
2. **Opzione categoria superiore** (art. 10 c. 3): il fabbricante puo' scegliere una procedura prevista per una categoria superiore, mai inferiore. Es. un'attrezzatura in categoria II puo' essere valutata con un modulo di III, ma non con il modulo A.
3. **Eccezioni che fissano il modulo**: per gli **insiemi per produzione di acqua calda** ex art. 3 c. 2 lett. c, l'Allegato II impone esame UE del tipo (modulo **B tipo di progetto**) oppure garanzia totale della qualita' (modulo **H**), indipendentemente dalla "fascia" PS/V che si leggerebbe sulla tabella 5.
4. **Ruolo dell'organismo notificato per modulo**:
   - Modulo A: nessun organismo notificato; il fabbricante esegue tutto in regime di controllo interno.
   - Modulo A2: organismo notificato esegue o fa eseguire prove sui prodotti a intervalli casuali.
   - Modulo B (tipo di progetto): organismo notificato esamina il progetto, rilascia certificato di esame UE del progetto. Esclude l'uso del metodo di progettazione sperimentale (Allegato I punto 2.2.4).
   - Modulo B (tipo di produzione): organismo notificato esamina il tipo di produzione (campione rappresentativo).
   - Modulo C2: prove sui prodotti a intervalli casuali a carico dell'organismo notificato.
   - Modulo D, D1, E, E1, H, H1: l'organismo notificato approva e sorveglia il sistema di qualita' del fabbricante (rivalutazione completa ogni tre anni; visite senza preavviso).
   - Modulo F: organismo notificato verifica l'attrezzatura (verifica per attrezzatura o statistica).
   - Modulo G: organismo notificato verifica ogni singola unita'.
5. **Visite senza preavviso e valutazione finale per categorie III e IV** (art. 10 c. 4): per le procedure di garanzia della qualita' applicate a categorie III e IV su attrezzature di art. 3 c. 1 lett. a) punto 1), c. 1 lett. a) punto 2) primo trattino, e c. 1 lett. b), l'organismo notificato, durante visite senza preavviso, preleva un campione e compie la valutazione finale ex Allegato I punto 3.2. Almeno due visite nel primo anno di fabbricazione. Cadenza successiva determinata in base ai criteri del punto 4.4 dei moduli D/E/H e del punto 5.4 del modulo H1.
6. **Produzione in unico esemplare di recipienti e attrezzature di categoria III di art. 3 c. 1 lett. b)** (art. 10 c. 5): se il fabbricante sceglie il modulo H, l'organismo notificato compie o fa compiere la valutazione finale ex Allegato I punto 3.2 per ciascun singolo esemplare; il fabbricante deve comunicare il calendario di produzione.
7. **Insiemi** (art. 10 c. 6): la valutazione globale comprende
   - valutazione di ciascuna attrezzatura costitutiva (con la procedura della sua categoria);
   - valutazione dell'integrazione (punti 2.3, 2.8, 2.9 Allegato I), per la categoria piu' elevata fra le attrezzature interessate (esclusi accessori di sicurezza);
   - valutazione della protezione (punti 2.10 e 3.2.3 Allegato I), per la categoria piu' elevata fra le attrezzature da proteggere.
8. **Documentazione tecnica**: per ogni modulo, l'Allegato III elenca elementi minimi obbligatori (descrizione generale, disegni di progettazione e fabbricazione, descrizioni e spiegazioni, norme armonizzate applicate o, in mancanza, descrizione delle soluzioni adottate per soddisfare i RES dell'Allegato I, calcoli, relazioni di prova, elementi su approvazione processi di fabbricazione, qualifiche del personale, ecc.). Conservazione: dieci anni dalla data di immissione sul mercato.
9. **Rappresentante autorizzato**: alcuni obblighi del fabbricante (dichiarazione UE, conservazione documentazione, cooperazione con autorita') possono essere adempiuti dal rappresentante autorizzato se specificati nel mandato (art. 4-ter). Restano in capo al fabbricante l'obbligo di garantire la conformita' ai RES (art. 4-bis c. 1) e di redigere la documentazione tecnica (art. 4-bis c. 2).

## Output

```
Selezione procedura di valutazione della conformita' - <descrizione attrezzatura>

Categoria PED: <I / II / III / IV>
Eventuale eccezione applicata: <es. "insieme acqua calda - moduli B(progetto) o H imposti">

Moduli ammissibili per la categoria <X> (art. 10 c. 2):
- <elenco moduli con denominazione completa>

Opzione categoria superiore (art. 10 c. 3): consentita, fissando l'attenzione su <modulo di categoria superiore eventualmente segnalato>.

Ruolo dell'organismo notificato per modulo:
- <riepilogo per ciascun modulo selezionato dall'utente>

Cadenze e visite (art. 10 c. 4 e c. 5): <se categoria III o IV con moduli di garanzia qualita': cita visite senza preavviso, valutazione finale, almeno due visite nel primo anno>

Documentazione tecnica:
- Conservazione 10 anni (art. 4-bis c. 3).
- Elementi minimi previsti dall'Allegato III per il modulo scelto.

Insiemi (se applicabile):
- <descrizione delle tre valutazioni: componenti, integrazione, protezione>

Rinvio:
- La scelta del modulo e' del fabbricante. Per moduli con coinvolgimento dell'organismo notificato,
  il fabbricante deve sceglierlo dalla banca dati NANDO della Commissione europea.
- Per modulo B (tipo di progetto), il metodo di progettazione sperimentale (Allegato I punto 2.2.4)
  non puo' essere usato.
```

## Limiti

- La skill non designa l'organismo notificato e non valida la sua notifica: la verifica e' sulla banca dati NANDO.
- La skill non scrive ne' verifica il contenuto puntuale del fascicolo tecnico per il modulo scelto: rinvia agli elementi minimi previsti dall'Allegato III e al fabbricante.
- La scelta fra moduli alternativi per una stessa categoria ha implicazioni operative (costi, tempi, sistema di qualita' richiesto, sorveglianza) che esulano dall'analisi normativa: spetta al fabbricante.
- Non gestisce il caso di approvazione europea di materiali (art. 11): se l'utente cita un'approvazione europea di materiali, la skill segnala la pertinenza dell'art. 11 ma non valuta l'approvazione.
