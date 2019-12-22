import math


def fight(health_x, exp_x, health_y, exp_y):
    strength_x = int(math.ceil((health_x / 2) * ((exp_x + 100) / 100)))
    strength_y = int(math.ceil((health_y / 2) * ((exp_y + 100) / 100)))
    new_health_x = health_x - strength_y
    new_health_y = health_y - strength_x
    new_exp_x = exp_x + int(math.ceil(strength_y / 2))
    if new_exp_x > 100:
        new_exp_x = 100
    new_exp_y = exp_y + int(math.ceil(strength_x / 2))
    if new_exp_y > 100:
        new_exp_y = 100

    return new_health_x, new_exp_x, new_health_y, new_exp_y


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
    count = 0
    for i in units:

        if i[0] == coordinates[0] and i[1] == coordinates[1]:
            return count
        else:
            count += 1
    return None


def move_unit(landscape, units, coordinates, direction):
    id = find_unit(units, coordinates)
    unit = units[id]
    new_coordinates = calc_new_coordinates(landscape, coordinates, direction)
    if new_coordinates is None:
        return None
    opponent_id = find_unit(units, new_coordinates)
    if opponent_id is None:
        new_unit = new_coordinates[0], new_coordinates[1], unit[2], unit[3]
        units[id] = new_unit
        return "Moved"
    opponent = units[opponent_id]
    fight_result = fight(unit[2], unit[3], opponent[2], opponent[3])
    new_unit = unit[0], unit[1], fight_result[0], fight_result[1]
    new_opponent = opponent[0], opponent[1], fight_result[2], fight_result[3]
    if fight_result[2] <= 0 and fight_result[0] > 0:
        units.remove(opponent)
        new_new_unit = new_coordinates[0], new_coordinates[1], fight_result[0], fight_result[1]
        units[id] = new_new_unit
        return "Win"
    if fight_result[0] <= 0:
        if fight_result[2] <= 0:
            units.remove(opponent)
        else:
            units[opponent_id] = new_opponent
        units.remove(unit)
        return "Loose"
    if fight_result[2] > 0 and fight_result[0] > 0:
        units[id] = new_unit
        units[opponent_id] = new_opponent
        return "Draw"
