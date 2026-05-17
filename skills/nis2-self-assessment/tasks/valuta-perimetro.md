# Task: Valutazione del perimetro NIS2 (D.Lgs. 138/2024 art. 3, 6)

Determina se l'organizzazione rientra nell'ambito di applicazione del D.Lgs. 138/2024 e, in caso affermativo, se e' classificata come "soggetto essenziale" o "soggetto importante".

## Obiettivo

Produrre una valutazione strutturata che concluda con uno dei 4 esiti:

- **SOGGETTO ESSENZIALE** - rientra nei criteri dell'art. 6 co. 1 lett. a-e o e' classificato dall'ACN ex art. 6 co. 2.
- **SOGGETTO IMPORTANTE** - rientra nell'ambito del decreto (art. 3) ma non e' essenziale.
- **FUORI AMBITO** - non rientra nelle tipologie degli Allegati I-IV o non supera la soglia size-cap rule e non rientra nei casi di applicazione indipendente dalle dimensioni.
- **AMBITO DUBBIO** - applicazione indipendente dalle dimensioni che richiede individuazione formale dall'ACN (art. 3 co. 8, 9, 13). Esito orientativo, da verificare con ACN.

## Input richiesti

Per la valutazione di perimetro:
- **Settore di attivita'** - descrizione delle attivita' economiche principali e secondarie. Riferimento a codice ATECO se disponibile.
- **Tipologia di soggetto** - struttura giuridica (S.p.A., S.r.l., PA, ente, societa' a controllo pubblico, ecc.)
- **Dimensioni** (Raccomandazione 2003/361/CE):
  - Numero di occupati (su base annuale media)
  - Fatturato annuo
  - Totale di bilancio annuo
  - Imprese collegate o associate (se applicabile, in base all'art. 6 par. 2 dell'Allegato alla Raccomandazione)
- **Servizi forniti** - quali servizi specifici, in quali settori dell'Allegato I o II.
- **Geografia** - sedi italiane e nell'UE, servizi forniti transfrontalieri.
- **Ruolo nella catena di approvvigionamento** - e' un fornitore di servizi TIC/sicurezza per soggetti essenziali/importanti? Detiene/gestisce sistemi su cui dipendono questi soggetti? (rilevante per art. 3 co. 10).
- **Stato attuale** - e' gia' identificato come operatore di servizi essenziali (D.Lgs. 65/2018), soggetto critico (Dir. 2022/2557 / decreto di recepimento), soggetto PSNC (DL 105/2019), soggetto regolato da DORA (Reg. UE 2022/2554), prestatore servizi fiduciari qualificato (Reg. eIDAS UE 910/2014)?

## Fonti

Leggere prima:
- `references/estratti/dlgs-138-2024-perimetro.md` - art. 3, 6, 7
- `references/estratti/dlgs-138-2024-allegati-i-iv.md` - mappa settori e tipologie

## Procedura

### Passo 1 - Verifica Allegati I-II (settori e tipologie privati)

Per il settore di attivita' dell'organizzazione, controllare se ricade in uno dei sottosettori dell'Allegato I (10 settori altamente critici) o dell'Allegato II (7 altri settori critici), e se la tipologia di soggetto specifica corrisponde a una delle voci elencate.

| Allegato | Settore | Tipologia rientra? |
|----------|---------|---------------------|
| I | 1. Energia (elettr./teleriscald./petrolio/gas/H2) | [SI/NO/PARZIALE] |
| I | 2. Trasporti (aereo/ferr./acqua/strada) | [SI/NO/PARZIALE] |
| I | 3. Bancario | [SI/NO] (vedi DORA per esclusione capi IV-V) |
| I | 4. Mercati finanziari | [SI/NO] (vedi DORA) |
| I | 5. Sanita' | [SI/NO/PARZIALE] |
| I | 6. Acqua potabile | [SI/NO] |
| I | 7. Acque reflue | [SI/NO] |
| I | 8. Infrastrutture digitali (IXP/DNS/TLD/cloud/DC/CDN/serv. fiduciari/fornitori reti/serv. comunic./serv. gestiti/sicurezza gestita) | [SI/NO/PARZIALE] |
| I | 9. Gestione servizi TIC B2B | [SI/NO] |
| I | 10. Spazio | [SI/NO] |
| II | 1. Servizi postali e di corriere | [SI/NO] |
| II | 2. Gestione rifiuti | [SI/NO] |
| II | 3. Sostanze chimiche | [SI/NO] |
| II | 4. Alimenti (ingrosso/produzione industriale) | [SI/NO] |
| II | 5. Fabbricazione (disp. medici/elettronica/elettr./macchinari/auto/altri trasporti) | [SI/NO/PARZIALE] |
| II | 6. Fornitori servizi digitali (mercati online/motori ricerca/social/registrar) | [SI/NO] |
| II | 7. Ricerca | [SI/NO] |

Se nessun "SI" per gli Allegati I-II, passare al Passo 2.

### Passo 2 - Verifica Allegato III (PA italiane)

Se l'organizzazione e' una PA italiana, verificare in quale categoria dell'Allegato III ricade:

| Categoria | Esempi | Rientra? |
|-----------|--------|----------|
| a) Centrali (Costituzionali, PCM, Ministeri, Agenzie fiscali, Autorita' indip.) | | [SI/NO] |
| b) Regionali (Regioni, Province autonome) | | [SI/NO] |
| c) Locali (Citta' metrop., Comuni > 100k abitanti, capoluoghi regione, ASL) | | [SI/NO] |
| d) Altri pubblici (Enti regolazione, servizi economici, struttura associativa, servizi assist./ric./cult., ricerca, zooprofilattici) | | [SI/NO] |

PA Allegato III: applicazione **indipendente dalle dimensioni** (art. 3 co. 6).

### Passo 3 - Verifica Allegato IV (ulteriori soggetti)

Per soggetti non classificati in passi 1-2:

| Tipologia Allegato IV | Rientra? |
|------------------------|----------|
| 1. Trasporto pubblico locale | [SI/NO] |
| 2. Istituti di istruzione che svolgono ricerca | [SI/NO] |
| 3. Soggetti di interesse culturale | [SI/NO] |
| 4. Societa' in house, partecipate, a controllo pubblico (D.Lgs. 175/2016) | [SI/NO] |

I soggetti Allegato IV sono "in ambito" solo se **individuati formalmente dall'ACN** (art. 3 co. 8 + co. 13). Senza individuazione, esito orientativo "AMBITO DUBBIO".

### Passo 4 - Applicazione indipendente dalle dimensioni (art. 3 co. 5)

Verificare se ricade in una delle 5 categorie sempre in ambito:

| Cat. art. 3 co. 5 | Rientra? |
|-------------------|----------|
| a) Soggetti critici (Dir. 2022/2557 / decreto recepimento) | [SI/NO] |
| b) Fornitori reti pubbliche di comunicazione elettronica o servizi comunicazione elettronica accessibili al pubblico | [SI/NO] |
| c) Prestatori di servizi fiduciari (qualificati e non) | [SI/NO] |
| d) Gestori TLD + fornitori DNS | [SI/NO] |
| e) Fornitori servizi di registrazione domini (registrar) | [SI/NO] |

Se SI: l'organizzazione e' in ambito INDIPENDENTEMENTE dalle dimensioni.

### Passo 5 - Verifica art. 3 co. 9 e co. 10 (criteri discrezionali)

Verificare se ricade in uno dei criteri di applicazione discrezionale:

| Criterio | Applicabile? |
|----------|--------------|
| co. 9 lett. a) Operatore di servizi essenziali ex D.Lgs. 65/2018 (NIS originale) | [SI/NO] |
| co. 9 lett. b) Unico fornitore nazionale di servizio essenziale | [SI/NO] |
| co. 9 lett. c) Perturbazione con impatto su sicurezza/incolumita'/salute pubblica | [SI/NO] |
| co. 9 lett. d) Rischio sistemico significativo, anche transfrontaliero | [SI/NO] |
| co. 9 lett. e) Critico per importanza nazionale/regionale | [SI/NO] |
| co. 9 lett. f) Critico come elemento sistemico catena approvvigionamento | [SI/NO] |
| co. 10 Impresa collegata che (a) decide su misure cyber, (b) gestisce sistemi cui dipende il soggetto, (c) effettua operazioni di sicurezza, (d) fornisce servizi TIC/sicurezza al soggetto essenz./important. | [SI/NO] |

Anche un solo SI -> ambito DUBBIO che richiede individuazione formale ACN.

### Passo 6 - Size-cap rule per soggetti privati (art. 3 co. 2)

Solo per soggetti privati in Allegato I-II che NON ricadono nei casi indipendenti dalle dimensioni:

L'organizzazione **supera i massimali per le piccole imprese** (Racc. 2003/361/CE Allegato art. 2 par. 2)?

> **Definizione di piccola impresa**: occupati < 50 **AND** (fatturato annuo OR totale di bilancio annuo) <= 10M EUR.
>
> Quindi NOT-piccola (= in ambito NIS2 ai sensi dell'art. 3 co. 2): occupati >= 50 **OPPURE** entrambi i parametri finanziari (fatturato AND bilancio) > 10M EUR.

Compilare:

| Misura | Valore | |
|--------|--------|---|
| Occupati (media annuale) | [N] | |
| Fatturato annuo | [EUR M] | |
| Totale di bilancio annuo | [EUR M] | |

Verificare la condizione di esclusione dall'ambito (= il soggetto e' piccola impresa):

- Occupati < 50? **AND**
- (Fatturato <= 10M OR Bilancio <= 10M)?

Se **entrambe** le condizioni sono vere -> e' piccola impresa -> **fuori ambito** salvo applicazione indipendente dalle dimensioni (Passo 4) o classificazione discrezionale ACN (Passo 5).

Se anche solo una delle due e' falsa -> **non e' piccola** -> **in ambito** se ricade in Allegato I-II.

Esempi:
- 60 dipendenti, 5M fatturato, 4M bilancio: occupati >= 50 -> NOT piccola -> in ambito (in Allegato I-II)
- 30 dipendenti, 15M fatturato, 12M bilancio: occupati < 50 ma valori finanziari entrambi > 10M -> NOT piccola -> in ambito
- 30 dipendenti, 15M fatturato, 8M bilancio: occupati < 50 e bilancio <= 10M -> piccola -> fuori ambito (size-cap)

### Passo 7 - Classificazione essenziale vs importante (art. 6)

Se in ambito, classificare:

**Soggetto essenziale (art. 6 co. 1)**:

> **Definizione di media impresa** (Racc. 2003/361/CE Allegato art. 2 par. 1): occupati < 250 **AND** (fatturato annuo <= 50M EUR **OR** totale di bilancio annuo <= 43M EUR).
>
> Quindi NOT-media (= "grande", soggetto essenziale via art. 6 co. 1 lett. a): occupati >= 250 **OPPURE** (fatturato > 50M **AND** bilancio > 43M).

| Lettera art. 6 co. 1 | Criterio | Soddisfatto? |
|---------|----------|--------------|
| a) | Soggetto Allegato I che e' "grande": occupati >= 250 **OPPURE** (fatturato > 50M EUR **AND** bilancio > 43M EUR) | [SI/NO] |
| b) | Soggetto critico ex Dir. 2022/2557 (indipendente dalle dimensioni) | [SI/NO] |
| c) | Fornitore reti/servizi comunicazione elettronica considerato "media impresa" o superiore | [SI/NO] |
| d) | Prestatore servizi fiduciari **qualificato** o gestore TLD o fornitore DNS (indipendente dalle dimensioni) | [SI/NO] |
| e) | PA centrale Allegato III lett. a) | [SI/NO] |

Se nessun SI all'art. 6 co. 1 ma il soggetto e' in ambito: **soggetto importante** (art. 6 co. 3).

L'ACN puo' inoltre individuare come essenziali soggetti dei commi 6, 8, 9, 10 dell'art. 3 (art. 6 co. 2).

### Passo 8 - Esclusioni e regimi speciali

- Settori 3 e 4 dell'Allegato I (banche, infrastrutture mercati finanziari): esclusi dai Capi IV-V del decreto se DORA-eligible (art. 3 co. 14). Per questi soggetti la skill segnala il rinvio a DORA e non procede con la gap analysis NIS2.
- Soggetti PSNC (DL 105/2019): la notifica PSNC assolve alla notifica NIS2 (art. 1 co. 8 DL 105/2019 come modificato). Le misure tecniche restano cumulative.

### Passo 9 - Sintesi e output

```markdown
# Valutazione perimetro NIS2 - [nome organizzazione]

**Data valutazione**: [data]
**Organizzazione valutata**: [ragione sociale, settore, P.IVA]
**Compilato da**: [nome / ruolo]

## Esito orientativo

**[SOGGETTO ESSENZIALE | SOGGETTO IMPORTANTE | FUORI AMBITO | AMBITO DUBBIO]**

## Motivazione

### Settori applicabili
[Allegato I/II/III/IV con voce specifica]

### Size-cap rule
- Occupati: [N]
- Fatturato: [EUR M]
- Bilancio: [EUR M]
- Classificazione: [Piccola / Media / Grande]
- Supera massimali per piccole imprese: [SI/NO]
- Supera massimali per medie imprese: [SI/NO]

### Applicazione indipendente dalle dimensioni
[lett. art. 3 co. 5/6/8/9/10 applicabile]

### Classificazione essenziale (art. 6 co. 1)
[lett. a/b/c/d/e applicabile, oppure NO]

## Obblighi conseguenti

[In base all'esito]

### Se ESSENZIALE o IMPORTANTE:
- Registrazione su piattaforma ACN (art. 7) - finestra: 1 gen - 28 feb
- Designazione punto di contatto NIS + sostituto (art. 7 co. 1 e co. 4)
- Approvazione modalita' di implementazione misure dal CdA (art. 23)
- Adozione misure tecniche/operative/organizzative (art. 24): 10 elementi minimi
- Formazione organi di amministrazione e dipendenti (art. 23 co. 2)
- Notifica incidenti significativi al CSIRT Italia (art. 25): 24h pre-notifica + 72h notifica + 1 mese report finale
- Sanzioni: fino a 10M EUR / 2% fatturato (essenziali) o 7M EUR / 1.4% (importanti) (art. 38 co. 9)

### Se FUORI AMBITO:
- Verificare periodicamente in caso di crescita dimensioni o cambio attivita'
- Considerare adesione volontaria al Framework Nazionale Cybersecurity come buona pratica
- Verificare se altre normative settoriali si applicano (DORA, codice comunicazioni elettroniche, PSNC)

### Se AMBITO DUBBIO:
- Contattare ACN per chiarimento sull'individuazione formale ex art. 3 co. 13
- Adottare comportamento prudenziale (registrazione preliminare in piattaforma) in attesa di pronuncia

## Casi correlati

- DORA (Reg. UE 2022/2554): se ente finanziario, regime sostanziale prevale
- PSNC (DL 105/2019): se gia' nel perimetro, notifica unificata possibile
- GDPR (Reg. UE 2016/679): notifica data breach al Garante in parallelo se dati personali coinvolti
- Codice comunicazioni elettroniche (D.Lgs. 259/2003): per fornitori reti/servizi

## Limiti di questa valutazione

- Si basa sulle informazioni fornite dall'utente. Cambi nelle dimensioni o nelle attivita' possono modificare l'esito.
- L'individuazione formale come soggetto NIS spetta al soggetto stesso sulla piattaforma ACN (art. 7) sotto la propria responsabilita'.
- L'individuazione discrezionale ex art. 3 co. 8, 9, 13 e art. 6 co. 2 spetta all'ACN.
- Esito orientativo: la valutazione finale richiede consulenza legale o consulente cybersecurity con esperienza NIS2.

## Rinvio al CISO / consulente cyber / legale

La presente valutazione di perimetro e' di supporto, non sostituisce la decisione di registrazione o classificazione che spetta al titolare con la consulenza del CISO / consulente cyber / legale. Sanzioni amministrative ex art. 38 D.Lgs. 138/2024.
```

## Casi tipici (esempi orientativi)

| Caso | Settore | Dimensioni | Esito |
|------|---------|-------------|-------|
| Utility elettrica con 600 dipendenti | Allegato I.1.a | Grande (occupati >= 250) | Essenziale (art. 6 co. 1 lett. a) |
| ASL Roma 1 | Allegato III.c.4 | (n/a, indip. dimensioni) | In ambito; importante salvo classificazione essenziale ACN |
| PMI manifatturiera 80 dipendenti, 25M fatturato, 18M bilancio | Allegato II.5 | Media (occupati >= 50, ma < 250) | In ambito; importante (Allegato II non puo' essere essenziale via lett. a) |
| Microimpresa SaaS, 30 dipendenti, 8M fatturato, 5M bilancio | Allegato I.8 (cloud) | Piccola (occupati < 50 e bilancio <= 10M) | Fuori ambito per size-cap; riconsiderare solo se classificato come soggetto critico ex Dir. 2022/2557 o ricade in art. 3 co. 9/10 |
| Azienda ospedaliera universitaria, 2000 dipendenti | Allegato I.5 | Grande | Essenziale (art. 6 co. 1 lett. a) |
| Comune di Bologna, 400.000 abitanti | Allegato III.c.2 + III.c.3 | (n/a, indip. dimensioni) | In ambito (art. 3 co. 6); importante salvo classificazione essenziale ACN ex art. 6 co. 2 |
| Comune di 10.000 abitanti | (non rientra in Allegato III lett. c) | (n/a) | Fuori ambito (manca tipologia in Allegato III) |
| Universita' privata con istituto di ricerca | Allegato IV.2 | (n/a, indip. dimensioni) | Ambito dubbio - in ambito solo se formalmente individuato dall'ACN ex art. 3 co. 8 + co. 13 |
| Fornitore di servizi gestiti (MSP) per cliente ospedaliero, 60 dipendenti, 9M fatturato, 7M bilancio | Allegato I.8 (managed services) o Allegato I.9 (gestione servizi TIC B2B) | Media (occupati >= 50) | **In ambito per size-cap** (art. 3 co. 2 - non e' piccola); importante salvo art. 6. NB: art. 3 co. 5 lett. b e art. 3 co. 10 NON si applicano automaticamente; lett. b e' per fornitori di reti/servizi di comunicazione elettronica, co. 10 richiede impresa collegata che soddisfi i criteri a-d |
| Banca commerciale di grandi dimensioni | Allegato I.3 | Grande | Essenziale ma esclusa dai Capi IV-V (DORA prevale ex art. 3 co. 14) |

## Limiti di questo task

- Decisione di perimetro orientativa, non costitutiva.
- Richiede dati dimensionali precisi: occupati ANNUALI medi, fatturato consolidato, bilancio.
- Per imprese collegate/associate (gruppi, holding) la valutazione e' piu' complessa: applicare art. 6 par. 2 dell'Allegato Racc. 2003/361/CE oppure la deroga art. 3 co. 4 D.Lgs. 138/2024.
- Per organizzazioni in piu' Stati membri, considerare la giurisdizione (art. 5 D.Lgs. 138/2024) e gli obblighi di notifica multilaterali.

## Esempi

Vedi `examples/`:
- `essenziale-utility-energia/` - utility energetica grande dimensione
- `importante-pmi-manifattura/` - media impresa manifatturiera

## Rinvio a task successivi

Se l'esito e' **SOGGETTO ESSENZIALE** o **SOGGETTO IMPORTANTE**, il soggetto e' tenuto a:

- **Registrazione e aggiornamento annuale sulla piattaforma ACN** (artt. 7 D.Lgs. 138/2024 + Det. ACN 127437/2026). Tra gli obblighi dell'aggiornamento annuale (finestra 15 aprile - 31 maggio) c'e' l'**elenco dei fornitori rilevanti NIS** ex art. 18 Det. 127437/2026: vedi task `elenco-fornitori-rilevanti.md`.
- **Gap analysis delle misure di sicurezza** ex art. 24 + Det. ACN 379907/2025: vedi task `gap-analysis-misure.md`. Per i soggetti inseriti per la prima volta nel 2026 si applicano i termini speciali della Det. ACN 127434/2026 (misure entro 31/07/2027; notifica incidenti dal 01/01/2027).
- **Verifica obblighi degli organi di amministrazione** (art. 23 D.Lgs. 138/2024): vedi task `check-obblighi-governance.md`.
- **Verifica di un eventuale incidente significativo** (art. 25 D.Lgs. 138/2024): vedi task `verifica-incidente-significativo.md`.
