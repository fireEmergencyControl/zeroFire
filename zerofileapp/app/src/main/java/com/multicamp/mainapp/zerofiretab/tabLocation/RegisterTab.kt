package com.multicamp.mainapp.zerofiretab.tabLocation

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.multicamp.mainapp.R
import com.multicamp.mainapp.zerofiretab.tabLocation.controldata.MyMqtt
import kotlinx.android.synthetic.main.activity_register_tab.*


/*class RegisterTab : Fragment(), View.OnClickListener {
    val sub_topic = "iot/#"
    val _topic = "iot:"
    val server_uri ="tcp://192.168.0.2:1883" //broker의 ip와 port
    var mymqtt : MyMqtt? = null
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        val view=inflater.inflate(R.layout.activity_register_tab, container, false)
        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)


    }

    override fun onClick(v: View?) {
        val NAME=registerNAME
        val ID=registerID
        val EMAIL=registerEMAIL
        val PLACE=workarea
        val CLASSES=registerClasses
        val PW=registerPW
        val PWC=registerPWcheck*/
/*
        if(v?.id==R.id.buttonRegister){
            fun data: Array<String> {
                data.add(NAME)
                data.append(ID)
                data.append(EMAIL)
                data.append(PLACE)
                data.append(CLASSES)
                data.append(PW)
                data.append(PWC)
            }

            mymqtt?.publish("iot/register", data)
        }
    }
}*/
