var h = 30
var t = 24
var d = 10

    $(function(){
    $('#t1').jqxGauge({
        width : 150, height : 150,
        min : -20,        max : 110,
        ranges : [ {
            startValue : -20, endValue : 0,    style : { fill : '#e2e2e2'}
        }, {
            startValue : 0, endValue : 25,
            style : {fill : '#00ccff'},
        }, {
            startValue : 26, endValue : 50,
            style : { fill : '#4cb848'},
        }, {
            startValue : 51,endValue : 75,
            style : {fill : '#fad00b'},
        }, {
            startValue : 76,endValue : 110,
            style : {fill : '#e53d37'},
        } ],
        labels : {position : 'outside'},
        animationDuration : 500,
        border : {visible : false},
        //caption : { value : "온도 : "+t+"°C"},
        caption : { value : "온도"},
        value : t
    });

	    $('#hu1').jqxGauge({
	        width : 150, height : 150,     min : 0,    max : 100,
	        border : {    visible : false},
	        //caption : {    value : "습도 : "+h+"%"},
	        caption : {    value : "습도"},
	        value : h
	    });
    });
