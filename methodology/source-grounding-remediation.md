# Source-grounding remediation - workflow corretto

> Documento operativo per chi (agent o umano) deve sistemare una skill non conforme alla Regola zero (vedi `AGENTS.md`).

## Cosa significa "remediation"

Una skill che ha `sha256: REPLACE_WHEN_DOWNLOADED`, `sha256: null` su fonti con `binary_path` non null, o estratti scritti senza lettura del PDF e' in violazione della Regola zero. **Remediation** vuol dire portarla in conformita': non basta cambiare l'hash, serve verificare che ogni contenuto della skill sia tracciabile al testo del PDF realmente letto.

## Cosa NON e' remediation

Sono **anti-pattern** vietati:

- **"Calcolo l'SHA256 via CI e committo"**: fa passare il check sintattico ma non rende la skill source-grounded. Le PR #115-#120 di maggio 2026 sono state chiuse per questo motivo.
- **"Cambio i placeholder in `null` cosi' la CI smette di lamentarsi"**: aggira la regola, non la rispetta. Se la fonte non puo' essere scaricata, va applicato il protocollo di rifiuto (vedi sotto).
- **"Lascio gli estratti come sono e aggiorno solo il `sources.yaml`"**: gli estratti scritti dai training data restano invenzione, anche con SHA256 reale a fianco. Una skill "con hash giusto ma estratti inventati" e' identica per la Regola zero a una "con hash sbagliato e estratti inventati".
- **"Sostituisco una fonte difficile da scaricare con una piu' accessibile"**: se non e' la fonte ufficiale, non vale. Non mettere "Wikipedia art. X" al posto di "G.U. del N del Y/Z/W art. X".

## Workflow corretto (per ogni skill non conforme)

### Step 1: leggi i PDF

Hai bisogno di **leggere** ogni PDF dichiarato in `sources.yaml`. Senza questo passo la remediation non puo' iniziare.

Se non puoi leggere il PDF (sandbox blocca host normativi, paywall, fonte ritirata, paese non supportato): **fermati e applica il protocollo di rifiuto** (`AGENTS.md` Regola zero). NON proseguire delegando a CI il solo calcolo dell'hash.

Vie alternative consentite per ottenere accesso al PDF:

1. l'utente fornisce il file via mirror su `raw.githubusercontent.com/<repo>/...`
2. l'utente paste-incolla il testo dei paragrafi rilevanti in un'issue o commento
3. l'utente carica i file in un bucket accessibile e fornisce URL + SHA256 calcolato localmente

Dopo aver ricevuto accesso, **leggi davvero il PDF**. Annota: numero pagina di ogni paragrafo citato, numero della tabella, esatto enunciato delle formule.

### Step 2: riscrivi gli estratti

Apri ogni `references/estratti/*.md` e confrontalo con quanto hai letto nel PDF. Per ogni affermazione presente nell'estratto:

- se il PDF la conferma testualmente: lascia, ma aggiungi citazione precisa (paragrafo + pagina)
- se il PDF la conferma con formulazione diversa: riscrivi parafrasando IL TESTO LETTO, citando paragrafo + pagina
- se il PDF NON la conferma: cancella l'affermazione (era invenzione dei training data)
- se il PDF dice cose che l'estratto non riporta e che sono rilevanti per la skill: aggiungile, citando

L'estratto risultante deve essere ricostruibile leggendo solo il PDF. Niente affermazioni non rintracciabili.

### Step 3: verifica le costanti del codice

Per ogni costante numerica nel codice di calcolo della skill (modulo Python in `tasks/lib/`, valori in tabelle dei `tasks/*.md`, ecc.):

- trova il punto del PDF dove la costante e' definita
- verifica letteralmente il valore (controlla anche il segno, l'unita' di misura, eventuali condizioni di applicabilita')
- aggiungi un commento nel codice con riferimento al paragrafo/tabella/equazione del PDF

Se una costante non e' rintracciabile nel PDF (es. perche' viene da un testo a pagamento o da un articolo accademico): rimuovila e rendi il valore un input dell'utente, oppure rinvia ad altra fonte verificabile (con relativa entry in `sources.yaml`).

### Step 4: verifica i tasks e gli examples

Stesso esercizio per `SKILL.md`, `AGENTS.md` (di skill), `tasks/*.md`, `examples/*/`: ogni affermazione normativa deve poter puntare a un paragrafo/articolo del PDF letto.

### Step 5: aggiorna sources.yaml e calcola gli hash

Solo dopo i passi 1-4:

```bash
./scripts/fetch-sources.sh <nome-skill>   # scarica i PDF dichiarati e committa SHA256 reali
./scripts/validate.sh <nome-skill>          # verifica che il check sintattico passi
```

Se sei in ambiente con sandbox che blocca i download: il fetch dei PDF e il calcolo degli hash possono essere delegati a CI tramite il workflow `auto-fetch-sources.yml` (se presente nel repo) **a condizione che lo step 1-4 sia stato completato lavorando su una copia del PDF ottenuta via protocollo di rifiuto**.

### Step 6: changelog e PR

- entry in `CHANGELOG.md` di skill di tipo `fix(source-grounding)` che descrive cosa hai cambiato negli estratti / nelle costanti del codice
- PR che cita l'issue di remediation con `Closes #N`
- la descrizione della PR deve elencare:
  - quali estratti sono stati riscritti
  - quali costanti del codice sono state verificate (e se qualcuna e' cambiata, motivare)
  - quali eventuali affermazioni sono state cancellate perche' non rintracciabili
  - link al PDF (URL della fonte ufficiale + SHA256)

## Criteri di chiusura issue

Una issue P1 di remediation puo' essere chiusa solo se la PR associata:

1. fa passare il workflow `source-grounding.yml` (check sintattico, necessario)
2. ha description che documenta esplicitamente lo step 2-4 (verifica semantica, necessario)
3. e' stata reviewed da un secondo paio di occhi (umano o agent indipendente che a sua volta ha letto il PDF) che confermi che gli estratti riflettono il testo letto

**Senza il punto 2 e 3, la PR non e' remediation. E' una scorciatoia, e va respinta.**

## Esempi storici

- **Mergati conformi**: `combinazioni-carico-ntc` (sha256 NTC 2018 reale, estratti coerenti con par. 2.5-2.6 NTC).
- **Aperti non conformi**: PR #89 (`predimensionamento-flessione-ca-ntc`), PR #90 (`cedimenti-edometrici-ntc`) - estratti scritti dai training data, costanti del codice non verificate vs PDF, hash placeholder. Bloccati pending remediation completa.
- **Chiusi per anti-pattern**: PR #115-#120 - tentavano di chiudere issue P1 con il solo calcolo SHA256 via CI, senza lettura del PDF e senza riscrittura degli estratti. Tutte chiuse.
