import RPi.GPIO as GPIO
import time

led_pin = 11;
power_pin = 7;
signal_pin = 2;
sensor_min = 0;
sensor_max = 521;

value = 0; # 센서값
level = 0; # 물수위

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(power_pin, GPIO.IN)
GPIO.setup(signal_pin, GPIO.IN)
GPIO.setup(sensor_min, GPIO.IN)
GPIO.setup(sensor_max, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        power = GPIO.input(power_pin,1) # 센서 켬
        time.sleep(1)
        value = GPIO.input(signal_pin,1) # 센서 값 읽어옴
        led = GPIO.input(led_pin,0) # 센서 끔

        level = map(value, sensor_min, sensor_max, 0, 10); # 10 단계
        print("현재 수위 상태 :")
        print(level);
        time.sleep(10)

except KeyboardInterrupt:
        GPIO.cleanup()

# 아두이노 코드
# #define POWER_PIN  7
# #define SIGNAL_PIN A5
# #define SENSOR_MIN 0
# #define SENSOR_MAX 521
#
# int value = 0; // variable to store the sensor value
# int level = 0; // variable to store the water level
#
# void setup() {
#   Serial.begin(9600);
#   pinMode(POWER_PIN, OUTPUT);   // configure D7 pin as an OUTPUT
#   digitalWrite(POWER_PIN, LOW); // turn the sensor OFF
# }
#
# void loop() {
#   digitalWrite(POWER_PIN, HIGH);  // turn the sensor ON
#   delay(10);                      // wait 10 milliseconds
#   value = analogRead(SIGNAL_PIN); // read the analog value from sensor
#   digitalWrite(POWER_PIN, LOW);   // turn the sensor OFF
#
#   level = map(value, SENSOR_MIN, SENSOR_MAX, 0, 4); // 4 levels
#   Serial.print("Water level: ");
#   Serial.println(level);
#
#   delay(1000);
# }

# 아두이노 코드
# #define POWER_PIN  7
# #define SIGNAL_PIN A5
#
# int value = 0; // variable to store the sensor value
#
# void setup() {
#   Serial.begin(9600);
#   pinMode(POWER_PIN, OUTPUT);   // configure D7 pin as an OUTPUT
#   digitalWrite(POWER_PIN, LOW); // turn the sensor OFF
# }
#
# void loop() {
#   digitalWrite(POWER_PIN, HIGH);  // turn the sensor ON
#   delay(10);                      // wait 10 milliseconds
#   value = analogRead(SIGNAL_PIN); // read the analog value from sensor
#   digitalWrite(POWER_PIN, LOW);   // turn the sensor OFF
#
#   Serial.print("Sensor value: ");
#   Serial.println(value);
#
#   delay(1000);
# }


# 물높이 센서 case 1
# #!/usr/bin/python3
# """
# # RPi.GPIO modul - Digital INPUT.
# # DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
# # 20,16,12 : Arduino Water level sensor
# """
# import RPi.GPIO as GPIO
# import time
#
# SENS = []
# SENS.extend((14, 15, 18))       # Arduino Sensors
# SENS.extend((23, 24))           # Blank
# SENS.extend((25, 8, 7, 1))      # XKC-Y25-T12V SKU: SEN0204
#
# PORTS = len(SENS)
#
# def setup():
#     # BroadCom Chip Pin# Set
#     GPIO.setmode(GPIO.BCM)
#     for n in range(PORTS):
#         GPIO.setup(SENS[n], GPIO.IN)
#
# def loop():
#     COUNT = 1
#     while True:
#         print('-------------- count: %s' % COUNT)
#
#         for n in range(PORTS):
#             num_bcm = str()
#             read_bcm = GPIO.input(SENS[n])
#
#             if SENS[n] >= 10:
#                 num_bcm = str(SENS[n])
#             else:
#                 num_bcm = '0' + str(SENS[n])
#             print('GPIO# %s = %s' % (num_bcm, read_bcm))
#
#         print()
#         time.sleep(1)
#         COUNT += 1
#
#
# def main():
#     setup()
#
#     try:
#         loop()
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#
#
# if __name__ == '__main__':
#     main()

# 물높이 센서 case 2
