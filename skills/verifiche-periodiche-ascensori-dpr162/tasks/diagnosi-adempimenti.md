# Task: Diagnosi degli adempimenti di esercizio di un ascensore (DPR 162/1999)

## Obiettivo

Dato un ascensore/montacarichi in esercizio (o in messa in esercizio),
determinare gli adempimenti applicabili: comunicazioni al comune, periodicita' e
soggetti della verifica periodica, casi di verifica straordinaria, obblighi di
manutenzione, libretto e targa.

## Input richiesti

- **tipo di impianto**: ascensore / montacarichi / apparecchio assimilato
  (velocita' <= 0,15 m/s);
- **fase**: nuova messa in esercizio oppure impianto esistente;
- **contesto**: condominio / stabilimento industriale o azienda agricola /
  servizio di pubblico trasporto (rileva per il soggetto verificatore);
- eventuali **eventi** (esito negativo di una verifica, incidente, modifiche
  costruttive);
- (facoltativo) data dell'ultima verifica / della dichiarazione di conformita'
  (per contestualizzare, senza calcolare date al posto dell'utente).

## Fonti da leggere

- `references/estratti/verifiche-ascensori-checklist.md` sezioni 2-6
- se serve conferma: `references/fonti/dpr-162-1999.md` (artt. 12-16)

## Procedura

### Passo 1 - Messa in esercizio (se nuovo impianto) - art. 12
Comunicazione al **comune entro 60 giorni** dalla dichiarazione di conformita'
(contenuti: dati tecnici, ditta di manutenzione abilitata DM 37/2008, soggetto
delle verifiche periodiche). Il comune assegna la **matricola entro 30 giorni**.
Oltre 60 giorni: allegare verbale di verifica straordinaria di attivazione.

### Passo 2 - Verifica periodica - art. 13
**Periodicita': ogni 2 anni.** Soggetto verificatore in base al contesto:
- condominio/generale: **ASL/ARPA** o **organismo di ispezione di tipo A
  accreditato** (ACCREDIA);
- stabilimenti industriali / aziende agricole: **ITL** (o gli altri soggetti);
- pubblico trasporto terrestre: **MIT**;
- anche **organismi di certificazione notificati**.
Verbale al proprietario e al manutentore; se negativo, comunicazione al comune.
Spese a carico del proprietario.

### Passo 3 - Verifica straordinaria - art. 14 (se ricorre un evento)
Necessaria dopo: esito negativo (fermo impianto fino a straordinaria favorevole);
incidente di notevole importanza (fermo immediato); modifiche costruttive.

### Passo 4 - Manutenzione - art. 15
Affidata a persona con **certificato di abilitazione** (prefetto) o ditta
specializzata. Controlli **almeno ogni 6 mesi (ascensori)** / **1 anno
(montacarichi)** su paracadute, limitatore di velocita', funi/catene, isolamento
elettrico e terra, con annotazione sul libretto. Pericolo in atto -> fermo
impianto.

### Passo 5 - Libretto e targa - art. 16
Verbali e visite nel **libretto**; **targa** con soggetto delle verifiche,
matricola, portata.

## Output atteso

- elenco degli adempimenti applicabili con la citazione dell'articolo;
- **periodicita' della verifica periodica** (2 anni) e **soggetto verificatore**
  in base al contesto;
- eventuali verifiche straordinarie dovute agli eventi indicati;
- obblighi di manutenzione con i controlli semestrali/annuali;
- promemoria su libretto e targa;
- avvertenza: la skill non calcola le date concrete delle scadenze e non
  sostituisce proprietario, manutentore e soggetto verificatore.
