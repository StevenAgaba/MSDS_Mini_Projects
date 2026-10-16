"""
microgrid.py

Solar Micro-Grid Dispatch Planner
"""

import numpy as np
from scipy.optimize import nnls


class MicroGrid:
    """
    Solves the energy dispatch system:

    3x + 2y = D1
    4x + y  = D2
    """

    def __init__(self):

        self.A = np.array([
            [3, 2],
            [4, 1]
        ])

    def determinant(self) -> float:
        return np.linalg.det(self.A)

    def condition_number(self) -> float:
        return np.linalg.cond(self.A)

    def solve_day(self, d1: float, d2: float):

        b = np.array([d1, d2])

        return np.linalg.solve(self.A, b)

    def solve_many_days(self, rhs_matrix):

        return np.linalg.solve(
            self.A,
            rhs_matrix
        )

    def solve_non_negative(self, d1, d2):

        b = np.array([d1, d2])

        solution, _ = nnls(
            self.A,
            b
        )

        return solution


class HybridMicroGrid(MicroGrid):
    """
    Extension model with diesel generator z.
    """

    def __init__(self):

        self.A = np.array([
            [3, 2, 1],
            [4, 1, 2],
            [1, 1, 1]
        ])

    def solve_hybrid(self, d1, d2, d3):

        b = np.array([
            d1,
            d2,
            d3
        ])

        return np.linalg.solve(
            self.A,
            b
        )