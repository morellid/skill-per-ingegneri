---
name: valutazione-impatto-clima-acustico-l-447
description: Supporto al tecnico competente in acustica ambientale (TCAA) e al progettista per la documentazione previsionale di impatto acustico (L. 447/1995 art. 8 c. 2 e c. 4) e per la valutazione previsionale di clima acustico (L. 447/1995 art. 8 c. 3) da allegare a SCIA, PdC, autorizzazione/licenza ex L. 447/1995 - mappa applicabilita' (impatto, clima, entrambi, nulla-osta), check completezza dei contenuti minimi della relazione, riferimenti puntuali a DPCM 14/11/1997 (valori limite) e DM 16/03/1998 (tecniche di misurazione). Use when user is preparing or reviewing a noise impact / noise climate assessment under Italian L. 447/1995 art. 8.
license: MIT
---

# Valutazione di impatto e clima acustico - L. 447/1995 art. 8

## Quando usare questa skill

Questa skill aiuta il **tecnico competente in acustica ambientale (TCAA)**,
l'ingegnere progettista o il consulente che predispone o revisiona la
**documentazione previsionale di impatto acustico** (ex art. 8 c. 2 e
c. 4 della L. 26 ottobre 1995 n. 447) o la **valutazione previsionale
di clima acustico** (ex art. 8 c. 3 della stessa legge), da allegare al
titolo abilitativo edilizio (PdC, SCIA), alla domanda di licenza /
autorizzazione all'esercizio di un'attivita' produttiva, sportiva o
ricreativa, oppure al procedimento di VIA.

Target: TCAA, ingegnere ambientale / acustico, progettista di opere o
insediamenti, consulente urbanistico, consulente del committente o
dell'amministrazione.

NON usare questa skill per:
- Eseguire misure fonometriche o calcoli predittivi di propagazione
  (la skill non sostituisce un fonometro classe 1 calibrato ne' un
  software di propagazione conforme a ISO 9613-2 / DPCM applicabili).
- Redigere documentazione di valutazione di **impatto ambientale (VIA)**
  in senso lato (D.Lgs. 152/2006 Parte II): la valutazione acustica e'
  un capitolo del SIA, ma la VIA include comparti diversi (aria, acque,
  rifiuti, ecc.) fuori scope.
- Verifica del **rumore in ambiente di lavoro** (esposizione dei
  lavoratori): disciplinata da D.Lgs. 81/2008 Titolo VIII Capo II,
  riferimento normativo e finalita' diverse, fuori scope.
- Adempimenti specifici della **classificazione acustica comunale**
  (zonizzazione ex art. 6 c. 1 lett. a) L. 447/1995): fuori scope.
- Predisposizione del **piano di risanamento acustico** comunale o
  aziendale (art. 7 e art. 15 L. 447/1995): fuori scope.

## Avvertenza

Questa skill e' uno strumento di **supporto** alla redazione/verifica
della documentazione previsionale di impatto e di clima acustico.
**Non sostituisce il giudizio del professionista firmatario** (TCAA
iscritto all'elenco nazionale ai sensi del D.Lgs. 17 febbraio 2017
n. 42 e tecnico abilitato per le competenze progettuali). L'utilizzo
improprio degli output e' responsabilita' esclusiva dell'utente. La
skill **non produce documenti pronti al deposito o alla firma**, **non
calcola valori previsionali di Leq**, **non riproduce testualmente
parametri o coefficienti dei decreti attuativi specifici delle
infrastrutture dei trasporti** (D.P.R. 459/1998 ferroviario, D.P.R.
142/2004 stradale), e **non sostituisce la verifica dei criteri di
dettaglio della legge regionale e del regolamento comunale** che, ai
sensi dell'art. 4 c. 1 lett. l) L. 447/1995 e dell'art. 6 c. 2 della
stessa legge, disciplinano contenuti e modalita' di presentazione della
documentazione.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da
`tasks/`:

- **Mappa applicabilita' art. 8 L. 447/1995**: quando l'utente chiede di
  capire se la sua opera/insediamento richiede documentazione di impatto
  acustico (c. 2), valutazione previsionale di clima acustico (c. 3),
  domanda con previsione di impatto acustico per concessione edilizia o
  licenza (c. 4), nulla-osta in caso di emissioni previste superiori ai
  limiti (c. 6), oppure nessuna documentazione - leggere
  `tasks/mappa-applicabilita-art-8.md`.
- **Check completezza documentazione di impatto acustico**: quando
  l'utente chiede di verificare se una documentazione di impatto
  acustico e' completa rispetto ai contenuti minimi attesi (sorgenti,
  classe acustica, periodo diurno/notturno, valori limite di emissione
  e di immissione assoluti, valori differenziali, modalita' di
  misurazione DM 16/03/1998) - leggere
  `tasks/check-completezza-impatto-acustico.md`.
- **Check completezza valutazione previsionale di clima acustico**:
  quando l'utente chiede di verificare se una valutazione di clima
  acustico per insediamento sensibile (scuola, ospedale, casa di cura,
  parco pubblico, nuovo insediamento residenziale prossimo a opere
  c. 2) e' completa - leggere `tasks/check-completezza-clima-acustico.md`.
- **Checklist relazione previsionale (contenuti tecnici)**: quando
  l'utente chiede cosa deve contenere la relazione previsionale in
  termini di descrittori, strumentazione, condizioni meteo, criterio
  differenziale, riferimenti normativi - leggere
  `tasks/checklist-relazione-previsionale.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita'
desidera, partendo da una breve qualificazione del caso (tipo opera o
insediamento, comune, classe acustica se nota, presenza di
infrastrutture dei trasporti adiacenti).

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input minimi (tipo opera/insediamento, comune, classe
   acustica della zona di intervento e di quelle confinanti, presenza
   di infrastrutture dei trasporti adiacenti, presenza di ambienti
   abitativi di terzi entro la portata acustica prevista, periodo di
   esercizio diurno/notturno).
4. Applica la procedura del task, citando articoli/commi puntuali
   (mai "la legge dice in generale"). Tutti i riferimenti normativi
   citati devono trovarsi nelle voci di `references/sources.yaml`.
5. Produci output strutturato: lista di item con esito "OK / mancante /
   da verificare / non applicabile", riferimento normativo, azione
   richiesta al professionista.
6. Includi sempre nel report finale il rinvio:
   - alla **verifica della legge regionale** applicabile (art. 4 c. 1
     lett. l) L. 447/1995);
   - alla **verifica del regolamento comunale** in materia di
     inquinamento acustico (art. 6 c. 2 L. 447/1995);
   - al **testo vigente** della L. 447/1995 su Normattiva al momento
     del deposito;
   - al **professionista firmatario**: TCAA iscritto all'elenco
     nazionale (D.Lgs. 42/2017 art. 21) per la parte fonometrica e
     previsionale, progettista abilitato per la parte progettuale.

## Fonti normative

Catalogate in `references/sources.yaml`. Estratti testuali in
`references/estratti/`:

- `legge-447-1995-art-8.md` - L. 26 ottobre 1995 n. 447, art. 8
  (impatto e clima acustico) + art. 4 c. 1 lett. l) (rinvio Regioni)
  + art. 6 c. 1 lett. d) (controllo comunale) + art. 2 (definizioni).
- `dpcm-14-11-1997-valori-limite.md` - DPCM 14 novembre 1997, articoli
  1-7 + Allegato (Tabelle A, B, C, D).
- `dm-16-03-1998-tecniche-misurazione.md` - DM Ambiente 16 marzo 1998,
  articoli 1-4 + Allegati A (definizioni), B (tecniche misure), C
  (rumore stradale e ferroviario), D (presentazione risultati).

## Limiti

Cosa questa skill NON fa:

- Non produce documenti auto-firmati ne' relazioni fonometriche /
  previsionali pronte al deposito.
- Non esegue calcoli previsionali di Leq, propagazione, attenuazione
  per distanza, schermatura o assorbimento atmosferico.
- Non riproduce in numeri i valori specifici dei decreti attuativi
  delle infrastrutture dei trasporti (DPR 459/1998, DPR 142/2004), che
  hanno fasce di pertinenza, tabelle e regimi propri non sostituibili
  con il DPCM 14/11/1997.
- Non interpreta dissensi qualificati nel procedimento autorizzativo.
- Non sostituisce la **legge regionale** e i **criteri regionali** di
  attuazione dell'art. 4 c. 1 lett. l) L. 447/1995, che disciplinano
  contenuti e modalita' di presentazione della documentazione di cui
  all'art. 8 commi 2, 3, 4.
- Non sostituisce il **regolamento comunale** in materia di inquinamento
  acustico (art. 6 c. 2 L. 447/1995).
- Non gestisce il **rumore in ambiente di lavoro** (D.Lgs. 81/2008
  Titolo VIII Capo II): scope diverso.
- Non gestisce la **classificazione acustica comunale** ne' il **piano
  di risanamento** (art. 6 c. 1 lett. a) e art. 7 L. 447/1995).
