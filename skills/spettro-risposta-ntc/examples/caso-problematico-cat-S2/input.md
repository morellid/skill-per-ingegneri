# Input - caso problematico (categoria di sottosuolo S2)

## Dati committente

Edificio residenziale su area golenale con depositi di terreni saturi suscettibili di liquefazione. La relazione geologica ha classificato il sottosuolo come **categoria S2** ai sensi NTC 2018 par. 3.2.2.

## Parametri di calcolo (tentativo)

| Parametro                    | Valore   |
|------------------------------|----------|
| Vita nominale V_N            | 50 anni  |
| Classe d'uso                 | II       |
| **Categoria di sottosuolo**  | **S2**   |
| Categoria topografica        | T1       |
| Stati limite richiesti       | SLV      |

## Parametri di pericolosita' al sito

Identici a quelli del caso conforme (`caso-conforme-fittizio-cu2-c-t1/input.json`, oggetto `parametri_pericolosita_sito`). Sono irrilevanti: il calcolo si rifiuta prima di leggerli.

## Comando di riproduzione

Estrai i parametri di pericolosita' dal caso conforme (con jq oppure copia manuale) e prova a invocare il modulo con `--cat-sottosuolo S2`:

```bash
jq '.parametri_pericolosita_sito' \
   ${CLAUDE_SKILL_DIR}/examples/caso-conforme-fittizio-cu2-c-t1/input.json \
   > /tmp/params-fittizio.json

python3 ${CLAUDE_SKILL_DIR}/tasks/lib/spettro.py \
    --tr-riferimento /tmp/params-fittizio.json \
    --vn 50 --classe-uso II \
    --cat-sottosuolo S2 --cat-topografica T1 \
    --stato-limite SLV
```

Output atteso: `ValueError` esplicito + exit code != 0 (vedi `expected-output.md`).
