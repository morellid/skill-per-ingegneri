---
name: cedimenti-edometrici-ntc
description: Calcola il cedimento edometrico (compressione monodimensionale) di un singolo strato omogeneo per verifiche SLE ai sensi di NTC 2018 par. 6.2.4. Dato lo spessore h0, l'indice dei vuoti iniziale e0, gli indici di compressione Cc (NC) e ricompressione Cr (OC), la tensione efficace verticale media iniziale sigma_0', la tensione di preconsolidazione sigma_p' e l'incremento Delta sigma_v', restituisce OCR, ramo (OC / NC / transizione), contributi parziali e cedimento totale Delta h in m e mm. Implementazione code-driven, formule chiuse della meccanica dei terreni classica (Terzaghi 1925 / Skempton 1944) come strumento di pre-dimensionamento delle verifiche SLE NTC. Use when an Italian structural or geotechnical engineer asks to estimate one-dimensional consolidation settlement of a homogeneous clay/silt layer under a uniform stress increment for NTC 2018 SLE checks. Target users are structural and geotechnical engineers in pre-design phase; the skill does not replace the geotechnical report or the on-site investigation.
license: MIT
---

# Cedimenti edometrici - compressione monodimensionale (NTC 2018 par. 6.2.4)

## Quando usare questa skill

Usare quando un ingegnere strutturista o geotecnico italiano deve:
- Stimare il cedimento edometrico di un singolo strato compressibile omogeneo (argilla / limo) sotto un incremento di tensione uniforme, ai fini delle verifiche agli stati limite di esercizio (SLE) di NTC 2018 par. 6.2.4
- Determinare il ramo della curva edometrica coinvolto (OC / NC / transizione) data la tensione di preconsolidazione sigma_p' del terreno
- Confrontare il cedimento stimato con i limiti di cedimento ammissibile dichiarati dal progettista o dalla relazione geotecnica
- Verificare valori di cedimento prodotti da altri software o fogli di calcolo, confrontandoli con la formulazione classica

**Non usare** quando l'utente chiede:
- Cedimenti di stratigrafie multilayer eterogenee: la skill copre il singolo strato omogeneo. Per stratigrafie con piu' strati il progettista deve sommare i contributi strato per strato (ciascuno con la sua h0, e0, Cc, Cr, sigma_0', sigma_p', Delta sigma'), e/o usare software geotecnico con discretizzazione automatica
- Cedimenti per scarico (rebound, swelling): la skill assume incremento di tensione non negativo (compressione)
- Cedimenti differenziali tra punti diversi della fondazione: la skill stima il cedimento medio di uno strato; differenziali, distorsioni angolari e tilt vanno valutati con metodi specifici (sovrapposizione di Boussinesq / Steinbrenner / Mindlin per Delta sigma puntuale, FEM)
- Cedimenti per consolidazione 2D / 3D, drenaggio radiale, condizioni non drenate o terreni strutturati: la skill assume compressione monodimensionale piena, drenaggio verticale ideale
- Cedimenti immediati (elastici) o secondari (creep, compressione secondaria con Calpha): la skill calcola solo il cedimento primario di consolidazione
- Stima dei parametri edometrici Cc, Cr, e0, sigma_p' a partire da prove di laboratorio: la skill richiede questi valori come input dalla relazione geotecnica
- Verifiche di capacita' portante (SLU): per il pre-dimensionamento di capacita' portante di fondazione superficiale vedi NTC par. 6.4.2 e formulazione Brinch-Hansen / Vesic - skill diversa, candidata in roadmap (issue #31)
- Cedimenti di pali o fondazioni profonde: NTC par. 6.4.3 e metodi specifici, fuori scope

## Avvertenza

Questa skill e' uno strumento di **pre-dimensionamento** del cedimento edometrico per singolo strato omogeneo. **Non sostituisce la relazione geotecnica del progettista firmatario, ne' le indagini in sito.** L'output e' deterministico (formule chiuse della meccanica dei terreni classica) ed e' confrontabile dal progettista contro fogli di calcolo o software geotecnico certificati: il confronto resta in capo al professionista. **Nello stato v0.1.0-alpha la skill non e' ancora stata validata con confronto numerico vs casi reali pubblicati**; i test interni coprono solo la consistenza delle formule. La skill non produce relazioni geotecniche pronte al deposito e non firma elaborati. Per stratigrafie multilayer, cedimenti differenziali, consolidazione 2D/3D, terreni strutturati, cedimenti immediati o secondari, **la skill rinvia a metodi e software specifici e al progettista geotecnico**. NTC 2018 par. 6.2.4 richiede al progettista di scegliere il metodo di calcolo idoneo all'opera e ai terreni: la skill copre il caso piu' semplice e ricorrente (compressione monodimensionale) e va usata con consapevolezza dei suoi limiti.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Calcolo cedimento edometrico**: l'utente chiede "stimami il cedimento di questo strato", "che cedimento mi aspetto?", "calcolami il cedimento per Delta sigma = ... e h0 = ..." -> leggi [`tasks/calcola-cedimento.md`](tasks/calcola-cedimento.md)

Se la richiesta e' generica ("aiutami con i cedimenti NTC"), chiedi conferma che si tratta di compressione monodimensionale di singolo strato omogeneo; in caso contrario rinvia.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule classiche della compressione monodimensionale (rami OC e NC della curva edometrica) sono implementate nel modulo Python [`tasks/lib/cedimenti.py`](tasks/lib/cedimenti.py). La test suite [`tasks/lib/test_cedimenti.py`](tasks/lib/test_cedimenti.py) copre **solo consistenza interna**: formule OC e NC, raccordo a sigma_f = sigma_p (transizione), continuita' del cedimento totale, monotonia in delta_sigma e in h0, coerenza fra delta_h_m e delta_h_mm, OCR calcolato, avvertenza per epsilon > 10%, validazione input non finiti / fuori dominio (Cr > Cc, sigma_p < sigma_0, scarichi, input negativi), CLI con error handling. **Non** confronta vs casi reali pubblicati: la validazione di campo e' prerequisito del release stabile.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni calcolo numerico (sigma_f, OCR, Delta h OC, Delta h NC, Delta h totale, epsilon) **devi invocare il modulo Python via Bash**. NON riprodurre i numeri "a mano" leggendo le formule dagli estratti in `references/estratti/`: gli estratti sono materiale di citazione normativa, non sostituiscono l'esecuzione del modulo. Calcolare a mano vanifica la ragion d'essere code-driven della skill (output deterministico e riproducibile, confrontabile dal progettista) e introduce errore stocastico.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill. Usala in tutti i comandi Bash:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/cedimenti.py --input-json input.json
```

In Codex e altri agent compatibili AGENTS.md, se la variabile non e' risolta, sostituiscila con il path assoluto della directory che contiene **questo** `SKILL.md`. Non usare path relativi.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' (al momento solo "calcolo cedimento edometrico singolo strato").
2. Carica il task file `tasks/calcola-cedimento.md`.
3. Acquisisci dall'utente i parametri dello strato (h0, e0, Cc, Cr) e dello stato tensionale (sigma_0', sigma_p', Delta sigma'). I parametri edometrici devono provenire dalla relazione geotecnica o da prove edometriche; NON inventarli.
4. Esegui il calcolo invocando il modulo.
5. Produci output strutturato: input riportati, derivati (sigma_f, OCR, ramo), contributi OC e NC, cedimento totale (m e mm), deformazione media epsilon, avvertenze, riferimenti.
6. Concludi con rinvio al progettista geotecnico: per stratigrafie reali servono metodi specifici, e la verifica del cedimento ammissibile resta a carico del firmatario.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM 17/01/2018 (NTC 2018) - in particolare par. 6.2.2 (analisi interazione terreno-fondazione), par. 6.2.4 (verifiche SLE - cedimenti)
- Circolare MIT n. 7 del 21/01/2019 - par. C6.2 con commento applicativo
- Formulazione classica della meccanica dei terreni (Terzaghi 1925, Skempton 1944), riferimento didattico standard: Lancellotta R., "Geotecnica"

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Solo singolo strato omogeneo (no stratigrafie multilayer; sommatorie strato per strato a carico del progettista)
- Solo compressione monodimensionale (no 2D / 3D, no drenaggio radiale)
- Solo cedimento primario di consolidazione (no immediato elastico, no secondario / creep)
- Solo carico in compressione (Delta sigma >= 0; no rebound / swelling)
- Non stima i parametri edometrici Cc, Cr, e0, sigma_p' (input dalla relazione geotecnica)
- Non calcola Delta sigma' a profondita' (usare Boussinesq / Steinbrenner / Mindlin separatamente)
- Non valuta cedimenti differenziali, distorsioni angolari, tilt
- Non calcola tempi di consolidazione (NTC par. 6.2.4 + Cv): richiede coefficiente di consolidazione e teoria di Terzaghi 1D, fuori scope skill v0.1
- Non sostituisce la relazione geotecnica firmata

**Ogni output va verificato dal progettista geotecnico/strutturale prima di essere usato per dimensionamento, asseverazione o deposito.**
