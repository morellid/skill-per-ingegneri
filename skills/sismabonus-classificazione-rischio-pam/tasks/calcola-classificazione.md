# Task: calcola classificazione rischio sismico DM 58/2017

## Obiettivo

Produrre, dato l'output dell'analisi di vulnerabilita' di un edificio esistente, la classificazione del rischio sismico ai sensi del DM 58/2017 Allegato A (metodo convenzionale): PAM, IS-V, classe PAM, classe IS-V, classe finale, e (se richiesto) salto classi tra stato di fatto e stato di progetto.

## Input richiesti

Per **ciascuno stato** (di fatto, opzionalmente di progetto), per **ciascuno dei 4 SL NTC** (SLO, SLD, SLV, SLC):
- `TR_C` [anni]: periodo di ritorno di capacita' dell'evento che porta l'edificio a quel SL (output dell'analisi di vulnerabilita', NTC 2018 cap. 8)
- `PGA_C` [g]: accelerazione di picco al suolo di capacita' associata
- `PGA_D` [g]: accelerazione di picco al suolo di domanda al sito (NTC 2018 par. 3.2 + Allegato A) - questa NON cambia tra fatto e progetto (dipende dal sito, non dall'edificio)

SLID e SLR sono convenzionali e fissati dal modulo:
- SLID: TR=10 anni, CR=0% (Allegato A punto 2.1)
- SLR: stessa lambda di SLC, CR=100% (termine di coda della formula PAM)

Se l'utente non ha eseguito l'analisi di vulnerabilita', spiegare che la skill richiede l'output dell'analisi e non lo produce. Suggerire NTC 2018 cap. 8 e Circ. 7/2019 cap. C8.

Se l'utente non ha PGA_D, suggerire la skill `spettro-risposta-ntc` per il calcolo dello spettro NTC al sito; PGA_D = a_g(SL) × S, ovvero il valore dello spettro elastico al periodo zero per ciascuno stato limite.

## Fonti

Estratti normativi in [`../references/estratti/`](../references/estratti/):
- `dm-58-2017-allegato-a-formula-pam.md` - formula trapezoidale PAM
- `dm-58-2017-allegato-a-isv.md` - definizione IS-V
- `dm-58-2017-allegato-a-tabelle-classi.md` - tabelle classi PAM e IS-V
- `dm-58-2017-allegato-a-salto-classi.md` - regola del salto classi

## Procedura

### Passo 1 - costruzione file JSON di input

Costruire un file JSON con struttura (sostituire `<...>` con i valori numerici - le chiavi PGA_D_* in `progetto` sono OPZIONALI: se assenti, la skill eredita la PGA_D di `fatto`):

```json
{
  "fatto": {
    "TR_C_SLO": "<anni>",
    "TR_C_SLD": "<anni>",
    "TR_C_SLV": "<anni>",
    "TR_C_SLC": "<anni>",
    "PGA_C_SLO": "<g>",
    "PGA_C_SLD": "<g>",
    "PGA_C_SLV": "<g>",
    "PGA_C_SLC": "<g>",
    "PGA_D_SLO": "<g>",
    "PGA_D_SLD": "<g>",
    "PGA_D_SLV": "<g>",
    "PGA_D_SLC": "<g>"
  },
  "progetto": {
    "TR_C_SLO": "<anni>",
    "TR_C_SLD": "<anni>",
    "TR_C_SLV": "<anni>",
    "TR_C_SLC": "<anni>",
    "PGA_C_SLO": "<g>",
    "PGA_C_SLD": "<g>",
    "PGA_C_SLV": "<g>",
    "PGA_C_SLC": "<g>"
  }
}
```

(Nota: nello schema sopra i valori sono mostrati come stringhe placeholder solo perche' JSON non ammette commenti; sostituirli con numeri reali.)

La sezione `progetto` e' opzionale: omessa se l'utente vuole solo classificare lo stato di fatto.

**Regola PGA_D in `progetto`** (per evitare typo silenziosi): o si forniscono TUTTE e 4 le chiavi `PGA_D_*` (caso anomalo: cambio sito), oppure NESSUNA (caso normale: PGA_D ereditata da `fatto`). Una sola o due o tre chiavi -> errore esplicito.

### Passo 2 - invocazione modulo

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/sismabonus.py --input-json caso.json
```

In Codex / altri agent: sostituire `${CLAUDE_SKILL_DIR}` con il path assoluto della skill installata.

**Capping**: di default il modulo applica il capping prescritto dall'Allegato A passo 2.1.3 (TR_C(SLO/SLD) := min(TR_C(SLO/SLD), TR_C(SLV))). Per disattivarlo (es. validazione vs software che applicano il capping a monte) usare `--no-capping`. Sconsigliato in tutti gli altri casi.

### Passo 3 - lettura e parafrasi output

L'output del modulo e' un JSON con campi:
- `fonte_normativa`: stringa di citazione
- `metodo`: "Convenzionale (DM 58/2017 Allegato A punto 2.1)"
- `capping_attivo`: bool (true se applicato il capping del passo 2.1.3)
- `fatto`: struttura `RisultatoClassificazione`
  - `pam`: `RisultatoPAM` con `PAM`, `PAM_percentuale`, `classe_PAM`, `contributi_trapezoidali` (4 termini SLID->SLO, SLO->SLD, SLD->SLV, SLV->SLC), `contributo_coda_SLR`, `monotona`
  - `isv`: `RisultatoISV` con `IS_V`, `IS_V_percentuale`, `classe_IS_V`
  - `classe_finale`: classe peggiore tra classe_PAM e classe_IS_V
  - `descrizione_classe_finale`: spiegazione testuale
  - `capping`: `CappingApplicato` con TR_C originali e capped per SLO/SLD + flag `SLO_modificato`/`SLD_modificato`
- `progetto`: idem (se richiesto)
- `salto_classi`: `RisultatoSaltoClassi` con `classe_stato_fatto`, `classe_stato_progetto`, `salto_classi`, `miglioramento_pam_percent`, `miglioramento_isv_percent` (se richiesto)

Riportare al committente:
1. Il dato `fonte_normativa` per esplicitare la base normativa.
2. Per ciascuno stato (fatto, progetto):
   - Tabella TR_C / lambda / PGA_C / PGA_D per i 4 SL NTC
   - PAM in % e classe PAM con citazione "Allegato A punto 2.1"
   - IS-V in % e classe IS-V con citazione "Allegato A punto 2.2"
   - Classe finale con citazione "Allegato A punto 2.3 - peggiore tra le due"
3. Se entrambi gli stati: salto classi e miglioramenti PAM/IS-V con citazione "Allegato A punto 3".
4. Se `monotona: false`: warning esplicito "Curva di Individuazione non monotona - verificare l'analisi di vulnerabilita' o applicare capping coerente con il punto 2.1; la PAM calcolata potrebbe non essere fisicamente significativa". Rinviare al progettista per la diagnosi.

### Passo 4 - rinvio al progettista

Concludere SEMPRE con:
> L'output va verificato dal progettista strutturale firmatario prima dell'uso per l'asseverazione tecnica (Allegato B / B-bis al DM 58/2017). La determinazione dell'aliquota di detrazione fiscale sismabonus (50/70/75/80/85%) e' demandata alla legislazione fiscale vigente e al commercialista; questa skill non la calcola.

## Output atteso

Un report markdown strutturato che include:
- Tabella di sintesi `Stato di fatto | Stato di progetto | Differenza`
- Per ciascuno stato: tabella SL / TR_C / PGA_C / PGA_D / lambda
- PAM/IS-V/classe per ciascuno stato
- Salto classi + miglioramenti
- Citazioni normative puntuali
- Warning se non monotona
- Avvertenza finale con rinvio al progettista

## Limiti

Questo task NON:
- Esegue l'analisi di vulnerabilita' (input dell'utente)
- Calcola PGA_D dal sito (input dell'utente; rinvio a `spettro-risposta-ntc`)
- Genera Allegato B / B-bis pronto al deposito
- Determina aliquote fiscali
- Applica capping automatico su lambda non monotona (rinvio al progettista)
