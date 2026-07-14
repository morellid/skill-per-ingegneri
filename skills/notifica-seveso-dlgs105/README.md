# notifica-seveso-dlgs105

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto RIR/sicurezza di processo da completare)

Skill di **supporto documentale agli obblighi degli stabilimenti a rischio di
incidente rilevante** (Seveso III) ai sensi del **D.Lgs. 105/2015** (attuazione
della direttiva 2012/18/UE).

**Non e' una skill di calcolo**: determina assoggettabilita', classificazione
(soglia inferiore/superiore) e adempimenti; non legge le soglie
sostanza-specifiche ne' redige il rapporto di sicurezza.

## Target

Gestori di stabilimenti, RSPP e tecnici della sicurezza di processo, consulenti
ambientali, uffici CTR/ISPRA/Regione.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `verifica-assoggettabilita` | Dato il profilo dello stabilimento (sostanze pericolose, quantita', attivita', esclusioni), determina se e' soggetto al decreto e se e' di soglia inferiore o superiore, rinviando all'allegato 1 per le soglie e la sommatoria |
| `checklist-adempimenti` | Verifica la completezza degli adempimenti (notifica art. 13, PPIR/SGS art. 14, RdS art. 15) con destinatari, termini e sanzioni |

Nucleo: **assoggettabilita'** (art. 2/3), **notifica** a CTR/Regione/ISPRA/
Prefettura/Comune/VVF (art. 13), **PPIR + SGS** per tutti (art. 14), **rapporto
di sicurezza** per la sola soglia superiore (art. 15), **sanzioni** (art. 28).

## Fonti consultate

- **D.Lgs. 26/6/2015 n. 105**, testo vigente su Normattiva (pagina indice pinnata
  `!vig=2026-07-14`) - artt. 2, 3, 13, 14, 15, 28 (attuazione dir. 2012/18/UE)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce le **soglie** dell'allegato 1 ne' esegue la **regola della
  sommatoria** (nota 4): rinvia all'allegato 1 e alla classificazione CLP (Reg.
  1272/2008)
- Non redige RdS, PPIR, SGS ne' i piani di emergenza interna/esterna
- Non copre l'istruttoria del RdS (art. 17), il nulla osta di fattibilita', la
  pianificazione territoriale (art. 22) o l'informazione al pubblico (art. 23-24)
  oltre ai richiami

**La skill e' un supporto documentale: non sostituisce il gestore, il CTR,
l'ISPRA ne' i tecnici incaricati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
