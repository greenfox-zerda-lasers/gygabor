'use strict';
// var mp3Folder = './mp3/';
// var fs = require('fs');
// fs.readdir(testFolder, (err, files) => {
//   files.forEach(file => {
//     console.log(file);
//   });
// })

var trackListHandling = (function (){
  var trackList = document.querySelectorAll('.track');
  var audioPlayer = document.querySelector('audio');
  var actualTrack = document.querySelector('.actual-track');


  function getTrack (){
    trackList.forEach( function (track) {
    track.addEventListener('click', function (){
      actualTrack.innerText = '';
      addTrackPlayer(track.dataset.src, track.innerText);
      })
    })
  }

  function addTrackPlayer(trackLink, trackName){
    audioPlayer.src = trackLink;
    audioPlayer.autoplay = 'true';
    addActualTrack(trackName);
  }

  function addActualTrack(trackName){
    var actualTrackName = document.createElement('p');
    actualTrackName.innerText = trackName;
    actualTrack.appendChild(actualTrackName);
  }

  return {
    playTrack: getTrack,
  };
})();
trackListHandling.playTrack();
