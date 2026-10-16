"""
Route revenue calculations.
"""

import statistics
import numpy as np


class Route:

    def __init__(
        self,
        name,
        passengers,
        fare
    ):

        self.name = name
        self.passengers = np.array(
            passengers
        )

        self.fare = fare

    def daily_revenue(self):

        return (
            self.passengers
            * self.fare
        )

    def total_revenue(self):

        return np.sum(
            self.daily_revenue()
        )
        
    def mean(self):

        return statistics.mean(
            self.passengers.tolist()
        )

    def variance(self):

        return float(
            np.var(
                self.passengers,
                ddof=1
            )
        )

    def std_dev(self):

        return float(
            np.std(
                self.passengers,
                ddof=1
            )
        )

