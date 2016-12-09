var currentImageNumber = 0;
var iconButton = document.querySelectorAll('.icon-button');
var container = document.querySelector('.container');
var navigationButtons = document.querySelector('.bottom-buttons');

navigationButtons.addEventListener('click', function(e){
  console.log(this.dataset.imageId);
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
    console.log(urlToDisplay)
    container.style.backgroundImage = urlToDisplay;

}

slide(currentImageNumber)
