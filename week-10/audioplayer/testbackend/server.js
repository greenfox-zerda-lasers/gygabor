'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var playlists = [
  {
    id: '01',
    name: 'All tracks'
  },
  {
    id: '02',
    name: 'Favorites'
  },
  {
    id: '03',
    name: 'Chill'
  },
  {
    id: '04',
    name: 'Electronic'
  }];

var tracks = [
  {
    id: '01',
    path: '/root/song01.mp3',
    playlist_id: ['01']
  },
  {
    id: '02',
    path: '/root/song02.mp3',
    playlist_id: ['01', '02']
  }
]

app.use(bodyParser.json());

app.get('/playlists', function (req, res) {
  res.json(playlists);
});

app.get('/bankinfo', function (req, res) {
  res.sendStatus(401);
});

app.post('/playlists', function (req, res) {
  playlists.push(req.body);
  res.json(playlists);
  // console.log(req.body);
});

app.delete('/playlists/:id', function (req, res) {
  function remaining(el) {
    return el.id != req.params.id;
  }
  playlists = playlists.filter(remaining);
  res.json(playlists);
})

app.get('/playlist-tracks', function (req, res) {
  res.json(tracks);
})

app.get('/playlist-tracks/:id', function (req, res) {
  var playlistIds = []
  playlists.forEach(function(e) {
    playlistIds.push(e.id);
  });
  // console.log(playlistIds);
  if (false === playlistIds.includes(req.params.id)) {
    res.sendStatus(404);
    console.log('ID does not exist');
  } else {
    function remaining(el) {
      return el.playlist_id.includes(req.params.id);
    }
    var temp = tracks.filter(remaining);
    // console.log(temp);
    res.json(temp);
  }
})

module.exports = app;
