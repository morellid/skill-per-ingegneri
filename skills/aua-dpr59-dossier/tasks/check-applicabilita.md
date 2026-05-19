# Task - Verifica applicabilita' dell'AUA

## Obiettivo

Determinare se un impianto/attivita' rientra nell'ambito di applicazione del
D.P.R. 59/2013 (art. 1) prima di impostare il dossier AUA.

## Input richiesti dall'utente

Chiedere all'utente, in ordine:

1. **Settore di attivita'** dell'impresa (codice ATECO o descrizione).
2. **Dimensione dell'impresa**: numero dipendenti, fatturato annuo, totale di
   bilancio (per il check PMI ai sensi del DM 18 aprile 2005, GU n.238 del
   12/10/2005, richiamato nell'art. 1 co. 1 del D.P.R. 59/2013).
3. **Soggezione ad AIA**: l'impianto rientra nelle categorie del D.Lgs.
   152/2006, Titolo III-bis Parte II (Allegato VIII, attivita' IPPC)?
4. **Soggezione a VIA**: il progetto e' sottoposto a VIA con provvedimento
   finale che assorbe e sostituisce gli altri atti di assenso ambientale
   (art. 26 co. 4 D.Lgs. 152/2006)?
5. **Regione/Provincia Autonoma** in cui ha sede l'impianto (per richiamare
   l'eventuale ampliamento regionale del perimetro ex art. 3 co. 2 e
   l'autorita' competente ex art. 2 co. 1 lett. b).
6. **Titoli ambientali attualmente in essere** (anche solo lista nominale).

## Fonti

- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 1 (Ambito di
  applicazione).
- `references/fonti/dpr-59-2013-articoli-1-12.md` art. 1 e art. 2.

## Procedura

### Step 1 - check dimensionale (PMI)

L'AUA si applica alle PMI come definite dall'art. 2 del DM 18 aprile 2005.
La definizione (Reg. CE 800/2008, oggi sostituito da Reg. UE 651/2014 ai fini
aiuti di Stato, ma il rinvio del D.P.R. 59/2013 e' al DM 18/4/2005 quale
norma di trasposizione interna in vigore al 2013) richiede:

- impresa **media**: < 250 dipendenti E (fatturato ≤ 50 M€ OPPURE totale di
  bilancio ≤ 43 M€), con autonomia di impresa;
- impresa **piccola**: < 50 dipendenti E (fatturato ≤ 10 M€ OPPURE totale
  di bilancio ≤ 10 M€);
- impresa **micro**: < 10 dipendenti E (fatturato ≤ 2 M€ OPPURE totale di
  bilancio ≤ 2 M€).

Se l'impresa supera la soglia "media" **e** non rientra in AIA, l'AUA si
applica comunque agli "impianti non soggetti ad AIA" (art. 1 co. 1, seconda
parte): la soglia PMI e' alternativa, non cumulativa, al criterio
"impianti non-AIA". Quindi per le grandi imprese non-AIA l'AUA si applica
ugualmente: chiarire all'utente la ratio.

### Step 2 - check AIA

Se l'impianto rientra in una categoria dell'Allegato VIII alla Parte II del
D.Lgs. 152/2006 (attivita' IPPC: impianti chimici di grandi dimensioni,
acciaierie, cementifici, allevamenti intensivi sopra soglie, ecc.), l'AUA
**non si applica**: si deve seguire la procedura AIA, regolata da norme
diverse.

Output di questo step: "applicabile" / "non applicabile (AIA)".

### Step 3 - check VIA assorbente

Verificare se il progetto e' sottoposto a VIA e se la normativa statale o
regionale prevede che il provvedimento finale di VIA comprenda e
sostituisca tutti gli altri atti di assenso ambientale (art. 26 co. 4
D.Lgs. 152/2006). Se SI, l'AUA non si applica (art. 1 co. 2 D.P.R.
59/2013).

### Step 4 - opt-out facoltativo (art. 3 co. 3)

Se l'impianto e' soggetto **solo** a comunicazione o ad autorizzazione di
carattere generale (es. tipologie dell'Allegato I del D.P.R. 59/2013 ex
art. 272 D.Lgs. 152/2006), segnalare all'utente che puo' scegliere di non
avvalersi dell'AUA (art. 3 co. 3): l'istanza passa comunque per il SUAP
ma resta nella forma di comunicazione o autorizzazione generale. In
questo scenario, valutare con l'utente i pro e i contro:

- pro AUA: durata 15 anni; titolo unico riusabile per ampliamenti futuri.
- pro opt-out: procedura piu' leggera per la singola comunicazione;
  evita di "consumare" la durata dell'AUA su attivita' che non la
  richiederebbero.

### Step 5 - perimetro regionale ampliato (art. 3 co. 2)

Ricordare all'utente di verificare se la propria Regione ha individuato
ulteriori atti di comunicazione, notifica o autorizzazione ambientale
ricompresi nell'AUA: in tal caso il perimetro dell'AUA puo' essere piu'
ampio della lista dell'art. 3 co. 1. La skill non conosce le discipline
regionali; rinvio alla legislazione regionale specifica.

## Output

Un report sintetico (Markdown) con la struttura seguente:

```
# Verifica applicabilita' AUA - [nome impianto]

## 1. Dimensione impresa
- Classificazione PMI: micro / piccola / media / non PMI
- [esito step 1]

## 2. Soggezione ad AIA
- Categoria Allegato VIII Parte II D.Lgs. 152/2006: si / no / da verificare
- [esito step 2]

## 3. Soggezione a VIA con assorbimento
- Procedura VIA: si / no
- VIA assorbente ex art. 26 co. 4 D.Lgs. 152/2006: si / no / da verificare
- [esito step 3]

## 4. Opt-out facoltativo (art. 3 co. 3)
- L'impianto e' soggetto solo a comunicazione/autorizzazione generale: si / no
- Consiglio: [scegliere AUA vs opt-out, con motivazione]

## 5. Perimetro regionale
- Regione: [...]
- Verificare ampliamento perimetro AUA ex art. 3 co. 2 D.P.R. 59/2013 nelle
  fonti regionali (legge regionale, delibere Giunta, modulistica SUAP).

## Conclusione
- L'AUA e' / non e' applicabile / da verificare ulteriormente.
- Prossimi passi consigliati: [...].

## Avvertenza
Questa verifica e' un'autoanalisi preliminare. La determinazione formale e'
del SUAP e dell'autorita' competente. Per la classificazione AIA/VIA
consultare un tecnico abilitato.
```

## Limiti del task

- Non determina la categoria AIA in autonomia: lasciare al tecnico la
  verifica puntuale dell'Allegato VIII (le voci richiedono interpretazione
  di soglie produttive e categorie merceologiche).
- Non valuta l'esito VIA: la decisione "VIA assorbente" e' della
  Commissione VIA competente.
- Non sostituisce la verifica del PMI Status nel contesto degli aiuti di
  Stato (per quello si usa l'autocertificazione PMI prevista dal Reg. UE
  651/2014); il check PMI qui e' ai soli fini ambito AUA.
