import numpy as np

from src.fishstock import FishStock


def test_stock_positive():

    model = FishStock()

    stock, _ = model.simulate()

    assert min(stock) > 0


def test_stock_length():

    model = FishStock()

    stock, _ = model.simulate()

    assert len(stock) == 53


def test_harvest_length():

    model = FishStock()

    _, harvests = model.simulate()

    assert len(harvests) == 52