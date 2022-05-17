package com.multicamp.mainapp.zerofiretab.tabLocation

import android.net.Uri
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.SeekBar
import androidx.fragment.app.Fragment
import com.multicamp.mainapp.zerofiretab.tabLocation.controldata.MyMqtt
import com.multicamp.mainapp.R
import kotlinx.android.synthetic.main.activity_control_tab.*
import org.eclipse.paho.client.mqttv3.MqttMessage
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.MediaController
import android.widget.VideoView

class ControlTab : Fragment(), View.OnClickListener {
    val sub_topic = "iot/#"
    val humidity_topic = "iot:humidity"
    val temperature_topic = "iot:temperature"
    val distance_topic = "iot:HC_SR04"
    val server_uri ="tcp://192.168.0.2:1883" //broker의 ip와 port
    var mymqtt : MyMqtt? = null
    var mwebview:WebView?=null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d("test","onCreateView!!!!!!!!!!!!!!!!!!!!!!!!!")
        val view=inflater.inflate(R.layout.activity_control_tab,container,false)

        mwebview=view.findViewById(R.id.cctvweb)
        mwebview?.setWebViewClient(WebViewClient())
        mwebview?.setBackgroundColor(255)
        mwebview?.settings?.loadWithOverviewMode=true
        mwebview?.settings?.useWideViewPort=true
        mwebview?.settings?.builtInZoomControls=true
        mwebview?.settings?.javaScriptEnabled=true
        mwebview?.settings?.javaScriptCanOpenWindowsAutomatically=false
        mwebview?.settings?.allowFileAccess=true
        mwebview!!.settings.cacheMode=WebSettings.LOAD_NO_CACHE
        mwebview?.settings?.domStorageEnabled=true
        mwebview?.settings?.allowContentAccess=true
        mwebview!!.loadUrl("http://192.168.0.2:8000/mqttvideo/")
//        mwebview!!.loadData("<html><head><style type='text/css'>body{margin:auto auto;text-align:center;}"+
//                "img{width:100%;} div{overflow: hidden;}"+
//                "</style></head><body><div><img src='http://192.168.0.2:8080/mqttvideo/'></div></body></html>",
//                "text/html",  "UTF-8");
        return view
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {

        super.onViewCreated(view, savedInstanceState)
        Log.d("test","onViewCreated!!!!!!!!!!!!!!!!!!!!!!!!!")
        //Mqtt통신을 수행할 Mqtt객체를 생성
        mymqtt = context?.let { MyMqtt(it, server_uri) }
        //블커에서 메시지가 전달되면 호출될 메소드를 넘기기
        mymqtt?.mysetCallback(::onReceived)
        //브로커연결
        mymqtt?.connect(arrayOf<String>(sub_topic,humidity_topic,temperature_topic,distance_topic)) //여기에 토픽 추가

        //이벤트 연결
        Forward.setOnClickListener(this)
        Stop.setOnClickListener(this)
        Backward.setOnClickListener(this)
        LeftForward.setOnClickListener(this)
        LeftBackward.setOnClickListener(this)
        RightForward.setOnClickListener(this)
        RightBackward.setOnClickListener(this)
        watermotor_on.setOnClickListener(this)
        watermotor_off.setOnClickListener(this)

        var listener = object: SeekBar.OnSeekBarChangeListener{
            // seekbar의 값이 변경되었을때
            // fromUser -> 사용자에 의해서 설정이 된 것인지 코드로 설정된 것인지 구분
            //              사용자가 설정 : true, 코드로 설정하면: false
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {

                if(fromUser){
                    Log.d("test","=, $progress ===")
                    when(seekBar?.id){
                        R.id.seekBar1 -> {
                            mymqtt?.publish("iot/water","servo:$progress")
                        }
                    }
                }else{

                }
            }
            // 사용자가 터치했을때
            override fun onStartTrackingTouch(seekBar: SeekBar?) {

            }
            //사용자가 터치를 끝냈을때
            override fun onStopTrackingTouch(seekBar: SeekBar?) {

            }

        }
        seekBar1.setOnSeekBarChangeListener(listener)
    }


    //액티비티내부에 디자인된 위젯을 액세스해야 하므로 외부 클래스에 있으면 액티비티의 구성요소를 접근하기 위해서
    //액티비티를 넘겨주어야 하는 번거로움을 없애기 위해 액티비티내부에 메소드를 정의
    fun onReceived(topic:String,message: MqttMessage){
        //토픽의 수신을 처리
        //EditText에 내용을 출력하기, 영상출력, .... 도착된 메시지안에서 온도랑 습도 데이터를 이용해서 차트그리기,
        // 모션 detact가 전달되면 Notification도 발생시키기.....
        val msg = String(message.payload)
        }


    override fun onClick(v: View?) {
        var data:String=""
        if(v?.id== R.id.Forward){
            data = "forward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.Stop){
            data = "stop"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.Backward){
            data = "backward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.LeftForward){
            data = "leftforward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.LeftBackward){
            data = "leftbackward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.RightForward){
            data = "rightforward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.RightBackward){
            data = "rightbackward"
            mymqtt?.publish("iot/servo","car:"+data)
        }else if(v?.id== R.id.watermotor_on){
            data = "watermotor_on"
            mymqtt?.publish("iot/servo","watermotor:"+data)
        }else if(v?.id== R.id.watermotor_off){
            data = "watermotor_off"
            mymqtt?.publish("iot/servo","watermotor:"+data)
        }else if(v?.id== R.id.camerastart){
            mymqtt?.publish("iot/camera","camera:start")
        }
    }
}
