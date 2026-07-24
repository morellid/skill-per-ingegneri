# Task — Inquadra proprietà e profilo resistente del legno strutturale (NTC 2018 §11.7.1)

Supporto documentale per inquadrare, per un materiale/prodotto a base di legno per uso strutturale (NTC 2018, DM
17/1/2018, par. 11.7): le **generalità** e i casi di qualificazione (§11.7.1) e le **proprietà** con il **profilo
resistente** e il coefficiente **kh** (§11.7.1.1). **Non** esegue le verifiche di progetto.

Fonte: `../references/fonti/ntc2018-par-11-7.md`; checklist: `../references/estratti/legno-materiali-checklist.md`.

## Input tipico

- Tipo di legno/prodotto: **massiccio**, **lamellare incollato**, pannelli, ecc.
- Classe di resistenza (es. C24, GL24h) o profilo resistente dichiarato.
- Geometria dell'elemento: **altezza h** della sezione (per flessione) o lato maggiore (per trazione parallela).

## Passi

1. **Generalità e qualificazione (§11.7.1)**
   - Verifica che il prodotto sia **qualificato** secondo il **§11.1**: **caso A** (Marcatura CE, norma
     armonizzata), **caso B** (qualificazione §11.7.10), **caso C** (Linee Guida CSLP per prodotti innovativi).
   - Ricorda: sistema di **qualità** e **rintracciabilità**; il **Direttore dei Lavori** rifiuta le forniture non
     conformi ed effettua i **controlli di accettazione** (§11.7.10.2); prove presso **laboratori art. 59 DPR
     380/2001** o notificati (D.Lgs 106/2017 + Reg. UE 305/2011).

2. **Proprietà dei materiali (§11.7.1.1)**
   - I **valori caratteristici di resistenza** sono il **frattile 5%**, da prove di **durata 300 s** a **20 ± 2 °C**
     e **UR 65 ± 5%**; la massa volumica caratteristica è il frattile 5%.
   - Il **profilo resistente** (Tab. 11.7.I) deve comprendere almeno: resistenze **fm,k, ft,0,k, ft,90,k, fc,0,k,
     fc,90,k, fv,k**; moduli **E0,mean, E0,05, E90,mean, Gmean**; massa volumica **ρk** (ed eventualmente ρmean).

3. **Coefficiente kh (effetto dimensione) (§11.7.1.1)**
   - **Legno massiccio** (dimensione di riferimento **150 mm**), per h < 150 mm: incrementa fm,k e ft,0,k con
     **kh = min[(150/h)^0,2 ; 1,3]** [11.7.1].
   - **Legno lamellare incollato** (dimensione di riferimento **600 mm**), per h < 600 mm:
     **kh = min[(600/h)^0,1 ; 1,1]** [11.7.2].
   - h in mm = altezza dell'elemento inflesso o lato maggiore dell'elemento teso.

4. **Output**: scheda con caso di qualificazione applicabile, verifica della completezza del profilo resistente
   (Tab. 11.7.I) e valore di kh calcolato per l'elemento. Segnala che le **verifiche di progetto** restano fuori
   scope.

## Cosa NON fare

- Non calcolare le **resistenze di progetto** (fd = kmod·fk/γM) né eseguire le verifiche (§4.4).
- Non trattare adesivi (§11.7.7), collegamenti (§11.7.8), durabilità (§11.7.9); non trattare la sismica (§7.7) né
  l'accettazione di muratura/cls/acciaio (§§11.10/11.2/11.3): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-11-7.md`.
