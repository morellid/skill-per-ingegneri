# Task: Determina regime edilizio e modulo unificato

Restituisce il modulo edilizio nazionale unificato (Edilizia libera, CILA, SCIA, SCIA alternativa al PdC, Permesso di Costruire) corretto per un intervento, con citazione precisa di articolo del DPR 380/2001 e voce della Tabella A del D.Lgs. 222/2016, integrato dalle modifiche del Salva Casa.

## Obiettivo

Restituire all'utente:
- Il **modulo unificato** corrispondente all'intervento (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / Permesso di Costruire / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis)
- La **citazione normativa**: articolo + comma + lettera del DPR 380, voce/sezione della Tabella A D.Lgs. 222/2016
- Le **eventuali alternative** (es. ristrutturazione pesante = PdC oppure SCIA alternativa a scelta del titolare)
- I **pre-requisiti** o autorizzazioni a monte (paesaggistica, MiC, sismica, idrogeologica)
- Un set di **avvertenze** su casi al limite e rinvii al SUE / regolamento edilizio comunale

## Input richiesti

Variabili minime da raccogliere all'inizio (chiedere all'utente se non fornite):

1. **Tipologia intervento** (rinvio art. 3 DPR 380):
   - Manutenzione ordinaria (lett. a)
   - Manutenzione straordinaria (lett. b)
   - Restauro / risanamento conservativo (lett. c)
   - Ristrutturazione edilizia (lett. d)
   - Nuova costruzione (lett. e)
   - Ristrutturazione urbanistica (lett. f)
   - Cambio destinazione d'uso senza opere (rinvio art. 23-ter)
   - Variante in corso d'opera (specificare titolo originario)
   - Sanatoria di opere gia' eseguite (specificare se si tratta di art. 36 o art. 36-bis Salva Casa)

2. **Immobile**: esistente / nuova edificazione su suolo libero. Se esistente, **stato legittimo accertato?** (art. 9-bis DPR 380, rinvio Salva Casa).

3. **Parti strutturali coinvolte**: si / no. (Discrimina CILA da SCIA per manutenzioni straordinarie e restauri).

4. **Modifiche** all'organismo edilizio: si/no per
   - Volumetria complessiva
   - Sagoma / sedime
   - Prospetti
   - Numero unita' immobiliari (frazionamento o accorpamento)
   - Destinazione d'uso (urbanisticamente rilevante)

5. **Vincoli sovraordinati**:
   - Paesaggistico (D.Lgs. 42/2004 parte III)
   - Beni culturali (D.Lgs. 42/2004 parte II)
   - Idrogeologico (R.D. 3267/1923)
   - Sismico (DPR 380 capo IV o regimi semplificati LR)
   - Idraulico / esondazione

6. **Zona urbanistica** (PRG/PUC): A (centro storico) / B (consolidato) / C (espansione) / D (produttiva) / E (agricola) / F (servizi). Per zone A il regime tende ad essere piu' restrittivo.

7. **Modalita' di affidamento dei lavori**: privato / appalto pubblico (per appalto pubblico subentrano gli adempimenti del Codice contratti, vedi skill `pfte-allegato-i7-checker`).

8. **Cantiere**: piu' imprese / unica impresa / autocostruzione (per discriminare obblighi D.Lgs. 81/2008 art. 90 + 99).

Se l'utente fornisce solo input parziali, **procedi con il decision tree** evidenziando i punti dipendenti dalle variabili mancanti, e segnala in chiaro quali regimi possono attivarsi/disattivarsi.

## Fonti normative

Leggere prima di procedere:
- [`references/estratti/dpr-380-2001-regimi-edilizi.md`](../references/estratti/dpr-380-2001-regimi-edilizi.md) - testo strutturato artt. 3, 6, 6-bis, 9-bis, 10, 22, 23, 23-ter, 34-bis, 36, 36-bis
- [`references/estratti/dlgs-222-2016-tabella-a.md`](../references/estratti/dlgs-222-2016-tabella-a.md) - struttura Tabella A sez. II Edilizia
- [`references/estratti/dl-69-2024-salva-casa.md`](../references/estratti/dl-69-2024-salva-casa.md) - sintesi delle modifiche

## Procedura

### Passo 1 - Inquadramento

Riassumi all'utente cio' che hai capito dell'intervento:

> "Sto classificando: [tipologia], su immobile [esistente/nuovo], con/senza opere strutturali, modifiche [sagoma/volume/destinazione], vincoli [paesaggio/MiC/idrogeologico], zona urbanistica [A/B/C/...]. Confermi?"

Se l'utente conferma, procedi. Se corregge, aggiorna l'inquadramento.

### Passo 2 - Decision tree principale

Applica nell'ordine:

#### Branch A - Sanatorie (opera gia' eseguita)

Se l'intervento e' **gia' eseguito senza titolo** o in difformita':

1. Identifica il titolo che **all'epoca** sarebbe stato necessario (CILA / SCIA / PdC).
2. Se **PdC**: regime **art. 36 DPR 380** (doppia conformita' piena: urbanistica ed edilizia, sia all'epoca sia oggi).
3. Se **CILA o SCIA**: regime **art. 36-bis DPR 380** (Salva Casa - doppia conformita' alleggerita: urbanistica oggi + edilizia all'epoca).
4. Se in tolleranza ex art. 34-bis: **NON serve sanatoria** (vedi task `verifica-salva-casa.md`).
5. Per immobili vincolati: **parere preventivo Soprintendenza** prima della sanatoria.

> Output: indica modulo "Sanatoria art. 36" o "Sanatoria semplificata art. 36-bis" della modulistica unificata 2025.

#### Branch B - Cambio destinazione d'uso senza opere (art. 23-ter)

1. **Stessa categoria funzionale**: edilizia libera, salvo regolamento comunale che imponga comunicazione.
2. **Categorie diverse, fuori zona A, post Salva Casa**: regime SCIA (art. 22).
3. **Categorie diverse in zona A (centro storico)**: regime PdC (art. 10) o regime piu' restrittivo del regolamento comunale.
4. **Cambio uso CON opere**: applica il regime del Branch C/D/E (sotto), prendendo il regime piu' alto fra opere e cambio.

#### Branch C - Manutenzione ordinaria (art. 3 lett. a)

-> **Edilizia libera** (art. 6 DPR 380). Modulo: NESSUNO obbligatorio (eventuale comunicazione opere libere se richiesta dal regolamento comunale).

#### Branch D - Manutenzione straordinaria (art. 3 lett. b)

1. **Senza opere su parti strutturali** (anche con frazionamento/accorpamento UI senza opere strutturali): **CILA** (art. 6-bis).
2. **Con opere su parti strutturali** (consolidamenti, sostituzione di solai, di travi portanti, di pilastri, apertura porte portanti): **SCIA** (art. 22).

#### Branch E - Restauro / risanamento conservativo (art. 3 lett. c)

1. Senza opere strutturali: **CILA**.
2. Con opere strutturali: **SCIA**.
3. Su immobile vincolato D.Lgs. 42/2004: regime sopra + **autorizzazione Soprintendenza** preventiva.

#### Branch F - Ristrutturazione edilizia (art. 3 lett. d)

1. **Ristrutturazione "leggera"** (no aumento UI, no modifica volume complessivo, no modifica sagoma/prospetti, no cambio destinazione urbanisticamente rilevante): **SCIA** (art. 22).
2. **Ristrutturazione "pesante"** (modifica volume, sagoma, prospetti, aumento UI, cambio destinazione in zona A, demolizione e ricostruzione con modifiche su immobili vincolati): **PdC** (art. 10 co. 1 lett. c) **o SCIA alternativa** (art. 23 co. 01 lett. a) a scelta del titolare.

> **Avvertenza**: se l'utente sceglie SCIA alternativa, l'inizio lavori e' dopo 30 gg dalla presentazione (non immediato), e le sanzioni in caso di SCIA errata sono assimilate a quelle del PdC. Segnalalo esplicitamente.

#### Branch G - Nuova costruzione (art. 3 lett. e)

1. **Nuova edificazione di edificio**: **PdC** (art. 10 co. 1 lett. a).
2. **In attuazione di piano attuativo dettagliato** (planivolumetriche, tipologiche, formali e costruttive): **PdC** o **SCIA alternativa** (art. 23 co. 01 lett. b/c) a scelta del titolare.
3. **Pertinenze fino al 20% del volume principale**: regime tipicamente **CILA o SCIA** (rinvio regolamento comunale).
4. **Pertinenze oltre il 20%**: assimilate a nuova costruzione - **PdC**.
5. **Tettoie/pergolati amovibili in dimensioni limitate**: edilizia libera (post Salva Casa).
6. **Manufatti temporanei** per attivita' di cantiere/eventi: regime variabile, di norma comunicazione preventiva.

#### Branch H - Ristrutturazione urbanistica (art. 3 lett. f)

-> **PdC** sempre (art. 10 co. 1 lett. b).

#### Branch I - Variante in corso d'opera

1. **Variante essenziale** (ridefinisce l'intervento): regime del titolo che sarebbe necessario per il nuovo intervento. Se cambia il regime (es. da SCIA a PdC), nuova istanza.
2. **Variante non essenziale strutturale**: SCIA in variante.
3. **Variante non essenziale non strutturale**: CILA in variante.
4. **Variante minore** (es. solo finiture, distribuzione interna senza opere strutturali): regolarizzabile con **SCIA prima della Segnalazione Certificata di Agibilita'** (art. 22 co. 2 + art. 24).

### Passo 3 - Pre-requisiti / autorizzazioni accessorie

Per ogni regime individuato, identifica le autorizzazioni a monte:

| Vincolo | Pre-requisito | Riferimento |
|---------|----------------|-------------|
| Bene culturale (parte II D.Lgs. 42) | Autorizzazione MiC (Soprintendenza) | art. 21 D.Lgs. 42/2004 |
| Vincolo paesaggistico (parte III) | Autorizzazione paesaggistica (ordinaria o semplificata) | art. 146 D.Lgs. 42/2004 + DPR 31/2017 |
| Vincolo idrogeologico | Autorizzazione regionale/forestale | R.D. 3267/1923 |
| Sismica zona 1/2 (e in zona 3 per opere significative) | Autorizzazione sismica preventiva o deposito sismico | DPR 380 artt. 93-94-bis (rinvio LR per regimi semplificati) |
| Vincolo idraulico (PAI/PGRA) | Parere/nulla osta Autorita' di bacino | varia per ambito |

### Passo 4 - Adempimenti accessori al cantiere

Per ogni regime:

- **Notifica preliminare di cantiere** (art. 99 D.Lgs. 81/2008): obbligatoria se cantiere con almeno 2 imprese, durata > 30 gg con almeno 20 lavoratori, o 500 uomini-giorno
- **Designazione CSP/CSE**: obbligatoria se cantiere con piu' imprese (D.Lgs. 81/2008 art. 90)
- **DURC** dell'impresa esecutrice
- **Pratica antincendio** (DPR 151/2011) se l'attivita' esercitata e' inserita nell'allegato

### Passo 5 - Output

Produci il report nel formato:

```markdown
# Determinazione regime edilizio - DPR 380/2001 + D.Lgs. 222/2016 + Salva Casa

**Data**: [oggi]
**Inquadramento intervento**:
- Tipologia: [...]
- Immobile: [esistente/nuovo, stato legittimo accertato si/no]
- Parti strutturali coinvolte: [si/no]
- Modifiche: volume [si/no], sagoma [si/no], prospetti [si/no], UI [si/no], destinazione [si/no]
- Vincoli: paesaggio [si/no], beni culturali [si/no], idrogeologico [si/no], sismica [zona], idraulico [si/no]
- Zona urbanistica: [A/B/C/D/E/F]

## Regime determinato

**Modulo unificato**: [Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis]
**Riferimento DPR 380**: art. [N] co. [M] lett. [X]
**Voce Tabella A D.Lgs. 222/2016**: sez. II - [paragrafo / lettera]
**Modulistica unificata**: modulo "[nome modulo]" della Conferenza Unificata 27/3/2025

### Motivazione

[Spiegazione del decision tree applicato, riferimenti agli articoli]

### Alternative

[Se applicabile: SCIA alternativa al PdC, etc. - spiegare la scelta del titolare]

## Pre-requisiti / autorizzazioni accessorie

| Pre-requisito | Applicabile | Riferimento |
|---------------|-------------|-------------|
| Autorizzazione paesaggistica | [si / no / da-verificare] | art. 146 D.Lgs. 42/2004 |
| Autorizzazione MiC | [si / no] | art. 21 D.Lgs. 42/2004 |
| Autorizzazione/deposito sismico | [si / no / da-verificare] | DPR 380 artt. 93-94-bis |
| Autorizzazione idrogeologica | [si / no] | R.D. 3267/1923 |

## Adempimenti accessori al cantiere

[Notifica preliminare, CSP/CSE, antincendio, etc.]

## Allegati richiesti

[Rinvio al task `genera-elenco-allegati.md` se l'utente lo richiede esplicitamente, oppure sintesi minima]

## Elementi non valutabili automaticamente dalla skill

- Conformita' specifica al PRG/PUC e al regolamento edilizio del Comune
- Eventuali integrazioni della Tabella A da regolamenti comunali (es. soglia pertinenze)
- Applicabilita' di leggi regionali specifiche (recupero sottotetti, paesaggio, distanze)
- Pareri preventivi di enti terzi (ASL, VVF, Soprintendenza, Ufficio Sismica)
- Stato di legittimita' specifico del singolo immobile

## Avvertenze e rinvio professionale

- Il regime e' determinato sulla base delle variabili dichiarate; verificare con il **regolamento edilizio comunale** se ci sono integrazioni locali.
- Per casi al limite (es. CILA vs SCIA su intervento misto, SCIA vs PdC su ristrutturazione "borderline pesante", classificazione di pertinenza) **interpellare lo sportello SUE/SUAP** del Comune competente prima del deposito.
- L'output non sostituisce la **firma del tecnico abilitato** sull'asseverazione del modulo.

**La presente determinazione e' uno strumento di supporto e non sostituisce il giudizio del tecnico abilitato firmatario ne' l'istruttoria del SUE/SUAP.**
```

## Casi limite da gestire

### Intervento misto (manutenzione + ristrutturazione + cambio uso)

Applica il **regime piu' alto** richiesto da una qualunque delle componenti. Es: manutenzione strutturale (SCIA) + cambio destinazione d'uso urbanisticamente rilevante in zona A (PdC) -> regime PdC. Segnalalo esplicitamente: "intervento composto, regime determinato dalla componente piu' restrittiva".

### Ristrutturazione "borderline" pesante/leggera

Se l'utente non e' chiaro su modifica di sagoma/prospetti, chiedere:
- "Le opere modificano la sagoma esterna? Si intendono variazioni della linea di colmo, della linea di gronda, dei prospetti?"
- "Si sposta il sedime?"
- "Aumentano le unita' immobiliari? Cambia la destinazione d'uso urbanisticamente rilevante?"

Se almeno una risposta e' "si" -> ristrutturazione pesante (PdC o SCIA alternativa). Se tutte "no" -> ristrutturazione leggera (SCIA).

### Pertinenza ambigua

Soglia 20% e' nazionale ma molti Comuni la riducono. Se utente non sa: indicare regime nazionale e segnalare "verificare regolamento edilizio comunale" come priorita' alta.

### Stato legittimo non accertato

Se l'utente non ha accertato lo stato legittimo: **bloccare** la determinazione del regime e segnalare che, ai sensi dell'art. 9-bis DPR 380 (Salva Casa), il professionista non puo' asseverare validamente la conformita' urbanistica senza accertamento dello stato legittimo. Suggerire la procedura di ricostruzione documentale o, in casi gravi, la sanatoria preventiva (art. 36 o 36-bis).

### Variante con cambio di regime

Se la variante in corso d'opera fa "saltare" il regime (es. SCIA -> PdC perche' aumenta volume), serve **nuova istanza** nel regime piu' alto, non variante. Segnalalo.

### Cambio destinazione d'uso ambiguo (categorie incerte)

Se la nuova destinazione non e' chiaramente in una delle 5 categorie (es. attivita' direzionale + commerciale promiscua), chiedere quale e' la **prevalente** e segnalare che la categoria del PRG/regolamento comunale puo' essere piu' specifica del regime nazionale.

## Limiti di questo task

- Determina il **regime nazionale**, non valuta il regolamento edilizio comunale.
- Non integra **leggi regionali** specifiche (es. recupero sottotetti, distanze, paesaggio).
- Non valuta la **adeguatezza tecnica** dell'intervento.
- Non emette **giudizi di legittimita'** su opere preesistenti senza titolo (rinvia ad apposita procedura di sanatoria).
- Non sostituisce il **DIP/RUP** per appalti pubblici (rinvio skill `pfte-allegato-i7-checker`).

## Esempi

Vedi `examples/`:
- `manutenzione-frazionamento-cila/` - manutenzione straordinaria con frazionamento UI senza opere strutturali (regime CILA)
- `cambio-uso-salva-casa-scia/` - cambio destinazione d'uso post Salva Casa (regime SCIA)
- `sanatoria-semplificata-art36bis/` - sanatoria di opera abusiva CILA-dovuta (regime art. 36-bis)
