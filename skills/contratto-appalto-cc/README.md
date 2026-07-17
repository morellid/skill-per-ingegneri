# contratto-appalto-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / esperto di contrattualistica da completare)

Skill di **supporto documentale** all'inquadramento del **contratto di appalto** di diritto privato
nel **Codice civile (R.D. 262/1942)**, Libro IV, Titolo III, **Capo VII (Dell'appalto)**, artt.
1655-1666 e 1671: nozione, subappalto, corrispettivo, materia, variazioni del progetto, verifica,
onerosità sopravvenuta, pagamento e recesso.

**Non redige il contratto** né gli atti, **non quantifica** importi e **non sostituisce** l'avvocato
né il CTU: inquadra la disciplina civilistica dell'appalto.

## Target

Ingegneri, appaltatori e committenti che devono inquadrare un contratto di appalto privato (opere o
servizi) e i suoi snodi (variazioni, verifica, pagamento, recesso).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-contratto-appalto` | Inquadra nozione, subappalto, corrispettivo, materia e regime della verifica/pagamento (artt. 1655-1658, 1662, 1665-1666) |
| `gestisci-variazioni-recesso` | Inquadra variazioni (soglia del sesto), onerosità sopravvenuta (soglia del decimo) e recesso del committente (artt. 1659-1661, 1664, 1671) |

Nucleo: **nozione** (organizzazione + rischio, art. 1655), **subappalto** previa autorizzazione
(art. 1656), **variazioni** (concordate/necessarie/ordinate, soglia del **sesto**, artt. 1659-1661),
**onerosità** con revisione oltre il **decimo** (art. 1664), **verifica e pagamento** con
accettazione anche tacita (artt. 1665-1666), **recesso** del committente con indennizzo (art. 1671).

## Fonti consultate

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - artt. 1655-1666, 1671 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il contratto d'appalto né gli atti (autorizzazioni, riserve, verbali, recesso).
- **Non quantifica** corrispettivi, revisioni o indennità.
- **Non tratta** la responsabilità per difformità/vizi/rovina (artt. 1667-1669, skill
  `responsabilita-appaltatore-rovina-cc`) né l'appalto pubblico (D.Lgs. 36/2023).

**La skill è un supporto documentale: non sostituisce l'avvocato, il CTU né la lettura degli artt.
1655 ss. del Codice civile e delle clausole contrattuali.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
