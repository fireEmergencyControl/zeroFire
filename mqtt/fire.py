# 수정필요함
import RPi.GPIO as gpio
import time

led_pin1 = 24
fire_sensor = 20

gpio.setmode(gpio.BCM)

gpio.setup(led_pin1,gpio.OUT)
gpio.setup(fire_sensor,gpio.OUT)

try:
    while 1:
        gpio.output(fire_sensor, gpio.HIGH)
        gpio.output(led_pin1, gpio.HIGH)
        time.sleep(1)
        gpio.output(led_pin1, gpio.LOW)
        time.sleep(1)

except KeyboardInterrupt():
    print("error")
finally:
    gpio.cleanup()

# arduino.cc
#
# int
# fire = 0;
#
# void
# setup()
# {
#   Serial.begin(9600);
# pinMode(9, OUTPUT);
# pinMode(8, OUTPUT);
# }
#
# void
# loop()
# {
#   fire = analogRead(A1);
# delay(100);
# Serial.print("Fire =");
# delay(500);
#
# if (fire > 0)
# {
#   digitalWrite(9, HIGH);
# tone(8, 1000, 50);
# delay(100);
#
# digitalWrite(9, LOW);
# tone(8, 200, 50);
# delay(100);
#
# } else {
#   digitalWrite(9, LOW);
# noTone(8);
# delay(100);
# }
#
# }

# 파이썬으로 변환 필요