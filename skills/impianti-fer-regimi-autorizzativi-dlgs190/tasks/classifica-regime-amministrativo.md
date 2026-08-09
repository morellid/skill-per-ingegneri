# Task: classifica-regime-amministrativo

Determina se un intervento su impianti a **fonti rinnovabili** ricade in **attivita' libera**
(art. 7), **PAS** (art. 8) o **autorizzazione unica** (art. 9) ai sensi del **D.Lgs. 190/2024**, e
quali termini e documenti ne conseguono.

## Input richiesti

- **Fonte e tipologia** di impianto (fotovoltaico, agrivoltaico, eolico, idroelettrico, biomasse,
  biometano, geotermico, solare termico, pompe di calore, cogenerazione, **accumulo**,
  **elettrolizzatore**) e **potenza** (elettrica o termica utile nominale, secondo la lettera
  dell'allegato).
- **Tipo di intervento**: nuova realizzazione oppure modifica/potenziamento/rifacimento/
  riattivazione/ricostruzione di impianto **esistente, abilitato o autorizzato** (sezione II degli
  allegati).
- **Collocazione**: su copertura, su strutture o manufatti fuori terra, su pertinenze, a terra in
  adiacenza, a terra in area industriale/artigianale/commerciale, discarica chiusa, cava esaurita,
  specchio d'acqua, ecc.; **zona urbanistica** (in particolare zona A o B del DM 1444/1968).
- **Vincoli e aree**: beni tutelati parte seconda o terza del **D.Lgs. 42/2004** (con indicazione
  se art. 136 c. 1 lett. b) o c)), **aree naturali protette** (L. 394/1991 o regionali), **siti
  Natura 2000**, vincolo **idrogeologico**, **sismico**, **vulcanico**, difesa, salute, pubblica
  incolumita', prevenzione incendi; eventuale **area idonea** o **zona di accelerazione**.
- **Interferenze**: con opere pubbliche o di interesse pubblico, con la **fascia di rispetto
  stradale**, o modifica/apertura di **accessi**.
- **Disponibilita'** della superficie e **compatibilita' urbanistica** (strumenti approvati e
  adottati, regolamenti edilizi).
- **Regione** competente e stato del suo **adeguamento** al decreto.
- Presenza di **altri interventi** dello stesso proponente, stessa fonte, in aree vicine.

## Fonti

- `references/estratti/triage-regimi-amministrativi.md` (checklist operativa).
- `references/fonti/dlgs-190-2024-regimi.md` (testo verbatim di artt. 1, 5, 6, 7, 8, 9 e Allegati
  A, B, C).

## Procedura

1. **Verifica preliminare regionale** (art. 1 cc. 3-4): la regione si e' adeguata? Nelle more si
   applica la **disciplina previgente**. Ha **innalzato le soglie** degli allegati A o B? Ha
   disciplinato l'**effetto cumulo** (artt. 7 c. 3, 8 c. 3)? Se la risposta non e' verificabile,
   dichiararlo come **assunzione da confermare**, non come risultato.
2. **Perimetra il progetto** (art. 6 c. 3): se ci sono piu' interventi della **medesima fonte** in
   **aree vicine** riconducibili a uno **stesso centro di interessi**, trattali come **progetto
   unico** e usa la **somma delle potenze**. Documenta il ragionamento: e' la difesa contro la
   contestazione di frazionamento artato.
3. **Cerca l'intervento negli allegati**, in ordine A -> B -> C, nella sezione giusta (**I** nuova
   realizzazione, **II** impianti esistenti). Riporta **lettera e numero** della voce individuata,
   non solo il regime.
4. Se la voce e' nell'**Allegato A**, applica i **filtri dell'art. 7** in questo ordine:
   - c. 2: vincoli parte seconda D.Lgs. 42/2004, aree protette, Natura 2000, parte terza, rischio
     idrogeologico/difesa/salute/pubblica incolumita'/sismico/vulcanico/incendi -> **PAS**;
   - c. 8: interferenze con opere pubbliche, fascia di rispetto stradale, accessi -> **PAS**;
   - cc. 4-6: se restano in attivita' libera ma insistono su immobili art. 136 c. 1 lett. b) o c),
     serve l'**autorizzazione paesaggistica** (30 giorni, parere Soprintendenza 20 giorni), salvo
     l'esenzione del c. 6;
   - c. 9: verifica se la voce rientra tra quelle **sempre esenti** (Allegato A sez. II lett. a)
     nn. 1) e 3), b), c), e), l));
   - c. 1: disponibilita' della superficie, NTC, codice della strada, compatibilita' urbanistica,
     eventuale comunicazione o titolo edilizio;
   - c. 7: **garanzia** bancaria o assicurativa se si occupa suolo non ancora antropizzato.
5. Se il regime e' la **PAS**, verifica la **preclusione dell'art. 8 c. 2** (assenza di
   disponibilita' delle superfici o di compatibilita' urbanistica -> si va in **AU**), poi mappa:
   comune procedente (c. 3-bis), adempimenti **preventivi** VIncA e titolo edilizio ex art. 10 DPR
   380/2001 con presentazione entro **90 giorni perentori** (cc. 12, 12-bis, 12-ter),
   documentazione **lett. a)-m)** del c. 4, soglia **> 1 MW** (oneri istruttori e compensazioni
   **1-3%**), termine applicabile (**30 / 45 / 60 giorni**), pubblicazione sul **BUR**, decadenza
   a **2 / 3 anni**, ed eventuale riduzione di un terzo dei termini per Allegato B sez. I lett. q)
   e sez. II lett. d) (c. 13).
6. Se il regime e' l'**autorizzazione unica**, individua la **competenza** (Allegato C sez. I ->
   regione o ente delegato; sez. II -> MASE), se serve la **verifica di assoggettabilita' a VIA**
   (preventiva, fino a 90 giorni), se si applica l'**art. 27-bis del D.Lgs. 152/2006** (VIA
   regionale, termine fino a 2 anni), poi la sequenza dell'art. 9 cc. 4-9 e i contenuti del
   provvedimento (c. 10), incluse **garanzie entro 120 giorni** e **compensazioni 1-4%** (non
   dovute su superfici edificate o coperture di parcheggi).
7. **Obbligo trasversale**: prevedi i **sistemi di raccolta delle acque meteoriche** per le nuove
   superfici impermeabilizzate, temporanee e permanenti (art. 6 c. 3-bis).
8. Se il regime risulta l'attivita' libera, passa al task
   [`adempi-modello-unico-parte-iii`](adempi-modello-unico-parte-iii.md).

## Output atteso

- **Regime individuato** con la **voce di allegato** (allegato, sezione, lettera, eventuale numero)
  e l'articolo applicabile.
- **Elenco dei fattori che modificano il regime** (vincoli, interferenze) con il comma che li
  prevede, oppure la dichiarazione esplicita che sono stati esclusi e sulla base di quale dato.
- **Potenza rilevante** usata e motivazione dell'eventuale aggregazione a progetto unico.
- **Mappa dei termini** e **checklist della documentazione** del regime individuato.
- **Assunzioni da confermare**, in particolare sulla disciplina regionale.

## Limiti

- Gli allegati elencano gli interventi con **soglie puntuali**: la voce va sempre riletta sul testo
  in `references/fonti/dlgs-190-2024-regimi.md`. Se nessuna voce corrisponde con certezza,
  **dichiaralo** invece di forzare la classificazione.
- Il testo trascritto e' **consolidato al 9 agosto 2026**: verificare che non siano intervenute
  ulteriori novelle.
- I criteri di **idoneita' delle aree** (art. 11-bis), le **zone di accelerazione** (art. 12) e la
  ripartizione dell'**Allegato C-bis** sono **fuori scope**: se l'esito dipende da essi, segnalalo.
- La classificazione **non sostituisce** l'asseverazione del tecnico abilitato ne' la valutazione
  dell'amministrazione competente.
