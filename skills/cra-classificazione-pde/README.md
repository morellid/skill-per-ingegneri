# cra-classificazione-pde

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1, autore + review adversariale)

Skill di supporto alla **classificazione dei prodotti con elementi digitali (PDE)** ai sensi del **Regolamento (UE) 2024/2847 - Cyber Resilience Act (CRA)** e alla selezione della procedura di valutazione della conformita' e della documentazione tecnica richieste.

## Target

Ingegneri/security engineer, product compliance manager, responsabili tecnici del fabbricante o del rappresentante autorizzato che debbano inquadrare un PDE rispetto al CRA prima dell'immissione sul mercato dell'Unione europea.

## Cosa fa

Quattro sotto-attivita':

1. **Verifica ambito di applicabilita' del CRA** (`tasks/check-ambito-applicabilita.md`): determina se un prodotto rientra nell'ambito del Regolamento (UE) 2024/2847 (Art. 2 - filtro positivo + esclusioni) e applica la definizione di PDE (Art. 3 punto 1).
2. **Classificazione del PDE** (`tasks/classifica-pde.md`): identifica se il PDE e' default, importante Classe I, importante Classe II (Allegato III), o critico (Allegato IV) sulla base di Art. 7-8.
3. **Scelta del modulo di valutazione della conformita'** (`tasks/scegli-procedura-conformita.md`): a partire dalla categoria, individua le procedure ammesse (modulo A, B+C, H, certificazione UE) e il ruolo dell'organismo notificato ex Art. 32 e Allegato VIII.
4. **Checklist documentazione tecnica** (`tasks/check-documentazione-tecnica.md`): verifica se la documentazione tecnica del PDE copre gli 8 punti dell'Allegato VII ex Art. 31.

## Cosa NON fa (limiti noti)

- Non produce DoC UE firmate, ne' fascicoli tecnici pronti per la marcatura CE.
- Non valuta tecnicamente la conformita' del PDE ai requisiti essenziali dell'Allegato I.
- Non sostituisce gli atti di esecuzione/delegati attesi (Art. 7 par. 4 - descrizione tecnica Allegato III, attesa per 11/12/2025; Art. 8 par. 1 - categorie Allegato IV soggette a certificazione UE).
- Non valida la scelta dell'organismo notificato (banca dati NANDO).
- Non copre gli obblighi di segnalazione vulnerabilita'/incidenti gravi (Art. 14, fuori scope v0.1).
- Non e' una guida operativa all'implementazione SBOM, politica CVD, aggiornamenti automatici (requisiti tecnici Allegato I, parte II).
- Non interpreta sanzioni amministrative del diritto interno (Art. 64).

## Installazione

Per installare la skill in Claude Code:

```bash
ln -s "$(pwd)/skills/cra-classificazione-pde" "$HOME/.claude/skills/cra-classificazione-pde"
```

Per Codex (OpenAI):

```bash
ln -s "$(pwd)/skills/cra-classificazione-pde" "$HOME/.agents/skills/cra-classificazione-pde"
```

## Fonti consultate

Fonte unica: **Regolamento (UE) 2024/2847** del Parlamento europeo e del Consiglio del 23 ottobre 2024 (Cyber Resilience Act), pubblicato in GU UE L del 20/11/2024. ELI: <http://data.europa.eu/eli/reg/2024/2847/oj>.

Dettaglio completo, SHA256 e path locale del PDF in `references/sources.yaml`. Trascrizione in `references/fonti/`. Estratto curato in `references/estratti/`.

## Disclaimer

Strumento di supporto alla redazione/verifica. Non sostituisce il giudizio del fabbricante o del professionista firmatario. Il fabbricante (o il rappresentante autorizzato) resta unico responsabile della corretta classificazione, della scelta della procedura di valutazione e della completezza della DoC UE e della documentazione tecnica.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
