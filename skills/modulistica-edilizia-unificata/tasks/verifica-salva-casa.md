# Task: Verifica applicabilita' Salva Casa

Verifica se le modifiche introdotte dal Salva Casa (DL 69/2024 conv. L. 105/2024) sono applicabili al caso in esame, distinguendo tra: nuove tolleranze costruttive (art. 34-bis), sanatoria semplificata (art. 36-bis), cambio destinazione d'uso (art. 23-ter), stato legittimo (art. 9-bis), edilizia libera ampliata (art. 6).

## Obiettivo

Restituire all'utente:
- L'**applicabilita' specifica** delle modifiche del Salva Casa al caso in esame
- Per ogni modifica applicabile: l'**effetto pratico** (nuova soglia di tolleranza, regime di sanatoria piu' favorevole, possibilita' di cambio uso senza opere, etc.)
- Eventuali **alternative procedurali** (es. art. 36-bis vs art. 36, edilizia libera vs CILA per VEPA)
- Avvertenze su **regime transitorio**, contenziosi pendenti, varianti regionali

## Input richiesti

Variabili minime (chiedere all'utente se non fornite):

1. **Tipologia di verifica richiesta**:
   a. Tolleranze art. 34-bis (verifica se le difformita' rilevate rientrano nelle nuove soglie graduate per superficie utile)
   b. Sanatoria art. 36-bis (verifica se l'opera abusiva e' sanabile con doppia conformita' alleggerita)
   c. Cambio destinazione d'uso art. 23-ter (verifica se il cambio rientra nel regime SCIA semplificato post Salva Casa)
   d. Stato legittimo art. 9-bis (verifica se l'immobile ha uno stato legittimo accertabile)
   e. Edilizia libera ampliata (VEPA, tende, pergolati, cappotto, etc.)

2. **Dati immobile**:
   - Indirizzo / identificativi catastali
   - Superficie utile (SU) - importante per art. 34-bis
   - Categoria d'uso attuale
   - Vincoli sovraordinati (paesaggio, beni culturali, idrogeologico, sismico, idraulico)
   - Zona urbanistica (PRG/PUC)
   - Anno di costruzione (rilevante per stato legittimo)

3. **Dati intervento**:
   - Descrizione delle opere o difformita'
   - Anno di realizzazione (per sanatorie)
   - Titolo originario (se esisteva): PdC, SCIA, CILA, nessuno

## Fonti normative

Leggere prima di procedere:
- [`references/estratti/dl-69-2024-salva-casa.md`](../references/estratti/dl-69-2024-salva-casa.md) - sintesi delle modifiche del Salva Casa
- [`references/estratti/dpr-380-2001-regimi-edilizi.md`](../references/estratti/dpr-380-2001-regimi-edilizi.md) - articoli del DPR 380 modificati

## Procedura

### Branch A - Tolleranze costruttive (art. 34-bis)

#### Passo A1 - Misura SU
Chiedere all'utente la **superficie utile** (SU) dell'unita' immobiliare interessata. Senza SU non si puo' applicare la soglia.

#### Passo A2 - Determina soglia applicabile

Per gli interventi **realizzati entro il 24 maggio 2024**, soglie graduate in funzione della SU calcolata sulla **superficie assentita** (art. 34-bis co. 1-ter):

| Superficie utile (SU) | Tolleranza % |
|------------------------|--------------|
| SU < 60 mq | 6% |
| SU < 100 mq | 5% |
| SU compresa tra 100 e 300 mq | 4% |
| SU compresa tra 300 e 500 mq | 3% |
| SU > 500 mq | 2% (regime pre-Salva Casa) |

#### Passo A3 - Verifica entita' delle difformita'

Le tolleranze si applicano a:
- **Misure di altezza, distacchi, cubatura, superficie coperta** (regime tradizionale)
- **Tolleranze esecutive (co. 1-bis)**: minore dimensionamento, mancata realizzazione di elementi architettonici non strutturali, irregolarita' geometriche, modifiche alle finiture, diverse collocazioni di impianti, diversa realizzazione dei vani interni

**Limiti**:
- NON si applica a difformita' che comportino **variazione del numero di unita' immobiliari**
- NON si applica a difformita' che comportino **variazione della destinazione d'uso** che modifichi la dotazione standard
- Per **immobili vincolati** (D.Lgs. 42/2004): tolleranze applicabili **solo previa autorizzazione** Soprintendenza

#### Passo A4 - Output Branch A

```markdown
## Verifica tolleranze art. 34-bis

**Immobile**: SU = [X] mq -> soglia applicabile **[Y]%**

**Difformita' rilevate**:
- [Descrizione 1]: scostamento [Z] mq / Z% rispetto a parametro autorizzato -> [in tolleranza / fuori tolleranza]
- ...

**Esito**:
- [In tolleranza] -> NESSUN titolo edilizio richiesto. Applicare l'art. 34-bis come tolleranza, integrando la dichiarazione nello stato legittimo.
- [Fuori tolleranza] -> Servira' SANATORIA: art. 36 (se opera richiedeva PdC) o art. 36-bis (se opera richiedeva CILA/SCIA).

**Avvertenza**: per immobili vincolati, l'applicazione richiede **autorizzazione preventiva Soprintendenza**.
```

### Branch B - Sanatoria semplificata (art. 36-bis)

#### Passo B1 - Identifica titolo dovuto all'epoca e tipologia di abuso

L'art. 36-bis (introdotto dal Salva Casa) si applica a:
- **parziali difformita'** dal permesso di costruire o dalla SCIA alternativa al PdC, nelle ipotesi disciplinate dall'art. 34 DPR 380
- **variazioni essenziali** ex art. 32 DPR 380
- assenza o difformita' dalla **SCIA "ordinaria"** art. 22 (regime art. 37)

Per le opere realizzate in **assenza** o **totale difformita'** dal **permesso di costruire** o dalla **SCIA alternativa al PdC** resta il regime dell'**art. 36** (doppia conformita' piena).

Per le opere CILA-dovute realizzate senza CILA si applica il regime sanzionatorio specifico dell'**art. 6-bis co. 5** DPR 380 (sanzione pecuniaria, non procedimento art. 36-bis).

Domande all'utente:
- "Che intervento e' stato realizzato? (manutenzione, ristrutturazione, nuova costruzione, etc.)"
- "Quando e' stato realizzato? (anno)"
- "C'era un titolo originario o e' stato realizzato senza titolo / in difformita' parziale?"
- "L'abuso e' una **parziale** difformita' dal titolo (entro art. 34) oppure una **totale** difformita'/assenza?"

Applicare il regime in vigore all'epoca per determinare il titolo dovuto, poi incrociare con la tipologia di abuso:
- Opera **CILA-dovuta** realizzata senza CILA: art. 6-bis co. 5 (sanzione, no procedimento art. 36 ne' 36-bis)
- Opera **SCIA art. 22-dovuta** realizzata senza SCIA o in difformita': **art. 36-bis applicabile** (regime art. 37)
- Opera **PdC o SCIA alternativa-dovuta** in **parziale** difformita' (art. 34) o **variazione essenziale** (art. 32): **art. 36-bis applicabile**
- Opera **PdC o SCIA alternativa-dovuta** realizzata in **assenza** o **totale difformita'**: **art. 36** (doppia conformita' piena)
- Edilizia libera: nessuna sanatoria necessaria

#### Passo B2 - Doppia conformita' alleggerita

Verifica:
- **Conformita' urbanistica vigente al momento della presentazione della domanda di sanatoria** (PRG/PUC e regolamento edilizio attuali) - SI/NO
- **Conformita' edilizia vigente al momento della realizzazione** (DPR 380 e norme tecniche all'epoca della realizzazione) - SI/NO

Se entrambe SI -> sanatoria art. 36-bis applicabile.
Se almeno una NO -> sanatoria art. 36-bis NON applicabile. In tal caso valutare:
- L'opera resta abusiva e si applicano le sanzioni demolitorie (art. 31, 33, 34 DPR 380)
- E' praticabile la **regolarizzazione attraverso adeguamento** dell'opera per renderla conforme + nuova istanza di titolo edilizio
- Per casi di lieve difformita' parziale, valutare l'art. 34 (sanzioni alternative)

#### Passo B3 - Procedimento

- Istanza al Comune con relazione tecnica asseverata sulla doppia conformita' alleggerita
- Documentazione probante dell'epoca di realizzazione (foto storiche, ortofoto, atti, dichiarazioni sostitutive)
- Pagamento sanzione pecuniaria graduata (importo specifico nei regolamenti comunali, base nazionale art. 36-bis)
- Per immobili vincolati: **parere preventivo Soprintendenza** (sospende i termini fino al rilascio)
- **Termini procedimentali (art. 36-bis co. 6)**:
  - **Permesso in sanatoria**: 45 gg dalla presentazione; decorso il termine, "la richiesta si intende accolta" (**silenzio-assenso**)
  - **SCIA in sanatoria**: termine ex **art. 19 co. 6-bis L. 241/1990** (60 gg per i poteri inibitori)
  - Termini sospesi in caso di parere paesaggistico/MiC fino al rilascio

#### Passo B4 - Output Branch B

```markdown
## Verifica sanatoria art. 36-bis (Salva Casa)

**Opera realizzata**: [descrizione, anno]
**Titolo dovuto all'epoca**: [CILA / SCIA / PdC / nessuno]
**Conformita' urbanistica oggi**: [SI / NO / da-verificare]
**Conformita' edilizia all'epoca**: [SI / NO / da-verificare]

**Esito**:
- [Applicabile] -> Procedere con istanza art. 36-bis. Modulo "Sanatoria semplificata art. 36-bis" della modulistica unificata 2025. Allegati: vedi task `genera-elenco-allegati.md`.
- [Non applicabile] -> Valutare alternative: art. 36 (doppia conformita' piena) se opera era PdC-dovuta; oppure adeguamento dell'opera + nuova istanza; oppure sanzioni demolitorie.

**Sanzione pecuniaria**: graduata in base alla gravita' (rinvio regolamento comunale per importi specifici).

**Termini procedimento**: per il PdC in sanatoria 45 gg con **silenzio-assenso** (art. 36-bis co. 6 DPR 380); per la SCIA in sanatoria si applica il termine dell'**art. 19 co. 6-bis L. 241/1990**; in caso di vincolo, termini sospesi fino al parere Soprintendenza.
```

### Branch C - Cambio destinazione d'uso (art. 23-ter post Salva Casa)

#### Passo C1 - Categorie funzionali

Identifica:
- **Categoria attuale**: residenziale (a) / turistico-ricettiva (a-bis) / produttiva e direzionale (b) / commerciale (c) / rurale (d)
- **Categoria nuova prevista**
- **Zona urbanistica** dell'immobile (A / B / C / D / E)
- **UI singola** o **intero edificio**?
- **Opere** edilizie associate al cambio: assenti / CILA-art. 6-bis / SCIA art. 22 / PdC

#### Passo C2 - Decision tree post Salva Casa (art. 23-ter co. 1-bis, 1-ter, 1-quater, 1-quinquies)

| Caso | Regime |
|------|--------|
| **Stessa categoria** funzionale, qualunque zona | Sempre consentito (co. 1-bis); senza opere = nessun titolo (salvo condizioni comunali); con opere = regime delle opere |
| Categorie a/a-bis/b/c, **UI singola**, zone **A/B/C**, **senza opere** | **SCIA** ex art. 19 L. 241/1990 (co. 1-quinquies); no obblighi standard/parcheggi (co. 1-quater); eventuale contributo oneri di urbanizzazione secondaria |
| Categorie a/a-bis/b/c, UI singola, zone A/B/C, con opere a regime **CILA art. 6-bis** | **SCIA** ex co. 1-quinquies (assorbe la CILA) |
| Categorie a/a-bis/b/c, UI singola, zone A/B/C, con opere a regime **SCIA art. 22** | Regime delle opere = SCIA art. 22 |
| Categorie a/a-bis/b/c, UI singola, zone A/B/C, con opere a regime **PdC** | Regime delle opere = PdC (o SCIA alternativa al PdC) |
| Cambio coinvolgente **categoria d) rurale**, oppure zone **D / E** | Fuori dal regime semplificato co. 1-ter; regime ordinario in funzione delle opere e del titolo che sarebbe richiesto |
| Cambio non riferito a UI singola (intero edificio in cambio) | Verificare disciplina regionale e comunale specifica |

#### Passo C3 - Verifiche aggiuntive

- **Compatibilita' con la zona urbanistica e con la disciplina comunale**: il regime del co. 1-ter opera "fatte salve le condizioni stabilite dalla disciplina regionale e comunale". Verificare NTA del PRG/PUC e regolamento edilizio per condizioni aggiuntive (es. soglia di superficie minima, requisiti acustici/igienico-sanitari della categoria di destinazione).
- **Standard urbanistici**: per i cambi del co. 1-ter, **non scatta** l'obbligo di reperire ulteriori aree per servizi e di dotazione minima di parcheggi (co. 1-quater).
- **Oneri**: ove previsto dalla disciplina regionale, e' dovuto il **contributo per gli oneri di urbanizzazione secondaria** (co. 1-quater).
- **Vincoli sovraordinati**: paesaggio, beni culturali, idrogeologico, sismica restano dovuti come autorizzazioni accessorie.
- **Cambio a uso turistico-ricettivo (cat. a-bis)**: verificare la **legge regionale turismo** per i requisiti specifici della tipologia (numero camere, classificazione, posti letto).

#### Passo C4 - Output Branch C

```markdown
## Verifica cambio destinazione d'uso art. 23-ter (post Salva Casa)

**Categoria attuale**: [a / a-bis / b / c / d]
**Categoria nuova**: [a / a-bis / b / c / d]
**Stessa categoria**: [SI / NO]
**Opere edilizie**: [SI / NO]
**Zona urbanistica**: [A / B / C / D / E / F]
**Vincoli**: [paesaggio / MiC / nessuno]

**Esito**:
- Regime applicabile: [Edilizia libera / SCIA / PdC]
- Riferimento DPR 380: art. 23-ter [+ art. 22 / 10 in funzione del regime]
- Modulistica unificata: [modulo corrispondente]

**Avvertenze**:
- Verifica compatibilita' con PRG/PUC e regolamento edilizio comunale.
- Per centri storici (zona A): regime tipicamente piu' restrittivo, verificare con SUE.
- Vincoli paesaggistici/MiC: verificare se l'autorizzazione e' richiesta anche per cambio uso senza opere.
- Per attivita' commerciali: verificare anche la conformita' al D.Lgs. 114/1998 e LR commercio.
- Per cambio a uso turistico-ricettivo (a-bis): verificare LR turismo e regolamento comunale.
```

### Branch D - Stato legittimo (art. 9-bis)

#### Passo D1 - Verifica esistenza titoli

Domande all'utente:
- "Ci sono titoli abilitativi (LP / Concessione / DIA / SCIA / PdC) per la costruzione e per gli interventi successivi?"
- "Anno di costruzione dell'edificio?"
- "Comune ha avuto regolamento edilizio prima del 1/9/1967?"

#### Passo D2 - Determina regime probatorio

- **Titoli presenti**: stato legittimo = ultimo titolo + eventuali titoli successivi parziali (co. 1-bis).
- **Costruzione anteriore al 1/9/1967 in Comune privo di regolamento edilizio**: stato legittimo dimostrabile con documentazione probante (co. 1-ter).
- **Costruzione successiva al 1/9/1967 senza titolo**: opera **abusiva**, valutare sanatoria (Branch B).

#### Passo D3 - Documentazione probatoria (co. 1-ter)

Cataloga:
- Cartografia storica (catasto storico, IGM, ortofoto)
- Atti di provenienza (notarili) che descrivano l'immobile
- Contratti di vendita / divisioni con date verificabili
- Pagamenti di oneri pregressi
- Dichiarazioni sostitutive di atto notorio (per integrazioni)
- Foto storiche datate

#### Passo D4 - Output Branch D

```markdown
## Verifica stato legittimo art. 9-bis (Salva Casa)

**Anno di costruzione**: [...]
**Titoli abilitativi disponibili**: [...]
**Comune ha avuto regolamento edilizio prima del 1/9/1967**: [SI / NO / da-verificare]

**Esito**:
- [Stato legittimo accertato (co. 1-bis)] -> Riferimento: ultimo titolo + eventuali titoli parziali successivi.
- [Stato legittimo dimostrabile (co. 1-ter)] -> Allegare documentazione probante (lista sopra).
- [Stato legittimo non accertabile / opera abusiva post 1967] -> Valutare sanatoria (Branch B) prima di procedere con qualunque nuovo titolo.

**Effetto pratico**: senza accertamento dello stato legittimo, il tecnico abilitato NON puo' asseverare validamente la conformita' urbanistica. Lo stato legittimo va dichiarato come allegato di TUTTI i moduli edilizi.
```

### Branch E - Edilizia libera ampliata (art. 6 post Salva Casa)

#### Passo E1 - Identifica opera

Casi tipici di estensione dell'edilizia libera post Salva Casa:
- **VEPA** (Vetrate Panoramiche Amovibili) su balconi, logge, porticati - **art. 6 co. 1 lett. b-bis**: **edilizia libera** se amovibili e senza creazione di nuovo locale autonomamente utilizzabile (salvo regolamento condominiale + vincoli paesaggistici)
- **Tende, tende a pergola anche bioclimatiche, pergotende** - **art. 6 co. 1 lett. b-ter**: opere di protezione dal sole/agenti atmosferici con struttura principale costituita da tende, telo retrattile o elementi mobili/regolabili, **senza creazione di nuovo locale autonomamente utilizzabile**: edilizia libera
- **Cappotto termico esterno**: edilizia libera (con limiti tecnici di sporgenza dalla sagoma)
- **Pannelli solari/fotovoltaici a servizio dell'edificio**: edilizia libera (con condizioni rinnovabili)

> **NB - tettoie**: non sono liberalizzate in via generale dall'art. 6. Le tettoie stabili restano soggette a CILA / SCIA / PdC in funzione di dimensione, struttura e disciplina locale. Verificare il regolamento edilizio comunale e l'eventuale glossario opere libere (DM 2/3/2018).

#### Passo E2 - Verifica condizioni

Per ogni opera, verifica:
- **Amovibilita'** (no fondazioni, no opere edili stabili)
- **Non creazione di nuovo locale autonomamente utilizzabile** (no nuova SU)
- **Rispetto vincoli paesaggistici** (se in vincolo, autorizzazione paesaggistica anche per opere edilizia libera, salvo DPR 31/2017 All. A)
- **Rispetto regolamento condominiale** (per VEPA, tende su parti comuni)
- **Rispetto regolamento edilizio comunale** (puo' avere prescrizioni cromatiche, dimensionali in centri storici)

#### Passo E3 - Output Branch E

```markdown
## Verifica edilizia libera ampliata (art. 6 post Salva Casa)

**Opera**: [descrizione]
**Amovibilita'**: [SI / NO]
**Crea nuovo locale autonomamente utilizzabile**: [SI / NO]
**Vincoli paesaggistici**: [SI / NO / DPR 31/2017 All. A]
**Regolamento condominiale**: [conforme / da-verificare]
**Regolamento edilizio comunale**: [conforme / da-verificare]

**Esito**:
- [Edilizia libera] -> Nessun titolo edilizio richiesto. Eventuale comunicazione opere libere se richiesta da regolamento comunale.
- [CILA] -> Se non rispetta i requisiti dell'art. 6, ricade in regime CILA (vedi task `determina-regime-edilizio.md`).

**Avvertenza**: per immobili in vincolo paesaggistico, anche le opere art. 6 possono richiedere autorizzazione paesaggistica (verificare DPR 31/2017 All. A per liberalizzazioni).
```

### Passo finale - Output integrato

Se l'utente chiede una verifica multipla (es. tolleranze + sanatoria), produrre output con sezioni separate per ogni branch attivato.

Il report finale deve contenere:
1. Sintesi del caso
2. Branch attivati
3. Esiti specifici
4. **Effetto operativo** (cosa fare in pratica)
5. Avvertenze su regime transitorio / varianti regionali
6. Rinvio al SUE / tecnico abilitato

```markdown
# Verifica applicabilita' Salva Casa

**Data**: [oggi]
**Caso**: [sintesi]

## Branch attivati e esiti

[sezioni A/B/C/D/E come sopra]

## Effetto operativo

- **Cosa fare**: [...]
- **Cosa NON fare**: [...]

## Avvertenze

- Le **leggi regionali** possono integrare/derogare le norme nazionali (recupero sottotetti, distanze, paesaggio).
- I **regolamenti comunali** possono essere piu' restrittivi (es. zone vincolate, centri storici).
- Per **pratiche pendenti** prima del 28/7/2024 (entrata in vigore L. 105/2024), valutare il regime transitorio con il SUE.
- L'output non sostituisce **istruttoria SUE** ne' giudizio del **tecnico abilitato**.

**La presente verifica e' uno strumento di supporto e non sostituisce il giudizio del tecnico abilitato firmatario ne' l'istruttoria del SUE/SUAP.**
```

## Casi limite da gestire

### Tolleranza al limite (es. 4,9% su 200 mq SU, soglia 4%)

Se la difformita' e' molto vicina alla soglia (entro 0,5 punti %), segnalare l'incertezza e suggerire la **misura accurata** in cantiere prima di asseverare la tolleranza. Considerare anche se le tolleranze esecutive (co. 1-bis) si sommano alle dimensionali.

### Sanatoria art. 36-bis su immobile vincolato

Per opere abusive su immobili vincolati (D.Lgs. 42/2004 parte II/III), il **parere Soprintendenza** e' un pre-requisito. Se la Soprintendenza nega, la sanatoria art. 36-bis NON e' applicabile. Avvisare che la procedura puo' essere bloccata indipendentemente dalla doppia conformita'.

### Cambio destinazione d'uso da residenziale a uso turistico-ricettivo (B&B, casa vacanza, locazione breve)

Salva Casa ha agevolato questo cambio, ma ricadono spesso anche le LR (es. LR Toscana per locazioni turistiche) e i regolamenti comunali. Segnalare che oltre al regime edilizio (SCIA post Salva Casa) servono **autorizzazioni amministrative** specifiche (SUAP turismo, codice CIN nazionale L. 191/2023) come adempimenti separati.

### Stato legittimo per immobili rurali ante 1967

Per immobili rurali costruiti prima del 1/9/1967 in Comuni che NON avevano regolamento edilizio, lo stato legittimo si dimostra con documentazione (co. 1-ter). Tipicamente: catasto rurale storico, atti di acquisto, fotografie aeree IGM. Indicare al titolare di consolidare la documentazione PRIMA di richiedere qualunque nuovo titolo.

### Edilizia libera ma in zona vincolata

Anche se l'opera e' "edilizia libera" ai sensi dell'art. 6, in zona vincolata paesaggio (parte III D.Lgs. 42) puo' essere comunque richiesta **autorizzazione paesaggistica**, salvo che l'opera rientri nelle liberalizzazioni del DPR 31/2017 All. A. Verificare sempre il vincolo prima di concludere "nessun titolo".

## Limiti di questo task

- Verifica l'**applicabilita' nazionale** del Salva Casa, non integra **leggi regionali** specifiche.
- Non sostituisce l'**istruttoria SUE** ne' il **parere Soprintendenza**.
- Non valuta la **adeguatezza tecnica** dell'opera o della documentazione probante.
- Non emette **giudizi di sanabilita'** definitivi - rinvia all'istruttoria del Comune.
- Per **contenziosi pendenti** o **provvedimenti di demolizione** gia' emessi, rinviare al legale specializzato.

## Esempi

Vedi `examples/`:
- `sanatoria-semplificata-art36bis/` - applicazione sanatoria art. 36-bis a opera CILA-dovuta abusiva
- `cambio-uso-salva-casa-scia/` - cambio destinazione d'uso post Salva Casa con regime SCIA
