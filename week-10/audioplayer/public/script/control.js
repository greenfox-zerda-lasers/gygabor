'use strict';

var controlPanel = (function (){
  var playButton = document.querySelector('#play-pause');

  playButton.addEventListener('click', function(){
      playTrack('../mp3/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3');
  })

  function playTrack (url){
    audio.load(url);
    audio.play();
  }

  return {
    playTrack: playTrack,
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
