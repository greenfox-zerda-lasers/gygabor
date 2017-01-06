'use strict';

var controlPanel = (function (){
  var playButton = document.querySelector('#play-pause');

  playButton.addEventListener('click', function(){
    playTrack()
  });

  function playTrack (){
    if (audio.paused()){
      playButton.style.background = 'url(img/pause.svg) no-repeat';
      playButton.style.backgroundPosition = 'center'
      audio.play();
    } else {
      playButton.style.background = 'url(img/play.svg) no-repeat';
      playButton.style.backgroundPosition = 'center'
      audio.pause();
    }
  }

  function loadTrack (url){
    audio.load(url);
    playTrack();
  };

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
