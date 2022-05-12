package com.multicamp.mainapp.zerofiretab.tabLocation

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.multicamp.mainapp.R
import kotlinx.android.synthetic.main.activity_current_tab.*

class CurrentTab : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val currentview = inflater.inflate(R.layout.activity_current_tab, container, false)
        return currentview
    }
}