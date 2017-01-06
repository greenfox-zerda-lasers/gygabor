'use strict';

var trackListHandling = (function (){
  var root = document.querySelector('.track-handling');
  var trackList = root.querySelector('.track-list');
  // var actualTrack = root.querySelector('.actual-track');
  var tracks = []

  var ajax = new Ajax();


  function loadAllTrack(){
    ajax.getAllTracks(function(res){
      tracks = res;
      render()
    })
  }

  function render(){
    clearList()
    var trackId = 1;
    tracks.forEach(function(track){
      var li = _createPlaylistItem(trackId, track);
      trackList.appendChild(li);
      trackId++;
    });
  }

  function clearList (){
    var nodeList = root.querySelectorAll('li');
    nodeList.forEach(function(li){
      trackList.removeChild(li);
    });
  }

  function _createPlaylistItem(id, trackData) {
		var li = document.createElement('li');
		li.innerHTML = id +'. ' + trackData.artist + ' - ' + trackData.title;
		li.addEventListener('click', function(){
			var trackPath = '../mp3/'+trackData.fileName;
			controlPanel.loadTrack(trackPath);
		});
		return li;
	}

  // function playTrack (){
  //   trackList.forEach( function (track) {
  //   track.addEventListener('click', function (){
  //     controlPanel.loadTrack(track.dataset.src);
  //     })
  //   })
  // }

  // function addTrackPlayer(trackLink, trackName){
  //   audioPlayer.src = trackLink;
  //   audioPlayer.autoplay = 'true';
  //   addActualTrack(trackName);
  // }

  // function addActualTrack(trackName){
  //   var actualTrackName = document.createElement('p');
  //   actualTrackName.innerText = trackName;
  //   actualTrack.appendChild(actualTrackName);
  // }

  return {
    loadAllTrack: loadAllTrack,
    // loadTrack: loadTrack
    // playTrack: playTrack,
  };
})();
// trackListHandling.playTrack();
