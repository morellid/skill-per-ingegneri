# Output atteso - Pressa piegatrice idraulica PB-150T

Esempio del tipo di output che la skill produce in tre fasi (qualifica -> procedura -> indice fascicolo), citando articoli e allegati del Reg. (UE) 2023/1230.

## 1. Qualificazione prodotto (task `qualifica-prodotto.md`)

```
Qualificazione prodotto - Reg. (UE) 2023/1230 - Pressa piegatrice idraulica PB-150T

1. Calendario applicazione: immissione marzo 2027 -> coperta dal Reg. 2023/1230 (applicazione 14/01/2027).
2. Esclusioni ex art. 2 par. 2: nessuna pertinente (la pressa non rientra nelle lett. a-q).
3. Qualifica:
   - Macchina (art. 3 punto 1 lett. a): SI - insieme equipaggiato di azionamento idraulico, parti mobili (punzone), applicazione determinata (piegatura a freddo della lamiera).
   - Prodotto correlato: NO.
   - Quasi-macchina: NO (esegue autonomamente un'applicazione specifica).
   - Componente di sicurezza autonomo: NO.
4. Apprendimento automatico per funzioni di sicurezza: NO.
5. Categoria All. I (preliminare, conferma nel task identifica-procedura-conformita):
   - All. I parte A: nessuna.
   - All. I parte B: potenziale categoria n. 9 (presse per lavorazione a freddo dei metalli, carico/scarico manuale, con elementi mobili che possono avere corsa > 6 mm e velocita' > 30 mm/s).
     Nota: la formula del testo del regolamento ("possono avere") si riferisce alla capacita' meccanica della macchina, non alla velocita' nominale di lavoro. La pressa PB-150T dichiara una velocita' di ritorno di 80 mm/s, quindi tra le velocita' del punzone "possibili" c'e' un valore (80 mm/s) che supera la soglia di 30 mm/s; la corsa massima 200 mm supera 6 mm; il carico/scarico e' manuale. Tutti e tre i criteri sono soddisfatti -> categoria 9 applicabile.
   - Non in All. I: NO.
6. Modifica sostanziale ex art. 3 punto 16: non pertinente (prodotto nuovo).
7. Operatore: fabbricante (art. 3 punto 18) - progettazione e fabbricazione in proprio, immissione con proprio marchio.

Esito: la pressa RICADE nel Reg. (UE) 2023/1230, qualifica di macchina, categoria All. I parte B n. 9. Regime documentale: All. IV parte A + All. V parte A + marcatura CE (art. 24).
```

## 2. Procedura di valutazione della conformita' (task `identifica-procedura-conformita.md`)

```
Procedura di valutazione della conformita' - Reg. (UE) 2023/1230 - Pressa piegatrice PB-150T

1. Collocazione in Allegato I:
   - parte A categoria n. -: NO.
   - parte B categoria n. 9 (presse per lavorazione a freddo dei metalli, carico/scarico manuale, con elementi mobili che possono avere corsa > 6 mm e velocita' > 30 mm/s): SI (la velocita' di ritorno 80 mm/s rientra nelle velocita' possibili del punzone, soglia 30 mm/s superata; corsa 200 mm > 6 mm; carico/scarico manuale).
   - non elencato in All. I: NO.

2. Regime procedurale (art. 25):
   - par. 2 (alto rischio): NO.
   - par. 3 (parte B - Modulo A condizionato): SI.
   - par. 4: NO.

3. Moduli ammissibili (art. 25 par. 3):
   - a) Modulo A (controllo interno della produzione, All. VI) - ammissibile SOLO se norme armonizzate o specifiche comuni coprono integralmente tutti i RES pertinenti per la categoria 9;
   - b) Modulo B (esame UE del tipo, All. VII) + Modulo C (conformita' al tipo, All. VIII);
   - c) Modulo H (garanzia qualita' totale, All. IX);
   - d) Modulo G (verifica dell'unita', All. X).

4. Moduli raccomandati nel caso concreto:
   - Il fabbricante dichiara di applicare integralmente UNI EN 12622 (norma armonizzata di prodotto per le presse piegatrici idrauliche) e altre armonizzate pertinenti.
   - Se l'applicazione integrale e' confermata e copre tutti i RES pertinenti (verifica del progettista), il Modulo A e' utilizzabile (art. 25 par. 3 lett. a).
   - In caso anche un solo RES pertinente non sia coperto da armonizzata/specifica comune applicata integralmente, occorre passare a Modulo B+C, H o G; il piu' tipico per produzione di serie e' B+C.

5. Organismo notificato:
   - richiesto se Modulo A non utilizzabile: SI.
   - se Modulo A puro: NO; marcatura CE senza numero ON (art. 24 par. 3 a contrario).

6. Documenti attesi:
   - documentazione tecnica All. IV parte A (vedi task struttura-fascicolo-tecnico.md);
   - dichiarazione UE di conformita' All. V parte A (vedi task struttura-dichiarazione-ue.md);
   - se Modulo B: certificato esame UE del tipo, validita' max 5 anni, riesame ad ogni modifica o evoluzione dello stato dell'arte (All. VII punto 7).

Rinvii:
- La scelta finale tra Modulo A puro e B+C/G/H spetta al fabbricante.
- La copertura integrale dei RES da parte di EN 12622 (e armonizzate complementari come EN ISO 12100, EN ISO 13849-1, EN 60204-1) richiede valutazione tecnica caso per caso del progettista. Questa skill NON valida tale copertura.
- Per la marcatura CE: posizione, leggibilita', indelebilita' ex art. 24 par. 1; apposizione prima dell'immissione ex art. 24 par. 2.
```

## 3. Indice fascicolo tecnico (task `struttura-fascicolo-tecnico.md`)

```
Indice fascicolo tecnico - Reg. (UE) 2023/1230 - Pressa piegatrice PB-150T
Allegato IV parte A

A1. Descrizione completa del prodotto e dell'uso previsto
    - Contenuto: scheda tecnica con tipo "pressa piegatrice idraulica", modello PB-150T, forza nominale 150 t, lunghezza utile 3100 mm; uso previsto (piegatura a freddo della lamiera di acciaio) e uso prevedibilmente errato.
    - Formato: relazione tecnica + foglio dati.
    - Riferimento: All. IV parte A lett. a.
    - Responsabile: ufficio tecnico.

A2. Valutazione del rischio
    - A2.1 Procedura seguita (es. UNI EN ISO 12100 - rinvio strutturale, norma armonizzata di metodo).
    - A2.2 Elenco RES applicabili da All. III (matrice prodotta dal progettista).
    - A2.3 Misure di protezione e rischi residui (laser frontale + blocco logico di sicurezza certificato, comando bimanuale opzionale, EN ISO 13849-1 PL pertinente).
    - Riferimento: All. IV parte A lett. b.
    - Responsabile: progettista + responsabile sicurezza.

A3. Disegni e schemi (lett. c)
    - Assieme generale, layout idraulico, schema elettrico, schema del circuito di sicurezza (canalizzazione del segnale laser, ridondanza, sorveglianza), disegni di dettaglio di ripari fissi e mobili.

A4. Descrizioni e spiegazioni (lett. d) - relazioni di supporto ai disegni.

A5. Riferimenti a norme armonizzate / specifiche comuni applicate (lett. e)
    - UNI EN 12622 (presse piegatrici idrauliche - norma di prodotto), edizione e data di pubblicazione GUUE.
    - UNI EN ISO 12100 (metodo), UNI EN ISO 13849-1 (controllo di sicurezza), UNI EN 60204-1 (equipaggiamento elettrico).
    - Indicare se applicazione integrale o parziale.

A6. Altre specifiche tecniche (lett. f) - solo se applicazione parziale o non disponibilita' di armonizzata per uno specifico RES.

A7. Relazioni e risultati di calcoli, prove, ispezioni, esami (lett. g) - es. calcolo dello spazio di arresto del punzone, prova di funzionalita' del sistema di rilevamento mani, prove EMC.

A8. Mezzi usati durante la produzione (lett. h) - schede di controllo qualita' in linea, criteri di accettazione (Nota: NON oggetto dell'esame ON nei Moduli B/H).

A9. Copia istruzioni per l'uso + informazioni All. III punto 1.7.4 (lett. i) - manuale d'uso e manutenzione in italiano, conforme ad art. 10 par. 7.

A10. Quasi-macchine incorporate (lett. j) - se la pressa integra ad es. un sistema di alimentazione automatica della lamiera fornito come quasi-macchina: includere la dichiarazione UE di incorporazione e le istruzioni di assemblaggio del fornitore. Non applicabile se la pressa e' interamente costruita in stabilimento.

A11. Dichiarazioni UE di altri prodotti incorporati (lett. k) - dichiarazioni di conformita' di componenti coperti da EMC, LVD, ecc. (blocco logico di sicurezza, PLC di sicurezza, encoder).

A12. Misure interne per produzione in serie (lett. l) - procedura interna che descrive controllo dei componenti di sicurezza, prove finali, etichettatura.

A13. Codice sorgente / logica software sicurezza (lett. m) - documentazione della logica programmata del PLC di sicurezza; tenuta a disposizione su richiesta motivata delle autorita'.

A14. Sistema basato su sensori (lett. n) - se il rilevamento mani e' basato su sensori laser intelligenti con elaborazione dati, descrizione del sistema, dati, prove e convalida. Per il modello PB-150T descritto: dipende dall'architettura del laser frontale; se il laser e' un componente "scatola nera" certificato, descrivere come componente; se il fabbricante implementa logiche di sicurezza, descrivere lo sviluppo, le prove e la convalida.

A15. Ricerche/prove per montaggio e messa in servizio in sicurezza (lett. o) - prove di installazione, prove di basamento, criteri di livellamento.

Note operative:
- Lingua: italiana + traduzione nelle lingue degli Stati membri di destinazione.
- Conservazione: almeno 10 anni dalla data di immissione sul mercato (art. 10 par. 3).
- Codice sorgente (lett. m) tenuto a disposizione su richiesta motivata.
- Lett. h ed l: non esaminate dall'ON nei Moduli B/H, ma parte del fascicolo per la vigilanza del mercato.

Rinvii:
- L'elenco RES (voce A2.2) richiede lettura diretta dell'Allegato III, fuori dal perimetro di questa skill.
- Per la dichiarazione UE corrispondente vedi task struttura-dichiarazione-ue.md.
- La compilazione e firma restano del fabbricante.
```
