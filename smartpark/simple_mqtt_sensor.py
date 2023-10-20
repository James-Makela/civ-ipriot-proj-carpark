""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random
from config_parser import parse_config
import mqtt_device
from sense_emu import SenseHat
sense2 = SenseHat()


class Sensor(mqtt_device.MqttDevice):

    @property
    def temperature(self):
        """Returns the current temperature"""
        #  return random.randint(10, 35)
        return sense2.temperature

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:

            # print("Press E when 🚗 entered!")
            # print("Press X when 🚖 exited!")
            # detection = input("E or X> ").upper()
            # if detection == 'E' or sense.stick.direction_up:
            #     self.on_detection(f"entered, {self.temperature}")
            # elif sense.stick.direction_down:
            #     self.on_detection(f"exited, {self.temperature}")
            # else:
            #     self.on_detection(f"exited, {self.temperature}")
            for event in sense2.stick.get_events():
                if event.action == 'pressed':
                    print(event.direction)
                    if event.direction == 'up':
                        self.on_detection(f"entered, {self.temperature}")
                    elif event.direction == 'down':
                        self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':
    config1 = parse_config('sensor')

    sensor1 = Sensor(config1)

    print("Sensor initialized")
    sensor1.start_sensing()

    sensor1.start_sensing()
