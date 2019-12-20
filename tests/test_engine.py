import pytest
from fantastic_spork import engine


@pytest.mark.parametrize(
    "health_x,exp_x,health_y,exp_y,expected_health_x,expected_exp_x,expected_health_y,expected_exp_y",
    [
        (100, 0, 100, 0, 50, 25, 50, 25),
        (100, 100, 100, 0, 50, 100, 0, 50),
        (10, 45, 1, 99, 9, 46, -7, 100),
    ],
)
def test_fight(health_x, exp_x, health_y, exp_y, expected_health_x, expected_exp_x, expected_health_y, expected_exp_y):
    assert engine.fight(health_x, exp_x, health_y, exp_y) == (
        expected_health_x, expected_exp_x, expected_health_y, expected_exp_y)


@pytest.mark.parametrize(
    "landscape,coordinates,direction,expected",
    [
        ([[1, 1], [1, 1]], (0, 0), "N", (0, 1)),
        ([[1, 0], [1, 1]], (0, 0), "N", None),
        ([[1, 1], [1, 1]], (1, 0), "S", None),
    ],
)
def test_move_unit(landscape, coordinates, direction, expected):
    assert engine.move_unit(landscape, coordinates, direction) == expected


@pytest.mark.parametrize(
    "units, coordinates,expected",
    [
        ([(0, 0, 100, 0), (3, 4, 50, 25)], (3, 4), 1),
        ([(0, 0, 100, 0), (3, 4, 50, 25)], (2, 2), None),

    ],
)
def test_find_unit(units, coordinates, expected):
    assert engine.find_unit(units, coordinates) == expected
