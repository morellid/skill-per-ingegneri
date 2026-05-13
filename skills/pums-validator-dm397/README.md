# Validatore PUMS - DM 397/2017

> Versione: 0.1.0-alpha
> Stato: in sviluppo

Skill che verifica la conformita' formale di un Piano Urbano di Mobilita' Sostenibile (PUMS) alle Linee guida italiane: DM 4 agosto 2017 n. 397 come modificato dal DM 28 agosto 2019 n. 396, con riferimento operativo al Vademecum MIMS del 27 settembre 2022.

## Target

- Tecnici di amministrazioni comunali (>100.000 ab.) e di citta' metropolitane, incaricati della redazione o aggiornamento del PUMS.
- Professionisti incaricati della redazione di PUMS o di documenti tecnici di supporto (es. mobility manager d'area, consulenti).
- Valutatori di istanze di accesso ai finanziamenti TRM (Trasporto Rapido di Massa) ai sensi dell'art. 2 DM 396/2019.

## Cosa fa

La skill copre 5 sotto-attivita' di validazione:

1. **`check-ambito-obbligo.md`** - Verifica che l'ente sia tra i soggetti obbligati (art. 3 c.1 DM 397/2017) e che le condizioni per i finanziamenti TRM (art. 2 DM 396/2019) siano soddisfatte.
2. **`check-procedura-redazione-pums.md`** - Verifica i passi a-h dell'Allegato 1 (gruppo di lavoro, quadro conoscitivo, partecipazione, obiettivi, scenari, VAS, adozione+approvazione, monitoraggio).
3. **`check-obiettivi-pums.md`** - Verifica i 17 macro-obiettivi minimi della Tabella 1 (nuova) suddivisi in aree A/B/C/D.
4. **`check-indicatori-tabella1.md`** - Verifica gli indicatori di risultato con tempo "0", target a 2/3, 5 e 10 anni e metodologie specifiche.
5. **`check-monitoraggio-aggiornamento.md`** - Verifica il piano di monitoraggio biennale (Vademecum 3.6) e la disciplina di aggiornamento (art. 4 c.1 DM 397/2017: quinquennale + 12 mesi pre-affidamento TPL).

Per il dettaglio operativo di ciascuna sotto-attivita' vedi `SKILL.md` e i singoli file in `tasks/`.

## Installazione

Vedi [README del repo](../../README.md) per le istruzioni di installazione delle skill in Claude Code e Codex CLI.

## Fonti consultate

- DM 4 agosto 2017 n. 397 (Linee guida PUMS) - testo originale.
- DM 28 agosto 2019 n. 396 (modifica del DM 397/2017) - introduce la nuova Tabella 1 con 17 macro-obiettivi e indicatori.
- Vademecum MIMS del 27 settembre 2022 (indirizzi operativi PUMS).

Dettaglio completo, hash SHA256 e URL canonici in `references/sources.yaml`. Estratti curati in `references/estratti/`. Conversione integrale delle fonti in `references/fonti/`.

## Limiti noti

- La skill produce check-list formali, **non un giudizio di merito** sulla qualita' del piano.
- Non valuta la coerenza tra scelte trasportistiche e contesto urbanistico.
- Non simula l'analisi della domanda di mobilita' ne' il monitoraggio degli indicatori.
- Non sostituisce: il giudizio del professionista firmatario, del Tavolo Tecnico PUMS, dell'autorita' competente per la VAS, ne' della competente amministrazione che valuta l'istanza di finanziamento.
- Non cataloga Linee guida regionali integrative (es. Lombardia, Emilia-Romagna). Il professionista firmatario e' tenuto a verificarle separatamente.
- La validazione di un PUMS rispetto agli avvisi specifici per i finanziamenti TRM richiede la lettura dell'avviso pubblicato dal Ministero competente, non coperto da questa skill.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
