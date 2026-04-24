# Validazione di una skill

Livelli e checklist per portare una skill dallo scaffold al release.

## Tre livelli di validazione

### Livello 1 - Self-check (autore)

Eseguibile dall'autore stesso. Obbligatorio prima di chiedere review esterna.

Checklist:
- [ ] `SKILL.md` con frontmatter `name` e `description` validi
- [ ] Tutti i file linkati da `SKILL.md` esistono
- [ ] `references/sources.yaml` valido e completo (ogni fonte ha url, accessed, sha256)
- [ ] Hash SHA256 verificati contro i binari locali
- [ ] Estratti normativi presenti in `references/estratti/` per le fonti pubbliche citate
- [ ] Almeno 2 esempi in `examples/` (1 conforme, 1 problematico)
- [ ] Disclaimer di responsabilita' professionale presente in `SKILL.md`
- [ ] `CHANGELOG.md` aggiornato con versione corrente
- [ ] `README.md` della skill che spiega come usarla
- [ ] Script `./scripts/validate.sh <skill-name>` passa senza errori

### Livello 2 - Validazione di dominio

Eseguibile da un ingegnere di dominio diverso dall'autore. Obbligatorio per release v1.0 (v0.x e' alpha).

Il validatore:
1. Legge la skill dall'esterno, come utente
2. Applica la skill a un caso reale del suo lavoro (con consenso cliente)
3. Verifica:
   - La skill produce output corretto?
   - Le citazioni normative sono accurate?
   - Ci sono falsi positivi o falsi negativi?
   - L'output e' utilizzabile o richiede rilavorazione eccessiva?

Output: report in `skills/<name>/validazione/<validatore-data>.md` con:
- Caso d'uso testato
- Output skill vs output atteso
- Problemi rilevati
- Raccomandazione: approve / revise / reject

### Livello 3 - Test di campo

Uso della skill da parte di 3+ ingegneri diversi, su casi reali, per almeno 2-3 settimane. Raccolta feedback strutturato.

Obbligatorio per stabilire "batterie" di test case che diventano parte di `examples/`.

## Checklist pre-release (v0.1.0-alpha)

Release minimo: self-check + almeno un validatore di dominio.

- [ ] Livello 1 completo
- [ ] Livello 2 completo con raccomandazione "approve" (eventualmente con revisioni minori applicate)
- [ ] Issue per feedback aperta su GitHub
- [ ] Annuncio al canale appropriato (commissione informatica Ordine, newsletter, etc.)

## Checklist pre-release (v1.0.0)

Stabile. Richiede:

- [ ] Livello 1, 2 e 3 completi
- [ ] Almeno 3 validatori di dominio indipendenti hanno approvato
- [ ] Minimo 10 casi di test documentati in `examples/`
- [ ] Log di almeno 20 utilizzi reali (non demo) con esito positivo
- [ ] Nessun bug critico aperto
- [ ] Disclaimer verificato da consulente legale (ideale)

## Aggiornamento test dopo modifica

Dopo ogni modifica non banale:
1. Rigirare `./scripts/validate.sh <skill-name>`
2. Verificare che gli esempi esistenti producano ancora output atteso
3. Se breaking change: richiedere nuova validazione di dominio

## Strumenti di supporto

`scripts/validate.sh <skill-name>` esegue:
- Parsing YAML del frontmatter
- Validazione schema di `sources.yaml`
- Check integrita' dei link interni (task files, estratti, esempi)
- Check presenza disclaimer
- Report in stdout
