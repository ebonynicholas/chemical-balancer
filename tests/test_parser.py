#!/usr/bin/env python3

from chem_balancer.parser import parse_formula, parse_equation

def test_parse_formula():
    assert parse_formula("H2O") == {"H": 2, "O": 1}

def test_parse_equation():
    lhs, rhs = parse_equation("H2 + O2 -> H2O")
    assert lhs == ["H2", "O2"]
    assert rhs == ["H2O"]
