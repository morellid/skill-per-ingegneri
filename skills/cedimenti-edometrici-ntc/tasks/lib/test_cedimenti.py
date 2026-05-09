#!/usr/bin/env python3
"""Test suite per cedimenti.py - consistenza interna formule edometriche."""

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

from cedimenti import (  # noqa: E402
    calcola_cedimento,
    cedimento_nc,
    cedimento_oc,
    ocr,
)


class TestOCR(unittest.TestCase):
    def test_ocr_uguale_uno_per_normalmente_consolidato(self):
        self.assertAlmostEqual(ocr(100.0, 100.0), 1.0)

    def test_ocr_maggiore_uno_per_over_consolidato(self):
        self.assertAlmostEqual(ocr(200.0, 100.0), 2.0)

    def test_ocr_input_invalido(self):
        with self.assertRaises(ValueError):
            ocr(0.0, 100.0)
        with self.assertRaises(ValueError):
            ocr(100.0, -10.0)


class TestCedimentoOC(unittest.TestCase):
    def test_formula_oc(self):
        # h0=2, e0=0.8, Cr=0.05, sigma_0=100, sigma_f=150
        # Delta h = 2 / 1.8 * 0.05 * log10(150/100) = 1.1111 * 0.05 * 0.17609 = 0.009783
        d = cedimento_oc(2.0, 0.8, 0.05, 100.0, 150.0)
        expected = 2.0 / 1.8 * 0.05 * math.log10(1.5)
        self.assertAlmostEqual(d, expected)

    def test_oc_sigma_uguale_zero_cedimento_zero(self):
        # sigma_f == sigma_0 -> log10(1) = 0 -> Delta h = 0
        self.assertAlmostEqual(cedimento_oc(2.0, 0.8, 0.05, 100.0, 100.0), 0.0)

    def test_oc_scarico_solleva(self):
        with self.assertRaises(ValueError):
            cedimento_oc(2.0, 0.8, 0.05, 100.0, 50.0)

    def test_oc_input_negativi(self):
        with self.assertRaises(ValueError):
            cedimento_oc(-2.0, 0.8, 0.05, 100.0, 150.0)
        with self.assertRaises(ValueError):
            cedimento_oc(2.0, 0.8, -0.05, 100.0, 150.0)
        with self.assertRaises(ValueError):
            cedimento_oc(2.0, 0.8, 0.05, 0.0, 150.0)


class TestCedimentoNC(unittest.TestCase):
    def test_formula_nc(self):
        # h0=2, e0=0.8, Cc=0.30, sigma_0=100, sigma_f=200
        # Delta h = 2/1.8 * 0.30 * log10(2) = 1.1111 * 0.30 * 0.30103 = 0.10034
        d = cedimento_nc(2.0, 0.8, 0.30, 100.0, 200.0)
        expected = 2.0 / 1.8 * 0.30 * math.log10(2.0)
        self.assertAlmostEqual(d, expected)

    def test_nc_maggiore_di_oc_a_parita_di_carico(self):
        # Cc > Cr di solito => cedimento NC > cedimento OC sullo stesso intervallo
        d_oc = cedimento_oc(2.0, 0.8, 0.05, 100.0, 200.0)
        d_nc = cedimento_nc(2.0, 0.8, 0.30, 100.0, 200.0)
        self.assertLess(d_oc, d_nc)


class TestEndToEnd(unittest.TestCase):
    def test_caso_oc_intero(self):
        # sigma_p = 250, sigma_0 = 100, delta = 100 -> sigma_f = 200 <= sigma_p -> ramo OC
        res = calcola_cedimento(
            h0=2.0, e0=0.8, c_c=0.30, c_r=0.05,
            sigma_0=100.0, sigma_p=250.0, delta_sigma=100.0,
        )
        self.assertEqual(res.ramo, "OC")
        self.assertAlmostEqual(res.delta_h_nc_m, 0.0)
        self.assertGreater(res.delta_h_oc_m, 0.0)
        self.assertAlmostEqual(res.delta_h_m, res.delta_h_oc_m)

    def test_caso_nc_intero(self):
        # sigma_p = 100 = sigma_0 -> NC
        res = calcola_cedimento(
            h0=2.0, e0=0.8, c_c=0.30, c_r=0.05,
            sigma_0=100.0, sigma_p=100.0, delta_sigma=100.0,
        )
        self.assertEqual(res.ramo, "NC")
        self.assertAlmostEqual(res.delta_h_oc_m, 0.0)
        self.assertGreater(res.delta_h_nc_m, 0.0)

    def test_caso_transizione(self):
        # sigma_0 = 100, sigma_p = 150, delta = 200 -> sigma_f = 300; sigma_p in mezzo
        res = calcola_cedimento(
            h0=2.0, e0=0.8, c_c=0.30, c_r=0.05,
            sigma_0=100.0, sigma_p=150.0, delta_sigma=200.0,
        )
        self.assertEqual(res.ramo, "transizione")
        self.assertGreater(res.delta_h_oc_m, 0.0)
        self.assertGreater(res.delta_h_nc_m, 0.0)
        self.assertAlmostEqual(res.delta_h_m, res.delta_h_oc_m + res.delta_h_nc_m)

    def test_caso_conforme_esempio_valori_pinnati(self):
        # Riproducibilita' valori expected-output.md di
        # examples/caso-conforme-strato-argilla-OC-transizione/.
        # Ancora i numeri attesi al modulo: se cambia la formula, il test rompe.
        res = calcola_cedimento(
            h0=2.0, e0=0.8, c_c=0.30, c_r=0.05,
            sigma_0=100.0, sigma_p=150.0, delta_sigma=200.0,
        )
        self.assertEqual(res.ramo, "transizione")
        self.assertAlmostEqual(res.sigma_f, 300.0)
        self.assertAlmostEqual(res.ocr, 1.5)
        self.assertAlmostEqual(res.delta_h_oc_m, 0.009782848, places=9)
        self.assertAlmostEqual(res.delta_h_nc_m, 0.100343332, places=9)
        self.assertAlmostEqual(res.delta_h_m, 0.110126180, places=9)
        self.assertAlmostEqual(res.delta_h_mm, 110.126180, places=6)
        self.assertAlmostEqual(res.epsilon_media, 0.055063090, places=9)
        self.assertEqual(res.avvertenze, [])

    def test_continuita_a_sigma_p(self):
        # cedimento totale per delta tale che sigma_f = sigma_p deve coincidere col solo OC
        # e con la transizione che ha NC ~ 0
        res_oc = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 200.0, 100.0)  # sigma_f=200=sigma_p
        self.assertEqual(res_oc.ramo, "OC")
        # appena sopra
        res_eps = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 200.0, 100.001)
        self.assertEqual(res_eps.ramo, "transizione")
        # delta totale deve essere continuo
        self.assertAlmostEqual(res_oc.delta_h_m, res_eps.delta_h_m, places=5)

    def test_delta_zero_ritorna_zero(self):
        res = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 0.0)
        self.assertAlmostEqual(res.delta_h_m, 0.0)
        self.assertTrue(any("delta_sigma = 0" in a for a in res.avvertenze))

    def test_ocr_calcolato(self):
        res = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 250.0, 100.0)
        self.assertAlmostEqual(res.ocr, 2.5)

    def test_epsilon_consistente(self):
        res = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 200.0)
        self.assertAlmostEqual(res.epsilon_media, res.delta_h_m / res.h0)

    def test_cedimento_in_mm(self):
        res = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 200.0)
        self.assertAlmostEqual(res.delta_h_mm, res.delta_h_m * 1000.0)

    def test_monotonia_delta_sigma(self):
        # cedimento crescente in delta_sigma a parita' di altri parametri
        d_a = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 50.0).delta_h_m
        d_b = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 100.0).delta_h_m
        d_c = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 200.0).delta_h_m
        self.assertLess(d_a, d_b)
        self.assertLess(d_b, d_c)

    def test_monotonia_h0(self):
        # cedimento proporzionale a h0
        d_1 = calcola_cedimento(1.0, 0.8, 0.30, 0.05, 100.0, 100.0, 100.0).delta_h_m
        d_2 = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 100.0).delta_h_m
        self.assertAlmostEqual(d_2, 2.0 * d_1)

    def test_avvertenza_epsilon_grande(self):
        # forzo cedimento elevato (Cc altissimo)
        res = calcola_cedimento(2.0, 0.8, 2.0, 0.10, 100.0, 100.0, 1000.0)
        self.assertGreater(res.epsilon_media, 0.10)
        self.assertTrue(any("epsilon" in a for a in res.avvertenze))

    def test_cr_maggiore_cc_solleva(self):
        with self.assertRaises(ValueError):
            calcola_cedimento(2.0, 0.8, 0.05, 0.30, 100.0, 100.0, 100.0)

    def test_sigma_p_minore_sigma_0_solleva(self):
        with self.assertRaises(ValueError):
            calcola_cedimento(2.0, 0.8, 0.30, 0.05, 200.0, 100.0, 50.0)

    def test_input_negativi(self):
        with self.assertRaises(ValueError):
            calcola_cedimento(-2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 100.0)
        with self.assertRaises(ValueError):
            calcola_cedimento(2.0, 0.0, 0.30, 0.05, 100.0, 100.0, 100.0)
        with self.assertRaises(ValueError):
            calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, -50.0)
        with self.assertRaises(ValueError):
            calcola_cedimento(float("nan"), 0.8, 0.30, 0.05, 100.0, 100.0, 100.0)

    def test_serializzazione_dict(self):
        res = calcola_cedimento(2.0, 0.8, 0.30, 0.05, 100.0, 100.0, 100.0)
        d = res.as_dict()
        self.assertIn("input", d)
        self.assertIn("derivati", d)
        self.assertIn("output", d)
        self.assertIn("delta_h_mm", d["output"])
        self.assertIn("OCR", d["derivati"])
        self.assertIn("ramo", d["derivati"])
        self.assertIn("riferimenti", d)


class TestCLI(unittest.TestCase):
    def _run(self, payload):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(payload, fh)
            path = fh.name
        try:
            module_path = os.path.join(HERE, "cedimenti.py")
            res = subprocess.run(
                [sys.executable, module_path, "--input-json", path],
                capture_output=True,
                text=True,
            )
            return res
        finally:
            os.unlink(path)

    def test_cli_ok(self):
        res = self._run(
            {
                "h0": 2.0, "e0": 0.8, "Cc": 0.30, "Cr": 0.05,
                "sigma_0": 100.0, "sigma_p": 100.0, "delta_sigma": 100.0,
            }
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        out = json.loads(res.stdout)
        self.assertIn("delta_h_mm", out["output"])
        self.assertIn("ramo", out["derivati"])

    def test_cli_campo_mancante(self):
        res = self._run({"h0": 2.0, "e0": 0.8})
        self.assertEqual(res.returncode, 2)
        self.assertIn("ERRORE", res.stderr)

    def test_cli_cr_maggiore_cc(self):
        res = self._run(
            {
                "h0": 2.0, "e0": 0.8, "Cc": 0.05, "Cr": 0.30,
                "sigma_0": 100.0, "sigma_p": 100.0, "delta_sigma": 100.0,
            }
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("Cr", res.stderr)

    def test_cli_sigma_p_minore_sigma_0(self):
        res = self._run(
            {
                "h0": 2.0, "e0": 0.8, "Cc": 0.30, "Cr": 0.05,
                "sigma_0": 200.0, "sigma_p": 100.0, "delta_sigma": 50.0,
            }
        )
        self.assertEqual(res.returncode, 2)
        self.assertIn("sigma_p", res.stderr)


if __name__ == "__main__":
    unittest.main()
