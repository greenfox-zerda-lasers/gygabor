// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

var cursorX;
var cursorY;

document.onmousemove = function(e){
    cursorX = e.pageX;
    cursorY = e.pageY;
}

function checkCursor(){
    console.log("Cursor at: " + cursorX + ", " + cursorY);
    setTimeout(checkCursor, 1500);
}

checkCursor()
