'use strict';

var trackListHandling = (function (){
  var root = document.querySelector('.track-handling');
  var trackList = root.querySelector('.track-list');
  var actualTrack = root.querySelector('.actual-track');
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
      addActualTrack(trackData);
		});
		return li;
	}

  function addActualTrack(trackData){
    var actualTrackName = root.querySelector('p');
    var addTrList = root.querySelector('#add-to-playlist');
    actualTrackName.innerText = '';
    actualTrackName.innerText = trackData.artist + ' - ' + trackData.title;
    // addTrList.addEventListener('click' function(){
    //   ajax.addTrackList(trackData, function(){
    //
    //   });
    // });
  }


  return {
    loadAllTrack: loadAllTrack,
    // loadTrack: loadTrack
    // playTrack: playTrack,
  };
})();
// trackListHandling.playTrack();
