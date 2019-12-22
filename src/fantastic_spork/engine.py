import math


class Unit:
    def __init__(self, x, y, health, experience):
        """Constructor"""
        self.x = x
        self.y = y
        self.health = health
        self.experience = experience

    def is_alive(self):
        """Returns True if the unit is alive"""
        if self.health > 0:
            return True
        else:
            return False

    def strength(self):
        """Calculates the unit's strength"""
        result = int(math.ceil((self.health / 2) * ((self.experience + 100) / 100)))
        return result

    def wound(self, points):
        """Updates health and experience after a fight"""
        self.health = self.health - points
        self.experience = self.experience + int(math.ceil(points / 2))
        if self.experience > 100:
            self.experience = 100

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


def fight(unit_x, unit_y):
    x = unit_x.strength()
    y = unit_y.strength()

    unit_x.wound(y)
    unit_y.wound(x)


def calc_new_coordinates(landscape, coordinates, direction):
    new_x, new_y = coordinates
    if direction == "N":
        new_y += 1
    elif direction == "S":
        new_y -= 1
    elif direction == "E":
        new_x += 1
    else:
        new_x -= 1
    if 0 <= new_x < len(landscape) and 0 <= new_y < len(landscape[0]) and landscape[new_x][new_y] == 1:
        return new_x, new_y
    return None


def find_unit(units, coordinates):
    for i in units:
        if i.x == coordinates[0] and i.y == coordinates[1]:
            return i
    return None


def move_unit(landscape, units, coordinates, direction):
    unit = find_unit(units, coordinates)

    new_coordinates = calc_new_coordinates(landscape, coordinates, direction)
    if new_coordinates is None:
        return None

    opponent = find_unit(units, new_coordinates)
    if opponent is None:
        unit.set_coordinates(new_coordinates[0], new_coordinates[1])
        return "Moved"

    fight(unit, opponent)

    if unit.is_alive() and not opponent.is_alive():
        units.remove(opponent)
        unit.set_coordinates(new_coordinates[0], new_coordinates[1])
        return "Win"

    if not unit.is_alive():
        if not opponent.is_alive():
            units.remove(opponent)
        units.remove(unit)
        return "Loose"

    if unit.is_alive() and opponent.is_alive():
        return "Draw"
