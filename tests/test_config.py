import unittest
import toml  # you can use toml, json,yaml, or ryo for your config file
import smartpark.config_parser as pc


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):
        parking_lot_config = pc.parse_config("carpark")
        self.assertEqual(parking_lot_config['location'], "L306")
        self.assertEqual(parking_lot_config['total-spaces'], 130)


if __name__ == "__main__":
    unittest.main()
