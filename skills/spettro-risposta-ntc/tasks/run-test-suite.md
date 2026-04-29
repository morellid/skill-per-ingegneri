# Task: esecuzione test suite del modulo di calcolo

## Obiettivo

Eseguire la test suite Python che verifica:
1. Le formule chiuse di NTC par. 3.2.3 (TR<->P_VR, eta, SS clamping, periodi caratteristici).
2. La continuita' di Se(T) ai raccordi TB, TC, TD.
3. L'interpolazione logaritmica sui 9 TR di riferimento (round-trip e bracket).
4. I valori canonici (VN=50 CU II -> TR_SLV ~ 475 anni).
5. Il rifiuto esplicito di S1/S2 e di TR fuori reticolo.

## Quando usare questo task

- "Verifico che il modulo dia ancora i valori attesi dopo una modifica"
- "Eseguo la regression suite prima di un release"
- "Voglio capire quali casi sono coperti dai test"

## Procedura

In Claude Code, dalla skill installata (qualunque sia la CWD):

```bash
cd ${CLAUDE_SKILL_DIR}/tasks/lib && python3 -m unittest test_spettro -v
```

Oppure direttamente:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/test_spettro.py -v
```

In Codex / altri agent compatibili AGENTS.md, sostituisci `${CLAUDE_SKILL_DIR}` con il path assoluto della directory che contiene il `SKILL.md` di questa skill (es. `~/.agents/skills/spettro-risposta-ntc/`).

## Output atteso

44 test, tutti pass. Le classi di test e cosa coprono:

| Classe                       | # | Cosa copre                                                                  |
|------------------------------|---|-----------------------------------------------------------------------------|
| `TestVitaTR`                 | 3 | V_R = V_N * C_U + clamp 35 anni; TR = -V_R/ln(1-P_VR); valori canonici      |
| `TestCoeffSottosuolo`        | 5 | SS cat. A/B/C clamping; CC formule; rifiuto S1/S2 e categorie invalide      |
| `TestEta`                    | 2 | eta(5%) = 1; clamp minimo 0.55                                              |
| `TestPeriodi`                | 1 | TB = TC/3; TC = CC*Tc*; TD = 4*ag/g + 1.6                                   |
| `TestInterpolazione`         | 3 | Round-trip sui nodi; bracket log-log; rifiuto fuori reticolo                |
| `TestRaccordiSeT`            | 5 | Continuita' Se(T) ai raccordi TB/TC/TD; T=0; T grande                       |
| `TestPipelineEndToEnd`       | 1 | Pipeline `calcola_parametri` con dataset realistico (TR ~ 475)              |
| `TestIO`                     | 2 | Carica JSON; rifiuta lunghezza errata                                       |
| `TestValidazioneInput`       | 7 | Hardening: zero/negativo/NaN/inf/stringa/bool/None-da-JSON                  |
| `TestCoperturaCategorie`     | 4 | Cat. sottosuolo D, E; topografiche T2/T3/T4; smorzamento xi != 5%           |
| `TestEsempioConforme`        | 2 | Anti-drift end-to-end: input.json + expected.json letti dalle examples/     |
| `TestCLI`                    | 9 | CLI: --input-json equivalente a flag scalari; error handling chiavi mancanti (sito, parametri_calcolo), stato_limite invalido, classe d'uso lowercase, file --tr-riferimento incompleto |

Esempio output:

```
Ran 44 tests in 0.00x s
OK
```

Se anche un solo test fallisce: NON usare la skill in produzione, segnala il fail come issue al maintainer. In particolare, un fail di `TestEsempioConforme.test_match_expected_json` indica drift fra `input.json`/`expected.json` (in `examples/caso-conforme-fittizio-cu2-c-t1/`) e l'output del modulo: rigenera il fixture o investiga l'eventuale regressione del modulo.

## Casi di confronto vs CSLP (validazione di campo)

I test interni qui descritti coprono la consistenza delle formule. La validazione "di campo" (Livello 2 di [`methodology/validazione.md`](../../../methodology/validazione.md)) richiede confronto numerico vs foglio Excel CSLP su almeno 10 casi reali.

Procedura per il validatore:
1. Scegli un sito reale (lat, lon).
2. Estrai dal foglio CSLP i parametri ag, F0, Tc* per i 9 TR di riferimento al sito.
3. Estrai dal foglio CSLP i valori TR, ag, F0, Tc*, S, eta, TB, TC, TD per ciascuno SL e per categoria sottosuolo/topografica scelta.
4. Esegui il modulo Python con gli stessi input.
5. Confronta tutti i parametri con tolleranza:
   - TR: tolleranza 0.5 anni
   - ag: tolleranza 0.0005 g
   - F0: tolleranza 0.01
   - Tc*: tolleranza 0.005 s
   - SS, S, CC, eta, TB, TC, TD: tolleranza 0.001 (relativa)
6. Documenta caso e risultato in un nuovo `examples/caso-<nome>/`.

Discrepanze entro tolleranza sono attese (interpolazione finita); discrepanze maggiori sono bug.
