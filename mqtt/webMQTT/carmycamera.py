import picamera
import threading
from threading import Thread
import io
import time

class Mycam(Thread):
    frame = None
    thread = None
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client
        
    
    def run(self):
        with picamera.PiCamera() as camera:
            while True:
                camera.resolution = (320,240)
                camera.hflip = True 
                camera.vflip = True        

                camera.start_preview()
                time.sleep(2)
                
                stream = io.BytesIO() 
                for f in camera.capture_continuous(stream,"jpeg",use_video_port=True): 
                    stream.seek(0)
                    self.frame = stream.read()
                    
                    stream.seek(0)
                    stream.truncate()
                    self.client.publish("picamera:mycamera",self.frame)