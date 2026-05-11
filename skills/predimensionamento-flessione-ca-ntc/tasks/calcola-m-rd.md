# Calcola M_Rd sezione c.a. flessione semplice SLU (NTC 2018 par. 4.1.2)

## Obiettivo

Calcolare il momento resistente `M_Rd` di una sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU, ai sensi di NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2, usando il modulo code-driven `tasks/lib/flessione_ca.py`.

## Input richiesti

Chiedi o ricava dall'utente:

| Campo      | Tipo   | Unita' | Note                                                                                |
|------------|--------|--------|-------------------------------------------------------------------------------------|
| `b`        | numero | mm     | larghezza sezione                                                                   |
| `h`        | numero | mm     | altezza totale sezione                                                              |
| `d`        | numero | mm     | altezza utile (dal lembo compresso al baricentro armatura tesa); deve essere `< h`  |
| `As`       | numero | mm^2   | area armatura tesa; l'utente la calcola da numero/diametro barre                    |
| `fck`      | numero | MPa    | resistenza caratteristica calcestruzzo; deve essere `<= 50` (Classe 1)              |
| `fyk`      | numero | MPa    | tensione caratteristica snervamento acciaio (B450C: 450)                            |
| `alpha_cc` | numero | -      | default 0.85 (carichi lunga durata); 1.0 per carichi di breve durata se motivato    |
| `gamma_c`  | numero | -      | default 1.5 (PERS); 1.0 per combinazioni eccezionali se motivato                    |
| `gamma_s`  | numero | -      | default 1.15                                                                        |
| `Es`       | numero | MPa    | default 200000                                                                      |
| `eps_cu`   | numero | -      | default 0.0035 (Classe 1)                                                           |

**Importante**: la skill **non calcola** `d` da copriferro/staffe/diametro; **non calcola** `A_s` da numero/diametro barre. L'utente fornisce direttamente i valori. Se l'utente da' "3 phi 16", ricorda che `A_s = n * pi * phi^2 / 4` e SUGGERISCI il valore (es. `3 * pi * 16^2 / 4 = 603.19 mm^2`) chiedendo conferma all'utente prima di passarlo al modulo.

## Schema JSON di input

```json
{
  "b": 300,
  "h": 500,
  "d": 460,
  "As": 603.19,
  "fck": 25,
  "fyk": 450,
  "alpha_cc": 0.85,
  "gamma_c": 1.5,
  "gamma_s": 1.15,
  "Es": 200000,
  "eps_cu": 0.0035
}
```

I campi `alpha_cc`, `gamma_c`, `gamma_s`, `Es`, `eps_cu` sono opzionali.

## Procedura

1. Acquisisci i campi sopra dall'utente. Se mancano, chiedi.
2. Salva il JSON in un file temporaneo.
3. Invoca il modulo:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/flessione_ca.py --input-json /path/al/file.json
```

(in Codex / altri agent sostituisci `${CLAUDE_SKILL_DIR}` con il path assoluto della skill.)

4. Se il modulo solleva errore (campo mancante, fck > 50 MPa, sezione sovra-armata, x >= d, d > h, input negativi/non finiti), riporta il messaggio bloccante e chiedi correzione all'utente. NON aggirare l'errore.
5. Riporta l'output del modulo nella forma:

```
Input
- Geometria: b = ... mm, h = ... mm, d = ... mm
- Armatura tesa: A_s = ... mm^2
- Materiali: fck = ... MPa, fyk = ... MPa
- Coefficienti: alpha_cc = ..., gamma_c = ..., gamma_s = ...

Materiali derivati
- f_cd = ... MPa                  [eq. [4.1.3] NTC par. 4.1.2.1.1.1]
- f_yd = ... MPa                  [eq. [4.1.5] NTC par. 4.1.2.1.1.3]
- eps_yd = ...                    [eps_yd = fyd/Es, Es da NTC par. 11.3.2.1]

Geometria interna
- x = ... mm                       [equilibrio Cc = T, stress-block lambda = 0.8]
- x/d = ...
- eps_s = ...                      [compatibilita' sezione piana]
- z = d - 0.4 x = ... mm           [braccio leva]

Output
- M_Rd = ... Nmm = ... kNm        [par. 4.1.2.3.4.2 NTC: M_Rd = A_s * f_yd * z]

Duttilita'
- Acciaio snerva: ... (eps_s ... vs eps_yd ...)
- x/d <= 0.45 (NTC 2018 par. 4.1.1.1, ridistribuzione momenti travi continue): ...
- Avvertenze: ...
```

6. Concludi con:

> M_Rd e' il momento resistente di pre-dimensionamento ai sensi di NTC par. 4.1.2.3.4.2. Il confronto M_Ed <= M_Rd resta in capo al progettista, dopo aver calcolato le sollecitazioni di una combinazione SLU (vedi skill `combinazioni-carico-ntc`). La skill non verifica taglio, torsione, fessurazione, deformabilita' SLE, ne' i requisiti di gerarchia delle resistenze in zona sismica (NTC par. 7.4). Per la verifica completa il progettista deve usare software di calcolo strutturale certificato.

## Casi particolari

- **fck > 50 MPa**: il modulo solleva ValueError. Riporta che NTC eq. 4.1.10-4.1.11 richiede stress-block con lambda < 0.8 e eta < 1 (Classe 2), fuori scope; suggerisci software di calcolo strutturale.
- **Sezione sovra-armata** (eps_s < eps_yd): il modulo solleva ValueError con messaggio esplicito. Suggerisci di aumentare b o h, ridurre A_s, o passare a sezione doppiamente armata (fuori scope skill v0.1).
- **x >= d**: configurazione patologica (asse neutro oltre l'armatura tesa). Il modulo solleva ValueError. Riporta il messaggio.
- **d > h**: errore geometrico. Il modulo solleva ValueError.
- **x/d > 0.45**: il modulo restituisce M_Rd ma con avvertenza nel campo `output.avvertenze`. Riporta l'avvertenza chiaramente.
- **Zona sismica CD"A" / CD"B"** (q > 1.5): la skill non applica i limiti NTC par. 7.4.4 / 7.4.6 (rho_min, rho_max, gerarchia delle resistenze). Avvertire esplicitamente l'utente che il pre-dimensionamento NON e' sufficiente per zona sismica e va integrato dal progettista.

## Limiti del task

Vedi `SKILL.md` sezione "Limiti". In particolare la skill non copre sezioni doppiamente armate, sezioni a T/L/circolari, fck > 50 MPa, pressoflessione, flessione deviata, SLE, taglio, torsione, requisiti sismici di duttilita'.
