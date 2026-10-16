import numpy as np
import pytest

from src.district import DistrictPopulation


def test_valid_creation():

    district = DistrictPopulation(
        "Test",
        np.array([2020, 2021]),
        np.array([100, 120])
    )

    assert len(district) == 2


def test_negative_population():

    with pytest.raises(ValueError):

        DistrictPopulation(
            "Test",
            np.array([2020, 2021]),
            np.array([100, -120])
        )


def test_unequal_lengths():

    with pytest.raises(ValueError):

        DistrictPopulation(
            "Test",
            np.array([2020]),
            np.array([100, 120])
        )