# AGENTS.md - trasmittanza-termica-opache-dm2015

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Calcolo code-driven della **trasmittanza termica U** di strutture opache
stratificate (pareti verticali, coperture, pavimenti) e **verifica dei limiti
per zona climatica del DM 26/06/2015** (requisiti minimi). Target: ingegneri,
architetti, termotecnici, certificatori energetici (contesto APE / Ecobonus /
ristrutturazione).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-26-06-2015-requisiti-minimi**: DM 26/06/2015 (MiSE), GU n. 162/2015 S.O.
  39 (hash reale b69e130f..., riproducibile, host gazzettaufficiale.it) -
  trascrizione di Allegato 1 par. 5.2, Appendice A Tab. 1-5, Appendice B Tab.
  1-4 in `references/fonti/dm-26-06-2015-requisiti-minimi.md`.

Estratto operativo con le tabelle: `references/estratti/dm-2015-limiti-trasmittanza.md`.

## Punti chiave (verificati sul testo)

- **Metodo U = 1/R_tot** con R_tot = R_si + somma(s/lambda) + R_se: fisica
  tecnica di pubblico dominio, **NON** nel decreto.
- **Il DM fornisce solo i valori limite di U** per zona climatica:
  - Appendice B (edifici esistenti in riqualificazione, contesto Ecobonus):
    Tab. 1 pareti verticali - AeB 0,45/0,40; C 0,40/0,36; D 0,36/0,32;
    E 0,30/0,28; F 0,28/0,26 (colonne 2015 / 2021);
  - Appendice A (edificio di riferimento, nuove costruzioni / ristrutt.
    importanti): Tab. 1 pareti - AeB 0,45/0,43; C 0,38/0,34; D 0,34/0,29;
    E 0,30/0,26; F 0,28/0,24 (2015 / 2019-2021).
- **Incremento +30%** dei limiti App. B (Cap. 5 par. 5.2) per isolamento
  dall'interno o in intercapedine.
- **Caveat cogenti**: i limiti del DM **includono i ponti termici** (la U 1D
  no -> verifica preliminare); verso ambienti non climatizzati -> fattore di
  correzione UNI/TS 11300-1; controterra -> trasmittanza equivalente UNI EN ISO
  13370.
- **lambda dei materiali e R_si/R_se NON sono nel decreto** (UNI/TS 11300, UNI
  EN ISO 6946, a pagamento): sono input dell'utente, mai riprodotti/inventati.

## Convenzioni specifiche

### Cosa NON fare
- Non calcolare a mano: usare sempre `tasks/lib/trasmittanza.py`.
- Non inventare/stimare i lambda dei materiali ne' le R_si/R_se: input utente.
- Non riprodurre il testo o i valori delle norme UNI a pagamento.
- Non attribuire al DM il metodo di calcolo o i lambda: il DM da' solo i limiti.
- Non presentare la verifica 1D come completa: i limiti includono i ponti
  termici, il calcolo 1D no -> sempre "preliminare".
- Non calcolare i serramenti per stratigrafia (Uw: UNI EN ISO 10077, dato del
  produttore): il modulo rifiuta `chiusura_trasparente`.
- Non applicare l'incremento +30% al regime `edificio_riferimento` (solo App. B).
- Non confondere Appendice A (edificio di riferimento) con Appendice B
  (riqualificazione): scegliere in base al regime.

### Cosa fare
- Citare la tabella precisa del DM (Appendice, numero, zona, anno) per il limite.
- Esporre il dettaglio delle resistenze e la tabella degli strati.
- Riportare integralmente le avvertenze del modulo.
- Chiudere con il rinvio alla relazione tecnica ex art. 8 D.Lgs. 192/2005.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con termotecnico, confronto con
  software di calcolo energetico - es. su casi UNI/TS 11300).

## Stato attuale

- Versione: 0.1.0-alpha (closes #29)
- Task files: 1 (`calcola-trasmittanza.md`) + modulo `tasks/lib/trasmittanza.py`
  con 19 test.
- Esempi: 1 conforme (cappotto EPS zona E) + 1 non conforme (muratura piena zona
  D con incremento +30% isolamento interno).
