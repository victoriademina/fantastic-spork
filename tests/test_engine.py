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
