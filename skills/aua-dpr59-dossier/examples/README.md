# Esempi - aua-dpr59-dossier

## Struttura degli esempi

Ogni esempio contiene:

- `input.md`: descrizione del caso (dati forniti dall'utente).
- `expected-output.md`: output atteso dalla skill (report di
  autoverifica AUA).
- `note.md`: commenti di dominio per i validatori e riferimenti agli
  articoli del D.P.R. 59/2013 e norme richiamate.

## Elenco esempi

### Conformi

- **`conforme-pmi-metalmeccanica-scarichi-emissioni/`**: PMI media
  metalmeccanica (carpenteria) con scarichi industriali su pubblica
  fognatura, emissioni in atmosfera convogliate non riconducibili a
  Allegato I (autorizzazione ex art. 269 D.Lgs. 152/2006), comunicazione
  rifiuti art. 216, e impatto acustico. Non rientra in AIA, non e' VIA
  assorbente. Esito: AUA applicabile, 4 titoli incorporati, termine
  120 giorni con conferenza di servizi.

### Problematici

- **`problematico-impianto-aia-fuori-perimetro/`**: Impianto chimico
  rientrante nell'attivita' 4.1 dell'Allegato VIII Parte II del D.Lgs.
  152/2006 (impianti chimici di base superiori a soglia produttiva).
  L'AUA non si applica perche' l'impianto e' soggetto ad AIA ex
  Titolo III-bis Parte II D.Lgs. 152/2006. Esito: rinvio a procedura
  AIA, fuori scope AUA.
