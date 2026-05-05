# Task: Guida compilazione assistita POS

Guida l'utente nella compilazione assistita di una **bozza di POS** conforme nella struttura ai contenuti minimi dell'Allegato XV del D.Lgs. 81/2008, usando se richiesto l'impostazione dei modelli semplificati del Decreto Interministeriale 9 settembre 2014.

## Obiettivo

Produrre una **bozza strutturata** di POS che:

- segua le voci minime dell'Allegato XV punto 3.2.1;
- organizzi i contenuti per sezioni leggibili e compilabili;
- distingua chiaramente tra dati confermati dall'utente e campi mancanti;
- non inventi informazioni non fornite;
- prepari il documento al successivo precheck.

## Input richiesti

Chiedere in modo progressivo:

1. Dati impresa:
   - denominazione, sede, datore di lavoro;
   - RSPP, medico competente se previsto, RLS/RLST;
   - direttore tecnico di cantiere, capocantiere;
   - numero e qualifiche dei lavoratori previsti in cantiere.
2. Dati cantiere:
   - oggetto lavori, localizzazione, committente;
   - durata, cronologia indicativa, turni se presenti;
   - presenza PSC/CSE;
   - impresa affidataria / esecutrice / subappaltatrice.
3. Lavorazioni:
   - elenco lavorazioni effettive dell'impresa;
   - fasi critiche (scavi, demolizioni, coperture, impianti, ecc.).
4. Mezzi e attrezzature:
   - macchine, impianti, ponteggi, opere provvisionali, trabattelli, PLE, ecc.
5. Sostanze e miscele:
   - prodotti chimici, miscele, SDS disponibili/non disponibili.
6. Rischi e misure:
   - rischi gia' identificati;
   - misure di prevenzione/protezione;
   - DPI previsti.
7. Coordinamento:
   - altre imprese, subappalti, interferenze attese, riferimenti al PSC.
8. Costi e allegati:
   - richiamo costi sicurezza dal PSC o sezione dedicata;
   - allegati gia' disponibili (attestati, nomine, SDS, PiMUS, certificazioni).

Se l'utente non ha tutto, procedere comunque e marcare i campi mancanti come `DA COMPLETARE`.

## Fonti normative

Leggere prima:

- `references/estratti/allegato-xv-testo.md` punto 3.2.1
- `references/estratti/dlgs-81-art-96-97.md`
- `references/estratti/decreto-interministeriale-2014-modelli-semplificati.md`

## Procedura

### Passo 1 - Chiarisci il perimetro

Prima di scrivere la bozza, chiarire:

- se l'utente vuole una **bozza libera** organizzata per Allegato XV;
- oppure una bozza che segua il **modello semplificato 2014**.

Se non specificato, usare una struttura ordinata per Allegato XV con titoli espliciti.

### Passo 2 - Costruisci la matrice dati mancanti

Preparare internamente una tabella di controllo:

| Voce Allegato XV | Dato disponibile | Stato |
|---|---|---|
| a.1 DdL, sede, recapiti | ... | OK / DA COMPLETARE |
| a.2 lavorazioni | ... | ... |
| ... | ... | ... |

Se il dato non c'e', non completarlo in modo presuntivo.

### Passo 3 - Redigi la bozza

Produrre una bozza in cui:

- i dati confermati siano inseriti in forma narrativa o tabellare;
- i dati mancanti siano marcati in modo visibile come `DA COMPLETARE`;
- le sezioni senza base documentale restino descrittive ma non attestative.

Regole operative:

- Non scrivere attestati, nomine o allegati come esistenti se l'utente non li ha forniti.
- Non dichiarare "i lavoratori sono formati" se non c'e' supporto documentale.
- Non dichiarare "nessuna interferenza" senza motivazione sul contesto.
- Se manca il PSC, non simulare i suoi contenuti: indicare `PSC non fornito` o `PSC non previsto` solo se confermato.

### Passo 4 - Evidenzia i punti critici

Alla fine della bozza aggiungere sempre una sezione:

- `Dati mancanti`
- `Allegati da reperire`
- `Punti da verificare con CSE/CSP/dat. lavoro`

### Passo 5 - Raccomanda il precheck

Terminata la bozza, proporre o avviare il task `precheck-bozza-pos.md` prima di considerare il documento utilizzabile.

## Output atteso

```markdown
# Bozza POS - [cantiere / impresa]

## 1. Dati identificativi impresa esecutrice
...

## 2. Mansioni di sicurezza
...

## 3. Descrizione attivita' di cantiere
...

## 4. Attrezzature, macchine, impianti e opere provvisionali
...

## 5. Sostanze e miscele pericolose
...

## 6. Valutazione/esito rumore
...

## 7. Misure preventive e protettive integrative
...

## 8. Procedure complementari e di dettaglio
...

## 9. DPI
...

## 10. Informazione e formazione
...

## 11. Coordinamento, interferenze, PSC/CSE
...

## 12. Costi sicurezza / richiamo PSC
...

## Dati mancanti
- ...

## Allegati da reperire
- ...

## Avvertenza
Bozza assistita ai fini di lavoro interno. Da completare e validare prima di firma o uso in cantiere.
```

## Limiti

- Questo task non sostituisce il giudizio tecnico del professionista firmatario.
- Non genera un POS definitivo pronto al deposito.
- Non valuta automaticamente la congruita' col PSC.
- Non verifica la veridicita' documentale delle dichiarazioni inserite.
