# Nota

Esempio ancorato al **§4.3.4.3.1.2** (resistenza dei connettori a piolo, [4.3.9]-[4.3.14]) delle NTC 2018,
trascritto in `references/fonti/ntc2018-par-4-3.md`.

Punti verificati sul testo:

- **PRd,a = 0,8·ftk·(π·d²/4)/γV** [4.3.9] e **PRd,c = 0,29·α·d²·√(fck·Ecm)/γV** [4.3.10]; si assume il
  **minore** dei due.
- **γV = 1,25** (§4.3.3); **ftk ≤ 500 MPa**; **d = 16-25 mm**.
- **α = 0,2·(hsc/d + 1)** per **3 ≤ hsc/d ≤ 4** [4.3.11a], **α = 1,0** per **hsc/d > 4** [4.3.11b]. Nel caso
  (hsc/d ≈ 5,26) → α = 1,0.
- **Lamiera grecata**: **kl** [4.3.13] (greche parallele) e **kt** [4.3.14] (greche trasversali; solo se
  ftk < 450 MPa; kt ≤ Tab. 4.3.II).

La skill **non** calcola PRd (serve Ecm dal §11.2, non trattato) né dimensiona la connessione: fornisce
formule, coefficienti e limiti. La Tab. 4.3.II (limiti di kt) è una tabella figurata, non riprodotta →
norma/EC4.
