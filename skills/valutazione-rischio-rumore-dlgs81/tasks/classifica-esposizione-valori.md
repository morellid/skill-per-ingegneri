# Task: classifica-esposizione-valori

Colloca un'esposizione al rumore rispetto ai **valori inferiori/superiori di azione**
e al **valore limite** (art. 189) e individua i conseguenti **obblighi** (misurazione,
misure, segnaletica, DPI, sorveglianza). **Non misura** ne' **calcola** i livelli.

## Input attesi
- Il **LEX,8h** (o LEX,w) e/o il **ppeak** stimati/dichiarati per la mansione o l'area
  (dato d'ingresso: non e' compito della skill misurarli).
- Il tipo di esposizione (continua/impulsiva; variabilita' giornaliera/settimanale).
- Presenza di lavoratori particolarmente sensibili (gravidanza, minori).

## Passi
1. **Fascia di esposizione** (art. 189 c. 1): colloca LEX/ppeak in una delle fasce:
   - **< 80 dB(A)** e < 135 dB(C): sotto i valori inferiori di azione;
   - **≥ 80 e < 85 dB(A)** (o ppeak ≥ 135 e < 137 dB(C)): tra inferiori e superiori;
   - **≥ 85 e ≤ 87 dB(A)** (o ppeak ≥ 137 e ≤ 140 dB(C)): tra superiori e limite;
   - **> 87 dB(A)** o > 140 dB(C): oltre il **valore limite** (non ammesso; con DPI
     l'esposizione effettiva all'orecchio deve rientrare - art. 193 c. 2).
2. **Base settimanale** (art. 189 c. 2-3): se l'esposizione varia molto tra i giorni,
   valuta l'uso del **LEX,w** (purche' ≤ 87 dB(A) e con misure di riduzione), usando il
   livello settimanale massimo ricorrente.
3. **Obbligo di misurazione** (art. 190 c. 2): se puo' ritenersi superato il **valore
   inferiore di azione**, segnala che occorre **misurare** i livelli (a cura del
   tecnico) e riportarli nel documento di valutazione.
4. **Conseguenze per fascia**: elenca gli obblighi attivati (rinvio ai task/estratto):
   misure ex art. 192 (programma se oltre i superiori; segnaletica/delimitazione);
   DPI ex art. 193 (messa a disposizione dagli inferiori, obbligo d'uso dai superiori);
   sorveglianza ex art. 196 (obbligo oltre i superiori, su richiesta oltre gli
   inferiori).

## Output
- Fascia di esposizione con il **rinvio all'art. 189** e l'elenco strutturato degli
  obblighi attivati (misurazione, misure, segnaletica, DPI, sorveglianza).
- Nota di rinvio: la **misura** dei livelli e la loro documentazione nel DVR restano
  al datore di lavoro e al tecnico competente in acustica.

## Riferimenti
- `../references/fonti/dlgs-81-2008-rumore.md` (artt. 188, 189, 190)
- `../references/estratti/rischio-rumore-checklist.md` (sez. A, B, C)
