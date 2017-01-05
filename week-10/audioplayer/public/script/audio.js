var audio = (function () {
	var audioNode = document.createElement('audio');
	// var timeCallback = function(){};
	// var endCallback = function(){};

	// audioNode.addEventListener('timeupdate', function(){
	// 	timeCallback(audioNode.currentTime / audioNode.duration * 100);
	// });
  //
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

	return {
		load: load,
		play: play,
		pause: pause,
    volume: volume,
    seek: seek,

		// seek: seek,
		// onUpdate: setUpdateEvent,
		// onComplete: setCompleteEvent
	}
})();
