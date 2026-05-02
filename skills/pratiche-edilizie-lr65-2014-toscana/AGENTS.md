# AGENTS.md - pratiche-edilizie-lr65-2014-toscana

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Determinazione del titolo abilitativo edilizio corretto e checklist documentale per pratiche
edilizie in Toscana ai sensi della LR Toscana 10 novembre 2014 n. 65 (LR 65/2014), integrata
con il DPR 380/2001 (Testo Unico Edilizia). Target: ingegneri, architetti, geometri e tecnici
SUE/SUAP che operano in Toscana e devono determinare il regime abilitativo applicabile a un
intervento edilizio e preparare la documentazione per la pratica.

Il rischio principale e' la scelta del titolo abilitativo sbagliato (es. CILA dove serve SCIA,
o SCIA dove serve PdC), con conseguente irregolarita' della pratica, sospensione lavori o
sanzioni. Un secondo rischio rilevante in Toscana e' l'omissione della denuncia/autorizzazione
al Genio Civile per interventi in zona sismica, che comporta illecito penale.

## Fonti autoritative

Fonti catalogate in `references/sources.yaml`:

- **LR Toscana 65/2014** - id `lr-toscana-65-2014` - legge regionale vigente (con modifiche 2019-2024)
- **DPR 380/2001** - id `dpr-380-2001-tue` - Testo Unico Edilizia (applicabile in Toscana per le materie non coperte da LR 65/2014)
- **DPGR 64/R/2018** - id `dpgr-64r-2018-regolamento-edilizio-tipo-toscana` - regolamento edilizio tipo regionale
- **D.Lgs. 42/2004** - id `dlgs-42-2004-codice-paesaggio` - vincoli paesaggistici e beni culturali
- **DM 28/7/2021** - id `dm-28-07-2021-classificazione-sismica` - classificazione sismica vigente
- **NTC 2018** - id `ntc-2018-dm-17-01-2018` - norme tecniche costruzioni (per interventi strutturali)

Estratti in `references/estratti/`:
- `lr-65-2014-titoli-abilitativi.md` - sintesi artt. titoli abilitativi LR 65/2014 (con avvertenza numerazione)
- `dpr-380-2001-artt-zona-sismica.md` - artt. 83, 93, 94, 65 DPR 380/2001 (zone sismiche)

## Articoli e punti chiave

**AVVERTENZA**: La LR 65/2014 ha subito modifiche negli anni 2019, 2020, 2021 e 2024.
La numerazione degli articoli indicata di seguito e' indicativa; verificare sempre il testo
vigente sul portale normativo della Regione Toscana prima di citare un articolo in un documento.

Articoli principali DPR 380/2001 applicabili in Toscana:
- **Art. 3**: definizioni categorie di intervento (manutenzione ordinaria/straordinaria, ristrutturazione, nuova costruzione)
- **Art. 6**: attivita' edilizia libera
- **Art. 6-bis**: CILA - comunicazione inizio lavori asseverata
- **Art. 10**: interventi soggetti a permesso di costruire
- **Art. 16**: contributo di costruzione (oneri urbanizzazione + costo costruzione)
- **Artt. 22-23**: SCIA e SCIA alternativa al PdC
- **Art. 23-ter**: mutamento della destinazione d'uso (modificato da DL 69/2024)
- **Art. 24**: certificato di agibilita'
- **Art. 65**: denuncia lavori strutturali
- **Artt. 93-94**: zone sismiche (deposito e autorizzazione Genio Civile)

Specificita' toscane LR 65/2014 (verificare numerazione sul testo vigente):
- Titolo VI: disciplina delle trasformazioni del territorio e attivita' edilizia
- Piano Strutturale (PS) e Piano Operativo (PO): strumenti urbanistici toscani (artt. 92-107 LR 65/2014)
- Titoli abilitativi edilizi: sezione specifica della LR 65/2014 (Capo I del Titolo VI o equivalente nel testo vigente)
- Contributo di costruzione: calcolato secondo tabelle comunali approvate dalla Regione

## Convenzioni specifiche

### Cosa NON fare

- Non affermare che un intervento e' sicuramente "CILA" o "SCIA" senza aver raccolto le informazioni sull'intervento strutturale e sulla zona sismica: in zona sismica 2 la presenza di parti strutturali cambia significativamente gli adempimenti.
- Non citare articoli della LR 65/2014 con certezza: la numerazione e' soggetta a variazioni per effetto delle modifiche 2019-2024. Usare la formulazione "verificare sul portale normativo regionale" quando si cita un articolo specifico.
- Non affermare mai che un progetto e' "conforme" o "approvato" dal SUE: la skill produce una checklist di supporto, non una valutazione di conformita' urbanistica.
- Non ignorare la zona sismica: in Toscana e' quasi sempre rilevante. Se non si conosce la zona sismica, chiedere al tecnico di verificarla.
- Non confondere le categorie di intervento del DPR 380/2001 (art. 3) con le categorie di intervento dei Piani Operativi comunali: spesso usano la stessa nomenclatura ma con perimetri diversi.
- Non trattare il portale APREA come unico canale: alcuni Comuni toscani usano portali propri per le pratiche SUE/SUAP.

### Cosa fare

- Raccogliere sempre le variabili di inquadramento prima di determinare il titolo: tipologia lavori, zona sismica, vincoli, parti strutturali, cambio d'uso.
- Avvertire sempre che i numeri di articolo della LR 65/2014 vanno verificati sul testo vigente.
- Segnalare sempre l'obbligo Genio Civile quando ci sono parti strutturali e zona sismica.
- Per la checklist documenti, distinguere chiaramente tra documenti obbligatori (sempre richiesti) e condizionali (dipendono dal caso specifico).
- Indicare sempre il Comune specifico nei passaggi che dipendono dal Piano Operativo o dal regolamento edilizio locale.
- Concludere sempre con un elenco di elementi da verificare allo sportello SUE/SUAP del Comune.

### Classificazione errori

- **Critico**: omissione denuncia/autorizzazione Genio Civile in zona sismica + intervento strutturale; scelta CILA invece di SCIA o PdC per interventi strutturali; inizio lavori senza PdC dove richiesto
- **Sostanziale**: mancanza di autorizzazione paesaggistica in zona vincolata; omissione del progetto strutturale per SCIA con parti strutturali; asseverazione incompleta
- **Formale**: documentazione incompleta ma non impeditiva; diritti di segreteria non allegati; ISTAT non compilato

## Validatori

- Nessun validatore Livello 2 identificato al momento del rilascio.
- La skill richiede validazione da tecnico abilitato toscano con esperienza SUE (geometra, ingegnere o architetto) e da responsabile del procedimento SUE di almeno un Comune toscano prima di passare a Livello 2.
- Priorita' di validazione: regime titoli (CILA/SCIA/PdC), obblighi Genio Civile zona sismica 2, lista allegati SCIA e PdC.

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 (revisione interna, nessun tecnico SUE toscano esterno)
- Task files: 2 (determina-tipo-pratica, checklist-documenti)
- Esempi: 1 CILA + 1 SCIA
- Known issues:
  - Numerazione articoli LR 65/2014 non verificata sul testo consolidato vigente
  - Non copre casi speciali: PdC in deroga, varianti in corso d'opera, proroga PdC
  - Non integra le specificita' del Salva Casa (DL 69/2024) per la Toscana (modifiche art. 36-bis, 34-bis): rinviare alla skill `modulistica-edilizia-unificata` per i casi di sanatoria
  - Non copre il recupero dei sottotetti (LR Toscana 5/2010 e s.m.i.)
  - La classificazione sismica per Comune specifico non e' embedata: va sempre verificata esternamente
