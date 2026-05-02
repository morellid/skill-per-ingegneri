# Estratto: ANAC Linea Guida n. 2 - Metodologia valutazione OEPV

**Fonte**: ANAC Delibera n. 424 del 2 maggio 2018 - Linee guida n. 2 (aggiornamento)
**Titolo**: "Offerta economicamente piu' vantaggiosa"
**Vigenza normativa**: Le Linee Guida ANAC erano vincolanti sotto D.Lgs. 50/2016 (vecchio codice). Sotto D.Lgs. 36/2023 (nuovo codice), ANAC non ha ancora emesso una nuova linea guida equivalente; la LG n. 2 e' quindi **non piu' formalmente vincolante** ma e' ancora largamente citata come riferimento di prassi e dalla giurisprudenza TAR/CdS nelle procedure non ancora concluse.
**Nota**: nella prassi del settore, le formule e i metodi descritti nella LG n.2 sono ancora ampiamente applicati dai disciplinari di gara come standard di fatto.

---

## Metodo aggregativo-compensatore

La formula base del metodo aggregativo-compensatore e':

```
Pi = Sigma_j (Wj x V(aij))
```

Dove:
- `Pi` = punteggio totale dell'offerta i
- `Wj` = peso del criterio j (somma di tutti i Wj = 100)
- `V(aij)` = coefficiente (tra 0 e 1) assegnato all'offerta i per il criterio j

Il punteggio finale e' la somma dei prodotti peso x coefficiente per tutti i criteri.

---

## Metodi di attribuzione del coefficiente V(aij)

### Metodo tabellare (on/off)

Per criteri con requisiti certi e verificabili:
- Requisito soddisfatto: V = 1
- Requisito non soddisfatto: V = 0

Variante a scala discreta: il disciplinare definisce soglie (es. 0 - 0.25 - 0.50 - 0.75 - 1.00) corrispondenti a livelli del requisito.

### Metodo discrezionale (giudizio della commissione)

Per criteri qualitativi che richiedono valutazione tecnica:

**Procedura:**
1. Ogni commissario esamina l'offerta tecnica individualmente
2. Ciascun commissario assegna un coefficiente provvisorio tra 0 e 1 (o su scala 0-10 con normalizzazione)
3. I coefficienti individuali vengono rivelati simultaneamente (nessun commissario conosce la valutazione degli altri prima di comunicare la propria)
4. Si calcola la media aritmetica dei coefficienti individuali come coefficiente provvisorio dell'offerta
5. Si riproporziona: il coefficiente finale e' calcolato dividendo per il coefficiente massimo ottenuto tra tutte le offerte

**Formula di riproporzionamento:**
```
V(aij) = media_ij / max(media_ij per tutti gli offerenti j)
```

Il miglior offerente per quel criterio ottiene sempre V(aij) = 1; gli altri ottengono valori tra 0 e 1.

**Attenzione**: il riproporzionamento deve essere esplicitamente previsto nel disciplinare, altrimenti la sua applicazione da parte della commissione e' contestabile.

### Metodo con formula quantitativa

Per criteri misurabili numericamente (tempo, percentuale, quantita'):

**Parametro crescente** (piu' e' alto, meglio e'): es. numero di risorse aggiuntive, percentuale di riduzione emissioni
```
V(ai) = Ra_i / Ra_max
```
Dove Ra_max = valore massimo tra tutte le offerte.

**Parametro decrescente** (meno e' alto, meglio e'): es. tempo di consegna, numero di giorni
```
V(ai) = Ra_min / Ra_i
```
Dove Ra_min = valore minimo tra tutte le offerte.

**Parametro con soglia** (valore ottimale predefinito):
```
Se Ra_i <= Ra_soglia: V(ai) = Ra_i / Ra_soglia
Se Ra_i > Ra_soglia: V(ai) = Ra_soglia / Ra_i
```

---

## Formula per il punteggio dell'offerta economica

### Formula lineare (la piu' comune)

```
Pe_i = Vmax x (Prezzo_min / Prezzo_i)
```

Dove:
- `Vmax` = punteggio massimo assegnato al criterio economico
- `Prezzo_min` = prezzo piu' basso tra tutte le offerte ammesse
- `Prezzo_i` = prezzo offerto dall'operatore i

L'offerente con il prezzo piu' basso ottiene il punteggio massimo; gli altri ottengono punteggi proporzionalmente inferiori.

**Esempio**: Vmax = 30, offerte: A = 100.000 EUR, B = 85.000 EUR, C = 92.000 EUR
- Prezzo_min = 85.000 (offerente B)
- Pe_A = 30 x (85.000 / 100.000) = 25,5 punti
- Pe_B = 30 x (85.000 / 85.000) = 30,0 punti
- Pe_C = 30 x (85.000 / 92.000) = 27,7 punti

### Formula bilineare con soglia di anomalia (alternativa, rara)

```
Se Ri <= Ra: V(ai) = X x Ri / Ra
Se Ri > Ra: V(ai) = X + (1 - X) x (Ri - Ra) / (Rmax - Ra)
```

Dove Ra e' il ribasso soglia di anomalia, X e' un fattore prestabilito (es. 0.8). Questa formula e' complessa e puo' generare contestazioni; si sconsiglia salvo casi specifici motivati.

---

## Calcolo punteggio tecnico complessivo

Per ogni offerente, il punteggio tecnico e' la somma dei contributi di tutti i criteri tecnici:

```
PT_i = Sigma_j (Wj x V(aij))   per tutti i criteri tecnici j
```

Il punteggio totale e':

```
P_totale_i = PT_i + Pe_i
```

---

## Esempio numerico completo (3 offerenti, 3 criteri tecnici + economico)

**Matrice criteri:**

| Criterio | Peso | Metodo |
|----------|------|--------|
| A - Qualita' metodologia | 30 | Discrezionale |
| B - Esperienza team (anni) | 15 | Tabellare (< 5 anni: 0; 5-10: 0.5; > 10: 1) |
| C - Riduzione tempi (gg) | 25 | Formula decrescente |
| D - Prezzo | 30 | Formula lineare |
| **TOTALE** | **100** | |

**Dati offerenti:**

| Offerente | Coeff. A (media comm.) | Anni esperienza (B) | Riduzione tempi (C, gg) | Prezzo (D, EUR) |
|-----------|------------------------|--------------------|-----------------------|----------------|
| Alfa | 7,2 | 12 anni | 10 gg | 340.000 |
| Beta | 8,8 | 8 anni | 5 gg | 290.000 |
| Gamma | 6,0 | 15 anni | 15 gg | 360.000 |

**Calcolo criterio A (discrezionale con riproporzionamento):**
- Media Alfa = 7,2; Media Beta = 8,8; Media Gamma = 6,0
- Max = 8,8 (Beta)
- V(A_Alfa) = 7,2 / 8,8 = 0,818; PA_Alfa = 30 x 0,818 = 24,5
- V(A_Beta) = 8,8 / 8,8 = 1,000; PA_Beta = 30 x 1,000 = 30,0
- V(A_Gamma) = 6,0 / 8,8 = 0,682; PA_Gamma = 30 x 0,682 = 20,5

**Calcolo criterio B (tabellare, scala: <5->0; 5-10->0.5; >10->1):**
- Alfa: 12 anni -> V=1 -> PB_Alfa = 15 x 1 = 15,0
- Beta: 8 anni -> V=0.5 -> PB_Beta = 15 x 0.5 = 7,5
- Gamma: 15 anni -> V=1 -> PB_Gamma = 15 x 1 = 15,0

**Calcolo criterio C (formula decrescente V = Rmin/Ri):**
- Rmin = 5 gg (Beta)
- V(C_Alfa) = 5/10 = 0,500 -> PC_Alfa = 25 x 0,500 = 12,5
- V(C_Beta) = 5/5 = 1,000 -> PC_Beta = 25 x 1,000 = 25,0
- V(C_Gamma) = 5/15 = 0,333 -> PC_Gamma = 25 x 0,333 = 8,3

**Punteggio tecnico:**

| Offerente | PA | PB | PC | PT |
|-----------|----|----|----|-----|
| Alfa | 24,5 | 15,0 | 12,5 | **52,0** |
| Beta | 30,0 | 7,5 | 25,0 | **62,5** |
| Gamma | 20,5 | 15,0 | 8,3 | **43,8** |

**Calcolo criterio D (formula lineare Pe_i = 30 x Prezzomin/Prezzo_i):**
- Prezzomin = 290.000 (Beta)
- PE_Alfa = 30 x (290.000/340.000) = 25,6
- PE_Beta = 30 x (290.000/290.000) = 30,0
- PE_Gamma = 30 x (290.000/360.000) = 24,2

**Classifica finale:**

| Pos. | Offerente | PT | PE | Totale |
|------|-----------|----|----|--------|
| 1 | **Beta** | 62,5 | 30,0 | **92,5** |
| 2 | Alfa | 52,0 | 25,6 | 77,6 |
| 3 | Gamma | 43,8 | 24,2 | 68,0 |

---

## Principi di base del metodo

1. **Confronto relativo**: i punteggi sono calcolati rispetto alle offerte presentate, non in assoluto. Il cambiamento di un'offerta modifica i punteggi di tutte le altre (tramite riproporzionamento)
2. **Compensabilita'**: un offerente puo' compensare una debolezza su un criterio con la forza su un altro (entro i limiti del metodo aggregativo)
3. **Trasparenza**: tutti i calcoli devono essere riproducibili dagli offerenti sulla base delle informazioni nel disciplinare
4. **Parita' di trattamento**: stessa formula, stessi criteri per tutti gli offerenti
