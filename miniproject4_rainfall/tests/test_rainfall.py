from src.region import Region


def test_total():

    region = Region(
        "Test",
        [10, 20, 30]
    )

    assert (
        region.annual_total()
        == 60
    )


def test_mean():

    region = Region(
        "Test",
        [10, 20, 30]
    )

    assert (
        region.mean()
        == 20
    )


def test_variation():

    region = Region(
        "Test",
        [10, 20, 30]
    )

    assert (
        region.coefficient_of_variation()
        > 0
    )