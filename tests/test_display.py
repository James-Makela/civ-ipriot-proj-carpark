import unittest
import smartpark.config_parser as pc
from smartpark.simple_mqtt_display import Display
from unittest.mock import MagicMock


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.config = pc.parse_config('display')
        self.display = Display(self.config)

    def test_display_is_display(self):
        self.assertIsInstance(self.display, Display)
