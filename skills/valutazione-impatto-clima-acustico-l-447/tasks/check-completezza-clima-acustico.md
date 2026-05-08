# Task: check completezza valutazione previsionale di clima acustico

## Obiettivo

Verificare la completezza dei contenuti minimi di una **valutazione
previsionale di clima acustico** redatta ai sensi dell'art. 8 c. 3 della
L. 26 ottobre 1995 n. 447, da allegare al titolo abilitativo (PdC, SCIA)
per la realizzazione delle seguenti tipologie di insediamenti:

- a) scuole e asili nido;
- b) ospedali;
- c) case di cura e di riposo;
- d) parchi pubblici urbani ed extraurbani;
- e) nuovi insediamenti residenziali prossimi alle opere di cui al
  c. 2 (aeroporti, strade A-F, discoteche, circoli/pubblici esercizi
  con macchinari rumorosi, impianti sportivi, ferrovie).

Differenza chiave rispetto al check di "impatto acustico" (c. 2/c. 4):
nel **clima acustico** il sito di progetto e' il **ricettore** (non la
sorgente). L'oggetto della valutazione e' la **rumorosita' attesa al
ricettore** (sorgenti gia' esistenti e prevedibili) per verificare se
la futura realizzazione dell'insediamento sensibile sia compatibile
con i valori limite della classe acustica della zona.

L'output e' una lista strutturata di item con esito **OK / mancante /
da verificare / non applicabile** e azione richiesta al professionista.

## Input richiesti

Chiedere all'utente, se non gia' fornito:

1. **Tipologia di insediamento sensibile** (scuola/asilo nido,
   ospedale, casa di cura/riposo, parco pubblico, insediamento
   residenziale prossimo a opere c. 2) - per attivare i criteri
   specifici della categoria.
2. **Documento da rivedere**: testo, indice o sintesi della
   valutazione di clima acustico oggetto della verifica.
3. **Ubicazione** (comune, indirizzo) e **classe acustica** del lotto
   secondo la classificazione comunale (art. 6 c. 1 lett. a) L. 447/1995),
   se disponibile. Se il comune non ha adottato la classificazione,
   regime transitorio DPCM 1/3/1991 (art. 8 c. 1 DPCM 14/11/1997).
4. **Sorgenti acustiche rilevanti gia' esistenti o programmate** in
   prossimita' del sito (es. strade, ferrovie, attivita' produttive,
   pubblici esercizi). Per ciascuna: tipologia e distanza approssimata.
5. **Periodo d'uso previsto** dell'insediamento (diurno, notturno,
   continuo) - rileva soprattutto per ospedali e residenze.
6. **Eventuali fasce di pertinenza acustica** delle infrastrutture dei
   trasporti adiacenti (DPR 459/1998 ferroviario, DPR 142/2004
   stradale): solo in termini di **presenza/assenza**; il dimensionamento
   delle fasce e' fuori scope.

## Fonti

Le citazioni provengono dagli estratti seguenti:

- `references/estratti/legge-447-1995-art-8.md` per l'art. 8 c. 3
  (clima acustico), l'art. 2 c. 1 lett. e-h (definizioni di immissione,
  emissione, qualita'), l'art. 4 c. 1 lett. l) (rinvio Regioni).
- `references/estratti/dpcm-14-11-1997-valori-limite.md` per le
  Tabelle A (classi), C (valori limite assoluti di immissione) e D
  (valori di qualita'); art. 4 (valori limite differenziali, ambienti
  abitativi); art. 6 (valori di attenzione).
- `references/estratti/dm-16-03-1998-tecniche-misurazione.md` per
  strumentazione (classe 1), tecniche di misura (allegato B), modalita'
  di misurazione del rumore stradale e ferroviario (allegato C),
  modalita' di presentazione (allegato D).

## Procedura

Per ciascuno dei punti sotto, cerca nel documento dell'utente se il
contenuto e' presente, parziale o assente. Restituisci esito
**OK / mancante / parziale / da verificare / non applicabile** con
riferimento normativo e azione consigliata.

### 1. Identificazione e qualificazione del professionista

- 1.1 Identificazione TCAA firmatario (cognome, nome, numero elenco
  nazionale o regionale ai sensi dell'art. 21 del D.Lgs. 17 febbraio
  2017 n. 42).
- 1.2 Identificazione del progettista incaricato dell'opera (per la
  parte di mitigazione, se prevista).
- 1.3 Identificazione del committente e della pratica edilizia (PdC
  o SCIA, numero protocollo se gia' assegnato).

### 2. Inquadramento territoriale del ricettore

- 2.1 Indirizzo, particella catastale, coordinate.
- 2.2 **Classe acustica** della zona di intervento secondo la
  classificazione comunale (art. 6 c. 1 lett. a) L. 447/1995).
- 2.3 Classe acustica delle zone confinanti (per verifica di
  accostabilita' fra classi: criteri operativi rinviati alla legge
  regionale ai sensi dell'art. 4 c. 1 lett. l) L. 447/1995).
- 2.4 Estratto cartografico con perimetro del lotto, ubicazione dei
  ricettori (aule, camere, ambienti riposo, aree gioco) e ubicazione
  delle sorgenti acustiche significative.
- 2.5 Per insediamenti del c. 3 lett. e) (residenziali prossimi a
  opere c. 2): identificazione delle opere c. 2 limitrofe e distanza.
- 2.6 In presenza di **infrastrutture dei trasporti** (strade,
  ferrovie): segnalare la **presenza** delle relative fasce di
  pertinenza acustica e rinviare al rispettivo decreto attuativo
  (DPR 459/1998 per la ferrovia, DPR 142/2004 per la strada). Il
  dimensionamento delle fasce non e' oggetto di questa skill.

### 3. Descrizione delle sorgenti gia' esistenti o programmate

Per ciascuna sorgente significativa al ricettore:

- 3.1 Tipologia (sorgente fissa, infrastruttura dei trasporti).
- 3.2 Caratteristiche operative rilevanti (per attivita': orari di
  funzionamento; per strada: traffico medio giornaliero o categoria
  D.Lgs. 285/1992; per ferrovia: tratto di linea, traffico).
- 3.3 Distanza dal ricettore e configurazione geometrica
  (schermature, ostacoli, vegetazione).
- 3.4 Eventuali misure fonometriche **gia' disponibili** o pianificate
  (data, durata, posizione, fonometro - vedi check punto 6).

### 4. Verifica rispetto ai valori limite della classe acustica

- 4.1 **Valori limite assoluti di immissione** (Tabella C DPCM
  14/11/1997, art. 3): confronto fra rumore previsto al ricettore
  (Leq in dB(A) per i periodi diurno 06:00-22:00 e notturno
  22:00-06:00) e i valori della classe del lotto. Riferimento
  numerico: cfr. `references/estratti/dpcm-14-11-1997-valori-limite.md`
  Tabella C.
- 4.2 **Valori di qualita'** (Tabella D DPCM 14/11/1997, art. 7):
  obiettivi a tendere ai sensi dell'art. 2 c. 1 lett. h) L. 447/1995.
  Per insediamenti sensibili (scuole, ospedali, case di cura) la
  valutazione del clima acustico deve segnalare se i valori previsti
  si avvicinano o superano i valori di qualita', anche se non si
  superano i limiti di immissione.
- 4.3 **Valori di attenzione** (DPCM 14/11/1997 art. 6): la skill
  segnala l'obbligo di tenerne conto solo quando la valutazione
  evidenzia rumore prevedibile gia' molto vicino al limite di
  immissione - rinvio diretto all'art. 6 del DPCM.
- 4.4 **Criterio differenziale** (DPCM 14/11/1997 art. 4): il limite
  differenziale (5 dB diurno, 3 dB notturno) si applica all'**interno
  degli ambienti abitativi**. Per l'insediamento sensibile in fase
  previsionale, va verificato se le sorgenti previste hanno
  caratteristiche tali da poterlo violare a finestre aperte/chiuse;
  non si applica nelle aree classe VI ne' nei casi dell'art. 4 c. 2
  (effetto trascurabile). Per la metodologia dei descrittori
  rilevati, rinvio a `references/estratti/dm-16-03-1998-tecniche-misurazione.md`
  (allegato B).
- 4.5 Se il comune **non ha adottato la classificazione acustica**:
  applicare regime transitorio DPCM 1/3/1991 ai sensi dell'art. 8
  c. 1 del DPCM 14/11/1997 e rinvio alla legge regionale per i
  criteri di applicazione transitoria.

### 5. Sorgenti che ricadono sotto regimi speciali

- 5.1 Strade: se infrastruttura adiacente al ricettore, rinvio al
  **DPR 142/2004** (fasce di pertinenza, valori limite specifici per
  classe di strada e per ricettori sensibili). I valori limite del
  DPCM 14/11/1997 **non si applicano all'interno delle fasce di
  pertinenza** (DPCM 14/11/1997 art. 3 c. 2). Lo skill **non sostituisce**
  la verifica puntuale della fascia.
- 5.2 Ferrovie: rinvio al **DPR 459/1998** (fasce di pertinenza,
  valori limite specifici, ricettori sensibili). Lo skill **non
  sostituisce** la verifica puntuale del DPR. Le misure per il rumore
  ferroviario seguono l'allegato C DM 16/3/1998 (tempo di misura T_M
  >= 24 h).
- 5.3 Aeroporti: rinvio al regime proprio (zonizzazione e fasce di
  rispetto - decreti attuativi; fuori scope di questa skill).

### 6. Metodologia di valutazione previsionale e (eventuali) misure

- 6.1 Descrizione del **modello previsionale** o della procedura di
  calcolo utilizzata (es. ISO 9613-2 per propagazione in aria libera,
  modelli specifici per traffico stradale o ferroviario). La skill
  non valida i parametri del modello.
- 6.2 Per misure fonometriche eseguite a supporto della valutazione
  (caratterizzazione del rumore residuo): conformita' al DM
  16/3/1998:
  - 6.2.1 Strumentazione classe 1 (DM 16/3/1998 art. 2 c. 1)
    conforme a EN 60651/1994 + EN 60804/1994; calibratore EN 60942/1998;
    filtri EN 61260/1995; verifica taratura biennale presso laboratorio
    di taratura SIT.
  - 6.2.2 Calibrazione **prima e dopo** ogni ciclo di misura, scarto
    massimo +/- 0.5 dB (DM 16/3/1998 art. 2 c. 2).
  - 6.2.3 Indicazioni di posizionamento del microfono (1.5 m dal
    piano di calpestio, almeno 1 m da superfici riflettenti;
    condizioni di misura in esterno descritte all'allegato B DM
    16/3/1998).
  - 6.2.4 Condizioni meteo durante le misure: vento <= 5 m/s (allegato
    B DM 16/3/1998 punto 6 e 7), assenza di precipitazione, fenomeno
    di inversione termica solo se rilevante.
  - 6.2.5 Tempo di misura T_M coerente con allegato A DM 16/3/1998
    e, per ferrovie/strade, allegato C DM 16/3/1998 (T_M >= 24 h
    ferroviario; T_M >= 1 settimana stradale - vedi estratto allegato C).
  - 6.2.6 Eventuali fattori correttivi K_I impulsivita' (3 dB),
    K_T tonalita' (3 dB), K_B bassa frequenza (3 dB) e criteri di
    riconoscimento (allegato A e B DM 16/3/1998).
- 6.3 Risultati presentati secondo allegato D del DM 16/3/1998
  (rapporto fonometrico): identificazione del tecnico, della
  strumentazione e della catena di misura, dello stato di taratura,
  delle condizioni meteorologiche, dei descrittori rilevati, della
  procedura di calibrazione.

### 7. Mitigazione progettuale (se richiesta)

Se la verifica al punto 4 evidenzia non conformita' al limite di
immissione o avvicinamento al limite tale da richiedere intervento:

- 7.1 Descrizione delle **misure di mitigazione** previste (barriere
  acustiche, schermature, isolamento di facciata, distribuzione interna
  degli ambienti sensibili rispetto alla sorgente, requisiti acustici
  passivi degli edifici - per quest'ultimo punto rinvio al DPCM 5/12/1997,
  fuori scope di questa skill).
- 7.2 Stima dell'efficacia attesa della mitigazione e nuova verifica
  rispetto al limite.
- 7.3 Se la mitigazione richiede provvedimenti di terzi (es. proprietario
  di infrastruttura adiacente): segnalare la non disponibilita' del
  progetto a risolvere autonomamente la non conformita' e rinviare
  all'amministrazione (art. 6 c. 1 lett. d) L. 447/1995, controllo
  comunale).

### 8. Conformita' formale

- 8.1 **Firma** del TCAA e del progettista, con indicazione del
  numero di iscrizione (rispettivamente: elenco nazionale TCAA D.Lgs.
  42/2017; ordine professionale di competenza).
- 8.2 **Data** della valutazione coerente con la fase del procedimento
  (deposito a corredo del titolo abilitativo).
- 8.3 **Allegati** dichiarati e presenti: planimetrie, foto del sito,
  estratti di mappa, eventuali certificati di taratura, eventuali
  rapporti di misura completi.
- 8.4 **Rinvio alla legge regionale** in materia di inquinamento
  acustico (art. 4 c. 1 lett. l) L. 447/1995): la skill segnala
  l'obbligo di verificarla nella regione di interesse, senza quotarne
  i contenuti.
- 8.5 **Rinvio al regolamento comunale** in materia di inquinamento
  acustico (art. 6 c. 2 L. 447/1995): la skill segnala l'obbligo di
  verificarlo presso l'Ufficio Ambiente del comune.

## Output

Restituire una lista markdown con un item per ciascun punto (1.1,
1.2, 2.1, ...). Ogni item deve avere esattamente questi campi:

| Campo | Significato |
|-------|-------------|
| Item | "1.1 Identificazione TCAA firmatario" |
| Esito | OK / mancante / parziale / da verificare / non applicabile |
| Riferimento normativo | citazione puntuale (art., comma, decreto) |
| Azione | cosa deve fare il professionista |

E un blocco finale con:

- **Sintesi** (2-3 righe) dei punti BLOCCANTI (mancante o parziale su
  contenuti normativi obbligatori) e dei punti DA VERIFICARE
  (richiedono la verifica del professionista, es. rinvio LR/regolamento).
- **Rinvio alla legge regionale** applicabile (art. 4 c. 1 lett. l)
  L. 447/1995).
- **Rinvio al regolamento comunale** in materia di inquinamento
  acustico (art. 6 c. 2 L. 447/1995).
- **Rinvio al testo vigente** L. 447/1995, DPCM 14/11/1997 e DM
  16/3/1998 (Normattiva).
- **Rinvio al TCAA firmatario** della relazione e al progettista per
  la parte progettuale.

## Limiti del task

- Non valida i risultati numerici dei modelli previsionali.
- Non quota i valori limite specifici delle infrastrutture dei
  trasporti (DPR 459/1998, DPR 142/2004): rinvio al testo vigente.
- Non sostituisce la verifica della classificazione acustica comunale
  ne' della legge regionale.
- Non riproduce in numeri parametri o coefficienti correttivi (K_I,
  K_T, K_B): solo riferimenti strutturali al DM 16/3/1998 allegati
  A e B.
- Non e' una decisione amministrativa: il responsabile del
  procedimento del comune ha l'ultima parola sulla compatibilita'
  acustica del progetto.
