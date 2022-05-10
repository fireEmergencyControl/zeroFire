package com.multicamp.mainapp.fragment_test1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.viewpager.widget.PagerAdapter
import com.google.android.material.tabs.TabLayout
import com.multicamp.mainapp.R
import com.multicamp.mainapp.fragment_test1.tabLocation.*
import kotlinx.android.synthetic.main.tab_main.*

class Tab_main : AppCompatActivity() {
    var view1=LoginTab()
    var view2=RegisterTab()
    var view3=ControlTab()
    var view4=CurrentTab()
    var view5=MapTab()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        getSupportActionBar()?.hide();
        setContentView(R.layout.tab_main)

        supportFragmentManager.beginTransaction().replace(R.id.linear1,view1).commit()

        tabs.addOnTabSelectedListener(object: TabLayout.OnTabSelectedListener{
            override fun onTabSelected(tab: TabLayout.Tab?) {
                val position=tab?.position
                var fragment: Fragment?=null
                when(position){
                    0-> fragment=view1
                    1-> fragment=view2
                    2-> fragment=view3
                    3-> fragment=view4
                    4-> fragment=view5
                }
                supportFragmentManager.beginTransaction().replace(R.id.linear1,fragment!!).commit()
            }

            override fun onTabUnselected(tab: TabLayout.Tab?) {

            }

            override fun onTabReselected(tab: TabLayout.Tab?) {

            }
        })
    }
}