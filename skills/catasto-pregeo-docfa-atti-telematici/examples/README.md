# Esempi

Casi di uso della skill `catasto-pregeo-docfa-atti-telematici`. Ogni esempio contiene:

- `input.md` - dati e contesto forniti dall'utente
- `expected-output.md` - output strutturato che la skill dovrebbe produrre (checklist, scelta tipologia, dichiarazioni, ecc.)
- `note.md` - commenti di dominio, fonti applicate, perche' l'esempio e' rappresentativo

## Esempi disponibili

- [`conforme-tm-villetta-piu-docfa/`](conforme-tm-villetta-piu-docfa/) - workflow completo conforme: nuova villetta unifamiliare con autorimessa, Tipo Mappale Pregeo + Docfa di accatastamento (causale Nuova Costruzione, A/7 + C/6).
- [`non-conforme-frazionamento-deposito-comunale/`](non-conforme-frazionamento-deposito-comunale/) - caso problematico: Tipo di Frazionamento (FR) trasmesso telematicamente dopo il 1/7/2025 con deposito comunale duplicato a cura del professionista. Errori e correzioni.

## Limiti

Questi esempi non sono test automatizzati: sono casi narrativi di riferimento per la validazione di dominio (Livello 2). Una batteria di test case sara' raccolta a valle del primo ciclo di feedback con un geometra/ingegnere edile validatore.
