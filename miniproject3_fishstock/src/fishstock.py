"""
Fish stock and price models.
"""

import numpy as np


class FishStock:
    """
    Logistic fish stock growth model with harvesting.
    """

    def __init__(
        self,
        r=0.4,
        K=10000,
        N0=4000
    ):

        self.r = r
        self.K = K
        self.N0 = N0

    def simulate(
        self,
        weeks=52,
        harvest_rate=0.1
    ):

        stock = [self.N0]

        harvests = []

        for _ in range(weeks):

            current = stock[-1]

            growth = (
                self.r
                * current
                * (1 - current/self.K)
            )

            harvest = harvest_rate * current

            nxt = (
                current
                + growth
                - harvest
            )

            stock.append(nxt)

            harvests.append(harvest)

        return (
            np.array(stock),
            np.array(harvests)
        )


class PriceModel:
    """
    Weekly fish-price random walk.
    """

    def __init__(
        self,
        start_price=12000,
        minimum=9000,
        maximum=16000,
        seed=42
    ):

        self.start_price = start_price
        self.minimum = minimum
        self.maximum = maximum

        self.rng = np.random.default_rng(seed)

    def simulate(
        self,
        weeks=52
    ):

        prices = [self.start_price]

        for _ in range(weeks - 1):

            change = self.rng.normal(
                0,
                300
            )

            new_price = (
                prices[-1]
                + change
            )

            new_price = np.clip(
                new_price,
                self.minimum,
                self.maximum
            )

            prices.append(new_price)

        return np.array(prices)