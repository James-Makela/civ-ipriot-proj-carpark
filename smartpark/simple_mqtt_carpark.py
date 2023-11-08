from datetime import datetime
import toml
import mqtt_device
from paho.mqtt.client import MQTTMessage
from config_parser import parse_config


class CarPark(mqtt_device.MqttDevice):
    """Creates a car park object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self._temperature = None

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        assert available > 0, "There should be no cars to exit"
        if available > self.config['total-spaces']:
            self.total_cars = 0
            return self.config['total-spaces']
        self.update_cars_in_config()
        return max(available, 0)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        if self.available_spaces == 0:
            spaces = "CARPARK FULL"
        else:
            spaces = f"SPACES: {self.available_spaces}"
        print(
            (
                f"TIME: {readable_time}, "
                + f"{spaces}, "
                + f"TEMPC: {self.temperature}"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"{spaces}, "
            + f"TEMPC: {self.temperature}"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()
        temp = round(float(payload.split(',')[1]), 1)
        self.temperature = temp
        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()

    def start_listening(self):
        self.client.loop_forever()

    def update_cars_in_config(self):
        full_config = parse_config("all")
        full_config['car-park']['total-cars'] = self.total_cars
        with open('../config/config.toml', "w") as config_file:
            toml.dump(full_config, config_file)


if __name__ == '__main__':
    configuration = parse_config('car-park')
    car_park = CarPark(configuration)
    car_park.start_listening()
    print("CarPark initialized")
