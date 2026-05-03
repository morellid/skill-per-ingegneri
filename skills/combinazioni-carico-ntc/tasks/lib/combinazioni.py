#!/usr/bin/env python3
"""Generatore combinazioni azioni NTC 2018 par. 2.5.3."""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional


PSI: Dict[str, Dict[str, float]] = {
    "A": {"psi0": 0.7, "psi1": 0.5, "psi2": 0.3},
    "B": {"psi0": 0.7, "psi1": 0.5, "psi2": 0.3},
    "C": {"psi0": 0.7, "psi1": 0.7, "psi2": 0.6},
    "D": {"psi0": 0.7, "psi1": 0.7, "psi2": 0.6},
    "E": {"psi0": 1.0, "psi1": 0.9, "psi2": 0.8},
    "F": {"psi0": 0.7, "psi1": 0.7, "psi2": 0.6},
    "G": {"psi0": 0.7, "psi1": 0.5, "psi2": 0.3},
    "H": {"psi0": 0.0, "psi1": 0.0, "psi2": 0.0},
    "VENTO": {"psi0": 0.6, "psi1": 0.2, "psi2": 0.0},
    "NEVE_LE_1000": {"psi0": 0.5, "psi1": 0.2, "psi2": 0.0},
    "NEVE_GT_1000": {"psi0": 0.7, "psi1": 0.5, "psi2": 0.2},
    "TERMICA": {"psi0": 0.6, "psi1": 0.5, "psi2": 0.0},
}

GAMMA: Dict[str, Dict[str, Dict[str, float]]] = {
    "EQU": {
        "G1": {"favorevole": 0.9, "sfavorevole": 1.1},
        "G2": {"favorevole": 0.8, "sfavorevole": 1.5},
        "Q": {"favorevole": 0.0, "sfavorevole": 1.5},
    },
    "A1": {
        "G1": {"favorevole": 1.0, "sfavorevole": 1.3},
        "G2": {"favorevole": 0.8, "sfavorevole": 1.5},
        "Q": {"favorevole": 0.0, "sfavorevole": 1.5},
    },
    "A2": {
        "G1": {"favorevole": 1.0, "sfavorevole": 1.0},
        "G2": {"favorevole": 0.8, "sfavorevole": 1.3},
        "Q": {"favorevole": 0.0, "sfavorevole": 1.3},
    },
}


@dataclass(frozen=True)
class Term:
    action: str
    coefficient: float
    value: float
    role: str

    @property
    def product(self) -> float:
        return self.coefficient * self.value


@dataclass(frozen=True)
class Combination:
    id: str
    kind: str
    leading_action: Optional[str]
    terms: List[Term]
    reference: str

    @property
    def result(self) -> float:
        return sum(t.product for t in self.terms)

    def expression(self) -> str:
        parts = [f"{fmt(t.coefficient)}*{t.action}" for t in self.terms if abs(t.coefficient) > 0]
        return " + ".join(parts) or "0"

    def as_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "leading_action": self.leading_action,
            "expression": self.expression(),
            "result": round(self.result, 6),
            "reference": self.reference,
            "terms": [
                {
                    "action": t.action,
                    "coefficient": t.coefficient,
                    "value": t.value,
                    "role": t.role,
                    "product": round(t.product, 6),
                }
                for t in self.terms
            ],
        }


def fmt(value: float) -> str:
    if abs(value - round(value)) < 1e-12:
        return str(int(round(value)))
    return f"{value:.6g}"


def finite_number(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field}: valore non numerico") from exc
    if not math.isfinite(number):
        raise ValueError(f"{field}: valore non finito")
    return number


def normalize_effect(value: str) -> str:
    effect = (value or "sfavorevole").strip().lower()
    aliases = {
        "unfavourable": "sfavorevole",
        "unfavorable": "sfavorevole",
        "sfav": "sfavorevole",
        "fav": "favorevole",
        "favourable": "favorevole",
        "favorable": "favorevole",
    }
    effect = aliases.get(effect, effect)
    if effect not in {"favorevole", "sfavorevole"}:
        raise ValueError(f"effetto non valido: {value!r}")
    return effect


def psi_for(category: str, key: str) -> float:
    cat = category.strip().upper()
    if cat not in PSI:
        raise ValueError(
            f"categoria variabile non supportata: {category!r}. "
            f"Supportate: {', '.join(sorted(PSI))}"
        )
    return PSI[cat][key]


def validate_profile(profile: str) -> str:
    normalized = profile.strip().upper()
    if normalized not in GAMMA:
        raise ValueError(f"gamma_profile non valido: {profile!r}. Usa EQU, A1 o A2")
    return normalized


def permanent_terms(data: Dict[str, Any], gamma_profile: Optional[str] = None) -> List[Term]:
    terms: List[Term] = []
    for idx, action in enumerate(data.get("permanent_actions", []), start=1):
        name = str(action.get("name") or f"G{idx}")
        kind = str(action.get("kind") or "G1").upper()
        if kind not in {"G1", "G2"}:
            raise ValueError(f"{name}: kind deve essere G1 o G2")
        value = finite_number(action.get("value"), f"{name}.value")
        if gamma_profile is None:
            coeff = 1.0
        else:
            effect = normalize_effect(action.get("effect", "sfavorevole"))
            gamma_kind = "G1" if (kind == "G2" and action.get("well_defined")) else kind
            coeff = GAMMA[gamma_profile][gamma_kind][effect]
        terms.append(Term(name, coeff, value, kind))

    prestress = data.get("prestress", 0.0)
    if prestress not in (None, 0, 0.0):
        terms.append(Term("P", 1.0, finite_number(prestress, "prestress"), "P"))
    return terms


def variable_specs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    variables: List[Dict[str, Any]] = []
    for idx, action in enumerate(data.get("variable_actions", []), start=1):
        name = str(action.get("name") or f"Q{idx}")
        category = str(action.get("category") or "").upper()
        if category not in PSI:
            raise ValueError(
                f"{name}: categoria variabile non supportata {category!r}. "
                f"Supportate: {', '.join(sorted(PSI))}"
            )
        variables.append(
            {
                "name": name,
                "category": category,
                "value": finite_number(action.get("value"), f"{name}.value"),
                "effect": normalize_effect(action.get("effect", "sfavorevole")),
            }
        )
    return variables


def variable_term(var: Dict[str, Any], coefficient: float, role: str) -> Term:
    return Term(var["name"], coefficient, var["value"], role)


def generate_combinations(data: Dict[str, Any]) -> List[Combination]:
    profile = validate_profile(str(data.get("gamma_profile") or "A1"))
    variables = variable_specs(data)
    combinations: List[Combination] = []

    base_slu = permanent_terms(data, profile)
    for i, lead in enumerate(variables, start=1):
        terms = list(base_slu)
        terms.append(variable_term(lead, GAMMA[profile]["Q"][lead["effect"]], "Q_principale"))
        for other in variables:
            if other is lead:
                continue
            terms.append(
                variable_term(
                    other,
                    GAMMA[profile]["Q"][other["effect"]] * psi_for(other["category"], "psi0"),
                    "Q_accompagnatrice_psi0",
                )
            )
        combinations.append(
            Combination(
                id=f"SLU-{profile}-{i}",
                kind=f"SLU fondamentale {profile}",
                leading_action=lead["name"],
                terms=terms,
                reference="NTC 2018 eq. 2.5.1 + Tab. 2.6.I",
            )
        )

    base_sle = permanent_terms(data, None)
    for i, lead in enumerate(variables, start=1):
        rare_terms = list(base_sle)
        rare_terms.append(variable_term(lead, 1.0, "Q_principale"))
        for other in variables:
            if other is lead:
                continue
            rare_terms.append(variable_term(other, psi_for(other["category"], "psi0"), "Q_accompagnatrice_psi0"))
        combinations.append(
            Combination(f"SLE-RARA-{i}", "SLE rara", lead["name"], rare_terms, "NTC 2018 eq. 2.5.2")
        )

        frequent_terms = list(base_sle)
        frequent_terms.append(variable_term(lead, psi_for(lead["category"], "psi1"), "Q_principale_psi1"))
        for other in variables:
            if other is lead:
                continue
            frequent_terms.append(variable_term(other, psi_for(other["category"], "psi2"), "Q_accompagnatrice_psi2"))
        combinations.append(
            Combination(f"SLE-FREQ-{i}", "SLE frequente", lead["name"], frequent_terms, "NTC 2018 eq. 2.5.3")
        )

    quasi_terms = list(base_sle)
    for var in variables:
        quasi_terms.append(variable_term(var, psi_for(var["category"], "psi2"), "Q_psi2"))
    combinations.append(
        Combination("SLE-QP-1", "SLE quasi permanente", None, quasi_terms, "NTC 2018 eq. 2.5.4")
    )

    seismic = data.get("seismic_action")
    if seismic is not None:
        terms = [Term("E", 1.0, finite_number(seismic, "seismic_action"), "E")]
        terms.extend(base_sle)
        for var in variables:
            terms.append(variable_term(var, psi_for(var["category"], "psi2"), "Q_psi2"))
        combinations.append(Combination("SIS-1", "Sismica", "E", terms, "NTC 2018 eq. 2.5.5"))

    exceptional = data.get("exceptional_action")
    if exceptional is not None:
        terms = list(base_sle)
        terms.append(Term("Ad", 1.0, finite_number(exceptional, "exceptional_action"), "Ad"))
        for var in variables:
            terms.append(variable_term(var, psi_for(var["category"], "psi2"), "Q_psi2"))
        combinations.append(Combination("ECC-1", "Eccezionale", "Ad", terms, "NTC 2018 eq. 2.5.6"))
    return combinations


def render_markdown(combinations: Iterable[Combination], profile: str) -> str:
    rows = [
        f"Profilo gamma SLU: `{profile}`",
        "",
        "| ID | Tipo | Principale | Espressione | Valore | Riferimento |",
        "|---|---|---|---|---:|---|",
    ]
    for combo in combinations:
        rows.append(
            "| {id} | {kind} | {leading} | `{expr}` | {result} | {ref} |".format(
                id=combo.id,
                kind=combo.kind,
                leading=combo.leading_action or "-",
                expr=combo.expression(),
                result=fmt(round(combo.result, 6)),
                ref=combo.reference,
            )
        )
    return "\n".join(rows)


def load_input(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("input JSON deve essere un oggetto")
    return data


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", help="Path al file JSON di input")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)

    try:
        data = load_input(args.input_json)
        combinations = generate_combinations(data)
        profile = validate_profile(str(data.get("gamma_profile") or "A1"))
        if args.format == "json":
            print(json.dumps([c.as_dict() for c in combinations], indent=2, ensure_ascii=False))
        else:
            print(render_markdown(combinations, profile))
    except Exception as exc:  # pragma: no cover
        print(f"ERRORE: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
