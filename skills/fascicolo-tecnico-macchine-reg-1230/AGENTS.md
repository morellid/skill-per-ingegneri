# AGENTS.md - fascicolo-tecnico-macchine-reg-1230

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill supporta la redazione e la verifica del **fascicolo tecnico** (documentazione tecnica) di macchine, prodotti correlati e quasi-macchine ai sensi del **Regolamento (UE) 2023/1230** del 14 giugno 2023, applicabile dal **14 gennaio 2027** in sostituzione della direttiva 2006/42/CE. Target: fabbricanti (uffici tecnici), professionisti incaricati (ingegneri meccanici/elettrici/sicurezza), consulenti CE.

## Fonti autoritative

- **Reg. (UE) 2023/1230** - id `reg-ue-2023-1230-macchine`, SHA256 `c0675483606c8cc65ec4829129f21859fad5f28d9ceb6ed8f938b0c79a714eec`, URL Eur-Lex CELEX 32023R1230, testo italiano GU UE L 165 del 29 giugno 2023.

Estratti gia' preparati in `references/estratti/`:
- `reg-ue-2023-1230-fascicolo-tecnico.md` - sintesi operativa orientata al workflow della skill: ambito, definizioni, scelta procedura (All. I + art. 25), contenuti All. IV parti A/B, dichiarazioni All. V parti A/B, marcatura CE, conservazione 10 anni.

Norme armonizzate UNI/CEN richiamate dal regolamento (es. UNI EN ISO 12100, UNI EN ISO 13849-1, UNI EN 60204-1, UNI EN 12622): **proprietary-paid**, NON trascritte. La skill usa solo rinvii strutturali (numero, ambito).

## Articoli e punti chiave

- **Art. 2 par. 1-2**: ambito ed esclusioni (a-q).
- **Art. 3 punto 1, 3, 4, 10, 12, 13, 14, 16, 18, 19, 24, 25**: definizioni di macchina, componente di sicurezza, funzione di sicurezza, quasi-macchina, immissione, messa in servizio, RES, modifica sostanziale, fabbricante, mandatario, norma armonizzata, marcatura CE.
- **Art. 6 par. 1**: rinvio ad All. I parte A (procedure art. 25 par. 2) e parte B (procedure art. 25 par. 3).
- **Art. 10 par. 1-8**: obblighi del fabbricante di macchine/prodotti correlati (fascicolo, dichiarazione UE, marcatura CE, identificazione, istruzioni d'uso, conservazione 10 anni).
- **Art. 11 par. 1-8**: obblighi del fabbricante di quasi-macchine (fascicolo All. IV parte B, dichiarazione di incorporazione, istruzioni di assemblaggio All. XI).
- **Art. 20 par. 1, 3, 6, 9**: presunzione di conformita' tramite norme armonizzate, specifiche comuni, certificazione cibersicurezza (Reg. (UE) 2019/881).
- **Art. 21**: dichiarazione UE di conformita' (rinvio All. V parte A).
- **Art. 22**: dichiarazione di incorporazione UE (rinvio All. V parte B).
- **Art. 23-24**: marcatura CE - apposizione prima dell'immissione (par. 2); numero ON se procedura con ON (par. 3).
- **Art. 25 par. 2-4**: procedure di valutazione della conformita' - parte A (Modulo B+C, H, G), parte B (Modulo A condizionato, B+C, H, G), non in All. I (Modulo A).
- **Art. 51 par. 2**: abrogazione direttiva 2006/42/CE dal 14/01/2027.
- **Art. 52**: disposizioni transitorie (prodotti immessi prima del 14/01/2027 conformi alla 2006/42/CE possono circolare; certificati esame CE del tipo restano validi fino a scadenza).
- **Art. 54**: applicazione dal 14/01/2027 con eccezioni anticipate elencate.
- **All. I parte A** (6 categorie): macchine ad alto rischio, sempre con organismo notificato.
- **All. I parte B** (19 categorie): macchine classiche, Modulo A condizionato all'applicazione integrale di norme armonizzate/specifiche comuni.
- **All. IV parte A** (lett. a-o): documentazione tecnica per macchine/prodotti correlati.
- **All. IV parte B** (lett. a-m): documentazione tecnica per quasi-macchine.
- **All. V parte A** (10 voci): struttura tipo dichiarazione UE di conformita'.
- **All. V parte B** (9 voci): struttura tipo dichiarazione di incorporazione UE.
- **All. VI**: Modulo A (controllo interno della produzione).
- **All. VII**: Modulo B (esame UE del tipo) - certificato validita' max 5 anni (punto 6.1).
- **All. VIII**: Modulo C.
- **All. IX**: Modulo H (garanzia qualita' totale).
- **All. X**: Modulo G (verifica dell'unita').
- **All. XI**: istruzioni per l'assemblaggio delle quasi-macchine (lett. a-n).

## Convenzioni specifiche

### Cosa NON fare

- Non confondere **macchina** con **quasi-macchina**: regime documentale, dichiarazione e marcatura CE sono diversi.
- Non apporre la **marcatura CE su una quasi-macchina** (e' vietato; la quasi-macchina ha solo dichiarazione di incorporazione UE).
- Non citare la direttiva 2006/42/CE come riferimento normativo positivo: per le immissioni dal 14/01/2027 e' abrogata. La 2006/42/CE compare solo per regime transitorio (art. 52).
- Non riprodurre il testo dell'**Allegato III** (RES): rinviare alla lettura diretta del regolamento.
- Non riprodurre il contenuto delle **norme armonizzate UNI/CEN** (proprietary-paid). Solo rinvii strutturali (numero norma, ambito di applicazione).
- Non concludere che il **Modulo A** sia utilizzabile per una categoria All. I parte B senza la verifica della copertura integrale dei RES da parte delle armonizzate applicate (art. 25 par. 3 lett. a).
- Non promettere che la skill validi l'applicabilita' di una specifica norma armonizzata al progetto: e' fuori scope.
- Non confondere **Allegato XII** (tavola di concordanza con 2006/42/CE) con **Allegato II** (elenco indicativo componenti di sicurezza) o **Allegato III** (RES). Sono tre cose diverse.

### Cosa fare

- Citare sempre il riferimento puntuale: articolo + paragrafo + lettera, oppure allegato + parte + lettera/punto numerato.
- Distinguere subito macchina vs quasi-macchina come primo passo del workflow.
- Per le procedure di conformita': mappare prima la categoria in All. I parte A/B/non-in-elenco, poi applicare l'art. 25 paragrafo corrispondente.
- Per la dichiarazione UE: rispettare l'ordine delle voci dell'All. V parte A (10) o parte B (9) - non rinominarle, non saltarne.
- Marcare esplicitamente che la firma, la responsabilita' e la conservazione decennale restano del fabbricante (o mandatario nei limiti del mandato).
- Per i RES applicabili: rinviare alla lettura diretta dell'Allegato III, senza riprodurlo.

## Validatori

- Da identificare per validazione Livello 2 (ingegnere meccanico/elettrico esperto in marcatura CE macchine, esterno all'autore della skill).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (`0.1.0-alpha` iniziale).
- Validazione: Livello 1 (validate.sh + review adversariale interna).
- Task files: `qualifica-prodotto.md`, `identifica-procedura-conformita.md`, `struttura-fascicolo-tecnico.md`, `check-completezza-fascicolo.md`, `struttura-dichiarazione-ue.md`.
- Esempi: 1 conforme (`pressa-piegatrice-allegato-i-parte-b`), 1 problematico (`quasi-macchina-attuatore-lineare-incompleto`).
