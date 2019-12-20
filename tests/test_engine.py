import pytest
from fantastic_spork import engine


@pytest.mark.parametrize(
    "health_x,health_y,expected_health_x,expected_health_y",
    [
        (100, 100, 50, 50),
        (75, 100, 25, 62),
        (10, 1, 9, -4),
    ],
)
def test_fight(health_x, health_y, expected_health_x, expected_health_y):
    assert engine.fight(health_x, health_y) == (expected_health_x, expected_health_y)
