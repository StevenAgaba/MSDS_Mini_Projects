from abc import ABC, abstractmethod
import numpy as np


class Forecaster(ABC):

    @abstractmethod
    def forecast(
        self,
        data
    ):
        pass


class MovingAverage(
    Forecaster
):

    def forecast(
        self,
        data
    ):

        return np.mean(
            data[-3:]
        )


class ExponentialSmoothing(
    Forecaster
):

    def __init__(
        self,
        alpha=0.3
    ):

        self.alpha = alpha

    def forecast(
        self,
        data
    ):

        value = data[0]

        for observation in data[1:]:

            value = (
                self.alpha
                * observation
                +
                (1-self.alpha)
                * value
            )

        return value


class LinearTrend(
    Forecaster
):

    def forecast(
        self,
        data
    ):

        x = np.arange(
            len(data)
        )

        slope, intercept = np.polyfit(
            x,
            data,
            1
        )

        return (
            slope * len(data)
            + intercept
        )