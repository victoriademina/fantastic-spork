import pytest
from fantastic_spork import engine


@pytest.mark.parametrize(
    "health,expected",
    [
        (100, True),
        (1, True),
        (0, False),
        (-1, False),
    ]
)
def test_unit_is_alive(health, expected):
    unit = engine.Unit(x=0, y=0, health=health, experience=0)
    assert unit.is_alive() == expected


@pytest.mark.parametrize(
    "health,experience,expected",
    [
        (100, 0, 50),
        (1, 0, 1),
        (100, 100, 100),
    ]
)
def test_unit_strength(health, experience, expected):
    unit = engine.Unit(x=0, y=0, health=health, experience=experience)
    assert unit.strength() == expected


@pytest.mark.parametrize(
    "health,experience,points,expected_health, expected_experience",
    [
        (100, 0, 50, 50, 25),
        (100, 100, 50, 50, 100),
    ]
)
def test_unit_wound(health, experience, points, expected_health, expected_experience):
    unit = engine.Unit(x=0, y=0, health=health, experience=experience)
    unit.wound(points)
    assert unit.health == expected_health
    assert unit.experience == expected_experience


def test_unit_set_coordinates():
    new_x = 20
    new_y = 30
    unit = engine.Unit(x=0, y=0, health=100, experience=0)
    unit.set_coordinates(new_x, new_y)
    assert unit.x == new_x
    assert unit.y == new_y


def test_unit_fight():
    unit_x = engine.Unit(x=0, y=0, health=100, experience=50)
    unit_y = engine.Unit(x=1, y=1, health=80, experience=0)
    engine.fight(unit_x, unit_y)
    assert unit_x.health == 60
    assert unit_x.experience == 70
    assert unit_y.health == 5
    assert unit_y.experience == 38


def test_find_unit():
    units = [engine.Unit(0, 0, 100, 0), engine.Unit(1, 1, 100, 0)]
    coordinates = (1, 1)
    assert engine.find_unit(units, coordinates) == units[1]


def test_find_unit_none():
    units = [engine.Unit(0, 0, 100, 0), engine.Unit(1, 1, 100, 0)]
    coordinates = (2, 1)
    assert engine.find_unit(units, coordinates) is None


@pytest.mark.parametrize(
    "landscape,units,coordinates,direction,expected",
    [
        ([[1, 1], [1, 1]], [engine.Unit(0, 0, 100, 0), engine.Unit(0, 1, 100, 0)], (0, 0), "E", "Moved"),
        ([[1, 1], [1, 1]], [engine.Unit(0, 0, 100, 0), engine.Unit(0, 1, 1, 0)], (0, 0), "N", "Win"),
        ([[1, 1], [1, 1]], [engine.Unit(0, 0, 100, 0), engine.Unit(0, 1, 100, 0)], (0, 0), "N", "Draw"),
        ([[1, 1], [1, 1]], [engine.Unit(0, 0, 1, 0), engine.Unit(0, 1, 100, 0)], (0, 0), "N", "Loose"),
        ([[1, 1], [1, 1]], [engine.Unit(0, 0, 100, 0), engine.Unit(0, 1, 100, 0)], (0, 0), "S", None),
    ],
)
def test_move_unit(landscape, units, coordinates, direction, expected):
    assert engine.move_unit(landscape, units, coordinates, direction) == expected


@pytest.mark.parametrize(
    "landscape,coordinates,direction,expected",
    [
        ([[1, 1], [1, 1]], (0, 0), "N", (0, 1)),
        ([[1, 0], [1, 1]], (0, 0), "N", None),
        ([[1, 1], [1, 1]], (1, 0), "S", None),
    ],
)
def test_calc_new_coordinates(landscape, coordinates, direction, expected):
    assert engine.calc_new_coordinates(landscape, coordinates, direction) == expected
