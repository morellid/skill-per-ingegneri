# Update cycle

Cosa fare quando la normativa cambia o emergono errori nelle skill.

## Trigger di aggiornamento

Monitorare costantemente:

- **Gazzetta Ufficiale** - modifiche legislative
- **Siti ministeriali** (MIT, MITE, Ministero del Lavoro) - decreti attuativi, chiarimenti
- **CNI e Ordini territoriali** - linee guida, circolari
- **INAIL** - aggiornamenti su sicurezza, normativa tecnica
- **UNI/CEI** - aggiornamenti norme tecniche (anche se testo non distribuibile)
- **Issue GitHub** - bug report da utenti
- **Feedback da validatori** - problemi emersi in uso reale

## Processo standard

### Trigger: modifica normativa

1. **Analisi impatto** (entro 7 giorni dalla pubblicazione):
   - Quali skill citano la norma modificata?
   - La modifica e' sostanziale (richiede aggiornamento skill) o marginale (citazione aggiornata ma logica invariata)?
   - La modifica introduce nuovi obblighi che creano opportunita' di nuove skill?

2. **Aggiornamento `sources.yaml`**:
   - Nuovo URL se la norma consolidata e' a URL diverso
   - Nuova `accessed`
   - Nuovo `sha256` del binario aggiornato
   - `notes` che descrive cosa e' cambiato

3. **Aggiornamento estratti** in `references/estratti/`:
   - Testo aggiornato degli articoli rilevanti
   - Marker `> [STORICO 2024-04]` se si tiene traccia della versione precedente

4. **Aggiornamento task files** se necessario:
   - Modifica procedurale, checklist, output atteso

5. **Version bump**:
   - Patch: correzione citazione, non cambia la logica
   - Minor: modifica non breaking dei task
   - Major: breaking change (es. la norma e' stata abrogata e sostituita integralmente)

6. **CHANGELOG.md**:
   ```markdown
   ## [0.2.0] - 2026-06-15
   ### Aggiornamento normativo
   - D.Lgs. 81/2008 art. 96: modificato da DL 45/2026 conv. L. 78/2026
   - Aggiornato `check-completezza.md` per nuovo comma 3-bis
   - Nuovo estratto in `references/estratti/dlgs-81-art-96-2026.md`
   ```

7. **Test di regressione**:
   - Rigirare gli esempi esistenti
   - Se cambia output: aggiornare expected-output con commento
   - Eventuale nuova validazione di dominio per major update

8. **Comunicazione**:
   - Note release su GitHub
   - Notifica agli utenti registrati (quando esistera' il canale)

### Trigger: bug report utente

1. **Triage** (entro 48h):
   - Conferma del bug (riproducibile?)
   - Severita' (critical, high, medium, low)
   - Impatto (quanti utenti, rischio di output errato)

2. **Fix**:
   - Patch version per bug minori
   - Minor/major se richiede ristrutturazione

3. **Regression test**: aggiungere il caso bug tra gli esempi

### Trigger: feedback da validatore

Vedi [`validazione.md`](validazione.md). I feedback di validazione vengono classificati e affrontati secondo severita'.

## Calendario di review periodica

Anche in assenza di trigger esterni:

- **Trimestrale**: scan di tutte le fonti citate, verifica che URL siano vivi, date ragionevoli
- **Semestrale**: review completa di almeno una skill, con rivalidazione di dominio
- **Annuale**: review dell'intero repo, cleanup di skill obsolete o deprecate

## Deprecation di skill

Se una skill diventa obsoleta (normativa abrogata, uso non piu' rilevante):

1. Tag versione finale con `-deprecated` in CHANGELOG
2. Issue di deprecation aperta con razionale
3. Spostamento in `skills/_archived/<nome>/` dopo 6 mesi
4. Redirect in README a skill sostitutiva (se esiste)

## Monitoraggio automatico (futuro)

Quando il repo sara' maturo, implementare:
- Script che scarica periodicamente le fonti e confronta hash
- Notifica se hash cambia (possibile modifica normativa)
- Crawl automatico di gazzettaufficiale.it per leggi citate
- Integrazione con feed RSS ministeriali

Per ora: processo manuale, con reminder in calendario.
