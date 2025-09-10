#!/usr/bin/env python3

import sys
import re
from chemical_balancer.parser import parse_equation
from chemical_balancer.matrix import build_matrix
from chemical_balancer.solver import solve_matrix

def main():
    if len(sys.argv) != 2:
        print("Usage: chemical_balancer 'LHS equation -> RHS equation'")
        sys.exit(1)

    equation = sys.argv[1]

    if not re.fullmatch('[a-zA-Z0-9+ ]*->[a-zA-Z0-9+ ]*', equation):
        print("Usage: chemical_balancer 'LHS equation -> RHS equation'")
        print("Equations must contain only letters, numbers and +")
        sys.exit(1)

    lhs, rhs = parse_equation(equation)
    elements, matrix = build_matrix(lhs, rhs)
    coeffs = solve_matrix(matrix)

    # For now, just print debug info
    print(f"Equation: {equation}")
    print(f"LHS: {lhs}")
    print(f"RHS: {rhs}")
    print(f"Elements: {elements}")
    print(f"Matrix: {matrix}")
    print(f"Coefficients: {coeffs}")

