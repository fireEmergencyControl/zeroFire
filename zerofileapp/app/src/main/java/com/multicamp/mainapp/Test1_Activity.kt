package com.multicamp.mainapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class Test1_Activity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        getSupportActionBar()?.hide();
        setContentView(R.layout.activity_test1_)
    }
}