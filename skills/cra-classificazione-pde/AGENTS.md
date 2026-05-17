# AGENTS.md - cra-classificazione-pde

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill di compliance per la **classificazione dei prodotti con elementi digitali (PDE)** ai sensi del **Regolamento (UE) 2024/2847 - Cyber Resilience Act**. Riferimento unico autoritativo: il testo del Regolamento pubblicato in GU UE L del 20/11/2024. Target utente: ingegneri/security engineer, product compliance manager, responsabili tecnici del fabbricante o del rappresentante autorizzato, che devono inquadrare un prodotto rispetto al CRA prima dell'immissione sul mercato (data di applicazione generale: 11/12/2027; art. 14 dal 11/9/2026; Capo IV dal 11/6/2026).

## Fonti autoritative

Unica fonte primaria: **Regolamento (UE) 2024/2847** - file `references/fonti/reg-ue-2024-2847-cra.md` (trascrizione fedele del PDF `not_in_repo/reg-ue-2024-2847-cra.pdf`, SHA256 `7c9ae1d683e7fbafef4ce5898b33279bb6f5f6746df3c4a08911c1a0d3a31db3`, scaricato da <https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32024R2847>).

Estratto curato in `references/estratti/reg-ue-2024-2847-cra-classificazione.md` (focus: ambito, classificazione, modulo, documentazione tecnica).

## Articoli e punti chiave

Quando l'agent produce output, deve citare il **riferimento puntuale al Regolamento (UE) 2024/2847**, non "il CRA" in generale:

- **Art. 2 par. 1**: ambito positivo (PDE con connessione dati logica/fisica diretta o indiretta a dispositivo o rete).
- **Art. 2 par. 2-4, 6-7**: esclusioni (medicali, veicoli, aviazione, marittimo, ricambi, sicurezza nazionale).
- **Art. 3 punto 1**: definizione di PDE (prodotto software o hardware e relative soluzioni di elaborazione dati da remoto, componenti separati inclusi).
- **Art. 7 par. 1-2**: PDE importanti (funzionalita' principale = categoria Allegato III; criteri a/b del par. 2 per Classi I e II).
- **Art. 8 par. 1-2**: PDE critici (Allegato IV; certificato UE liv. "sostanziale" se previsto da atto delegato).
- **Art. 13 par. 4**: la valutazione dei rischi va nella documentazione tecnica (art. 31, Allegato VII).
- **Art. 13 par. 8**: periodo di assistenza, minimo 5 anni.
- **Art. 13 par. 12**: il fabbricante redige la documentazione tecnica e segue le procedure prima dell'immissione.
- **Art. 13 par. 13**: documentazione tecnica e DoC UE conservate 10 anni o periodo di assistenza, se piu' lungo.
- **Art. 27 par. 9**: il certificato europeo di cibersicurezza liv. "sostanziale" sopprime l'obbligo di valutazione da parte di terzi per i requisiti coperti.
- **Art. 28 + Allegato V**: contenuto DoC UE (8 elementi).
- **Art. 30 par. 4**: per il modulo H il numero ON e' apposto accanto alla marcatura CE.
- **Art. 31 + Allegato VII**: contenuto documentazione tecnica (8 punti).
- **Art. 32 par. 1**: procedure ammesse PDE ordinario (A, B+C, H, certificazione UE).
- **Art. 32 par. 2**: PDE importante Classe I (procedure del par. 1 solo se norme armonizzate applicate integralmente; altrimenti B+C o H).
- **Art. 32 par. 3**: PDE importante Classe II (B+C, H o certificazione UE liv. sostanziale).
- **Art. 32 par. 4**: PDE critici (certificazione UE liv. sostanziale ex art. 8 par. 1 o procedure del par. 3).
- **Art. 32 par. 5**: PDE open source qualificati (procedure del par. 1 se doc tecnica pubblica).
- **Allegato III**: 19 categorie Classe I, 4 categorie Classe II.
- **Allegato IV**: 3 categorie critiche (HSM, smart meter gateway, smart card).
- **Art. 69**: transitorie (validita' fino 11/6/2028 certificati esame UE tipo pre-esistenti; obblighi art. 14 anche per prodotti immessi prima dell'11/12/2027).
- **Art. 71**: date di applicazione.
- **Art. 64**: sanzioni (3 fasce: 15M/2,5%, 10M/2%, 5M/1%).

## Convenzioni specifiche

### Cosa NON fare
- Non inventare categorie o sottocategorie dell'Allegato III/IV. Se il prodotto e' di confine, segnalalo e rinvia all'atto di esecuzione attesa per l'11/12/2025 (art. 7 par. 4) o all'atto delegato attesa ex art. 8 par. 1.
- Non assumere che il modulo A sia sempre disponibile: per Classe II e PDE critici non lo e' mai. Per Classe I lo e' solo se le norme armonizzate sono applicate integralmente (art. 32 par. 2).
- Non confondere "norma armonizzata applicata" con "presunzione di conformita'". La presunzione (art. 27) c'e' solo quando i riferimenti sono stati pubblicati in GU UE.
- Non scrivere "marcatura CE = libero accesso al mercato": il CRA vincola anche dopo l'immissione (gestione vulnerabilita', segnalazione, conservazione documenti per 10 anni).
- Non scrivere date di applicazione "approssimate": usare sempre `11 dicembre 2027` (generale), `11 settembre 2026` (art. 14), `11 giugno 2026` (Capo IV), `11 giugno 2028` (transitorie certificati altri atti).
- Non confondere "PDE critico" (Allegato IV, art. 8) con "PDE importante Classe II" (Allegato III, art. 7): sono regimi distinti, con procedure ammesse parzialmente sovrapponibili.
- Non assumere che gestori di software open source (art. 3 punto 14) coincidano con fabbricanti: il regime e' diverso e gli OSS commerciali ricevono trattamenti specifici (sanzioni escluse, doc pubblica come prerequisito per usare modulo A per PDE importanti).
- Non rispondere a "quanto e' la sanzione?" senza specificare la fascia: il regolamento ha 3 fasce (Allegato I + artt. 13-14: fino 15M/2,5%; vari altri obblighi: fino 10M/2%; informazioni fuorvianti: fino 5M/1%).

### Cosa fare
- Per ogni classificazione produrre **una catena di citazioni** con riferimento puntuale: ambito (art. 2 par. 1), tipo di prodotto (art. 3 punto 1), funzionalita' principale (Allegato III o IV), eventuale interpretazione dei criteri (art. 7 par. 2 lett. a/b), procedura (art. 32 par. N).
- Per la **matrice procedure-categoria** fare riferimento alla tabella nell'estratto curato, ma riportarla per esteso (no scorciatoie verso "vedi tabella").
- Quando si discute di documentazione tecnica, distinguere chiaramente i 8 punti dell'Allegato VII e mostrare la corrispondenza con gli obblighi sostantivi (art. 13).
- Distinguere chiaramente tra: marcatura CE, numero ON accanto alla marcatura (solo modulo H, art. 30 par. 4), certificato di esame UE del tipo (modulo B), certificato europeo di cibersicurezza (Reg. (UE) 2019/881).
- Concludere ogni output con un disclaimer di responsabilita' del fabbricante/professionista firmatario.

## Validatori

- Validatore di dominio (security/compliance engineer con esperienza CRA) - da identificare per Livello 2 validation.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (`0.1.0-alpha`).
- Validazione: Livello 1 (autore + adversarial review).
- Task files: 4 (`check-ambito-applicabilita`, `classifica-pde`, `scegli-procedura-conformita`, `check-documentazione-tecnica`).
- Esempi: 1 conforme + 1 problematico.
