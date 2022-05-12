package com.multicamp.mainapp.zerofiretab.tabLocation

import android.graphics.Color
import android.os.Bundle
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
import kotlinx.android.synthetic.main.activity_current_tab.*

class CurrentTab : Fragment() {
    private var chart: LineChart? = null
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {val view=inflater.inflate(R.layout.activity_current_tab,container,false)
        return view
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        chart = this.linechart
        val values = ArrayList<Entry>()
        for (i in 0..9) {
            val randval = (Math.random() * 40).toFloat()
            values.add(Entry(i.toFloat(), randval))
        }
        val set1: LineDataSet
        set1 = LineDataSet(values, "DataSet 1")
        val dataSets = ArrayList<ILineDataSet>()
        dataSets.add(set1)

        val data = LineData(dataSets)
        set1.color = Color.BLACK
        set1.setCircleColor(Color.BLACK)
        linechart.setData(data)
    }
}