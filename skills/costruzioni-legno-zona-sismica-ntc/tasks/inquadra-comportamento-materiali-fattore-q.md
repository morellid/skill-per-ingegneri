# Task — Inquadra comportamento, materiali e fattore di comportamento (NTC 2018 §7.7.1-7.7.3)

Supporto documentale per inquadrare, per un edificio in legno in zona sismica (NTC 2018, DM 17/1/2018, par. 7.7):
gli **aspetti concettuali** e la classe di duttilità (§7.7.1), i **materiali** e le proprietà delle zone
dissipative (§7.7.2) e i **fattori di comportamento** q0 (§7.7.3). **Non** esegue verifiche né progetta i
collegamenti.

Fonte: `../references/fonti/ntc2018-par-7-7.md`; checklist: `../references/estratti/legno-sismica-checklist.md`.

## Input tipico

- Tipologia strutturale prevista: **parete a telaio** (platform frame), **pannelli XLAM/CLT**, telaio di travi e
  pilastri, ecc., e scelta del **comportamento** (dissipativo/non dissipativo).
- Materiali e pannelli di rivestimento previsti (particelle, compensato, OSB) con relativi spessori.
- Tipologia dei collegamenti/mezzi di unione previsti (a gambo cilindrico, incollati, nodi di carpenteria).

## Passi

1. **Aspetti concettuali / duttilità (§7.7.1)**
   - Scegli il comportamento: **dissipativo** (→ classe di duttilità **CD "A"** o **CD "B"**, nel rispetto del
     §7.7.3) oppure **non dissipativo** (capacità di membrature e collegamenti secondo il **§4.4**, senza
     requisiti aggiuntivi).
   - Nel comportamento dissipativo, localizza le **zone dissipative nei collegamenti** (o in elementi
     specificatamente progettati); le **membrature lignee** si considerano **a comportamento elastico**.
   - Applica la **progettazione in capacità**: le componenti non dissipative si dimensionano sulla capacità della
     zona dissipativa **amplificata del fattore di sovraresistenza ηRd** (Tab. 7.2.I); valori inferiori sono
     ammessi solo se **≥ 1,3 (CD "A")** / **≥ 1,1 (CD "B")** e giustificati con evidenze teorico-sperimentali.

2. **Materiali e proprietà delle zone dissipative (§7.7.2)**
   - Per il legno si applica il **§4.4**; nelle zone dissipative solo materiali/mezzi con **comportamento
     oligociclico**.
   - Le **unioni incollate** sono in generale **non dissipative** (salvo in serie con un elemento duttile in
     capacità); i **nodi di carpenteria** sono dissipativi solo se evitano rotture fragili e sono anti-sconnessione.
   - **Pannelli di rivestimento** (pareti di taglio/diaframmi): particelle **≥ 13 mm**, compensato **≥ 9 mm**,
     OSB **≥ 12 mm** (a coppia) / **≥ 15 mm** (singoli); connettori a gambo cilindrico conformi al **§11.7.8**.

3. **Fattori di comportamento (§7.7.3)**
   - **q0** (valore di base) dalla **Tab. 7.3.II** per la classe di duttilità; nel framework generale **q = q0·KR**
     (§7.3.1).
   - Per le strutture dissipative è **obbligo del Progettista giustificare q0** sulla base della capacità
     dissipativa del sistema e dei criteri di dimensionamento dei collegamenti (progettazione in capacità,
     evitando rotture fragili).

4. **Output**: scheda con comportamento e classe di duttilità, esito requisiti materiali/pannelli (conformi/non
   conformi, con il valore mancante), q0 di riferimento (con rinvio alla Tab. 7.3.II) e rinvio ai paragrafi.
   Segnala sempre che le **verifiche** restano fuori scope.

## Cosa NON fare

- Non eseguire le **verifiche** di resistenza/duttilità né calcolare il **q0 numerico** (Tab. 7.3.II) per
  tipologia: rinvia al progettista.
- Non progettare i **collegamenti**; non trattare i requisiti **statici** (§4.4) né il framework **generale** del
  fattore q (§7.3.1): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-7-7.md`.
