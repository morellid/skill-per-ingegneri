# Redazione della dichiarazione CBAM annuale (Art. 6)

## Obiettivo

Strutturare la **dichiarazione CBAM annuale** del dichiarante CBAM autorizzato ex Art. 6 Reg. 2023/956, da presentare nel registro CBAM **entro il 30 settembre** dell'anno successivo all'anno civile di importazione, con **prima applicazione nel 2027 per l'anno civile 2026** (Art. 6 §1 ▼M1).

La skill produce una **check-list di contenuti obbligatori**, un confronto fra le informazioni gia' disponibili presso il dichiarante e quanto richiesto dall'Art. 6 §2 ▼M1 (lettere a-d), un elenco delle verifiche di coerenza con le dichiarazioni doganali (Hx) e con i codici TARIC dichiarati, e una mappa degli elementi che richiedono **verifica accreditata** ex Art. 8 §1 ▼M1.

La skill **non** redige il deposito finale: tutti gli output sono lavorabili (markdown / tabelle) e devono essere validati dal responsabile compliance / consulente CBAM prima dell'inserimento nel registro CBAM.

## Input richiesti

Chiedere all'utente:

1. **Anno civile di importazione oggetto della dichiarazione** (per la prima applicazione: 2026).
2. **Identificativi del dichiarante**:
   - numero di conto CBAM (formato `CBAM-XX-YYYY-AAANNNNNNNNNNN`);
   - EORI, sede di stabilimento, eventuale AEO;
   - se RDI: EORI dell'importatore rappresentato (e, in caso di rappresentanze multiple per lo stesso importatore, lista dei RDI - vedi Considerando 7 Reg. 2025/2083).
3. **Estratto delle dichiarazioni doganali Hx dell'anno**: lista di operazioni con NC, paese di origine, quantita' (massa netta in tonnellate / MWh per elettricita'), data, codice TARIC dichiarato (Y128 / Y134-Y238). Servono per:
   - calcolare il **quantitativo totale** Art. 6 §2 lettera a ▼M1, **comprese le merci sotto soglia** (vedi nota sotto);
   - controllo incrociato con Art. 25 §2 ▼M1 (le autorita' doganali comunicano alla Commissione le stesse informazioni; il registro CBAM effettua **cross-check**).
4. **Documentazione sulle emissioni incorporate**:
   - se metodo emissioni effettive (Art. 7 §2 lettera a + Allegato IV punti 2-3): dati del gestore dell'impianto in paese terzo + **relazione di verifica del verificatore accreditato** ex Art. 8 §1 ▼M1 + Allegato VI;
   - se metodo valori predefiniti (Art. 7 §2 lettera b + Allegato IV punto 4.1): non occorre verifica accreditata; usare i valori pubblicati dalla Commissione (con maggiorazione applicata nella dichiarazione annuale).
5. **Documentazione per la detrazione del carbon price paese terzo** (Art. 9 ▼M1), se applicabile:
   - prove di pagamento, riferimenti normativi del paese terzo, certificazione da **persona indipendente** (con nome e recapiti su documento);
   - in alternativa: ricorso ai **prezzi predefiniti annuali del carbonio** calcolati dalla Commissione (Art. 9 §4 ▼M1, disponibili dal 2027) - obbligatorio se emissioni dichiarate via valori predefiniti.
6. **Adeguamento per assegnazione gratuita** (Art. 31): dato fornito dall'utente (la skill non lo calcola).
7. **Eventuale delega** della presentazione a terzo con EORI + stabilimento UE (Art. 5 §7bis ▼M1, introdotto dall'Omnibus). Il dichiarante resta **responsabile** anche se la presentazione e' delegata.

## Fonti

- Trascrizione integrale degli articoli rilevanti del Reg. 2023/956 consolidato in `references/fonti/reg-ue-2023-956-cbam-consolidato.md`.
- Estratto curato in `references/estratti/reg-ue-2023-956-articoli-fase-definitiva.md` sezione C (Dichiarazione CBAM e calcolo emissioni).
- Ratio dell'inserimento delle merci sotto soglia nel quantitativo dichiarato + delega + persona indipendente: `references/estratti/reg-ue-2025-2083-considerando-chiave.md` considerando 7, 14-15, 19-22.
- Coerenza dichiarazione CBAM <-> operazioni doganali: `references/estratti/circ-adm-36-2025-codici-taric.md` paragrafo "Coerenza con dichiarazione CBAM (Art. 6)".

Articoli da citare:

- **Art. 6 §1 ▼M1** (termine 30/9, prima volta 2027 per 2026).
- **Art. 6 §2 ▼M1** lettere a-d (contenuto della dichiarazione).
- **Art. 6 §6 ▼M1** (delega a terzo con EORI + stabilimento UE).
- **Art. 7 §§2, 5 ▼M1** (emissioni effettive vs valori predefiniti; conservazione registrazioni Allegato V).
- **Art. 8 §1 ▼M1** (verifica solo per emissioni effettive).
- **Art. 9 §§1-4 ▼M1** (detrazione carbon price paese terzo).
- **Allegato IV punto 4.1 ▼M1** (valori predefiniti).
- **Allegato V** (registrazioni da conservare).
- **Allegato VI** (principi di verifica).
- **Art. 22 §1 ▼M1** (restituzione certificati entro 30/9, in concomitanza con la dichiarazione).
- **Art. 25 §§2-3 ▼M1** (controllo incrociato con dati doganali).

## Procedura

### Passo 1 - Verificare la legittimazione a presentare la dichiarazione

Solo il **dichiarante CBAM autorizzato** presenta la dichiarazione (Art. 6 §1 ▼M1). Casi speciali:

- **RDI**: presenta la dichiarazione per le merci da lui importate per conto dell'importatore rappresentato (anche se quest'ultimo e' esentato Art. 2bis, le merci sotto soglia restano da rendicontare - Considerando 7 Reg. 2025/2083 e Art. 6 §2 lettera a ▼M1 "comprese le merci sotto soglia").
- **Importatore con qualifica revocata / non rilasciata (Art. 17 §7bis respinta)**: non presenta la dichiarazione - la sanzione Art. 26 §2bis ▼M1 **dispensa** dall'obbligo di presentare la dichiarazione e restituire i certificati (rinvio a `assess-rischio-sanzionatorio.md`).
- **Delega**: e' possibile delegare la presentazione a un terzo con EORI e stabilimento UE (Art. 5 §7bis e Art. 6 §6 ▼M1); il dichiarante resta responsabile.

### Passo 2 - Strutturare il quantitativo totale (Art. 6 §2 lettera a ▼M1)

Per ciascun **tipo di merci** (codice NC raggruppato per famiglia di Allegato I) e ciascun **paese di origine**, indicare:
- quantitativo totale: **MWh** per elettricita', **tonnellate** (massa netta) per le altre merci CBAM;
- **comprese le merci sotto soglia** (Art. 2bis): la dichiarazione contiene tutte le importazioni dell'anno, non solo quelle che hanno fatto scattare la qualifica.

Tabella raccomandata:

| Codice NC | Famiglia Allegato I | Paese di origine | Quantita' (t / MWh) | Codice TARIC usato in dogana | Note |
|-----------|---------------------|------------------|---------------------|------------------------------|------|

Riconciliare le righe con l'estratto Hx (Art. 25 §2 ▼M1): la Commissione effettua cross-check automatici.

### Passo 3 - Calcolare le emissioni totali incorporate (Art. 6 §2 lettera b ▼M1)

Per ciascuna combinazione (NC, paese di origine):

- **se metodo emissioni effettive** (Art. 7 §2 lettera a + Allegato IV pt. 2-3): valore dichiarato dal gestore impianto paese terzo, **verificato da verificatore accreditato** ex Art. 8 §1 ▼M1; copie della relazione di verifica e di Allegato VI vanno allegate (Art. 6 §2 lettera d ▼M1);
- **se metodo valori predefiniti** (Art. 7 §2 lettera b + Allegato IV pt. 4.1): valore predefinito pubblicato dalla Commissione, comprensivo della **maggiorazione proporzionale** (atti di esecuzione Art. 7 §7); se manca il valore del paese specifico, si applica l'intensita' media dei **10 paesi esportatori** con le intensita' di emissione piu' elevate (Allegato IV pt. 4.1 ▼M1 + considerando 35 Reg. 2025/2083).

Formula Allegato IV pt. 4.1: `SEEg = (AttrEmg + EEInpMat) / ALg`, dove `EEInpMat = sum(Mi * SEEi)` per i precursori `i` di Allegato I provenienti da paesi non esenti.

**Avvertenza**: la skill non calcola emissioni effettive (richiede dati impianto + verifica). Se l'utente segnala emissioni effettive, la skill richiede la **relazione di verifica** e si limita a controllare la coerenza tra il numero dichiarato e i precursori indicati.

### Passo 4 - Calcolare il numero totale di certificati da restituire (Art. 6 §2 lettera c ▼M1)

```
N_cert_da_restituire = ceiling( E_tot - detrazione_Art9 - adeguamento_Art31 )
```

dove:
- `E_tot` = emissioni totali incorporate dell'anno (Passo 3);
- `detrazione_Art9` = certificati corrispondenti al carbon price effettivamente pagato in paese terzo (Art. 9 §1 ▼M1; documentazione Art. 9 §2; certificazione persona indipendente; conservazione 4 anni Art. 9 §3);
- `adeguamento_Art31` = adeguamento per assegnazione gratuita ETS (Art. 31 - fuori scope di calcolo skill, dato dall'utente).

Per la detrazione: se emissioni dichiarate via valori predefiniti, la riduzione e' applicabile **solo** via prezzi predefiniti annuali pubblicati dalla Commissione (Art. 9 §4 ▼M1 + considerando 21 Reg. 2025/2083). Precursori gia' soggetti a EU ETS o sistema collegato non rientrano (considerando 18, 21).

### Passo 5 - Allegare la documentazione (Art. 6 §2 lettera d + Allegato VI)

Per ogni combinazione (NC, paese) dichiarata via emissioni effettive: copia della relazione di verifica + dati di Allegato VI (principi di verifica). Conservare in azienda gli elementi di Allegato V (registrazioni - Art. 7 §5 ▼M1).

### Passo 6 - Coerenza con dichiarazione doganale (Circolare ADM 36/2025)

Verificare riga per riga la coerenza tra dichiarazione CBAM e operazioni doganali. Ricordare la citazione testuale della Circolare 36/2025: *"Le informazioni da fornire ai sensi dell'art. 6 ('Dichiarazione CBAM') dovranno sempre essere coerenti con le operazioni doganali svolte e, pertanto, correttamente rendicontate dai soggetti dichiaranti e/o rappresentanti, anche in caso di perfezionamenti attivi e passivi o di reintroduzioni di merce CBAM o di prodotti trasformati partendo da merce CBAM"*.

Segnalare al professionista i casi di:
- perfezionamento attivo (Art. 256 CDU) - rientra nell'ambito (Art. 2 §1 Reg. CBAM);
- perfezionamento passivo / reintroduzioni - **giudizio del professionista**;
- operazioni con Y238 (deroga 17 §7bis): se domanda accolta dopo la presentazione della dichiarazione provvisoria, occorre re-dichiarare con Y128.

### Passo 7 - Punti che richiedono giudizio del professionista

Elencare esplicitamente:

- scelta del metodo (effettive vs predefinite) per ciascuna combinazione (NC, paese);
- accettazione del livello di **verifica accreditata** ricevuta (Art. 8 §1) e gestione degli scostamenti tra dato verificato e dato del gestore;
- determinazione dell'**adeguamento Art. 31** in base agli atti di esecuzione vigenti al momento della presentazione;
- documentazione Art. 9 (carbon price paese terzo) e scelta della **persona indipendente** che certifica;
- riconciliazione delle merci **sotto soglia** (Art. 2bis) col quantitativo Art. 6 §2 lettera a;
- gestione di perfezionamenti / reintroduzioni / Y238 (Circolare ADM 36/2025).

## Output atteso

Report markdown strutturato con:

1. **Intestazione** (dichiarante, numero conto CBAM, anno civile di riferimento, termine di presentazione = 30/9/AAAA+1).
2. **Tabella quantitativi** (Art. 6 §2 lettera a) per NC + paese + quantita' + codice TARIC + note.
3. **Tabella emissioni** (Art. 6 §2 lettera b) per NC + paese + metodo (effettive/predefiniti) + valore + relazione di verifica si/no.
4. **Calcolo certificati** (Art. 6 §2 lettera c) con scomposizione `E_tot`, detrazione Art. 9, adeguamento Art. 31, numero finale.
5. **Allegati** (Art. 6 §2 lettera d) - elenco relazioni di verifica + documentazione carbon price.
6. **Check-list coerenza Hx** (Circolare ADM 36/2025).
7. **Punti che richiedono giudizio del professionista** (vedi Passo 7).
8. **Avvertenza standard** + rinvio a `references/fonti/reg-ue-2023-956-cbam-consolidato.md` per il riscontro testuale di Art. 6, 7, 8, 9.
