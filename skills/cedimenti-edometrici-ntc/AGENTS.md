# AGENTS.md - cedimenti-edometrici-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per la stima del cedimento edometrico (compressione monodimensionale) di singolo strato omogeneo, ai fini delle verifiche agli stati limite di esercizio (SLE) di NTC 2018 par. 6.2.4. Riferimenti normativi: DM 17/01/2018 (NTC 2018) e Circolare MIT 21/01/2019 n. 7. Riferimento didattico/tecnico: meccanica dei terreni classica (Terzaghi 1925, Skempton 1944, Lancellotta "Geotecnica"). Target: ingegneri strutturisti e geotecnici italiani in fase di pre-dimensionamento.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **NTC 2018** (DM 17/01/2018) - id `ntc2018-dm-17-01-2018`, hash da calcolare al fetch
- **Circ. 7/2019 MIT** (21/01/2019) - id `circ-7-2019-mit`, hash da calcolare al fetch
- **Lancellotta R., "Geotecnica"** - id `lancellotta-geotecnica`, riferimento didattico (non incorporato; testo a pagamento)

Estratti pertinenti in `references/estratti/`:
- `ntc2018-par-6-2.md` - par. 6.2.2 e 6.2.4 (interazione terreno-fondazione, verifiche SLE - cedimenti)
- `circ-7-2019-c-6-2.md` - C6.2 commento applicativo
- `formulazione-edometrica-classica.md` - formulazione Terzaghi/Skempton (dominio pubblico tecnico)

## Articoli e punti chiave

- **NTC par. 6.2.2** - analisi dell'interazione terreno-fondazione: il progettista sceglie il metodo di calcolo idoneo
- **NTC par. 6.2.4** - verifiche SLE: cedimento ammissibile dichiarato dal progettista, confronto con cedimento calcolato
- **Circ. 7/2019 par. C6.2** - commento applicativo, rinvio a metodi consolidati di letteratura
- **Formulazione classica** - cedimento edometrico per singolo strato omogeneo:
  - ramo OC (sigma_f' <= sigma_p'): Delta h = h0/(1+e0) * Cr * log10(sigma_f'/sigma_0')
  - ramo NC (sigma_0' >= sigma_p'): Delta h = h0/(1+e0) * Cc * log10(sigma_f'/sigma_0')
  - transizione (sigma_0' < sigma_p' < sigma_f'): Delta h = h0/(1+e0) * [Cr * log10(sigma_p'/sigma_0') + Cc * log10(sigma_f'/sigma_p')]

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti sono materiale di citazione: ti servono per spiegare i passaggi, NON per riprodurre sigma_f, OCR, Delta h, epsilon in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/cedimenti.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non inventare i parametri edometrici** (Cc, Cr, e0, sigma_p'): devono provenire dalla relazione geotecnica o da prove edometriche su campioni indisturbati. La skill non ha database di valori "tipici" perche' la dispersione tra terreni e' troppo elevata; suggerirli a memoria induce in errore il progettista.
- **Non confondere sigma_p' (preconsolidazione, parametro del terreno) con sigma_f' (tensione finale dopo carico)**: sono concetti diversi. sigma_p' viene da prova edometrica (metodo Casagrande / Janbu); sigma_f' = sigma_0' + Delta sigma'.
- **Non eseguire il calcolo per scarico** (Delta sigma' < 0): il modulo solleva ValueError. Per scarichi (rebound) la formula non si applica nello stesso modo; rinviare a metodo specifico.
- **Non eseguire il calcolo per OCR < 1** (sigma_p' < sigma_0'): non e' fisicamente ammissibile (la preconsolidazione non puo' essere inferiore alla tensione attuale). Il modulo solleva ValueError; verificare con il progettista i parametri edometrici dichiarati.
- **Non sommare cedimenti di strati diversi internamente**: la skill calcola SINGOLO strato. Per stratigrafie multilayer il progettista deve ripetere il calcolo per ogni strato e sommare i contributi.
- **Non confondere cedimento totale con cedimento differenziale**: la skill stima il cedimento medio dello strato sotto carico. Differenziali e distorsioni angolari richiedono Delta sigma' puntuale (Boussinesq) e calcoli separati.
- **Non confondere cedimento primario con cedimento secondario** (compressione secondaria, creep): la skill calcola solo il primario di consolidazione. Per il secondario serve Calpha e tempo, fuori scope.
- **Non usare path relativi tipo `tasks/lib/cedimenti.py`** nei comandi Bash: usa sempre `${CLAUDE_SKILL_DIR}/tasks/lib/cedimenti.py` (Claude Code) o il path assoluto della skill installata.

### Cosa fare

- **Citare sempre il riferimento normativo o didattico** per ogni passaggio (es. "ramo OC (sigma_f <= sigma_p) - formulazione classica Terzaghi/Skempton, applicabile per verifiche SLE NTC par. 6.2.4").
- **Eseguire il modulo Python** per il calcolo, non riprodurre i numeri "a mano".
- **Mostrare la struttura completa**: input (h0, e0, Cc, Cr, sigma_0', sigma_p', Delta sigma'), derivati (sigma_f', OCR, ramo), contributi (Delta h OC, Delta h NC), output (Delta h totale m e mm, epsilon), avvertenze.
- **Concludere con rinvio al progettista geotecnico**: la skill stima il cedimento medio di un singolo strato. Per stratigrafie reali, cedimenti differenziali, tempi di consolidazione (Cv), il progettista deve usare metodi specifici. Il confronto con il cedimento ammissibile resta a carico del firmatario.
- **Quando l'utente non e' sicuro su Cc / Cr / sigma_p'**: rinviare alla relazione geotecnica o a prove edometriche, NON suggerire valori a memoria.
- **Quando epsilon > 10%**: la skill produce un'avvertenza. Comunicarla esplicitamente: per deformazioni elevate il metodo edometrico e' approssimato e va validato con prove specifiche.

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere geotecnico che esegua confronto vs casi pubblicati (Lancellotta esempi, Cestari, Holtz & Kovacs) o vs software geotecnico certificato (es. Plaxis, GeoStudio Sigma/W, Settle3D) su almeno 5 casi reali con copertura: terreni argillosi e limosi, OCR da 1 a 5, h0 da 1 a 10 m, Delta sigma' da 50 a 500 kPa.

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh cedimenti-edometrici-ntc`); test suite Python: 28/28 pass (5 classi: OCR, cedimento OC, cedimento NC, end-to-end con copertura ramo OC / NC / transizione + raccordo a sigma_p + avvertenza epsilon > 10%, monotonia in delta_sigma e h0, validazione input fuori dominio Cr > Cc / sigma_p < sigma_0 / scarichi / negativi / NaN; CLI con error handling). Livello 2 (vs casi pubblicati e software geotecnico) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-cedimento.md`
- Modulo di calcolo: `tasks/lib/cedimenti.py` + `tasks/lib/test_cedimenti.py`
- Esempi: 1 conforme (`caso-conforme-strato-argilla-OC-transizione`) + 1 problematico (`caso-problematico-ocr-minore-1`)
