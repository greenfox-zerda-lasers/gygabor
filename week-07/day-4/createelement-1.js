// Add an item that says 'The Green Fox' to the asteroid list.
var asteroidList = document.querySelector('.asteroids');

function addListElement(element){
  var newLi = document.createElement('li');
  newLi.innerText = element;

  asteroidList.appendChild(newLi);
}
addListElement('The Green Fox');

// Add an item that says 'The Lamplighter' to the asteroid list.
addListElement('The Lamplighter');

// Add a heading saying 'I can add elements to the DOM!' to the .container.

var newHeader = document.createElement('h1');

var headerText = document.createTextNode('I can add elements to the DOM!');

newHeader.appendChild(headerText);

document.body.insertBefore(newHeader, asteroidList);

// Add an image, any image, to the container.
var container = document.querySelector('.container');

var image = document.createElement('img');

image.src = 'http://punkrocker.org.uk/punkscene/johnnythunders77bio.jpg';

container.appendChild(image);
