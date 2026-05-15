# Task: verifica ambito di applicabilita' PED

## Obiettivo

Verificare se l'attrezzatura a pressione descritta dall'utente ricade nell'ambito di applicazione del D.Lgs 26/2016 (recepimento Direttiva 2014/68/UE - PED) e quindi richiede classificazione e procedura di valutazione della conformita' secondo questa skill, o se ricade in regimi paralleli (apparecchi a pressione semplici, ADR/RID, esclusioni, ecc.).

## Input richiesti

Chiedi all'utente:

- Tipo di attrezzatura: recipiente, tubazione, accessorio di sicurezza, accessorio a pressione, insieme.
- Pressione massima ammissibile PS (bar relativi).
- Volume V (litri) per i recipienti, o dimensione nominale DN per le tubazioni.
- Fluido contenuto (stato fisico - gas/vapore o liquido - e identificazione chimica o famiglia).
- Temperatura massima ammissibile TS (gradi C) e temperatura minima ammissibile.
- Destinazione d'uso (uso industriale fisso, trasporto, militare, navale, nucleare, semplice riscaldamento d'acqua, ecc.).
- Data prevista di immissione sul mercato (per attrezzature pre-19/7/2016 si applica la previgente Dir. 97/23/CE - art. 3 c. 2 D.Lgs 26/2016).

## Fonti

- `references/estratti/dlgs-26-2016-classificazione-moduli.md` sezione 1 (operatori) e sezione 9 (disposizioni transitorie).
- `references/fonti/dlgs-26-2016.md` art. 4 (libera circolazione), art. 4-bis (obblighi fabbricante), art. 3 del D.Lgs 26/2016 (disposizioni finali).

## Procedura

1. **Soglia minima PS**: l'ambito PED si applica solo a PS > 0,5 bar (criterio classico della direttiva PED, replicato nel D.Lgs 93/2000 come modificato dal D.Lgs 26/2016). Se PS <= 0,5 bar, l'attrezzatura non e' soggetta a PED.
2. **Esclusioni tipiche** (segnalare all'utente per verifica puntuale sull'art. 1 del D.Lgs 93/2000 come modificato; questa skill non sostituisce la lettura dell'articolo):
   - recipienti per il trasporto (ADR, RID, IMDG, ICAO);
   - attrezzature classificate non oltre la categoria I e gia' soggette a direttive specifiche (macchine, ascensori, dispositivi medici, ecc.);
   - apparecchi a pressione semplici (Dir. 2014/29/UE, recepita da altro decreto);
   - attrezzature militari, nucleari, recipienti specificamente progettati per impianti nucleari;
   - radiatori e tubazioni di riscaldamento ad acqua calda di tipo "civile";
   - apparecchi destinati al funzionamento all'esterno della normativa PED (es. tubi flessibili, valvole semplici);
   - attrezzature gia' immesse sul mercato prima del 19 luglio 2016 conformi alla 97/23/CE (art. 3 c. 2 D.Lgs 26/2016).
3. **Equiparazione operatore-fabbricante**: se l'utente non e' il fabbricante ma immette sul mercato con proprio nome/marchio o modifica un'attrezzatura immessa in modo tale da poterne condizionare la conformita', e' ritenuto fabbricante ai sensi dell'art. 4-sexies e applica tutti gli obblighi dell'art. 4-bis.
4. **Insiemi**: se l'utente descrive un assemblaggio coordinato di piu' attrezzature a pressione (art. 3 c. 2 D.Lgs 93/2000 modificato), avvisa che la valutazione globale dell'insieme e' regolata dall'art. 10 c. 6 (valutazione di ogni attrezzatura, dell'integrazione, della protezione).
5. **Norme armonizzate**: se l'utente menziona conformita' a norme armonizzate pubblicate in GUCE, segnala che opera la presunzione di conformita' ai RES dell'Allegato I (art. 5 c. 1), ma la skill non valida l'applicabilita' della specifica norma armonizzata al progetto.

## Output

Restituisci un report strutturato in italiano:

```
Verifica ambito PED - <descrizione attrezzatura>

1. Soglia PS > 0,5 bar: <SI / NO> (PS dichiarata: <PS> bar)
2. Tipo: <recipiente / tubazione / accessorio sicurezza / accessorio pressione / insieme>
3. Esclusioni potenzialmente applicabili: <elenco esclusioni segnalate>
4. Operatore: <fabbricante / equiparato ex art. 4-sexies / importatore / distributore>
5. Disposizioni transitorie: <applicabili / non applicabili> (data immissione: <data>)
6. Esito: <RICADE in PED / NON ricade in PED / VERIFICA PUNTUALE su art. 1 D.Lgs 93/2000 modificato>

Rinvio:
- Per la verifica puntuale dell'art. 1 e delle esclusioni si rimanda alla lettura del D.Lgs 93/2000 come modificato dal D.Lgs 26/2016.
- La classificazione finale e la responsabilita' procedurale restano del fabbricante (o del professionista firmatario).
```

## Limiti

- La skill non legge il testo dell'art. 1 del D.Lgs 93/2000 (modificato) per la lista puntuale delle esclusioni: la fornisce in sintesi e rinvia alla lettura diretta.
- Non valuta se un fluido sia "gas instabile", "infiammabile", "tossico" ecc. ai sensi del Regolamento CE 1272/2008: tale classificazione e' a monte (scheda di sicurezza del fluido) e va portata dall'utente.
- Per le esclusioni ai sensi di direttive parallele (es. macchine 2006/42/CE) il limite e' che la skill non verifica se la direttiva alternativa copre tutti i rischi pressione: questo richiede valutazione del professionista.
