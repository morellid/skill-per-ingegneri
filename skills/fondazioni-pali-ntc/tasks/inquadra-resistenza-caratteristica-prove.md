# Task - Inquadra la resistenza caratteristica, i controlli d'integrità e le prove di carico (§6.4.3.1.1, 6.4.3.6, 6.4.3.7)

## Obiettivo

Inquadrare come si determina la **resistenza caratteristica R_k** dei pali (fattori di correlazione ξ) e
gli obblighi di **controlli d'integrità** e **prove di carico** (NTC 2018 §6.4.3.1.1, 6.4.3.6, 6.4.3.7).

## Input richiesti

- metodo di determinazione della resistenza: **prove di carico statico** su pali pilota, **metodi
  analitici / prove in sito**, o **prove dinamiche**;
- numero di **prove** o di **verticali di indagine** disponibili;
- numero e **diametro** dei pali (piccolo/medio d < 80 cm, grande d ≥ 80 cm).

## Procedura (ancorata al testo)

1. **Resistenza caratteristica R_k** (§6.4.3.1.1). R_k è il **minore** tra i valori ottenuti applicando ai
   valori **medio** e **minimo** delle resistenze i **fattori di correlazione ξ**, in funzione:
   - **prove di carico statico** su pali pilota → **Tab. 6.4.III** (ξ1/ξ2, per numero di prove: da 1,40 a
     1,0 per ≥5 prove);
   - **metodi analitici / prove in sito** → **Tab. 6.4.IV** (ξ3/ξ4, per numero di **verticali indagate**:
     da 1,70 a 1,40 (ξ3) e 1,21 (ξ4) per ≥10 verticali). Si contano solo le verticali spinte oltre la
     lunghezza dei pali;
   - **prove dinamiche** ad alto livello di deformazione su pali pilota → **Tab. 6.4.V** (ξ5/ξ6).

   Poi **R_d = R_k / γR** (Tab. 6.4.II) e, per i carichi trasversali, γT = 1,3 (Tab. 6.4.VI).

2. **Controlli d'integrità** (§6.4.3.6). Quando la qualità dipende dai procedimenti esecutivi e dai
   terreni, controlli (prove dirette/indirette) su almeno il **5% dei pali**, **minimo 2**; per gruppi di
   pali di **grande diametro (d ≥ 80 cm)** con **≤ 4 pali**, su **tutti** i pali del gruppo.

3. **Prove di carico di progetto** (§6.4.3.7.1). Su **pali pilota** identici a quelli da realizzare; carico
   di prova **≥ 2,5× l'azione di progetto SLE**; resistenza assunta al cedimento della testa pari al **10%
   del diametro** (d < 80 cm) o **≥ 5%** (d ≥ 80 cm). Ammesse prove dinamiche adeguatamente interpretate.

4. **Prove in corso d'opera** (§6.4.3.7.2). Prove statiche a **1,5× l'azione SLE** (o **1,2×** se i pali
   sono strumentati). Numero minimo per sistema di fondazione: **1** (≤20 pali), **2** (21-50), **3**
   (51-100), **4** (101-200), **5** (201-500), **~5+n/500** (n>500). Le statiche possono ridursi con prove
   dinamiche sostitutive e controlli non distruttivi sul ≥50% dei pali, ma **almeno una prova statica**.

## Output

Una nota che indichi: la tabella di correlazione ξ pertinente al metodo scelto e il conteggio di prove/
verticali; il numero minimo di **controlli d'integrità** e di **prove di carico** (di progetto e in corso
d'opera) e i relativi livelli di carico. **La skill inquadra le regole; non calcola R_k/R_d, non
interpreta le prove né dimensiona i pali.**
