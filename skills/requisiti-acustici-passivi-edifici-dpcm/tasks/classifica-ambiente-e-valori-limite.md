# Task: classifica-ambiente-e-valori-limite

Classifica l'**ambiente abitativo** nella categoria della **Tabella A** e individua i **valori limite** dei
requisiti acustici passivi della **Tabella B** secondo il **DPCM 5 dicembre 1997**. Supporto documentale: **non**
esegue misure/calcoli né il collaudo.

## Quando usarla

Il progettista/tecnico deve stabilire quali valori limite di isolamento e rumore si applicano a un edificio in
base alla sua destinazione d'uso. Per le grandezze/indici e i limiti degli impianti usa
`inquadra-grandezze-e-rumore-impianti`.

## Passi

1. **Classifica l'ambiente** (Tab. A, art. 2): individua la categoria in base alla destinazione d'uso:
   - **A** residenza o assimilabili;
   - **B** uffici e assimilabili;
   - **C** alberghi, pensioni e attività assimilabili;
   - **D** ospedali, cliniche, case di cura e assimilabili;
   - **E** attività scolastiche a tutti i livelli e assimilabili;
   - **F** attività ricreative o di culto o assimilabili;
   - **G** attività commerciali o assimilabili.
2. **Individua i valori limite** (Tab. B) per la categoria — R'w / D2m,nT,w / L'n,w / LASmax / LAeq:
   - **D**: 55 / 45 / 58 / 35 / 25;
   - **A, C**: 50 / 40 / 63 / 35 / 35;
   - **E**: 50 / 48 / 58 / 35 / 25;
   - **B, F, G**: 50 / 42 / 55 / 35 / 35.
3. **Interpreta il verso della verifica**: **R'w** (isolamento tra partizioni) e **D2m,nT,w** (isolamento di
   facciata) sono valori **minimi** (in opera **≥** limite); **L'n,w** (calpestio), **LASmax** e **LAeq** (rumore
   impianti) sono valori **massimi** (in opera **≤** limite).
4. **Nota su R'w** (Tab. B, nota *): i valori di R'w sono riferiti a elementi di separazione tra **due distinte
   unità immobiliari**.
5. **Nota edilizia scolastica** (Tab. B): per il **tempo di riverberazione** degli edifici scolastici si applica la
   circolare MLLPP n. 3150 del 22/5/1967 (fuori dal dettaglio di questa skill).

Usa la checklist in `../references/estratti/requisiti-acustici-passivi-checklist.md` (sezione 3).

## Output atteso

Un inquadramento che indichi la **categoria** dell'ambiente (Tab. A) e i **valori limite** applicabili (Tab. B,
R'w/D2m,nT,w/L'n,w/LASmax/LAeq) con il **verso della verifica** (minimi per gli isolamenti, massimi per i rumori),
con **rinvio all'articolo/tabella** del DPCM. Nessuna misura né calcolo.

## Cosa NON fare

- Non **eseguire** misure o calcoli degli indici né il **collaudo** in opera (compete al tecnico competente in
  acustica, L. 447/1995).
- Non applicare valori di altre norme (es. classificazione UNI 11367) al posto della Tab. B del DPCM.
