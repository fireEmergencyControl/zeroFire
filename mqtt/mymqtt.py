from multiprocessing import Event
import signal
import paho.mqtt.client as mqtt
from mydevice import MyDeivice
from mysensor import MySensor
from threading import Thread
import paho.mqtt.publish as publish

from mycame import MyCamera

# Event 객체 - 쓰레드 간의 간단한 통식을 위해 사용한 객체
# - 키보드 인터럽트 시그널을 감지하고 감지하면 미리 등록한 이벤트가 발생햇을 때 처리할 함수가 실행하도록 구현
# 1. 이벤트 객체를 만들기
#    내부적으로 flag변수를 갖고 있다.
#    is_set : 내부 플래그를 True로 설정되었으면 True를 반환
#    set : 내부 플래그를 Ture 설정
# 2. 이벤트가 발생되면 실행할 callback 함수를 정의
# 3. 키보드인터럽트 시그널을 리스닝하고 있다가 이벤트가 발생하면 반응할 수 있도록 등록 - signal 함수가 담당


class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # 1. 이벤트 객체를 생성
        self.exit_event = Event()
        self.led = MyDeivice(self.client)
        self.mysensor = MySensor(self.client)
        self.mysensor.start()
        self.camera = MyCamera()
    # broker접속에 성공하면 자동으로 호출되는 callback 함수

    def mymqtt_conncet(self):
        try:
            print("브로커 연결하기")
            self.client.connect("xxxx", 1883, 60)
            signal.signal(signal.SIGINT, self.singal_hanlder)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start()
        except KeyboardInterrupt:
            pass
        finally:
            print("종료")
    # 2. 언터럽트가 발생되면서 이벤트가 발생되면 호출한 콜백함수

    def singal_hanlder(self, signum, frame):
        print("singal_handelr++++++++++++++++++++++++++++++++")
        self.exit_event.set()  # 이벤트 객체가 갖고 있는 플래그변수가 True로 셋팅
        self.led.clean()
        # 현재 이벤트 발생을 체크하고 다른 작업을 수해아기 위한 코드 - 다른 메소드에서 처리
        if self.exit_event.is_set():
            print(
                "이벤트객체의 플래그 변수가 True로 발생 - 이벤트가 발생하면 얻떤 작업을 실행하기 위해서 (다른 메소드 내부에서 반복문 빠져나오기~....")
            exit(0)

    # 사용자 정의 함수 - mqtt 서버연결과 쓰레드 생성 및 시작을 사용자 정의 함수
    def on_connect(self, client, userdata, flags, rc):
        print("connect..." + str(rc))
        if rc == 0:  # 연결이 성공하면 구독신청
            client.subscribe("iot/#")
        else:
            print("연결실패.....")

    # 라즈베리파이가 메시지를 받으면 호출되는 함수이므로 받은 메시지에 대한 처리를 구현
    def on_message(self, client, userdata, message):
        myval = message.payload.decode("utf-8")

        if myval == "led:on":
            self.led.led_on()
        elif myval == "led:off":
            self.led.led_off()
        else:
            pass

        if myval == "motion:detected":
            self.led.start()

        if myval == "start":
            while True:
                frame = self.camera.getStreaming()
                publish.single("iot/mycamera", frame, hostname="xxxx")

        print(myval)


if __name__ == "__main__":
    try:
        mqtt = MqttWorker()
        mqtt.mymqtt_conncet()
        mqtt.on_connect
        mqtt.on_message
    except KeyboardInterrupt:
        pass
    finally:
        print("종료")
