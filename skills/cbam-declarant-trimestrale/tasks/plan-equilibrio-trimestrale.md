# Pianificazione dell'obbligo trimestrale 50 % di certificati CBAM (Art. 22 §2)

## Obiettivo

Stimare il numero di **certificati CBAM** che il dichiarante CBAM autorizzato deve detenere sul proprio conto nel registro CBAM **al termine di ciascun trimestre** a decorrere dal **1° gennaio 2027** (Art. 22 §2 ▼M1 + Art. 36 punto 2 + Reg. 2025/2083 Art. 2), in modo da rispettare l'**equilibrio del 50 %** delle emissioni incorporate cumulate dall'inizio dell'anno civile.

Fornire un **calendario di acquisto** sulla **piattaforma centrale comune** (operativa dal 1/2/2027, Art. 20 §1 ▼M1), un **range di esposizione** in EUR sulla base del prezzo settimanale Art. 21 §1 ▼M1 (con la **deroga 2026** = media trimestrale ETS, Art. 21 §1bis ▼M1) e indicare il **margine di sicurezza** rispetto al rischio di shortfall (eventuale sanzione Art. 26 §1).

## Input richiesti

Chiedere all'utente:

1. **Anno civile di riferimento** (per la prima applicazione: **2027**; il 2026 ha solo il regime di restituzione annuale dell'Art. 22 §1 - **nessun** obbligo trimestrale).
2. **Volumi attesi di importazione per trimestre** (Q1-Q4), per ciascuna combinazione (codice NC a 8 cifre, paese di origine), in massa netta (tonnellate) o in MWh per l'elettricita'.
3. **Metodo di calcolo prescelto** ai sensi dell'Art. 22 §2 lettere a-b ▼M1:
   - lettera **a**: valori predefiniti Allegato IV **senza** la maggiorazione di cui al punto 4.1; oppure
   - lettera **b**: numero di certificati CBAM restituiti per l'anno civile **precedente** per **stesse merci con stesso codice NC e stessi paesi di origine** (richiede che esista una dichiarazione CBAM dell'anno precedente).
4. **Adeguamento per assegnazione gratuita** (Art. 31): l'utente ha una formula gia' calcolata in base agli atti di esecuzione vigenti? In caso negativo: avvertire che la skill non calcola Art. 31, ma usa il dato dell'utente come variabile di input (default = 0 se non fornito; flag professionista).
5. **Saldo del conto CBAM all'inizio dell'anno civile** (per riacquisti / certificati residui non cancellati).
6. **Carbon price paese terzo** (Art. 9 ▼M1): l'utente ha gia' una stima della detrazione? Anche qui solo come input (con flag).
7. **Prezzo di riferimento dei certificati**:
   - per anno 2027: media settimanale chiusure ETS sulla piattaforma d'asta (Art. 21 §1 ▼M1); l'utente fornisce un range realistico o accetta un range conservativo;
   - per anno 2026 (rilevante solo per la **restituzione annuale** Art. 22 §1, **non** per l'obbligo trimestrale): media trimestrale ETS del trimestre di importazione (Art. 21 §1bis ▼M1 - deroga 2026).

## Fonti

- Estratto di riferimento: `references/estratti/reg-ue-2023-956-articoli-fase-definitiva.md` sezione D (Vendita, prezzo e restituzione certificati).
- Testo integrale degli articoli: `references/fonti/reg-ue-2023-956-cbam-consolidato.md`.
- Ratio: `references/estratti/reg-ue-2025-2083-considerando-chiave.md` considerando 26-28 (piattaforma e diritti, vendita certificati, riduzione 80% -> 50%).

Articoli da citare:

- **Art. 22 §1 ▼M1** (restituzione annuale entro 30/9, prima volta 2027 per anno 2026).
- **Art. 22 §2 ▼M1** lettere a-b (obbligo trimestrale 50 %, dal 2027). Tiene conto dell'**adeguamento Art. 31**.
- **Art. 22 §2bis ▼M1** (chi supera la soglia rispetta l'obbligo entro la fine del trimestre **successivo**).
- **Art. 20 §1 ▼M1** (vendita via piattaforma centrale comune dal 1/2/2027) e §5bis (diritti a carico dei dichiaranti per coprire i costi della piattaforma).
- **Art. 21 §1 ▼M1** (prezzo settimanale) e **§1bis ▼M1** (deroga 2026 - prezzo trimestrale).
- **Art. 23 ▼M1** §§1-2bis (riacquisto eccedenza entro 31 ottobre, limite = certificati Art. 22 §2; per il 2027 i certificati relativi al 2026 sono riacquistabili solo nel 2027).
- **Art. 24 §1 ▼M1** (cancellazione certificati il 1° novembre di ogni anno - quelli acquistati nell'anno anteriore all'anno civile precedente).
- **Allegato IV punto 4.1** (valori predefiniti = intensita' media paese esportatore + maggiorazione; quando manca il dato del paese, intensita' media dei 10 paesi esportatori con le intensita' piu' elevate).
- **Art. 31** (adeguamento per assegnazione gratuita - fuori scope del calcolo della skill, rinvio agli atti di esecuzione).

## Procedura

### Passo 1 - Verificare l'applicabilita' temporale

L'**obbligo trimestrale 50 %** decorre dal **1° gennaio 2027** (Art. 36 + Reg. 2025/2083 Art. 2). Per l'anno 2026 vale **solo** il regime di restituzione annuale Art. 22 §1 (entro 30/9/2027 per l'anno 2026).

Se l'utente chiede di pianificare il 2026, ricordare:
- nessuna detenzione trimestrale obbligatoria (Art. 22 §2 non si applica al 2026);
- la vendita di certificati e' attiva dal **1/2/2027** (Art. 20 §1 ▼M1);
- per i certificati acquistati nel 2027 per emissioni 2026, il prezzo e' calcolato come **media trimestrale** ETS del trimestre di importazione (Art. 21 §1bis ▼M1).

### Passo 2 - Stima delle emissioni incorporate per trimestre

Per ciascun trimestre Q (Q1, Q2, Q3, Q4) e ciascuna combinazione (NC, paese di origine):

- **Caso A - Metodo Art. 22 §2 lettera a** (valori predefiniti **senza maggiorazione**):
  ```
  E_Q (t CO2e) = sum_{NC, paese} [ Vol_{Q,NC,paese} * VP_{NC,paese, senza_maggiorazione} ]
  ```
  dove `VP_{NC,paese, senza_maggiorazione}` e' il valore predefinito dell'Allegato IV punto 4.1 **al netto** della maggiorazione proporzionale (la maggiorazione si applica nel calcolo della dichiarazione annuale ma **non** ai fini dell'obbligo trimestrale, per esplicita previsione dell'Art. 22 §2 lettera a ▼M1).
- **Caso B - Metodo Art. 22 §2 lettera b** (baseline anno precedente):
  ```
  E_Q (t CO2e) = sum_{NC, paese} [ Vol_{Q,NC,paese} * (cert_restituiti_anno_prec_{NC,paese} / Vol_anno_prec_{NC,paese}) ]
  ```
  ammissibile **solo** se le combinazioni (NC, paese) del trimestre Q corrispondono a quelle dichiarate nell'anno precedente. Per nuove combinazioni resta obbligatorio il metodo lettera a.

Sommare cumulativamente dall'inizio dell'anno: `E_cum_Q1, E_cum_Q2 = E_Q1+E_Q2, E_cum_Q3, E_cum_Q4`.

### Passo 3 - Calcolo dei certificati richiesti

Per ciascun trimestre Q, applicare:

```
N_cert_Q = ceiling( 0.5 * (E_cum_Q - adeguamento_Art31_cum_Q - detrazione_Art9_cum_Q) )
```

dove:

- 1 certificato CBAM = 1 t CO2e (Art. 20 §2 ▼M1);
- `adeguamento_Art31` e `detrazione_Art9` vanno richiesti all'utente (la skill **non** li calcola);
- l'obbligo del 50 % e' "almeno" -> il dichiarante puo' detenere di piu' (per fluttuazione del prezzo) ma non di meno (Art. 22 §2: "almeno il 50 %").

Per il **caso Art. 22 §2bis ▼M1** (importatore che ha superato la soglia in corso d'anno): l'obbligo del 50 % cumulativo va rispettato **entro la fine del trimestre successivo** a quello del superamento (es. superamento in Q2 -> obbligo Q3 fine).

### Passo 4 - Determinare il saldo da acquistare per trimestre

```
acquisto_Q = max(0, N_cert_Q - saldo_iniziale_anno - acquisti_cum_precedenti + riacquisti/cancellazioni)
```

Considerare:
- la **cancellazione automatica** il 1° novembre (Art. 24 §1 ▼M1): si sterilizzano i certificati acquistati nell'anno anteriore all'anno civile precedente (es. il 1/11/2028 si cancellano i certificati acquistati nel 2026 - regola di deroga Art. 24 §2 ▼M1 per il 1/11/2027 sui certificati acquistati per emissioni 2026);
- il **riacquisto eccedenza** richiedibile entro il **31 ottobre** di ogni anno di restituzione (Art. 23 §1 ▼M1), con limite pari ai certificati che il dichiarante doveva acquistare ex Art. 22 §2 nell'anno (Art. 23 §2 ▼M1);
- per il 2027 i certificati relativi al 2026 sono **riacquistabili solo nel 2027** (Art. 23 §2bis ▼M1).

### Passo 5 - Stima dell'esposizione in EUR

Per ciascun trimestre Q (anno 2027 in poi):

```
EUR_Q ~ acquisto_Q * prezzo_settimanale_medio_Q
```

dove `prezzo_settimanale_medio_Q` deriva da Art. 21 §1 ▼M1 (media chiusure ETS della settimana, calcolato dalla Commissione). Fornire un **range** (basso/centrale/alto) usando lo storico ETS 2024-2025 come riferimento e segnalare l'incertezza.

Per il 2026 (rilevante solo per restituzione annuale Art. 22 §1, prima volta 2027): usare la **media trimestrale** ETS del trimestre di importazione (Art. 21 §1bis ▼M1).

Aggiungere indicazione qualitativa sui **diritti** a carico del dichiarante per la copertura dei costi della piattaforma centrale (Art. 20 §5bis ▼M1, valore non ancora determinato - rinvio agli atti delegati).

### Passo 6 - Calendario operativo

Produrre un calendario con:

- **31 marzo, 30 giugno, 30 settembre, 31 dicembre** = fine trimestre Q1/Q2/Q3/Q4 (verifica saldo conto >= 50 % cumulato);
- **30 settembre dell'anno successivo** = scadenza di restituzione (Art. 22 §1 ▼M1);
- **31 ottobre dell'anno successivo** = ultima data per richiedere il riacquisto eccedenza (Art. 23 §1 ▼M1);
- **1° novembre** = cancellazione automatica certificati anteriori (Art. 24 §1 ▼M1).

Marcare il **1° febbraio 2027** come **prima data utile di acquisto** sulla piattaforma centrale comune (Art. 20 §1 ▼M1): tra 1/1/2027 e 1/2/2027 la piattaforma non e' ancora attiva; per il **Q1 2027** l'obbligo di detenzione e' al 31/3/2027, quindi l'acquisto puo' avvenire tra il 1/2/2027 e il 31/3/2027.

### Passo 7 - Margine di sicurezza

Indicare almeno tre fonti di incertezza:
- volatilita' del prezzo ETS settimanale (Art. 21 §1 ▼M1);
- aggiornamento dei **valori predefiniti** Allegato IV (atti di esecuzione Art. 7 §7 in evoluzione);
- **adeguamento Art. 31** in evoluzione (phase-out quote ETS free, vedi considerando 26-28 Reg. 2025/2083).

Raccomandare un margine prudenziale (es. +5/10 % sui certificati teorici) **lasciando la scelta numerica al professionista**.

## Output atteso

Report markdown contenente:

1. **Profilo del soggetto** (numero conto CBAM, anno di pianificazione, metodo Art. 22 §2 scelto).
2. **Tabella per trimestre Q1-Q4**: volumi attesi, emissioni cumulate, certificati richiesti (50 %), saldo iniziale, acquisto teorico, esposizione in EUR (range).
3. **Calendario operativo** con scadenze chiave (Art. 22 §1, §2, Art. 23 §1, Art. 24 §1).
4. **Box "Variabili che il professionista deve fissare"**: adeguamento Art. 31, detrazione carbon price Art. 9, range prezzi ETS, eventuale Art. 22 §2bis per superamento soglia in corso d'anno.
5. **Avvertenza standard** + rinvio a `references/fonti/reg-ue-2023-956-cbam-consolidato.md` per il riscontro testuale di Art. 22, 23, 24, 20, 21.
