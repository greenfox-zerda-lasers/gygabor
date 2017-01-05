'use strict';

var trackListHandling = (function (){
  var trackList = document.querySelectorAll('.track');
  // var audioPlayer = document.querySelector('audio');
  var actualTrack = document.querySelector('.actual-track');

  // function loadTrack(){
  //
  // }

  function playTrack (){
    trackList.forEach( function (track) {
    track.addEventListener('click', function (){
      controlPanel.playTrack(track.dataset.src);
      })
    })
  }

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
    // loadTrack: loadTrack
    playTrack: playTrack,
  };
})();
trackListHandling.playTrack();
