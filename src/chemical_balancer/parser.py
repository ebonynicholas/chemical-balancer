#!/usr/bin/env python3

import re
import collections

def parse_formula(formula: str) -> dict[str, int]:
    elements = re.findall('[A-Z][a-z]{0,1}[0-9]*', formula)
    parsed_elements = collections.defaultdict(str)
    for element in elements:
        letters = re.search('[A-Za-z]*', element)
        number = re.search('[0-9]*', element)
        parsed_elements[letters] = number
    return dict

def parse_equation(equation: str) -> tuple[list[str], list[str]]:
    sides = re.split('->', equation)
    lhs = re.findall('[A-Za-z]*[0-9]*', sides[0])
    rhs = re.findall('[A-Za-z]*[0-9]*', sides[0])
    return (lhs, rhs)
