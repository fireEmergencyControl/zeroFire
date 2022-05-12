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
var host = "192.168.0.5";
var port = 9001;
var matt;
//callback함수 - 접속이 완료된 후 호출되는 함수
function onConnect(){
    console.log("접속완료");
    mqtt.subscribe("senser/#");
    // 웹페이지 접속하자마자 메시지 보내기
    message = new Paho.MQTT.Message("start");
    // topic 설정
    message.destinationName = "iot/web";
    // MQTT 메시지 보내기 - publish
    mqtt.send(message);
}
function onFailure(){
    console.log("접속실패");
}
//2. 메시지가 전송되면 호출될 콜백함수를 정의
function onMessageArrived(msg){

    document.getElementById("myimg").src = "data:image/jpeg;base64,"+btoa(String.fromCharCode.apply(null, msg.payloadBytes));
    let words = msg.payloadString.split(":");
    if(words=="fire") {
        var audio = new Audio();
        audio.src = "./static/audio/sound.mp3";
        audio.volume = 0.9;
        var promise = audio.play();
        if (promise !== undefined) {
            promise.then(_ => {
            // Autoplay started!
            }).catch(error => {
            // Autoplay was prevented.
            // Show a "Play" button so that user can start playback.
            });
        }
        console.log("오디오 실행");
        alert("화재가 발생했습니다.");
    }
    let tempHum = []
    let result = parseInt(words[1]);
    if(words[0]=="tempeature") {
        tempHum[0] = result;
    }
    if(words[0]=="humidity") {
        tempHum[1] = result;
    }
console.log( words[0] + ':' + result);
}
//publish 하는 함수 정의
function sendMsg(msg){    alert(msg);
    message = new Paho.MQTT.Message(msg);
    message.destinationName = "iot/led";
    mqtt.send(message);
}

//mqtt통신을 관리하기 위한 사용자정의 함수
function MQTTConnect(){
    console.log("접속완료" + host + "," + port);
    // mqtt 통신을 위한 클라이언트 객체 생성
    mqtt = new Paho.MQTT.Client(host, port, "javascript_client");
    // "javascript_client"는 클라이언트 id
    // mqtt 통신을 위해 필요한 설정을 명시
    var options = {
        timeout:3,
        onSuccess:onConnect,
        onFailure:onFailure,
    }
    // 3. 콜백함수등록
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.connect(options);
}
function ckFunc(){
    mychk = document.myform.led;
    chkVal = "";//체크되어 있는 항목의 문자열을 추가할 변수
    if(mychk.checked) {
        chkVal = "led_on";
    }else {
        chkVal = "led_off";
    }
    sendMsg(chkVal);
}
MQTTConnect();