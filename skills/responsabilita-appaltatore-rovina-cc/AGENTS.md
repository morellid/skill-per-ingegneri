# AGENTS.md - responsabilita-appaltatore-rovina-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **responsabilità dell'appaltatore** per **difformità e vizi** dell'opera e
per la **rovina e i gravi difetti** degli edifici: garanzia, termini (denuncia, decadenza,
prescrizione), rimedi, responsabilità decennale, secondo il **Codice civile, artt. 1667, 1668, 1669**.
Target: ingegneri, direttori dei lavori, CTU e consulenti tecnici di parte.

**È una skill documentale**: inquadra presupposti e termini di legge; **non accerta** i vizi/la
rovina, il nesso causale o il quantum, **non fornisce** interpretazione giurisprudenziale, non
sostituisce il legale, il CTU o il giudice.

## Nota sull'area

Area **forense**. Complementare a `relazione-peritale-ctu-cpc` (relazione del CTU nel merito), a
`accertamento-tecnico-preventivo-cpc` (ATP/CTP preventiva) e a `compensi-ctu-dpr115`: questa copre il
**regime sostanziale** della responsabilità dell'appaltatore (diritto civile).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cc-artt-1667-1668-1669**: Codice civile (R.D. 262/1942), pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `f817bc32...`; codice 042U0262). Artt. 1667, 1668, 1669 (idGruppo 208,
  flagTipoArticolo 2) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/cc-artt-1667-1668-1669.md`; estratto operativo in
`references/estratti/responsabilita-appaltatore-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 1667**: garanzia per difformità/vizi; esclusione per vizi noti/riconoscibili accettati salvo
  mala fede; **denuncia 60 gg** a pena di decadenza (non necessaria se riconosciuti/occultati);
  **prescrizione 2 anni** dalla consegna; eccezione del committente convenuto per il pagamento.
- **Art. 1668**: rimedi (eliminazione a spese dell'appaltatore / riduzione del prezzo / risarcimento se
  colpa; risoluzione se opera inadatta).
- **Art. 1669**: **responsabilità decennale** per rovina/pericolo di rovina/gravi difetti di immobili
  a lunga durata (vizio del suolo/difetto di costruzione), verso committente e **aventi causa**;
  **denuncia entro 1 anno** dalla scoperta; **prescrizione 1 anno** dalla denuncia.

## Convenzioni specifiche

### Cosa NON fare
- Non **accertare** i vizi/la rovina, il nesso causale o il quantum (spetta al CTU).
- Non fornire l'**interpretazione giurisprudenziale** dell'art. 1669 né la strategia processuale.
- Non **confondere i termini**: art. 1667 (60 gg / 2 anni) vs art. 1669 (10 anni / 1 anno / 1 anno).

### Cosa fare
- **Distinguere** garanzia per vizi (1667-1668) da responsabilità per rovina (1669); **verificare i
  termini** e i **rimedi**; rinviare al CTU/legale per accertamenti e strategia.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del Codice civile pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 1667-1669.

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista o CTU esperto in edilizia).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-garanzia-vizi.md`, `inquadra-rovina-1669.md`)
- Esempi: 2 (vizi scoperti dopo la consegna - artt. 1667-1668; gravi difetti dell'edificio - art. 1669)
