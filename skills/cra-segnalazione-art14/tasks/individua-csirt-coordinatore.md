# Task: individuare il CSIRT coordinatore territorialmente competente

## Obiettivo

Stabilire **a quale terminale nazionale** il fabbricante deve indirizzare le notifiche
dell'art. 14, applicando il criterio dello stabilimento principale (art. 14, par. 7) e,
se il fabbricante non e' stabilito nell'Unione, la cascata delle lettere a)-d).

## Input richiesti

1. **Dove sono prevalentemente adottate le decisioni relative alla cibersicurezza** dei
   PDE del fabbricante. Non "dov'e' la sede legale": il criterio del testo e' questo.
2. Se il punto 1 non e' determinabile: numero di dipendenti per stabilimento nell'Unione.
3. Se il fabbricante non ha stabilimento nell'Unione, nell'ordine e per quanto noto:
   - Stato membro del rappresentante autorizzato e per quanti PDE agisce;
   - Stato membro dell'importatore e quanti PDE immette sul mercato;
   - Stato membro del distributore e quanti PDE mette a disposizione;
   - Stato membro con il maggior numero di utilizzatori.
4. Se ci sono state notifiche precedenti e a quale CSIRT.

## Fonti

- `../references/estratti/cra-art14-obblighi-e-termini.md`, sezione D.
- `../references/estratti/csirt-coordinatore-e-canale-italiano.md` (tutte le sezioni).
- `../references/fonti/reg-ue-2024-2847-cra-segnalazione.md`, art. 14 par. 7; art. 16.
- `../references/fonti/dir-ue-2022-2555-nis2-segnalazione.md`, art. 12 par. 1.
- `../references/fonti/dlgs-138-2024-csirt-italia.md`, art. 2 c. 1 lett. i), artt. 15-16.

## Procedura

### Passo 1 - Il fabbricante ha uno stabilimento principale nell'Unione?

Il criterio del par. 7, secondo comma, e' lo Stato membro **"in cui sono prevalentemente
adottate le decisioni relative alla cibersicurezza dei suoi prodotti con elementi
digitali"**.

Non usare come sostituti: sede legale, sede fiscale, Stato di costituzione, Stato in cui
si vende di piu'. Se questi divergono dal luogo delle decisioni di cibersicurezza,
segnalalo esplicitamente nell'output.

Se il criterio decisionale non e' determinabile, si applica il criterio sussidiario: lo
Stato membro dello stabilimento con il **maggior numero di dipendenti** nell'Unione.

### Passo 2 - Fabbricante senza stabilimento principale nell'Unione: applica la cascata

Il par. 7, terzo comma, fissa un ordine **vincolante**, da percorrere sulla base delle
informazioni a disposizione del fabbricante. Non si sceglie la voce piu' comoda: si
scende alla successiva solo quando la precedente non e' applicabile.

| Ordine | Criterio |
|---|---|
| a) | Stato membro del **rappresentante autorizzato** che agisce per il maggior numero di PDE del fabbricante |
| b) | Stato membro dell'**importatore** che immette sul mercato il maggior numero di PDE |
| c) | Stato membro del **distributore** che mette a disposizione il maggior numero di PDE |
| d) | Stato membro in cui e' situato il **maggior numero di utilizzatori** dei PDE |

Nota di stabilita': **solo** per il caso della lett. d) il quarto comma consente al
fabbricante di continuare a usare **lo stesso** CSIRT per le notifiche successive. Negli
altri casi il testo non prevede questa continuita': se la situazione cambia, il CSIRT
competente puo' cambiare.

### Passo 3 - Traduci lo Stato membro nel CSIRT designato coordinatore

Il CRA **non nomina** il CSIRT di alcuno Stato membro. La figura viene dall'art. 12,
par. 1, della direttiva (UE) 2022/2555, che impone a ogni Stato membro di designare uno
dei propri CSIRT come coordinatore ai fini della divulgazione coordinata delle
vulnerabilita'.

- **Italia**: la designazione e' nel D.Lgs. 138/2024, art. 16, comma 1 - il **CSIRT
  Italia** e' designato coordinatore. Ai sensi dell'art. 2, comma 1, lett. i), il CSIRT
  Italia opera **all'interno dell'Agenzia per la cybersicurezza nazionale (ACN)**.
- **Altri Stati membri**: la designazione e' nel rispettivo atto di recepimento della
  NIS2, che **non e' fra le fonti lette da questa skill**. Non nominare il CSIRT di un
  altro Stato membro a memoria: indica lo Stato membro competente secondo i Passi 1-2 e
  rinvia alla verifica sull'elenco dei CSIRT coordinatori (Rete di CSIRT nazionali /
  ENISA) e sull'atto di recepimento nazionale.

### Passo 4 - Ricorda i destinatari simultanei

L'art. 14, par. 1 e 3, impone la notifica **al CSIRT coordinatore e all'ENISA**,
"simultaneamente". L'art. 14, par. 7, precisa che le notifiche trasmesse sul terminale
del CSIRT competente sono contemporaneamente accessibili all'ENISA. Non presentare la
notifica all'ENISA come un adempimento separato da fare a parte, ne' ometterla.

### Passo 5 - Avvertenza sul canale operativo

Chiudi sempre con questa avvertenza, senza attenuarla:

- Nessuna delle fonti lette descrive il **terminale italiano per la notifica
  elettronica**: non ci sono URL, modalita' di accreditamento, credenziali o tempistiche
  di attivazione nel testo del CRA, della NIS2 o del D.Lgs. 138/2024.
- L'art. 16 (piattaforma unica) **non e' fra le disposizioni anticipate** dall'art. 71,
  par. 2, all'11 settembre 2026. Lo stato effettivo della piattaforma va verificato sui
  canali ufficiali ENISA e ACN/CSIRT Italia al momento dell'uso.
- La **politica nazionale di divulgazione coordinata delle vulnerabilita'** prevista
  dall'art. 16, comma 4, del D.Lgs. 138/2024 e' un atto successivo, non letto da questa
  skill: puo' contenere prescrizioni operative rilevanti.

Non inventare indirizzi, portali o moduli. Se l'utente chiede "qual e' il link",
rispondi che le fonti normative non lo contengono e che va cercato su ACN/CSIRT Italia
ed ENISA.

### Passo 6 - Non confondere i regimi

Se il fabbricante e' **anche** sottoposto al regime di notifica del D.Lgs. 138/2024, non
dedurne che la notifica NIS2 assolva l'obbligo del CRA o viceversa. I due regimi hanno
presupposti, termini e destinatari propri e nessuna fonte letta prevede che uno assorba
l'altro. Non affermare se quel decreto si applichi al fabbricante: di esso questa skill
ha letto i soli artt. 2, 15 e 16, che non ne definiscono l'ambito soggettivo. Segnala la
sovrapposizione come punto da chiarire col consulente, non come semplificazione.

## Output

1. Stato membro competente, con il criterio applicato (decisioni di cibersicurezza,
   dipendenti, o quale lettera della cascata) e i dati su cui si fonda.
2. CSIRT coordinatore: nominato solo per l'Italia (CSIRT Italia presso ACN); per gli
   altri Stati membri, rinvio alla verifica con la fonte da consultare.
3. Promemoria dei destinatari simultanei (CSIRT + ENISA).
4. Se ricorre la lett. d), nota sulla possibilita' di mantenere lo stesso CSIRT.
5. Avvertenza del Passo 5, integrale.
6. Se rilevante, nota sulla sovrapposizione NIS2/CRA del Passo 6.

## Limiti

- Non elenca i CSIRT coordinatori degli altri Stati membri: le designazioni nazionali non
  sono fra le fonti lette.
- Non descrive l'accreditamento al terminale nazionale ne' alla piattaforma dell'art. 16.
- Non stabilisce dove sia lo stabilimento principale: applica il criterio ai fatti che il
  fabbricante fornisce. Se i fatti sono ambigui, espone le alternative senza sceglierne
  una.
- Non contiene il testo della politica nazionale CVD ne' del D.L. 82/2021: entrambi sono
  citati dalle fonti ma non letti.
