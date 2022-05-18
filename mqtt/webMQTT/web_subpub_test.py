import mymqtt
import mysensor
import RPi.GPIO as gpio

# 테스트 작업을 위한 클래스
if __name__ == '__main__':
    try:
        mqtt = mymqtt.MqttWorker()
        mqtt.mymqtt_connect() #callback 함수가 아니므로 인스턴스 변수를 이용해서 호출해야 한다.
        for i in range(10):
            print(i)
    
    except KeyboardInterrupt:
        gpio.cleanup()
        pass
    
    finally:
         
        print("종료")