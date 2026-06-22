# Denuncia opere strutturali e autorizzazione sismica - DPR 380/2001

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1, source-grounded; non ancora validata da
> dominio terzo)

Skill che guida il professionista nel determinare quali pratiche strutturali e
sismiche del DPR 380/2001 si applicano a un intervento edilizio in Italia, con
checklist degli allegati e dei soggetti firmatari.

## Target

- Ingegneri strutturisti incaricati della progettazione strutturale di nuove
  costruzioni o di interventi su esistenti;
- Direttori dei lavori di opere in c.a., c.a.p. o struttura metallica;
- Costruttori (imprese edili) tenuti alla denuncia ex art. 65 DPR 380;
- Responsabili dell'ufficio tecnico di committenze pubbliche e private.

## Cosa fa

Sotto-attivita' disponibili (vedi `SKILL.md` per i dettagli):

- **Diagnosi adempimenti**: dato un intervento, indica quali pratiche servono e
  in che ordine, classificando l'intervento ex art. 94-bis.
- **Checklist denuncia ex art. 65** (opere in c.a./c.a.p./metalliche).
- **Checklist preavviso e autorizzazione zona sismica** (artt. 93, 94, 94-bis).
- **Checklist collaudo statico ex art. 67**.

## Installazione

Vedi `README.md` di root del repo per le istruzioni generali di installazione
delle skill (Claude Code, Codex CLI).

## Fonti consultate

- DPR 6 giugno 2001 n. 380 - Testo unico edilizia (versione multivigente
  Normattiva al 2026-05-22), articoli 65, 67, 83, 93, 94, 94-bis.

Dettaglio in `references/sources.yaml`. Trascrizione fedele degli articoli in
`references/fonti/dpr-380-2001-testo-unico-edilizia.md`. Estratti operativi in
`references/estratti/`.

## Limiti noti

- La classificazione operativa puntuale degli interventi ex art. 94-bis comma 2
  e' delegata a elencazioni regionali: la skill copre il quadro statale; per la
  classificazione regionale verificare la disciplina vigente nel comune di
  intervento (per la Toscana esiste la skill dedicata
  `pratiche-edilizie-lr65-2014-toscana`).
- La distinzione fra adeguamento, miglioramento e intervento locale e' tema
  delle NTC 2018 capitolo 8: resta valutazione tecnica del progettista
  strutturale.
- La skill non si occupa di sanzioni per opere realizzate senza denuncia o
  senza autorizzazione (artt. 71-76 e 95 e ss. DPR 380) - fuori scope v0.1.
- La skill non determina il titolo edilizio (PdC / SCIA / CILA): per quello
  vedi `modulistica-edilizia-unificata`.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
