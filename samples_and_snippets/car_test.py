from samples_and_snippets.get_car import get_car
from smartpark.car import Car
from samples_and_snippets.numberplate_generator import create_plate

car = Car(create_plate(), get_car())

print(car.number_plate, car.make_model)
