// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var asteroidList = document.getElementsByClassName('asteroids');
console.log(asteroidList)
function modifiList(){
  var king = asteroidList.getElementsByTagName('tagName')('li')[0];
  asteroidList.removeChild(king);
}

modifiList();
