import json
import random

car_file = open('../config/cartypes.json')


cars_list = json.load(car_file)


def get_car():
    rand1 = random.randint(0, len(cars_list)) - 1
    rand2 = random.randint(0, len(cars_list[rand1])) - 1

    output = f"{cars_list[rand1]['brand']}, {cars_list[rand1]['models'][rand2]}"
    return output

