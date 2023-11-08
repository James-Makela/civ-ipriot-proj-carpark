import unittest
import smartpark.config_parser as pc
from smartpark.simple_mqtt_carpark import CarPark


class TestCarPark(unittest.TestCase):
    """
    This is the unittest class to test the class CarPark
    """
    def setUp(self):
        self.config = pc.parse_config("car-park")
        self.car_park = CarPark(self.config)
        self.free_spots = self.car_park.available_spaces

    def test_car_park_is_car_park(self):
        self.assertIsInstance(self.car_park, CarPark)

    def test_car_entry_reduces_available_spots(self):
        self.car_park.on_car_entry()
        self.assertEqual(self.car_park.available_spaces, self.free_spots - 1)

    def test_car_exit_gives_correct_result(self):
        self.car_park.on_car_exit()
        if self.config["total-cars"] == 0:
            self.assertEqual(self.car_park.available_spaces, self.free_spots)
        else:
            self.assertEqual(self.car_park.available_spaces, self.free_spots + 1)


if __name__ == "__main__":
    unittest.main()
