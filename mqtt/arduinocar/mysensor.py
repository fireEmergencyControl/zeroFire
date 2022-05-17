from threading import Thread
from paho.mqtt import publish
import time
import RPi.GPIO as gpio
import adafruit_dht
import board
import io
import picamera
import threading

class PirSensor(Thread):
    def __init__(self):
        super().__init__() #상속받은 클래스의 매개변수 없는 생성자를 호출
        gpio.setmode(gpio.BCM)
        self.pir_pin = 17
        gpio.setup(self.pir_pin,gpio.IN)
        # self.client = client
        
    def run(self):
        try:
            while True:
                if gpio.input(self.pir_pin) == 1:             
                    print("motion detected....")
                    publish.single("iot/pir","motion detected",hostname="172.30.1.55") # ,hostname="172.30.1.55"
                else:                   
                    print("no motion....")
                time.sleep(1) 
        
        except KeyboardInterrupt:
            pass
        finally:
            pass
        
class DHT11(Thread):
    def __init__(self,client):
        super().__init__() #상속받은 클래스의 매개변수 없는 생성자를 호출
        self.mydht11 = adafruit_dht.DHT11(board.D13)
        self.client = client
        
    def run(self):
        while True:
            try:
                humidity_data = self.mydht11.humidity
                temperature_data = self.mydht11.temperature
                # self.client.publish([{"iot/DHT11/humidity",humidity_data},{"iot/DHT11/temperature",temperature_data}])
                self.client.publish("iot:humidity","humidity:"+str(humidity_data))
                self.client.publish("iot:temperature","temperature:"+str(temperature_data))
                print(humidity_data,temperature_data)
                time.sleep(2) # 대기시간이 2초 필요 - 센서 내부에서 초기화작업시 필요한 시간
            
            except RuntimeError as error:
                print(error.args[0])
            
            finally:
                pass
            
class HC_SR04(Thread):
    def __init__(self,client):
        super().__init__() #상속받은 클래스의 매개변수 없는 생성자를 호출
        gpio.setmode(gpio.BCM)
        self.TRIGER = 5
        self.ECHO = 6 
        gpio.setup(self.TRIGER,gpio.OUT)
        gpio.setup(self.ECHO,gpio.IN)
        self.client = client
    
    def getDistance(self):
        gpio.output(self.TRIGER,False)
        time.sleep(1)
        gpio.output(self.TRIGER,True)
        time.sleep(0.00001)
        gpio.output(self.TRIGER,False)

        while gpio.input(self.ECHO) == 0 :
            pulse_start = time.time() # 현재 시간을 측정
            
        while gpio.input(self.ECHO) == 1 :
            pulse_end= time.time() # ECHO가 LOW
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration*340*100/2
        distance = round(distance,2)
        
        return distance
    
    def run(self):
        try:
            while True:
                distance_value = HC_SR04.getDistance(self)
                if 2 < distance_value < 400:
                    self.client.publish("iot:HC_SR04","distance:"+str(distance_value))
                    print("distance: %.2f cm" % distance_value)
                else:
                    print("범위가 벗어남")
        except KeyboardInterrupt:
            pass
        finally:
            gpio.cleanup() 
            
# class MyCamera(Thread):
#     def __init__(self,client):
#         super().__init__() #상속받은 클래스의 매개변수 없는 생성자를 호출
#         self.frame = None
#         self.thread = None
#         self.client = client
    
#     # streaming메소드를 쓰레드로 동작시키며 스트리밍되는 frame을 외부로 보내는 메소드
#     def getStreaming(self):
#         if MyCamera.thread is None:
#             MyCamera.thread = Thread(target=self.streaming)
#             MyCamera.thread.start()
#             while self.frame is None: #프레임이 생길때까지 대기
#                 time.sleep(0)
#         return self.frame
        
        
        
#     # Thread로 실행흐름을 분리 - 파이카메라로 찍은 영상을 프레임 단위로 보내는 메소드
#     # 인스턴스메소드, 클래스메소드(@classmethod 표시)
#     # io모듈은 다양한 i/o처리를 위해 제공되는 모듈
#     # 텍스트,바이너리, raw
#     # 텍스트 
#     # - string, f = open("myfile.txt","r")
#     # - io.StringIO(메모리 스트림)
#     # 바이너리
#     # f = open("myfile.jpg","rb")
#     # 인메모리 바이너리스트림
#     # io.BytesIO(b'XXXXXX')
    
#     @classmethod
#     def streaming(self,c):  #c는 클래스명
#         with picamera.PiCamera() as camera:
#             camera.resolution = (320,240)
#             camera.hflip = True
#             camera.vflip = True
            
#             camera.start_preview()
#             time.sleep(2)
            
#             stream = io.BytesIO() # 한컷한컷 저장
#             for f in camera.capture_continuous(stream, "jpeg", use_video_port=True):
#                 stream.seek(0)
#                 c.frame = stream.read()   #c는 클래스명
#                 # 다음캡쳐를 위한 준비 -파일의 내용을 비우기
#                 stream.seek(0)
#                 stream.truncate()
                
#     def run(self):
#         try:
#             while True:
#                 frame = self.camera.getStreaming()
#                 self.client.publish("picamera:mycamera",frame,hostname="172.30.1.55")   
#         except KeyboardInterrupt:
#             pass
#         finally:
#             gpio.cleanup() 
            
