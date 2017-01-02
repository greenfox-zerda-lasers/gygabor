// var mp3Folder = './mp3/';
// var fs = require('fs');
// fs.readdir(testFolder, (err, files) => {
//   files.forEach(file => {
//     console.log(file);
//   });
// })

var trackListHandling = (function (){
  var trackList = document.querySelectorAll('.track-list');
var audioPlayer = document.querySelector('audio');

  function getTrack (){
    trackList.forEach( function (track) {
    track.addEventListener('click', function (){
      addTrackPlayer(track.dataset.src);
      })
    })
  }

  function addTrackPlayer(trackLink){
    audioPlayer.src = trackLink;
    audioPlayer.autoplay = 'true'
  }

  return {
    playTrack: getTrack,
  };
})();
trackListHandling.playTrack();
