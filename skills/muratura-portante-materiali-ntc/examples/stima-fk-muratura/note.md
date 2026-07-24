# Nota — stima della resistenza a compressione fk

- **Ancoraggio**: fbk = 0,8·fbm (elementi artificiali), la validità per giunti 5-15 mm e i valori della Tab.
  11.10.VI provengono da `../../references/fonti/ntc2018-par-11-10.md` (§11.10.3.1.2), verificati sull'immagine
  della pagina PDF 367 (GU 363).
- **fbk = 0,8·fbm vs 0,75·fbm**: il fattore 0,8 vale per gli **elementi artificiali**; per gli **elementi naturali
  di pietra squadrata** si usa fbk = 0,75·fbm [11.10.3] e la Tab. 11.10.VII (stessi valori).
- **Interpolazione**: nell'esempio fbk = 10,0 è un valore tabellato, quindi fk si legge direttamente. Per valori
  intermedi (es. fbk = 8,0) si interpola linearmente; l'**estrapolazione è sempre vietata**.
- **Alternativa sperimentale**: in alternativa alla stima, fk può essere determinata su n muretti (n ≥ 6, UNI EN
  1052-1); la tabella è una via di progetto semplificata.
- **Limite della skill**: fk è caratteristico; la resistenza di progetto (fd = fk/γM) e le verifiche sono al §4.5
  (skill dedicata) e restano fuori scope.
