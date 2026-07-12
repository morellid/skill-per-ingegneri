#!/usr/bin/env python3
"""Test suite per periodo_t1.py - consistenza con NTC 2018 [7.3.6] e Circ. 7/2019 [C7.3.2]."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from periodo_t1 import (  # noqa: E402
    C1_TABELLA,
    H_MAX_FORMULA_M,
    LAMBDA_RIDOTTO,
    LAMBDA_UNITARIO,
    stima_t1,
    t1_da_altezza,
    t1_da_spostamento,
)


class TestFormula736(unittest.TestCase):
    """[7.3.6] NTC 2018: T1 = 2*sqrt(d)."""

    def test_valori_chiusi(self):
        # d = 0,04 m -> T1 = 2*0,2 = 0,4 s (calcolo chiuso della formula)
        self.assertAlmostEqual(t1_da_spostamento(0.04), 0.4, places=12)
        # d = 0,0625 m -> T1 = 2*0,25 = 0,5 s
        self.assertAlmostEqual(t1_da_spostamento(0.0625), 0.5, places=12)

    def test_monotonia(self):
        self.assertLess(t1_da_spostamento(0.01), t1_da_spostamento(0.09))

    def test_input_invalidi(self):
        for bad in (0.0, -1.0, float("nan"), float("inf"), "x", None):
            with self.assertRaises(ValueError):
                t1_da_spostamento(bad)


class TestFormulaC732(unittest.TestCase):
    """[C7.3.2] Circ. 7/2019: T1 = C1*H^(3/4)."""

    def test_coefficienti_tabella(self):
        # Valori C1 trascritti da Circ. 7/2019 par. C7.3.3.2
        self.assertEqual(C1_TABELLA["telaio-acciaio"], 0.085)
        self.assertEqual(C1_TABELLA["telaio-legno"], 0.085)
        self.assertEqual(C1_TABELLA["telaio-ca"], 0.075)
        self.assertEqual(C1_TABELLA["muratura"], 0.050)
        self.assertEqual(C1_TABELLA["altro"], 0.050)

    def test_valore_chiuso_h16(self):
        # H = 16 m, telaio c.a.: H^(3/4) = 8 -> T1 = 0,075*8 = 0,6 s
        self.assertAlmostEqual(t1_da_altezza(16.0, "telaio-ca"), 0.6, places=12)

    def test_valore_chiuso_h16_acciaio(self):
        # H = 16 m, telaio acciaio: T1 = 0,085*8 = 0,68 s
        self.assertAlmostEqual(t1_da_altezza(16.0, "telaio-acciaio"), 0.68, places=12)

    def test_valore_chiuso_h16_muratura(self):
        # H = 16 m, muratura: T1 = 0,050*8 = 0,4 s
        self.assertAlmostEqual(t1_da_altezza(16.0, "muratura"), 0.4, places=12)

    def test_esponente(self):
        # raddoppiando H, T1 cresce di 2^(3/4)
        r = t1_da_altezza(32.0, "telaio-ca") / t1_da_altezza(16.0, "telaio-ca")
        self.assertAlmostEqual(r, 2 ** 0.75, places=12)

    def test_tipologia_sconosciuta(self):
        with self.assertRaises(ValueError):
            t1_da_altezza(10.0, "telaio-cap")


class TestStimaT1(unittest.TestCase):
    def test_metodo_ntc(self):
        ris = stima_t1("ntc", d_m=0.04, h_m=21.0, massa_uniforme=True)
        self.assertAlmostEqual(ris.t1_s, 0.4, places=12)
        self.assertIn("[7.3.6]", ris.formula)

    def test_metodo_circolare(self):
        ris = stima_t1("circolare", h_m=16.0, tipologia="telaio-ca", massa_uniforme=True)
        self.assertAlmostEqual(ris.t1_s, 0.6, places=12)
        self.assertIn("[C7.3.2]", ris.formula)

    def test_avvertenza_h_oltre_40(self):
        ris = stima_t1("circolare", h_m=45.0, tipologia="telaio-ca", massa_uniforme=True)
        self.assertTrue(any("40" in a for a in ris.avvertenze))
        self.assertEqual(H_MAX_FORMULA_M, 40.0)

    def test_avvertenza_massa_non_uniforme(self):
        ris = stima_t1("circolare", h_m=20.0, tipologia="muratura", massa_uniforme=False)
        self.assertTrue(any("NON approssimativamente uniforme" in a for a in ris.avvertenze))

    def test_condizione_2_5_tc(self):
        # T1 = 0,6 s; TC = 0,3 s -> 2,5*TC = 0,75 s -> condizione soddisfatta
        ris = stima_t1(
            "circolare", h_m=16.0, tipologia="telaio-ca",
            tc_s=0.3, n_orizzontamenti=5, massa_uniforme=True,
        )
        self.assertTrue(ris.condizione_t1_su_tc)
        self.assertAlmostEqual(ris.limite_analisi_statica_s, 0.75, places=12)

    def test_condizione_2_5_tc_violata(self):
        # T1 = 0,6 s; TC = 0,2 s -> 2,5*TC = 0,5 s -> violata
        ris = stima_t1(
            "circolare", h_m=16.0, tipologia="telaio-ca",
            tc_s=0.2, n_orizzontamenti=5, massa_uniforme=True,
        )
        self.assertFalse(ris.condizione_t1_su_tc)
        self.assertTrue(any("2,5*TC" in a for a in ris.avvertenze))

    def test_lambda_085(self):
        # T1 = 0,6 < 2*TC = 0,8 e 5 orizzontamenti -> lambda = 0,85
        ris = stima_t1(
            "circolare", h_m=16.0, tipologia="telaio-ca",
            tc_s=0.4, n_orizzontamenti=5, massa_uniforme=True,
        )
        self.assertEqual(ris.lambda_forze, LAMBDA_RIDOTTO)

    def test_lambda_1_per_pochi_orizzontamenti(self):
        ris = stima_t1(
            "circolare", h_m=16.0, tipologia="telaio-ca",
            tc_s=0.4, n_orizzontamenti=2, massa_uniforme=True,
        )
        self.assertEqual(ris.lambda_forze, LAMBDA_UNITARIO)

    def test_lambda_1_per_t1_grande(self):
        # T1 = 0,6 >= 2*TC = 0,6 -> lambda = 1,0 (condizione stretta T1 < 2*TC)
        ris = stima_t1(
            "circolare", h_m=16.0, tipologia="telaio-ca",
            tc_s=0.3, n_orizzontamenti=5, massa_uniforme=True,
        )
        self.assertEqual(ris.lambda_forze, LAMBDA_UNITARIO)

    def test_input_mancanti(self):
        with self.assertRaises(ValueError):
            stima_t1("ntc")
        with self.assertRaises(ValueError):
            stima_t1("circolare", h_m=10.0)
        with self.assertRaises(ValueError):
            stima_t1("modale")


class TestCli(unittest.TestCase):
    def _run(self, *args):
        proc = subprocess.run(
            [sys.executable, os.path.join(HERE, "periodo_t1.py"), *args],
            capture_output=True, text=True,
        )
        return proc

    def test_cli_circolare(self):
        proc = self._run(
            "--metodo", "circolare", "--h", "16", "--tipologia", "telaio-ca",
            "--tc", "0.4", "--orizzontamenti", "5", "--massa-uniforme", "si",
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertAlmostEqual(out["T1_s"], 0.6, places=6)
        self.assertEqual(out["lambda_forze_7_3_7"], 0.85)

    def test_cli_ntc(self):
        proc = self._run("--metodo", "ntc", "--d", "0.04", "--h", "21")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertAlmostEqual(out["T1_s"], 0.4, places=6)

    def test_cli_errore(self):
        proc = self._run("--metodo", "ntc")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("errore", json.loads(proc.stdout))


if __name__ == "__main__":
    unittest.main()
