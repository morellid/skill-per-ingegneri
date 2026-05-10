# Task: Stesura DVR (D.Lgs. 81/2008 art. 28-29)

Costruisce un DVR conforme ai contenuti minimi dell'art. 28 co. 2, sulla base delle informazioni dell'azienda fornite dall'utente.

## Obiettivo

Produrre un documento strutturato che contenga i 6 elementi obbligatori dell'art. 28 co. 2 (lett. a-f) + indicazione dei rischi specifici dei Titoli dedicati del D.Lgs. 81 + apparato di firme e data certa.

Per imprese fino a 10/50 lavoratori e' supportata anche la modalita' "procedure standardizzate" (DM 30/11/2012).

## Input richiesti

### Anagrafica azienda
- Ragione sociale, P.IVA, sede legale, sede operativa
- Codice ATECO (e specificita' attivita')
- Numero lavoratori (per scelta procedura)
- Data inizio attivita' (rilevante per art. 28 co. 3-bis - 90 giorni)

### Soggetti
- Datore di lavoro (nome)
- RSPP (nome, interno/esterno, attestati)
- Medico competente (se nominato - obbligatorio nei casi art. 41)
- RLS o RLST (consultazione obbligatoria art. 29 co. 2)
- Addetti emergenze (PS, AI, evacuazione)
- Preposti, dirigenti

### Mansioni e numero lavoratori per mansione
Ogni mansione e' un'unita' di valutazione rischi.

### Luoghi di lavoro
Sedi, aree (uffici, magazzino, produzione, laboratorio, ecc.)

### Attrezzature di lavoro
Macchine, utensili, attrezzi, mezzi di trasporto

### Sostanze e miscele
Chimiche, biologiche

### Tipologie di rischio attese
(la skill puo' suggerire mappatura standard - vedi `mappa-rischi-mansione.md`)

## Fonti

Leggere prima:
- `references/estratti/dlgs-81-art-17-28-29.md` - 6 contenuti minimi DVR + modalita'

## Procedura

### Passo 1 - Verifica scelta della procedura

| N. lavoratori | Settore | Procedura |
|----------------|---------|-----------|
| Fino a 10 | Standard (no esclusi art. 31 co. 6 lett. a-d, g) | Procedure standardizzate (DM 30/11/2012) - obbligatorie |
| Fino a 50 | Standard (no rischi chimici/biologici/ATEX/cancerogeni/amianto) | Procedure standardizzate facoltative O DVR completo |
| > 50 oppure settori esclusi | Qualsiasi | DVR completo art. 28-29 |

In caso di dubbio, optare per **DVR completo**.

### Passo 2 - Intestazione del DVR

```markdown
## DOCUMENTO DI VALUTAZIONE DEI RISCHI

**Riferimento normativo**: D.Lgs. 81/2008 art. 17 co. 1 lett. a), art. 28, art. 29
**Versione**: v1.0 - [data]
**Stato**: bozza (richiede firma DdL/RSPP/RLS/MC per data certa)

### Anagrafica
- Ragione sociale: [...]
- P.IVA / CF: [...]
- Sede legale: [...]
- Unita' produttive: [...]
- Codice ATECO: [...]
- Attivita' principale: [...]

### Soggetti del SPP
- Datore di lavoro: [...]
- RSPP: [nome, ruolo interno/esterno, attestati]
- Medico competente: [se nominato] / [non obbligatorio per: motivazione]
- RLS / RLST: [nome o territoriale]
- Addetti PS: [nominativi + attestati]
- Addetti AI: [nominativi + attestati]
- Preposti: [...]

### Lavoratori
- Numero totale: N
- Distribuzione per mansione:
  - Mansione 1: N lavoratori
  - Mansione 2: N lavoratori
  ...
- Tipologie contrattuali: [tempo determinato, somministrato, autonomi presenti, ecc.]
```

### Passo 3 - Lettera a) Relazione sulla valutazione dei rischi

Per ogni mansione/luogo/attivita':

1. **Identifica i rischi** usando una checklist tassonomica (vedi `mappa-rischi-mansione.md` per template per mansione)
2. **Stima** ciascun rischio per probabilita' (P) e gravita' (G), entrambe 1-4
3. **Calcola rischio = P x G** (1-16) e classifica:
   - 1-2: trascurabile
   - 3-4: basso
   - 5-8: medio
   - 9-16: alto
4. **Documenta**: descrivere ciascun rischio identificato

Criteri adottati per la valutazione (esempio):
- Metodologia matriciale P x G
- Riferimenti tecnici: linee guida INAIL settoriali, ISO 45001, riferimenti UNI per rischi specifici (es. ISO 11228 per MMC)
- Coinvolgimento RSPP + medico competente (per rischi sanitari)

### Passo 4 - Lettera b) Misure di prevenzione e protezione attuate + DPI

Per ogni rischio, indicare misure attuate:

```markdown
| Rischio | Misure preventive | Misure protettive | DPI | Stato |
|---------|-------------------|-------------------|-----|-------|
| Rischio caduta dall'alto | Parapetti H 1m su passerelle | Linea vita per manutenzione tetto | Imbracatura EN 361 + cordino EN 355 | Attuato |
| Rischio rumore lavorazioni meccaniche | Insonorizzazione macchine | Cabina insonorizzata | Cuffie SNR>30 dB | Attuato |
| ... | ... | ... | ... | ... |
```

### Passo 5 - Lettera c) Programma di miglioramento

Identificare i rischi residui (per cui le misure attuate non sono ottimali) e proporre programma di miglioramento:

```markdown
| Misura prevista | Rischio mitigato | Tempi | Responsabile | Costo stimato |
|-----------------|------------------|-------|---------------|---------------|
| Sostituzione macchina X con modello a vibrazioni ridotte | Vibrazioni MMC | Q3 2026 | Direttore produzione | EUR 25.000 |
| Adozione esoscheletro per movimentazione carichi | MMC | Q4 2026 | RSPP | EUR 8.000 |
| ... | ... | ... | ... | ... |
```

### Passo 6 - Lettera d) Procedure di attuazione + ruoli

Indicare le procedure operative + chi le esegue:

```markdown
- **Procedura PR-001 - Uso DPI**: tutti i lavoratori, supervisione preposto
- **Procedura PR-002 - Lockout/tagout per manutenzione**: manutentori, supervisione capo manutenzione
- **Procedura PR-003 - Emergenza incendio**: tutti, gestione addetti AI
- **Procedura PR-004 - Pronto soccorso**: addetti PS
- **Procedura PR-005 - Movimentazione manuale carichi**: addetti magazzino, formazione
- **Procedura PR-006 - Manutenzione attrezzature**: ufficio manutenzione, periodicita' definita
- ...
```

Roles:
- Datore di lavoro: responsabile generale
- RSPP: coordinamento, monitoraggio, aggiornamento DVR
- Medico competente: sorveglianza sanitaria + idoneita'
- Preposto: vigilanza diretta + segnalazione anomalie
- Lavoratore: uso DPI, segnalazione rischi, partecipazione formazione

### Passo 7 - Lettera e) Nominativi soggetti partecipanti alla valutazione

```markdown
La presente valutazione e' stata effettuata in collaborazione tra:
- Datore di lavoro: [nome] - firma: ...
- RSPP: [nome] - firma: ...
- Medico competente: [nome se applicabile] - firma: ...
- Consultato il RLS: [nome] - firma: ... (data consultazione: ...)
```

Sottoscrizione di tutti = data certa (art. 28 co. 2).

### Passo 8 - Lettera f) Mansioni a rischio specifico

Mansioni che richiedono **riconosciuta capacita' professionale, specifica esperienza, adeguata formazione e addestramento**. Esempi tipici:

- Lavorazioni elettriche sotto tensione (PES, PAV, PEI)
- Movimentazione carichi sospesi (gru a torre, autogru)
- Lavori in spazi confinati (DPR 177/2011)
- Lavori in quota (corso formazione + visita medica idoneita')
- Saldature in atmosfere a rischio
- Manutenzione sistemi a pressione
- Esposti ad amianto (formazione abilitante)

Per ciascuna: dichiarare formazione richiesta + addestramento.

### Passo 9 - Sezioni specifiche dei Titoli D.Lgs. 81

A seconda delle attivita' aziendali, integrare con sezioni specifiche:

| Titolo | Cosa | Quando applicabile |
|--------|------|---------------------|
| II - Luoghi di lavoro | Layout, vie esodo, microclima, illuminazione | Sempre |
| III - Attrezzature + DPI | Conformita' macchine, DPI per rischio | Sempre |
| IV - Cantieri | Rinvio POS/PSC | Solo per attivita' in cantieri |
| V - Segnaletica | Segnaletica salute/sicurezza | Sempre |
| VI - Movimentazione manuale carichi | Valutazione MMC | Per lavoratori che movimentano > 3 kg ripetitivi |
| VII - Videoterminali | Valutazione VDT | Per VDT > 20h/settimana |
| VIII Capo II - Rumore | LEX,8h, picchi, soglie | Sempre per ambienti rumorosi |
| VIII Capo III - Vibrazioni | A(8) mano-braccio o corpo intero | Per uso attrezzi vibranti o veicoli |
| VIII Capo IV - CEM | Misurazioni / valutazione | Per esposizioni significative (saldatura ad arco, RM, ecc.) |
| VIII Capo V - Ottiche | Laser, IR, UV | Per attivita' specifiche |
| IX - Agenti chimici | Schede SDS, esposizioni, valutazione | Se uso sostanze chimiche |
| IX Capo II - Cancerogeni / mutageni / RT | Sostanze in lista | Se applicabile |
| X - Biologici | Esposizioni accidentali o intenzionali | Sanita', allevamento, rifiuti, lab |
| XI - ATEX | Zone, sorgenti rilascio | Se atmosfere esplosive |

### Passo 10 - Stress lavoro-correlato (art. 28 co. 1-bis)

Sezione obbligatoria. Metodologia INAIL/Commissione Consultiva:

**Fase 1 - valutazione preliminare** (indicatori oggettivi):
- Eventi sentinella: infortuni, malattie professionali, assenze, turnover, sanzioni disciplinari
- Fattori di contenuto: orario, carico, autonomia, monotonia
- Fattori di contesto: relazioni, autorita', sviluppo carriera, ruolo

Se la fase 1 evidenzia rischi -> **Fase 2 - valutazione approfondita** (questionari ai lavoratori, focus group, interviste).

### Passo 11 - Differenze (art. 28 co. 1)

Sezione che valuta:
- **Genere**: rischi specifici per donne (gravidanza, allattamento, scarsita' fisica per certi sforzi)
- **Eta'**: lavoratori giovani (D.Lgs. 345/1999), lavoratori anziani
- **Provenienza**: lavoratori stranieri (formazione in lingua, cultura sicurezza)
- **Tipologia contrattuale**: somministrati, distaccati, autonomi che lavorano in azienda

### Passo 12 - Output finale

Documento strutturato con tutte le sezioni. Possibili formati:
- Word/PDF (tradizionale)
- Sistema informatizzato con marca temporale
- Foglio elettronico per matrice rischi (riferito da documento principale)

Custodia: presso unita' produttiva (art. 29 co. 4). Disponibile a ispezioni autorita'.

## Procedura semplificata "procedure standardizzate" (DM 30/11/2012)

Per imprese fino a 10/50 lavoratori, esiste un **modello semplificato** approvato dalla Commissione Consultiva.

Schema:
1. **Modulo 1 - Anagrafica azienda**
2. **Modulo 2 - Identificazione fattori di rischio per area di rischio** (lista predefinita)
3. **Modulo 3 - Valutazione dei rischi** (matrice P x G)
4. **Modulo 4 - Programma miglioramento**
5. **Modulo 5 - Verbale consultazione RLS**

Il modello e' meno discrezionale (riduce rischio errore di omissione) ma comunque strutturato.

INAIL ha pubblicato esempi compilati per molti settori.

## Output strutturato

Il task produce documento markdown completo strutturato. Esempio iniziale:

```markdown
# DVR - [nome azienda]

[intestazione]
[lett. a) relazione]
[lett. b) misure]
[lett. c) programma]
[lett. d) procedure + ruoli]
[lett. e) nominativi e firme]
[lett. f) mansioni a rischio specifico]
[Titoli specifici applicabili]
[Stress lavoro-correlato]
[Differenze]

## Avvertenze

- Documento bozza redatto con strumento di supporto. **Va revisionato dal RSPP** [nome], **consultato il RLS** [nome], integrato del **medico competente** [nome se applicabile], e firmato dal **datore di lavoro** [nome] per acquisire data certa.
- Aggiornamento obbligatorio in caso di: modifiche significative processo/organizzazione, infortuni significativi, sorveglianza sanitaria che lo richiede (vedi task `valuta-aggiornamento.md`).
- Custodia presso unita' produttiva (art. 29 co. 4).

Sanzioni applicabili: arresto da tre a sei mesi o ammenda da 2.500 a 6.400 euro per omessa redazione DVR (art. 55 co. 1).
```

## Casi limite

### Nuova impresa
Art. 28 co. 3-bis: 90 giorni dall'inizio per redigere il DVR. Nel frattempo, evidenza documentale di adempimento art. 28 co. 2 lett. b/c/d/e/f + comunicazione al RLS.

### Datore di lavoro che svolge anche RSPP
Possibile per piccole imprese (art. 34) con specifica formazione RSPP-DdL. Indicare nel DVR.

### Azienda senza dipendenti diretti (solo soci/familiari)
Spesso fuori dall'obbligo D.Lgs. 81 ma applicabile DPR 547/55 e altri. Verificare caso per caso. Per "lavoro accessorio", "occasionale", "tirocini": diversi regimi.

### DVR informatizzato
Strumenti come OIRA INAIL, software commerciali (Blumatica, Acca, ecc.). Output deve comunque rispettare contenuti minimi art. 28 co. 2.

## Limiti di questo task

- Skill non sostituisce la valutazione tecnica del RSPP/medico competente
- Per misurazioni quantitative (rumore, vibrazioni, chimico, ecc.) servono tecnici abilitati con strumentazione tarata
- Per settori specialistici (sanita', industria pesante) potrebbero esserci linee guida specifiche da integrare

## Esempi

Vedi `examples/`:
- `dvr-pmi-ufficio/` - PMI 25 dipendenti settore servizi (uffici + smart working)
