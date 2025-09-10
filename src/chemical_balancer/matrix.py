#!/usr/bin/env python3

from parser import parse_formula

def build_matrix(lhs: list[str], rhs: list[str]) -> tuple[list[str], list[list[int]]]:
    """Return (elements, matrix) where matrix rows=elements, cols=species."""
    all_species = lhs + rhs
    all_elements = {}
    for species in all_species:
        all_elements.update(parse_formula(species).keys())
    
    for element in all_elements:
        for species in all_species:
            element_counts = parse_formula(species)
            if element_counts[element]:
                
    # TODOa