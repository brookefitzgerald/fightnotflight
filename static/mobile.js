function initacc(){
    motionsensor = initDeviceMotionEvent();
}


function punch(){
    accel = motionsensor.acceleration();
    var points = 0;
    var thresh = 10;
    if (accel > thresh){
         points = accel / thresh;
    }
    return points;
}

function sendPunch(punchPoints){
    var punchNotify = new XMLHttpRequest();
    punchNotify.open("POST", "url/punch", );
    var punchsend = punchNotify.send(punchPoints);
}
