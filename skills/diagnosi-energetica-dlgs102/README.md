# diagnosi-energetica-dlgs102

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con EGE/energy manager da completare)

Skill di **supporto documentale all'obbligo di diagnosi energetica** delle grandi
imprese e delle imprese a forte consumo di energia ai sensi dell'**art. 8 del
D.Lgs. 102/2014** (attuazione della direttiva 2012/27/UE).

**Non e' una skill di calcolo**: determina applicabilita', esenzioni, periodicita'
e sanzioni, non esegue la diagnosi.

## Target

Energy manager, EGE, ESCo, consulenti energetici, imprese obbligate.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `verifica-obbligo` | Dato il profilo dell'impresa (dimensione, fatturato/bilancio, consumi in tep, ISO 50001, energivora): determina se la diagnosi e' obbligatoria, le esenzioni (< 50 tep, ISO 50001), la periodicita' quadriennale e il soggetto esecutore |
| `checklist-adempimento` | Verifica la completezza degli adempimenti (esecuzione, ESCo/EGE certificati, comunicazione ENEA, interventi per le energivore) |

Obbligo (art. 8): grandi imprese (> 250 occupati e fatturato > 50 mln, oppure
bilancio > 43 mln) ed energivore; diagnosi **ogni 4 anni** da **ESCo/EGE
certificati** (UNI CEI 11352/11339); comunicazione all'**ENEA**.

## Fonti consultate

- **D.Lgs. 4/7/2014 n. 102**, testo vigente su Normattiva (pagina indice pinnata
  `!vig=2026-07-14`) - artt. 2, 8, 16 (attuazione dir. 2012/27/UE)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non esegue la diagnosi energetica ne' calcola consumi/risparmi
- Non riproduce l'allegato 2 (criteri minimi) ne' le norme UNI CEI 11352/11339 e
  ISO 50001 (a pagamento)
- Non stabilisce nel merito se un'impresa sia "energivora" (DM MiSE 21/12/2017)
- Non copre gli altri istituti del D.Lgs. 102/2014 (contatori/fatturazione art. 9,
  certificati bianchi/TEE) oltre ai richiami

**La skill e' un supporto documentale: non sostituisce l'impresa ne' l'auditor
certificato.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
