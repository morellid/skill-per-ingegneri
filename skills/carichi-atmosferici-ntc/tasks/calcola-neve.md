# Calcola carico neve sulla copertura (NTC 2018 par. 3.4)

## Obiettivo

Calcolare il carico neve `q_s` sulla copertura, ai sensi di NTC 2018 par. 3.4, usando il modulo code-driven `tasks/lib/carichi_atmosferici.py` sotto-comando `neve`.

## Input richiesti

Chiedi o ricava dall'utente:

| Campo                | Tipo    | Note                                                                                            |
|----------------------|---------|-------------------------------------------------------------------------------------------------|
| `zona`               | stringa | `I-Alpina`, `I-Mediterranea`, `II`, `III` - da NTC par. 3.4.2 in funzione del Comune del sito  |
| `a_s`                | numero  | altitudine del sito (m s.l.m.); deve essere `>= 0`                                              |
| `alpha_deg`          | numero  | inclinazione delle falde (gradi); range valido `[0, 90]`                                        |
| `classe_esposizione` | stringa | `battuta_dai_venti`, `normale` (default), `riparata` - da NTC Tab. 3.4.I                        |
| `c_t`                | numero  | coefficiente termico (default 1.0); != 1 solo a fronte di studio termico specifico              |

**Importante**: la skill incorpora le 4 zone neve e le formule di NTC par. 3.4.2. Verifica che la zona sia tra quelle previste; per Comuni in fascia di confine tra zone, chiedi conferma o suggerisci di consultare la copia ufficiale di NTC.

## Schema JSON di input

```json
{
  "zona": "II",
  "a_s": 350.0,
  "alpha_deg": 25.0,
  "classe_esposizione": "normale",
  "c_t": 1.0
}
```

## Procedura

1. Acquisisci i campi sopra dall'utente. Se mancano, chiedi.
2. Salva il JSON in un file temporaneo.
3. Invoca il modulo:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/carichi_atmosferici.py neve --input-json /path/al/file.json
```

(in Codex / altri agent sostituisci `${CLAUDE_SKILL_DIR}` con il path assoluto della skill.)

4. Se il modulo solleva errore (zona invalida, `a_s < 0`, `alpha` fuori `[0, 90]`, classe non riconosciuta), riporta il messaggio bloccante e chiedi correzione all'utente. NON aggirare l'errore.
5. Riporta l'output del modulo nella forma:

```
Input
- Zona neve: ...                        [NTC par. 3.4.2]
- Altitudine sito a_s = ... m
- Inclinazione falde alpha = ... deg
- Classe esposizione c_E: ...           [NTC Tab. 3.4.I]
- c_t = ...                             [NTC par. 3.4.4, default 1.0]

Valori intermedi
- q_sk = ... kN/m^2                     [NTC par. 3.4.2 zona ..., a_s = ...]
- mu_1 = ...                             [NTC par. 3.4.5.2.1, alpha = ...]
- c_E = ...                              [NTC Tab. 3.4.I]

Output
- q_s = ... kN/m^2                       [eq. 3.4.1 NTC]
```

6. Concludi con:

> L'output e' un valore caratteristico ai sensi di NTC par. 3.4. La combinazione SLU/SLE va eseguita a valle (vedi skill `combinazioni-carico-ntc`). Il calcolo copre solo coperture ad una/due falde regolari (par. 3.4.5.2.1, mu_1). Per accumuli, deriva, scorrimento, sporgenze (par. 3.4.5.5) o coperture multiple il progettista deve eseguire calcolo separato. Il valore e' verificato dal progettista strutturale firmatario.

## Casi particolari

- **alpha >= 60 deg**: la skill restituisce `mu_1 = 0` e `q_s = 0` (NTC par. 3.4.5.2.1). Comunicalo esplicitamente: e' comportamento corretto, non un errore.
- **a_s = 0** (mare): la skill applica la formula del primo tratto (`a_s <= 200 m`), e.g. zona III -> `q_sk = 0.60 kN/m^2`. Output corretto.
- **Zona di confine tra Comuni**: chiedi all'utente di confermare la zona dopo lookup ufficiale (per esempio in caso di Comune al limite tra zona II e III), non assegnare automaticamente.
- **c_t < 1**: chiedi all'utente se ha eseguito studio termico specifico (par. 3.4.4 NTC); se no, sconsiglia e usa `c_t = 1`.

## Limiti del task

Vedi `SKILL.md` sezione "Limiti". In particolare la skill non copre `mu_2` ne `mu_3` (carichi accidentali a deriva, accumulo, sporgenze): per coperture non ordinarie il progettista deve eseguire il calcolo separato seguendo NTC par. 3.4.5.5 e Circolare C3.4.
