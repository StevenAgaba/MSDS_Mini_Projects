"""
district.py

District population data model.
"""

import numpy as np
import statistics


class DistrictPopulation:
    """
    Stores and validates district population data.
    """

    def __init__(
        self,
        name: str,
        years: np.ndarray,
        populations: np.ndarray
    ) -> None:

        self.name = name
        self.years = np.array(years)
        self.populations = np.array(populations)

        self._validate()

    def _validate(self) -> None:

        if len(self.years) != len(self.populations):
            raise ValueError(
                "Years and population arrays must have equal lengths."
            )

        if np.any(self.populations < 0):
            raise ValueError(
                "Population values cannot be negative."
            )

    def mean(self) -> float:
        return statistics.mean(self.populations)

    def median(self) -> float:
        return statistics.median(self.populations)

    def variance(self) -> float:
        return statistics.variance(self.populations)

    def std_dev(self) -> float:
        return statistics.stdev(self.populations)

    def __len__(self) -> int:
        return len(self.populations)

    def __repr__(self) -> str:
        return (
            f"DistrictPopulation(name='{self.name}', "
            f"records={len(self)})"
        )