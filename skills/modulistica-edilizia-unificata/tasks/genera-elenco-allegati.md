# Task: Genera elenco allegati per modulo unificato

Per il modulo edilizio individuato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis), produce l'elenco strutturato degli allegati richiesti come da modulistica nazionale unificata 2025 (Conferenza Unificata 27/3/2025).

## Obiettivo

Restituire all'utente:
- L'**elenco strutturato** degli allegati per il modulo, distinguendo:
  - **Sempre obbligatori** (ogni istanza)
  - **Condizionali** (con condizione esplicita)
  - **Facoltativi** (a discrezione del tecnico/SA)
- Per ogni allegato: la **descrizione**, la **fonte normativa** (articolo del DPR 380, D.Lgs. 81/2008, D.Lgs. 42/2004, etc.), la **forma** richiesta (firma digitale, asseverazione, ricevuta)
- Un set di **avvertenze** sui casi in cui il Comune puo' richiedere allegati locali aggiuntivi

## Input richiesti

Variabili minime (chiedere all'utente se non fornite):

1. **Modulo individuato**: Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis. Se non noto, prima eseguire il task `determina-regime-edilizio.md`.

2. **Tipologia intervento** (rinvio art. 3 DPR 380): per discriminare allegati condizionali (es. relazione strutturale solo se opere strutturali).

3. **Vincoli sovraordinati** (paesaggistico, beni culturali, idrogeologico, sismico, idraulico): determinano allegati specifici.

4. **Cantiere**: piu' imprese / unica impresa / autocostruzione - per discriminare obblighi D.Lgs. 81/2008 (notifica, CSP/CSE, PSC).

5. **Attivita' soggetta a prevenzione incendi** (DPR 151/2011): si / no / da-verificare.

6. **Intervento incidente sulla prestazione energetica** (D.Lgs. 192/2005): si / no.

7. **Contributo di costruzione**: applicabile (si per PdC e SCIA alternativa, no per CILA e SCIA "pure" salvo cambio uso urbanisticamente rilevante).

## Fonti normative

Leggere prima di procedere:
- [`references/estratti/modulistica-unificata-2025.md`](../references/estratti/modulistica-unificata-2025.md) - struttura dei moduli e allegati ricorrenti
- [`references/estratti/dpr-380-2001-regimi-edilizi.md`](../references/estratti/dpr-380-2001-regimi-edilizi.md) - articoli di rinvio

## Procedura

### Passo 1 - Verifica modulo

Conferma con l'utente il modulo per cui generare la checklist. Se non noto, instradare a `determina-regime-edilizio.md`.

### Passo 2 - Allegati strutturali del modulo (sempre obbligatori)

Per **TUTTI** i moduli (ad eccezione dell'edilizia libera "pura" che non richiede modulo):

| Allegato | Forma | Riferimento |
|----------|-------|-------------|
| Procura speciale (se delega) | Firma digitale del titolare | art. 21 DPR 445/2000 |
| Ricevuta diritti di segreteria | PDF della ricevuta | regolamento comunale |
| Imposta di bollo | Marca da bollo dematerializzata o assolta in modo virtuale | DPR 642/1972 |
| Documentazione fotografica dello stato di fatto | PDF / immagini (date, vedute principali) | prassi |
| Estratto di mappa catastale | PDF rilasciato da Agenzia Entrate / Catasto | prassi |
| Visura catastale delle UI interessate | PDF Agenzia Entrate | prassi |
| Stralcio strumento urbanistico (PRG/PUC) | PDF con riferimento alle norme tecniche di attuazione applicabili | prassi |
| Elaborati grafici (planimetria stato di fatto, di progetto, raffronto) | PDF firmati digitalmente dal progettista | prassi + asseverazione tecnico |
| Relazione tecnica asseverata | PDF firmato digitalmente, con asseverazione di conformita' | art. 6-bis / 22 / 23 / 10 DPR 380 |
| Dichiarazione di stato legittimo dell'immobile | Asseverazione tecnico abilitato | art. 9-bis DPR 380 (Salva Casa) |

### Passo 3 - Allegati specifici per modulo

#### Edilizia libera (art. 6 DPR 380)

**Nessun modulo nazionale obbligatorio**. Eventuale "comunicazione opere libere" facoltativa (richiesta da alcuni regolamenti comunali, p. es. zone vincolate o centri storici).

Se la "comunicazione opere libere" e' richiesta:
- Descrizione sintetica dell'opera
- Documentazione fotografica
- Eventuale autorizzazione paesaggistica (se in vincolo e l'opera non rientra in DPR 31/2017 All. A)

#### CILA (art. 6-bis DPR 380)

Allegati base (vedi Passo 2) + condizionali:

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Notifica preliminare di cantiere | Cantieri ex art. 90 co. 3 (piu' imprese, anche non contemporanee), cantieri di unica impresa con entita' presunta >= 200 uomini-giorno, o cantieri inizialmente non soggetti che vi rientrino in seguito | art. 99 co. 1 D.Lgs. 81/2008 |
| Designazione CSP/CSE + DURC + idoneita' tecnico-professionale imprese | Cantiere multiimpresa | art. 90 + 97 D.Lgs. 81/2008 |
| Autorizzazione paesaggistica (ordinaria o semplificata) | Vincolo paesaggio non rientrante in DPR 31/2017 All. A | art. 146 D.Lgs. 42/2004 + DPR 31/2017 |
| Autorizzazione MiC (Soprintendenza) | Bene culturale (parte II D.Lgs. 42/2004) | art. 21 D.Lgs. 42/2004 |
| Autorizzazione vincolo idrogeologico | Zona soggetta | R.D. 3267/1923 |
| Pratica antincendio (CILA antincendio o SCIA antincendio o PdC antincendio) | Attivita' soggetta DPR 151/2011 | DPR 151/2011 |
| Relazione tecnica L. 10 / D.Lgs. 192 | Intervento incidente su prestazione energetica | D.Lgs. 192/2005 + DM 26/6/2015 |
| Pratica acustica DPCM 5/12/1997 | Nuovo edificio o ristrutturazione pesante (di norma non si applica a CILA pura) | DPCM 5/12/1997 |

#### SCIA (art. 22 DPR 380)

Allegati base + condizionali della CILA (sopra) + specifici della SCIA:

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Relazione strutturale (descrizione delle opere strutturali) | Sempre per SCIA che riguarda parti strutturali | art. 65 + 67 DPR 380 + NTC 2018 |
| Calcoli strutturali e relazione di calcolo | Opere strutturali significative | art. 65 DPR 380 + NTC 2018 |
| Deposito sismico / autorizzazione sismica preventiva | Zona sismica e incidenza dell'opera | DPR 380 artt. 93-94-bis (rinvio LR per regimi semplificati) |
| Relazione di calcolo geotecnico | Opere di fondazione/scavi rilevanti | NTC 2018 cap. 6 |
| Collaudo statico / direzione lavori strutturale (designazione) | Opere strutturali significative | art. 67 DPR 380 |
| Documentazione idraulica (se in fascia PAI/PGRA) | Vincolo idraulico | piano di gestione del rischio alluvioni |

#### SCIA alternativa al PdC (art. 23 DPR 380)

Allegati della SCIA (sopra) + specifici:

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Computo metrico estimativo dell'opera | Sempre (per calcolo contributo di costruzione) | art. 16 DPR 380 |
| Asseverazione di pagamento contributo di costruzione (oneri urbanizzazione + costo costruzione) | Sempre (anticipato o rateizzato) | art. 16 DPR 380 |
| Conformita' a piano attuativo (NTA, planivolumetrico) | Se la SCIA alternativa e' adottata in attuazione di piano dettagliato (art. 23 co. 01 lett. b/c) | art. 23 DPR 380 |
| Eventuale convenzione urbanistica | Se l'intervento e' in attuazione di piano attuativo convenzionato | prassi |

> **Nota**: la SCIA alternativa NON puo' iniziare immediatamente; servono **30 gg** di attesa (a differenza della SCIA "pura"). Sanzioni in caso di SCIA alternativa errata sono assimilate a quelle del PdC.

#### Permesso di Costruire (art. 10 DPR 380)

Allegati base + condizionali (cantiere, vincoli) + specifici:

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Computo metrico estimativo | Sempre (per calcolo contributo di costruzione) | art. 16 DPR 380 |
| Prospetto di calcolo del contributo di costruzione | Sempre (escluse opere art. 17/18 esonerate) | art. 16 DPR 380 |
| Ricevuta pagamento (o piano di rateizzazione) del contributo | Sempre | art. 16 DPR 380 |
| Convenzione urbanistica + relativi atti | Se in attuazione di piano attuativo o operazioni di trasformazione | prassi + LR varie |
| Pareri preventivi VVF / ASL / Soprintendenza | Se applicabili | DPR 151/2011, regolamenti sanitari, D.Lgs. 42/2004 |
| Studio di impatto ambientale o Verifica di assoggettabilita' a VIA | Se opera in All. II/III/IV D.Lgs. 152/2006 | D.Lgs. 152/2006 parte II |
| Relazione paesaggistica completa (Allegato A) o semplificata (Allegato B) | Se in vincolo | DPR 31/2017 |
| Relazione strutturale + calcoli + deposito/autorizzazione sismica | Se opere strutturali | DPR 380 capo IV + NTC 2018 |
| Relazione tecnica L. 10 / D.Lgs. 192 | Sempre per nuovo edificio o intervento incidente sulla prestazione energetica | D.Lgs. 192/2005 |
| Documentazione barriere architettoniche | Sempre per nuova costruzione e per interventi su edifici aperti al pubblico | L. 13/1989 + DM 236/1989 + DPR 503/1996 |
| Pratica acustica DPCM 5/12/1997 | Nuovo edificio o ristrutturazione pesante | DPCM 5/12/1997 |
| Pratica antincendio (CILA / SCIA / PdC antincendio in funzione dell'attivita') | Se attivita' soggetta DPR 151/2011 | DPR 151/2011 |
| Notifica preliminare di cantiere + designazione CSP/CSE | Cantiere con piu' imprese, sopra soglia D.Lgs. 81 | art. 90 + 99 D.Lgs. 81/2008 |

#### Sanatoria art. 36 DPR 380 (doppia conformita' piena)

Allegati base + specifici:

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Relazione tecnica asseverata sulla doppia conformita' urbanistica ed edilizia (sia all'epoca sia oggi) | Sempre | art. 36 DPR 380 |
| Documentazione probante dell'epoca di realizzazione | Sempre | prassi |
| Computo della sanzione pecuniaria (contributo di costruzione doppio) | Sempre | art. 36 co. 2 DPR 380 |
| Parere Soprintendenza | Se immobile vincolato | art. 21 D.Lgs. 42/2004 |
| Stato legittimo dell'immobile (parte non in sanatoria) | Sempre | art. 9-bis DPR 380 |
| Elaborati grafici di rilievo dell'opera difforme/abusiva | Sempre | prassi |

#### Sanatoria semplificata art. 36-bis DPR 380 (Salva Casa - doppia conformita' alleggerita)

| Allegato | Quando obbligatorio | Riferimento |
|----------|----------------------|-------------|
| Relazione tecnica asseverata sulla doppia conformita' alleggerita: urbanistica vigente alla data della domanda + edilizia vigente all'epoca della realizzazione | Sempre | art. 36-bis DPR 380 (Salva Casa) |
| Documentazione probante dell'epoca di realizzazione (foto storiche, ortofoto, atti, dichiarazioni sostitutive di atto notorio) | Sempre | prassi |
| Stato legittimo dell'immobile (parte non in sanatoria) | Sempre | art. 9-bis DPR 380 |
| Computo della sanzione pecuniaria graduata | Sempre | art. 36-bis DPR 380 |
| Parere preventivo Soprintendenza | Se immobile vincolato | art. 36-bis + D.Lgs. 42/2004 |
| Documentazione fotografica stato di fatto | Sempre | prassi |
| Elaborati grafici di rilievo dell'opera difforme/realizzata | Sempre | prassi |

> **Differenza chiave art. 36 vs art. 36-bis** (versione coordinata post Salva Casa, vedi `dpr-380-2001-regimi-edilizi.md`):
> - **art. 36**: opere PdC/SCIA-alternativa-dovute realizzate in **assenza** o **totale difformita'** -> doppia conformita' piena.
> - **art. 36-bis**: parziali difformita' (art. 34), variazioni essenziali (art. 32), abusi del regime SCIA art. 22 (art. 37) -> doppia conformita' alleggerita.
> - **art. 6-bis co. 5**: CILA omessa -> sanzione pecuniaria, non procedimento di sanatoria art. 36/36-bis.
> - **Termini procedimentali**: PdC in sanatoria art. 36-bis = 45 gg con **silenzio-assenso** (co. 6); SCIA in sanatoria = termine art. 19 co. 6-bis L. 241/1990; sospensione per parere Soprintendenza.

### Passo 4 - Allegati locali / SUE-specifici

Segnalare sempre che il **Comune puo' richiedere allegati aggiuntivi**:
- Modulistica regionale (es. sismica regionale, paesaggio regionale)
- Dichiarazioni anti-mafia per appalti pubblici
- Dichiarazioni su tributi locali (TARI, IMU)
- Allegati per tematiche specifiche (verde pubblico, accessibilita' rafforzata, energia)
- Pareri di Comitati locali (es. Commissione del Paesaggio, Commissione Edilizia)

### Passo 5 - Output

Produci il report nel formato:

```markdown
# Elenco allegati - Modulo [nome modulo]

**Data**: [oggi]
**Modulo**: [Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis]
**Riferimento normativo**: art. [X] DPR 380/2001
**Modulistica unificata**: Conferenza Unificata 27/3/2025 (Salva Casa)
**Inquadramento intervento**:
- Tipologia: [...]
- Vincoli: [...]
- Cantiere: [...]
- Attivita' antincendio: [...]
- Intervento energetico: [...]

## 1. Allegati sempre obbligatori (base + specifici del modulo)

| # | Allegato | Forma | Riferimento |
|---|----------|-------|-------------|
| 1 | Procura speciale (se delega) | Firma digitale | art. 21 DPR 445/2000 |
| 2 | ... | ... | ... |

## 2. Allegati condizionali (con condizione esplicita)

| # | Allegato | Quando obbligatorio | Riferimento |
|---|----------|----------------------|-------------|
| 1 | Notifica preliminare cantiere | [si / no in funzione del cantiere] | art. 99 D.Lgs. 81/2008 |
| 2 | Autorizzazione paesaggistica | [si / no in funzione del vincolo] | art. 146 D.Lgs. 42/2004 |
| ... | ... | ... | ... |

## 3. Allegati facoltativi / a discrezione SA

[Eventuale lista]

## 4. Allegati locali / SUE-specifici

- Modulistica regionale [LR di settore]
- Dichiarazioni su tributi locali
- Pareri Commissioni locali (Paesaggio, Edilizia)
- Eventuali integrazioni del regolamento edilizio comunale

## 5. Avvertenze e rinvio professionale

- L'elenco e' generato sulla base dei dati dichiarati; **integrazioni locali** del Comune possono aggiungere allegati specifici.
- L'asseverazione del tecnico abilitato copre la conformita' urbanistico-edilizia ma **non sostituisce** i pareri di enti terzi (Soprintendenza, ASL, VVF, Ufficio Sismica).
- Il **modulo nazionale** e' integrabile e adattato dal Comune: scaricare sempre il modulo dal portale SUE/SUAP del Comune competente.
- L'output non sostituisce la **firma del tecnico abilitato**.

**La presente checklist e' uno strumento di supporto e non sostituisce il giudizio del tecnico abilitato firmatario ne' l'istruttoria del SUE/SUAP.**
```

## Casi limite da gestire

### Modulo "concentrato" (vincoli multipli)

Se l'intervento ricade in piu' vincoli (paesaggio + sismica + idrogeologico), gli allegati si **sommano**, e si attiva la **Conferenza dei Servizi** (CdS) o la **richiesta tramite SUAP** che concentra i pareri. Segnalare: "ricorrono presupposti per CdS / SUAP - tempi e iter da concordare con il Comune".

### Pertinenze e opere minori

Per pertinenze e opere minori (es. tettoia di 15 mq), gli allegati sono spesso ridotti rispetto a una manutenzione straordinaria piena. Verificare con il Comune se accetta una "scheda intervento semplificata" allegata al CILA.

### Sanatoria con piu' opere abusive di regime diverso

Se nello stesso immobile ci sono opere abusive in regimi diversi, servono istanze distinte (o un'unica istanza con prospetti separati per ciascun regime): art. 36 per assenza/totale difformita' da PdC o SCIA alternativa; art. 36-bis per parziali difformita' (art. 34), variazioni essenziali (art. 32) e abusi del regime SCIA art. 22 (ex art. 37); art. 6-bis co. 5 (sanzione pecuniaria) per CILA omessa. Segnalalo al SUE.

### Antincendio post-modifica (CILA non sufficiente)

Se l'intervento modifica un'attivita' soggetta DPR 151/2011 in modo significativo, NON basta una CILA: serve la **valutazione di progetto VVF** (cat. B/C) o la **SCIA antincendio** (cat. A/B/C) PRIMA o CONTESTUALMENTE alla CILA edilizia. Avvisare l'utente.

## Limiti di questo task

- Genera **l'elenco degli allegati**, non i contenuti tecnici.
- Non valuta la **completezza tecnica** di un singolo allegato.
- Non integra automaticamente le **integrazioni regionali e comunali**.
- Non sostituisce il **modulo nazionale o regionale** specifico (la skill cita la struttura, non riempie il PDF).
- Non emette **pareri di accettabilita'** della pratica al SUE.

## Esempi

Vedi `examples/`:
- `manutenzione-frazionamento-cila/` - elenco allegati per CILA con frazionamento UI
- `cambio-uso-salva-casa-scia/` - allegati per SCIA cambio destinazione d'uso
- `sanatoria-semplificata-art36bis/` - allegati per sanatoria art. 36-bis
