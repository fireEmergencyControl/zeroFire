import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
from threading import Thread
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
# FLAME
FLAME = 17  # BCM. 17, wPi. 0, Physical. 11(DOUT에 연결)
GPIO.setup(FLAME, GPIO.IN)
# DHT11
import board
import Adafruit_DHT
mydht11 = Adafruit_DHT.DHT11(board.D6)  # GPIO06 번 핀

# buzzer
class MyBuzzer(Thread):
    def __init__(self, client):
        super().__init__()
        gpio.setmode(gpio.BCM)
        gpio.setup(self.buzzer, gpio.OUT)
        self.buzzer = 19
        self.pwm = gpio.PWM(self.buzzer, 1)
        self.client = client

    def start(self):
        try:
            while True:
                self.pwm.start(10)
                self.pwm.ChangeFrequency(262)  # 주파수의 변경
                time.sleep(0.5)
                self.pwm.ChangeFrequency(294)  # high 구간을 0으로 설정 - 소리가 꺼진다.
                time.sleep(0.5)
                time.sleep(2)
                self.pwm.ChangeDutyCycle(0)
                self.pwm.stop()
        except KeyboardInterrupt:
            pass
        finally:
            gpio.cleanup()

#
# import RPi.GPIO as GPIO
# import time
#
# buzzer = 18
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(buzzer, GPIO.OUT)
#
# pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
# pwm.start(50.0)  # 듀티비를 50%로 설정
#
# scale = [262, 294, 330, 349, 392, 440, 494, 523]
#
# for i in range(0, 8):
#     pwm.ChangeFrequency(scale[i])
#     time.sleep(1.0)
#
# pwm.stop()
# GPIO.cleanup()

# buzzer thread prototype
# class alertbuzzer:
#     def __init__(self, sound, scale, on, off):
#         self.sound = sound
#         self.scale = scale
#         self.on = on
#         self.off = off
#
#     def set_buz(self, set):
#         self.set = set
#         self.buzzer = 18
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.buzzer,GPIO.OUT)
#
#     def run_buz(self):
#         super().__init__()
#         pwm = GPIO.PWM(self.buzzer, 1.0)
#         pwm.start(50.0)
#
#     def buz_off(self):
#         super().__init__()
#         pwm = GPIO.PWM(self.buzzer, 1.0)
#         pwm.stop()
#         GPIO.cleanup()

# flame

class Flame(Thread):
    def __init__(self,flame):
        super().__init__()
        gpio.setmode(gpio.BCM)
        self.flame_sensor=17
        gpio.setup(17,gpio.IN)
        self.flame = flame

    def run(self):
        try:
            while(1):
                now = time.localtime()
                timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" %
                             (now.tm_year, now.tm_mon, now.tm_mday,
                              now.tm_hour, now.tm_min, now.tm_sec))
                if GPIO.input(FLAME) == 1:  # 평소 1을 전송함
                    print(timestamp, "안전")
                else:                      # 불꽃 감지시 0을 전송함
                    print(timestamp, "화재 경보")
                time.sleep(1)
        except:
            print("err or Ctrl - C")
        finally:
            GPIO.cleanup()
            print("END")

# DHT 11

class DHT(Thread):
    def __init__(self):
        super().__init__()
        gpio.setmode(gpio.BCM)
        self.mydht11=6
        gpio.setup(6,gpio.IN)

    def run2(self):
        while True:
            try:
                humidity_data = mydht11.humidity
                temperature_data = mydht11.temperature
                print(humidity_data, temperature_data)
                time.sleep(1)
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass
