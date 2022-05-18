from cgi import test
import threading
import paho.mqtt.client as mqtt
from threading import Thread, Event
from mysensor import DHT11
from device import LED, SERVO, CARMOTOR, WATERMOTOR
from carmycamera import Mycam
import RPi.GPIO as gpio
import paho.mqtt.publish as publisher

class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.led = LED()
        self.servo = SERVO()
        self.motor = CARMOTOR()
        self.watermotor = WATERMOTOR()
        
        self.exit_event = Event()
        self.DHT11 = DHT11(self.client)
        self.DHT11.start()
        self.camera = Mycam(self.client)
        self.camera.start()
        
        
        # self.HC_SR04 = HC_SR04(self.client)
        # self.HC_SR04.start()
        
        # self.camera =  MyCamera(self.client)
        # self.camera.start(self.client)
    
    def signal_handler(self,signum,frame):
        print("signal_handler===================================")
        self.exit_event.set() # 이벤트객체가 갖고 있는 플래그 변수가 True로 셋팅
        self.led.clean()
        # 현재 이벤트 발생을 체크하고 다른 작업을 수행하기 위한 코드 - 다른 메소드에서 처리
        if self.exit_event.is_set():
            print("이벤트객체의 플래그변수가 Ture로 바뀜 - 이벤트가 발생하면 어떤 작업을 실행하기 위해서(다른 메소드 내부에서 반복문 빠져나오기~....)")
            exit(0)
        
    def mymqtt_connect(self): # 사용자정의 함수 - mqtt서버연결과 쓰레드생성 및 시작을 사용자정의 함수로 정의
        try:
            print("브로커 연결 시작하기")
            self.client.connect("172.30.1.21",1883,60)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start()
        except KeyboardInterrupt:
            pass
        finally:
            print("종료") 
               
    def on_connect(self,client, userdata, flags, rc): # broker접속에 성공하면 자동으로 호출되는 callback함수
        print("connect..."+str(rc)) # rc가 0이면 성공 접속, 1이면 실패
        if rc==0 : #연결이 성공하면 구독신청
            client.subscribe("iot/#")
            client.subscribe("web")
        else:
            print("연결실패.....")   
            
    # 라즈베리파이가 메시지를 받으면 호출되는 함수이므로 받은 메시지에 대한 처리를 구현
    def on_message(self,client, userdata, message): 
        try:
            print("test~~~~~")
            myval = message.payload.decode("utf-8")
            print(message.topic+"-----"+myval)
            myval2 = myval.split(":")
            # if myval == "led_on":
            #     self.led.led_on()
            # elif myval == "led_off":
            #     self.led.led_on()
            # elif myval == "0":
            #     self.servo.getDuty(int(myval))
            # elif myval == "180":
            #     self.servo.getDuty(int(myval))
            if myval2[1] == "forward":
                self.motor.forward()
            elif myval2[1] == "backward":
                self.motor.backward()
            elif myval2[1] == "leftforward":
                self.motor.left()
            elif myval2[1] == "leftbackward":
                self.motor.backwardleft()
            elif myval2[1] == "rightforward":
                self.motor.right()
            elif myval2[1] == "rightbackward":
                self.motor.backwardright()
            elif myval2[1] == "stop":
                self.motor.stop()    
            elif myval2[0] == "servo":
                self.servo.getDuty(int(myval2[1]))
            elif myval2[1] == "watermotor_on":
                self.watermotor.watermotor_on()
            elif myval2[1] == "watermotor_off":
                self.watermotor.watermotor_off()
            elif myval2[1] == "start":
                camerathread = threading.Thread(target=self.cameratest)
                camerathread.start()
                
        except:
            pass
        finally:
            pass
        

         
        
        

        