# Estratti curati - Circolare ADM 36/2025 - Codici TARIC e adempimenti

Fonte primaria: `references/fonti/circ-adm-36-2025-cbam.md`
Sorgente: ADM Direzione Dogane, prot. 0869339 del 24/12/2025.
Consultata: 2026-05-18.

> Indice operativo dei codici documento TARIC introdotti dalla Circolare 36/2025
> per il CBAM definitivo. Per il testo letterale rinviare a
> `fonti/circ-adm-36-2025-cbam.md`.

---

## Quadro generale

- **Avvio fase definitiva CBAM**: 1° gennaio 2026.
- **Autorita' competente nazionale (CBAM)**: MASE - Ministero dell'Ambiente e
  della Sicurezza Energetica (pagina "EU ETS - Italia :: CBAM").
- **Autorita' di controllo doganale**: Agenzia delle Dogane e dei Monopoli
  (ADM), Direzione Dogane.
- **Registro CBAM**: gestito dalla Commissione UE; modalita' applicative ex
  Reg. di esecuzione (UE) **3210/2024**.

## Tabella codici documento TARIC (Tabella 1 della circolare)

| Codice  | Significato operativo                                                                  | Quando usarlo                                                                |
|---------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Y128** | Numero di conto CBAM (qualifica di dichiarante autorizzato verificata via CERTEX)     | Importatore o rappresentante doganale indiretto **autorizzato**             |
| **Y134** | Deroga Art. 2 §4 - merci originarie di Busingen, Helgoland o Livigno                  | Origine in territori dell'Allegato III punto 1                              |
| **Y135** | Deroga Art. 2 §3 - merci destinate ad attivita' militari                              | Uso militare ex Art. 1 punto 49 Reg. del. 2015/2446                          |
| **Y136** | Deroga Art. 2 §3bis - elettricita'/idrogeno da piattaforma continentale o ZEE         | Energia elettrica o idrogeno di Allegato III punti 1-2                       |
| **Y137** | Deroga Art. 2bis - esenzione de minimis (massa netta ≤ soglia di Allegato VII)        | Importatore sotto soglia (50 t cumulativi nell'anno civile)                  |
| **Y237** | Merci originarie dell'UE                                                              | Origine UE per merci che altrimenti rientrerebbero in Allegato I             |
| **Y238** | Domanda di qualifica presentata entro 31 marzo 2026 (Art. 17 §7bis)                   | Deroga transitoria - usabile **fino al 27 settembre 2026**                  |

## Formalismo del numero di conto CBAM (codice Y128)

```
CBAM-XX-YYYY-AAANNNNNNNNNNN
```

dove:
- `XX` = codice paese (es. `IT`);
- `YYYY` = anno corrente;
- `AAA` = sequenza di 3 caratteri alfabetici;
- `NNNNNNNNNNN` = identificativo numerico di 11 cifre.

Esempio: `CBAM-IT-2025-ABC00000000001`.

Dichiarazione nel messaggio Hx:

```xml
<GoodsItem>
  <SupportingDocument>
    <Type>Y128</Type>
    <ReferenceNumber>2025-IT- CBAM-IT-2025-ABC00000000001</ReferenceNumber>
  </SupportingDocument>
</GoodsItem>
```

NOTA (n. 10 della circolare): questa modalita' compilativa "modifica e
sostituisce quanto indicato al paragrafo dal titolo "certificato CBAM"
nell'avviso "INTEROPERABILITA' CERTEX - RILASCIO 5.1" pubblicato sul portale
ADM in data 17/11/2025".

## Regole operative su autorizzazione

- **Importatore stabilito UE**: chiede direttamente la qualifica oppure si
  avvale di un rappresentante doganale indiretto autorizzato.
- **Rappresentante doganale indiretto** che accetta: deve essere autorizzato
  **anche se l'importatore rappresentato e' esentato ex Art. 2bis**.
- **Importatore che applica Art. 2bis (sotto soglia)**: presenta la domanda
  "nei casi in cui si prevede di superare la citata soglia unica basata sulla
  massa netta".
- Il rappresentante doganale indiretto e' soggetto a **tutti** gli obblighi
  CBAM per le merci importate per conto dell'importatore rappresentato.
- Domanda di autorizzazione: tramite **registro CBAM** (Art. 14). Possibilita'
  introdotta dal Reg. 2083/2025: indicare il **numero AEO** nella domanda per
  velocizzare il procedimento.

## Deroga transitoria Art. 17 §7bis (Y238)

Citazione testuale dalla circolare: "in deroga all'articolo 4 e in assenza di
qualifica di dichiarante autorizzato CBAM, sara' temporaneamente possibile
importare merce CBAM qualora sia stata gia' presentata al registro CBAM
l'istanza di autorizzazione. Tale deroga e' consentita **fino al 31 marzo
2026** e permette all'importatore (o rappresentante doganale indiretto) di
continuare ad importare tali merci fino a quando l'autorita' competente non
adotti la pertinente decisione e comunque **non oltre il 27 settembre 2026**".

## Conseguenze per importazioni non consentite

"Le articolazioni territoriali di ADM [...] vieteranno, fatte salve le citate
deroghe, tutte le importazioni effettuate da soggetti non autorizzati".

Procedura: "le merci oggetto di importazione non consentita dovranno essere
fermate e dovra' immediatamente essere informata l'autorita' competente ai
fini dell'eventuale irrogazione delle sanzioni individuate dall'art. 26 del
Regolamento". Restano salve eventuali ulteriori sanzioni doganali.

Nelle more dello scambio informativo automatico con il MASE, gli Uffici UADM
inviano verbale di constatazione e documentazione alla casella mail della
Direzione Dogane, informando per conoscenza la Direzione Territoriale.

## Coerenza con dichiarazione CBAM (Art. 6)

"Le informazioni da fornire ai sensi dell'art. 6 ("Dichiarazione CBAM")
dovranno sempre essere coerenti con le operazioni doganali svolte e, pertanto,
correttamente rendicontate dai soggetti dichiaranti e/o rappresentanti, anche
in caso di perfezionamenti attivi e passivi o di reintroduzioni di merce CBAM o
di prodotti trasformati partendo da merce CBAM".

## Definizione di elusione (nota 11 della circolare)

"Per pratiche di elusione si intende una modifica della configurazione degli
scambi di merci, derivante da una pratica, un processo o una lavorazione per i
quali non vi sia una sufficiente motivazione o giustificazione economica, se
non quella di eludere, in tutto o in parte, uno degli obblighi previsti dal
presente regolamento. Tale pratica, processo o lavorazione puo' consistere, tra
l'altro, nel:

a) modificare leggermente le merci in questione per farle rientrare nei codici
   NC non elencati nell'allegato I, tranne quando la modifica ne altera le
   caratteristiche essenziali;

b) frazionare artificiosamente le importazioni, anche mediante accordi non
   genuini, per evitare il superamento della soglia unica basata sulla massa".
