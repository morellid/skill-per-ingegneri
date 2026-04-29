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

| Superficie utile (SU) | Tolleranza % |
|------------------------|--------------|
| Fino a 60 mq | 6% |
| Da 60 a 100 mq | 5% |
| Da 100 a 300 mq | 4% |
| Da 300 a 500 mq | 3% |
| Oltre 500 mq | 2% (regime pre-Salva Casa) |

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

#### Passo B1 - Identifica titolo dovuto all'epoca

L'art. 36-bis si applica **solo** a opere che, all'epoca della loro realizzazione, sarebbero state assoggettate a **CILA o SCIA** (non PdC).

Domande all'utente:
- "Che intervento e' stato realizzato? (manutenzione, ristrutturazione, nuova costruzione, etc.)"
- "Quando e' stato realizzato? (anno)"
- "C'era un titolo originario o e' stato realizzato senza titolo / in difformita' parziale?"

Applicare il regime in vigore all'epoca per determinare il titolo dovuto:
- **CILA o SCIA** -> art. 36-bis applicabile
- **PdC** -> art. 36 (doppia conformita' piena, NON si applica art. 36-bis)
- Edilizia libera -> nessuna sanatoria necessaria

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
- Per immobili vincolati: **parere preventivo Soprintendenza**
- **Termine**: 45 gg per provvedimento espresso. **Silenzio-rifiuto** (no silenzio-assenso).

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

**Termini procedimento**: 45 gg, silenzio-rifiuto.
```

### Branch C - Cambio destinazione d'uso (art. 23-ter post Salva Casa)

#### Passo C1 - Categorie funzionali

Identifica:
- **Categoria attuale**: residenziale (a) / turistico-ricettiva (a-bis) / produttiva e direzionale (b) / commerciale (c) / rurale (d)
- **Categoria nuova prevista**

#### Passo C2 - Decision tree post Salva Casa

| Caso | Regime |
|------|--------|
| Stessa categoria, no opere | Edilizia libera (salvo regolamento comunale) |
| Stessa categoria, con opere | Regime delle opere |
| Categorie diverse, no opere, fuori zona A | **SCIA** (post Salva Casa, ampliato) |
| Categorie diverse, con opere, fuori zona A | Regime piu' alto fra opere e cambio |
| Centro storico (zona A) | Regime piu' restrittivo, generalmente PdC |

#### Passo C3 - Verifiche aggiuntive

- **Compatibilita' con la zona urbanistica**: il cambio uso non deve violare il PRG/PUC. Es: cambio da residenziale a commerciale ammesso in zona B/C/D, ma non in zona E (agricola).
- **Dotazione standard**: il cambio non deve generare un aumento del carico urbanistico oltre la dotazione standard ammessa (DM 1444/1968 art. 3 e ss.).
- **Vincoli sovraordinati**: paesaggio, beni culturali possono limitare il cambio.
- **Regolamento edilizio comunale**: puo' essere piu' restrittivo (es. tutela commerciale dei centri storici, vincolo ricettivo).

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
- **VEPA** (Vetrate Panoramiche Amovibili) su balconi/logge: **edilizia libera** (salvo regolamento condominiale + vincoli paesaggistici)
- **Tende, pergolati, tettoie a protezione del sole** di limitate dimensioni e amovibili: edilizia libera
- **Cappotto termico esterno**: edilizia libera (con limite tecnici di sporgenza dalla sagoma)
- **Pannelli solari/fotovoltaici a servizio dell'edificio**: edilizia libera (con condizioni post-rinnovabili)

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
