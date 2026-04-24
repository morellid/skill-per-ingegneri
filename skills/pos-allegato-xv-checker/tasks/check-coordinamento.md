# Task: Verifica coordinamento e gestione interferenze

Verifica che il POS documenti adeguatamente il coordinamento con le altre imprese esecutrici, la gestione delle interferenze tra lavorazioni, e la conformita' agli obblighi art. 96 (e se POS affidataria, art. 97 co. 3) del D.Lgs. 81/2008.

## Obiettivo

Produrre un report strutturato che indichi:
- Presenza e adeguatezza dei riferimenti al PSC e al CSE
- Identificazione delle altre imprese previste in cantiere
- Misure di coordinamento attivo documentate (riunioni, procedure, comunicazioni)
- Identificazione e mitigazione delle interferenze
- Conformita' agli obblighi art. 96 D.Lgs. 81

## Input richiesti

- Sezione(i) del POS su: accettazione PSC, coordinamento, interferenze, sfasamento
- Idealmente: PSC di riferimento (per confronto incrociato)
- Idealmente: elenco delle imprese esecutrici e subappaltatori previsti
- Tipologia POS: impresa affidataria (obblighi aggiuntivi art. 97) o impresa esecutrice (obblighi art. 96)

## Fonti normative

Leggere prima:
- `references/estratti/dlgs-81-art-96-97.md` completo (art. 96 co. 1 lett. a-g, co. 1-bis, co. 2; art. 97 co. 1, 2, 3 lett. a-b, 3-bis, 3-ter)
- `references/estratti/allegato-xv-testo.md` punto 3.2.1 lett. d), g), h), l)

## Procedura

### Passo 1 - Verifica riferimenti al PSC e al CSE

Controllare nel POS:
- [ ] Citazione esplicita del PSC con identificazione (nome CSP, data, revisione)
- [ ] Dichiarazione di presa visione, accettazione e vincolo al PSC
- [ ] Indicazione del CSE nominato (ove nominato)
- [ ] Impegno a rispettare eventuali modifiche al PSC in fase di esecuzione

Se il cantiere non ha PSC (fuori campo Titolo IV Capo I):
- Verificare che il POS dichiari esplicitamente l'assenza di PSC
- In tal caso gli obblighi di coordinamento ricadono sul datore di lavoro ex art. 26 (DUVRI)

### Passo 2 - Verifica identificazione altre imprese

Controllare:
- [ ] Elenco delle altre imprese esecutrici previste in cantiere (anche se preliminare)
- [ ] Elenco subappaltatori (se l'impresa del POS e' affidataria)
- [ ] Lavoratori autonomi subaffidatari dichiarati (voce a.2 dell'Allegato XV 3.2.1)
- [ ] Indicazione di quando ciascuna impresa intervira' (fase del cronoprogramma)

Flag: POS che dichiara "nessuna altra impresa" senza spiegazione in cantieri di dimensione tale da richiederle quasi certamente (es. nuova costruzione senza subappalto elettrico, idraulico, finiture).

### Passo 3 - Verifica misure di coordinamento attivo

Il POS dovrebbe documentare almeno:
- [ ] Riunioni di coordinamento periodiche (frequenza, chi partecipa)
- [ ] Procedure di comunicazione tra imprese e con CSE (telefono, app, riunioni ad hoc)
- [ ] Referente operativo per il coordinamento (nome, ruolo)
- [ ] Registrazione delle attivita' di coordinamento (verbali, registro presenze)

Flag: POS che usa formula "si terranno riunioni di coordinamento" senza specificare frequenza, modalita', partecipanti.

### Passo 4 - Verifica gestione interferenze

Le interferenze possono essere:
- **Temporali**: stessa area, momenti diversi (es. demolizione prima, posa pavimenti dopo)
- **Spaziali**: stesso tempo, aree diverse (es. piano terra elettrici, piano 1 muratori)
- **Incrociate**: stesso tempo, stessa area (rare e da evitare - serve sfasamento o coordinamento intensivo)

Controllare:
- [ ] Identificazione delle interferenze attese (o dichiarazione "nessuna interferenza" motivata)
- [ ] Misure specifiche per ciascuna interferenza
- [ ] Eventuale sfasamento temporale o spaziale documentato nel cronoprogramma
- [ ] Riferimento alle misure del PSC punto 2.3 (se disponibile)

Flag: POS generici come "le interferenze saranno gestite dal CSE" senza contributo proprio alla mitigazione (viola l'obbligo art. 96 co. 1 lett. g - il POS deve includere il contributo dell'impresa alla sicurezza).

### Passo 5 - Verifica art. 96 (obblighi base impresa)

Per ogni lettera dell'art. 96 co. 1, il POS dovrebbe contenere elementi di conformita':

| Lett | Obbligo | Elementi attesi nel POS |
|------|---------|------------------------|
| a | Misure conformi Allegato XIII | Riferimento o descrizione (prescrizioni per i cantieri) |
| b | Accesso e recinzione visibili | Descrizione accesso cantiere, recinzione, cartellonistica |
| c | Disposizione materiali senza crollo | Procedure di stoccaggio, aree deposito |
| d | Protezione influenze atmosferiche | Teli, ripari, procedure sospensione per vento/pioggia/caldo |
| e | Rimozione materiali pericolosi | Procedure con coordinamento committente/RL (es. amianto) |
| f | Stoccaggio/evacuazione detriti | Big-bag, autotrasporto, formulari rifiuti |
| g | Redazione POS | Il POS stesso e' attuazione di questo obbligo |

Flag assenze significative, ma segnalarle come "verifica formale" - l'obbligo e' pratico, il POS documenta.

### Passo 6 - Se POS affidataria: verifica art. 97 co. 3

Obblighi aggiuntivi per l'impresa affidataria:
- [ ] Coordinamento tra interventi propri e esecutrici (art. 97 co. 3 lett. a)
- [ ] Verifica congruenza POS delle esecutrici rispetto al proprio (lett. b)
- [ ] Trasferimento senza ribasso degli oneri sicurezza alle esecutrici (co. 3-bis) - vedi anche `check-costi-sicurezza.md`
- [ ] Formazione adeguata del DdL, dirigenti, preposti (co. 3-ter)

Flag: POS affidataria che non documenta la verifica di congruenza dei POS delle esecutrici (oggi sempre piu' richiesto in sede di verifica).

### Passo 7 - Output

```markdown
# Verifica coordinamento e interferenze

**Data verifica**: [data]
**POS analizzato**: [id]
**Tipologia**: [impresa affidataria | impresa esecutrice | impresa in proprio senza subappalti]
**Contesto cantiere**: [se dichiarato]

## Sintesi

- Riferimento PSC: [SI/NO/NON APPLICABILE] - [dettaglio]
- CSE identificato: [SI/NO]
- Altre imprese documentate: [SI/NO/NON APPLICABILE]
- Misure di coordinamento attivo: [STRUTTURATE/GENERICHE/ASSENTI]
- Interferenze trattate: [N identificate con misure | NESSUNA con motivazione | OMISSIONE]
- Conformita' art. 96: [completa/parziale/lacunosa]
- Conformita' art. 97 (se affidataria): [documentata/non documentata]

**Esito**: [CONFORME | CONFORME CON NOTE | LACUNOSO | NON CONFORME]

## Dettaglio

### Riferimenti PSC/CSE
- PSC: [citazione nel POS e dettaglio]
- CSE: [nome e ruolo se dichiarato]
- Dichiarazione di accettazione PSC: [SI/NO]

### Altre imprese e subappalti
- Impresa affidataria: [nome]
- Imprese esecutrici: [elenco]
- Subappaltatori: [elenco]
- Lavoratori autonomi: [elenco]
- Fasi di intervento: [sommario]

### Coordinamento attivo
- Riunioni: [frequenza/modalita'/partecipanti]
- Comunicazioni: [canali]
- Referente operativo: [nome/ruolo]
- Registrazione: [modalita']

### Interferenze
- Temporali identificate: [lista]
- Spaziali identificate: [lista]
- Misure per ognuna: [lista]
- Sfasamento documentato: [SI/NO]

### Art. 96 - compliance
| Lettera | Stato nel POS |
|---------|---------------|
| a) Allegato XIII | ... |
| b) Accesso/recinzione | ... |
| ... | ... |

### Art. 97 (se affidataria)
- Coordinamento con esecutrici: ...
- Verifica congruenza POS esecutrici: ...
- Trasferimento oneri sicurezza: ...
- Formazione DdL/dirigenti/preposti: ...

## Problemi rilevati
| # | Area | Problema | Riferimento | Priorita' |
|---|------|----------|-------------|-----------|
| ... |

## Raccomandazioni
...

## Limiti
- Verifica su documento, non su cantiere.
- Non e' possibile verificare che il coordinamento dichiarato avvenga realmente.
- La congruenza POS affidataria vs POS esecutrici richiede tutti i POS del cantiere (raramente disponibili alla skill).
- Le interferenze reali emergono spesso in esecuzione e non sono prevedibili dal documento.

## Rinvio al professionista firmatario
**Il coordinamento effettivo in cantiere e' responsabilita' del CSE ex art. 92 D.Lgs. 81/2008. Questo report verifica la documentazione scritta, non la pratica operativa.**
```

## Casi limite

### POS di impresa unica senza PSC
Se il cantiere ha unica impresa e rientra nei casi di esclusione PSC, il POS non ha coordinamento esterno da documentare. Il report si concentra su:
- Dichiarazione motivata di assenza PSC/altre imprese
- Conformita' art. 96 per gli obblighi base
- Eventuale coordinamento con committente ex art. 26 DUVRI

### Dichiarazione "nessuna interferenza" in cantieri complessi
In cantieri di nuova costruzione oltre una certa entita', l'assenza totale di interferenze e' improbabile (muratori + elettricisti + idraulici + coperture + finiture). Dichiarazioni generiche di "nessuna interferenza" vanno flaggate come sospette.

### Affidataria con molti subappalti non dichiarati
Se il POS affidataria non elenca i subappaltatori previsti (anche se l'elenco e' preliminare), e' carenza di trasparenza. In esecuzione sara' necessario aggiornare con verbali/varianti, ma l'elenco iniziale dovrebbe esserci.

## Limiti di questo task

- Verifica documentale. Non puo' dire se il coordinamento "funzionera'" in cantiere.
- Non dispone dei POS delle altre imprese per verifiche incrociate reali.
- Non verifica l'effettiva presenza alle riunioni dichiarate.
- La responsabilita' finale del coordinamento operativo e' del CSE.

## Esempi

Vedi `examples/`:
- `coordinamento-affidataria-strutturato/` - POS affidataria con altre imprese, riunioni, interferenze, art. 97 documentato
- `coordinamento-generico-lacunoso/` - POS con riferimenti generici senza contenuto operativo
