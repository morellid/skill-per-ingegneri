# AGENTS.md - ped-classificazione-conformita

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la classificazione delle attrezzature a pressione (recipienti, tubazioni, accessori di sicurezza e a pressione, insiemi) e la scelta della procedura di valutazione della conformita' ai sensi del **D.Lgs 26/2016**, decreto modificativo del D.Lgs 93/2000 che recepisce in Italia la **Direttiva 2014/68/UE (PED - Pressure Equipment Directive)**. Target utente: ingegnere meccanico o tecnico della sicurezza che lavora per il fabbricante (o suo rappresentante autorizzato, importatore, distributore quando equiparati a fabbricante ex art. 4-sexies).

## Fonti autoritative

- **D.Lgs 26/2016** (GU Serie Generale n.53 del 04/03/2016, codice atto 16G00034) - hash `20e9eb35c39f6f2c51773e58d6864694583ea9b45af5a3d45e6d3540ca1387f5`, id `dlgs-26-2016-ped` in `references/sources.yaml`. URL: https://www.gazzettaufficiale.it/eli/gu/2016/03/04/53/sg/pdf

Trascrizione fedele in `references/fonti/dlgs-26-2016.md`. Estratto curato (parti citate dai task) in `references/estratti/dlgs-26-2016-classificazione-moduli.md`.

La Direttiva 2014/68/UE (CELEX 32014L0068) non e' inclusa come fonte separata: il D.Lgs 26/2016 ne riproduce il contenuto tecnico in lingua italiana e costituisce la norma vincolante nell'ordinamento italiano. La tavola di concordanza articolo-per-articolo direttiva-decreto e' citata dall'art. 3 c. 3 del D.Lgs 26/2016 e rinvia all'Allegato VI della direttiva 2014/68/UE.

## Articoli e punti chiave

Riferimenti ricorrenti nei task e negli esempi della skill:

- **Art. 4-bis** (obblighi dei fabbricanti): documentazione tecnica ex Allegato III, dichiarazione UE, marcatura CE, conservazione decennale.
- **Art. 4-quater, 4-quinquies, 4-sexies**: obblighi di importatori, distributori; estensione obblighi del fabbricante.
- **Art. 5** (presunzione di conformita' e dichiarazione UE): norme armonizzate, struttura della dichiarazione UE ex Allegato VII.
- **Art. 9 c. 1**: classificazione dei fluidi in gruppo 1 (17 classi di pericolo da Regolamento CE 1272/2008, piu' fluidi a TS > punto di infiammabilita') e gruppo 2 (residuo).
- **Art. 9 c. 2**: recipienti multi-scomparto - categoria piu' elevata.
- **Art. 10 c. 2**: mappa categoria -> moduli ammissibili (I: A; II: A2, D1, E1; III: B+D, B+F, B+E, B+C2, H; IV: B+D, B+F, G, H1).
- **Art. 10 c. 3**: il fabbricante puo' optare per una procedura di categoria superiore.
- **Art. 10 c. 6**: valutazione globale di un insieme (componenti, integrazione punti 2.3/2.8/2.9 Allegato I, protezione punti 2.10/3.2.3 Allegato I).
- **Art. 15** (marcatura CE): apposizione visibile, leggibile, indelebile sull'attrezzatura/insieme o sulla sua targhetta; non duplicata sui componenti gia' marcati; apposta prima dell'immissione sul mercato.
- **Allegato II punti 1-4** e **eccezioni testuali** alle tabelle: gas instabili in recipienti (cat. III); estintori portatili e bombole respiratori (cat. III); insiemi acqua calda (Modulo B tipo di progetto o Modulo H); pentole a pressione (cat. III); gas instabili in tubazioni (cat. III); tubazioni > 350 gradi C (cat. III).
- **Allegato III**: elenco dei 12 moduli (A, A2, B tipo di progetto, B tipo di produzione, C2, D, D1, E, E1, F, G, H, H1).

## Convenzioni specifiche

### Cosa NON fare
- **Mai inventare valori soglia delle tabelle 1-9 dell'Allegato II.** Sono diagrammi grafici nel PDF. Se l'utente fornisce PS e V/DN, la skill deve indicare la tabella applicabile e le eccezioni testuali, ma rinviare al PDF (`not_in_repo/dlgs-26-2016-gu53.pdf`, pagg. 23-26) per il punto preciso della linea di demarcazione.
- **Mai citare l'art. 9 o l'art. 10 senza specificare il comma**. La struttura modificativa del decreto rende essenziale la precisione del rinvio (es. "art. 9 c. 1 lett. a) punto 4) D.Lgs 26/2016").
- **Mai produrre una dichiarazione UE di conformita' "pronta alla firma"**: la skill puo' descrivere gli elementi obbligatori (Allegato VII), non produrre il documento finale. Il fabbricante e' il solo responsabile.
- Mai promettere che la skill sostituisca l'analisi del fabbricante o del professionista firmatario.
- Mai trattare i moduli come fungibili: per una stessa categoria, la scelta fra moduli alternativi cambia attivita' dell'organismo notificato e impatti operativi; la skill descrive la scelta, non la fa al posto del fabbricante.

### Cosa fare
- **Citare sempre l'articolo e il comma** (es. "ai sensi dell'art. 10 c. 2 lett. b) D.Lgs 26/2016") quando si afferma un fatto normativo. Per le eccezioni alle tabelle, citare anche la tabella di riferimento (es. "eccezione gas instabili in tubazioni - tabella 6, Allegato II").
- **Ordine standard di output** per la classificazione di un'attrezzatura: (1) ambito di applicabilita'; (2) gruppo del fluido; (3) tabella applicabile (con eccezioni); (4) categoria; (5) moduli ammissibili; (6) rinvio al fabbricante per la scelta finale e per la dichiarazione UE.
- **Distinguere chiaramente** quando un'affermazione e' testuale del decreto (citare il comma) e quando e' una osservazione metodologica della skill (es. "la skill non legge le tabelle grafiche").
- **Limite di responsabilita'**: ogni output deve terminare con il rinvio al fabbricante / professionista firmatario per la verifica finale.

## Validatori

- Non identificato per Livello 2 validation in questa versione `0.1.0-alpha`. Validatore atteso: ingegnere meccanico o RSPP/RSPI con esperienza specifica PED, non coincidente con l'autore della skill, prima della promozione a `1.0.0`.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (corrente `0.1.0-alpha`).
- Validazione: Livello 1 (validazione strutturale + adversarial review).
- Task files: 5 file in `tasks/` (check ambito, classifica fluido, determina categoria, scegli procedura, check marcatura/dichiarazione).
- Esempi: 1 conforme (recipiente categoria I, fluido gruppo 2, modulo A) + 1 problematico (errata classificazione gruppo).
