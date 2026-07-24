# Task — Qualifica i prodotti in legno e l'accettazione in cantiere (NTC 2018 §11.7.2-11.7.6, §11.7.10)

Supporto documentale per individuare la **norma di riferimento** e la **modalità di qualificazione** dei prodotti
in legno strutturale (§11.7.2-11.7.6) e per impostare i **controlli di accettazione** in cantiere (§11.7.10)
secondo le NTC 2018 (DM 17/1/2018). **Non** esegue le verifiche di progetto.

Fonte: `../references/fonti/ntc2018-par-11-7.md`; checklist: `../references/estratti/legno-materiali-checklist.md`.

## Input tipico

- Tipo di prodotto: **legno massiccio**, **legno con giunti a dita**, **legno lamellare/massiccio incollato**,
  **pannelli a base di legno**, altri derivati.
- Classe di resistenza delle tavole (per il lamellare) e documentazione di fornitura (marcatura CE / certificato).

## Passi

1. **Individua la norma e il caso di qualificazione (§11.7.2-11.7.6)**
   - **Legno massiccio** (§11.7.2): **UNI EN 14081-1** + Marcatura CE (caso A) o qualificazione §11.7.10 (caso B);
     classificato **elemento per elemento**; classi di resistenza **UNI EN 338**; profili UNI 11035; prove UNI EN 384.
   - **Legno con giunti a dita** (§11.7.3): **caso C** (Linee Guida); singoli elementi UNI EN 14081-1; sistema
     qualità UNI EN ISO 9001 certificato da organismo terzo.
   - **Legno lamellare/massiccio incollato** (§11.7.4): **UNI EN 14080** + Marcatura CE; tavole UNI EN 14081-1;
     **classi di resistenza delle tavole > C30 solo con classificazione a macchina**; lamelle classificate
     individualmente.
   - **Pannelli a base di legno** (§11.7.5): **UNI EN 13986** (caso A); valori caratteristici da UNI EN
     12369-1/2/3.
   - **Altri prodotti derivati** (§11.7.6): **caso C** (Linee Guida CSLP).

2. **Controlli di accettazione in cantiere (§11.7.10)**
   - Il **Direttore dei Lavori** verifica l'**identificazione e rintracciabilità** dei prodotti qualificati, la
     **documentazione di accompagnamento** (marcatura CE/certificato, manuale di posa) e la corrispondenza con
     quanto qualificato/marcato CE e indicato in **progetto**; può far eseguire ulteriori prove presso laboratori
     abilitati.

3. **Output**: scheda con norma di riferimento e caso di qualificazione per il prodotto, note sulla classificazione
   (a vista/a macchina; limite C30 per il lamellare) e checklist di accettazione in cantiere. Segnala che le
   **verifiche di progetto** restano fuori scope.

## Cosa NON fare

- Non calcolare le **resistenze di progetto** (fd = kmod·fk/γM) né eseguire le verifiche (§4.4).
- Non applicare la via a macchina/a vista fuori dai casi indicati (per le tavole del lamellare con classi > C30
  solo classificazione a macchina).
- Non trattare adesivi/collegamenti/durabilità (§§11.7.7-11.7.9) né l'accettazione di muratura/cls/acciaio
  (§§11.10/11.2/11.3): rinvia alle skill dedicate.
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-11-7.md`.
