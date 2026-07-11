# Task: Verifica ammissibilita' del progetto al Piano Transizione 5.0

Inquadra il progetto di innovazione rispetto ai requisiti di ammissibilita' del Piano Transizione 5.0 (art. 38 DL 19/2024, DM 24/7/2024, circolare MIMIT 25877/2024). Restituisce un report strutturato di **conformita' / non conformita' / da-valutare** per ciascun requisito, con citazione precisa di articolo e comma e rinvio al certificatore.

## Obiettivo

Restituire all'utente:

- Esito sull'**ambito soggettivo**: l'impresa rientra fra i beneficiari? Ricade in cause di esclusione?
- Esito sull'**ambito oggettivo**: gli investimenti rientrano fra i beni agevolabili (Allegato A/B L. 232/2016, autoproduzione FER, formazione)?
- Esito su **avvio e completamento**: rispetto delle finestre temporali (1/1/2024 - 31/12/2025).
- Esito su **soglie di risparmio energetico** (preliminare, da confermare con calcolo dettagliato): riduzione >=3% struttura produttiva o >=5% processo interessato.
- Esito su **DNSH e attivita' escluse** (art. 5 DM): combustibili fossili, ETS oltre benchmark, discariche/inceneritori/TMB, rifiuti speciali pericolosi.
- Esito su **soggetto certificatore**: e' uno dei soggetti abilitati ex art. 15 co. 6 DM? La certificazione/iscrizione e' in corso di validita'?
- Esito su **terzieta'**: il certificatore e' indipendente rispetto all'impresa beneficiaria (Allegato III)?
- **Tetto** dei costi ammissibili: non oltre 50 mln EUR/anno per beneficiario.
- Lista di **elementi da approfondire** prima di passare al calcolo dei risparmi.

## Input richiesti

Variabili minime da raccogliere (chiedere se non fornite):

1. **Soggetto beneficiario**:
   - ragione sociale, P.IVA, CF;
   - residenza fiscale (Italia o stabile organizzazione in Italia);
   - forma giuridica, dimensione (PMI / grande impresa);
   - settore economico (codice ATECO);
   - eventuali procedure concorsuali in corso, sanzioni interdittive ex D.Lgs. 231/2001 o codice antimafia;
   - rispetto della normativa salute e sicurezza sul lavoro e dei contributi previdenziali/assistenziali.

2. **Investimenti**:
   - tipologia: beni materiali Allegato A L. 232/2016 / beni immateriali Allegato B / autoproduzione FER (no biomasse) / formazione personale;
   - importo stimato per categoria (in EUR);
   - data di avvio (primo impegno giuridicamente vincolante a ordinare i beni o impegno irreversibile);
   - data di completamento prevista (entro 31/12/2025);
   - localizzazione della struttura produttiva (regione, provincia, comune, dati catastali).

3. **Perimetro del programma di misura**:
   - struttura produttiva (sito, particelle catastali contigue, autonomia tecnica/funzionale/organizzativa)?
   - processo interessato (linea/processo che garantisce in autonomia la trasformazione input/output)?
   - su quale dei due si calcola la riduzione dei consumi (3% / 5%)?

4. **DNSH e attivita' escluse**:
   - l'attivita' rientra nell'ETS UE?
   - investimenti connessi a combustibili fossili, discariche, inceneritori, TMB, rifiuti speciali pericolosi?
   - schede DNSH applicabili (A, B, C, D, E, F1, F2 dell'Allegato VII circolare MIMIT)?

5. **Soggetto certificatore**:
   - ruolo: EGE / ESCo / ingegnere sez. A/B / perito industriale (sezione "meccanica ed efficienza energetica" o "impiantistica elettrica ed automazione");
   - numero certificazione / iscrizione albo, organismo di certificazione, data rilascio e validita';
   - dichiarazione di terzieta' (Allegato III): assenza di consulenza nei 3 anni precedenti, assenza di legami economici/familiari con l'impresa;
   - polizza assicurativa professionale (art. 15 co. 8 DM): si'/no, massimale.

6. **Cumuli e altre agevolazioni** (segnalazione, non valutazione di merito):
   - il progetto cumula con altre agevolazioni (Industria 4.0, ZES, contributi regionali)?

Se l'utente fornisce solo input parziali, **procedi con un report a piu' rami** che evidenzi i requisiti dipendenti dalle variabili mancanti.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dl-19-2024-art-38.md` - inquadramento del Piano e soglie minime
- `references/estratti/dm-24-07-2024-articoli-chiave.md` - articoli chiave del decreto attuativo (art. 4, 5, 6, 7, 8, 15, 18)
- `references/estratti/faq-mimit-soggetti-certificatori.md` - FAQ chiave MIMIT
- `references/estratti/circolare-mimit-criteri-risparmio.md` - sezione DNSH (cap. 4)
- `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md` - fase post-chiusura: credito 89,77% per le pratiche tecnicamente ammissibili

## Procedura

### Passo 1 - Inquadramento sintetico

Riassumi all'utente cio' che hai compreso del progetto:

> "Sto verificando l'ammissibilita' del progetto Transizione 5.0 per: [ragione sociale], settore [ATECO], investimenti [tipologie] per [importo EUR], avvio [data], completamento [data], perimetro su [struttura produttiva | processo interessato], certificatore [EGE/ESCo/ingegnere/perito]. Confermi?"

Se l'utente conferma, procedi. Se corregge, aggiorna l'inquadramento.

### Passo 2 - Verifica ambito soggettivo (art. 38 co. 1-2 DL 19/2024 + art. 3 DM)

Tabella di verifica:

| Requisito | Riferimento | Esito |
|---|---|---|
| Impresa residente in Italia o stabile organizzazione | art. 38 co. 1 DL | [Conforme / Non conforme / Da-verificare] |
| Indipendenza dalla forma giuridica, settore, dimensione, regime fiscale | art. 38 co. 1 DL | [Conforme] |
| Assenza procedure concorsuali (RD 267/1942, D.Lgs. 14/2019) | art. 38 co. 2 lett. a DL | [...] |
| Assenza sanzioni interdittive (D.Lgs. 231/2001, codice antimafia D.Lgs. 159/2011) | art. 38 co. 2 lett. b DL | [...] |
| Rispetto normativa sicurezza sul lavoro | art. 38 co. 2 lett. c DL | [...] |
| Rispetto obblighi contributivi (DURC) | art. 38 co. 2 lett. c DL | [...] |

### Passo 3 - Verifica ambito oggettivo (art. 4-8 DM 24/7/2024)

| Voce | Riferimento | Esito |
|---|---|---|
| Beni materiali Allegato A L. 232/2016, nuovi, strumentali, interconnessi | art. 6 co. 1 lett. a DM | [Conforme / Non conforme / Da-verificare] |
| Beni immateriali Allegato B L. 232/2016, nuovi, strumentali (con condizioni Energy Dashboarding per software gestione impresa) | art. 6 co. 1 lett. b DM | [...] |
| Esclusioni: art. 164 TUIR, ammortamento <6,5%, fabbricati, allegato 3 L. 208/2015, beni gratuitamente devolvibili | art. 6 + art. 1 co. 1053 L. 178/2020 | [...] |
| Autoproduzione FER per autoconsumo: non biomasse, localizzazione su particelle catastali della struttura o connessione POD esistente o medesima zona di mercato (autoconsumo a distanza) | art. 7 DM | [...] |
| Formazione: limite 10% dei beni A/B+FER, max 300.000 EUR, durata >=12 ore, esame finale, soggetti formatori abilitati, moduli A1-A4 + B1-B4 obbligatori | art. 8 DM | [...] |

> **Importante**: la riduzione minima dei consumi e' verificata **esclusivamente sugli investimenti sub a)** (beni 4.0). Gli investimenti FER e formazione **concorrono al credito d'imposta** ma non al calcolo della soglia 3%/5%.

### Passo 4 - Verifica avvio e completamento (art. 4 DM)

| Requisito | Riferimento | Esito |
|---|---|---|
| Avvio dal 1/1/2024 (primo impegno irreversibile) | art. 4 co. 3 DM | [...] |
| Completamento entro 31/12/2025 | art. 38 co. 4 DL + art. 4 co. 4 DM | [...] |
| Comunicazione preventiva al GSE prima dell'investimento (per prenotazione del credito) | art. 12 co. 1 DM | [...] |
| Comunicazione di avanzamento (con pagamento >=20% acconto) entro 30 giorni dalla conferma del credito prenotato | art. 12 co. 4 DM + FAQ MIMIT 2.11 | [...] |
| Comunicazione di completamento entro 28 febbraio 2026 | art. 12 + cap. 7 circolare MIMIT | [...] |

> **Nota vigenza (2026)**: le finestre temporali di questa tabella sono chiuse (completamento 31/12/2025, comunicazione di completamento 28/2/2026). Il task resta utilizzabile per verifiche retrospettive e in sede di controllo. Per le pratiche "tecnicamente ammissibili" rimaste senza copertura per esaurimento delle risorse, il credito e' riconosciuto nella misura dell'89,77% ex art. 8 DL 38/2026 (conv. L. 88/2026): vedi il caso limite dedicato e `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md`.

### Passo 5 - Verifica preliminare sulla soglia di risparmio (art. 9 DM)

> Verifica solo che il progetto **dichiari** una riduzione dei consumi compatibile con almeno una delle due soglie. Il calcolo dettagliato e' demandato al task `calcola-riduzione-consumi.md`.

| Soglia minima | Riferimento | Esito preliminare |
|---|---|---|
| Riduzione >=3% sui consumi della struttura produttiva | art. 38 co. 4 DL + art. 9 DM | [Dichiarata: si'/no] |
| Riduzione >=5% sui consumi del processo interessato | art. 38 co. 4 DL + art. 9 DM | [Dichiarata: si'/no] |
| Definizione del perimetro (struttura produttiva o processo interessato) coerente con il tipo di investimento | cap. 2.1 circolare MIMIT, esempi 1-4 | [Coerente / Da rivedere] |

> Una sola delle due soglie deve essere rispettata, non entrambe. Per la scelta del perimetro, consultare cap. 2.1 della circolare MIMIT 25877/2024 (estratto in `circolare-mimit-criteri-risparmio.md`).

### Passo 6 - DNSH e attivita' escluse (art. 5 + 18 DM, cap. 4 circolare)

Verifica la **non applicazione** delle clausole di esclusione:

| Esclusione | Eccezioni | Esito |
|---|---|---|
| Combustibili fossili (uso a valle) | uso temporaneo e tecnicamente inevitabile per transizione; macchine non stradali Stage I -> Stage V | [Conforme / Non conforme / Da-verificare] |
| Attivita' ETS sopra benchmark UE 2021/447 | proj. innov. senza impatto diretto su CO2 dell'attivita' o con emissioni inferiori al benchmark gratuito di riferimento | [...] |
| Discariche, inceneritori, TMB | proj. innov. su impianti esistenti con specifiche condizioni di efficienza/recupero materiali | [...] |
| Attivita' che generano elevate dosi di rifiuti speciali pericolosi | proj. innov. che non incrementano i rifiuti per unita' prodotta, etc. | [...] |

Schede DNSH applicabili (Allegato VII circolare):

- [ ] Scheda A - Acquisto/Leasing/Noleggio apparecchiature elettriche/elettroniche (obbligatoria se beni A/B);
- [ ] Scheda B - Servizi informatici di hosting e cloud (obbligatoria se applicabile);
- [ ] Scheda C - Produzione elettricita' da pannelli solari;
- [ ] Scheda D - Produzione elettricita' da energia eolica;
- [ ] Scheda E - Produzione elettricita' da energia idroelettrica;
- [ ] Scheda F1 - Produzione calore/freddo da geotermia;
- [ ] Scheda F2 - Produzione energia termica da pompe di calore.

### Passo 7 - Soggetto certificatore (art. 15 co. 6-8 DM)

| Requisito | Riferimento | Esito |
|---|---|---|
| Soggetto rientra fra: EGE UNI CEI 11339, ESCo UNI CEI 11352, ingegnere sez. A/B, perito industriale "meccanica ed efficienza energetica" / "impiantistica elettrica ed automazione" con esperienza in efficienza energetica processi produttivi | art. 15 co. 6 DM + FAQ MIMIT 2.3 | [Conforme / Non conforme] |
| Certificazione (per EGE/ESCo) o iscrizione albo (per ingegnere/perito) **in corso di validita'** | art. 15 co. 6 DM | [...] |
| Per EGE/ESCo: organismo di certificazione **accreditato Accredia** | art. 15 co. 6 lett. a/b DM | [...] |
| Polizza assicurativa professionale (idonea copertura RC) | art. 15 co. 8 DM | [...] |
| Dichiarazione di terzieta' (Allegato III): assenza consulenza/legami economici/familiari nei 3 anni precedenti | art. 15 co. 7 DM | [...] |

### Passo 8 - Tetto dei costi ammissibili (art. 4 DM)

| Vincolo | Riferimento | Esito |
|---|---|---|
| Costi ammissibili <= 50 mln EUR/anno per beneficiario | art. 4 + art. 38 co. 7 DL | [Compatibile] |
| Cumulo con altre agevolazioni (segnalazione) | art. 11 DM | [Da approfondire con consulente fiscale] |

### Passo 9 - Output

Produrre il report nel formato:

```markdown
# Verifica ammissibilita' Piano Transizione 5.0

**Data**: [oggi]
**Soggetto beneficiario**: [ragione sociale, P.IVA, CF]
**Settore**: [codice ATECO]
**Localizzazione struttura produttiva**: [regione, provincia, comune, dati catastali]
**Perimetro del programma di misura**: [struttura produttiva | processo interessato]
**Certificatore**: [EGE/ESCo/ingegnere/perito - n. cert/iscrizione]
**Importo investimenti previsti**: [tot EUR]
**Avvio**: [data] | **Completamento previsto**: [data]

## 1. Ambito soggettivo
[tabella esiti]

## 2. Ambito oggettivo
[tabella esiti]

## 3. Avvio e completamento
[tabella esiti]

## 4. Soglia di risparmio energetico (preliminare)
- soglia perseguita: [3% struttura | 5% processo]
- riduzione dichiarata ex ante: [X%]
- esito preliminare: [Conforme | Da confermare con calcolo]
[Rinvio a tasks/calcola-riduzione-consumi.md]

## 5. DNSH e attivita' escluse
[tabella esiti]
- schede DNSH applicabili: [...]

## 6. Soggetto certificatore
[tabella esiti]

## 7. Tetto costi ammissibili
[tabella esiti]

## 8. Esito complessivo
- [Ammissibile | Ammissibile con riserve | Non ammissibile]

## 9. Elementi da approfondire prima della certificazione ex ante
- [...]

## 10. Elementi non automaticamente verificabili dalla skill
- Sopralluogo fisico presso la struttura produttiva (richiesto dai modelli Allegato VIII / X)
- Verifica della validita' effettiva delle certificazioni EGE/ESCo presso Accredia
- Verifica dell'idoneita' della polizza assicurativa (massimale, copertura specifica per asseverazioni Transizione 5.0)
- Verifica della terzieta' dichiarata (assenza consulenza nei 3 anni precedenti)
- Conformita' tecnica dei beni agli allegati A/B L. 232/2016 (oggetto della perizia tecnica art. 16 DM, non di questa skill)
- Eventuali profili di **cumulo** con altre agevolazioni

## 11. Avvertenze e rinvio professionale
- L'esito e' generato sulla base delle variabili dichiarate; verificare con il consulente fiscale e con il revisore legale dei conti.
- La skill **non sostituisce** la perizia tecnica asseverata caratteristiche/interconnessione (art. 16 DM) ne' la certificazione contabile (art. 17 DM).
- La certificazione tecnica ex ante e' resa ai sensi degli artt. 46 e segg. DPR 445/2000 e degli artt. 359 e 481 c.p.: false dichiarazioni espongono a **responsabilita' penale aggravata** oltre che civile.
- Conservazione documentazione probatoria per 5 anni (art. 19 DM).

**La presente verifica di ammissibilita' e' uno strumento di supporto e non sostituisce il giudizio professionale del valutatore indipendente.**
```

## Casi limite da gestire

### Avvio del progetto antecedente al 1/1/2024
Non ammissibile (art. 38 co. 1 DL). Spiegare che il primo impegno giuridicamente vincolante a ordinare i beni deve essere stato assunto a partire dall'1/1/2024.

### Investimenti gia' completati
Verificare se il progetto e' stato completato prima della comunicazione preventiva. In tal caso si applica la **FAQ MIMIT 2.13**: e' comunque obbligatoria la comunicazione ex ante (con relativa certificazione), seguita dalla comunicazione ex post saltando la "Conferma 20%". Segnalare comunque l'inversione temporale.

### Beni di costo unitario inferiore a 300.000 EUR
Per la perizia tecnica caratteristiche/interconnessione (art. 16 DM) e' ammessa **autodichiarazione del legale rappresentante** in luogo della perizia di ingegnere/perito (FAQ MIMIT 2.4 e 2.12). Il rischio resta in capo al legale rappresentante. La skill segnala l'opzione ma non valuta l'idoneita' tecnica.

### ESCo come beneficiaria e certificatrice
Una ESCo puo' essere **beneficiaria** dell'incentivo per investimenti che realizza presso il cliente in EPC (FAQ MIMIT 2.15). Tuttavia, **non puo' essere contemporaneamente certificatrice del proprio progetto**: l'imparzialita' richiesta dall'Allegato III preclude l'identita' fra beneficiario e valutatore indipendente. Se il certificatore proposto e' una ESCo del medesimo gruppo del beneficiario, segnalare il **rischio di conflitto di interessi** e rinviare al MIMIT/GSE per la verifica formale.

### Attivita' ETS
Se l'impresa rientra nell'ETS UE, applicare il **filtro analitico** dell'art. 5 co. 1 lett. b DM: non basta dichiarare ETS, occorre verificare che le emissioni dirette previste al completamento non superino il benchmark UE 2021/447. Rinviare a Reg. UE 2021/447 e alle schede DNSH dell'Allegato VII.

### Cumulo con Industria 4.0 (4.0 vs 5.0)
Il Piano Transizione 5.0 non si cumula con il **credito d'imposta Industria 4.0** sul medesimo investimento (rinvio a chiarimenti MEF/Agenzia Entrate). Se l'impresa ha gia' beneficiato di Transizione 4.0 sui medesimi beni, segnalare **incompatibilita'** salvo verifica del consulente fiscale.

### Pratica "tecnicamente ammissibile" rimasta senza copertura (art. 8 DL 38/2026)
Se l'impresa ha presentato la comunicazione di completamento ex art. 38 co. 10 DL 19/2024 e ha ricevuto dal GSE la comunicazione che l'investimento risponde tecnicamente ai requisiti del DM 24/7/2024, nonche' dell'esaurimento delle risorse, non si tratta di inammissibilita': l'art. 8 DL 38/2026 (conv. con mod. L. 88/2026) riconosce un credito d'imposta pari all'**89,77%** del richiesto, riferito agli investimenti allegati A/B L. 232/2016 e alle spese di formazione (plafond 1.302,3 mln per il 2026), compensabile in F24 con **codice tributo 7079 entro il 31/12/2026**. Le spese di certificazione sono rimborsate pro quota tramite il **contributo del comma 3-bis** (decreto attuativo MIMIT non ancora pubblicato alla data di `last_verified`). I requisiti verificati da questo task restano rilevanti: l'art. 8 co. 3 richiama il DM 24/7/2024 "anche ai fini delle attivita' di controllo". Dettagli: `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md`.

## Limiti di questo task

- Genera la **verifica preliminare di ammissibilita'**, non un parere di accreditamento del beneficiario.
- Non valuta in concreto l'**idoneita' tecnica** dei beni agli allegati A/B L. 232/2016 (rinvio a perizia art. 16 DM).
- Non sostituisce la **certificazione contabile** ne' i pareri di prassi dell'Agenzia delle Entrate.
- Non gestisce le **modifiche normative successive** alla data di `last_verified` di `sources.yaml` (verificare aggiornamenti).

## Esempi

Vedi `examples/`:
- `conforme-investimento-3-2-mln/` - PMI manifatturiera, due macchine 4.0 + software MES + autoproduzione FV + formazione, riduzione 10,10% sul processo interessato (Fascia 2)
- `non-conforme-cogenerazione-fossili/` - Investimento in cogeneratore alimentato da gas naturale escluso da DNSH
