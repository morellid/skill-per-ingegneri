# Note - Importatore alluminio sotto soglia, conforme

## Scopo dell'esempio

Mostrare il caso tipico di una PMI italiana che:

- importa alluminio CBAM da paesi terzi (Turchia, Marocco) e da Norvegia (origine territori Allegato III pt. 1, esclusa);
- e' **sotto soglia** Art. 2bis ma con margine stretto e con prospettiva di superarla in corso d'anno;
- ha gia' fatto la cosa giusta: presentazione della domanda di autorizzazione **entro il 31/3/2026** (deroga transitoria Art. 17 §7bis ▼M1) -> puo' usare il codice TARIC **Y238** fino alla decisione.

Si esercita la sotto-attivita' `tasks/check-qualifica-e-deroghe.md` con:

- mappatura codici TARIC riga per riga (Y134 / Y238 / Y128) - vedi tabella decisionale nell'output;
- conferma dell'applicabilita' dell'AEO (Art. 5 §5 lettera g bis ▼M1) e assenza di garanzia (Art. 17 §5 ▼M1);
- rinvio al task `plan-equilibrio-trimestrale.md` per il 2027.

## Cosa l'esempio NON copre

- Calcolo dei certificati per la dichiarazione annuale 2026 (rinviato al 2027, fuori scope di questo esempio).
- Strategia di sostituzione fornitori per restare sotto soglia.
- Documentazione Art. 9 (carbon price paese terzo) - non e' fornita nell'input.

## Verifiche operate dalla skill

- Coerenza tra codice TARIC e fattispecie applicabile.
- Coerenza tra Art. 5 §1ter ▼M1 e prospettiva di superamento (domanda presentata prima del superamento).
- Calendario della deroga Art. 17 §7bis (27/9/2026 ultima data).
- Identificazione della cd. "lista importatori > 90 % soglia" (Art. 25bis ▼M1).
