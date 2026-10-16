from src.route import Route


def test_revenue():

    route = Route(
        "Test",
        [10,20],
        1000
    )

    assert (
        route.total_revenue()
        == 30000
    )


def test_mean():

    route = Route(
        "Test",
        [10,20],
        1000
    )

    assert route.mean() == 15


def test_std():

    route = Route(
        "Test",
        [10,20],
        1000
    )

    assert route.std_dev() > 0