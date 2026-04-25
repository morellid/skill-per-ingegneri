# Task: Valutazione necessita' di aggiornamento DVR (art. 29 co. 3)

Determina se un DVR esistente deve essere rielaborato/aggiornato e in che modo, sulla base degli eventi/cambiamenti occorsi nell'azienda.

## Obiettivo

Decisione strutturata se il DVR debba essere:
- **Rielaborato integralmente** (causale art. 29 co. 3)
- **Aggiornato in parte** (modifica circoscritta)
- **Confermato senza modifiche** (nessuna causale rilevante)

Con stima dei tempi (entro 30 giorni dalla causale, art. 29 co. 3).

## Input richiesti

- DVR esistente (data emissione, contenuti principali)
- Eventi/cambiamenti dell'ultimo periodo:
  - Modifiche del processo produttivo
  - Modifiche dell'organizzazione del lavoro
  - Acquisto nuove attrezzature / sostanze
  - Cambio sede o layout
  - Infortuni significativi
  - Risultati sorveglianza sanitaria
  - Variazioni numero lavoratori o mansioni
  - Cambiamenti normativi rilevanti

## Fonti

Leggere prima: `references/estratti/dlgs-81-art-17-28-29.md` (par. 3 art. 29)

## Procedura

### Passo 1 - Quattro causali esplicite art. 29 co. 3

Per ciascuna causale, valutare se applicabile:

#### Causale 1 - Modifiche del processo produttivo o dell'organizzazione del lavoro

Esempi che innescano:
- Acquisto/dismissione di una linea produttiva
- Cambio fornitore principale di sostanze chimiche
- Riorganizzazione turni (es. introduzione lavoro notturno)
- Cambio sede produttiva
- Ristrutturazione layout (nuove postazioni, percorsi modificati)
- Aumento significativo del personale

Esempi che NON innescano:
- Sostituzione di una macchina con modello equivalente
- Modifiche organizzative minori (cambio orario di 30 minuti)
- Variazioni di produzione entro le linee gia' valutate

#### Causale 2 - Evoluzione della tecnica, della prevenzione o della protezione

Esempi:
- Disponibilita' di nuove tecnologie di abbattimento polveri/rumore
- Nuovi DPI piu' efficaci diventati standard
- Nuove norme tecniche armonizzate (CEN, UNI) per misure di prevenzione

Esempi NON:
- Marketing di prodotti senza dimostrazioni di efficacia superiore

#### Causale 3 - Infortuni significativi

Soglia "significativi":
- Infortunio mortale o lesioni permanenti
- Infortunio con prognosi > 40 giorni
- Mancato infortunio (near-miss) con potenziale grave
- Cluster di infortuni minori sulla stessa attrezzatura/postazione

Esempi NON:
- Infortunio singolo con prognosi < 7 giorni e gia' coperto da DVR esistente

#### Causale 4 - Sorveglianza sanitaria che evidenzia necessita'

Esempi:
- Aumento di casi di malattia correlata all'esposizione (es. ipoacusia, dermatite, lombalgia)
- Risultati audiometrici che superano soglie
- Casi di "non idoneita'" o "idoneita' con prescrizioni" del medico competente
- Sospetta nuova malattia professionale

### Passo 2 - Causale aggiuntiva: modifiche normative

Anche se non esplicita nell'art. 29 co. 3, una **modifica normativa rilevante** (nuovo decreto, nuovo titolo, nuovi limiti) puo' richiedere aggiornamento DVR. Esempi recenti:
- Nuove sostanze chimiche aggiunte alla lista cancerogeni (D.Lgs. 11/04/2024)
- Nuovo DM Antincendio 02/09/2021 -> piano emergenza
- Nuove indicazioni stress termico (Note INL 2022-2023)

### Passo 3 - Determinare ambito dell'aggiornamento

Sulla base delle causali identificate:

- **Modifica circoscritta** (es. nuova attrezzatura): aggiornare le sezioni interessate (mansione, attrezzature, MMC se cambiano i carichi). Non serve riscrittura integrale.
- **Riorganizzazione significativa**: rivedere relazione rischi + misure + ruoli. Possibile rielaborazione di buona parte del documento.
- **Cambio sede produttiva**: praticamente nuovo DVR.

### Passo 4 - Tempi e formalita'

Art. 29 co. 3:
- Aggiornamento **entro 30 giorni** dalla causale
- Aggiornare anche le **misure di prevenzione**
- Comunicazione immediata al **RLS**
- Documentazione dell'aggiornamento (storico modifiche)

### Passo 5 - Output

```markdown
# Valutazione aggiornamento DVR - [azienda]

**Data valutazione**: [data]
**DVR vigente**: versione [v.X], data [...]
**Tempo trascorso da ultima rielaborazione**: [N anni/mesi]

## Causali identificate

| # | Causale | Descrizione evento/cambiamento | Data | Significativita' |
|---|---------|-------------------------------|------|-------------------|
| C1 | Modifica processo/organizzazione | Acquisto nuova linea X | YYYY-MM-DD | Alta |
| ... | ... | ... | ... | ... |

## Esito

**[RIELABORAZIONE INTEGRALE / AGGIORNAMENTO PARZIALE / NESSUNA AZIONE NECESSARIA]**

## Sezioni del DVR da aggiornare

| Sezione | Motivo | Priorita' |
|---------|--------|-----------|
| Lett. a) Relazione rischi | Nuova attrezzatura X aggiunge rischio rumore | Alta |
| Lett. b) Misure | Nuove misure per rumore | Alta |
| Lett. c) Programma miglioramento | Aggiungere obiettivi su nuova attrezzatura | Media |
| Lett. d) Procedure | Procedura per uso nuova attrezzatura | Alta |

## Tempi

- **Scadenza per rielaborazione (art. 29 co. 3)**: 30 giorni dalla causale
- **Comunicazione RLS**: immediata (anche prima della rielaborazione formale)
- **Aggiornamento misure di prevenzione**: contestuale all'aggiornamento DVR

## Coinvolgimenti

- DdL: firma aggiornamento
- RSPP: revisione tecnica
- Medico competente: integra rischi sanitari (es. nuova esposizione)
- RLS: consultazione obbligatoria

## Sinergia con altri obblighi

- **Formazione**: se nuovi rischi richiedono formazione integrativa per i lavoratori
- **DPI**: se nuovi rischi richiedono DPI aggiuntivi
- **Sorveglianza sanitaria**: nuovi protocolli per esposti
- **POS** (se cantieri): aggiornare anche POS dei singoli cantieri se applicabile

## Limiti

- Decisione strutturale, non sostituisce valutazione tecnica del RSPP
- Per casi complessi (ad es. infortunio mortale) coinvolgere subito INL/ASL e legale

## Rinvio

**Procedere con rielaborazione/aggiornamento sotto coordinamento RSPP, in collaborazione con medico competente, consultando RLS. Adempimento entro 30 giorni dalla causale.**
```

## Casi limite

### Pandemia / emergenza sanitaria
COVID-19 ha richiesto aggiornamenti diffusi DVR (rischio biologico). Eventi simili futuri richiedono aggiornamento entro 30 giorni dalla causale.

### Smart working / lavoro agile
L'introduzione di smart working modifica luogo di lavoro (domicilio) e richiede valutazione specifica del rischio (Titolo VII VDT + ergonomia + isolamento).

### Cambio applicazione normativa (es. ATEX dopo identificazione zone)
Se l'azienda ha sempre operato senza valutazione ATEX e poi viene rilevata una zona pericolosa, il DVR va integrato con sezione dedicata.

### Trasferimento di azienda
Cessione di ramo d'azienda: il successore aderisce al DVR esistente o rielabora? Generalmente rielabora se cambiano organizzazione/processi/responsabili (consigliato).

## Limiti di questo task

- Valutazione di principio, l'esecuzione richiede tecnico (RSPP)
- Casi grigi (es. ammodernamenti graduali) richiedono giudizio professionale
