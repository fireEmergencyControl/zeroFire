import paho.mqtt.publish as publish
from threading import Thread
import RPi.GPIO as gpio
import adafruit_dht
import board
import time


class MySensor(Thread):

    # def getPir(self):
    #     if gpio.input(27) == 1:
    #         print("motion detected.....")
    #         publish.single("iot/test", "motion:detected",
    #                        hostname="192.168.0.5")
    #     if gpio.input(27) == 0:
    #         publish.single("iot/test", "motion:nodetced")

    def getDistance(self):
        gpio.output(self.TRIGER, False)
        time.sleep(1)
        gpio.output(self.TRIGER, True)
        time.sleep(0.0001)
        gpio.output(self.TRIGER, False)

        while gpio.input(self.ECHO) == 0:
            pulse_start = time.time()  # 현재 시간을 측정 - HIGH 신호가 발생되는 시간을 측정

        while gpio.input(self.ECHO) == 1:
            pulse_end = time.time()  # ECHO핀이 신호가 발생되는 시간을 측정

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 340 * 100 / 2
        distance = round(distance, 2)

        return distance

    def __init__(self, client):
        super().__init__()
        self.TRIGER = 5
        self.ECHO = 6
        # self.PIR = 27
        self.MYDRTT1 = adafruit_dht.DHT11(board.D20)
        self.client = client

        # gpio.setup(self.PIR, gpio.IN)
        gpio.setup(self.TRIGER, gpio.OUT)
        gpio.setup(self.ECHO, gpio.IN)
        gpio.setmode(gpio.BCM)

    def run(self):
        while True:
            try:
                # self.getPir()
                self.distance = self.getDistance()
                self.humidity_data = self.MYDRTT1.humidity
                self.tempeature_data = self.MYDRTT1.temperature
                self.msg_humidity = 'humidity:' + str(self.humidity_data)
                self.msg_tempeature = 'tempeature:' + str(self.tempeature_data)
                msg_distance = 'distance:' + str(self.distance)

                self.client.publish('iot/test', msg_distance)
                self.client.publish('iot/test', self.msg_humidity)
                self.client.publish('iot/test', self.msg_tempeature)
                time.sleep(1)
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass
