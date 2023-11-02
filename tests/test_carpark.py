import unittest
import smartpark.config_parser as pc
import smartpark
from smartpark import simple_mqtt_carpark
from smartpark.simple_mqtt_carpark import CarPark


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.config = pc.parse_config("carpark")
        self.carpark = CarPark(self.config)
        self.free_spots = self.carpark.available_spaces

    def test_carpark_is_carpark(self):
        self.assertIsInstance(self.carpark, CarPark)

    def test_car_entry_reduces_available_spots(self):
        self.carpark.on_car_entry()
        self.assertEqual(self.carpark.available_spaces, self.free_spots - 1)

    def test_car_exit_gives_correct_result(self):
        self.carpark.on_car_exit()
        if self.config["total-cars"] == 0:
            self.assertEqual(self.carpark.available_spaces, self.free_spots)
        else:
            self.assertEqual(self.carpark.available_spaces, self.free_spots + 1)


if __name__ == "__main__":
    unittest.main()
