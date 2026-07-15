# Estratto operativo - Specifiche tecniche ICT negli appalti PA

> Sintesi operativa a supporto della redazione delle specifiche tecniche di una
> procedura ICT e della fase di analisi comparativa/acquisto software.
> Ogni riga rinvia alla fonte trascritta in `references/fonti/`. Non sostituisce
> la lettura del Codice, del CAD e delle Linee guida AgID.

## 1. Prima della gara: analisi comparativa delle soluzioni (art. 68 CAD)

Prima di acquisire programmi informatici (o parti di essi), la PA effettua una
**valutazione comparativa tecnico-economica** tra le soluzioni disponibili sul
mercato (art. 68, c. 1, lett. a-f):

| Soluzione | Rif. |
|---|---|
| a) software sviluppato per conto della PA | art. 68 c.1 a) |
| b) riutilizzo di software sviluppato per conto della PA | art. 68 c.1 b) |
| c) software libero o a codice sorgente aperto | art. 68 c.1 c) |
| d) software fruibile in modalita' cloud computing | art. 68 c.1 d) |
| e) software proprietario mediante licenza d'uso | art. 68 c.1 e) |
| f) combinazione delle precedenti | art. 68 c.1 f) |

**Criteri della valutazione comparativa** (art. 68, c. 1-bis):
- a) costo complessivo (acquisto, implementazione, mantenimento, supporto);
- b) livello di utilizzo di **formati e interfacce aperti** e di **standard** per
  interoperabilita' e cooperazione applicativa;
- c) garanzie del fornitore su sicurezza, protezione dati personali, livelli di
  servizio.

**Ricorso al proprietario** (art. 68, c. 1-ter): consentito solo se dalla
valutazione risulta **motivatamente** l'impossibilita' di accedere a soluzioni
gia' disponibili nella PA o a software libero/open source adeguati. Modalita' e
criteri definiti dall'AgID (rinvio, non riprodotto).

## 2. Riuso e titolarita' dei diritti nel capitolato (art. 69 CAD)

- Software realizzato **su specifiche indicazioni del committente pubblico**:
  obbligo di rendere disponibile il **codice sorgente** con documentazione, in
  repertorio pubblico sotto **licenza aperta**, in uso gratuito ad altre PA
  (salvo motivate ragioni di ordine/sicurezza pubblica, difesa, elezioni) -
  art. 69 c. 1.
- Nel **capitolato o nelle specifiche di progetto** e' previsto - salvo che
  risulti eccessivamente oneroso per comprovate ragioni tecnico-economiche - che
  l'amministrazione committente sia **titolare di tutti i diritti** sui programmi
  e servizi ICT appositamente sviluppati per essa - art. 69 c. 2.
- Pubblicazione di codice, documentazione e descrizione tecnico-funzionale sulle
  piattaforme individuate dall'AgID - art. 69 c. 2-bis.

## 3. Formulazione delle specifiche tecniche (art. 79 + allegato II.5)

Le specifiche tecniche sono inserite nei documenti di gara (all. II.5, Parte II,
A, punto 1) e devono:
- consentire **pari accesso** agli operatori e non creare ostacoli
  ingiustificati alla concorrenza (punto 4);
- tenere conto dell'**accessibilita' per le persone con disabilita'** negli
  appalti destinati a persone fisiche (punto 3).

**Modalita' di formulazione** (all. II.5, Parte II, A, punto 5) - una tra:
- a) **prestazioni / requisiti funzionali** (parametri sufficientemente precisi);
- b) **riferimento a norme** (ordine di preferenza: norme che recepiscono norme
  europee -> valutazioni tecniche europee -> **specifiche tecniche comuni** (TIC)
  -> norme internazionali -> altri riferimenti -> norme nazionali). Ciascun
  riferimento contiene l'espressione **"o equivalente"**;
- c) prestazioni/requisiti (a) con riferimento alle norme (b) come presunzione di
  conformita';
- d) mix di (a) e (b) per caratteristiche diverse.

**Divieto di marchi/brevetti** (all. II.5, Parte II, A, punto 6): le specifiche
non possono menzionare fabbricazione/provenienza determinata, marchio, brevetto,
tipo, origine che favoriscano/eliminino imprese o prodotti; ammesso **in via
eccezionale** solo se non e' possibile una descrizione precisa altrimenti, sempre
con **"o equivalente"**.

**Equivalenza** (all. II.5, punti 7-8): non si puo' escludere un'offerta che
ottempera in modo equivalente; l'offerente prova l'equivalenza con qualsiasi
mezzo appropriato, compresi i mezzi di prova dell'art. 105 del Codice.

**Definizioni utili (settore TIC)** (all. II.5, Parte I): "specifica tecnica
comune" = specifica tecnica nel settore delle TIC elaborata ex artt. 13-14 Reg.
(UE) 1025/2012.

## 4. Etichettature (art. 80 + allegato II.5, Parte II, B)

L'etichettatura specifica (caratteristiche ambientali/sociali) puo' essere
richiesta come mezzo di prova se (all. II.5, B, punto 1, lett. a-e): requisiti
connessi all'oggetto, oggettivi/verificabili/non discriminatori, stabiliti con
procedura aperta, accessibili, stabiliti da terzi indipendenti. Vanno accettate
etichettature **equivalenti** e altri mezzi di prova (punti 2-3).

## 5. Confini della skill (cosa NON copre)

- Non redige il capitolato/disciplinare completo ne' sceglie la soluzione.
- Non definisce i **criteri di aggiudicazione / OEPV** (art. 108 del Codice):
  vedi skill `oepv-valutatore-offerte-tecniche`.
- Non riproduce le **Linee guida AgID** (analisi comparativa, riuso,
  publiccode.yml) ne' le norme tecniche citate (a pagamento).
- Non calcola importi, base d'asta o soglie.
