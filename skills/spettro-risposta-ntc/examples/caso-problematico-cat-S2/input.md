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

Stesso file JSON dell'esempio conforme (`caso-conforme-fittizio-cu2-c-t1/input.md`).

## Comando

```bash
python3 tasks/lib/spettro.py \
    --tr-riferimento /tmp/params-fittizio.json \
    --vn 50 --classe-uso II \
    --cat-sottosuolo S2 --cat-topografica T1 \
    --stato-limite SLV
```
