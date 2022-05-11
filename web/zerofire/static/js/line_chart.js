var host = "192.168.0.5";
var port = 9001;
var matt;
//callback함수 - 접속이 완료된 후 호출되는 함수
function onConnect(){
    console.log("접속완료");
    mqtt.subscribe("iot/#");
//        // 웹페이지 접속하자마자 메시지 보내기
//        message = new Paho.MQTT.Message("start");
//        // topic 설정
//        message.destinationName = "iot/web";
//        // MQTT 메시지 보내기 - publish
//        mqtt.send(message);
}
function onFailure(){
    console.log("접속실패");
}
//2. 메시지가 전송되면 호출될 콜백함수를 정의
function onMessageArrived(msg){
    var temp = [];
    var hum = [];

//        document.getElementById("myimg").src = "data:image/jpeg;base64,"+btoa(String.fromCharCode.apply(null, msg.payloadBytes));
    let words = msg.payloadString.split(":");
    let result = parseInt(words[1]);
    if(words[0]=="tempeature") {
        for(var i = 0; i < 10; i++) {
            temp[i] = result;
        }
    if(words[0]=="humidity") {
        for(var i = 0; i < 10; i++) {
            hum[i] = result;
        }
    }
    const labels = [
    '지금',
    '5초 전',
    '10초 전',
    '15초 전',
    '20초 전',
    '25초 전',
    '30초 전',
    '35초 전',
    '40초 전',
    '45초 전',
    '50초 전',
];

    const data = {
    labels: labels,
    datasets: [
        {
          label: '온도',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data : [temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]],
        }
    ]
    };

    const config = {
    type: 'line',
    data: data,
    options: {
        plugins: {
            title: {
                display: true,
                text: '지역 온도, 습도, 이산화탄소 농도'
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: '색상'
                }
            },
            y: {
                title: {
                    display: true,
                    text: '변곡량'
                }
            }
        },
    }
    };
    const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  const data2 = {
    labels: labels,
    datasets: [
        {
          label: '습도',
          backgroundColor: 'rgb(200, 99, 132)',
          borderColor: 'rgb(200, 99, 132)',
          data2 : [hum[1],hum[2],hum[3],hum[4],hum[5],hum[6],hum[7],hum[8],hum[9],hum[10]],
        }
    ]
    };
     const config2 = {
    type: 'line',
    data: data2,
    options: {
        plugins: {
            title: {
                display: true,
                text: '지역 온도, 습도, 이산화탄소 농도'
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: '색상'
                }
            },
            y: {
                title: {
                    display: true,
                    text: '변곡량'
                }
            }
        },
    }
    };
    const myChart2 = new Chart(
    document.getElementById('myChart2'),
    config2
  );
//        alert(temp);
//    alert([temp[1],temp[2],temp[3],temp[4],temp[5],temp[6]] );

//        alert([5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 75] )
    }
//    alert(temp)

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