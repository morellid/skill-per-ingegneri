from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from combinazioni import GAMMA, PSI, generate_combinations, psi_for


FIXTURE = {
    "gamma_profile": "A1",
    "permanent_actions": [
        {"name": "G1", "kind": "G1", "value": 10.0, "effect": "sfavorevole"},
        {"name": "G2", "kind": "G2", "value": 2.0, "effect": "sfavorevole", "well_defined": False},
    ],
    "prestress": 0.0,
    "variable_actions": [
        {"name": "Q_A", "category": "A", "value": 3.0, "effect": "sfavorevole"},
        {"name": "Neve", "category": "NEVE_LE_1000", "value": 1.2, "effect": "sfavorevole"},
        {"name": "Vento", "category": "VENTO", "value": 0.8, "effect": "sfavorevole"},
    ],
    "seismic_action": 4.5,
    "exceptional_action": 7.0,
}


class TestTabelle(unittest.TestCase):
    def test_psi_known_values(self):
        self.assertEqual(PSI["E"]["psi2"], 0.8)
        self.assertEqual(psi_for("vento", "psi0"), 0.6)
        self.assertEqual(psi_for("NEVE_GT_1000", "psi2"), 0.2)

    def test_gamma_known_values(self):
        self.assertEqual(GAMMA["A1"]["G1"]["sfavorevole"], 1.3)
        self.assertEqual(GAMMA["A2"]["Q"]["sfavorevole"], 1.3)
        self.assertEqual(GAMMA["EQU"]["G2"]["favorevole"], 0.8)


class TestCombinazioni(unittest.TestCase):
    def test_numero_combinazioni(self):
        combos = generate_combinations(FIXTURE)
        self.assertEqual(len(combos), 12)

    def test_slu_prima_variabile_principale(self):
        slu = next(c for c in generate_combinations(FIXTURE) if c.id == "SLU-A1-1")
        self.assertEqual(slu.leading_action, "Q_A")
        coeffs = {t.action: t.coefficient for t in slu.terms}
        self.assertAlmostEqual(coeffs["G1"], 1.3)
        self.assertAlmostEqual(coeffs["G2"], 1.5)
        self.assertAlmostEqual(coeffs["Q_A"], 1.5)
        self.assertAlmostEqual(coeffs["Neve"], 1.5 * 0.5)
        self.assertAlmostEqual(coeffs["Vento"], 1.5 * 0.6)

    def test_sle_frequente(self):
        freq = next(c for c in generate_combinations(FIXTURE) if c.id == "SLE-FREQ-1")
        coeffs = {t.action: t.coefficient for t in freq.terms}
        self.assertAlmostEqual(coeffs["Q_A"], 0.5)
        self.assertAlmostEqual(coeffs["Neve"], 0.0)
        self.assertAlmostEqual(coeffs["Vento"], 0.0)

    def test_sismica_usa_psi2(self):
        sis = next(c for c in generate_combinations(FIXTURE) if c.id == "SIS-1")
        coeffs = {t.action: t.coefficient for t in sis.terms}
        self.assertAlmostEqual(coeffs["E"], 1.0)
        self.assertAlmostEqual(coeffs["Q_A"], 0.3)
        self.assertAlmostEqual(coeffs["Neve"], 0.0)
        self.assertAlmostEqual(coeffs["Vento"], 0.0)

    def test_g2_well_defined_usa_gamma_g1(self):
        data = dict(FIXTURE)
        data["permanent_actions"] = [
            {"name": "G2_def", "kind": "G2", "value": 2.0, "effect": "sfavorevole", "well_defined": True}
        ]
        slu = next(c for c in generate_combinations(data) if c.id == "SLU-A1-1")
        coeffs = {t.action: t.coefficient for t in slu.terms}
        self.assertAlmostEqual(coeffs["G2_def"], 1.3)

    def test_categoria_non_supportata(self):
        data = dict(FIXTURE)
        data["variable_actions"] = [{"name": "Q_I", "category": "I", "value": 1.0}]
        with self.assertRaises(ValueError):
            generate_combinations(data)


class TestCli(unittest.TestCase):
    def test_cli_json(self):
        module = os.path.join(os.path.dirname(__file__), "combinazioni.py")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(FIXTURE, handle)
            path = handle.name
        try:
            proc = subprocess.run(
                [sys.executable, module, path, "--format", "json"],
                check=True,
                text=True,
                capture_output=True,
            )
            parsed = json.loads(proc.stdout)
            self.assertEqual(parsed[0]["id"], "SLU-A1-1")
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
