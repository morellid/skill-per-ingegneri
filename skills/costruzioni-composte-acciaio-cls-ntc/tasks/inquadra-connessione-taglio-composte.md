# Task - Inquadra il sistema di connessione a taglio delle strutture composte (§4.3.4.3)

## Obiettivo

Inquadrare il **grado di connessione** e la **resistenza dei connettori a taglio** (pioli con testa) del
sistema di connessione acciaio-calcestruzzo, secondo le NTC 2018 §4.3.

## Input richiesti

- geometria del piolo (diametro d, altezza dopo la saldatura hsc) e materiale (ftk);
- classe del calcestruzzo della soletta (fck) e modulo Ecm;
- tipo di soletta (piena o con lamiera grecata, orientamento delle greche).

## Procedura (ancorata al testo)

1. **Grado di connessione** (§4.3.4.3). Determinare il **grado di connessione K = N/Nf** (N connettori
   presenti, Nf per il completo sviluppo del momento resistente plastico). Verificare che i connettori siano
   **duttili** (es. pioli con testa di altezza ≥ 4 diametri, diametro 16-25 mm) per ammettere una
   connessione parziale entro i limiti [4.3.7]-[4.3.8].

2. **Resistenza dei pioli con testa** (§4.3.4.3.1.2). La resistenza di progetto a taglio di un piolo (in
   soletta piena) è il **minore** fra:
   - **PRd,a = 0,8·ftk·(π·d²/4)/γV** [4.3.9] (rottura del piolo);
   - **PRd,c = 0,29·α·d²·√(fck·Ecm)/γV** [4.3.10] (rifollamento del calcestruzzo);
   con **γV = 1,25**, **ftk ≤ 500 MPa**, **d compreso tra 16 e 25 mm** e **α = 0,2·(hsc/d + 1)** per
   **3 ≤ hsc/d ≤ 4** [4.3.11a] o **α = 1,0** per **hsc/d > 4** [4.3.11b].

3. **Riduzione per lamiera grecata** (§4.3.4.3.1.2). Se la soletta è realizzata con **lamiera grecata**,
   ridurre la resistenza con: **kl = 0,6·b0·(hsc − hp)/hp² ≤ 1,0** [4.3.13] per greche **parallele**;
   **kt = 0,7·b0·(hsc − hp)/hp²/nr** [4.3.14] per greche **trasversali** (nr pioli per greca; solo se
   ftk < 450 MPa; kt non superiore ai limiti della Tab. 4.3.II).

4. **Dettagli e armatura trasversale** (§4.3.4.3.4-5). Rispettare la disposizione dei connettori e prevedere
   l'armatura trasversale per la trasmissione dello scorrimento.

## Output

Una nota che indichi: il **grado di connessione** K e il requisito di duttilità; la **resistenza di progetto
del piolo** come minore fra PRd,a e PRd,c (con γV, α, ftk ≤ 500 MPa, d 16-25 mm); l'eventuale **riduzione**
per lamiera grecata (kl/kt). **La skill inquadra le formule e i limiti; non calcola PRd né il numero di
connettori, e non dimensiona la connessione.**
