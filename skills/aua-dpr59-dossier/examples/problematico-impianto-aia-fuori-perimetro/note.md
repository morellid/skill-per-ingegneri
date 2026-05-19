# Note di dominio - esempio problematico

## Punto chiave del caso

Caso "trabocchetto" in cui l'utente potrebbe essere tentato di usare
l'AUA perche' percepisce un dossier modesto (modifiche a emissioni e
scarichi). Il triage corretto e' invece: l'impianto rientra in AIA,
quindi e' **fuori perimetro AUA**, indipendentemente dalla dimensione
PMI dell'impresa. La skill deve riconoscere immediatamente l'esclusione
e indirizzare al regime AIA, non al regime AUA.

## Riferimenti normativi attivati (esclusione)

- **art. 1 co. 1 D.P.R. 59/2013**: "impianti non soggetti ad AIA"
  -> esclusione esplicita degli impianti AIA dal perimetro AUA.
- **Allegato VIII Parte II D.Lgs. 152/2006, voce 4.1**: impianti
  chimici per la produzione su scala industriale di prodotti chimici
  organici di base mediante trasformazione chimica.

## Norme collegate per la strada corretta

- D.Lgs. 152/2006, Titolo III-bis Parte II (disciplina AIA, artt.
  29-bis a 29-quattuordecies).
- D.Lgs. 152/2006 art. 5 co. 1 lett. l-bis: definizione di modifica
  sostanziale ai fini AIA (diversa da quella AUA ex art. 6 D.P.R.
  59/2013).
- D.Lgs. 152/2006 art. 29-nonies: comunicazione modifiche AIA.
- D.Lgs. 152/2006 art. 29-octies: riesame AIA.

## Insidie comuni che la skill deve evitare

1. **Confondere PMI e ambito AUA**: il dimensionamento "non PMI" non
   chiude da solo la verifica - l'AUA si applica anche alle imprese
   non-PMI purche' l'impianto sia non-AIA. Qui pero' l'impianto **e'**
   AIA, quindi il ragionamento non puo' partire dalla dimensione.
2. **Confondere modifica AIA e modifica AUA**: l'art. 6 D.P.R. 59/2013
   regola le modifiche dell'AUA in essere. Per impianti AIA si applica
   la disciplina degli artt. 29-nonies e 29-octies D.Lgs. 152/2006.
3. **Provare a usare AUA per "qualche pezzo" non AIA**: l'esclusione e'
   per impianto, non per singolo titolo. Un impianto AIA non puo' avere
   in parallelo un'AUA per alcune emissioni: tutti i suoi titoli
   ambientali rientrano nell'AIA unica.
4. **Confondere AIA in vigore con scadenza prossima**: l'AIA in
   scadenza si rinnova, non si converte in AUA.

## Cosa la skill deve fare correttamente

1. Riconoscere immediatamente l'esclusione AUA ex art. 1 co. 1 quando
   l'impianto e' AIA.
2. Spiegare che la "non PMI" da sola non chiuderebbe la verifica, ma
   la classificazione AIA si'.
3. Rinviare a strumento dedicato AIA (la skill non lo e').
4. Spiegare che le definizioni di "modifica sostanziale" AIA e AUA non
   sono interscambiabili.
5. Restituire un report breve, esplicito sull'esclusione: l'utente non
   deve essere indirizzato a un percorso AUA inutile.

## Cosa la skill NON deve fare

- Non deve produrre un mapping completo dei titoli incorporabili: il
  caso e' chiuso al passaggio "AIA si'".
- Non deve calcolare termini AUA: non sono applicabili.
- Non deve interpretare le voci dell'Allegato VIII Parte II per
  l'utente: la voce 4.1 e' gia' nota al consulente e l'AIA e' in
  essere.

## Stato di validazione

- Validato dall'autore (Livello 1 - autovalidazione 2026-05-19).
- Validazione Livello 2 (ingegnere ambientale di dominio terzo):
  pendente.
- Validazione Livello 3 (consulente AIA con esperienza Regione):
  pendente.
