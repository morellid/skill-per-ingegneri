# Task — Verifica i requisiti di duttilità e i dettagli (NTC 2018 §7.7.3.1, §§7.7.5-7.7.7)

Supporto documentale per confrontare i **mezzi di unione** e le **disposizioni costruttive** di un edificio in
legno in zona sismica con le **precisazioni sulla duttilità** del par. 7.7.3.1 e con le disposizioni/verifiche
dei par. 7.7.5-7.7.7 delle NTC 2018 (DM 17/1/2018). **Non** sostituisce le verifiche di resistenza/duttilità.

Fonte: `../references/fonti/ntc2018-par-7-7.md`; checklist: `../references/estratti/legno-sismica-checklist.md`.

## Input tipico

- Classe di duttilità adottata (**CD "A"** o **CD "B"**) e tipologia delle zone dissipative.
- Collegamenti/mezzi di unione: tipo (perni, chiodi, spinotti, bulloni), **diametro d**, spessore delle
  membrature lignee collegate; per pareti/diaframmi a telaio: diametro dei chiodi e spessore del rivestimento.
- Presenza di **giunti di carpenteria** e schema degli **impalcati** (diaframma rigido/deformabile, vincoli).

## Passi

1. **Precisazioni sulla duttilità (§7.7.3.1)**
   - Requisito di prova: le zone dissipative devono deformarsi plasticamente per **almeno 3 cicli** a inversione
     completa, con **rapporto di duttilità statica ≥ 4 (CD "B")** / **≥ 6 (CD "A")**, senza riduzione di
     resistenza **> 20%**.
   - Ciò si ritiene soddisfatto se:
     a) collegamenti **legno-legno o legno-acciaio** con perni/chiodi **d ≤ 12 mm** e spessore delle membrature
        lignee collegate **≥ 10d**;
     b) **pareti e diaframmi con telaio in legno** con chiodi **d ≤ 3,1 mm** e rivestimento strutturale (legno o
        derivati) di **spessore ≥ 4d**.
   - Se non tutte le prescrizioni sono rispettate ma è assicurato lo spessore minimo **≥ 8d (caso a)** / **≥ 3d
     (caso b)**, le zone dissipative sono da considerare in **CD "B"**.

2. **Disposizioni costruttive (§7.7.5)**
   - Zone dissipative localizzate dove plasticizzazioni/instabilità locali non compromettono la stabilità globale.
   - **Impalcati** (§7.7.5.3, oltre §4.4): niente fattori di incremento della capacità dei mezzi di unione ai
     bordi; forze di taglio secondo la disposizione effettiva dei controventi; vincoli impalcato-pareti **bilateri**;
     tutti i bordi dei rivestimenti collegati al telaio.

3. **Verifiche di sicurezza (§7.7.6) e dettagli (§7.7.7)**
   - Sovraresistenza per: collegamenti di elementi tesi o alle fondazioni; collegamenti diaframma-controvento.
   - **Giunti di carpenteria**: nessun rischio di rottura fragile se la verifica per tensioni tangenziali (§4.4) è
     soddisfatta con un **ulteriore coefficiente parziale di sicurezza pari a 1,3**.
   - Per le strutture dissipative vale quanto riportato nelle verifiche di resistenza (RES) del §7.3.6.1 quando i
     requisiti del §7.7.3 sono soddisfatti e la **resistenza del materiale è ridotta del 20%** (degrado ciclico).
   - **Perni/bulloni d > 16 mm non devono essere utilizzati** nei collegamenti legno-legno/legno-acciaio (salvo
     come elementi di chiusura dei connettori).

4. **Output**: tabella collegamento-per-collegamento con d, spessori, esito rispetto alle regole a)/b) del
   §7.7.3.1 e alla classe di duttilità risultante; nota sulle disposizioni di impalcato e sui coefficienti (1,3
   per i giunti di carpenteria, riduzione 20%). Segnala che è un inquadramento, non una verifica di resistenza.

## Cosa NON fare

- Non confondere le regole di duttilità dei mezzi di unione (**geometriche**) con le **verifiche** di resistenza/
  duttilità degli elementi/collegamenti: queste restano fuori scope.
- Non applicare la regola b) (pareti/diaframmi) a un collegamento legno-acciaio (regola a) e viceversa.
- Non inventare valori: ogni limite deve essere rintracciabile in `../references/fonti/ntc2018-par-7-7.md`.
