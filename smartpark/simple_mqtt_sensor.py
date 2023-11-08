""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
from config_parser import parse_config
import mqtt_device
from sense_emu import SenseHat

sense = SenseHat()


class Sensor(mqtt_device.MqttDevice):

    @property
    def temperature(self):
        """Returns the current temperature"""
        return sense.temperature

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'up':
                        self.on_detection(f"entered, {self.temperature}")
                    elif event.direction == 'down':
                        self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':
    configuration1 = parse_config('sensor')
    sensor1 = Sensor(configuration1)

    print("Sensor initialized")
    sensor1.start_sensing()
