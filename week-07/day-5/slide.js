var currentImageNumber = 0;
var iconButton = document.querySelectorAll('.icon-button');
var container = document.querySelector('.container');
var navigationButtons = document.querySelectorAll('.navbutton');

iconButton.forEach(function(element){
  element.addEventListener('click', function(){
    slide(this.dataset.imageId);
  });
});

navigationButtons.forEach(function(element){
  element.addEventListener('click', function(){
    var nextImageNumber = ''
    if (this.dataset.imageId === '-1'){
      nextImageNumber = parseInt(currentImageNumber) - 1
    } else {
      nextImageNumber = parseInt(currentImageNumber) + 1
    }
    if (nextImageNumber < 0){
      nextImageNumber = 4;
    } else if (nextImageNumber > 4){
      nextImageNumber = 0;
    }
    slide(nextImageNumber);
  });
});


function navButtonImage(){
  for (var i = 0; i < iconButton.length; i++){
    urlToDisplay = 'url("img/img' + i + '.jpg")';
    iconButton[i].style.backgroundImage = urlToDisplay;
  }
}

navButtonImage()

function slide(imageNumber){
    urlToDisplay = 'url("img/img' + imageNumber + '.jpg")';
    container.style.backgroundImage = urlToDisplay;
    currentImageNumber = imageNumber;
}

slide(currentImageNumber);
