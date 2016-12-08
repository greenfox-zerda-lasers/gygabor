// Does the third p have a cat class?
var paragraphs = document.querySelectorAll('p');

function isThirdCat(){
  if (paragraphs[2].getAttribute('class') === 'cat'){
    alertCat();
  }
}

isThirdCat()

// If so, alert 'YEAH CAT!'
function alertCat(){
  alert('YEAH CAT!');
}

// If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
function chngApple(){
  if (paragraphs[3].classList.contains('dolphin')){
    document.querySelector('.apple').innerText = 'pear';
  }
}
chngApple();

// If the first p has an 'apple' class, replace cat's content with 'dog'
function chngCat(){
  if (paragraphs[0].classList.contains('apple')){
    document.querySelector('.cat').innerText = 'dog'
  }
}
chngCat();

// Make apple red
var apple = document.querySelector('.apple');
apple.classList.add('red');

// Make balloon less balloon-like
var balloon = document.querySelector('.balloon');
balloon.setAttribute('style', 'background-color: red');
