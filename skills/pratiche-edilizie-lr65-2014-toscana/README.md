# Pratiche edilizie LR 65/2014 Toscana - Document checker

> Versione: 0.1.0-alpha
> Stato: alpha - non validato da tecnico abilitato toscano o tecnico SUE esterno

Determina il titolo abilitativo edilizio corretto (Edilizia libera, CILA, SCIA, PdC)
per interventi in Toscana ai sensi della LR 65/2014 e genera la checklist dei documenti
da allegare alla pratica, incluse le specificita' regionali (zona sismica, Genio Civile,
vincolo paesaggistico).

## Target

Ingegneri, architetti, geometri e tecnici SUE/SUAP che operano in Toscana e devono:
- Determinare il titolo abilitativo corretto per un intervento edilizio
- Preparare la documentazione per la pratica CILA, SCIA o Permesso di Costruire

## Cosa fa

- **Determina il titolo abilitativo**: dato un intervento, determina se serve CILA, SCIA
  o Permesso di Costruire (o edilizia libera), con motivazione normativa e indicazione
  degli adempimenti connessi (zona sismica, Genio Civile, vincoli paesaggistici)
- **Genera la checklist documenti**: dato il tipo di pratica e le caratteristiche
  dell'intervento, produce la checklist dei documenti obbligatori e condizionali
  da allegare prima della presentazione allo SUE/SUAP

Per il dettaglio tecnico di ogni sotto-attivita' vedi `SKILL.md`.

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/pratiche-edilizie-lr65-2014-toscana" "$HOME/.claude/skills/pratiche-edilizie-lr65-2014-toscana"

# Codex
ln -sfn "$(pwd)/skills/pratiche-edilizie-lr65-2014-toscana" "$HOME/.agents/skills/pratiche-edilizie-lr65-2014-toscana"
```

## Fonti principali

- LR Toscana 10 novembre 2014 n. 65 - Norme per il governo del territorio
  https://raccoltanormativa.consiglio.regione.toscana.it/
- DPR 6 giugno 2001 n. 380 - Testo Unico Edilizia
  https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-06-06;380
- Regione Toscana - Pratiche edilizie e SUE
  https://www.regione.toscana.it/pratiche-edilizie

Dettaglio completo in `references/sources.yaml`.

## Limiti noti

- Non copre le sanatorie (art. 36 e 36-bis DPR 380/2001): usare skill `modulistica-edilizia-unificata`
- Non copre il recupero dei sottotetti LR Toscana 5/2010
- La numerazione degli articoli della LR 65/2014 va verificata sul portale normativo regionale:
  la legge ha subito modifiche nel 2019, 2020, 2021 e 2024
- Non conosce le specificita' del Piano Operativo di ogni Comune: segnala il rinvio allo SUE
- La classificazione sismica per Comune specifico va verificata esternamente (INGV / Regione Toscana)
- Non calcola il contributo di costruzione (dipende dalle tabelle del Comune)
- Non e' stata validata da tecnico abilitato toscano con esperienza SUE: versione alpha

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
