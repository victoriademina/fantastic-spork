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
