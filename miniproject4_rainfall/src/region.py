"""
Region rainfall model.
"""

import numpy as np


class Region:

    def __init__(
        self,
        name: str,
        rainfall
    ):

        self.name = name
        self.rainfall = np.array(
            rainfall
        )

    def annual_total(self):

        return np.sum(
            self.rainfall
        )

    def mean(self):

        return np.mean(
            self.rainfall
        )

    def wettest_month(self):

        return np.argmax(
            self.rainfall
        )

    def driest_month(self):

        return np.argmin(
            self.rainfall
        )

    def coefficient_of_variation(self):

        return (
            np.std(self.rainfall)
            /
            np.mean(
                self.rainfall
            )
        )