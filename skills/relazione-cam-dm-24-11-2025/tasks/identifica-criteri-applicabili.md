# Task: Identifica il regime e i criteri CAM applicabili (DM 24.11.2025)

Data la procedura e la tipologia di intervento, determina (1) quale regime CAM si applica (DM 24/11/2025 oppure regime transitorio DM 256/2022) e (2) quali criteri dell'Allegato 1 al DM 24/11/2025 si applicano, producendo la bozza della Tabella 1 di applicabilita' del modello MASE.

## Obiettivo

Restituire all'utente:

- **Regime applicabile** (DM 24/11/2025 vs transitorio DM 256/2022) con motivazione basata su art. 1 co. 2 e art. 2 DM 24/11/2025 e circolare MASE 10/4/2026.
- **Tipologia di intervento identificata** secondo le definizioni dell'art. 3 DPR 380/2001 (richiamate dall'art. 3 DM 24/11/2025), con motivazione.
- **Bozza della Tabella 1 di applicabilita'** (modello MASE): per ogni criterio dei capitoli 2.1-2.5 (e 3.1 per il capitolato del progetto esecutivo), esito Applicabile / Non applicabile / Parzialmente applicabile con motivazione tecnica da completare.
- **Elenco dei criteri premianti potenzialmente rilevanti** (2.6 progettazione, 3.2 lavori, 4.3 congiunto) se l'aggiudicazione e' col miglior rapporto qualita'/prezzo.
- **Avvertenze specifiche** per il caso in esame.

## Input richiesti

Raccogliere dall'utente (chiedere se non forniti):

1. **Dati della procedura** (per il regime):
   - data (prevista) di pubblicazione del bando o di invio degli inviti;
   - tipo di affidamento: servizio di progettazione/DL, servizi di manutenzione, esecuzione lavori, congiunto progettazione esecutiva + lavori, progettazione interna alla SA;
   - per lavori/congiunti: in vigenza di quale DM e' stato validato il progetto a base di gara (PFTE per il congiunto, esecutivo per i lavori) e data di validazione.
2. **Tipologia di intervento**: descrizione breve (es. "nuova scuola", "manutenzione straordinaria facciata", "adeguamento sismico", "passerella ciclopedonale"). Ricondurla alle definizioni dell'art. 3 DPR 380/2001; ricordare che l'ambito include anche **opere di ingegneria civile e manufatti in genere** (par. 1.1 Allegato 1), escluse le infrastrutture stradali (CAM strade DM 5/8/2024).
3. **Caratteristiche rilevanti per l'applicabilita' dei singoli criteri**: presenza di aree verdi, movimenti di terra, demolizioni, impianti oggetto di intervento, edificio esistente vs nuova opera.
4. **Criterio di aggiudicazione**: prezzo piu' basso o miglior rapporto qualita'/prezzo (determina la rilevanza dei premianti).

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-cam-2025-ambito-transitorio.md` - regime temporale e transitorio
- `references/estratti/dm-cam-2025-relazione-cam-struttura.md` - regole di applicabilita' per capitolo e per criterio; elenco criteri
- `references/fonti/dm-cam-24-11-2025-allegato-1.md` - intestazioni di capitolo trascritte + elenco completo dei criteri
- `references/estratti/dlgs-36-2023-art57.md` - obbligo di applicazione

## Procedura

### Passo 1 - Determinazione del regime (nuovo DM vs transitorio)

Applica le regole dell'estratto `dm-cam-2025-ambito-transitorio.md`:

1. **Bando/invito prima del 2/2/2026** -> DM 256/2022 (circolare MASE, par. B).
2. **Servizio di progettazione/DL con bando/invito dal 2/2/2026** -> DM 24/11/2025.
3. **Lavori o congiunto con bando/invito dal 2/2/2026**:
   - progetto a base di gara validato in conformita' al **DM 24/11/2025** -> DM 24/11/2025;
   - progetto validato in conformita' al **DM 256/2022** e bando/invito **entro tre mesi dalla validazione** -> regime transitorio DM 256/2022 (art. 2);
   - progetto validato in conformita' al DM 256/2022 ma bando/invito **oltre tre mesi** dalla validazione -> DM 24/11/2025 (il progetto va adeguato).
4. **Progettazione interna** non ancora validata al 2/2/2026 -> DM 24/11/2025, anche con incarico precedente (art. 1 co. 2 lett. c).

Riassumi:
> "La tua procedura ricade nel regime **[DM 24/11/2025 / transitorio DM 256/2022]** perche': [motivazione con citazione]. Confermi i dati (data bando, data e regime di validazione del progetto)?"

Se il regime e' quello transitorio: avverti che questa skill e' costruita sul DM 24/11/2025 e che per i criteri del DM 256/2022 valgono gli estratti [STORICO] (`dm-256-2022-*.md`); prosegui solo su richiesta esplicita.

### Passo 2 - Identificazione della tipologia di intervento

Riconduci l'intervento alle definizioni dell'art. 3 DPR 380/2001 (manutenzione ordinaria, manutenzione straordinaria, restauro e risanamento conservativo, ristrutturazione edilizia, nuova costruzione, ristrutturazione urbanistica), richiamate dall'art. 3 DM 24/11/2025. Il DM 24/11/2025 **non usa piu' le categorie NC/R1/R2/MS** del DM 256/2022: la tipologia serve solo ad applicare le regole di applicabilita' dei singoli criteri.

Se l'oggetto non e' un edificio: verifica che rientri comunque nell'ambito (opere di ingegneria civile, manufatti - par. 1.1) e che non sia un'infrastruttura stradale (CAM strade).

### Passo 3 - Applicabilita' per capitolo

Applica le regole di capitolo (trascritte in `dm-cam-24-11-2025-allegato-1.md`):

| Capitolo | Obbligatorieta' | Manutenzione ordinaria/straordinaria |
|---|---|---|
| 2.1 Clausole contrattuali progettazione (2.1.1 Relazione CAM, 2.1.2 capitolato, 2.1.3 BIM) | obbligatorio (art. 57 co. 2) | SI, si applica |
| 2.2 Territoriale-urbanistico (2.2.1-2.2.9) | obbligatorio | secondo le "Indicazioni al progettista" dei singoli criteri |
| 2.3 Edifici e altre opere (2.3.1-2.3.17) | obbligatorio | secondo le "Indicazioni al progettista" dei singoli criteri (es. 2.3.1 diagnosi energetica NON si applica a manutenzione ordinaria/straordinaria) |
| 2.4 Prodotti da costruzione (2.4.1-2.4.18) | obbligatorio | SI, si applica |
| 2.5 Cantiere (2.5.1-2.5.4) | obbligatorio | SI, si applica (costi nel quadro economico) |
| 2.6 Premianti progettazione (2.6.1-2.6.10) | solo se miglior rapporto qualita'/prezzo | - |
| 3.1 Clausole contrattuali lavori (3.1.1-3.1.4) | obbligatorio per l'appaltatore; il progettista le riporta nel capitolato del progetto esecutivo | SI, si applica |
| 3.2 Premianti lavori / 4.3 premianti congiunto | solo se miglior rapporto qualita'/prezzo | - |

Per l'affidamento congiunto: cap. 4 rinvia a 2.1+3.1 (clausole), 2.2-2.5 (specifiche), 2.6+3.2+4.3 (premianti).

### Passo 4 - Applicabilita' per singolo criterio

Per ogni criterio dei capitoli applicabili (elenco completo nella fonte `dm-cam-24-11-2025-allegato-1.md`), verifica le **"Indicazioni al progettista"** riportate in corsivo sotto il titolo del criterio nel PDF ufficiale dell'Allegato 1 (par. 1.3.5): molte delimitano l'applicabilita' per tipologia di intervento o per presenza di elementi specifici. Esempi trascritti in fonte:

- **2.2.1** (biodiversita'): si applica a nuova costruzione, ristrutturazione urbanistica, ristrutturazione edilizia, demolizione e ricostruzione, restauro e risanamento conservativo, manutenzione ordinaria e straordinaria "qualora siano previsti interventi nelle aree verdi".
- **2.3.1** (diagnosi energetica): NON si applica a manutenzione ordinaria o straordinaria; per gli ampliamenti si applica solo se connessi energeticamente all'edificio principale.

Per i criteri di cui la skill non ha la trascrizione integrale, NON inventare condizioni di applicabilita': indica "[VERIFICARE indicazioni al progettista nel testo del criterio - PDF ufficiale Allegato 1]" e chiedi all'utente di leggere il criterio.

### Passo 5 - Output: bozza della Tabella 1 del modello MASE

Produci la tabella con le colonne del modello ufficiale (fonte `modello-relazione-cam-2026.md`):

| Criterio | Applicabile | Non applicabile | Parzialmente applicabile | Motivazione tecnica | Criterio del protocollo energetico ambientale applicato | Criterio DNSH correlato |
|---|---|---|---|---|---|---|
| 2.1.1 Relazione CAM di progetto | X | | | clausola contrattuale obbligatoria | [se pertinente] | [se pertinente] |
| ... una riga per ogni criterio dei capitoli applicabili ... | | | | | | |

Regole di compilazione:
- ogni esclusione o applicazione parziale deve avere una **motivazione tecnica** (criterio 2.1.1: "illustrate e giustificate dal punto di vista tecnico");
- le colonne protocollo/DNSH si compilano solo se il progetto adotta un protocollo di sostenibilita' o e' soggetto a DNSH (es. PNRR);
- chiudi con l'elenco dei criteri premianti proponibili (cap. 2.6/3.2/4.3) se l'aggiudicazione e' col miglior rapporto qualita'/prezzo.

### Passo 6 - Avvertenze finali

1. La valutazione di applicabilita' resta responsabilita' del progettista: la tabella prodotta e' una bozza da verificare criterio per criterio sul testo integrale dell'Allegato 1.
2. Restano salvi vincoli, tutele e regolamenti locali piu' restrittivi (criterio 2.1.1).
3. Se il progetto e' soggetto a DNSH (PNRR) o adotta un protocollo di sostenibilita', la relazione dovra' documentare le correlazioni (modello MASE, Tabella 1 e Scheda Tipo).

## Output

1. Regime applicabile con motivazione e citazioni.
2. Tipologia di intervento (art. 3 DPR 380/2001) con motivazione.
3. Bozza Tabella 1 di applicabilita' (modello MASE) con motivazioni da completare.
4. Elenco premianti proponibili (se pertinente).
5. Avvertenze.

## Limiti

- La skill non riproduce i requisiti puntuali dei singoli criteri: per ognuno rinvia alle "Indicazioni al progettista" e al testo del criterio nel PDF ufficiale.
- Non decide l'applicabilita' nei casi dubbi: li segnala come "[VERIFICARE]" con rinvio al testo e al RUP/SA.
- Non copre il regime transitorio nel merito (criteri DM 256/2022): estratti [STORICO] disponibili ma la skill e' costruita sul DM 24/11/2025.
