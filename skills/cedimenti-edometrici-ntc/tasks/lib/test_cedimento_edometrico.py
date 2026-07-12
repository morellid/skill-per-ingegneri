#!/usr/bin/env python3
"""Test suite per cedimento_edometrico.py - consistenza con FHWA NHI-06-088 par. 7.5.2."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from cedimento_edometrico import (  # noqa: E402
    cedimento_multistrato,
    cedimento_strato,
)


class TestEq72NC(unittest.TestCase):
    """[7-2] NC: Sc = Cc/(1+e0) * H0 * log10(pf/p0)."""

    def test_valore_chiuso(self):
        # h0=2, e0=0.8, Cc=0.30, p0=100, dp=100 -> pf/p0=2
        # Sc = 0.30/1.8 * 2 * log10(2) = 0.1003433... m
        ris = cedimento_strato(2.0, 0.8, 0.30, 100.0, 100.0)
        atteso = 0.30 / 1.8 * 2.0 * math.log10(2.0)
        self.assertEqual(ris.caso, "NC")
        self.assertEqual(ris.equazione, "[7-2]")
        self.assertAlmostEqual(ris.s_m, atteso, places=12)

    def test_nc_esplicito_sigmap_uguale(self):
        a = cedimento_strato(2.0, 0.8, 0.30, 100.0, 100.0)
        b = cedimento_strato(2.0, 0.8, 0.30, 100.0, 100.0, sigma_p=100.0)
        self.assertAlmostEqual(a.s_m, b.s_m, places=12)
        self.assertEqual(b.caso, "NC")

    def test_monotonia_in_dp(self):
        s1 = cedimento_strato(2.0, 0.8, 0.30, 100.0, 50.0).s_m
        s2 = cedimento_strato(2.0, 0.8, 0.30, 100.0, 200.0).s_m
        self.assertLess(s1, s2)


class TestEq74OC(unittest.TestCase):
    """[7-4] OC con pf > pc: due termini Cr e Cc."""

    def test_valore_chiuso_esempio_repo(self):
        # Esempio conforme del repo: h0=2, e0=0.8, Cc=0.30, Cr=0.05,
        # p0=100, pc=150, dp=200 -> pf=300
        # S = 2/1.8 * (0.05*log10(1.5) + 0.30*log10(2)) = 0.110126... m
        ris = cedimento_strato(2.0, 0.8, 0.30, 100.0, 200.0, sigma_p=150.0, Cr=0.05)
        atteso = 2.0 / 1.8 * (0.05 * math.log10(1.5) + 0.30 * math.log10(2.0))
        self.assertEqual(ris.caso, "OC")
        self.assertEqual(ris.equazione, "[7-4]")
        self.assertAlmostEqual(ris.s_m, atteso, places=12)
        self.assertAlmostEqual(ris.s_m, 0.110126, places=5)
        # dominato dal ramo vergine
        self.assertGreater(
            ris.dettaglio["termine_vergine_m"], ris.dettaglio["termine_ricompressione_m"]
        )

    def test_oc_pf_sotto_pc_rifiutato(self):
        # pf = 120 <= pc = 150: caso non coperto dalle eq. trascritte
        with self.assertRaises(ValueError) as ctx:
            cedimento_strato(2.0, 0.8, 0.30, 100.0, 20.0, sigma_p=150.0, Cr=0.05)
        self.assertIn("pf > pc", str(ctx.exception))

    def test_oc_senza_cr_rifiutato(self):
        with self.assertRaises(ValueError):
            cedimento_strato(2.0, 0.8, 0.30, 100.0, 200.0, sigma_p=150.0)

    def test_avvertenza_cr_maggiore_cc(self):
        ris = cedimento_strato(2.0, 0.8, 0.30, 100.0, 200.0, sigma_p=150.0, Cr=0.40)
        self.assertTrue(any("Cr > Cc" in a for a in ris.avvertenze))


class TestEq76UC(unittest.TestCase):
    """[7-6] UC (OCR < 1): rifiuto di default, calcolo solo se dichiarato."""

    def test_ocr_minore_1_rifiutato_di_default(self):
        # Esempio problematico del repo: p0=200, pc=100 -> OCR=0.5
        with self.assertRaises(ValueError) as ctx:
            cedimento_strato(2.0, 0.8, 0.30, 200.0, 50.0, sigma_p=100.0, Cr=0.05)
        self.assertIn("OCR < 1", str(ctx.exception))

    def test_uc_dichiarato_valore_chiuso(self):
        # S = 2/1.8 * (0.30*log10(200/100) + 0.30*log10(250/200))
        ris = cedimento_strato(
            2.0, 0.8, 0.30, 200.0, 50.0, sigma_p=100.0, sottoconsolidato=True
        )
        atteso = 2.0 / 1.8 * (
            0.30 * math.log10(2.0) + 0.30 * math.log10(250.0 / 200.0)
        )
        self.assertEqual(ris.caso, "UC")
        self.assertEqual(ris.equazione, "[7-6]")
        self.assertAlmostEqual(ris.s_m, atteso, places=12)
        self.assertTrue(any("sottostimato" in a for a in ris.avvertenze))

    def test_uc_maggiore_del_solo_incremento(self):
        # FHWA 7.5.2.3: ignorare la sottoconsolidazione sottostima il totale
        uc = cedimento_strato(
            2.0, 0.8, 0.30, 200.0, 50.0, sigma_p=100.0, sottoconsolidato=True
        )
        nc_solo_dp = cedimento_strato(2.0, 0.8, 0.30, 200.0, 50.0)
        self.assertGreater(uc.s_m, nc_solo_dp.s_m)


class TestMultistrato(unittest.TestCase):
    def test_somma_strati(self):
        strati = [
            {"h0": 2.0, "e0": 0.8, "Cc": 0.30, "sigma_0": 100.0, "delta_sigma": 100.0},
            {
                "h0": 2.0, "e0": 0.8, "Cc": 0.30, "Cr": 0.05,
                "sigma_0": 100.0, "sigma_p": 150.0, "delta_sigma": 200.0,
            },
        ]
        out = cedimento_multistrato(strati)
        s1 = cedimento_strato(2.0, 0.8, 0.30, 100.0, 100.0).s_m
        s2 = cedimento_strato(2.0, 0.8, 0.30, 100.0, 200.0, sigma_p=150.0, Cr=0.05).s_m
        self.assertAlmostEqual(out["S_totale_m"], round(s1 + s2, 6), places=6)
        self.assertEqual(len(out["strati"]), 2)
        self.assertEqual(out["strati"][0]["caso"], "NC")
        self.assertEqual(out["strati"][1]["caso"], "OC")
        self.assertTrue(any("cap. 12" in a for a in out["avvertenze"]))

    def test_lista_vuota(self):
        with self.assertRaises(ValueError):
            cedimento_multistrato([])

    def test_input_invalidi(self):
        for campo, valore in [
            ("h0", -1.0), ("e0", float("nan")), ("Cc", 0.0),
            ("sigma_0", 0.0), ("delta_sigma", -5.0),
        ]:
            strato = {
                "h0": 2.0, "e0": 0.8, "Cc": 0.30,
                "sigma_0": 100.0, "delta_sigma": 100.0,
            }
            strato[campo] = valore
            with self.assertRaises(ValueError, msg=campo):
                cedimento_multistrato([strato])


class TestCli(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, os.path.join(HERE, "cedimento_edometrico.py"), *args],
            capture_output=True, text=True,
        )

    def test_cli_oc(self):
        proc = self._run(
            "--h0", "2", "--e0", "0.8", "--cc", "0.30", "--cr", "0.05",
            "--sigma0", "100", "--sigmap", "150", "--dsigma", "200",
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertAlmostEqual(out["S_totale_mm"], 110.1, places=1)
        self.assertEqual(out["strati"][0]["equazione_FHWA"], "[7-4]")

    def test_cli_ocr_minore_1(self):
        proc = self._run(
            "--h0", "2", "--e0", "0.8", "--cc", "0.30", "--cr", "0.05",
            "--sigma0", "200", "--sigmap", "100", "--dsigma", "50",
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("OCR < 1", json.loads(proc.stdout)["errore"])


if __name__ == "__main__":
    unittest.main()
