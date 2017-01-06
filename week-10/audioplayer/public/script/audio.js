var audio = (function () {
	var audioNode = document.createElement('audio');

	var timeCallback = function(position){
		var seekSlider = document.querySelector('input[type="range-seek"]');
			seekSlider.rangeSlider.update({value: position})
	};
	// var endCallback = function(){};

	audioNode.addEventListener('timeupdate', function(){
		timeCallback(audioNode.currentTime / audioNode.duration * 100);
	});

	// audioNode.addEventListener('ended', function(){
	// 	endCallback();
	// });
  //
	// function setUpdateEvent( cb ) {
	// 	timeCallback = cb;
	// }
  //
	// function setCompleteEvent( cb ) {
	// 	endCallback = cb;
	// }

	function load( url ) {
    audioNode.src = url;
    console.log(audioNode.src)
	}

	function play(){
		audioNode.play();
	}
  //
	function pause(){
		audioNode.pause();
	}

  function volume(value){
    audioNode.volume = value;
  }

	function seek( percent ){
		audioNode.currentTime = audioNode.duration * percent;
	}

  function isPaused() {
		return audioNode.paused;
	}

	return {
		load: load,
		play: play,
		pause: pause,
    volume: volume,
    seek: seek,
    paused: isPaused

		// seek: seek,
		// onUpdate: setUpdateEvent,
		// onComplete: setCompleteEvent
	}
})();
