# AUA - dossier ex D.P.R. 59/2013

> Versione: 0.1.0-alpha
> Stato: in sviluppo (non ancora validata da dominio terzo)

Skill di supporto alla preparazione e all'autoverifica del dossier per
l'Autorizzazione Unica Ambientale ai sensi del D.P.R. 13 marzo 2013, n. 59.

## Target

- Ingegneri ambientali e consulenti HSE che predispongono istanze AUA
  per imprese clienti.
- Tecnici SUAP e ufficio ambiente di Province/Citta' metropolitane/ARPA
  che istruiscono dossier AUA.
- Addetti ufficio ambiente di PMI che gestiscono internamente l'AUA.

La skill **non** e' destinata a impianti soggetti ad AIA (D.Lgs. 152/2006,
Titolo III-bis Parte II) ne' a progetti con VIA assorbente
(art. 26 co. 4 D.Lgs. 152/2006).

## Cosa fa

Sotto-attivita' supportate (dettaglio in `SKILL.md` e nei task):

- **Verifica applicabilita'**: controllo se l'impianto rientra nel
  perimetro AUA (PMI, non-AIA, non-VIA assorbente).
  Task: `tasks/check-applicabilita.md`.
- **Mapping titoli incorporabili**: quali titoli ambientali confluiscono
  nell'AUA ex art. 3 co. 1 lett. a-g, g-bis, g-ter e quali restano fuori.
  Task: `tasks/mappa-titoli-art3.md`.
- **Pianificazione termini procedurali**: 30/90/120/150 giorni,
  conferenza di servizi, cronoprogramma. Task: `tasks/pianifica-termini.md`.
- **Pianificazione rinnovo**: finestra 6 mesi pre-scadenza, checklist
  documentale, continuita' esercizio nelle more. Task:
  `tasks/pianifica-rinnovo.md`.
- **Triage modifica sostanziale/non sostanziale**: classificazione
  modifica ex art. 6 e flusso procedurale (comunicazione vs nuova
  istanza). Task: `tasks/triage-modifica-art6.md`.

## Installazione

La skill e' distribuita come cartella `skills/aua-dpr59-dossier/`
all'interno del repository `skill-per-ingegneri`. Per usarla con Claude
Code o con Codex CLI, posizionarla (o creare un symlink) nella directory
delle skill dell'agent di scelta:

- Claude Code: `~/.claude/skills/aua-dpr59-dossier/`
- OpenAI Codex CLI: `~/.agents/skills/aua-dpr59-dossier/`

Riferimenti operativi nel `README.md` del repository.

## Fonti consultate

Fonte principale:

- D.P.R. 13 marzo 2013, n. 59 - Regolamento AUA, testo vigente da
  Normattiva (`https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2013-03-13;59`),
  accessed 2026-05-19.

Fonti collegate citate ma non riprodotte (rinvio a Normattiva per il
testo letterale): D.Lgs. 152/2006 (Codice Ambiente), L. 447/1995
(legge quadro inquinamento acustico), L. 241/1990 (procedimento
amministrativo), D.P.R. 160/2010 (SUAP), D.Lgs. 101/2020 (radiazioni
ionizzanti), D.Lgs. 99/1992 (fanghi in agricoltura), DM 18 aprile 2005
(definizione PMI).

Dettaglio completo in `references/sources.yaml`.

## Limiti noti

- Non valuta nel merito tecnico i singoli titoli incorporati (scarichi,
  emissioni, rifiuti, acustica, fanghi, radiazioni): la skill aggrega
  e procedimentalizza, non calcola.
- Non distribuisce modulistica regionale: le Regioni e Province Autonome
  adottano propri moduli SUAP che la skill non riproduce.
- Non interpreta giurisprudenza amministrativa (TAR, Consiglio di Stato)
  ne' la prassi delle ARPA o delle autorita' competenti locali.
- Non valuta l'applicabilita' di AIA o VIA: per questi rinviare a
  strumenti dedicati e al D.Lgs. 152/2006.
- L'Allegato I del D.P.R. 59/2013 (tipologie di impianti soggetti ad
  autorizzazione di carattere generale) contiene tabelle in formato
  grafico nella GU originale: la skill rimanda alla GU n.124 del
  29-05-2013 S.O. n.42 per il dettaglio.
- Output del **professionista firmatario**: la skill produce report di
  autoverifica, non documenti pronti al deposito al SUAP.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
