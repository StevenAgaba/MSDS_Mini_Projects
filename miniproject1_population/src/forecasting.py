"""
forecasting.py

Forecasting models.
"""

from abc import ABC, abstractmethod
import numpy as np


class Forecaster(ABC):

    @abstractmethod
    def fit(self, x, y):
        pass

    @abstractmethod
    def predict(self, horizon):
        pass


class LinearTrendForecaster(Forecaster):

    def fit(self, x, y):
        self.x = np.array(x)
        self.coefficients = np.polyfit(x, y, 1)

    def predict(self, horizon):

        slope, intercept = self.coefficients

        future_x = np.arange(
            self.x[-1] + 1,
            self.x[-1] + horizon + 1
        )

        return slope * future_x + intercept


class ExponentialCAGRForecaster(Forecaster):

    def fit(self, x, y):

        self.last_value = y[-1]

        years = len(y) - 1

        self.cagr = (
            (y[-1] / y[0]) ** (1 / years)
        ) - 1

    def predict(self, horizon):

        forecasts = []

        for i in range(1, horizon + 1):

            forecasts.append(
                self.last_value *
                ((1 + self.cagr) ** i)
            )

        return np.array(forecasts)


class FibonacciForecaster(Forecaster):

    def fit(self, x, y):

        self.last_value = y[-1]
        self.phi = 1.618

    def predict(self, horizon):

        forecasts = []

        value = self.last_value

        for _ in range(horizon):

            value = value * self.phi
            forecasts.append(value)

        return np.array(forecasts)