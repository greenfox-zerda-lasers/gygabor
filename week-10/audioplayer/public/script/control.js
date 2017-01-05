'use strict';

var controlPanel = (function (){
  var playButton = document.querySelector('#play-pause');

  playButton.addEventListener('click', function(){
    if (audio.paused()){
      playButton.style.background = 'url(img/pause.svg) no-repeat';
      playButton.style.backgroundPosition = 'center'
      audio.play();
    } else {
      playButton.style.background = 'url(img/play.svg) no-repeat';
      playButton.style.backgroundPosition = 'center'
      audio.pause();
    }
  })

  function loadTrack (url){
    audio.load(url);
  }

  return {
    loadTrack: loadTrack,
  }
})();
		// audio.play();
		// function logUpdate( time ){
		// 	console.log(time);
		// 	// slider should be updated here
		// }
		// audio.onUpdate( logUpdate );
		// audio.onComplete(function(){
		// 	console.log('READY');
		// });
		// setTimeout(function () {
		// 	// audio.seek(99);
		// 	// audio.pause()
		// }, 100);
