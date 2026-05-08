#!/usr/bin/env python3
"""Test suite per carichi_atmosferici.py - consistenza interna formule NTC 2018."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from carichi_atmosferici import (  # noqa: E402
    CATEGORIE_ESPOSIZIONE,
    CLASSI_ESPOSIZIONE_NEVE,
    RHO_ARIA,
    ZONE_NEVE,
    calcola_carico_neve,
    calcola_pressione_vento,
    carico_neve_al_suolo_qsk,
    coefficiente_esposizione_ce,
    coefficiente_esposizione_neve_ce,
    coefficiente_forma_mu1,
    coefficiente_ritorno_cr,
    pressione_cinetica_qr,
    velocita_progetto_vr,
    velocita_riferimento_vb,
)


class TestVelocitaRiferimento(unittest.TestCase):
    def test_pianura_ritorna_v_b_0(self):
        self.assertAlmostEqual(velocita_riferimento_vb(25.0, 1000.0, 0.40, 100.0), 25.0)

    def test_alla_quota_a_0_ritorna_v_b_0(self):
        # raccordo: a_s = a_0
        self.assertAlmostEqual(velocita_riferimento_vb(25.0, 1000.0, 0.40, 1000.0), 25.0)

    def test_quota_oltre_a_0_aumenta_velocita(self):
        # a_s = 1500 m, a_0 = 1000 m, k_s = 0.40 -> v_b = 25 * (1 + 0.4 * 0.5) = 30
        self.assertAlmostEqual(
            velocita_riferimento_vb(25.0, 1000.0, 0.40, 1500.0), 30.0, places=6
        )

    def test_quota_negativa_solleva(self):
        with self.assertRaises(ValueError):
            velocita_riferimento_vb(25.0, 1000.0, 0.40, -10.0)

    def test_quota_oltre_1500_solleva(self):
        with self.assertRaises(ValueError):
            velocita_riferimento_vb(25.0, 1000.0, 0.40, 1600.0)

    def test_v_b_0_non_positivo_solleva(self):
        with self.assertRaises(ValueError):
            velocita_riferimento_vb(0.0, 1000.0, 0.40, 100.0)

    def test_nan_solleva(self):
        with self.assertRaises(ValueError):
            velocita_riferimento_vb(float("nan"), 1000.0, 0.40, 100.0)


class TestCoefficienteRitorno(unittest.TestCase):
    def test_t_r_50_anni_e_uno(self):
        self.assertEqual(coefficiente_ritorno_cr(50.0), 1.0)

    def test_t_r_alto_supera_uno(self):
        # T_R 200 anni: c_r > 1
        self.assertGreater(coefficiente_ritorno_cr(200.0), 1.0)

    def test_t_r_basso_inferiore_uno(self):
        # T_R 10 anni: c_r < 1
        self.assertLess(coefficiente_ritorno_cr(10.0), 1.0)

    def test_fuori_intervallo_solleva(self):
        with self.assertRaises(ValueError):
            coefficiente_ritorno_cr(2.0)
        with self.assertRaises(ValueError):
            coefficiente_ritorno_cr(1000.0)

    def test_monotonia(self):
        # c_r monotono crescente in T_R nell'intervallo valido
        valori = [coefficiente_ritorno_cr(t) for t in (5, 10, 20, 50, 100, 200, 500)]
        for i in range(len(valori) - 1):
            self.assertLess(valori[i], valori[i + 1] + 1e-9)


class TestPressioneCinetica(unittest.TestCase):
    def test_formula(self):
        # v_r = 25 m/s, q_r = 0.5 * 1.25 * 625 = 390.625 N/m^2
        self.assertAlmostEqual(pressione_cinetica_qr(25.0), 0.5 * RHO_ARIA * 625.0)

    def test_v_r_negativo_solleva(self):
        with self.assertRaises(ValueError):
            pressione_cinetica_qr(-1.0)

    def test_velocita_progetto(self):
        self.assertAlmostEqual(velocita_progetto_vr(25.0, 1.2), 30.0)


class TestCoefficienteEsposizione(unittest.TestCase):
    def test_categorie_complete(self):
        for cat in ("I", "II", "III", "IV", "V"):
            c_e = coefficiente_esposizione_ce(20.0, cat)
            self.assertGreater(c_e, 0.0)
            self.assertLess(c_e, 10.0)

    def test_z_minore_zmin_e_clampato(self):
        # categoria IV ha z_min = 8 m; c_e(2) = c_e(8)
        c_e_basso = coefficiente_esposizione_ce(2.0, "IV")
        c_e_zmin = coefficiente_esposizione_ce(8.0, "IV")
        self.assertAlmostEqual(c_e_basso, c_e_zmin)

    def test_categoria_invalida_solleva(self):
        with self.assertRaises(ValueError):
            coefficiente_esposizione_ce(10.0, "VI")

    def test_categoria_case_insensitive(self):
        a = coefficiente_esposizione_ce(10.0, "ii")
        b = coefficiente_esposizione_ce(10.0, "II")
        self.assertAlmostEqual(a, b)

    def test_z_zero_solleva(self):
        with self.assertRaises(ValueError):
            coefficiente_esposizione_ce(0.0, "II")

    def test_monotonia_in_z(self):
        # c_e crescente in z (oltre z_min) per ogni categoria
        for cat in CATEGORIE_ESPOSIZIONE:
            zmin = CATEGORIE_ESPOSIZIONE[cat]["z_min"]
            valori = [
                coefficiente_esposizione_ce(z, cat) for z in (zmin, zmin + 5, zmin + 50)
            ]
            self.assertLessEqual(valori[0], valori[1])
            self.assertLessEqual(valori[1], valori[2])

    def test_formula_esplicita(self):
        # categoria II: k_r=0.19, z_0=0.05, c_t=1, z=10 m
        # ln(10/0.05) = ln(200) ~ 5.298317
        # c_e = 0.19^2 * 1 * 5.298 * (7 + 5.298) = 0.0361 * 5.298 * 12.298
        expected = 0.19 ** 2 * math.log(10.0 / 0.05) * (7.0 + math.log(10.0 / 0.05))
        self.assertAlmostEqual(coefficiente_esposizione_ce(10.0, "II"), expected)


class TestPressioneVentoEndToEnd(unittest.TestCase):
    def test_caso_completo(self):
        res = calcola_pressione_vento(
            v_b_0=25.0,
            a_0=1000.0,
            k_s=0.40,
            a_s=300.0,           # pianura
            categoria_esposizione="II",
            z=10.0,
            c_p=0.8,
            c_d=1.0,
            c_t=1.0,
            t_r_anni=50.0,
        )
        # a_s 300 < a_0 1000 -> v_b = 25
        self.assertAlmostEqual(res.v_b, 25.0)
        self.assertEqual(res.c_r, 1.0)
        self.assertAlmostEqual(res.v_r, 25.0)
        self.assertAlmostEqual(res.q_r, 390.625)
        # p > 0
        self.assertGreater(res.p, 0)

    def test_serializzazione_dict(self):
        res = calcola_pressione_vento(
            v_b_0=25.0, a_0=1000.0, k_s=0.40, a_s=100.0,
            categoria_esposizione="III", z=15.0, c_p=1.0,
        )
        d = res.as_dict()
        self.assertIn("input", d)
        self.assertIn("intermedi", d)
        self.assertIn("output", d)
        self.assertIn("riferimenti_ntc", d)
        self.assertIn("p_kN_m2", d["output"])

    def test_t_r_diverso_50(self):
        res_50 = calcola_pressione_vento(
            v_b_0=25.0, a_0=1000.0, k_s=0.40, a_s=100.0,
            categoria_esposizione="II", z=10.0, c_p=0.8, t_r_anni=50.0,
        )
        res_200 = calcola_pressione_vento(
            v_b_0=25.0, a_0=1000.0, k_s=0.40, a_s=100.0,
            categoria_esposizione="II", z=10.0, c_p=0.8, t_r_anni=200.0,
        )
        # T_R 200 -> v_r maggiore -> q_r maggiore -> p maggiore
        self.assertGreater(res_200.p, res_50.p)


# ---------------------------------------------------------------------------
# NEVE
# ---------------------------------------------------------------------------

class TestQskZone(unittest.TestCase):
    def test_zone_a_quota_zero(self):
        self.assertAlmostEqual(carico_neve_al_suolo_qsk("I-Alpina", 0.0), 1.50)
        self.assertAlmostEqual(carico_neve_al_suolo_qsk("I-Mediterranea", 0.0), 1.50)
        self.assertAlmostEqual(carico_neve_al_suolo_qsk("II", 0.0), 1.00)
        self.assertAlmostEqual(carico_neve_al_suolo_qsk("III", 0.0), 0.60)

    def test_zone_a_200m_pianeggia(self):
        for z in ZONE_NEVE:
            self.assertAlmostEqual(
                carico_neve_al_suolo_qsk(z, 200.0),
                carico_neve_al_suolo_qsk(z, 0.0),
            )

    def test_oltre_200m_cresce(self):
        for z in ZONE_NEVE:
            self.assertGreater(
                carico_neve_al_suolo_qsk(z, 1000.0),
                carico_neve_al_suolo_qsk(z, 200.0),
            )

    def test_zona_invalida_solleva(self):
        with self.assertRaises(ValueError):
            carico_neve_al_suolo_qsk("IV", 100.0)

    def test_quota_negativa_solleva(self):
        with self.assertRaises(ValueError):
            carico_neve_al_suolo_qsk("II", -1.0)

    def test_formula_alpina_1000m(self):
        # 1.39 * (1 + (1000/728)^2)
        expected = 1.39 * (1.0 + (1000.0 / 728.0) ** 2)
        self.assertAlmostEqual(carico_neve_al_suolo_qsk("I-Alpina", 1000.0), expected)

    def test_zona_case_insensitive(self):
        # accetta varianti di case e separatori
        ref = carico_neve_al_suolo_qsk("I-Alpina", 500.0)
        for variante in ("i-alpina", "I-ALPINA", "i alpina", "I-Alpina "):
            self.assertAlmostEqual(carico_neve_al_suolo_qsk(variante, 500.0), ref)


class TestMu1(unittest.TestCase):
    def test_pendenza_bassa(self):
        self.assertAlmostEqual(coefficiente_forma_mu1(0.0), 0.8)
        self.assertAlmostEqual(coefficiente_forma_mu1(15.0), 0.8)
        self.assertAlmostEqual(coefficiente_forma_mu1(30.0), 0.8)

    def test_pendenza_intermedia(self):
        # 45 deg: 0.8 * (60-45)/30 = 0.4
        self.assertAlmostEqual(coefficiente_forma_mu1(45.0), 0.4)

    def test_pendenza_alta(self):
        self.assertAlmostEqual(coefficiente_forma_mu1(60.0), 0.0)
        self.assertAlmostEqual(coefficiente_forma_mu1(75.0), 0.0)

    def test_continuita_30(self):
        # raccordo a 30 deg: continuo
        self.assertAlmostEqual(coefficiente_forma_mu1(30.0), 0.8)
        # appena sopra 30
        self.assertAlmostEqual(coefficiente_forma_mu1(30.001), 0.8 * (60.0 - 30.001) / 30.0, places=4)

    def test_alpha_fuori_dominio(self):
        with self.assertRaises(ValueError):
            coefficiente_forma_mu1(-1.0)
        with self.assertRaises(ValueError):
            coefficiente_forma_mu1(91.0)


class TestCEneve(unittest.TestCase):
    def test_classi(self):
        self.assertEqual(coefficiente_esposizione_neve_ce("battuta_dai_venti"), 0.9)
        self.assertEqual(coefficiente_esposizione_neve_ce("normale"), 1.0)
        self.assertEqual(coefficiente_esposizione_neve_ce("riparata"), 1.1)

    def test_normalizzazione(self):
        # accetta varianti con spazi/trattini/case
        self.assertEqual(coefficiente_esposizione_neve_ce("Normale"), 1.0)
        self.assertEqual(coefficiente_esposizione_neve_ce("battuta-dai-venti"), 0.9)
        self.assertEqual(coefficiente_esposizione_neve_ce("battuta dai venti"), 0.9)

    def test_classe_invalida(self):
        with self.assertRaises(ValueError):
            coefficiente_esposizione_neve_ce("scarsa")


class TestCaricoNeveEndToEnd(unittest.TestCase):
    def test_caso_pianura_alpina_normale(self):
        # zona I-Alpina, a_s=100, alpha=15, c_E normale
        # q_sk = 1.50, mu_1 = 0.8, c_E = 1.0, c_t = 1.0
        # q_s = 0.8 * 1.50 * 1.0 * 1.0 = 1.20 kN/m2
        res = calcola_carico_neve("I-Alpina", 100.0, 15.0, "normale")
        self.assertAlmostEqual(res.q_sk, 1.50)
        self.assertAlmostEqual(res.mu_1, 0.8)
        self.assertAlmostEqual(res.q_s, 1.20)

    def test_pendenza_oltre_60_zero(self):
        res = calcola_carico_neve("II", 100.0, 70.0, "normale")
        self.assertEqual(res.mu_1, 0.0)
        self.assertEqual(res.q_s, 0.0)

    def test_serializzazione_dict(self):
        res = calcola_carico_neve("II", 500.0, 20.0, "riparata")
        d = res.as_dict()
        self.assertIn("output", d)
        self.assertIn("q_s_kN_m2", d["output"])
        self.assertIn("riferimenti_ntc", d)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

class TestCLI(unittest.TestCase):
    def _run(self, cmd, payload):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(payload, fh)
            path = fh.name
        try:
            module_path = os.path.join(HERE, "carichi_atmosferici.py")
            res = subprocess.run(
                [sys.executable, module_path, cmd, "--input-json", path],
                capture_output=True,
                text=True,
            )
            return res
        finally:
            os.unlink(path)

    def test_vento_cli_ok(self):
        res = self._run(
            "vento",
            {
                "v_b_0": 25.0, "a_0": 1000.0, "k_s": 0.40, "a_s": 100.0,
                "categoria_esposizione": "II", "z": 10.0, "c_p": 0.8,
            },
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        out = json.loads(res.stdout)
        self.assertIn("p_kN_m2", out["output"])

    def test_neve_cli_ok(self):
        res = self._run(
            "neve",
            {"zona": "II", "a_s": 300.0, "alpha_deg": 15.0, "classe_esposizione": "normale"},
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        out = json.loads(res.stdout)
        self.assertIn("q_s_kN_m2", out["output"])

    def test_vento_campo_mancante(self):
        res = self._run(
            "vento",
            {"v_b_0": 25.0},  # incompleto
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("ERRORE", res.stderr)

    def test_neve_zona_invalida(self):
        res = self._run(
            "neve",
            {"zona": "IV", "a_s": 100.0, "alpha_deg": 10.0},
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("ERRORE", res.stderr)


if __name__ == "__main__":
    unittest.main()
