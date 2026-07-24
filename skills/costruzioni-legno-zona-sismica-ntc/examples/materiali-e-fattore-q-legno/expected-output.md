# Esempio — Output atteso: materiali/pannelli e comportamento dissipativo (parete a telaio)

> Supporto documentale (NTC 2018, par. 7.7). Non è una verifica strutturale: le verifiche di resistenza/duttilità
> restano a carico del progettista.

## 1. Comportamento e classe di duttilità (§7.7.1)

- Adottando il **comportamento strutturale dissipativo**, la struttura deve appartenere alla **CD "A"** o alla
  **CD "B"** (nel rispetto dei requisiti del §7.7.3).
- Le **zone dissipative** vanno localizzate nei **collegamenti** (qui: la chiodatura di collegamento tra telaio e
  rivestimento delle pareti di taglio); le **membrature lignee** si considerano a **comportamento elastico**.
- In progettazione in capacità, le componenti non dissipative si dimensionano sulla capacità della zona
  dissipativa **× ηRd** (Tab. 7.2.I); eventuali valori inferiori solo se **≥ 1,3 (CD "A")** / **≥ 1,1 (CD "B")** e
  giustificati.

## 2. Requisiti dei pannelli di rivestimento (§7.7.2)

| Requisito (§7.7.2) | Limite | Valore proposto | Esito |
|---|---|---|---|
| Pannello OSB (UNI EN 300), disposto singolarmente | spessore ≥ 15 mm | 15 mm | ✅ |
| Mezzi di unione a gambo cilindrico | conformi §11.7.8 | conformi | ✅ |
| Unioni incollate nelle zone dissipative | in generale non dissipative | assenti | ✅ (non pertinente) |

- Il pannello **OSB da 15 mm disposto singolarmente** rispetta il minimo del §7.7.2 (≥ 15 mm se singolo; sarebbe
  ≥ 12 mm se disposto a coppia). **Requisito soddisfatto.**
- (Per confronto: particelle ≥ 13 mm, compensato ≥ 9 mm.)

## 3. Fattore di comportamento q0 (§7.7.3)

- **q0 si ricava dalla Tab. 7.3.II** in funzione della tipologia strutturale e della classe di duttilità; nel
  framework generale **q = q0·KR** (§7.3.1).
- Per una struttura dissipativa è **obbligo del Progettista giustificare la scelta di q0**, sulla base della
  capacità dissipativa del sistema e dei criteri di dimensionamento dei collegamenti (progettazione in capacità).

## Sintesi

- Comportamento **dissipativo** → **CD "A"/CD "B"**; zone dissipative nella **chiodatura** delle pareti di taglio.
- **Pannello OSB 15 mm singolo conforme** al §7.7.2.
- **q0 da Tab. 7.3.II**, da giustificare a cura del Progettista.

**Fuori scope**: verifiche di resistenza/duttilità, q0 numerico, requisiti statici §4.4 e framework del fattore q
§7.3.1 (skill dedicate). Non sostituisce il progettista.
