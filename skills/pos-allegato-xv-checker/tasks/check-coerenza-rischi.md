# Task: Verifica coerenza rischi - misure

Verifica che per ogni rischio identificato nel POS sia prevista almeno una misura di prevenzione/protezione coerente, e viceversa che ogni misura faccia riferimento a un rischio concreto identificato nel cantiere. Questo controllo incrocia la voce g) del POS (misure integrative rispetto al PSC) con le analisi dei rischi richiamate nel POS stesso o nel DVR.

## Obiettivo

Produrre un report strutturato che evidenzi:
- Rischi dichiarati privi di misure corrispondenti
- Misure dichiarate senza riferimento a un rischio specifico (possibile boilerplate copia-incolla)
- Coppie rischio-misura sospette per incoerenza tecnica
- Stima qualitativa della coerenza complessiva

## Input richiesti

- Sezione del POS relativa all'analisi dei rischi (puo' essere esplicita o rinvio al DVR/PSC)
- Sezione del POS relativa alle misure di prevenzione e protezione (voce g dell'Allegato XV 3.2.1)
- Elenco DPI (voce i) e procedure (voce h) - utili come misure accessorie
- Opzionale: PSC di riferimento, per distinguere misure PSC da misure POS-integrative
- Opzionale: natura del cantiere (edilizia civile, scavi, demolizioni, impianti, ecc.) per calibrare le attese

Se l'input e' parziale, dichiararlo nel report e limitare la verifica al fornito.

## Fonti normative

Leggere prima:
- `references/estratti/allegato-xv-testo.md` punto 3.2.1 lett. g) (misure integrative) e lett. d), i), h)
- `references/estratti/allegato-xv-testo.md` Allegato XV.2 (tassonomia elementi essenziali analisi rischi area cantiere)
- D.Lgs. 81/2008 Titolo IV Capo II (art. 95-101) - principi di valutazione e coordinamento rischi

## Procedura

### Passo 1 - Estrazione rischi dal POS

Identificare nel testo del POS tutti i rischi dichiarati o richiamati. Fonti tipiche:
- Sezione esplicita "analisi rischi" o "valutazione rischi"
- Rinvio al DVR con estratto allegato
- Rinvio al PSC (nel qual caso i rischi generali del PSC valgono anche per il POS)
- Elenco fasi di lavoro con rischi associati
- Tabelle di matrice rischi x probabilita' x magnitudo

Produrre una lista normalizzata dei rischi, usando la tassonomia standard cantiere:

**Rischi dell'area di cantiere** (Allegato XV.2):
- Caduta di materiali dall'alto
- Linee aeree e condutture sotterranee
- Traffico e viabilita'
- Edifici interferenti
- Altri cantieri o insediamenti
- Rumore ambientale
- Polveri, fibre, fumi, vapori, gas
- Infrastrutture da proteggere

**Rischi delle lavorazioni** (comuni):
- Caduta dall'alto
- Seppellimento negli scavi
- Elettrocuzione / contatti elettrici
- Rumore (esposizione lavoratori)
- Vibrazioni (mano-braccio e corpo intero)
- Polveri inalabili, nebbie, fumi
- Agenti chimici (solventi, resine, cemento)
- Agenti biologici (raro in edilizia ma possibile in demolizioni con amianto o muffe)
- Movimentazione manuale carichi
- Urti, schiacciamento, compressione
- Caduta oggetti dall'alto
- Tagli, lacerazioni, abrasioni
- Microclima (caldo/freddo)
- Stress termico (nuovo pattern post 2021)
- Interferenze tra lavorazioni
- Incendio, atmosfere esplosive

Ogni rischio estratto va taggato con: tipo, fase di lavoro associata (se indicato), magnitudo/probabilita' se dichiarate.

### Passo 2 - Estrazione misure dal POS

Identificare tutte le misure preventive e protettive dichiarate nel POS. Fonti tipiche:
- Voce g) "misure integrative rispetto al PSC"
- Voce h) "procedure complementari"
- Voce i) "elenco DPI"
- Eventuali sezioni dedicate a singoli rischi

Normalizzare le misure usando la tassonomia Allegato XV.1:
- **Apprestamenti** (opere provvisionali): ponteggi, parapetti, andatoie, armature scavi, recinzioni
- **Attrezzature di sicurezza**: impianti antincendio, impianti elettrici di cantiere conformi
- **Infrastrutture**: viabilita' pedonale, aree di deposito
- **Mezzi e servizi di protezione collettiva**: segnaletica, avvisatori acustici, illuminazione emergenza, estinguenti, servizi emergenza
- **DPI**: per tipologia di rischio
- **Procedure operative**: sequenze, turni, cronoprogramma, coordinamento
- **Informazione/formazione**: briefing, attestati, registri

### Passo 3 - Matrice rischi-misure

Costruire una matrice bidirezionale:

**Direzione 1**: per ogni rischio, identificare le misure corrispondenti attese e verificarne la presenza. Usare il seguente prontuario di attese minimali:

| Rischio | Misure attese (minimali) |
|---------|--------------------------|
| Caduta dall'alto (> 2m) | Parapetti O imbracatura + linea vita O ponteggio conforme + DPI III categoria + formazione specifica |
| Seppellimento scavi | Armature scavi / sbadacchiature / pareti inclinate per terreno coerente + segregazione area |
| Elettrocuzione | Quadro ASC + differenziali + messa a terra + isolamento cavi + verifiche periodiche |
| Rumore > 85 dB(A) | DPI uditivi obbligatori + segnaletica + rotazione personale + formazione |
| Polveri inalabili | Aspirazione localizzata O nebulizzazione acqua + FFP2/FFP3 + formazione |
| Vibrazioni | Attrezzi a bassa vibrazione + guanti antivibrazione + rotazione + sorveglianza sanitaria |
| Movimentazione carichi | Mezzi meccanici quando possibile + formazione tecniche sollevamento + limiti peso |
| Caduta oggetti dall'alto | Reti di protezione + tettoie + segregazione area sottostante + elmetti |
| Urti/schiacciamento da macchine | Delimitazione aree operatrici + segnaletica + segnali acustici + procedure coordinamento operatore-pedoni |
| Agenti chimici | Scheda SDS per ogni sostanza + DPI specifici (guanti chimici, occhiali, maschera) + procedure travaso |
| Taglio/lacerazione | Guanti taglio-resistenti + protezioni lame attrezzi + formazione uso attrezzature |
| Stress termico (caldo) | Pause, idratazione, cronoprogramma evita ore di punta estive, indumenti ventilati |
| Incendio / infiammabili | Estinguenti in loco + divieto fumo + stoccaggio infiammabili + addetto antincendio formato |
| Interferenze lavorazioni | Sfasamento spaziale O temporale + riunioni coordinamento + procedure in comune + coordinatore operativo |

**Direzione 2**: per ogni misura dichiarata, verificare che corrisponda ad almeno un rischio identificato. Una misura "orfana" (senza rischio agganciato) e' segnale di:
- Boilerplate copia-incolla (misura copiata da altro POS senza senso contestuale)
- Analisi rischi incompleta (il rischio esiste ma non e' stato esplicitato)

### Passo 4 - Flag per incoerenze

Tipologie di incoerenza:

1. **Rischio senza misura** (gap grave): il POS identifica un rischio ma non descrive misure per mitigarlo.
2. **Misura senza rischio** (possibile boilerplate): misura dichiarata senza riferimento a un rischio specifico del cantiere.
3. **Misura inadeguata al rischio** (incoerenza tecnica): la misura esiste ma e' tecnicamente insufficiente. Esempi:
   - "Guanti generici" per rischio chimico (servirebbero guanti chimici specifici per la sostanza)
   - "Maschera generica" per polveri (serve classe FFP2/FFP3 a seconda)
   - "Cinture di sicurezza" (terminologia obsoleta, oggi: imbracature anticaduta III categoria)
4. **Misura duplicativa del PSC** (non integrativa): voce g) richiede misure integrative, non ripetizione letterale del PSC.

### Passo 5 - Output

```markdown
# Verifica coerenza rischi - misure

**Data verifica**: [data]
**POS analizzato**: [id]
**Contesto cantiere**: [se dichiarato]

## Sintesi

- Rischi estratti dal POS: N
- Misure estratte dal POS: M
- Coppie rischio-misura coerenti: P (stima %)
- Rischi senza misura: X
- Misure senza rischio chiaro: Y
- Coppie sospette per inadeguatezza: Z

**Esito**: [COERENTE | COERENTE CON NOTE | INCOERENZE SIGNIFICATIVE | INCOMPLETO]

## Matrice rischi-misure

| Rischio (dal POS) | Fase | Misure corrispondenti (dal POS) | Esito | Note |
|------------------|------|-------------------------------|-------|------|
| Caduta dall'alto | Elevazioni | Ponteggio; Parapetti; Imbracature; Elmetti | OK | Misure adeguate |
| Polveri | Demolizioni | Maschera FFP3; Aspirazione | OK | |
| Rumore | Demolizioni | (nessuna misura specifica nel POS) | GAP | Rischio dichiarato > 85 dB(A), DPI uditivi attesi |
| ... | ... | ... | ... | ... |

## Misure senza rischio associato (possibile boilerplate)

- Misura X (voce g paragrafo Y del POS)
  - Non risulta agganciata a un rischio specifico
  - Possibile copia da template senza adattamento

## Incoerenze tecniche

| Rischio | Misura dichiarata | Problema | Raccomandazione |
|---------|------------------|----------|-----------------|
| Chimico (solventi vernici) | "Guanti generici" | Guanti non qualificati per rischio chimico | Specificare guanti conformi EN 374 per solventi usati |
| ... | ... | ... | ... |

## Misure duplicative del PSC

Voci della sezione "misure integrative" che risultano copia del PSC invece che integrazioni:
- ...

## Raccomandazioni

1. Integrare [rischio X] con misura [...]
2. Verificare adeguatezza di [misura Y] rispetto a [specifico rischio]
3. Sostituire boilerplate della voce g con descrizione specifica delle misure integrative effettive

## Limiti di questa verifica

- Matching basato su parole chiave + tassonomia standard. L'adeguatezza tecnica puntuale (es. classe specifica di DPI) richiede verifica di dominio.
- Non sostituisce la valutazione in cantiere da parte del CSE.
- Non verifica l'efficacia operativa delle misure (che si osserva in cantiere).
- Se il POS rinvia al DVR o al PSC, la verifica e' limitata al contenuto del POS. Consigliabile fornire anche gli altri documenti per una verifica completa.

## Rinvio al professionista firmatario

**La valutazione di adeguatezza tecnica delle misure rispetto al cantiere specifico e alle singole lavorazioni spetta al CSE, al datore di lavoro e al coordinatore per la sicurezza. Questo report e' strumento di supporto, non decisione finale.**
```

## Casi limite

### POS che rinvia tutto al PSC
Se la voce g) dice "si adottano integralmente le misure del PSC" senza misure integrative proprie, segnalarlo come inadeguato: la lettera g) richiede **misure integrative rispetto al PSC**, non una delega al PSC.

Eccezione: se il cantiere non ha PSC (lavori esclusi dal campo di applicazione del Titolo IV Capo I), allora il POS deve assorbire le misure di valutazione autonomamente. Segnalare la situazione e verificare coerenza del solo POS.

### Cantiere senza rischi specifici dichiarati
Se il POS non dichiara esplicitamente rischi (es. rinvia genericamente al DVR senza estratto), il matching non puo' partire. Il report dichiara questa limitazione e suggerisce di fornire:
- Estratto DVR aziendale sui rischi del mestiere
- Analisi rischi specifica del cantiere

### Rischi teorici ma non attesi per il cantiere
Alcuni POS elencano rischi generici (es. "rischio nucleare", "rischio biologico") che non pertinenti. Non trattarli come violazione ma segnalare come sovraestensione, utile per capire se il POS e' stato calibrato sul cantiere.

## Limiti di questo task

- Matching basato su estrazione testuale + tassonomia. Possono sfuggire:
  - Rischi descritti in forma non standard (es. narrativi invece di tabellari)
  - Misure descritte in modo indiretto (es. in un allegato al POS non letto)
- Non e' un'analisi di adeguatezza tecnica - solo di completezza e coerenza apparente
- Non valuta la compatibilita' con il cronoprogramma
- Non sostituisce il giudizio del CSE sull'effettivo controllo del rischio residuo

## Esempi

Vedi `examples/` per test case:
- `coerenza-buona-pos-allegato-xv/` - POS con rischi e misure ben matchati (basato sul caso `conforme-cantiere-piccolo`)
- `coerenza-incoerente-boilerplate/` - POS con misure generiche e rischi non coperti
