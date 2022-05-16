var map;
// 페이지가 로딩이 된 후 호출하는 함수입니다.
function initTmap(){
    // map 생성
    // Tmap.map을 이용하여, 지도가 들어갈 div, 넓이, 높이를 설정합니다.
    map = new Tmapv2.Map("map_div", {
        center : new Tmapv2.LatLng(37.566481622437934, 126.98502302169841), // 지도 초기 좌표
        width : "100%", // map의 width 설정
        height : "400px" // map의 height 설정
    });
};

//경로안내 요청 함수
function getRP() {
    var s_latlng = new Tmapv2.LatLng (37.509442,127.055525);
    var e_latlng = new Tmapv2.LatLng (37.510048,127.054935);

    var optionObj = {
        reqCoordType:"WGS84GEO", //요청 좌표계 옵셥 설정입니다.
        resCoordType:"WGS84GEO",  //응답 좌표계 옵셥 설정입니다.
        trafficInfo:"Y"
    };

    var params = {
        onComplete:onComplete,
        onProgress:onProgress,
        onError:onError
    };

    // TData 객체 생성
    var tData = new Tmapv2.extension.TData();

    // TData 객체의 경로요청 함수
    tData.getRoutePlanJson(s_latlng, e_latlng, optionObj, params);
}

//경로안내
function onComplete() {
    console.log(this._responseData); //json으로 데이터를 받은 정보들을 콘솔창에서 확인할 수 있습니다.

    var jsonObject = new Tmapv2.extension.GeoJSON();
    var jsonForm = jsonObject.rpTrafficRead(this._responseData);

    //교통정보 표출시 생성되는 LineColor 입니다.
    var trafficColors = {

        // 사용자가 임의로 색상을 설정할 수 있습니다.
        // 교통정보 옵션 - 라인색상
        trafficDefaultColor:"#000000", //교통 정보가 없을 때
        trafficType1Color:"#009900", //원할
        trafficType2Color:"#7A8E0A", //서행
        trafficType3Color:"#8E8111",  //정체
        trafficType4Color:"#FF0000"  //정체
    };
    jsonObject.drawRouteByTraffic(map, jsonForm, trafficColors);
    map.setCenter(new Tmapv2.LatLng(37.509442,127.055525));
    map.setZoom(17);
}

//데이터 로드중 실행하는 함수입니다.
function onProgress(){

}

//데이터 로드 중 에러가 발생시 실행하는 함수입니다.
function onError(){
    alert("onError");
}