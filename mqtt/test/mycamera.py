import io
import threading
import picamera
import time

class MyCamera:
    frame = None
    thread = None
    # streaming메소드를 쓰레드로 동작시키며 스트리밍되는 frame을 외부로 보내는 메소드
    def getStreaming(self):
        if MyCamera.thread is None:
            MyCamera.thread = threading.Thread(target=self.streaming)
            MyCamera.thread.start()
            while self.frame is None: #프레임이 생길때까지 대기
                time.sleep(0)
        return self.frame
        
        
        
    # Thread로 실행흐름을 분리 - 파이카메라로 찍은 영상을 프레임 단위로 보내는 메소드
    # 인스턴스메소드, 클래스메소드(@classmethod 표시)
    # io모듈은 다양한 i/o처리를 위해 제공되는 모듈
    # 텍스트,바이너리, raw
    # 텍스트 
    # - string, f = open("myfile.txt","r")
    # - io.StringIO(메모리 스트림)
    # 바이너리
    # f = open("myfile.jpg","rb")
    # 인메모리 바이너리스트림
    # io.BytesIO(b'XXXXXX')
    
    @classmethod
    def streaming(c):  #c는 클래스명
        with picamera.PiCamera() as camera:
            camera.resolution = (320,240)
            camera.hflip = True
            camera.vflip = True
            
            camera.start_preview()
            time.sleep(2)
            
            stream = io.BytesIO() # 한컷한컷 저장
            for f in camera.capture_continuous(stream, "jpeg", use_video_port=True):
                stream.seek(0)
                c.frame = stream.read()   #c는 클래스명
                # 다음캡쳐를 위한 준비 -파일의 내용을 비우기
                stream.seek(0)
                stream.truncate()