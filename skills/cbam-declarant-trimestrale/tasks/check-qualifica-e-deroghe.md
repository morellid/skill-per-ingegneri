# Verifica della qualifica e applicabilita' delle deroghe

## Obiettivo

Stabilire, per il soggetto e l'ambito merceologico forniti dall'utente:

1. se serve la **qualifica di dichiarante CBAM autorizzato** (Art. 4 + Art. 5 Reg. 2023/956);
2. se si applica una delle **esclusioni/esenzioni** del Capo I (Art. 2 §§3, 3bis, 4 e Art. 2bis);
3. quale **codice documento TARIC** dichiarativo va indicato per ciascuna importazione (Tabella 1 Circolare ADM 36/2025: Y128 / Y134 / Y135 / Y136 / Y137 / Y237 / Y238);
4. se e' applicabile la **deroga transitoria Art. 17 §7bis** (presentazione domanda entro 31/3/2026) e fino a quando;
5. le conseguenze dell'eventuale **mancanza di qualifica** (rinvio cross-cutting al task `assess-rischio-sanzionatorio.md`).

## Input richiesti

Chiedere all'utente:

1. **Identificazione del soggetto**:
   - tipologia: importatore stabilito UE / importatore non stabilito UE / rappresentante doganale indiretto (RDI);
   - EORI (eventuale) e Stato membro di stabilimento;
   - eventuale possesso di certificato **AEO** (Operatore Economico Autorizzato, Reg. UE 952/2013 Art. 38), perche' velocizza la domanda di autorizzazione (Art. 5 §5 lettera g bis ▼M1);
   - per RDI: nome/EORI dell'importatore rappresentato e suo Stato di stabilimento.

2. **Ambito merceologico previsto per l'anno civile in corso**:
   - settori CBAM coinvolti (ferro/acciaio, alluminio, fertilizzanti, cemento, elettricita', idrogeno - Allegato I del Reg. 2023/956);
   - **codici NC a 8 cifre** previsti e relativi quantitativi attesi in massa netta (per elettricita': MWh);
   - paesi di origine attesi;
   - eventuale uso di regime di **perfezionamento attivo** ex Art. 256 CDU.

3. **Stato della domanda di autorizzazione** (se applicabile):
   - presentata? data di presentazione? nel registro CBAM?
   - se gia' rilasciata: **numero di conto CBAM** (formato `CBAM-XX-YYYY-AAANNNNNNNNNNN`);
   - se in valutazione: l'autorita' competente ha attivato la consultazione facoltativa di altre autorita' (Art. 17 §1 ▼M1, max 15 giorni civili)?
   - presenza dei due esercizi finanziari precedenti? In caso negativo, prevista garanzia ex Art. 17 §5 ▼M1.

4. **Origine delle merci**:
   - origine UE (per coerenza con codice Y237)?
   - origine territori Allegato III punto 1 (Islanda, Liechtenstein, Norvegia, Svizzera, Busingen, Helgoland, Livigno, Ceuta/Melilla con condizioni Art. 2 §6)?
   - merci destinate ad attivita' militari ex Art. 1 punto 49 Reg. del. 2015/2446?
   - elettricita' o idrogeno da piattaforma continentale / ZEE di SM o di paesi Allegato III punti 1-2?

## Fonti

- Trascrizione integrale degli articoli rilevanti del Reg. 2023/956 consolidato in `references/fonti/reg-ue-2023-956-cbam-consolidato.md`.
- Estratti curati in:
  - `references/estratti/reg-ue-2023-956-articoli-fase-definitiva.md` sezioni A (ambito, soglie) e B (qualifica e autorizzazione);
  - `references/estratti/reg-ue-2025-2083-considerando-chiave.md` considerando 2-13 (ratio dell'esenzione de minimis + monitoraggio soglia + deroga transitoria);
  - `references/estratti/circ-adm-36-2025-codici-taric.md` (tabella codici, formalismo Y128, regole operative).

Articoli da citare:

- **Art. 2** §§1-4 (ambito), **Art. 2 §3 ▼M1** (militari -> Y135), **Art. 2 §3bis ▼M1** (elettricita'/idrogeno piattaforma continentale -> Y136), **Art. 2 §4** (territori Allegato III -> Y134).
- **Art. 2bis ▼M1** + **Allegato VII punto 1** (esenzione de minimis, soglia 50 t -> Y137; Art. 2bis §4 esclude elettricita' e idrogeno).
- **Art. 3 punto 15 ▼M1** (definizione di importatore, conto di appuramento).
- **Art. 4** (importazione solo da dichiarante CBAM autorizzato).
- **Art. 5 §§1, 1bis, 1ter, 2, 2bis ▼M1** (chi e quando deve chiedere la qualifica).
- **Art. 5 §5 lettera g bis ▼M1** (AEO accelera).
- **Art. 17 §§1, 5, 7, 7bis ▼M1** (procedimento + deroga transitoria + garanzia).
- **Allegato III punto 1** (territori esclusi); **Allegato VII punto 1** (soglia 50 t).
- **Circolare ADM 36/2025** Tabella 1 (Y128, Y134-Y137, Y237, Y238) + nota 10 (formalismo Y128).

## Procedura

### Passo 1 - Stabilire se il soggetto rientra nell'ambito (Art. 2 §1)

Se le merci attese **non** sono di Allegato I (verifica spettante al dichiarante via classificazione doganale), il CBAM non si applica. Avvertire che la skill non determina caso per caso il matching codice NC -> Allegato I.

### Passo 2 - Verificare le esclusioni del Capo I

Per ciascuna combinazione (NC, origine, uso):

| Condizione                                                                  | Esclusione                       | TARIC |
|-----------------------------------------------------------------------------|----------------------------------|-------|
| Origine territori Allegato III punto 1 (Islanda, Liechtenstein, Norvegia, Svizzera; Busingen, Helgoland, Livigno, e Ceuta/Melilla con Art. 2 §6) | Art. 2 §4                        | Y134  |
| Uso militare ex Art. 1 punto 49 Reg. del. 2015/2446                         | Art. 2 §3 ▼M1                    | Y135  |
| Elettricita' o idrogeno da piattaforma continentale / ZEE di SM o paesi Allegato III punti 1-2 | Art. 2 §3bis ▼M1                  | Y136  |
| Merci di origine UE che altrimenti rientrerebbero in Allegato I             | (no esclusione formale, ma codice di gestione doganale) | Y237  |

Se nessuna delle precedenti, proseguire al Passo 3.

### Passo 3 - Verificare l'esenzione de minimis (Art. 2bis ▼M1)

Soglia: **50 tonnellate** di massa netta cumulativa in un anno civile (Allegato VII punto 1), considerata sul totale di ferro/acciaio + alluminio + fertilizzanti + cemento (**non** elettricita' ne' idrogeno - Art. 2bis §4).

Classificare il caso:

- **Importatore strutturalmente sotto soglia** (es. < 50 t/anno con margine ampio):
  - non occorre essere autorizzati per la maggior parte delle operazioni;
  - codice TARIC: **Y137** (Circolare 36/2025 Tabella 1);
  - se il soggetto e' un **RDI**, deve **comunque** essere autorizzato (Art. 5 §1bis ▼M1) anche se l'importatore rappresentato e' esentato;
  - segnalare il rischio di **superamento in corso d'anno**: Art. 2bis §2 ▼M1 fa scattare gli obblighi su **tutte** le emissioni dell'anno; Art. 5 §1ter ▼M1 richiede di presentare la domanda **prima** del superamento (Considerando 10 Reg. 2025/2083).
- **Importatore sopra soglia o che prevede di superarla**:
  - serve la qualifica di dichiarante CBAM autorizzato (Art. 4 + Art. 5 §1 / §1bis / §1ter ▼M1);
  - codice TARIC: **Y128** (numero di conto CBAM) se autorizzato; **Y238** se domanda presentata entro 31/3/2026 e ancora in valutazione (vedi Passo 5);
  - segnalare il **monitoraggio Art. 25bis ▼M1**: la Commissione trasmette periodicamente alla autorita' competente la lista degli importatori che superano **il 90 % della soglia** (Considerando 9 Reg. 2025/2083).
- **Importatore non stabilito UE**:
  - non puo' essere dichiarante CBAM autorizzato direttamente; serve un **RDI** che si assuma la qualifica (Art. 5 §2 ▼M1).

### Passo 4 - Determinare il codice TARIC per ciascuna importazione

Procedere per esclusione, dall'alto verso il basso:

1. Y134 (origine territori Allegato III pt. 1);
2. Y135 (uso militare);
3. Y136 (elettricita'/idrogeno piattaforma continentale/ZEE);
4. Y237 (origine UE);
5. Y137 (sotto soglia de minimis - Art. 2bis);
6. Y238 (deroga transitoria - vedi Passo 5);
7. Y128 (dichiarante autorizzato, regola ordinaria).

Per Y128 verificare il **formalismo** (Circolare 36/2025 nota 10):

```
CBAM-XX-YYYY-AAANNNNNNNNNNN
```

dove `XX` = codice paese (es. `IT`), `YYYY` = anno corrente, `AAA` = sequenza 3 caratteri alfabetici, `NNNNNNNNNNN` = 11 cifre. Nel messaggio Hx: `<Type>Y128</Type>`, `<ReferenceNumber>YYYY-XX- CBAM-XX-YYYY-AAANNNNNNNNNNN</ReferenceNumber>`.

### Passo 5 - Verificare la deroga transitoria Art. 17 §7bis ▼M1

Se l'utente ha presentato domanda **entro il 31 marzo 2026** e l'autorita' competente non ha ancora deciso:

- usabile temporaneamente il codice **Y238** fino alla decisione e **comunque non oltre il 27 settembre 2026**;
- se la domanda viene respinta: l'autorita' determina entro un mese le emissioni del periodo 1/1/2026 - data della decisione, sulla base delle informazioni Art. 25 §3 e dei valori predefiniti Allegato IV; queste emissioni alimentano il calcolo sanzionatorio Art. 26 §2bis (rinvio a `assess-rischio-sanzionatorio.md`).

Se la domanda e' stata presentata **dopo il 31/3/2026**, la deroga **non si applica**: si rimane non autorizzati con esposizione Art. 25 §1 (blocco/rifiuto sdoganamento) + Art. 26 §2 (3-5x sanzione §1) o §2bis se sopra soglia.

### Passo 6 - Verificare obblighi del RDI (Considerando 7-8 Reg. 2025/2083)

Se il soggetto e' un RDI:

- **deve** essere autorizzato prima di accettare un incarico CBAM, **anche se** l'importatore rappresentato e' esentato Art. 2bis (Art. 5 §1bis ▼M1);
- **se l'importatore rappresentato supera la soglia ed e' rappresentato da piu' RDI**: ciascun RDI presenta dichiarazione CBAM **per le merci da esso importate** (comprese quelle sotto soglia) e restituisce i certificati (Considerando 7 Reg. 2025/2083);
- e' soggetto agli **stessi obblighi e sanzioni** dell'importatore (Art. 5 §2bis ▼M1; Considerando 8); eccezione: non e' sanzionato se non ha accettato di agire come dichiarante per un importatore stabilito UE.

### Passo 7 - Produrre il report

Strutturare un report markdown con:

1. **Profilo del soggetto** (tipologia, EORI, AEO si/no, eventuale numero di conto CBAM).
2. **Tabella decisionale per codice TARIC** per ciascuna combinazione (NC, origine, uso) elencata dall'utente.
3. **Verifica qualifica**: necessaria si/no, motivazione (Art. 4 + Art. 5 §X), eventuale obbligo di garanzia (Art. 17 §5 ▼M1).
4. **Deroga Art. 17 §7bis**: applicabile? scadenza (27/9/2026 al piu' tardi)? rischio in caso di diniego (rinvio a `assess-rischio-sanzionatorio.md`).
5. **Punti che richiedono giudizio del professionista**: matching NC -> Allegato I, qualificazione di importazioni miste / perfezionamenti attivi/passivi / reintroduzioni ex Circolare ADM 36/2025, pratiche di elusione (Art. 27 §2 lettera b).
6. **Avvertenza** standard (vedi processo generale SKILL.md punto 6).

## Output atteso

Report markdown di 1-3 pagine con:

- intestazione (soggetto, EORI, data dell'analisi, ambito merceologico sintetico);
- tabella codici TARIC riga-per-riga;
- box "qualifica si/no/condizionata" con articolo motivante;
- box "deroga 17 §7bis" se applicabile;
- elenco "professionista deve verificare" + avvertenza finale + rinvio a `references/fonti/reg-ue-2023-956-cbam-consolidato.md` e `references/fonti/circ-adm-36-2025-cbam.md` per riscontro testuale.
