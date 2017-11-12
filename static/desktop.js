function displayInit(){
    width = window.innerWidth;

}

function getposition(){
    var posrequest = new XMLHttpRequest();
    posrequest.open("Get", "url/pos");
    var pos = posrequest.send();
    return pos;
}

function displayPos(pos){

}
