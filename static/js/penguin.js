var canvasWidth = 300;
var canvasHeight = 530;

var x=0;
var y=0;

var spriteWidth = 1500;
var spriteHeight = 530;

var rows = 1;
var cols = 5;

var trackRight = 0;
var trackLeft = 1;

var width = spriteWidth/cols;
var height = spriteHeight/rows;

var curFrame = 0;
var frameCount = 5;

var srcX;
var srcY=0;

var speed = 1;

var canvas = document.getElementById('canvas');
canvas.width = canvasWidth;
canvas.height = canvasHeight;
var ctx = canvas.getContext("2d");

var character = new Image();
character.src = "static/frazzledpenguin.png";

function updateFrame(){
    curFrame = ++curFrame % frameCount;
    srcX = curFrame * width;
    ctx.clearRect(0,0,width,height);
}

function draw(){
    updateFrame();
    ctx.drawImage(character,srcX,srcY,width,height,0,0,width,height);
}