# Valutazione dell'esposizione sanzionatoria CBAM (Art. 26)

## Obiettivo

Mappare, per un caso concreto, l'**esposizione sanzionatoria** del dichiarante CBAM autorizzato (o del soggetto privo di qualifica) ai sensi dell'**Art. 26 ▼M1** del Reg. (UE) 2023/956, distinguendo le quattro fattispecie:

- **§1 - mancata o incompleta restituzione** dei certificati entro il 30 settembre (Art. 22 §1 ▼M1) - sanzione per certificato non restituito **identica** a quella per emissioni in eccesso ex Art. 16 §3 Dir. 2003/87/CE (e maggiorata ex Art. 16 §4), nell'anno di importazione;
- **§1bis - riduzione possibile** se l'errore deriva da informazioni inesatte fornite da terzi (verificatore accreditato, persona indipendente che certifica il carbon price);
- **§2 - importazione non consentita o autorizzazione respinta** - sanzione **da 3 a 5 volte** quella del §1;
- **§2bis - non autorizzato che ha superato la soglia** Art. 2bis - sanzione su **tutte** le emissioni incorporate nelle merci importate senza autorizzazione nell'anno civile pertinente; il pagamento dispensa dall'obbligo di dichiarare e restituire; possibile riduzione se superamento ≤ **10 %** della soglia o caso Art. 17 §7bis respinto;
- **§4bis - regola di calcolo** ai fini di §1 e §2: la quantita' di certificati si determina su **massa netta + valori predefiniti** (Allegato IV) **+ adeguamento Art. 31**.

Indicare inoltre le conseguenze doganali correlate (Art. 25 §1 ▼M1 + Avviso ADM 21/10/2025: blocco merci alla frontiera, rifiuto dello sdoganamento) e le procedure operative di ADM in caso di importazione non consentita (Circolare 36/2025).

## Input richiesti

Chiedere all'utente:

1. **Fattispecie sospetta o accertata** (selezione multipla):
   - mancata restituzione entro 30/9 di alcuni o tutti i certificati dovuti (§1);
   - restituzione incompleta dovuta a errore basato su informazioni di terzi - verificatore o persona indipendente (§1bis);
   - importazione senza qualifica di dichiarante CBAM autorizzato (§2 o §2bis);
   - autorizzazione **respinta** dopo aver operato in regime di deroga Art. 17 §7bis (§2 e §2bis ridotta);
   - superamento della soglia di massa Art. 2bis (50 t) **senza** aver presentato/ottenuto la qualifica.
2. **Dati quantitativi del caso**:
   - numero certificati che il dichiarante avrebbe dovuto restituire (se gia' stimato);
   - massa netta delle merci importate "non autorizzate" (per §2bis);
   - eventuale percentuale di superamento della soglia (≤ 10 % o > 10 %);
   - anno civile di importazione (rilevante per fissare l'**importo base** ex Dir. 2003/87/CE Art. 16 §§3-4 in vigore in quell'anno).
3. **Ruolo del soggetto**:
   - importatore stabilito UE / RDI / importatore non stabilito;
   - eventuale ricorso a verificatore accreditato o persona indipendente che ha fornito informazioni inesatte (per la riduzione §1bis).
4. **Stato della procedura**:
   - autorita' competente nazionale (per Italia: MASE) ha gia' contestato? in che forma?
   - ADM ha bloccato merci alla frontiera (Art. 25 §1)?
   - sono stati avviati ricorsi (Art. 25bis §3 ▼M1: ricorso senza effetti sospensivi)?

## Fonti

- Estratto curato: `references/estratti/reg-ue-2023-956-articoli-fase-definitiva.md` sezione E (Controllo doganale, monitoraggio soglia, sanzioni).
- Trascrizione integrale: `references/fonti/reg-ue-2023-956-cbam-consolidato.md` Art. 25, Art. 25bis, Art. 26.
- Considerando di indirizzo: `references/estratti/reg-ue-2025-2083-considerando-chiave.md` considerando 31-32 (riduzione per errori da terzi; non autorizzati e soglia).
- Conseguenze in dogana e procedura ADM: `references/estratti/avviso-adm-conseguenze-non-conformita.md` + `references/estratti/circ-adm-36-2025-codici-taric.md` paragrafo "Conseguenze per importazioni non consentite".
- Rinvio testuale all'importo base: **Direttiva 2003/87/CE Art. 16 §§3-4** (EU ETS), citata come parametro dall'Art. 26 §1 Reg. CBAM (testo nella fonte Reg. 2023/956 consolidato, **non** una fonte autonoma di questa skill).

Articoli da citare:

- **Art. 25 §1 ▼M1** (sdoganamento solo per dichiaranti autorizzati - fatto salvo Art. 2bis).
- **Art. 25bis ▼M1** (monitoraggio soglia, lista importatori > 90 % soglia, decisione formale §3; accordi non genuini di frazionamento = grave violazione §4).
- **Art. 26 §§1, 1bis, 2, 2bis, 3, 4bis ▼M1**.
- **Direttiva 2003/87/CE Art. 16 §3** (€100/quota indicizzato) e **§4** (maggiorazione).
- **Avviso ADM 21/10/2025** (blocco/rifiuto/sanzioni) e **Circolare ADM 36/2025** (procedura territoriale).

## Procedura

### Passo 1 - Qualificare la fattispecie

Per ciascuna voce dell'input, classificare:

| Caso utente                                                       | Norma sanzionatoria |
|-------------------------------------------------------------------|---------------------|
| Dichiarante autorizzato: mancata restituzione entro 30/9          | Art. 26 §1 ▼M1      |
| Dichiarante autorizzato: errore da informazioni di terzi          | Art. 26 §1bis ▼M1 (riduzione) |
| Importazione senza qualifica, sotto la soglia Art. 2bis           | Art. 26 §2 ▼M1 (3-5x §1) |
| Importazione senza qualifica, ha superato la soglia Art. 2bis     | Art. 26 §2bis ▼M1 (su tutte le emissioni dell'anno) |
| Autorizzazione respinta dopo deroga Art. 17 §7bis                 | Art. 26 §2 ▼M1 + §2bis ridotta (Art. 26 §2bis lettera b) |
| Superamento soglia ≤ 10 % senza autorizzazione                    | Art. 26 §2bis ridotta (non inferiore a §1) |
| Accordi non genuini di frazionamento (elusione)                   | Art. 25bis §4 ▼M1 + Art. 26 §2bis ▼M1 |

### Passo 2 - Calcolare la base certificati ai fini sanzionatori (Art. 26 §4bis ▼M1)

**Per §1 e §2**: il numero totale di certificati che avrebbero dovuto essere restituiti si calcola su:

```
N_cert = (massa netta merci importate) * (valori predefiniti Allegato IV) - adeguamento Art. 31
```

con i **valori predefiniti** ai sensi dell'Allegato IV punto 4.1 ▼M1 (intensita' media paese esportatore + maggiorazione; quando manca, 10 paesi con intensita' piu' elevate). La skill non calcola Art. 31 (chiedere all'utente o lasciare flag).

**Per §2bis**: tutte le emissioni incorporate nelle merci importate **senza autorizzazione** nell'anno civile pertinente. Stessa metodologia (valori predefiniti + adeguamento Art. 31).

### Passo 3 - Determinare l'importo unitario di sanzione

L'importo unitario per "certificato non restituito" e' fissato dall'**Art. 16 §3 Direttiva 2003/87/CE** (€100/quota indicizzato all'IPC EU dal 2013) e dalla maggiorazione **§4** della stessa direttiva, **applicabile nell'anno di importazione delle merci** (Art. 26 §1 Reg. CBAM ▼M1).

La skill **non determina l'importo numerico**: cita la regola di rinvio e indica al professionista che la cifra esatta per l'anno specifico va consultata presso l'autorita' competente (MASE) e/o nella documentazione ETS (Commissione UE). Per il 2024 l'importo era ~€124/quota; per il 2026 sara' aggiornato dalla Commissione.

### Passo 4 - Applicare il moltiplicatore (§2)

Se la fattispecie e' "importazione non consentita o autorizzazione respinta" (Art. 26 §2 ▼M1):

```
Sanzione_§2 = N_cert * Importo_unitario * k     con k in [3, 5]
```

Il moltiplicatore `k` si determina caso per caso (autorita' competente), tenuto conto di:
- durata del comportamento;
- gravita';
- portata;
- natura intenzionale;
- reiterazione;
- cooperazione con l'autorita'.

La skill **non** sceglie il `k`: presenta il range [3x, 5x] della sanzione base.

### Passo 5 - Applicare il regime speciale (§2bis)

Se la fattispecie e' "non autorizzato che ha superato la soglia":

```
Base_§2bis = (tutte le emissioni incorporate nell'anno) * Importo_unitario
```

**Riduzione possibile** (Art. 26 §2bis lettere a-b ▼M1):

- **lettera a**: superamento della soglia di massa netta **≤ 10 %** (rispetto ai 50 t Allegato VII);
- **lettera b**: caso Art. 17 §7bis respinto (domanda presentata entro 31/3/2026 e poi non accolta dall'autorita').

La sanzione ridotta resta "effettiva, proporzionata e dissuasiva" e **non puo' essere inferiore** alla sanzione §1. Il pagamento della sanzione §2bis **dispensa** dall'obbligo di presentare la dichiarazione e restituire i certificati per quelle importazioni (Art. 26 §2bis ▼M1 + Considerando 32 Reg. 2025/2083; deroga al §3).

### Passo 6 - Considerare le conseguenze doganali (Art. 25 §1 + Avviso ADM)

Indipendentemente dal regime sanzionatorio Art. 26, ricordare la triplice conseguenza dall'**Avviso ADM 21/10/2025**:

- **blocco delle merci alla frontiera**;
- **rifiuto dello sdoganamento**;
- **applicazione di sanzioni**.

E la procedura della **Circolare ADM 36/2025**: le articolazioni territoriali di ADM "vieteranno, fatte salve le citate deroghe, tutte le importazioni effettuate da soggetti non autorizzati"; "le merci oggetto di importazione non consentita dovranno essere fermate e dovra' immediatamente essere informata l'autorita' competente ai fini dell'eventuale irrogazione delle sanzioni individuate dall'art. 26 del Regolamento". Restano salve ulteriori sanzioni doganali (CDU).

### Passo 7 - Evidenziare la responsabilita' del RDI

Se il soggetto e' RDI: stesse sanzioni dell'importatore (Art. 5 §2bis ▼M1; Considerando 8 Reg. 2025/2083). Eccezione: non sanzionato se **non ha accettato** di agire come dichiarante per un importatore stabilito UE.

### Passo 8 - Produrre il report

Strutturare un report markdown con:

1. **Profilo del caso** (soggetto, EORI, anno civile, fattispecie qualificata Art. 26 §X).
2. **Base di calcolo** (Art. 26 §4bis): massa netta, valori predefiniti applicati, adeguamento Art. 31 (variabile).
3. **Sanzione base §1** (importo unitario rinviato a Dir. 2003/87/CE Art. 16 §§3-4 dell'anno di importazione).
4. **Eventuale moltiplicatore §2** (range 3x-5x) con motivazione discrezionale rinviata all'autorita'.
5. **Eventuale §2bis** (su tutte le emissioni dell'anno) con riduzione lettera a (≤ 10 %) o lettera b (17 §7bis respinta).
6. **Eventuale riduzione §1bis** se errore da informazioni di terzi.
7. **Conseguenze doganali** (Art. 25 §1 + Avviso ADM 21/10/2025 + Circolare ADM 36/2025).
8. **Punti che richiedono giudizio del professionista**: scelta del moltiplicatore §2, qualificazione di eventuale elusione (Art. 27 §2 lettera b), determinazione dell'adeguamento Art. 31, strategia di ricorso (Art. 25bis §3, ricorso senza effetti sospensivi).
9. **Avvertenza standard** + rinvio a `references/fonti/reg-ue-2023-956-cbam-consolidato.md` per il riscontro testuale di Art. 25, 25bis, 26.

## Note sulla quantificazione

La skill **non produce stime numeriche definitive di sanzione** senza un dato di prezzo (importo unitario Dir. 2003/87/CE Art. 16 §§3-4 dell'anno di importazione) confermato dal professionista. Quando l'utente fornisce un importo, la skill calcola:

- `Sanzione_§1_min = N_cert * importo_unitario`;
- `Sanzione_§2 in [3 * Sanzione_§1, 5 * Sanzione_§1]`;
- `Sanzione_§2bis = (tutte le emissioni dell'anno) * importo_unitario` (con eventuale riduzione lettera a/b da fissare dal professionista, non inferiore a Sanzione_§1).
