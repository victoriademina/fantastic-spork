import math


def fight(health_x, health_y):
    new_health_x = health_x - int(math.ceil(health_y / 2))
    new_health_y = health_y - int(math.ceil(health_x / 2))

    return new_health_x, new_health_y
