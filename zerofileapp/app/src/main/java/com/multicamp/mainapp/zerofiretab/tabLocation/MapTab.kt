package com.multicamp.mainapp.zerofiretab.tabLocation

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import androidx.fragment.app.Fragment
import com.multicamp.mainapp.R
//import com.skt.Tmap.TMapView
import kotlinx.android.synthetic.main.activity_map_tab.*
import kotlinx.android.synthetic.main.activity_map_tab.view.*


/*class MapTab : Fragment() , View.OnClickListener{
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        val view=inflater.inflate(R.layout.activity_map_tab, container, false)

        val lltmapview:LinearLayout=view.findViewById(R.id.lltmapview)

        val tMapView = TMapView(activity)

        tMapView.setSKTMapApiKey("l7xx3e11578207e548d6ad10e40da3887e2a")
        lltmapview.addView(tMapView)

        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        lltmapview.setOnClickListener(this)

    }

    override fun onClick(v: View) {
        when(v.id){
            R.id.lltmapview -> {
                Log.d("test1", "click1!!!!!!!!!!!!!!")
            }
        }
    }

    /*tMapView.setOnClickListenerCallBack(new TMapView.OnClickListenerCallback() {
        @Override
        public boolean onPressEvent(ArrayList arrayList, ArrayList arrayList1, TMapPoint tMapPoint, PointF pointF) {
            //Toast.makeText(MapEvent.this, "onPress~!", Toast.LENGTH_SHORT).show();
            return false;
        }

        @Override
        public boolean onPressUpEvent(ArrayList arrayList, ArrayList arrayList1, TMapPoint tMapPoint, PointF pointF) {
            //Toast.makeText(MapEvent.this, "onPressUp~!", Toast.LENGTH_SHORT).show();
            return false;
        }
    });

// 롱 클릭 이벤트 설정
    tMapView.setOnLongClickListenerCallback(new TMapView.OnLongClickListenerCallback() {
        @Override
        public void onLongPressEvent(ArrayList arrayList, ArrayList arrayList1, TMapPoint tMapPoint) {
            //Toast.makeText(MapEvent.this, "onLongPress~!", Toast.LENGTH_SHORT).show();
        }
    });

// 지도 스크롤 종료
    tMapView.setOnDisableScrollWithZoomLevelListener(new TMapView.OnDisableScrollWithZoomLevelCallback() {
        @Override
        public void onDisableScrollWithZoomLevelEvent(float zoom, TMapPoint centerPoint) {
            Toast.makeText(MapEvent.this, "zoomLevel=" + zoom + "\nlon=" + centerPoint.getLongitude() + "\nlat=" + centerPoint.getLatitude(), Toast.LENGTH_SHORT).show();
        }
    });*/
}

*/