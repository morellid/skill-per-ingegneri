# Esempi - dm37-2008-dichiarazione-conformita

## Struttura degli esempi

Ogni esempio contiene:
- `input.md`: descrizione del caso (dati DdC forniti dall'utente)
- `expected-output.md`: output atteso dalla skill (report di verifica)
- `note.md`: commenti di dominio per i validatori

## Elenco esempi

### Conformi

- **`conforme-elettrico-residenziale-piccolo/`**: DdC corretta per impianto elettrico appartamento 85 mq, 3 kW. Nessuna soglia Art. 5 superata. Relazione materiali specifica. Schema impianto presente. Norma CEI 64-8 citata. Esito: COMPLETA.

### Problematici

- **`problematico-progetto-mancante/`**: DdC incompleta per impianto elettrico ufficio 350 mq, 15 kW. Progetto obbligatorio (soglia 6 kW superata) ma non allegato. Formula dichiarativa generica. Relazione materiali inadeguata. Esito: INCOMPLETA - NON CONFORME.
