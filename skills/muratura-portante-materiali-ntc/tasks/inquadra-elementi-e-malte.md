# Task — Inquadra elementi e malte per muratura portante (NTC 2018 §11.10.1-11.10.2)

Supporto documentale per inquadrare, per una muratura portante (NTC 2018, DM 17/1/2018, par. 11.10): gli
**elementi** e le categorie I/II con le relative **prove di accettazione** (§11.10.1) e le **malte** (classi, tipi,
prove) (§11.10.2). **Non** esegue le verifiche di progetto.

Fonte: `../references/fonti/ntc2018-par-11-10.md`; checklist: `../references/estratti/muratura-materiali-checklist.md`.

## Input tipico

- Elementi previsti: tipo (laterizio, silicato di calcio, calcestruzzo, pietra…), **categoria dichiarata (I/II)**,
  resistenza dichiarata (media fbm o caratteristica fbk), volume di fornitura.
- Malta prevista: **classe** (M…), tipo (a prestazione garantita / a composizione prescritta / prodotta in cantiere).

## Passi

1. **Elementi e categoria (§11.10.1)**
   - Verifica che gli elementi siano conformi alla **UNI EN 771** e rechino la **Marcatura CE**. Individua il
     sistema VVCP (Tab. 11.10.I): **Categoria I → 2+**, **Categoria II → 4**.
   - Ricorda: **Categoria I** = resistenza dichiarata con **probabilità di insuccesso ≤ 5%**; **Categoria II** non
     soddisfa il requisito. Il **coefficiente γM** dipende dalla categoria (§4.5.6).

2. **Prove di accettazione degli elementi (§11.10.1.1)**
   - Prove **obbligatorie** per la muratura portante, presso **laboratorio art. 59 DPR 380/2001**, a cura del
     **Direttore dei Lavori**.
   - Se dichiarata la **resistenza media fbm**: **1 campione ogni 350 m³** (Cat. II) / **650 m³** (Cat. I);
     **n elementi (n ≥ 6)**; esito positivo se **media ≥ fbm** [11.10.1] **e** **f1 ≥ 0,80·fbm** [11.10.2].
   - Se dichiarata la **sola resistenza caratteristica fbk**: su 6 elementi, positivo se **f1 ≥ fbk**.

3. **Malte (§11.10.2)**
   - Classe **M** + numero = **fm in N/mm²** (Tab. 11.10.II: M2,5/M5/M10/M15/M20/Md). **Per la muratura portante
     non sono ammesse malte con fm < 2,5 N/mm².**
   - Tipo: **a prestazione garantita** (UNI EN 998-2, CE sistema 2+); **a composizione prescritta** (sistema 4;
     per le composizioni in volume vale la **Tab. 11.10.V**); **prodotta in cantiere** (secondo progetto).
   - **Prove di accettazione**: ≥ **3 provini 40×40×160 mm ogni 350 m³** (composizione prescritta/cantiere) o
     **ogni 700 m³** (prestazione garantita); media ≥ valore di progetto.

4. **Output**: scheda con categoria/sistema VVCP degli elementi, criteri di accettazione applicabili (in funzione
   di fbm/fbk e categoria) e classe/tipo di malta con le relative prove. Segnala che le **verifiche di progetto**
   restano fuori scope.

## Cosa NON fare

- Non eseguire le **verifiche di progetto** né calcolare le **resistenze di progetto** (fd = fk/γM).
- Non trattare il progetto (§4.5), la sismica (§7.8) né l'accettazione di **cls/acciaio** (§§11.2/11.3): rinvia
  alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-11-10.md`.
