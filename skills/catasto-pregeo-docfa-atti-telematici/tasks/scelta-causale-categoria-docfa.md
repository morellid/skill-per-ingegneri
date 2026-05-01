# Task - Scelta della causale Docfa e della categoria catastale

## Obiettivo

Aiutare il professionista a:

1. scegliere correttamente la **causale di presentazione** Docfa (Quadro A per accatastamento, Quadro B per variazione) in funzione dell'intervento;
2. scegliere la **categoria catastale** corretta dell'UIU (Gruppi A, B, C - destinazione ordinaria; Gruppi D, E - destinazione speciale e particolare; Gruppo F - categorie fittizie senza rendita);
3. evitare gli errori ricorrenti di abbinamento causale/categoria che vengono respinti dall'Ufficio Provinciale Territorio (es. F/4 su unica UIU, F/3 su UIU gia' censita produttiva di reddito).

L'output e' una **scheda di tipizzazione + decisione fra causali alternative + scelta della categoria** con rinvio al Vademecum Docfa per la verifica di dettaglio.

## Input richiesti

Chiedi all'utente:

1. **Versione di Docfa in uso** (vigente: 4.00.5 da luglio 2019). Avvisa se eventuali nuove versioni ne hanno modificato i menu.
2. **Tipo di dichiarazione**: accatastamento (Quadro A) o variazione (Quadro B)? Se l'utente non lo sa, applica il decision tree del paragrafo "Procedura - 1. Distinguere accatastamento da variazione".
3. **Descrizione dell'intervento fisico/giuridico**: nuova costruzione, ampliamento, ristrutturazione, demolizione totale/parziale, divisione in piu' UIU, fusione di UIU, cambio di destinazione, regolarizzazione (es. art. 1 co. 336 L. 311/2004), riconoscimento ruralita', ultimazione di fabbricato gia' in F/3, ecc.
4. **Stato del fabbricato e delle UIU**: ultimato, non ultimato, allacciato a reti pubbliche, degrado, in corso di costruzione, su area di corte di altra UIU, su lastrico solare, ecc.
5. **Categoria catastale precedente** (se variazione): categoria attuale di ciascuna UIU oggetto di variazione e categoria proposta per l'unita' derivata.
6. **Riferimenti catastali**: foglio, particella, eventuali subalterni esistenti, eventuale presenza di partita speciale 0 (BCC) o 1 (area di enti urbani).

## Fonti

- `references/estratti/dm-28-1998-uiu.md` - definizione UIU, mappa Gruppo F
- `references/estratti/vademecum-docfa-categorie-causali.md` - causali Quadro A/B, categorie A-F
- `references/sources.yaml`: `ade-vademecum-docfa-v1`, `ade-circolare-2t-2016-categorie-DE`, `ade-circolare-6t-2012-stima-D-E`, `legge-208-2015-imbullonati`

## Procedura

### 1. Distinguere accatastamento da variazione

```
L'UIU e' gia' censita nel Catasto Fabbricati (con un identificativo subalterno o senza)?
|-- NO: accatastamento (Quadro A).
|   Casi tipici:
|   - nuova costruzione su particella mai accatastata (la particella va prima
|     mappata al CT con Tipo Mappale Pregeo, generandosi in automatico la F/6);
|   - unita' afferenti edificate in sopraelevazione di un fabbricato gia'
|     censito;
|   - unita' afferenti edificate su area di corte gia' censita di altra UIU;
|   - unita' afferenti su area urbana (F/1) o lastrico solare (F/5);
|   - dichiarazione di accatastamento ai sensi dell'art. 1 co. 336 L. 311/2004
|     (notifica del Comune di unita' difformi);
|   - fabbricato ex rurale (art. 2 co. 36 o 37 DL 262/2006);
|   - fabbricato rurale ai sensi DM 26/7/2012 o art. 13 co. 14-ter DL 201/2011.
|-- SI: variazione (Quadro B).
    Casi tipici:
    - variazione planimetrica (divisione, fusione, frazionamento per
      trasferimento di diritti, ampliamento, ristrutturazione, demolizione
      totale/parziale, diversa distribuzione spazi interni);
    - variazione toponomastica (cambio civico/strada);
    - ultimazione di fabbricato urbano (passaggio da F/3 a categoria ordinaria);
    - variazione di destinazione (cambio categoria);
    - presentazione planimetria mancante;
    - modifica identificativo;
    - richiesta ruralita' (passaggio a fabbricato rurale strumentale);
    - dichiarazione ai sensi art. 1 co. 22 L. 208/2015 (esclusione "imbullonati"
      dalla rendita di UIU di Gruppo D/E gia' accatastate);
    - dichiarazione ai sensi art. 1 co. 579 L. 205/2017.
```

### 2. Causali Quadro A (accatastamento)

Causali principali (Vademecum cap. 2.2.1.4):

| Causale | Quando si usa |
|---|---|
| Nuova costruzione | edificio mai dichiarato al CF (presuppone Tipo Mappale Pregeo gia' approvato) |
| Unita' afferenti - in sopraelevazione | nuove UIU realizzate sopra il fabbricato esistente |
| Unita' afferenti - edificate su aree di corte | nuove UIU realizzate sull'area pertinenziale di altra UIU |
| Unita' afferenti - Altro | casi residuali (es. "RECUPERO PER ERRATA SOPPRESSIONE" che richiede tipo operazione "R - Recuperata", da motivare nel Quadro D - cfr. cap. 2.4.2) |

Tipologia di documento (Vademecum cap. 2.2.1.5):

- Dichiarazione **ordinaria** (caso generale);
- art. 1 co. 336 L. 311/2004 (regolarizzazione su segnalazione del Comune);
- Fabbricato ex rurale (art. 2 co. 36 o 37 DL 262/2006);
- Fabbricato mai dichiarato (art. 2 co. 36 DL 262/2006);
- Fabbricato rurale DM 26/7/2012;
- Fabbricato rurale art. 13 co. 14-ter DL 201/2011 (rurali strumentali).

### 3. Causali Quadro B (variazione)

Causali codificate (Vademecum cap. 2.3.1.5):

**Variazione planimetrica**:
- Divisione (di una UIU in piu' UIU)
- Frazionamento per trasferimento di diritti
- Fusione (di piu' UIU in una)
- Ampliamento
- Demolizione totale (vedere se si genera area urbana F/1 - dipende dal contesto, cfr. Quadro D del Vademecum cap. 2.4.2)
- Demolizione parziale
- Diversa distribuzione degli spazi interni
- Ristrutturazione (interna alla UIU)
- Frazionamento e fusione (combinazione)

**Altre causali**:
- Variazione toponomastica
- Ultimazione di fabbricato urbano (da F/3 a categoria ordinaria)
- Variazione di destinazione (cambio categoria)
- Altre (sezione residuale - motivare nel Quadro D)
- Presentazione planimetria mancante (riferimento all'attestazione AdE - rasterizzazione o accertamento d'Ufficio - obbligatorio nel Quadro D, cfr. cap. 2.4.2)
- Modifica identificativo
- Richiesta ruralita'
- Unita' afferenti (in sede di variazione: edificate su area urbana, lastrico solare, altro)

Tipologia di documento (Vademecum cap. 2.3.1.6):

- Dichiarazione **ordinaria**;
- art. 1 co. 336 L. 311/2004;
- art. 1 co. 340 L. 311/2004 (sanatoria);
- Stralcio da categoria E (art. 2 co. 40 DL 262/2006);
- Fabbricato rurale DM 26/7/2012;
- Fabbricato rurale art. 13 co. 14-ter DL 201/2011;
- art. 1 co. 22 L. 208/2015 (esclusione "imbullonati" da rendita D/E);
- art. 1 co. 579 L. 205/2017.

### 4. Scelta della categoria catastale

Decision tree per la categoria (Vademecum cap. 1.2 - 1.3.1):

```
Esiste autonomia funzionale e reddituale (DM 28/1998 art. 2)?
|-- NO: l'UIU non si dichiara in autonomia. Va dichiarata come BCC (partita
|   speciale 0) o BCNC (partita speciale di servizio) - cfr. Vademecum
|   cap. 1.1.3.
|-- SI:
    L'immobile ha rendita ordinaria o rientra in stima diretta?
    |-- ordinaria (caratteristiche comparabili con UIU di riferimento):
    |   - Gruppo A (abitazioni - A/1...A/11 a seconda del tipo: signorile,
    |     civile, economica, popolare, ultrapopolare, rurale, villini, ville,
    |     palazzi di pregio, uffici/studi privati, abitazioni tipiche dei
    |     luoghi);
    |   - Gruppo B (uso collettivo - B/1 collegi/conventi/caserme,
    |     B/2 case di cura/ospedali no profit, B/3 prigioni, B/4 uffici
    |     pubblici, B/5 scuole/laboratori scientifici, B/6 biblioteche/musei,
    |     B/7 cappelle/oratori non culto pubblico, B/8 magazzini sotterranei);
    |   - Gruppo C (negozi/laboratori - C/1 negozi/botteghe, C/2 magazzini,
    |     C/3 laboratori arti e mestieri, C/4 sportivi no profit, C/5
    |     stabilimenti balneari no profit, C/6 stalle/scuderie/autorimesse,
    |     C/7 tettoie chiuse o aperte).
    |   La consistenza si determina in: vani (Gruppo A), m3 (Gruppo B),
    |   m2 (Gruppo C). La rendita = tariffa d'estimo x consistenza
    |   (Vademecum cap. 1.3.3).
    |-- speciale o particolare (caratteristiche singolari, non confrontabili):
    |   - Gruppo D (destinazione speciale - D/1 opifici, D/2 alberghi,
    |     D/3 teatri/cinema, D/4 case di cura/ospedali for profit,
    |     D/5 banche/assicurazioni for profit, D/6 sportivi for profit,
    |     D/7 industriali speciali, D/8 commerciali speciali, D/9 edifici
    |     galleggianti/sospesi/ponti privati a pedaggio, D/10 rurali
    |     strumentali);
    |   - Gruppo E (destinazione particolare - E/1 stazioni trasporto,
    |     E/2 ponti pedaggio comunali/provinciali, E/3 fabbricati pubblici
    |     speciali, E/4 recinti pubblici, E/5 fortificazioni, E/6 fari/
    |     semafori/torri orologio, E/7 culti pubblici, E/8 cimiteri,
    |     E/9 destinazione particolare residuale).
    |   La rendita si determina in **stima diretta** (procedimento diretto
    |   o indiretto, Vademecum cap. 1.3.4 + Circ. 6/T 2012). Per UIU di
    |   Gruppo D/E vanno escluse dalla stima le componenti "imbullonati"
    |   (art. 1 co. 21 L. 208/2015 + Circ. 2/E 2016).
    |   E' obbligatoria la **destinazione d'uso codificata** (Vademecum
    |   Prospetti 1.6 - 1.24) per ogni UIU di D/E.
    |-- senza rendita (Gruppo F, art. 3 DM 28/1998):
        - F/1 area urbana (da demolizione totale, da frazionamento di UIU
          per trasferimento di diritti, area urbanizzata non pertinenziale
          e non reddituale);
        - F/2 unita' collabente (degrado totale, no allacci a reti pubbliche
          - DSAN obbligatoria + relazione + foto, cfr. Vademecum cap. 1.2.4);
        - F/3 unita' in corso di costruzione (NC non ultimata - relazione
          stato avanzamento lavori obbligatoria);
        - F/4 unita' in corso di definizione (porzioni non definite quando
          le altre sono accatastate - solo se intervento ex art. 3 co. 1
          lett. d) DPR 380/2001 e fabbricato composto da PIU' UIU);
        - F/5 lastrico solare;
        - F/6 fabbricato in attesa di dichiarazione (iscritta automaticamente
          dopo Tipo Mappale, in attesa del Docfa di accatastamento);
        - F/7 infrastrutture di reti pubbliche di comunicazione (escluse
          dalle UIU dal 1/7/2016, censibili senza rendita).
```

> **Errori ricorrenti che la skill deve segnalare**:
>
> - **F/2** non puo' essere attribuita a immobili iscrivibili in altra categoria, ne' a manufatti "non individuabili ne' perimetrabili" (privi di copertura E delimitati da muri di altezza inferiore a 1 m).
> - **F/3** non puo' essere attribuita in dichiarazione di variazione per UIU gia' censite produttive di reddito, ne' per UIU gia' in F/2/F/4/F/7.
> - **F/4** NON e' ammessa per l'unica UIU oggetto di intervento edilizio: serve un fabbricato composto da PIU' UIU. La rendita ordinaria gia' tiene conto delle perdite reddituali per manutenzione (Vademecum cap. 1.2.4 nota 36).
> - **A/10 (uffici/studi privati)** non e' usabile in sede di accatastamento per immobili che non rispettano le caratteristiche tipologiche della categoria (consistenza in vani, ubicazione, ecc.). Per uffici di grandi dimensioni con caratteristiche speciali, valutare D/8 codice 0601 (Uffici strutturati).
> - Per le **categorie del Gruppo D ed E**, la "destinazione d'uso" codificata (Prospetti 1.6 - 1.24 Vademecum) e' obbligatoria.

### 5. Output

Produci una scheda strutturata con:

1. **Tipo di dichiarazione**: accatastamento (Quadro A) o variazione (Quadro B).
2. **Causale di presentazione** identificata, con riferimento al Vademecum cap. 2.2.1.4 o 2.3.1.5.
3. **Tipologia di documento** (ordinaria, art. 1 co. 336 L. 311/2004, fabbricato ex rurale, ecc.) con riferimento al Vademecum cap. 2.2.1.5 o 2.3.1.6.
4. **Categoria catastale proposta** (es. "A/3 - abitazione di tipo economico" oppure "C/6 - autorimessa" oppure "F/3 - unita' in corso di costruzione") con motivazione sulla scelta del Gruppo (ordinario / speciale / particolare / fittizio) e citazione del Vademecum cap. 1.2 - 1.3.1.
5. **Per UIU di Gruppo D/E**: rinvio alla scelta della destinazione d'uso codificata fra i Prospetti 1.6 - 1.24 (la skill cita esempi ma non sostituisce la scelta del professionista).
6. **Dichiarazioni obbligatorie nel Quadro D** in funzione della causale e della categoria F/x scelta (rinvio al task `check-pre-trasmissione-docfa.md` per la lista dettagliata).
7. **Limiti**: la skill non determina classe e consistenza, ne' calcola la rendita; non valida l'autonomia funzionale e reddituale (sopralluogo del professionista); non interpreta atti notarili o titoli edilizi sottostanti.
8. **Rinvio**: al manuale operativo Docfa 4 e al Vademecum Docfa per la compilazione campo-per-campo, e al firmatario per la responsabilita' professionale (artt. 359, 481 c.p. + art. 76 DPR 445/2000).

## Limiti

Il task NON:

- determina **classe e consistenza** dell'UIU (compito del professionista in base alle caratteristiche oggettive e alla comparazione - art. 11 co. 1 DL 70/1988);
- calcola la **rendita catastale** (richiede tariffa d'estimo per zona censuaria comunale, variabile);
- interpreta i **titoli edilizi sottostanti** all'intervento (CILA, SCIA, PdC, ecc. - rinvio alla skill `modulistica-edilizia-unificata`);
- valuta il **cumulo con esenzioni fiscali** (rurali, IMU, TARI);
- riproduce l'elenco completo delle **destinazioni d'uso codificate** Gruppi D/E (Prospetti 1.6 - 1.24 Vademecum - rinvio al PDF);
- sostituisce il **sopralluogo** per la verifica dello stato dei luoghi (presupposto per F/2, F/3, F/4 e per la determinazione di consistenza/classe).

Il **firmatario del Docfa** resta responsabile penalmente, civilmente e disciplinarmente per la veridicita' delle dichiarazioni rese.
