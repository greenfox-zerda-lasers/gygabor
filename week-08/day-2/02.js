// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout
var clearSetTimeout = document.querySelector('.clear-button');
var alertTime;

function ale(){
  alert('I\'m delayed');
}

clearSetTimeout.addEventListener('click', function(){
  clearTimeout(alertTime);
});

alertTime = setTimeout(ale, 3000);
