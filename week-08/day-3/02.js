var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC&limit=16')
xhr.send()
xhr.onreadystatechange = ready

function ready(rsp) {
	if( xhr.readyState === XMLHttpRequest.DONE ) {
		var imgData = JSON.parse(xhr.response);
    display(imgData.data);
	}
}

function display(imgList){
  imgList.forEach( function(picture){
    var gifUrl = picture.images.downsized_large.url;
    var button = document.createElement('button');
    button.style.background = 'url('+ picture.images.fixed_width_still.url +') no-repeat';
    button.style.cursor = 'pointer';
    button.style.backgroundSize = 'cover';
    var  navBar = document.querySelector('nav');
    navBar.appendChild(button);
    button.addEventListener('click', function(){
      displayGif(gifUrl);
    });
  });
}

var image = document.createElement('img');
var gifSection = document.querySelector('section');
gifSection.appendChild(image);

function displayGif(gifUrl){
  
  image.src = gifUrl;

}
