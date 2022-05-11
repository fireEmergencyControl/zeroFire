package com.multicamp.mainapp

import android.graphics.Color
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.github.mikephil.charting.charts.LineChart
import com.github.mikephil.charting.data.Entry
import com.github.mikephil.charting.data.LineData
import com.github.mikephil.charting.data.LineDataSet
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*


/*class MainActivity : Fragment() {
    var chart: LineChart? = null
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(
            R.layout.activity_main,
            container,
            false
        )
        return view
    }
    val values = ArrayList<Entry>()
    override fun onInflate(context: Context, attrs: AttributeSet, savedInstanceState: Bundle?) {
        super.onInflate(context, attrs, savedInstanceState)
        for (i in 0..9) {
            val `val` = (Math.random() * 10).toFloat()
            values.add(Entry(i.toFloat(), `val`))
        }
        val set1: LineDataSet
        set1 = LineDataSet(values, "DataSet 1")
        val dataSets = ArrayList<ILineDataSet>()
        dataSets.add(set1) // add the data sets

// create a data object with the data sets
        val data = LineData(dataSets)
// black lines and points
        set1.color = Color.BLACK
        set1.setCircleColor(Color.BLACK)

// set data
        linechart.setData(data)
    }
}
*/


class MainActivity : AppCompatActivity() {
    private var chart: LineChart? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        chart = findViewById(R.id.linechart)
        val values = ArrayList<Entry>()
        for (i in 0..9) {
            val `val` = (Math.random() * 10).toFloat()
            values.add(Entry(i.toFloat(), `val`))
        }
        val set1: LineDataSet
        set1 = LineDataSet(values, "DataSet 1")
        val dataSets = ArrayList<ILineDataSet>()
        dataSets.add(set1) // add the data sets

        // create a data object with the data sets
        val data = LineData(dataSets)

        // black lines and points
        set1.color = Color.BLACK
        set1.setCircleColor(Color.BLACK)

        // set data
        linechart.setData(data)
    }
}