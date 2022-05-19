var host = "172.30.1.21";
var port = 9001;
var mqtt;
temp=0;
hu=0;
function onConnect(){
    console.log("접속 완료");
    mqtt.subscribe("iot:HC_SR04");
    mqtt.subscribe("iot:humidity");
    mqtt.subscribe("iot:temperature");
    mqtt.subscribe("picamera:mycamera");
    mqtt.subscribe("alert:fire");
    message = new Paho.MQTT.Message("start");
    message.destinationName = "web" //토픽설정
    //mqtt메세지 보내기 - publish
    mqtt.send(message);
}
//callback 함수 - 접속이 실패된 후 호출되는 함수
function onFailure(){
    console.log("접속 실패")
    setTimeout(MQTTconnect,reconnectTimeout)
}
// 2. 메시지가 전송되면 호출될 콜백함수 정의
function onMessageArrived(msg){
    mytopic = msg.destinationName.split(":")
    console.log(msg.payloadBytes);

    if(mytopic[1]=="mycamera"){
    document.getElementById("myimg").src = "data:image/jpeg;base64,"+btoa(String.fromCharCode.apply(null,msg.payloadBytes))
    }

    if(mytopic[1]=="fire") {
//    alert("지역에서 불이 발생했습니다.");
    alert();
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
    }


     if(mytopic[1]=="humidity"){
     result = msg.payloadString.split(",")
     result[0] = parseInt(result[0]);
     result[1] = parseInt(result[1]);
     temp = result[0];
     hu = result[1];
     console.log("온습도:"+msg.payloadString);
     $ ( "#hu1" ) .jqxGauge ( 'setValue' , temp);
     $ ( "#t1" ) .jqxGauge ( 'setValue' , hu);
     let tem = "온도 : "+String(hu);
     let h = "습도 : "+String(temp);
     $("#hu").text(h);
     $("#temp").text(tem);
    }

     if(mytopic[1]=="temperature"){
     temp = parseInt(msg.payladString);
     console.log("온도:"+msg.payladString);
     console.log("temp:"+result[0]);
        var ctx = document.getElementById('myChart').getContext('2d');

    }
}
//publish하는 함수 정의
function sendMsg(msg){
    //alert(msg)
    /*
    1. message객체 생성하기
    2. 토픽을 설정
    3. send메소드 호출
    */
    message = new Paho.MQTT.Message(msg);
    message.destinationName = "iot/led" //토픽설정
    //mqtt메세지 보내기 - publish
    //data = "test:test"
    mqtt.send(message);
}
// mqtt통신을 관리하기 위한 사용자정의 함수
function MQTTConnect(){
    //console.log("mqtt접속"+host+","+port);
    //mqtt통신을 위한 클라이언트 객체 생성
    mqtt = new Paho.MQTT.Client(host,port,"javascript_client"); //"javascript_client"는 클라이언트 id(TOPIC아님)
    //mqtt통신을 위해 필요한 설정을 명시
    var options = {
        timeout:3,
        onSuccess:onConnect, //접속 성공 했을 때 실행될 콜백함수 등록
        onFailure:onFailure,
    }
    // 3. 메시지가 도착하면 실행될 콜백함수를 등록한다.
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.connect(options);
}

function alert(){
    Swal.fire('화재 발생!!')
}

 MQTTConnect();


