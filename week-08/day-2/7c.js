// Based on the previous example create an array of images taken from flickr
// https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/

// Display a progress bar while the images are loading
// You can create your own or use the built in HTML5 version:
// https://developer.mozilla.org/en/docs/Web/HTML/Element/progress



var imgLink = ['https://c7.staticflickr.com/8/7022/26823638062_0c8af9f8cc_b.jpg', 'https://c7.staticflickr.com/8/7799/26683911430_c4662bf0ec_b.jpg', 'https://c2.staticflickr.com/9/8574/16635664865_9f5e9e2918_b.jpg'];
var images = [];
var prgbar = document.querySelector('progress');
prgbar.max = imgLink.length

imgLink.forEach(function(imgLink){
  var picture = document.createElement('img');
  picture.src = imgLink;
  images.push(picture);
});

function progressBar(value){
  prgbar.value += value;
}

images.forEach(function(image){
  image.addEventListener('load', function(){
    document.body.appendChild(image);
    progressBar(1);
  });
});
