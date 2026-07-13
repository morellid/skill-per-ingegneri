#!/usr/bin/env python3
"""Test suite per capacita_portante.py - consistenza con FHWA NHI-06-089 par. 8.4 e NTC Tab. 6.4.I."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from capacita_portante import (  # noqa: E402
    GAMMA_R_CARICO_LIMITE,
    capacita_portante,
    fattori_capacita,
    fattori_falda,
    fattori_forma,
)


class TestFattoriN(unittest.TestCase):
    """Eq. [8-2][8-3][8-4][8-5]; cross-check con Table 8-2 (phi=0 trascritto)."""

    def test_phi_zero_table_8_2(self):
        f = fattori_capacita(0.0)
        self.assertAlmostEqual(f["Nc"], 5.14, places=2)   # eq. 8-4 / Table 8-2
        self.assertAlmostEqual(f["Nq"], 1.0, places=6)    # eq. 8-2 con phi=0
        self.assertAlmostEqual(f["Ngamma"], 0.0, places=6)

    def test_phi_30_valori_chiusi(self):
        # eq. 8-2: Nq = e^(pi*tan30)*tan^2(60) = 18.401...
        f = fattori_capacita(30.0)
        self.assertAlmostEqual(f["Nq"], 18.401, places=3)
        # eq. 8-3: Nc = (Nq-1)*cot(30) = 30.140
        self.assertAlmostEqual(f["Nc"], 30.140, places=3)
        # eq. 8-5: Ngamma = 2*(Nq+1)*tan(30) = 22.402
        self.assertAlmostEqual(f["Ngamma"], 22.402, places=3)

    def test_monotonia(self):
        self.assertLess(fattori_capacita(20)["Nq"], fattori_capacita(35)["Nq"])

    def test_dominio(self):
        with self.assertRaises(ValueError):
            fattori_capacita(75.0)
        with self.assertRaises(ValueError):
            fattori_capacita(-1.0)


class TestFattoriForma(unittest.TestCase):
    """Table 8-4."""

    def test_nastro_tutti_uno(self):
        f = fattori_forma(30.0, 2.0, 20.0, 30.14, 18.40)
        self.assertEqual(f, {"sc": 1.0, "sq": 1.0, "sgamma": 1.0})

    def test_quadrata_phi_30(self):
        f = fattori_forma(30.0, 2.0, 2.0, 30.140, 18.401)
        self.assertAlmostEqual(f["sc"], 1.0 + 18.401 / 30.140, places=4)
        self.assertAlmostEqual(f["sq"], 1.0 + math.tan(math.radians(30)), places=4)
        self.assertAlmostEqual(f["sgamma"], 0.6, places=6)

    def test_quadrata_phi_zero(self):
        f = fattori_forma(0.0, 2.0, 2.0, 5.14, 1.0)
        self.assertAlmostEqual(f["sc"], 1.2, places=6)  # 1 + B/(5L)
        self.assertEqual(f["sq"], 1.0)
        self.assertEqual(f["sgamma"], 1.0)


class TestFattoriFalda(unittest.TestCase):
    """Table 8-5 con interpolazione."""

    def test_falda_profonda(self):
        f = fattori_falda(10.0, 1.0, 2.0)  # soglia = 4.0
        self.assertEqual((f["Cwq"], f["Cwgamma"]), (1.0, 1.0))

    def test_falda_al_piano_campagna(self):
        f = fattori_falda(0.0, 1.0, 2.0)
        self.assertEqual((f["Cwq"], f["Cwgamma"]), (0.5, 0.5))

    def test_falda_al_piano_di_posa(self):
        f = fattori_falda(1.0, 1.0, 2.0)
        self.assertEqual((f["Cwq"], f["Cwgamma"]), (1.0, 0.5))

    def test_interpolazioni(self):
        # DW = 0.5, Df = 1: Cwq = 0.75; Cwgamma = 0.5
        f = fattori_falda(0.5, 1.0, 2.0)
        self.assertAlmostEqual(f["Cwq"], 0.75, places=6)
        self.assertAlmostEqual(f["Cwgamma"], 0.5, places=6)
        # DW = 2.5 fra Df=1 e soglia=4: Cwgamma = 0.5 + 0.5*(1.5/3) = 0.75
        f = fattori_falda(2.5, 1.0, 2.0)
        self.assertAlmostEqual(f["Cwq"], 1.0, places=6)
        self.assertAlmostEqual(f["Cwgamma"], 0.75, places=6)


class TestCapacitaPortante(unittest.TestCase):
    def test_nastro_drenato_valore_chiuso(self):
        # B=2, Df=1, gamma=18, phi=30, c'=0, nastro, falda profonda:
        # qult = 18*1*18.401 + 0.5*18*2*22.402 = 331.22 + 403.23 = 734.45 kPa
        ris = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                condizione="drenata", phi=30.0)
        self.assertAlmostEqual(ris.qult_kpa, 734.45, delta=0.05)
        self.assertAlmostEqual(ris.q_rd_kpa, 734.45 / 2.3, delta=0.05)
        self.assertEqual(GAMMA_R_CARICO_LIMITE, 2.3)  # Tab. 6.4.I NTC

    def test_nastro_non_drenato_valore_chiuso(self):
        # cu=50, B=2, Df=1, gamma=18: qult = 50*5.14 + 18*1*1 = 275.07... (Nc=2+pi)
        ris = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                condizione="non-drenata", c=50.0)
        atteso = 50.0 * (2.0 + math.pi) + 18.0
        self.assertAlmostEqual(ris.qult_kpa, atteso, places=6)

    def test_rettangolare_forma_applicata(self):
        quad = capacita_portante(B=2.0, L=2.0, Df=1.0, gamma_sotto=18.0,
                                 condizione="drenata", phi=30.0)
        nastro = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                   condizione="drenata", phi=30.0)
        # sq > 1 aumenta il termine q; sgamma = 0.6 riduce il termine peso
        self.assertNotAlmostEqual(quad.qult_kpa, nastro.qult_kpa, places=1)
        self.assertAlmostEqual(quad.dettaglio["fattori_forma"]["sgamma"], 0.6, places=4)

    def test_eccentricita_dimensioni_efficaci(self):
        # eB = 0.2 < B/6 = 0.333: B' = 1.6; A' = B'*L' con L'=L
        ris = capacita_portante(B=2.0, L=3.0, Df=1.0, gamma_sotto=18.0,
                                condizione="drenata", phi=30.0, eB=0.2)
        self.assertAlmostEqual(ris.dettaglio["B_eff_m"], 1.6, places=6)
        self.assertAlmostEqual(ris.dettaglio["A_eff_m2"], 1.6 * 3.0, places=4)

    def test_eccentricita_oltre_limite_rifiutata(self):
        # eB = 0.4 >= B/6 = 0.333 -> resize (FHWA 8.4.3.1)
        with self.assertRaises(ValueError) as ctx:
            capacita_portante(B=2.0, L=3.0, Df=1.0, gamma_sotto=18.0,
                              condizione="drenata", phi=30.0, eB=0.4)
        self.assertIn("1/6", str(ctx.exception))

    def test_falda_riduce_qult(self):
        asciutto = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                     condizione="drenata", phi=30.0)
        bagnato = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                    condizione="drenata", phi=30.0, DW=0.0)
        self.assertLess(bagnato.qult_kpa, asciutto.qult_kpa)

    def test_confronto_ed(self):
        ris = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                condizione="drenata", phi=30.0, Ed_kn=400.0)
        # R_d per metro = (734.45/2.3)*2 = 638.65 kN/m > 400
        self.assertTrue(ris.esito_ed)
        ris2 = capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                                 condizione="drenata", phi=30.0, Ed_kn=700.0)
        self.assertFalse(ris2.esito_ed)
        self.assertTrue(any("[6.2.1]" in a for a in ris2.avvertenze))

    def test_input_invalidi(self):
        with self.assertRaises(ValueError):
            capacita_portante(B=2.0, L=1.0, Df=1.0, gamma_sotto=18.0,
                              condizione="drenata", phi=30.0)  # L < B
        with self.assertRaises(ValueError):
            capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                              condizione="non-drenata", c=50.0, phi=25.0)
        with self.assertRaises(ValueError):
            capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                              condizione="drenata", phi=0.0, c=0.0)
        with self.assertRaises(ValueError):
            capacita_portante(B=2.0, L=None, Df=1.0, gamma_sotto=18.0,
                              condizione="mista", phi=30.0)


class TestCli(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, os.path.join(HERE, "capacita_portante.py"), *args],
            capture_output=True, text=True,
        )

    def test_cli_nastro(self):
        proc = self._run("--b", "2", "--df", "1", "--gamma", "18",
                         "--condizione", "drenata", "--phi", "30")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertAlmostEqual(out["qult_kPa"], 734.45, delta=0.05)
        self.assertAlmostEqual(out["q_Rd_kPa"], 319.33, delta=0.05)

    def test_cli_eccentricita_rifiutata(self):
        proc = self._run("--b", "2", "--l", "3", "--df", "1", "--gamma", "18",
                         "--condizione", "drenata", "--phi", "30", "--eb", "0.4")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("errore", json.loads(proc.stdout))


if __name__ == "__main__":
    unittest.main()
