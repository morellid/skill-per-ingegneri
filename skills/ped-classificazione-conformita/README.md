# PED - Classificazione e valutazione della conformita'

> Versione: 0.1.0-alpha
> Stato: in sviluppo (validazione Livello 1 - adversarial review interna). Da promuovere dopo validazione Livello 2 da ingegnere meccanico di dominio diverso dall'autore.

Skill di supporto per impostare la classificazione PED di un'attrezzatura a pressione e la selezione della procedura di valutazione della conformita', ai sensi del **D.Lgs 26/2016** (recepimento della Direttiva 2014/68/UE).

## Target

Ingegneri meccanici, tecnici della sicurezza, responsabili qualita' che lavorano per il fabbricante (o rappresentante autorizzato, importatore, distributore equiparato) di un'attrezzatura a pressione con PS > 0,5 bar. La skill copre la fase pre-immissione sul mercato (classificazione, scelta del modulo, predisposizione documentazione tecnica, marcatura CE, dichiarazione UE), non la fase di esercizio.

## Cosa fa

Cinque sotto-attivita':

1. **Verifica ambito di applicabilita'** (`tasks/check-ambito-applicabilita.md`): identifica se l'attrezzatura ricade nel D.Lgs 26/2016 o in esclusioni e direttive parallele.
2. **Classificazione del fluido** (`tasks/classifica-fluido.md`): determina gruppo 1 o gruppo 2 secondo art. 9 c. 1.
3. **Determinazione della categoria** (`tasks/determina-categoria.md`): indica la tabella applicabile dell'Allegato II, le eccezioni testuali, e rinvia al PDF della GU per la lettura grafica della categoria.
4. **Scelta della procedura di valutazione della conformita'** (`tasks/scegli-procedura-conformita.md`): elenca i moduli ammissibili per la categoria ex art. 10 c. 2, con coinvolgimento o meno dell'organismo notificato.
5. **Checklist marcatura CE e dichiarazione UE** (`tasks/check-marcatura-ce-dichiarazione.md`): verifica completezza degli adempimenti di marcatura e contenuto della dichiarazione UE ex art. 5 e art. 15.

Per il dettaglio tecnico di routing e processo vedi `SKILL.md`.

## Installazione

Symlink alla cartella della skill nel percorso di discovery del proprio agent:

```bash
# Claude Code
ln -sfn "$(pwd)/skills/ped-classificazione-conformita" "$HOME/.claude/skills/ped-classificazione-conformita"

# OpenAI Codex
ln -sfn "$(pwd)/skills/ped-classificazione-conformita" "$HOME/.agents/skills/ped-classificazione-conformita"
```

## Fonti consultate

- **D.Lgs 15 febbraio 2016, n. 26** (recepimento Direttiva 2014/68/UE - PED) - GU Serie Generale n.53 del 04/03/2016. Trascrizione fedele in `references/fonti/dlgs-26-2016.md`.

Dettaglio completo (URL, accessed, sha256, licenza) in `references/sources.yaml`.

## Limiti noti

- Le tabelle 1-9 dell'Allegato II del decreto sono diagrammi grafici nel PDF della GU. La skill rinvia al PDF per la lettura puntuale dei valori soglia che delimitano le categorie I, II, III, IV in funzione di PS, V o DN. Non e' possibile, partendo da PS e V/DN, restituire la categoria come funzione chiusa senza la lettura visiva del diagramma.
- La skill non produce dichiarazioni UE di conformita' firmate ne' fascicoli tecnici pronti alla marcatura CE: il fabbricante (o suo rappresentante autorizzato) resta l'unico responsabile.
- Non copre verifiche periodiche post-marcatura (D.Lgs 81/2008, DM 329/2004), apparecchi a pressione semplici (Dir. 2014/29/UE), trasporto (ADR/RID), apparecchi militari, ne' calcoli strutturali (sollecitazioni, spessori, prove idrostatiche).
- Validazione Livello 2 (ingegnere meccanico esterno all'autore) non ancora ottenuta: la skill e' attualmente `0.1.0-alpha`.

## Avvertenza

Strumento di supporto, non sostitutivo del giudizio del fabbricante o del professionista firmatario. Vedi `SKILL.md` sezione "Avvertenza" per la formula completa.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
