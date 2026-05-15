# Task: determina la categoria PED (I, II, III, IV)

## Obiettivo

Identificare la **tabella** dell'Allegato II del D.Lgs 26/2016 applicabile all'attrezzatura, applicare le eventuali **eccezioni testuali**, e rinviare al PDF della GU per la lettura grafica della **categoria** (I, II, III o IV) in funzione di PS e V o DN.

## Input richiesti

Da `tasks/check-ambito-applicabilita.md` (eseguito a monte): tipo di attrezzatura, PS, V o DN, gruppo del fluido. Conferma all'utente:

- Tipo: recipiente (gas/vapore vs liquido) / tubazione (gas/vapore vs liquido) / accessorio di sicurezza / accessorio a pressione / insieme.
- Gruppo del fluido (output di `tasks/classifica-fluido.md`).
- PS (bar).
- V (litri) per i recipienti o DN per le tubazioni.
- TS (gradi C) - rilevante per l'eccezione "tubazioni > 350 gradi C".
- Per attrezzature speciali: e' una pentola a pressione? un estintore portatile? una bombola per apparecchi respiratori? un insieme per produzione di acqua calda? il fluido e' un gas instabile?

## Fonti

- `references/estratti/dlgs-26-2016-classificazione-moduli.md` sezione 3 (tabelle) e sezione 4 (eccezioni).
- `references/fonti/dlgs-26-2016.md` Allegato II.
- PDF della GU: `not_in_repo/dlgs-26-2016-gu53.pdf` pagg. 23-26 per la lettura grafica delle tabelle 1-9.

## Procedura

1. **Selezione della tabella applicabile**:
   - **Tabella 1**: recipienti per gas o vapori, fluidi gruppo 1.
   - **Tabella 2**: recipienti per gas o vapori, fluidi gruppo 2.
   - **Tabella 3**: recipienti per liquidi, fluidi gruppo 1.
   - **Tabella 4**: recipienti per liquidi, fluidi gruppo 2.
   - **Tabella 5**: attrezzature a pressione sottoposte a fiamma o altrimenti riscaldate con rischio di surriscaldamento (es. caldaie, insiemi per produzione di acqua calda).
   - **Tabella 6**: tubazioni per gas o vapori, fluidi gruppo 1.
   - **Tabella 7**: tubazioni per gas o vapori, fluidi gruppo 2.
   - **Tabella 8**: tubazioni per liquidi, fluidi gruppo 1.
   - **Tabella 9**: tubazioni per liquidi, fluidi gruppo 2.
2. **Accessori di sicurezza** (Allegato II punto 2): categoria IV. Eccezione: se fabbricati per un'attrezzatura specifica, possono ricevere la stessa categoria dell'attrezzatura protetta (lo decide il fabbricante).
3. **Accessori a pressione** (Allegato II punto 3): classificati come recipienti o tubazioni, scegliendo PS e V o DN; se sia V che DN sono adeguati, usa la categoria piu' elevata.
4. **Eccezioni testuali alle tabelle** (Allegato II - applica PRIMA della lettura del diagramma):
   - **Recipienti gas instabili** (tabella 1, categorie I o II) -> categoria **III** (eccezione testuale sotto la tabella 1).
   - **Estintori portatili e bombole per apparecchi respiratori** -> almeno categoria **III** (eccezione testuale dell'Allegato II).
   - **Insiemi per produzione di acqua calda** (art. 3 c. 2 lett. c del D.Lgs 93/2000 modificato) -> esame UE del tipo modulo B tipo di progetto **oppure** modulo H (eccezione testuale sotto la tabella 5).
   - **Pentole a pressione** -> controllo della progettazione con una procedura di almeno categoria **III** (eccezione testuale sotto la tabella 5 o area domestica).
   - **Tubazioni gas instabili** (tabella 6, categorie I o II) -> categoria **III** (eccezione testuale sotto la tabella 6).
   - **Tubazioni con fluidi a T > 350 gradi C** (tabella 7, categoria II) -> categoria **III** (eccezione testuale sotto la tabella 7).
5. **Lettura del diagramma** (se nessuna eccezione si applica): la tabella selezionata e' un diagramma cartesiano con PS sull'asse verticale e V o DN sull'asse orizzontale, con linee di demarcazione fra le categorie. **La skill non legge il diagramma**: rinvia all'utente la lettura del PDF della GU (pagg. 23-26) per identificare la fascia.
6. **Insiemi** (art. 10 c. 6): la "categoria" di un insieme e' una funzione composita. Per l'integrazione (punti 2.3, 2.8, 2.9 Allegato I) si usa la categoria piu' elevata fra le attrezzature interessate, esclusi gli accessori di sicurezza. Per la protezione (punti 2.10 e 3.2.3 Allegato I) si usa la categoria piu' elevata fra le attrezzature da proteggere. Ogni attrezzatura costitutiva e' classificata separatamente con questo stesso task.
7. **Recipienti multi-scomparto** (art. 9 c. 2): categoria piu' elevata fra le categorie dei singoli scomparti.

## Output

```
Determinazione categoria PED - <descrizione attrezzatura>

Input:
- Tipo: <recipiente gas/vapore | recipiente liquido | tubazione gas/vapore | tubazione liquido | accessorio sicurezza | accessorio pressione | insieme>
- PS: <PS> bar
- V o DN: <V o DN>
- Gruppo fluido: <gruppo 1 / gruppo 2>
- TS: <TS> gradi C

Tabella applicabile: <tabella N>

Eccezioni testuali applicabili:
- <elenco eccezioni che la skill rileva, o "nessuna">

Categoria proposta:
- Se eccezione testuale applicabile: la categoria e' fissata da quella eccezione.
- Se nessuna eccezione: la categoria va letta sul diagramma della tabella N. La skill rinvia
  al PDF della GU n.53 del 04/03/2016 (`not_in_repo/dlgs-26-2016-gu53.pdf`, pagg. 23-26).
  La lettura puntuale del diagramma e' a carico dell'utente/professionista.

Note:
- <eventuali note su gas instabili, T > 350 C, accessori, insiemi, multi-scomparto>

Rinvio:
- La lettura grafica della tabella e' a carico del fabbricante o del professionista firmatario.
- Per insiemi e accessori il fabbricante decide la categoria della valutazione globale e
  delle singole attrezzature.
```

## Limiti

- La skill non legge le immagini delle tabelle 1-9 dell'Allegato II e non fabbrica valori soglia di PS/V o PS/DN: l'output finale richiede la lettura visuale del PDF della GU.
- Le eccezioni testuali sono riportate fedelmente dal decreto; la skill non interpreta casi limite ("e' un'attrezzatura sottoposta a fiamma?", "e' un insieme per produzione di acqua calda nel senso dell'art. 3 c. 2 lett. c?"): tali qualificazioni sono del professionista.
- Per gli insiemi, la skill calcola le categorie per integrazione e protezione, ma il fabbricante deve nominare distintamente le attrezzature costitutive e decidere su quale di esse appoggiare la valutazione globale.
- La skill non gestisce attrezzature che potrebbero ricadere fra tabella 1 e tabella 5 (es. caldaia che contiene fluido di gruppo 1): segnala il caso e rinvia al fabbricante.
