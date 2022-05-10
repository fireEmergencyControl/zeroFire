import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
from threading import Thread
import mycamera

class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.camera = mycamera.MyCamera()
        
        
    def mymqtt_connect(self): # 사용자정의 함수 - mqtt서버연결과 쓰레드생성 및 시작을 사용자정의 함수로 정의
        try:
            print("브로커 연결 시작하기")
            self.client.connect("172.30.1.55",1883,60)
            self.client.loop_forever()
            
        except KeyboardInterrupt:
            pass
        
        finally:
            print("종료") 
            
               
    def on_connect(self,client, userdata, flags, rc): # broker접속에 성공하면 자동으로 호출되는 callback함수
        print("connect..."+str(rc)) # rc가 0이면 성공 접속, 1이면 실패
        if rc==0 : #연결이 성공하면 구독신청
            client.subscribe("web")
        else:
            print("연결실패.....")   
            
            
    # 라즈베리파이가 메시지를 받으면 호출되는 함수이므로 받은 메시지에 대한 처리를 구현
    def on_message(self,client, userdata, message): 
        try:
            myval = message.payload.decode("utf-8")
            print(message.topic+"-----"+myval)
            if myval == "start":
                while True:
                    frame = self.camera.getStreaming()
                    publisher.single("picamera:mycamera",frame,hostname="172.30.1.55")           
        except:
            pass
        finally:
            pass
        
if __name__ == '__main__':
    mymqtt = MqttWorker()
    mymqtt.mymqtt_connect()