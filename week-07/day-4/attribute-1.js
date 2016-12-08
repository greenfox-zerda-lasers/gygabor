// Write the image's url to the console.
var image = document.querySelector('img');
console.log(image.getAttribute('src'));

// Replace the image with a picture of yourself.
image.setAttribute('src', 'http://www.monsterchildren.com/wp-content/uploads/2015/12/monster-children-lemmy-motorhead-256x256.png');

// Make the link point to the Green Fox Academy website.
var linkGreen = document.querySelector('a');
linkGreen.setAttribute('href', 'http://www.greenfoxacademy.com/');

// Disable the second button.
var secondButton = document.querySelector('.this-one');
secondButton.disabled = true;

// Replace its text with 'Don't click me!'.

var buttons = document.querySelectorAll('button');
if (buttons){
  buttons.forEach(function(butt){
    butt.innerText = 'Don\'t click me!'
  })
}
