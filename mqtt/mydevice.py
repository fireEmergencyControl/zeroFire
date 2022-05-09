import RPi.GPIO as gpio
import time


class MyDeivice():
    def __init__(self, client):
        super().__init__()
        self.LED = 17
        self.client = client
        gpio.setmode(gpio.BCM)
        gpio.setup(self.LED, gpio.OUT)

    def start(self):
        for i in range(5):
            gpio.output(self.LED, True)
            time.sleep(1)
            gpio.output(self.LED, False)
            time.sleep(1)

    def led_on(self):
        gpio.output(self.LED, True)
        print("led_on")

    def led_off(self):
        gpio.output(self.LED, False)
        print("led_off")

    def clean(self):
        gpio.cleanup()
