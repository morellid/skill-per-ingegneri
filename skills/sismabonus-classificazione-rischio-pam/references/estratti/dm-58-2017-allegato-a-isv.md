# DM 58/2017 Allegato A punto 2.2 - Indice di Sicurezza per la Vita IS-V

> Fonte: DM 58/2017 Allegato A (testo aggiornato dal DM 65/2017).
> Testo letto da: references/fonti/dm-65-2017-all-a.md (trascrizione verbatim del PDF ufficiale MIT)
> URL PDF ufficiale: https://www.mit.gov.it/nfsmitgov/files/media/normativa/2017-03/DM%2065%20del%2007-03-2017%20All%20A.pdf
> SHA256 PDF: 8392e1dddd5ff99de3fab805e86414bd61ac8fc022a95ba2731c485a48fa5878
> Data accesso: 2026-05-10
> Licenza: dominio pubblico (atto normativo italiano)
> Verifica semantica: ogni affermazione e' rintracciabile in references/fonti/dm-65-2017-all-a.md
> (sezione "Pagine 2-5: Sezione 2.1", passo 9 e Tabella 2).

## Definizione

L'**Indice di Sicurezza Strutturale per la Vita (IS-V)** e' definito dal rapporto tra:
- l'**Accelerazione di Picco al Suolo di Capacita'** PGA_C(SLV) che determina il raggiungimento dello Stato Limite di salvaguardia della Vita per l'edificio
- l'**Accelerazione di Picco al Suolo di Domanda** PGA_D(SLV) che le NTC 2018 prescrivono al sito per il medesimo Stato Limite

## Formula

```
IS-V = PGA_C(SLV) / PGA_D(SLV)
```

espresso come frazione adimensionale; per la Tab. classi IS-V (Allegato A punto 2.3) moltiplicare per 100 per ottenere la percentuale.

## Significato fisico

- **IS-V > 100%**: l'edificio sopporta accelerazioni superiori a quelle di domanda al sito - sicurezza > requisito normativo (classe A+).
- **IS-V = 100%**: l'edificio sopporta esattamente le accelerazioni di domanda - sicurezza piena ma "al limite" (classe A).
- **IS-V < 100%**: l'edificio NON sopporta le accelerazioni di domanda al SLV - margine di sicurezza ridotto rispetto al requisito normativo per nuove costruzioni; per edifici esistenti puo' essere accettabile in funzione della classe d'uso, della destinazione e della vita residua.

## Note operative

- L'IS-V usa la PGA al sito al periodo zero. Non confondere con l'ordinata di spettro Se(T=0): per la componente orizzontale Se(T=0) = a_g x S x F_0 x eta x (T_B/T_B) / F_0 = a_g x S (al periodo nullo, F_0 e eta vanno via). Quindi PGA_D = a_g x S, dove S = S_S x S_T (Tab. 3.2.IV e 3.2.V NTC 2018).
- Per edifici **esistenti** l'IS-V e' sempre minore o uguale a quello richiesto per nuove costruzioni (per definizione dell'analisi di vulnerabilita'). Edifici fuori zona sismica con domanda molto bassa possono comunque avere IS-V > 100% senza interventi.
- L'IS-V e' un parametro **separato** dal PAM: due edifici con stesso IS-V possono avere PAM molto diversi, perche' il PAM dipende anche dal comportamento agli SL meno severi (SLO, SLD).

## Verifiche semantiche effettuate vs PDF (2026-05-10)

1. **Definizione IS-V**: CONFERMATA - il PDF al passo 9 (pag. 4) dice: "Si determina l'indice di
   sicurezza per la vita IS-V, ovvero il rapporto tra la PGAC (di capacita') che ha fatto
   raggiungere al fabbricato lo stato limite di salvaguardia della vita umana e la PGAD
   (di domanda) del sito in cui e' posizionato la costruzione, con riferimento al medesimo
   stato limite." - cioe' IS-V = PGAC(SLV) / PGAD(SLV).
2. **Tabella classi IS-V (Tabella 2, pag. 3 del PDF)**: CONFERMATA con i seguenti valori esatti:
   - A+: 100% < IS-V (strettamente maggiore)
   - A: 80% <= IS-V < 100%
   - B: 60% <= IS-V < 80%
   - C: 45% <= IS-V < 60%
   - D: 30% <= IS-V < 45%
   - E: 15% <= IS-V < 30%
   - F: IS-V <= 15%
3. **Ambiguita' bordo IS-V = 100%**: CONFERMATA - il PDF pone A+: `100% < IS-V` (esclusivo) e
   A: `80% <= IS-V < 100%` (esclusivo a 100%). Il valore esatto 100% non e' formalmente
   coperto. L'interpretazione conservativa (IS-V=100% -> classe A) e' quella adottata.
4. **Non esiste classe G per IS-V**: CONFERMATO - la Tabella 2 del PDF elenca solo 7 classi
   (da A+ a F), non include G.

## Riferimenti puntuali

- PDF DM 65/2017 All. A pag. 3 (Tabella 2): classi IS-V con soglie
- PDF DM 65/2017 All. A pag. 4 (passo 9): definizione IS-V = PGAC(SLV)/PGAD(SLV)
- PDF DM 65/2017 All. A pag. 4 (passo 11): classe finale = peggiore tra PAM e IS-V
- Trascrizione verbatim: references/fonti/dm-65-2017-all-a.md
