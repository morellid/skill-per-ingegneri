# Estratto operativo - gap analysis ABSC (Misure Minime ICT PA, Circ. AgID 2/2017)

> Checklist parafrasata dalla fonte in `references/fonti/circolare-agid-2-2017.md`. Il
> livello ESATTO (Minimo/Standard/Alto) di ciascun controllo va letto sulle tabelle in
> formato grafico del PDF ufficiale. NON sostituisce l'assessment tecnico.

## 0. Inquadramento (artt. 1-3)

- [ ] **Destinatario**: l'ente rientra tra i soggetti dell'**art. 2 c.2 del C.A.D.**
      (PA e assimilati)? (art. 2).
- [ ] **Responsabile dell'attuazione** individuato: il responsabile della struttura per
      l'organizzazione/innovazione/tecnologie (art. 17 C.A.D.) o dirigente designato
      (art. 3).
- [ ] **Livello obiettivo** per (sotto)insiemi omogenei di sistemi: Minimo (obbligatorio),
      Standard (base), Alto (target). Le amministrazioni NSC: almeno "standard".

## 1. Gap analysis sugli 8 gruppi ABSC

Per **ciascun** gruppo, valutare i controlli (ABSC_ID `x.y.z`) e registrare livello,
stato di attuazione, evidenze e azioni:

- [ ] **ABSC 1 - Inventario dispositivi**: gestione attiva dei dispositivi hardware in
      rete; accesso solo ai dispositivi autorizzati.
- [ ] **ABSC 2 - Inventario software**: gestione attiva del software; esecuzione del
      solo software autorizzato (whitelisting).
- [ ] **ABSC 3 - Configurazioni sicure**: configurazioni di sicurezza di laptop, server,
      workstation con controllo delle variazioni.
- [ ] **ABSC 4 - Vulnerabilita'**: valutazione e correzione continua delle vulnerabilita'.
- [ ] **ABSC 5 - Privilegi di amministratore**: uso appropriato delle utenze privilegiate.
- [ ] **ABSC 8 - Difese contro i malware**: controllo di installazione/diffusione/
      esecuzione di codice maligno.
- [ ] **ABSC 10 - Copie di sicurezza**: backup e ripristino delle informazioni critiche.
- [ ] **ABSC 13 - Protezione dei dati**: prevenzione dell'esfiltrazione, riservatezza e
      integrita' dei dati rilevanti.

Per ogni controllo indicare la Subcategory **FNSC** (Framework Nazionale Cyber Security)
gia' associata nella tabella, come raccordo.

## 2. Livelli (come leggerli)

- [ ] **Minimo**: controlli **obbligatori** (soglia sotto cui nessuna PA puo' scendere).
- [ ] **Standard**: base di riferimento nella maggior parte dei casi.
- [ ] **Alto**: obiettivo a cui tendere (strutture complesse).
- [ ] Il flag esatto per ogni `ABSC_ID` e' nelle **colonne della tabella (PDF, pagg.
      ~68-73)**: non desumerlo, leggilo.

## 3. Modulo di implementazione (art. 4, Allegato 2)

- [ ] Riportare **sinteticamente** come ciascuna misura e' implementata.
- [ ] **Firma digitale con marcatura temporale** del responsabile (art. 3) e del
      responsabile legale della struttura.
- [ ] **Conservare** il modulo; in caso di **incidente** trasmetterlo al **CERT-PA** con
      la segnalazione.
- [ ] Rispetto dei **tempi** (la circolare fissava l'attuazione entro il 31/12/2017;
      verificare lo stato per gli enti non ancora adeguati) (art. 5).

## Avvertenze

- La skill **imposta** la gap analysis: lo **stato reale** dei controlli si accerta con
  analisi tecnica dei sistemi.
- Per alcuni soggetti si aggiungono obblighi piu' recenti (**NIS2, D.Lgs 138/2024**): le
  MMS-PA restano la base ma non esauriscono il quadro.
