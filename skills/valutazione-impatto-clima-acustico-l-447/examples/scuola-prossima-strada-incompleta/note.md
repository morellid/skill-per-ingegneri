# Note sull'esempio "scuola prossima a strada di tipo C - clima acustico incompleto"

## Cosa illustra

- Caso classico di **valutazione di clima acustico carente** depositata
  insieme al PdC: privo di TCAA, privo di misure, privo di cartografia,
  privo di rinvio alla disciplina specifica delle infrastrutture
  stradali.
- Punto critico **DPR 142/2004**: per scuola/insediamento sensibile
  adiacente a strada di tipo C, il regime delle fasce di pertinenza
  prevale sui limiti generici di Tabella C del DPCM 14/11/1997
  (DPCM 14/11/1997 art. 3 c. 2). La skill non quota i valori del
  DPR 142/2004, ma deve segnalarne la rilevanza.
- Punto critico **firma TCAA**: il D.Lgs. 17 febbraio 2017 n. 42 art.
  21 ha riformato il sistema dell'elenco nazionale. La skill deve
  richiedere conferma della corretta iscrizione.
- Per traffico stradale, **T_M >= 1 settimana** (DM 16/3/1998 allegato C):
  un cenno alle "non sono state svolte misure" deve far scattare la
  segnalazione di un'omissione tecnica sostanziale.

## Cosa NON illustra

- Calcolo previsionale di Leq con modelli di propagazione del rumore
  stradale (NMPB, RLS, ecc.).
- Dimensionamento delle fasce A e B del DPR 142/2004.
- Caso in cui la scuola **non** ricada in fascia di pertinenza:
  qui non e' possibile concluderlo a priori; le dimensioni delle
  fasce per strada C extraurbana secondaria sono definite dal
  DPR 142/2004 (rinvio strutturale, fuori scope).
- Requisiti acustici passivi degli edifici (DPCM 5/12/1997): rinvio
  fuori scope.

## Cosa controllare nel run reale

- Che la skill **non quoti i valori di fascia DPR 142/2004**
  fabbricandoli, ma li rinvii al testo vigente.
- Che la skill identifichi la **firma TCAA mancante** come bloccante
  (la dichiarazione di compatibilita' senza firma di TCAA non e'
  valutazione ai sensi della L. 447/1995).
- Che la skill segnali **carenza di misure ante operam** come
  bloccante per insediamento sensibile esposto a infrastruttura di
  trasporto.
- Che i rinvii formali (LR Veneto, regolamento comunale Padova,
  Normattiva, DPR 142/2004) siano presenti nell'output finale.
