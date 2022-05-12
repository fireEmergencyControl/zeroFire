package com.multicamp.mainapp


import android.R
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment


class MainActivity:Fragment(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }
}


/*class MainActivity : Fragment() {
    private var chart: LineChart? = null
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {val view=inflater.inflate(R.layout.activity_main,container,false)
        return view
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        chart = this.linechart
        val values = ArrayList<Entry>()
        for (i in 0..9) {
            val randval = (Math.random() * 10).toFloat()
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
}*/

/*class LightFragment : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {val view: View = inflater.inflate(R.layout.fragment_light, container, false)
        val textView: TextView = view.findViewById(R.id.text_view)
        val joypadView: JoypadView = view.findViewById(R.id.joypad)
        joypadView.setListener(object : Listener() {
            fun onUp() {
                textView.setText(R.string.text_view_up)
            }

            fun onMove(distance: Float, dx: Float, dy: Float) {
                val wheelsPower: WheelsPower = WheelsPower.wheelsPower(distance, dx, dy)
                textView.text = getString(
                    R.string.text_view_move,
                    distance,
                    dx,
                    dy,
                    wheelsPower.getLeft(),
                    wheelsPower.getRight()
                )
            }
        })
        return view
    }
}*/