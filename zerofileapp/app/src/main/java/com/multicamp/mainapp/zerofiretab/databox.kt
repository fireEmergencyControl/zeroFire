package com.multicamp.mainapp.zerofiretab

import android.content.Context
import android.util.Log
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.*

data class Login(
    val code:String,
    val msg:String
)

class MyMqtt (context: Context, uri:String){
    var mqttClient: MqttAndroidClient = MqttAndroidClient(context,uri, MqttClient.generateClientId())
    fun setCallback(callback:(topic:String,message: MqttMessage)->Unit){
        mqttClient.setCallback(object : MqttCallback {
            override fun connectionLost(cause: Throwable?) {
                Log.d("mymqtt","connectionLost")
            }

            override fun messageArrived(topic: String?, message: MqttMessage?) {
                callback(topic!!,message!!)
            }

            override fun deliveryComplete(token: IMqttDeliveryToken?) {
                Log.d("mymqtt","deliveryComplete")
            }
        })
    }
    fun connect(topic:Array<String>){
        val mqttConnectOptions= MqttConnectOptions()
        mqttClient.connect(mqttConnectOptions,null,object: IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
                Log.d("mymqtt","브로커 접속 성공....")
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                Log.d("mymqtt","브로커 접속 실패....")
            }
        })
    }
    private fun subscribeTopic(topic:String,qos:Int=0){
        mqttClient.subscribe(topic,qos,null,object: IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
                Log.d("mymqtt","subscribe 성공....")
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                Log.d("mymqtt","subscribe 실패....")
            }
        })
    }
    fun publish(topic:String,payload:String,qos:Int=0){
        if(mqttClient.isConnected===false){
            mqttClient.connect()
        }
        val message= MqttMessage()
        message.payload=payload.toByteArray()
        message.qos=qos
        mqttClient.publish(topic,message,null,object : IMqttActionListener {
            override fun onSuccess(asyncActionToken: IMqttToken?) {
                Log.d("mymqtt","메세지 전송 성공....")
            }

            override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                Log.d("mymqtt","메세지 전송 실패....")
            }
        })
    }
}