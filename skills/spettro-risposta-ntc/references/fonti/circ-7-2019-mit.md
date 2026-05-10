# Circolare MIT n. 7 del 21/01/2019 - Trascrizione verbatim paragrafi rilevanti

**Fonte**: Circolare del Ministero delle Infrastrutture e dei Trasporti n. 7 del 21 gennaio 2019 -
"Istruzioni per l'applicazione dell'aggiornamento delle Norme tecniche per le costruzioni"
**Pubblicazione**: Supplemento Ordinario n. 5 alla Gazzetta Ufficiale n. 35 dell'11 febbraio 2019
**URL**: https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg
**PDF GU**: https://www.gazzettaufficiale.it/eli/gu/2019/02/11/35/so/5/sg/pdf
**Data accesso**: 2026-05-10
**SHA256**: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
**Licenza**: pubblico dominio

Trascrizione verbatim (o parafrasi fedele con indicazione pagina/riga del testo estratto con pdftotext)
dei paragrafi rilevanti per la skill `spettro-risposta-ntc`.
Le righe di riferimento sono quelle del testo estratto con `pdftotext` dal PDF originale.

---

## C2.4 - Vita nominale di progetto, classi d'uso e periodo di riferimento

### C2.4.1 - Vita nominale di progetto

*(p. 37 del S.O. n. 5; estratto pdftotext righe 3583-3609)*

> Al punto 2.4.1 delle norme, anche ai fini delle verifiche sismiche, e' definita la "vita nominale di progetto" di un'opera, VN, che e'
> convenzionalmente definita come il numero di anni nel quale l'opera, purche' ispezionata e manutenuta come previsto in
> progetto, mantenga i livelli prestazionali e svolga le funzioni per i quali e' stata progettata.
> Le opere sono classificate in tre differenti categorie, per ciascuna delle quali viene fissato il valore minimo di VN: 10 anni per le
> strutture temporanee e provvisorie e quelle in fase di costruzione, 50 anni per le opere con livelli di prestazione ordinari, 100 anni
> per le opere con livelli di prestazione elevati.

### C2.4.3 - Periodo di riferimento per l'azione sismica

*(p. 38-39 del S.O. n. 5; estratto pdftotext righe 3679-3750)*

> Il periodo di riferimento VR di una costruzione, valutato moltiplicando la vita nominale VN (espressa in anni) per il coefficiente
> d'uso della costruzione CU (VR = VN * CU), riveste notevole importanza, in quanto, assumendo che la legge di ricorrenza dell'azione
> sismica sia un processo poissoniano, e' utilizzato per valutare, fissata la probabilita' di superamento PVR corrispondente allo stato
> limite considerato (Tabella 3.2.I della NTC), il periodo di ritorno TR dell'azione sismica cui fare riferimento per la verifica.

**Tab. C2.4.I - Intervalli di valori attribuiti a VR al variare di VN e CU**

*(estratto pdftotext righe 3688-3730)*

| VITA NOMINALE VN | CU classe I | CU classe II | CU classe III | CU classe IV |
|---|---|---|---|---|
| <= 10 | 35 | 35 | 35 | 35 |
| >= 50 | >= 35 | >= 50 | >= 75 | >= 100 |
| >= 100 | >= 70 | >= 100 | >= 150 | >= 200 |

**Nota operativa**: La tabella C2.4.I della Circolare mostra che per VN <= 10 anni (costruzioni temporanee,
CU min = 0.7, VR = 10 * 0.7 = 7 anni) VR viene assunto pari a 35 anni per tutte le classi d'uso.
Questo rappresenta il VR minimo applicabile, coerente con il limite inferiore del reticolo INGV
(TR_min = 30 anni). Il VR minimo = 35 anni non e' enunciato esplicitamente come formula nella NTC 2018
par. 2.4.3, ma emerge dall'applicazione della Tabella C2.4.I della Circolare.

---

## C3.2 - Azione sismica

*(p. 42 del S.O. n. 5; estratto pdftotext righe 3887-3934)*

> Il par. 3.2, inerente la definizione dell'azione sismica, presenta alcune variazioni introdotte allo scopo di aggiornare approcci e
> procedure di calcolo all'attuale stato delle conoscenze.
> Il dato di partenza per la definizione dell'azione sismica rimane sempre lo studio di pericolosita' sismica italiana di base, i cui
> risultati sono stati prodotti e messi in rete dall'Istituto Nazionale di Geofisica e Vulcanologia (INGV).

> I valori di ag, FO e T*C sono riportati negli allegati A e B al decreto del Ministro delle Infrastrutture 14 gennaio 2008 pubblicato nel
> S.O. alla Gazzetta Ufficiale del 4 febbraio 2008 n. 29 e negli eventuali successivi aggiornamenti.

*(estratto pdftotext righe 3928-3932)*

### C3.2.1 - Stati limite e relative probabilita' di superamento

*(p. 44 del S.O. n. 5; estratto pdftotext righe 4056-4139)*

> Viene preliminarmente valutato il periodo di riferimento VR della costruzione (espresso in anni), ottenuto come prodotto tra la
> vita nominale VN fissata all'atto della progettazione ed il coefficiente d'uso CU che compete alla classe d'uso nella quale la
> costruzione ricade (v. par. 2.4 delle NTC). Si ricava poi, per ciascuno stato limite e relativa probabilita' di eccedenza PVR nel periodo
> di riferimento VR, il periodo di ritorno TR del sisma. Si utilizza a tal fine la relazione:
>
> TR = -VR / ln(1 - PVR) = -CU * VN / ln(1 - PVR)     [C.3.2.1]

**Tab. C.3.2.I - Valori di TR espressi in funzione di VR**

| Stati Limite | TR (approssimato, al variare di VR) |
|---|---|
| SLO | ~ VR / 0.21 (approssimazione della formula -VR/ln(1-0.81)) |
| SLD | ~ VR (approssimazione) |
| SLV | ~ 9.5 * VR (approssimazione della formula -VR/ln(1-0.10)) |
| SLC | ~ 19.5 * VR (approssimazione della formula -VR/ln(1-0.05)) |

Nota: i valori approssimati in tabella derivano dalla formula [C.3.2.1]; la tabella C.3.2.I originale riporta le espressioni simboliche, non i valori numerici.

### C3.2.3 - Valutazione dell'azione sismica

*(p. 47-48 del S.O. n. 5; estratto pdftotext righe 4430-4519)*

> L'accelerazione spettrale massima dipende dal coefficiente S = SS*ST che comprende gli effetti delle amplificazioni stratigrafica (SS) e topografica (ST). Per le componenti orizzontali dell'azione sismica, il periodo TC di inizio del tratto a velocita' costante dello spettro, e'
> funzione invece del coefficiente CC, dipendente anch'esso dalla categoria di sottosuolo.

> Per le componenti orizzontali dell'azione sismica il coefficiente SS e' definito nella Tabella 3.2.IV delle NTC. Esso e' il rapporto tra
> il valore dell'accelerazione massima attesa in superficie e quello su sottosuolo di categoria A ed e' definito in funzione della
> categoria di sottosuolo e del livello di pericolosita' sismica di base del sito (descritto dal prodotto Fo*ag).

### C3.2.3.2.1 - Spettro di risposta elastico in accelerazione delle componenti orizzontali

*(p. 48 del S.O. n. 5; estratto pdftotext righe 4609-4620)*

> Il fattore eta tiene conto delle capacita' dissipative delle costruzioni alterando lo spettro di risposta assunto a riferimento, per il
> quale eta=1, definito come lo spettro elastico con smorzamento viscoso convenzionale xi = 5%. La relazione [3.2.4] puo' essere
> utilizzata per costruzioni che non subiscono significativi danneggiamenti e puo' essere utilizzata nel campo di smorzamenti
> convenzionali compresi tra i valori xi = 5% e xi = 28%. Al di fuori di questo campo, la scelta del valore del fattore eta deve essere
> adeguatamente giustificata.

**Nota importante**: La Circolare al C3.2.3.2.1 fa riferimento alla relazione "[3.2.4]" per il fattore eta,
confermando che l'equazione eta = sqrt(10/(5+xi)) >= 0.55 e' identificata come eq. [3.2.4] nelle NTC 2018
(non [3.2.6] come scritto erroneamente negli estratti precedenti).

---

## Procedura di interpolazione logaritmica sui TR di riferimento

*(riferimento: Allegato A al DM 14/01/2008, richiamato da NTC 2018 par. 3.2 e Circolare C3.2.1)*

La Circolare (C2.4.3, p. 38) conferma:

> "In particolare la tabella mostra i valori di VR corrispondenti ai valori di VN che individuano le frontiere tra i tre tipi di costruzione
> considerati (tipo 1, tipo 2, tipo 3); valori di VN intermedi tra detti valori di frontiera (e dunque valori di VR intermedi tra quelli
> mostrati in tabella) sono consentiti ed i corrispondenti valori dei parametri necessari a definire l'azione sismica sono ricavati
> utilizzando le formule d'interpolazione fornite nell'Allegato A alle NTC."

La formula di interpolazione logaritmica e' quella definita nell'Allegato A al DM 14/01/2008:

> log(p) = log(p_k) + (log(p_{k+1}) - log(p_k)) * log(T*/T_k) / log(T_{k+1}/T_k)

dove p e' il parametro (ag, Fo o TC*), T_k e T_{k+1} sono i TR di riferimento che brackettano T*, e p_k, p_{k+1} i valori corrispondenti.

I 9 TR di riferimento del reticolo sono: {30, 50, 72, 101, 140, 201, 475, 975, 2475} anni.
