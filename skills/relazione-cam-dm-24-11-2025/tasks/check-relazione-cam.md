# Task: Verifica relazione CAM esistente (DM 24.11.2025)

Data una Relazione CAM di progetto gia' redatta, verifica completezza e conformita' al criterio 2.1.1 dell'Allegato 1 al DM MASE 24/11/2025 e al modello MASE (versione 02/02/2026), e segnala lacune, sezioni mancanti o affermazioni insufficientemente supportate.

## Obiettivo

Restituire all'utente:

- **Esito complessivo**: CONFORME / LACUNOSA / NON CONFORME (con spiegazione)
- **Verifica del regime**: la relazione applica il set di criteri giusto (DM 24/11/2025 vs transitorio DM 256/2022)?
- **Tabella di verifica per sezione e per criterio**: esito (OK / LACUNOSO / MANCANTE / NON APPLICABILE giustificato o meno) con anomalie
- **Lista delle azioni correttive** prioritizzate

## Input richiesti

1. **Testo della relazione da verificare** (incollato o allegato).
2. **Dati della procedura** per la verifica del regime: data bando/inviti; per lavori/congiunti, regime e data di validazione del progetto a base di gara.
3. **Tipologia di intervento** dichiarata (se assente, chiederla).
4. **Criterio di aggiudicazione** (prezzo piu' basso / miglior rapporto qualita'/prezzo).
5. **Eventuali allegati citati** (rapporto LCA, piani, EPD...): la verifica e' possibile anche senza, ma l'esito sara' parziale.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-cam-2025-ambito-transitorio.md` - regime applicabile
- `references/estratti/dm-cam-2025-relazione-cam-struttura.md` - requisiti del criterio 2.1.1 e struttura del modello MASE
- `references/fonti/modello-relazione-cam-2026.md` - struttura di riferimento (sezioni, Tabella 1, Scheda Tipo, allegati)
- `references/fonti/dm-cam-24-11-2025-allegato-1.md` - elenco criteri e regole di capitolo

## Procedura

### Passo 1 - Verifica del regime normativo citato

- La relazione cita il **DM 24/11/2025** come riferimento? Se cita ancora il **DM 256/2022**, verifica con i dati della procedura se il regime transitorio (art. 2 + circolare MASE 10/4/2026: progetto validato in conformita' al DM 256/2022 + bando entro tre mesi dalla validazione) e' effettivamente invocabile. Se non lo e', segnala:
> "ATTENZIONE: la relazione applica i criteri del DM 23/06/2022 n. 256, abrogato dal 2/2/2026 (art. 4 DM 24/11/2025). Per questa procedura [motivazione] si applica il DM 24/11/2025: la relazione va interamente riallineata ai nuovi criteri (numerazione e requisiti diversi)."
- Verifica che le **citazioni dei criteri usino la numerazione del DM 24/11/2025** (es. la Relazione CAM e' il criterio 2.1.1, non 2.2.1 come nel DM 256/2022; i prodotti da costruzione sono il cap. 2.4, non 2.5).

### Passo 2 - Verifica strutturale contro il modello MASE

La relazione contiene almeno (modello, par. 1):

- [ ] sezione **Normativa** (criterio 2.1.1 citato; altri decreti CAM; normative ambientali specifiche es. DNSH; norma tecnica LCA; protocollo di sostenibilita' eventualmente adottato)
- [ ] **strategia ambientale** (par. 3.1): approccio LCA se presente, GWPtotal, economia circolare
- [ ] **descrizione del progetto** (par. 3.2) con tipologia di intervento
- [ ] **Tabella 1 di applicabilita'** dei criteri (par. 3.3) con motivazione tecnica per ogni esclusione/limitazione
- [ ] paragrafo **protocollo di sostenibilita'** se un protocollo e' usato per dimostrare criteri (equivalenza requisito/verifica documentata - par. 3.4 e 1.3.5)
- [ ] **gruppo di lavoro** (par. 3.5)
- [ ] **una Scheda Tipo per ogni criterio applicato** (par. 3.6) con tutti i campi (referente, obiettivi, risultati, verifica, documentazione di riferimento, protocollo, DNSH)
- [ ] eventuale proposta di **criteri premianti** per i lavori (par. 3.7)
- [ ] sezione **Allegati** (par. 4) con i piani/rapporti applicabili

L'assenza del modello MASE in quanto tale non e' di per se' un vizio (il modello "potra' fungere da guida", criterio 2.1.1), ma i **contenuti** del criterio 2.1.1 devono comunque esserci: scelte progettuali per ogni criterio, elaborati richiamati, requisiti dei prodotti, mezzi di prova per la DL.

### Passo 3 - Verifica criterio per criterio

Costruisci (o riusa dalla relazione) l'elenco dei criteri applicabili (task `identifica-criteri-applicabili.md`) e per ciascuno assegna:

- **OK**: scheda/sezione presente, scelte progettuali descritte, elaborati richiamati, mezzi di verifica indicati.
- **LACUNOSO**: presente ma senza dati specifici, senza elaborati richiamati o senza mezzi di prova; oppure motivazione di esclusione generica ("non pertinente") senza giustificazione tecnica (violazione del criterio 2.1.1).
- **MANCANTE**: criterio applicabile non trattato (ne' applicato ne' escluso con motivazione).
- **NON APPLICABILE - GIUSTIFICATO / NON GIUSTIFICATO**: esclusione con/senza motivazione tecnica documentata.

Controlli trasversali (par. 1.3.5):

- i mezzi di prova citati sono ammissibili? Segnala qualunque riferimento a prodotti "certificati CAM" / "attestati di conformita' ai CAM": non sono ammissibili come mezzo di prova;
- se un protocollo di sostenibilita' e' usato per dimostrare criteri: c'e' l'equivalenza documentata requisito-per-requisito e la documentazione del protocollo in allegato?
- se il progetto e' PNRR/DNSH: le correlazioni DNSH sono riportate nelle schede?
- la relazione e' coerente col **livello di progettazione** (dovuta dal PFTE e per ogni fase, criterio 2.1.1)?

Per verificare il merito dei singoli requisiti prestazionali serve il **testo integrale del criterio nel PDF ufficiale**: dove la skill non dispone della trascrizione, marca l'esito come "[VERIFICA DI MERITO DA COMPLETARE sul testo del criterio X.Y.Z]" senza inventare soglie.

### Passo 4 - Esito complessivo e azioni correttive

- **CONFORME**: struttura completa e tutti i criteri applicabili OK o esclusi con giustificazione tecnica.
- **LACUNOSA**: uno o piu' criteri LACUNOSI o esclusioni non giustificate, o sezioni del modello incomplete.
- **NON CONFORME**: regime sbagliato (criteri del DM abrogato fuori dal transitorio), criteri obbligatori MANCANTI, o mezzi di prova inammissibili usati come unica dimostrazione.

Per ogni anomalia: criterio, problema, correzione proposta, documento/elaborato da produrre. Ordina per priorita' (prima le non conformita' di regime, poi i criteri mancanti, poi le lacune).

### Passo 5 - Avvertenze finali

1. La verifica si basa sul testo fornito: non sostituisce la verifica della documentazione allegata (rapporto LCA, EPD, rapporti di prova) ne' quella ex art. 42 / allegato I.7 del Codice.
2. La relazione verificata deve essere firmata dal progettista responsabile.
3. Per i dubbi interpretativi sui singoli criteri consultare il testo integrale dell'Allegato 1 (PDF ufficiale MASE) e la pagina "CAM vigenti".

## Output

1. Esito complessivo con motivazione sintetica
2. Verifica del regime (Passo 1)
3. Check strutturale contro il modello MASE (Passo 2)
4. Tabella di verifica per criterio (Passo 3)
5. Lista azioni correttive prioritizzate (Passo 4)
6. Avvertenze

## Limiti

- La verifica riguarda completezza formale e coerenza con il criterio 2.1.1 e il modello MASE; non valuta la correttezza tecnica delle scelte progettuali.
- Non verifica la veridicita' dei dati dichiarati ne' i documenti allegati non forniti.
- La verifica di merito dei requisiti prestazionali dei singoli criteri richiede il testo integrale del criterio (PDF ufficiale): la skill la segnala come da completare, senza inventare soglie.
- Non aggiorna automaticamente i requisiti a fronte di modifiche successive a `last_verified`.
