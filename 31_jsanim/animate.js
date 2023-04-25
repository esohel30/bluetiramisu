var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = canvas.getContext("2d");

ctx.fillStyle = "#0000ff";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

var radius = 0;
var growing  = true;


let drawCirc = function(e) {
    let x = e.offsetX;
    let y = e.offsetY;
    ctx.fillStyle = "#0000ff";
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fill();
  }


  var drawDot = (e) => {
    clear();
    requestID = window.requestAnimationFrame(drawDot);
    drawCirc(e);
    if (growing == true) {
        radius++;
    } else {
        radius--;
    }
    if (radius == 100) {
        growing = false;
        radius--;
    }
    if (radius == 0) {
        growing = true;
        radius++;
    }
};



var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener("click",drawDot);
stopButton.addEventListener("click", stopIt) ;



  