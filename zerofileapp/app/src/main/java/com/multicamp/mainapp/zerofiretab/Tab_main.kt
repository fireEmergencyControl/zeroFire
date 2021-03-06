package com.multicamp.mainapp.zerofiretab

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.google.android.material.tabs.TabLayout
import com.multicamp.mainapp.MainActivity
import com.multicamp.mainapp.R
import com.multicamp.mainapp.zerofiretab.tabLocation.*
import kotlinx.android.synthetic.main.tab_main.*

class Tab_main : AppCompatActivity() {
    var view0=ControlTab()
    var view1=CurrentTab()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        getSupportActionBar()?.hide();
        setContentView(R.layout.tab_main)

        supportFragmentManager.beginTransaction().replace(R.id.layout1,view0).commit()

        tabs.addOnTabSelectedListener(object: TabLayout.OnTabSelectedListener{
            override fun onTabSelected(tab: TabLayout.Tab?) {
                val position=tab?.position
                var fragment: Fragment?=null
                when(position){
                    0-> fragment=view0
                    1-> fragment=view1
                }
                supportFragmentManager.beginTransaction().replace(R.id.layout1,fragment!!).commit()
            }

            override fun onTabUnselected(tab: TabLayout.Tab?) {

            }

            override fun onTabReselected(tab: TabLayout.Tab?) {

            }
        })
    }
}