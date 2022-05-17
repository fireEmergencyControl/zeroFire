package com.multicamp.mainapp.zerofiretab

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.AttributeSet
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import com.multicamp.mainapp.R
import kotlinx.android.synthetic.main.activity_login.*
import okhttp3.*
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.*
import org.json.JSONObject
import kotlin.concurrent.thread

class LoginActivity : AppCompatActivity(),View.OnClickListener{
    var mymqtt:MyMqtt?=null
    val server_uri="tcp://192.168.0.2:1883"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        mymqtt= MyMqtt(this,server_uri)
        mymqtt?.setCallback(::onReceived)
        mymqtt?.connect(arrayOf<String>("iot/#"))
        loginSubmit.setOnClickListener(this)
//        {
//            thread{
//                var jsonobj=JSONObject()
//                jsonobj.put("ID",loginID.text)
//                jsonobj.put("pass",loginPW.text)
//                val client=OkHttpClient()
//                val jsondata=jsonobj.toString()
//                val builder= Request.Builder()
//                val url="http://127.0.0.1:8000/login"
//                builder.url(url)
//                builder.post(RequestBody.create(MediaType.parse("application/json"),jsondata))
//                val myrequest:Request=builder.build()
//                Log.d("test","test55555555555555555555555555555555")
//                val response:Response=client.newCall(myrequest).execute()
//                Log.d("test","test66666666666666666666666666666666")
//                val result:String?=response.body()?.string()
//                Log.d("http",result!!+"result here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
//                val nextIntent= Intent(this,Tab_main::class.java)
//                startActivity(nextIntent)
//            }
//        }
    }
    override fun onClick(v:View?){
        var ID=loginID.text.toString()
        var pass=loginPW.text.toString()
        var data:String=""
        if(v?.id==R.id.loginSubmit){
            data="login"
        }
        mymqtt?.publish("iot/$data",ID+":"+pass)

        val nextIntent= Intent(this,Tab_main::class.java)
        startActivity(nextIntent)
    }


    fun onReceived(topic:String,message:MqttMessage){
        val msg=String(message.payload)
        Log.d("mymqtt","onReceived message 1111111111111")

    }
}



//////////////////////////////////////////////////////////////////////////////



