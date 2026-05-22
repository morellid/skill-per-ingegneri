# Task: diagnosi adempimenti struttura DPR 380

## Obiettivo

Dato un intervento edilizio in Italia, stabilire quale combinazione di adempimenti
strutturali e sismici del DPR 380/2001 si applica:
- denuncia opere c.a./c.a.p./metalliche ex art. 65 (si/no, con quali allegati);
- preavviso scritto e progetto ex art. 93 in zona sismica (si/no);
- autorizzazione preventiva dell'ufficio tecnico regionale ex art. 94 (si/no/silenzio assenso);
- classificazione dell'intervento ex art. 94-bis (rilevante / minore rilevanza / priva di rilevanza);
- collaudo statico ex art. 67 oppure dichiarazione di regolare esecuzione del direttore dei lavori.

L'output e' una **diagnosi procedurale**, non un parere tecnico-strutturale.

## Input richiesti

Chiedere all'utente, in modo esplicito, tutti i dati seguenti prima di applicare la
decision tree. Se uno qualsiasi manca, fermarsi e chiederlo.

1. **Tipologia di intervento**: nuova costruzione / ampliamento / sopraelevazione /
   adeguamento sismico / miglioramento sismico / riparazione / intervento locale su
   esistente / demolizione e ricostruzione / variante a opere gia' denunciate.
2. **Sistemi costruttivi e materiali strutturali**: c.a. normale, c.a.p.,
   struttura metallica, muratura ordinaria, muratura armata, legno, altro.
3. **Sicurezza e pubblica incolumita'**: l'opera, in caso di collasso, puo'
   interessare la pubblica incolumita'? (di norma si' per qualsiasi edificio o
   parte di edificio non temporanea, comprese opere accessorie portanti).
4. **Ubicazione**: comune di realizzazione e zona sismica (1 / 2 / 3 / 4) come
   classificata dalla disciplina regionale vigente. Se in zona 2, chiedere anche
   il valore di accelerazione `ag` di riferimento, perche' l'art. 94-bis usa due
   soglie all'interno della zona 2 (0,15 g - 0,20 g e 0,20 g - 0,25 g).
5. **Destinazione e classe dell'opera**: edificio strategico per la protezione
   civile, edificio rilevante per conseguenze di collasso, edificio ordinario,
   edificio con presenza solo occasionale di persone o edificio agricolo (punto
   2.4.2 NTC 2018), altro.
6. **Caratteristiche tipologiche** (solo per nuove costruzioni in zona sismica):
   l'opera rientra nelle "usuali tipologie" oppure si discosta per particolare
   complessita' strutturale richiedendo piu' articolate calcolazioni e verifiche?
   (valutazione del progettista - chiedere conferma).

## Fonti

- `references/estratti/dpr-380-art-65-denuncia-ca.md`
- `references/estratti/dpr-380-art-67-collaudo.md`
- `references/estratti/dpr-380-artt-93-94-94bis-zone-sismiche.md`

## Procedura

### Passo A - L'art. 65 si applica?

L'art. 65 DPR 380 si applica se l'opera e' realizzata con sistemi costruttivi
disciplinati dalle NTC vigenti, in particolare:
- conglomerato cementizio armato (c.a.) normale,
- conglomerato cementizio armato precompresso (c.a.p.),
- struttura metallica.

Per altre tipologie (es. muratura portante, legno) si applicano le procedure
generali del Capo II DPR 380 ma l'obbligo specifico ex art. 65 e' quello
dedicato al c.a./c.a.p./metallico. Verificare comunque presso lo sportello
unico se ci sono prassi regionali che estendono l'art. 65.

### Passo B - L'opera ricade in zona sismica?

Se zona 1, 2 o 3: l'art. 93 si applica sicuramente.
Se zona 4: si applica l'art. 93 ma l'obbligo di autorizzazione preventiva
ex art. 94 puo' essere derogato dai decreti dell'art. 83 e dalla disciplina
regionale (la zona 4 e' di bassa sismicita').

### Passo C - Doppia pratica o pratica unica?

- Se solo Passo A si applica (no zona sismica): **denuncia ex art. 65** allo
  sportello unico, con allegati art. 65 comma 3.
- Se Passo A e Passo B si applicano: **preavviso ex art. 93** allo sportello
  unico, che vale anche come denuncia ex art. 65 per il comma 5 dell'art. 93.
  Una sola pratica, ma con i contenuti minimi del progetto richiesti dall'art. 93
  comma 3 (planimetria, piante, prospetti, sezioni, relazione tecnica) e
  l'asseverazione del progettista del comma 4.
- Se Passo B si applica ma Passo A no (es. costruzione in muratura ordinaria in
  zona sismica): solo art. 93. La denuncia "secondaria" ex art. 65 non si applica
  perche' il sistema costruttivo non rientra.

### Passo D - Serve l'autorizzazione preventiva ex art. 94?

Applicare la classificazione ex art. 94-bis comma 1:

- L'intervento e' **"rilevante"** (lettera a)?
  - a.1) adeguamento o miglioramento sismico su esistente in **zona 1** o **zona 2 con ag 0,20-0,25 g**;
  - a.2) **nuova costruzione che si discosta dalle usuali tipologie** o ha
    particolare complessita' strutturale, in zone diverse da bassa sismicita'
    (zone 3 e 4);
  - a.3) intervento su **edificio strategico o opera infrastrutturale strategica**
    in zone diverse da bassa sismicita' (zone 3 e 4).

  Se si': **autorizzazione preventiva ex art. 94 obbligatoria** (art. 94-bis comma 3).
  Rilascio entro 30 giorni, decorsi i quali si forma silenzio assenso (art. 94
  comma 2 e 2-bis).

- L'intervento e' **"di minore rilevanza"** (lettera b)?
  - b.1) adeguamento/miglioramento su esistente in zona 2 con ag 0,15-0,20 g o zona 3;
  - b.2) **riparazioni o interventi locali** su esistenti (anche se strategici);
  - b.3) nuove costruzioni non rientranti nella lettera a.2;
  - b.3-bis) nuove costruzioni con presenza solo occasionale di persone o
    edifici agricoli del punto 2.4.2 NTC 2018.

  Se si': **autorizzazione preventiva NON dovuta** (art. 94-bis comma 4). Il
  preavviso ex art. 93 e' comunque dovuto. La regione puo' istituire controlli a
  campione (art. 94-bis comma 5).

- L'intervento e' **"privo di rilevanza"** (lettera c.1)?

  Se si': autorizzazione preventiva NON dovuta. Preavviso ex art. 93 comunque dovuto.

> **Attenzione operativa**: l'art. 94-bis comma 2 demanda l'elencazione operativa
> degli interventi a linee guida nazionali (MIT + Conferenza Unificata) e ad
> elencazioni regionali. Le regioni hanno facolta' di adattare le proprie liste.
> Prima di concludere la diagnosi, **verificare l'elencazione regionale vigente
> nel comune di intervento**. La diagnosi prodotta da questa skill resta una
> mappatura del quadro statale.

### Passo E - Collaudo statico ex art. 67

L'art. 67 si applica a tutte le costruzioni di cui all'art. 53 comma 1 la cui
sicurezza interessi la pubblica incolumita'. Salvo le eccezioni:

- comma 8-bis: riparazioni e interventi locali su esistenti (come definiti dalla
  normativa tecnica) -> certificato di collaudo **sostituito** dalla dichiarazione
  di regolare esecuzione resa dal direttore dei lavori;
- comma 8-ter: interventi di art. 94-bis comma 1 lett. b) n. 2 e lett. c) n. 1
  (stesso esito - dichiarazione di regolare esecuzione del DL).

Per le opere soggette a collaudo: nomina del collaudatore contestuale alla
denuncia ex art. 65 (art. 67 comma 3). Il collaudatore deve essere ingegnere o
architetto iscritto all'albo da **almeno 10 anni** e non aver partecipato a
progettazione, direzione, esecuzione (art. 67 comma 2).

### Passo F - Varianti

Se il progetto viene variato in corso d'opera: ogni variante alle opere
strutturali deve essere denunciata **prima** dell'esecuzione, con la stessa
forma e allegati della denuncia originaria (art. 65 comma 5). In zona sismica,
ex art. 94-bis comma 2 ultima parte, le linee guida nazionali individuano le
"varianti di carattere non sostanziale" per le quali non occorre preavviso ex
art. 93: verificare elencazione regionale.

## Output atteso

Restituire all'utente un riepilogo in 4 sezioni:

1. **Quadro adempimenti**: tabella delle pratiche dovute (art. 65 / art. 93 /
   art. 94 / art. 67), con destinatario (SUE, UTR, entrambi) e citazione dell'articolo.
2. **Classificazione ex art. 94-bis**: rilevante / minore rilevanza / priva di
   rilevanza, con motivazione esplicita riferita alla lettera del comma 1.
3. **Documenti da allegare**: per ogni pratica dovuta, l'elenco minimo degli
   allegati (rinviare alle checklist dedicate per il dettaglio operativo:
   `tasks/checklist-denuncia-art-65.md`, `tasks/checklist-zona-sismica-art-93-94.md`,
   `tasks/checklist-collaudo-art-67.md`).
4. **Avvertenze**: rinvio al progettista strutturale per la classificazione
   sostanziale dell'intervento; rinvio alla disciplina regionale per
   l'elencazione operativa ex art. 94-bis; richiamo all'obbligo del titolo
   edilizio (PdC/SCIA/CILA) che e' procedura distinta e parallela.

## Limiti

- La skill non determina la zona sismica del comune ne' il valore di `ag`: sono
  input forniti dall'utente, reperibili dalla classificazione regionale vigente.
- La distinzione fra "intervento locale", "riparazione", "miglioramento sismico"
  e "adeguamento sismico" e' definita dalle NTC 2018 capitolo 8 e resta in capo
  al progettista strutturale.
- La skill non si occupa di sanatoria postuma per pratiche non depositate (art.
  95 e ss. DPR 380, art. 65 comma 5 in caso di varianti non denunciate).
- La skill non determina autonomamente se un'opera "si discosta dalle usuali
  tipologie" (art. 94-bis comma 1 lett. a.2): valutazione del progettista.
