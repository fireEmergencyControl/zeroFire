import RPi.GPIO as gpio
import time


class MyBuzzer():
    def __init__(self, client):
        super().__init__()
        self.Buzzer = 19
        self.client = client
        gpio.setmode(gpio.BCM)
        gpio.setup(self.Buzzer, gpio.OUT)
        self.pwm = gpio.PWM(self.Buzzer, 1)

    def start(self):
        self.pwm.start(10)
        while True:
            self.pwm.ChangeFrequency(262)  # 주파수의 변경
            time.sleep(0.5)
            self.pwm.ChangeFrequency(294)  # high 구간을 0으로 설정 - 소리가 꺼진다.
            time.sleep(0.5)
            time.sleep(2)
            self.pwm.ChangeDutyCycle(0)
            self.pwm.stop()
            gpio.cleanup()
