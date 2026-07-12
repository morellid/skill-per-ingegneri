# periodo-proprio-t1-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1)

Skill code-driven per la **stima preliminare del periodo del modo di vibrare principale T1** ai sensi delle **NTC 2018 par. 7.3.3.2** e della **Circolare 7/2019 par. C7.3.3.2**.

Due formule, con gerarchia dichiarata dalla Circolare:

- **[7.3.6] NTC 2018**: `T1 = 2*sqrt(d)` - d = spostamento laterale elastico del punto piu' alto dell'edificio [m] sotto la combinazione [2.5.7] applicata in orizzontale (richiede un modello; e' la stima "piu' affidabile" secondo la Circolare);
- **[C7.3.2] Circ. 7/2019**: `T1 = C1*H^(3/4)` - prima approssimazione da altezza H [m] e tipologia (C1 = 0,085 telaio acciaio/legno; 0,075 telaio c.a.; 0,050 muratura o altro).

In piu', se TC e' fornito: check `T1 <= 2,5*TC` per l'analisi lineare statica e coefficiente `lambda` (0,85/1,0) per le forze [7.3.7].

## Target

Ingegneri strutturisti in fase di inquadramento preliminare / screening dell'analisi lineare statica.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `stima-periodo-t1` | Stima T1 con [7.3.6] o [C7.3.2], check dei limiti (H <= 40 m, massa uniforme), condizione 2,5*TC e lambda |

Calcolo deterministico con `tasks/lib/periodo_t1.py` (22 test in `tasks/lib/test_periodo_t1.py`):

```bash
python3 tasks/lib/periodo_t1.py --metodo circolare --h 16 --tipologia telaio-ca \
  --tc 0.4 --orizzontamenti 5 --massa-uniforme si
```

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/periodo-proprio-t1-ntc" "$HOME/.claude/skills/periodo-proprio-t1-ntc"

# OpenAI Codex
ln -sfn "$(pwd)/skills/periodo-proprio-t1-ntc" "$HOME/.agents/skills/periodo-proprio-t1-ntc"
```

## Fonti consultate

- **DM 17 gennaio 2018 (NTC 2018)** - GU n. 42 del 20/02/2018 S.O. n. 8 - par. 7.3.3.2 e 2.5.3
- **Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.** - GU n. 35 dell'11/02/2019 S.O. n. 5 - par. C7.3.3.2

Dettaglio (URL, SHA256, trascrizioni) in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

Non esegue analisi modale, non calcola d, non calcola TC/TD/Sd(T1) (vedere `spettro-risposta-ntc`), non valuta la regolarita' in altezza, non copre edifici esistenti/ponti. **La stima e' preliminare: non sostituisce l'analisi modale ne' il giudizio del progettista firmatario.**

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
