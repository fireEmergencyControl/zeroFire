package com.multicamp.mainapp.zerofiretab.tabLocation

import android.content.Context
import android.graphics.Color
import android.os.Bundle
import android.os.Handler
import android.os.SystemClock
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.github.mikephil.charting.charts.LineChart
import com.github.mikephil.charting.data.Entry
import com.github.mikephil.charting.data.LineData
import com.github.mikephil.charting.data.LineDataSet
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet
import com.multicamp.mainapp.R
import com.multicamp.mainapp.zerofiretab.tabLocation.controldata.MyMqtt
import kotlinx.android.synthetic.main.activity_current_tab.*
import org.eclipse.paho.client.mqttv3.MqttMessage
import kotlin.concurrent.thread

class CurrentTab : Fragment() {
    private var chart: LineChart? = null
    var mymqtt : MyMqtt? = null
    val humidity_topic = "iot:humidity"
    val temperature_topic = "iot:temperature"
    val server_uri ="tcp://192.168.0.2:1883" //broker의 ip와 port
    var isrunning=false
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {val view=inflater.inflate(R.layout.activity_current_tab,container,false)
        return view
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        startButton.setOnClickListener {
            Log.d("test","testlog1@@@@@@@@@@@@")
            if (isrunning == false) {
                isrunning = true
                startButton.text = "그래프 구현중"
                startButton.isClickable = false
                val thread = ThreadClass()
                thread.start()
            }
        }
    }


    inner class ThreadClass : Thread() {
        override fun run() {
            Log.d("test","testlog2@@@@@@@@@@@@")
            fun onReceived(topic:String,message: MqttMessage){
                val msg=String(message.payload)
                val msgdata = msg.split(":")
                if (msgdata[0]=="humidity"){
                    "습도:"+msgdata[1]+"\n"
                }else if(msgdata[0]=="temperature"){
                    "온도:"+msgdata[1]+"\n"
                }
                Log.d("received",msg)
            }
            val input = Array<Double>(30, {})

            Log.d("test","testlog1@@@@@@@@@@@@")
            // Entry 배열 생성
            var entries: ArrayList<Entry> = ArrayList()
            // Entry 배열 초기값 입력
            entries.add(Entry(0F, 0F))
            // 그래프 구현을 위한 LineDataSet 생성
            var dataset: LineDataSet = LineDataSet(entries, "input")
            // 그래프 data 생성 -> 최종 입력 데이터
            var data: LineData = LineData(dataset)
            Log.d("test","testlog2@@@@@@@@@@@@")
            // chart.xml에 배치된 lineChart에 데이터 연결
            linechart.data = data

            requireActivity().runOnUiThread(Runnable {
                // 그래프 생성
                linechart.animateXY(1, 1)
            })

            Log.d("test","testlog3@@@@@@@@@@@@")
            for (i in 0 until input.size) {

                SystemClock.sleep(100)
                data.addEntry(Entry(i.toFloat(), input[i].toFloat()), 0)
                data.notifyDataChanged()
                linechart.notifyDataSetChanged()
                linechart.invalidate()
            }
            startButton.text = "시작"
            startButton.isClickable = true
            isrunning = false
        }
    }
}
