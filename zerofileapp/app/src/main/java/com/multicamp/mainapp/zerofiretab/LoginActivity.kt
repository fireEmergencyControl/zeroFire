package com.multicamp.mainapp.zerofiretab

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.os.Looper
import android.util.AttributeSet
import android.util.Log
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.multicamp.mainapp.R
import kotlinx.android.synthetic.main.activity_login.*
import okhttp3.*
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.*
import org.json.JSONObject
import kotlin.concurrent.thread

class LoginActivity : AppCompatActivity(){
    var mymqtt:MyMqtt?=null
    val server_uri="tcp://192.168.0.2:1883"
    var udpThread:Thread?=null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        mymqtt= MyMqtt(this,server_uri)
        mymqtt?.setCallback(::onReceived)
        mymqtt?.connect(arrayOf<String>("iot/#"))
        loginSubmit.setOnClickListener {
            thread{
                var jsonobj=JSONObject()
                jsonobj.put("ID",loginID.text)
                jsonobj.put("PW",loginPW.text)
                val client=OkHttpClient()
                val jsondata=jsonobj.toString()
                val builder= Request.Builder()
                val url="http://127.0.0.1:8000/loginandroid"
                val nextIntent= Intent(this,Tab_main::class.java)
                builder.url(url)
                builder.post(RequestBody.create(MediaType.parse("application/json"),jsondata))
                val myrequest:Request=builder.build()
                val response:Response=client.newCall(myrequest).execute()
                var result:String?=response.body()?.string()
                print(result)
                Log.d("test",result+"test result 11111111111111111111111111111111111111")
                result = result?.replace("\""," ")?.trim()
                if(result=="ok"){
                    Log.d("test",result!!+"ok result here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    startActivity(nextIntent)
                }else{
                    Log.d("test","else result here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    runOnUiThread {Toast.makeText(this,"로그인 실패!!",Toast.LENGTH_SHORT).show()}

                }

                Log.d("test",result!!+"result here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            }
        }
    }

//    override fun onClick(v:View?){
//        var ID=loginID.text.toString()
//        var pass=loginPW.text.toString()
//        var data:String=""
//        if(v?.id==R.id.loginSubmit){
//            data="login"
//        }
//        mymqtt?.publish("iot/$data",ID+":"+pass)
//
//        val nextIntent= Intent(this,Tab_main::class.java)
//        startActivity(nextIntent)
//    }


    fun onReceived(topic:String,message:MqttMessage){
        val msg=String(message.payload)
        Log.d("mymqtt","onReceived message 1111111111111")

    }
}



//////////////////////////////////////////////////////////////////////////////



