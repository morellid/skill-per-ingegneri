# Output atteso - Carico dei tramezzi e riduzione del sovraccarico

## Tramezzi come carico distribuito g2 (§3.1.3)

Per gli edifici per abitazioni e uffici, il peso proprio dei **tramezzi interni** può essere ragguagliato
a un **carico permanente uniformemente distribuito g2**, in funzione del **peso proprio per unità di
lunghezza G2** della partizione, purché il solaio abbia adeguata capacità di ripartizione trasversale.

Con **G2 ≈ 1,5 kN/m** si ricade nella fascia **1,00 < G2 ≤ 2,00 kN/m** → **g2 = 0,80 kN/m²**. Questo valore
si somma agli altri carichi permanenti non strutturali (massetti, pavimenti, ecc.).

> Se un divisorio avesse **G2 > 5,00 kN/m** (es. una parete pesante), **non** si userebbe il carico
> equivalente: andrebbe considerato con il suo **effettivo posizionamento** sul solaio.

## Riduzione per area di influenza α_A (§3.1.4.1)

Per la categoria **A** (residenziale) e per una **trave** con **area di influenza A = 40 m²**, il
sovraccarico può essere ridotto con il coefficiente [3.1.1]:

**α_A = (5/7)·ψ0 + 10/A ≤ 1,0**

dove **ψ0** è il coefficiente di combinazione della **Tab. 2.5.I** (non riprodotta qui; per la categoria A
vale ψ0 = 0,7). Sostituendo A = 40 m²: **α_A = 0,714·ψ0 + 10/40 = 0,714·ψ0 + 0,25**. Il valore va poi
confrontato con il limite **≤ 1,0** (e, per le categorie **C e D**, non può essere **< 0,6**; per la A non
c'è il limite inferiore di 0,6). La skill fornisce la **formula e i vincoli**: il valore numerico di ψ0 e
il calcolo finale spettano al progettista.

## Riduzione per numero di piani α_n (§3.1.4.1)

Per il **pilastro** di un edificio con **più di 2 piani** (qui 5 piani) e categoria **A÷D**, la
sollecitazione dovuta ai sovraccarichi sulle membrature verticali può essere ridotta con [3.1.2]:

**α_n = (2 + (n − 2)·ψ0) / n**

con **n = numero di piani caricati** (n = 5): **α_n = (2 + 3·ψ0)/5**.

## Attenzione: non si combinano

I due coefficienti **α_A e α_n NON possono essere combinati** tra loro: si applica l'uno **oppure**
l'altro a seconda dell'elemento (orizzontale con area di influenza vs verticale multipiano).

## Nota

La skill inquadra il **carico equivalente dei divisori** e le **formule di riduzione** con i loro vincoli:
**non calcola** i valori numerici (che dipendono da ψ0, Tab. 2.5.I) **né dimensiona** gli elementi, compito
del progettista.
