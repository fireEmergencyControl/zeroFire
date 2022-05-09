import RPi.GPIO as gpio
import time

LED = 17


class Led:
    gpio.setmode(gpio.BCM)
    gpio.setup(LED, gpio.OUT)

    def start(self):
        for i in range(5):
            gpio.output(LED, True)
            time.sleep(1)
            gpio.output(LED, False)
            time.sleep(1)

    def led_on(self):
        gpio.output(LED, True)
        print("led_on")

    def led_off(self):
        gpio.output(LED, False)
        print("led_off")


if __name__ == "__main__":
    try:
        while True:
            led = Led()
            led.start()

    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()
