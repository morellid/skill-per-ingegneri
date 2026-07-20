# Nota

Esempio ancorato al **§3.6.1.5.1** (incendio di progetto, curva nominale standard) delle NTC 2018, trascritto
in `references/fonti/ntc2018-par-3-6-1.md`.

Punti verificati sul testo:

- **[3.6.2]**: **θg = 20 + 345·log10(8t + 1)** °C, con t in minuti primi; è la curva nominale standard per
  materiali cellulosici.
- **Curva nominale** → temperature per il tempo pari alla classe, **senza raffreddamento** (§3.6.1.5.1); la
  verifica mantiene la resistenza per il **tempo della classe** (§3.6.1.5.4).
- Valori del caso: t = 30 → log10(241) ≈ 2,382 → θg ≈ 842 °C; t = 60 → log10(481) ≈ 2,682 → θg ≈ 945 °C
  (coerente con la ISO 834). Alternative: idrocarburi [3.6.3], esterna [3.6.4].

I calcoli sono applicazione diretta della formula [3.6.2] (illustrazione). La skill **non** esegue l'analisi
termica negli elementi né la verifica meccanica, e **non** fornisce le proprietà dei materiali ad alta
temperatura (Eurocodici parte 1-2).
