import mqtt_device
from config_parser import parse_config
from sense_emu import SenseHat


class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""

    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')

    @staticmethod
    def display(*args) -> None:
        sense = SenseHat()
        print('*' * 20)
        for val in args:
            print(val)
            sense.show_message(val)
        print('*' * 20)

    def on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        data = data.split(',')
        free_spaces = data[0]
        current_time = data[1]
        temperature = data[2]
        self.display(free_spaces, current_time, temperature)

    def start_listening(self):
        self.client.loop_forever()


if __name__ == '__main__':
    configuration = parse_config('display')
    display = Display(configuration)
    display.start_listening()
