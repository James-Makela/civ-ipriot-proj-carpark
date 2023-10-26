import mqtt_device
import time
from config_parser import parse_config
from sense_emu import SenseHat


class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""

    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        sense = SenseHat()
        print('*' * 20)
        for val in args:
            print(val)
            # time.sleep(.2)
            sense.show_message(val)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        self.display(*data.split(','))
        # TODO: Parse the message and extract free spaces,\
        #  temperature, time


if __name__ == '__main__':
    config = parse_config('display')
    display = Display(config)
