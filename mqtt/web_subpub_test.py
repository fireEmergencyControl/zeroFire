from mymqtt import MqttWorker
if __name__ == "__main__":
    try:
        mqtt = MqttWorker()
        mqtt.mymqtt_conncet()
        for i in range(10):
            print(i)
    except KeyboardInterrupt:
        pass
    finally:
        print("종료===============================")
