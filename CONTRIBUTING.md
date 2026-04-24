# Contribuire a skill-per-ingegneri

## Prima di contribuire

- Essere ingegnere iscritto all'Albo (o professionista equivalente) nel dominio della skill cui si contribuisce.
- Avere familiarita' con il formato [Anthropic skill-creator](https://docs.anthropic.com/) e la struttura di questo repo.
- Aver letto [`methodology/generazione-skill.md`](methodology/generazione-skill.md) e [`methodology/validazione.md`](methodology/validazione.md).

## Principi non negoziabili

1. **Solo fonti ufficiali**. Ogni affermazione normativa nelle skill e' riconducibile a un documento identificato in `sources.yaml` con URL, data di consultazione, hash SHA256.
2. **Responsabilita' professionale**. Ogni skill include un disclaimer che l'output non sostituisce il giudizio del professionista firmatario.
3. **Validazione pre-release**. Nessuna skill raggiunge v1.0 senza almeno una validazione da parte di un ingegnere di dominio diverso dall'autore.
4. **Changelog sempre aggiornato**. Ogni modifica incrementa semver e appare in CHANGELOG.md della skill.

## Processo

### Nuova skill

1. Leggi [`methodology/criteri-selezione.md`](methodology/criteri-selezione.md) per valutare se il task proposto e' adatto.
2. Apri una issue con la proposta (cosa fa, su quali fonti si basa, dominio applicativo).
3. Una volta approvata, usa lo scaffold: `scripts/new-skill.sh nome-skill`.
4. Segui [`methodology/generazione-skill.md`](methodology/generazione-skill.md).
5. PR con la skill a versione `0.1.0-alpha`, marcata come draft finche' non passa validazione.

### Modifica a skill esistente

1. Apri una issue che identifica il problema o il miglioramento.
2. PR con modifiche mirate:
   - Bug fix: patch version (`0.1.0 → 0.1.1`)
   - Miglioramento compatibile: minor version (`0.1.0 → 0.2.0`)
   - Breaking change o major update normativo: major version (`0.x.y → 1.0.0`)
3. CHANGELOG.md aggiornato con descrizione e riferimento al trigger normativo se applicabile.

### Aggiornamento fonti normative

Quando una norma cambia (modifica legislativa, decreto attuativo, nuova linea guida):

1. Verifica l'impatto sulle skill che la citano.
2. Aggiorna `sources.yaml`: nuovo URL se cambia, nuova `accessed`, nuovo `sha256`, nuovo `excerpt_path`.
3. Aggiorna gli estratti in `references/estratti/` se necessari.
4. Incrementa la versione della skill.
5. CHANGELOG.md: sezione "Aggiornamento normativo" con riferimento esatto.

## Stile

- **Lingua**: contenuti utente in italiano, struttura/metadata in inglese.
- **Punteggiatura**: caratteri standard ASCII. Evitare trattini lunghi, virgolette tipografiche, apostrofi tipografici.
- **Commit message**: in inglese, formato [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`).
- **File YAML**: indentazione 2 spazi.
- **Markdown**: una frase per riga per diff puliti (opzionale).

## Codice di condotta

Il repo ha obiettivi professionali e istituzionali. Discussioni tecniche e critiche costruttive sono benvenute. Polemiche personali, spam e self-promotion non pertinente vengono rimossi.
