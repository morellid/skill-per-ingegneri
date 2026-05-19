# Task: identifica la procedura di valutazione della conformita'

## Obiettivo

Determinare quale **procedura di valutazione della conformita'** il fabbricante deve applicare a una macchina o a un prodotto correlato ai sensi dell'art. 25 del Reg. (UE) 2023/1230 e dell'Allegato I (parte A o B): Modulo A (controllo interno della produzione), Modulo B + Modulo C (esame UE del tipo + conformita' al tipo), Modulo G (verifica dell'unita'), Modulo H (garanzia qualita' totale). Indicare se la procedura richiede un **organismo notificato** e quindi se la marcatura CE deve essere seguita dal **numero ON**.

Nota: questo task riguarda solo le macchine e i prodotti correlati. Per le quasi-macchine non si parla di procedura di valutazione della conformita' (non c'e' marcatura CE): si redige documentazione tecnica All. IV parte B e dichiarazione di incorporazione UE.

## Input richiesti

Prerequisito: il prodotto e' gia' stato qualificato come **macchina** o **prodotto correlato** dal task `qualifica-prodotto.md`. Se non lo e', esegui prima quel task.

Chiedi all'utente:

- Descrizione tecnica della macchina/prodotto correlato (tipologia, uso previsto, parti mobili).
- Eventuali coincidenze sospette con le categorie elencate in Allegato I parti A o B (vedi elenco nella sez. 2 dell'estratto).
- Se la macchina o il prodotto correlato integra **sistemi/componenti con apprendimento automatico** che garantiscono **funzioni di sicurezza**.
- Se il fabbricante ha intenzione di applicare **norme armonizzate** o **specifiche comuni** che coprono **tutti i RES pertinenti** (rilevante per scegliere il Modulo A in parte B).
- Numero di unita' prodotte: pezzo unico, piccola serie, serie.
- Se la macchina rientra in un **sistema qualita' certificato** (es. ISO 9001) e il fabbricante intende usare il Modulo H.

## Fonti

- `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md` sezione 2 (procedure art. 25; All. I parti A e B; conseguenze marcatura CE; presunzione conformita').
- `references/fonti/reg-ue-2023-1230-macchine.md` art. 6 par. 1, art. 20, art. 24 par. 3, art. 25 par. 1-5, Allegato I parte A (6 categorie testuali), Allegato I parte B (19 categorie testuali), Allegato VI (Modulo A), Allegato VII (Modulo B, validita' max 5 anni), Allegato VIII (Modulo C), Allegato IX (Modulo H), Allegato X (Modulo G).

## Procedura

1. **Confronto con Allegato I parte A** (categorie ad alto rischio - sempre con ON):
   - 1. Dispositivi amovibili di trasmissione meccanica, compresi i loro ripari.
   - 2. Ripari dei dispositivi amovibili di trasmissione meccanica.
   - 3. Ponti elevatori per veicoli.
   - 4. Apparecchi portatili a carica esplosiva per il fissaggio o altre macchine ad impatto.
   - 5. Componenti di sicurezza con apprendimento automatico autoevolutivo per funzioni di sicurezza.
   - 6. Macchine che integrano sistemi con apprendimento automatico autoevolutivo per funzioni di sicurezza, non immessi separatamente (limitatamente a tali sistemi).
   Se il prodotto ricade in una di queste 6 categorie -> **art. 25 par. 2**: scegli tra a) Modulo B + Modulo C; b) Modulo H; c) Modulo G. **Modulo A non e' ammesso**.
2. **Confronto con Allegato I parte B** (categorie classiche con possibile Modulo A):
   - 1. Seghe circolari (mono/multilame) per legno o carne, tipi 1.1-1.4.
   - 2. Spianatrici ad avanzamento manuale per legno.
   - 3. Piallatrici su una faccia ad avanzamento integrato, carico/scarico manuale, per legno.
   - 4. Seghe a nastro a carico/scarico manuale per legno o carne, tipi 4.1-4.2.
   - 5. Macchine combinate dei tipi 1-4 e 7 per legno.
   - 6. Tenonatrici a mandrini multipli ad avanzamento manuale per legno.
   - 7. Fresatrici ad asse verticale "toupies" ad avanzamento manuale per legno.
   - 8. Seghe a catena portatili da legno.
   - 9. Presse (comprese piegatrici) per lavorazione a freddo dei metalli, carico/scarico manuale, con elementi mobili a corsa > 6 mm e velocita' > 30 mm/s.
   - 10. Formatrici per plastica a iniezione/compressione con carico/scarico manuale.
   - 11. Formatrici per gomma a iniezione/compressione con carico/scarico manuale.
   - 12. Macchine per lavori sotterranei: locomotive e benne di frenatura (12.1); armatura semovente idraulica (12.2).
   - 13. Veicoli per raccolta rifiuti domestici a carico manuale con compressione.
   - 14. Apparecchi per sollevamento di persone (o persone e cose) con pericolo di caduta verticale > 3 metri.
   - 15. Dispositivi di protezione per rilevare la presenza di persone.
   - 16. Ripari mobili automatici interbloccati per le macchine dei punti 9, 10, 11.
   - 17. Blocchi logici per assicurare funzioni di sicurezza.
   - 18. Strutture di protezione in caso di ribaltamento (ROPS).
   - 19. Strutture di protezione contro la caduta di oggetti (FOPS).
   Se il prodotto ricade in una di queste 19 categorie -> **art. 25 par. 3**: scegli tra a) **Modulo A se** il fabbricante applica integralmente norme armonizzate o specifiche comuni che coprono **tutti i RES pertinenti**; b) Modulo B + Modulo C; c) Modulo H; d) Modulo G.
3. **Categoria non in Allegato I**: il prodotto non rientra ne' in parte A ne' in parte B -> **art. 25 par. 4**: si applica il **Modulo A** (controllo interno della produzione, All. VI). Non e' richiesto ON.
4. **Verifica condizionale del Modulo A per parte B** (art. 25 par. 3 lett. a):
   - Il fabbricante deve applicare norme armonizzate ex art. 20 par. 1 o specifiche comuni ex art. 20 par. 3 che coprono **tutti i RES pertinenti** per quella categoria.
   - Se anche un solo RES pertinente non e' coperto da armonizzata o specifica comune **applicata integralmente**, il Modulo A puro non e' utilizzabile -> ripieghi su b), c) o d).
   - La skill non valida l'applicabilita' della singola norma armonizzata al progetto: chiede al fabbricante di confermare.
5. **Marcatura CE - conseguenza** (art. 24 par. 3):
   - Procedure con ON (par. 2 lett. a/b/c, par. 3 lett. b/c/d) -> marcatura CE + **numero ON**.
   - Modulo A puro (par. 3 lett. a, par. 4) -> marcatura CE **senza numero ON**.
6. **Indicazioni operative per moduli**:
   - **Modulo A** (All. VI): controllo interno della produzione, niente ON, dichiarazione UE redatta dal fabbricante, conservazione 10 anni.
   - **Modulo B** (All. VII): esame UE del tipo da parte di un ON; certificato con **validita' non superiore a 5 anni**; riesame su modifica del tipo, evoluzione dello stato dell'arte o prima della scadenza. Non e' una procedura completa: va combinato con Modulo C.
   - **Modulo C** (All. VIII): conformita' al tipo basata sul controllo interno della produzione. Marcatura CE + numero ON (quello del Modulo B). Sempre combinato con Modulo B.
   - **Modulo G** (All. X): verifica dell'unita' da parte di un ON. Tipicamente pezzi unici o piccolissime serie. ON appone o fa apporre il proprio numero sul prodotto e rilascia certificato.
   - **Modulo H** (All. IX): garanzia qualita' totale - il fabbricante applica un sistema qualita' approvato da un ON per progettazione, fabbricazione, ispezione finale, collaudo; sorveglianza dell'ON.

## Output

Restituisci un report strutturato in italiano:

```
Procedura di valutazione della conformita' - Reg. (UE) 2023/1230 - <prodotto>

1. Collocazione in Allegato I:
   - parte A categoria n. <X>: <SI / NO>
   - parte B categoria n. <Y>: <SI / NO>
   - non elencato in All. I: <SI / NO>

2. Regime procedurale (art. 25):
   - par. 2 (alto rischio - obbligo ON): <SI / NO>
   - par. 3 (parte B - Modulo A condizionato): <SI / NO>
   - par. 4 (non in All. I - Modulo A libero): <SI / NO>

3. Moduli ammissibili:
   - <elenco con riferimento ad allegato (All. VI/VII+VIII/IX/X) e par. art. 25>

4. Moduli raccomandati nel caso concreto:
   - <indicazione, con motivazione: numero unita', presenza di sistema qualita', applicazione integrale di norme armonizzate, ecc.>

5. Organismo notificato:
   - richiesto: <SI / NO>
   - se SI: la marcatura CE sara' seguita dal numero ON (art. 24 par. 3).
   - se NO (Modulo A puro): marcatura CE senza numero ON.

6. Documenti attesi:
   - documentazione tecnica All. IV parte A (vedi task `struttura-fascicolo-tecnico.md`);
   - dichiarazione UE di conformita' All. V parte A (vedi task `struttura-dichiarazione-ue.md`);
   - se Modulo B: certificato di esame UE del tipo, validita' max 5 anni, riesame da prevedere.

Rinvii:
- La scelta finale tra moduli alternativi spetta al fabbricante.
- L'applicabilita' di specifiche norme armonizzate (art. 20 par. 1) o specifiche comuni (art. 20 par. 3) non e' validata dalla skill: e' valutazione tecnica del progettista e dell'eventuale organismo notificato.
- La selezione e la notifica dell'organismo notificato sono responsabilita' del fabbricante (organismi notificati art. 26-42, fuori scope skill).
```

## Limiti

- La skill non valida se una **norma armonizzata** specifica copra integralmente i RES pertinenti per la categoria All. I parte B: la risposta sulla disponibilita' del Modulo A in parte B dipende da questa verifica, che e' tecnica e a carico del fabbricante.
- Le categorie 5 e 6 di Allegato I parte A (apprendimento automatico per funzioni di sicurezza) sono nuove rispetto alla 2006/42/CE: la qualifica di "sistema autoevolutivo" e' giuridicamente determinante e va istruita con cura dal fabbricante.
- La skill non confronta i costi/tempi tra moduli: la scelta tra B+C, G, H per le parti A o tra A, B+C, G, H per le parti B e' una decisione economica e organizzativa del fabbricante.
- La skill non si pronuncia sull'idoneita' del singolo organismo notificato selezionato dal fabbricante.
