from picamera import PiCamera, Color
from time import sleep
import datetime
import paho.mqtt.publish as publish


class MyCamera():
    def __init__(self):
        super().__init__()
        self.now = datetime.datetime.now()
        # 사진 찍기
        self.camera = PiCamera()  # PICamera 객체 생성
        self.camera.start_preview()  # 미리보기 화면 시작

        sleep(3)

    def run(self):
        for i in range(1, 6):
            self.camera.capture(
                "/home/pi/mywork/raspberry/test_img/date_frame_test%s.jpg" % i)
            sleep(2)
        self.camera.stop_preview()

    def send(self):
        for i in range(1, 6):
            file = open(
                "/home/pi/mywork/raspberry/test_img/date_frame_test%s.jpg" % i, "rb")
            filedeta = file.read()
            bytefiledata = bytearray(filedeta)
            print(bytefiledata)
            file.close()
            publish.single("test/img", bytefiledata, hostname="172.30.1.39")


if __name__ == "__main__":
    camera = MyCamera()
    camera.run()
    camera.send()
