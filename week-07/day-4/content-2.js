// fill every paragraph with the last one's content.
var lastPar = document.getElementsByClassName('dog');

var allPar = document.getElementsByTagName('p');

for (var i = 0; i < allPar.length; i++){
  allPar[i].innerHTML = lastPar[0].innerHTML
}
