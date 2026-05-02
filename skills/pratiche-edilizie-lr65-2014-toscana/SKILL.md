---
name: pratiche-edilizie-lr65-2014-toscana
description: Determina il titolo abilitativo edilizio corretto (Edilizia libera, CILA, SCIA, Permesso di Costruire) per un intervento in Toscana ai sensi della LR 65/2014 e genera la checklist documentale completa degli allegati richiesti, includendo le specificita' regionali (zona sismica, vincolo paesaggistico, competenze Genio Civile). Use when an architect, engineer, or geometra working in Tuscany needs to determine the correct procedural regime for a building intervention under LR Toscana 65/2014, or wants a structured checklist of documents to attach to CILA, SCIA, or Permesso di Costruire before submission to the SUE/SUAP.
license: MIT
---

# Pratiche edilizie LR 65/2014 Toscana - Document checker

## Quando usare questa skill

Usare quando un ingegnere, architetto o geometra che opera in Toscana chiede di:

- Determinare **quale titolo abilitativo** e' necessario per un intervento edilizio in Toscana (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / Permesso di Costruire) ai sensi della LR Toscana 10 novembre 2014 n. 65
- Ottenere la **checklist dei documenti** da allegare alla pratica (CILA / SCIA / PdC), incluse le specificita' regionali toscane (denuncia Genio Civile, zona sismica, vincolo paesaggistico, Piano Strutturale / Piano Operativo)
- Verificare se l'intervento richiede **autorizzazioni sovraordinate** (paesaggistica Soprintendenza, nulla osta idrogeologico, autorizzazione sismica Genio Civile)
- Capire le **differenze rispetto al regime nazionale** (DPR 380/2001): la LR 65/2014 introduce titoli e procedure parzialmente diverse rispetto alla legge nazionale

**Non usare** se l'utente chiede:
- Redazione del **contenuto tecnico** di una relazione o asseverazione: la skill lista i documenti richiesti, non li redige
- Verifica di **conformita' urbanistica** ai piani comunali (PS/PO): la skill segnala l'obbligo di verifica ma non legge i piani comunali
- Calcolo del **contributo di costruzione** o degli oneri: la skill indica che vanno calcolati ma non calcola l'importo
- Parere di **legittimita'** di un intervento gia' eseguito senza titolo (sanatoria): usare skill `modulistica-edilizia-unificata` per il regime nazionale (art. 36 / 36-bis DPR 380/2001)
- Interventi **al di fuori della Toscana**: usare skill `modulistica-edilizia-unificata` per il regime nazionale standard

## Avvertenza

Questa skill e' uno strumento di **supporto alla scelta del titolo abilitativo e all'identificazione degli allegati** richiesti in Toscana ai sensi della LR 65/2014.
**Non sostituisce il giudizio del tecnico abilitato firmatario, ne' del responsabile del procedimento dello sportello SUE/SUAP del Comune competente.**
La LR 65/2014 ha subito aggiornamenti nel 2019, 2020, 2021 e 2024; verificare sempre la versione vigente sul portale della Regione Toscana o su Normattiva prima di procedere.
Ogni output richiede revisione e asseverazione da parte del tecnico abilitato firmatario.

## Sotto-attivita' disponibili

Questa skill supporta due sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Determina il titolo abilitativo**: l'utente descrive l'intervento e chiede "che pratica serve?", "CILA o SCIA?", "serve il Permesso di Costruire?", "e' edilizia libera?" -> leggi [`tasks/determina-tipo-pratica.md`](tasks/determina-tipo-pratica.md)
- **Genera checklist documenti**: l'utente conosce gia' il titolo (CILA / SCIA / PdC) e chiede "quali allegati servono?", "cosa devo presentare allo SUE?", "checklist documenti CILA Toscana" -> leggi [`tasks/checklist-documenti.md`](tasks/checklist-documenti.md)

Se la richiesta non e' chiara, chiedi all'utente quale delle due sotto-attivita' vuole eseguire e raccogli le **variabili di inquadramento** prima di procedere.

## Processo generale

1. **Inquadra l'intervento**: tipologia lavori, immobile esistente o nuovo, parti strutturali coinvolte, cambio destinazione d'uso, Comune (per PS/PO), zona sismica, presenza di vincoli (paesaggistico, idrogeologico, beni culturali)
2. **Identifica la sotto-attivita'**: usa il routing sopra
3. **Carica il task file** corrispondente e applica la procedura
4. **Produci l'output** con riferimento preciso agli articoli della LR 65/2014 e del DPR 380/2001 per ogni decisione
5. **Concludi** sempre con:
   - elenco degli **elementi non automaticamente verificabili** dalla skill (regolamento edilizio comunale, NTA del Piano Operativo, prescrizioni di Soprintendenza, verifiche sismiche Genio Civile)
   - rinvio allo **sportello SUE/SUAP** per i casi borderline
   - rinvio al **tecnico abilitato firmatario** per la redazione e l'asseverazione

## Quadro normativo di riferimento

La LR Toscana 65/2014 si sovrappone al DPR 380/2001 (Testo Unico Edilizia). Il regime e':
- LR 65/2014 prevale sulle norme regionali precedenti (sostituisce LR 1/2005)
- DPR 380/2001 rimane applicabile per le materie non disciplinate dalla legge regionale
- I Comuni toscani operano attraverso **Piano Strutturale (PS)** e **Piano Operativo (PO)** invece del tradizionale PRG

### Titoli abilitativi edilizi in Toscana

**AVVERTENZA CRITICA**: La LR 65/2014 ha subito modifiche negli anni 2019, 2020, 2021 e 2024.
La numerazione degli articoli indicata in questa skill e' indicativa e NON deve essere copiata
in asseverazioni o relazioni tecniche senza aver verificato il testo vigente sul portale della
Regione Toscana. Citare sempre "LR 65/2014 testo vigente" senza numero di articolo se non si
e' verificato il testo aggiornato.

| Titolo | Quando | Norma di riferimento |
|--------|--------|----------------------|
| Edilizia libera | Manutenzione ordinaria, opere interne senza modifica parametri, interventi minori | LR 65/2014 (verificare articolo) + art. 6 DPR 380/2001 |
| CILA | Manutenzione straordinaria **non strutturale**, restauro/risanamento leggero senza modifiche strutturali | LR 65/2014 (verificare articolo) + art. 6-bis DPR 380/2001 |
| SCIA | Ristrutturazione edilizia (inclusi interventi strutturali), cambio uso, ampliamenti minori | LR 65/2014 (verificare articolo) + artt. 22-23 DPR 380/2001 |
| SCIA alternativa al PdC | Demolizione e ricostruzione senza incremento volumetrico, ristrutturazione pesante | LR 65/2014 (verificare articolo) + art. 23 DPR 380/2001 |
| Permesso di Costruire | Nuova costruzione, ampliamenti rilevanti, interventi in zone specifiche per certi casi | LR 65/2014 (verificare articolo) + art. 10 DPR 380/2001 |

### Specificita' toscane rispetto al regime nazionale

1. **Zona sismica e Genio Civile**: quasi tutta la Toscana e' in zona sismica (classificazione regionale approvata con DGRT 421/2014, aggiornata successivamente). Gli interventi strutturali in zona sismica richiedono preavviso, deposito o autorizzazione al Genio Civile ai sensi degli artt. 93-94 DPR 380/2001 e del DPGR 1/R/2022 (regolamento regionale sismico). La procedura esatta (deposito, autorizzazione preventiva, controllo a campione) dipende dalla zona sismica e dalla tipologia di intervento: verificare sempre sul portale della Regione Toscana e con il Genio Civile competente. La classificazione sismica per Comune e' disponibile sul portale della Regione Toscana (non su DM nazionale: la classificazione toscana e' stabilita da DGRT 421/2014 e s.m.i.).

2. **Piano Strutturale e Piano Operativo**: i Comuni toscani adottano PS e PO ai sensi degli artt. 92-107 LR 65/2014. Le NTA del PO sostituiscono le NTA del vecchio PRG e possono imporre prescrizioni aggiuntive rispetto al regime statale.

3. **Vincolo paesaggistico**: la Toscana ha estesa copertura paesaggistica (art. 142 D.Lgs. 42/2004 e PIT con valenza paesaggistica). Per interventi in zona vincolata: procedimento ordinario con parere Soprintendenza (artt. 146-149 D.Lgs. 42/2004) o procedimento semplificato (DPR 31/2017) a seconda della tipologia di intervento. Nota: la fonte corretta per il procedimento semplificato e' il **DPR 13 febbraio 2017 n. 31** (non DPCM 13/9/2017).

4. **Recupero sottotetti**: LR Toscana 5/2010 (parzialmente abrogata da LR 65/2014) - verificare le norme comunali vigenti per i recuperi abitativi dei sottotetti.

5. **Contributo di costruzione**: calcolato secondo le tabelle approvate da ciascun Comune; per CILA spesso non dovuto; per SCIA e PdC calcolato come somma oneri di urbanizzazione + costo di costruzione.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- LR Toscana 10 novembre 2014 n. 65 "Norme per il governo del territorio" (testo vigente)
- DPR 6 giugno 2001 n. 380 - Testo Unico Edilizia (versione consolidata)
- DPGR Toscana 18 dicembre 2018 n. 64/R - Regolamento edilizio tipo regionale
- D.Lgs. 22 gennaio 2004 n. 42 - Codice del paesaggio (per vincoli paesaggistici)
- DM 28 luglio 2021 - Classificazione sismica del territorio nazionale

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`lr-65-2014-titoli-abilitativi.md`](references/estratti/lr-65-2014-titoli-abilitativi.md) - artt. 134-140 LR 65/2014 (titoli abilitativi)
- [`dpr-380-2001-artt-zona-sismica.md`](references/estratti/dpr-380-2001-artt-zona-sismica.md) - artt. 93-94 DPR 380/2001 (zone sismiche, Genio Civile)

## Limiti

Questa skill NON fa:
- Non legge il **Piano Operativo (PO) o Piano Strutturale (PS)** del Comune specifico: segnala l'obbligo di verifica e rinvia allo sportello SUE
- Non integra le **prescrizioni dei regolamenti edilizi comunali**: segnala il rinvio al regolamento locale
- Non calcola il **contributo di costruzione**: indica che va calcolato e rinvia al Comune
- Non sostituisce la **denuncia al Genio Civile** ne' l'istruttoria antisismica
- Non emette pareri di **Soprintendenza** ne' verifica i vincoli culturali/paesaggistici in modo puntuale
- Non valuta la **congruita' tecnica** del progetto (strutturale, impiantistica, energetica)
- Non gestisce le specificita' delle **varianti in corso d'opera**
- Non copre il **regime sanzionatorio** per abusi edilizi ne' le procedure di sanatoria
- Non e' aggiornata in tempo reale alle modifiche legislative: LR 65/2014 ha subito 4+ aggiornamenti tra il 2019 e il 2024
