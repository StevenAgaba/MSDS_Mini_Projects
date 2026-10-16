import numpy as np

from src.microgrid import MicroGrid


def test_matrix_shape():

    grid = MicroGrid()

    assert grid.A.shape == (2, 2)


def test_solution_dimension():

    grid = MicroGrid()

    solution = grid.solve_day(
        600,
        650
    )

    assert len(solution) == 2


def test_determinant_nonzero():

    grid = MicroGrid()

    assert grid.determinant() != 0