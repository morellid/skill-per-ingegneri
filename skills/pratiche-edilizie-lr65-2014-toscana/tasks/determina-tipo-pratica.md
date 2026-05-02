# Task: Determina il titolo abilitativo edilizio in Toscana (LR 65/2014)

Dato un intervento edilizio, determina il titolo abilitativo corretto tra:
Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / Permesso di Costruire,
ai sensi della LR Toscana 65/2014 e del DPR 380/2001.

## Obiettivo

Produrre una risposta strutturata che indichi:
- **Titolo abilitativo** richiesto (con motivazione normativa)
- **Riferimento normativo** preciso (articolo LR 65/2014 + articolo DPR 380/2001)
- **Autorizzazioni sovraordinate** necessarie (paesaggistica, sismica Genio Civile, etc.)
- **Elementi di incertezza** che richiedono verifica al SUE/SUAP

## Input richiesti

1. **Descrizione dell'intervento** (tipo di lavori, parti interessate)
2. **Tipologia di immobile**: residenziale / commerciale / produttivo / pubblico / altro
3. **Stato dell'immobile**: nuovo (assente) o esistente; se esistente, anno di costruzione indicativo
4. **Parti strutturali coinvolte**: si/no (pilastri, travi, solai, pareti portanti, fondazioni)
5. **Cambio di destinazione d'uso**: si/no; se si', da quale a quale categoria
6. **Comune**: per identificare zona sismica e Piano Operativo applicabile
7. **Vincoli presenti** (se noti): paesaggistico art. 142 D.Lgs. 42/2004, beni culturali, idrogeologico, ecc.
8. **Localizzazione urbanistica** (se nota): zona A (centro storico), zona B (residenziale consolidata), zona C, D, etc.

Se l'utente non fornisce alcune di queste informazioni, chiedi quelle strettamente necessarie
prima di procedere. Non procedere senza almeno intervento + parti strutturali coinvolte.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/lr-65-2014-titoli-abilitativi.md` (artt. 134-140 LR 65/2014)
- `references/estratti/dpr-380-2001-artt-zona-sismica.md` (artt. 93-94 DPR 380/2001)

## Procedura

### Passo 1 - Identifica la categoria di intervento

Classificare l'intervento nelle categorie del DPR 380/2001 (artt. 3, 6, 10, 22, 23) e
della LR 65/2014, rispondendo alle seguenti domande in sequenza:

**1a. E' manutenzione ordinaria?**
- Manutenzione ordinaria: riparazione, rinnovamento e sostituzione di finiture (tinteggiatura, infissi, pavimentazioni, impianti senza alterazione delle reti), interventi idraulici ed elettrici di ripristino
- Risposta si' -> **Edilizia libera** (art. 6 co. 1 DPR 380/2001 + art. 136 LR 65/2014)
- Risposta no -> vai a 1b

**1b. E' un intervento elencato nell'edilizia libera Toscana?**
Interventi tipici di edilizia libera in Toscana (art. 136 LR 65/2014):
- Opere interne senza modifica di sagoma, prospetti, volumi o parametri urbanistici, senza incidere sulle parti strutturali
- Eliminazione di barriere architettoniche senza alterazione della sagoma
- Installazione di pompe di calore < 12 kW
- Sostituzione di serramenti/infissi di identiche dimensioni (senza modifica prospetto)
- Pannelli solari / fotovoltaici integrati (con limitazioni in zone vincolate)
- Pertinenze di modesta entita' (verificare soglie nel regolamento edilizio comunale)
- Risposta si' -> **Edilizia libera** (verificare regolamento edilizio comunale per le soglie precise)
- Risposta no -> vai a 1c

**1c. E' manutenzione straordinaria non strutturale?**
Manutenzione straordinaria: rinnovamento e sostituzione di parti anche strutturali dell'edificio MA senza alterarne i volumi, le superfici, i prospetti, e senza cambio di destinazione d'uso. Include:
- Rifacimento di impianti con nuova distribuzione
- Sostituzione infissi con modifica di dimensioni
- Riassetto degli spazi interni senza incidere sulle strutture portanti
- Risposta si' (non strutturale) -> **CILA** (art. 137 LR 65/2014 + art. 6-bis DPR 380/2001)
- Risposta si' (con intervento strutturale) -> continua valutazione a 1d
- Risposta no -> vai a 1d

**1d. E' ristrutturazione edilizia o cambio di destinazione d'uso?**

Ristrutturazione edilizia: interventi volti a trasformare gli organismi edilizi mediante un insieme sistematico di opere. Include:
- Modifica di prospetti (apertura/chiusura finestre, modifica dimensioni aperture)
- Interventi sulle strutture portanti (consolidamento, modifica, sostituzione di travi/pilastri/solai)
- Divisione/accorpamento di unita' immobiliari con modifica delle superfici
- Cambio destinazione d'uso con opere (es. da cantina ad abitazione)
- Soprelevazione o ampliamento

Risposta si' (ristrutturazione senza demolizione, senza incremento volumetrico, senza zona sismica 2) -> **SCIA** (art. 140 LR 65/2014 + art. 22 DPR 380/2001)

Risposta si' (ristrutturazione con demolizione e ricostruzione, o cambio sagoma significativo) -> **SCIA alternativa al PdC** o **Permesso di Costruire** (vedi passo 1e)

Risposta no -> vai a 1e

**1e. E' nuova costruzione, ampliamento rilevante o intervento soggetto a PdC?**

Richiedono Permesso di Costruire (artt. 134-135 LR 65/2014 + art. 10 DPR 380/2001):
- Nuovi edifici (costruzione dal suolo)
- Ampliamenti volumetrici rilevanti (soglia da verificare nel Piano Operativo)
- Demolizione e ricostruzione con incremento di volume o modifica di sagoma significativa
- Interventi in zona A (centri storici) per alcune categorie di ristrutturazione pesante (verificare NTA del PO)
- Costruzione di parcheggi pertinenziali nel sottosuolo non inclusi nel titolo originario (verificare caso per caso)
- Cambio di destinazione d'uso da non residenziale a residenziale in zone specifiche (verificare NTA del PO)

Risposta si' -> **Permesso di Costruire** (o SCIA alternativa se ammessa dal PO)

### Passo 2 - Verifica la zona sismica

Per quasi tutto il territorio toscano valgono le seguenti zone sismiche (DM 28/7/2021):
- **Zona sismica 1** (pericolo piu' alto): alcuni comuni del pistoiese, area Mugello
- **Zona sismica 2**: gran parte della Toscana (Firenze, Siena, Arezzo, parte Pisa/Livorno...)
- **Zona sismica 3**: alcune aree costiere (parte Livorno, Grosseto...)
- **Zona sismica 4** (pericolosita' minima): non presente in Toscana

**Implicazioni per il titolo abilitativo**:

Per interventi in **zona sismica 2** con parti strutturali coinvolte:
- Se rilevante ai fini sismici (art. 94 DPR 380/2001): obbligo di **autorizzazione preventiva del Genio Civile** prima dell'inizio lavori (non solo deposito)
- Presentare il progetto strutturale al Genio Civile e attendere il via libera prima di iniziare
- Il titolo edilizio (SCIA/PdC) e' parallelo e non sostituisce l'autorizzazione sismica

Per interventi in **zona sismica 3** con parti strutturali coinvolte:
- **Denuncia deposito al Genio Civile** prima dell'inizio lavori (art. 93 DPR 380/2001)
- Controllo a campione (non obbligatorio in tutti i casi): il Genio Civile seleziona i progetti da controllare
- Non e' necessario attendere il nulla osta, ma il deposito deve precedere l'inizio lavori

Per interventi di edilizia libera e CILA **senza intervento strutturale**: nessun obbligo Genio Civile.

**ATTENZIONE**: La classificazione sismica per comune specifico va verificata sull'applicazione INGV o sul sito della Regione Toscana. La Regione Toscana fornisce la classificazione aggiornata per ogni Comune.

### Passo 3 - Verifica i vincoli sovraordinati

Per ogni intervento, verificare se presenti (l'utente deve indicarli o verificarli al Comune):

**Vincolo paesaggistico (art. 142 D.Lgs. 42/2004)**:
- Corsi d'acqua + fascia 150 m
- Boschi e foreste
- Fascia costiera 300 m
- Zone di interesse paesaggistico specifico (piani paesaggistici regionali)
- Se presente: serve **autorizzazione paesaggistica** (procedura ordinaria o semplificata DPCM 13/9/2017) prima o contestualmente al titolo edilizio

**Vincolo beni culturali (D.Lgs. 42/2004 Parte II)**:
- Edifici storici di interesse architettonico
- Se presente: serve **autorizzazione Soprintendenza** (art. 21 D.Lgs. 42/2004)

**Vincolo idrogeologico**:
- Aree a rischio idrogeologico (Piano di Bacino, PAI)
- Se presente: verifica nulla osta idrogeologico (competenza varia per Autorita' di Bacino o Genio Civile)

### Passo 4 - Verifica cambio di destinazione d'uso

Il cambio di destinazione d'uso in Toscana segue le regole del DPR 380/2001 (artt. 23-ter, 32) integrate dalla LR 65/2014 e dalle NTA del Piano Operativo comunale:
- Cambio d'uso **senza opere**: generalmente SCIA o CIL (a seconda della categoria e del PO)
- Cambio d'uso **con opere**: il titolo si determina in base alle opere (SCIA o PdC)
- Cambio da categorie non residenziali a residenziale: verificare NTA del PO (alcuni Comuni lo vietano o lo assoggettano a PdC)
- I Comuni toscani possono imporre limitazioni aggiuntive in specifiche zone del PO

### Passo 5 - Output

Produrre un output strutturato nel seguente formato:

```markdown
# Determinazione titolo abilitativo - [descrizione breve intervento]

**Comune**: [nome o "non specificato"]
**Intervento**: [breve descrizione]
**Data analisi**: [data]

---

## Titolo abilitativo richiesto: [EDILIZIA LIBERA / CILA / SCIA / SCIA alternativa al PdC / PERMESSO DI COSTRUIRE]

**Motivazione**: [articolo LR 65/2014 + articolo DPR 380/2001]

**Classificazione intervento**: [manutenzione ordinaria / manutenzione straordinaria / ristrutturazione / nuova costruzione / ...]

---

## Autorizzazioni e adempimenti connessi

| Adempimento | Richiesto | Condizione | Riferimento |
|-------------|-----------|------------|-------------|
| Denuncia Genio Civile (sismica) | [si/no/da verificare] | [zona sismica X] | Art. 93-94 DPR 380/2001 |
| Autorizzazione paesaggistica | [si/no/da verificare] | [vincolo art. 142 D.Lgs. 42/2004] | D.Lgs. 42/2004 |
| Autorizzazione Soprintendenza | [si/no/da verificare] | [vincolo beni culturali] | Art. 21 D.Lgs. 42/2004 |
| Nulla osta VVF | [si/no/da verificare] | [attivita' soggette DPR 151/2011] | DPR 151/2011 |
| Parere ASL / ARPAT | [si/no/da verificare] | [salubrità/impatto ambientale] | LR Toscana / regolamento edilizio |

---

## Elementi da verificare al SUE/SUAP

- Classificazione sismica aggiornata del Comune: [verificare su INGV / Regione Toscana]
- Piano Operativo vigente e NTA: [verificare zone, categorie d'uso ammesse, indici edilizi]
- Regolamento edilizio comunale: [soglie per edilizia libera, pertinenze, requisiti locali]
- [eventuali altri elementi non verificabili dalla skill]

---

## Avvertenze

- Questo output e' un supporto informativo; il tecnico abilitato firmatario deve
  asseverare il regime applicabile sotto propria responsabilita'
- La LR 65/2014 e' stata modificata negli anni 2019, 2020, 2021 e 2024; verificare
  la versione vigente su Normattiva o sul portale Regione Toscana
- In caso di dubbio sul regime applicabile, interpellare lo sportello SUE/SUAP
  del Comune competente
```

## Limiti di questo task

- La corrispondenza tra intervento e titolo abilitativo richiede informazioni dettagliate;
  in assenza di dati precisi, l'output indica le opzioni possibili con le condizioni
- Non copre i casi speciali (condono, sanatoria, variante in corso d'opera)
- Non verifica la compatibilita' con i piani urbanistici comunali (PO/PS)
- La classificazione sismica per Comune specifico deve essere verificata esternamente

## Esempi

Vedi `examples/`:
- `cila-manutenzione-straordinaria/` - rifacimento impianti senza intervento strutturale, zona sismica 3
- `scia-ristrutturazione-strutturale/` - ristrutturazione con consolidamento strutturale, zona sismica 2, vincolo paesaggistico
