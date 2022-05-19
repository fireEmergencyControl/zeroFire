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
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
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

class CurrentTab : Fragment(){
    var currentview: WebView?=null

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        val view=inflater.inflate(R.layout.activity_current_tab,container,false)
        currentview=view.findViewById(R.id.chartview)
        currentview?.setWebViewClient(WebViewClient())
        currentview?.setBackgroundColor(255)
        currentview?.settings?.loadWithOverviewMode=true
        currentview?.settings?.useWideViewPort=true
        currentview?.settings?.builtInZoomControls=true
        currentview?.settings?.javaScriptEnabled=true
        currentview?.settings?.javaScriptCanOpenWindowsAutomatically=false
        currentview?.settings?.allowFileAccess=true
        currentview!!.settings.cacheMode=WebSettings.LOAD_NO_CACHE
        currentview?.settings?.domStorageEnabled=true
        currentview?.settings?.allowContentAccess=true
        currentview!!.loadUrl("http://192.168.0.2:8000/index")
        return view
    }
}